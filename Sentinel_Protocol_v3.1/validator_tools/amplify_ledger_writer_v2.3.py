import os
import json
import hashlib
import requests
from datetime import datetime
from pathlib import Path

# === INTRO ===
print("\U0001f512 AMPLIFY_LEDGER Writer v2.3 – Sentinel Protocol v3.1")

# === PROMPTS ===
audit_log_path = input("📄 Enter full path to the audit log `.json` file: ").strip()
session_log_path = input("📄 Enter full path to the corresponding session log `.json` file: ").strip()
txid = input("🔗 Enter Bitcoin TXID: ").strip()

# === HASH + 2ha + OTS FILENAME: SESSION LOG ===
with open(session_log_path, "rb") as f:
    session_bytes = f.read()
sha256_session = hashlib.sha256(session_bytes).hexdigest()
session_2ha_path = session_log_path.replace(".json", ".2ha")
ots_session_path = session_log_path.replace(".json", ".hash.ots")
if not os.path.exists(session_2ha_path):
    raise FileNotFoundError(f"❌ .2ha not found: {session_2ha_path}")
if not os.path.exists(ots_session_path):
    raise FileNotFoundError(f"❌ .ots file not found: {ots_session_path}")
with open(session_2ha_path, "r") as f:
    ripemd160_session = f.read().strip()

# === HASH + 2ha + OTS FILENAME: AUDIT LOG ===
with open(audit_log_path, "rb") as f:
    audit_bytes = f.read()
sha256_audit = hashlib.sha256(audit_bytes).hexdigest()
audit_2ha_path = audit_log_path.replace(".json", ".2ha")
ots_audit_path = audit_log_path.replace(".json", ".hash.ots")
if not os.path.exists(audit_2ha_path):
    raise FileNotFoundError(f"❌ .2ha not found: {audit_2ha_path}")
if not os.path.exists(ots_audit_path):
    raise FileNotFoundError(f"❌ .ots file not found: {ots_audit_path}")
with open(audit_2ha_path, "r") as f:
    ripemd160_audit = f.read().strip()

# === BLOCK HEIGHT ===
def fetch_block_height(txid):
    try:
        url = f"https://mempool.space/api/tx/{txid}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("status", {}).get("block_height")
    except Exception as e:
        print(f"[!] Could not fetch block height: {e}")
        return None

block_height = fetch_block_height(txid)

# === META_ID ===
meta_id = Path(session_log_path).stem.replace("session_log_", "").split("_")[0]
timestamp = datetime.utcnow().isoformat() + "Z"

# === LEDGER OBJECT ===
entry = {
    "meta_id": meta_id,
    "anchored_file": {
        "session_log": os.path.basename(session_log_path),
        "sha256": sha256_session,
        "2ha": ripemd160_session,
        "ots": os.path.basename(ots_session_path)
    },
    "confirmation_log": {
        "audit_log": os.path.basename(audit_log_path),
        "sha256": sha256_audit,
        "2ha": ripemd160_audit,
        "ots": os.path.basename(ots_audit_path)
    },
    "op_return": {
        "txid": txid,
        "block_height": block_height,
        "payload": f"SENTINEL|{meta_id}|{ripemd160_session}"
    },
    "validated_by": "VALIS_v2.4",
    "status": "anchored",
    "timestamp": timestamp
}

# === WRITE LEDGER ===
LEDGER_ROOT = Path("ledger_registry")
LEDGER_ROOT.mkdir(exist_ok=True)
ledger_path = LEDGER_ROOT / f"AMPLIFY_LEDGER_{meta_id}.json"

if ledger_path.exists():
    with open(ledger_path, "r") as f:
        existing = json.load(f)
    existing["audits"].append(entry)
else:
    existing = {
        "meta_id": meta_id,
        "audits": [entry]
    }

with open(ledger_path, "w") as f:
    json.dump(existing, f, indent=4)

print(f"[✅] AMPLIFY LEDGER updated: {ledger_path}")
