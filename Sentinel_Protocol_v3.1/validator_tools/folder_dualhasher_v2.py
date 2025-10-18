#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sentinel Protocol v4 — folder_dualhasher_v2.py
Performs deterministic dual-hash (SHA-256 + RIPEMD-160) computation over all files in a given folder.
Now includes user-prompted directory input and enhanced error handling.
"""

import os
import hashlib
from Crypto.Hash import RIPEMD

def folder_dual_hash(folder_path: str) -> str:
    """Compute combined RIPEMD160(SHA256) hash of all files within a folder (sorted by name)."""
    hashes = []

    for root, _, files in os.walk(folder_path):
        for name in sorted(files):
            path = os.path.join(root, name)
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                sha256 = hashlib.sha256(data).hexdigest()
                hashes.append(sha256)
            except (OSError, IOError) as e:
                print(f"⚠️  [Warning] Could not read file: {path} ({e})")

    if not hashes:
        raise ValueError("No files were hashed. Verify that the directory is not empty or inaccessible.")

    joined = ''.join(hashes).encode()
    ripemd = RIPEMD.new()
    ripemd.update(joined)
    return ripemd.hexdigest()

def main():
    print("\n🔒 Sentinel Protocol v4 — Folder Dual Hasher (v2)")
    print("---------------------------------------------------")

    folder_path = input("Enter folder path to hash (or drag folder here): ").strip()

    # Handle quoted paths (macOS Finder drag often includes quotes)
    if folder_path.startswith('"') and folder_path.endswith('"'):
        folder_path = folder_path[1:-1]

    if not folder_path or not os.path.isdir(folder_path):
        print("❌ Invalid path. Please ensure the directory exists and try again.")
        return

    print(f"\n📂 Target directory: {folder_path}\n")
    print("⏳ Computing dual hash...")

    try:
        result = folder_dual_hash(folder_path)
        print(f"\n✅ Dual RIPEMD160(SHA256) folder hash:\n{result}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()