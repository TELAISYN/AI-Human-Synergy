import os
import csv

print("📁 Enter full path to directory containing `.hash` and `.2ha` files:")
folder_path = input(">>> ").strip()

if not os.path.isdir(folder_path):
    raise FileNotFoundError(f"❌ Directory does not exist: {folder_path}")

output_rows = []
for file in os.listdir(folder_path):
    if file.endswith(".hash"):
        base = file[:-5]
        hash_path = os.path.join(folder_path, f"{base}.hash")
        twoha_path = os.path.join(folder_path, f"{base}.2ha")

        try:
            with open(hash_path, "r") as hf:
                sha256 = hf.read().strip()
        except Exception:
            sha256 = "ERROR"

        try:
            with open(twoha_path, "r") as tf:
                ripemd160 = tf.read().strip()
        except Exception:
            ripemd160 = "MISSING"

        output_rows.append([base, sha256, ripemd160])

# Print to terminal
print("\n✅ Extracted Hash Summary:\n")
print(f"{'Filename':<60} {'SHA256':<64} {'RIPEMD160'}")
print("-" * 140)
for row in output_rows:
    print(f"{row[0]:<60} {row[1]:<64} {row[2]}")

# Optional CSV export
output_csv = os.path.join(folder_path, "hash_audit_report.csv")
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Filename", "SHA256", "RIPEMD160"])
    writer.writerows(output_rows)

print(f"\n📄 Exported summary to: {output_csv}")