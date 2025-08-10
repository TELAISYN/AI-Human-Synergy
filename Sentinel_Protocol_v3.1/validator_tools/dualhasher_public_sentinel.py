import os
import hashlib
import shutil

# === Prompt for Directory ===
EVIDENCE_DIR = input("📁 Enter the full path to the evidence directory: ").strip()
EVIDENCE_DIR = os.path.abspath(os.path.expanduser(EVIDENCE_DIR))
FROZEN_DIR = os.path.join(EVIDENCE_DIR, "frozen_sources")
os.makedirs(FROZEN_DIR, exist_ok=True)

# === Batch Hasher Loop ===
total = 0
for filename in sorted(os.listdir(EVIDENCE_DIR)):
    full_path = os.path.join(EVIDENCE_DIR, filename)

    if not os.path.isfile(full_path):
        continue
    if filename.endswith((".hash", ".2ha", ".ots")) or "frozen_sources" in full_path:
        continue

    try:
        print(f"\n🔎 Hashing: {filename}")
        with open(full_path, "rb") as f:
            file_bytes = f.read()

        # SHA256
        sha256_digest = hashlib.sha256(file_bytes).digest()
        sha256_hex = sha256_digest.hex()
        hash_path = full_path + ".hash"
        with open(hash_path, "w") as hf:
            hf.write(sha256_hex)
        print(f"[SHA256] → {sha256_hex[:12]}...")

        # RIPEMD160 of SHA256
        ripemd160 = hashlib.new("ripemd160")
        ripemd160.update(sha256_digest)
        ripemd160_hex = ripemd160.hexdigest()
        twoha_path = full_path + ".2ha"
        with open(twoha_path, "w") as tf:
            tf.write(ripemd160_hex)
        print(f"[2HA] → {ripemd160_hex[:12]}...")

        # Copy original + hash files to frozen_sources/
        for ext in ["", ".hash", ".2ha"]:
            source_file = full_path + ext
            if os.path.exists(source_file):
                shutil.copy2(source_file, os.path.join(FROZEN_DIR, os.path.basename(source_file)))

        total += 1

    except Exception as e:
        print(f"[❌] Failed on {filename}: {e}")

# === Final Report
print(f"\n✅ Hashing complete. Total files processed: {total}")