#!/usr/bin/env python3
import os
import hashlib
import shutil

# ---- RIPEMD160(SHA256) helper with fallback ----
def ripemd160_of_sha256_hex(sha256_hex: str) -> str:
    raw = bytes.fromhex(sha256_hex)
    try:
        h = hashlib.new("ripemd160")
        h.update(raw)
        return h.hexdigest()
    except (ValueError, TypeError):
        # Fallback to pycryptodome if available
        try:
            from Crypto.Hash import RIPEMD
        except ImportError as e:
            raise RuntimeError(
                "RIPEMD160 not available in hashlib and pycryptodome not installed. "
                "Install with: pip install pycryptodome"
            ) from e
        h = RIPEMD.new()
        h.update(raw)
        return h.hexdigest()

def sha256_file_stream(path, buf_size=1024*1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(buf_size), b""):
            h.update(chunk)
    return h.hexdigest()

# ---- Prompt for Directory ----
EVIDENCE_DIR = input("📁 Enter the full path to the evidence directory: ").strip()
EVIDENCE_DIR = os.path.abspath(os.path.expanduser(EVIDENCE_DIR))
FROZEN_DIR = os.path.join(EVIDENCE_DIR, "frozen_sources")
os.makedirs(FROZEN_DIR, exist_ok=True)

SKIP_EXTS = {".hash", ".2ha", ".ots"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}

total = 0
for filename in sorted(os.listdir(EVIDENCE_DIR)):
    full_path = os.path.join(EVIDENCE_DIR, filename)

    if not os.path.isfile(full_path):
        continue
    if filename in SKIP_NAMES:
        continue
    if any(filename.endswith(ext) for ext in SKIP_EXTS):
        continue
    if os.path.commonpath([full_path, FROZEN_DIR]) == FROZEN_DIR:
        continue  # safety: don’t process files inside frozen_sources

    try:
        print(f"\n🔎 Hashing: {filename}")

        # SHA256 (streamed)
        sha256_hex = sha256_file_stream(full_path)
        with open(full_path + ".hash", "w") as hf:
            hf.write(sha256_hex)
        print(f"[SHA256] → {sha256_hex[:12]}...")

        # RIPEMD160(SHA256)
        twoha_hex = ripemd160_of_sha256_hex(sha256_hex)
        with open(full_path + ".2ha", "w") as tf:
            tf.write(twoha_hex)
        print(f"[2HA] → {twoha_hex[:12]}...")

        # Copy original + hash files to frozen_sources/
        for ext in ["", ".hash", ".2ha"]:
            src = full_path + ext
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(FROZEN_DIR, os.path.basename(src)))

        total += 1

    except Exception as e:
        print(f"[❌] Failed on {filename}: {e}")

print(f"\n✅ Hashing complete. Total files processed: {total}")