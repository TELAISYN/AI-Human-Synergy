# ✅ Validator Reproducibility Troubleshooting Checklist  

**Title:** Validator Reproducibility Troubleshooting Checklist\
**Protocol:** Sentinel Protocol\
**Version:** v3.1\
**System:** AI-Human Synergy™\
**Commander:** Dr. Fernando Telles\
**Date Finalized:** 08 August 2025\
**Status:** Internal
**Purpose:** Ensure byte-perfect `.2ha` (RIPEMD160(SHA256)) reproducibility for Sentinel Protocol Ordinals

---

## ⚙️ Recommended Environment Settings

### ✅ VS Code Settings (Windows/macOS)
- **Disable automatic line ending conversion**
    - Open `Settings` → search: `End of Line`
    - Set to: `LF` (Unix) — DO NOT use `CRLF` (Windows)
    - Alternatively, set in bottom-right corner (click → select `LF`)
- **Disable Auto Save Triggers**
    - `"files.autoSave": "off"`
- **Ensure UTF-8 Encoding**
    - `"files.encoding": "utf8"`  
    - `"files.autoGuessEncoding": false`

### ✅ File Save Format
- **Save as:** Plain UTF-8 `.md` or `.pdf`
- **Use Only:** VS Code, Sublime Text, or `nano`  
- **Avoid:** Microsoft Word, Notepad, Google Docs exports

---

## 🧪 Canonical Hashing Steps (Local)

1. **Download original file from source repo**
2. **Do NOT open in Word/Notepad** — use `VS Code`, `Sublime`, or `cat` to preview
3. **Run canonical hash sequence:**
    ```bash
    openssl sha256 filename.md
    echo -n "<SHA256>" | xxd -r -p | openssl ripemd160
    ```
4. **Match the RIPEMD160 output to `.2ha` or Ordinal payload**

---

## 🧯 Known Pitfalls

| ❌ Issue | ⚠️ Cause | ✅ Fix |
|--------|--------|--------|
| `RIPEMD160 mismatch` | Line endings (CRLF) | Set to `LF` |
| `Different hashes on different OS` | File contains invisible BOM | Re-save using UTF-8 no BOM |
| `Validator hash differs from Commander` | Copy-paste added newline or whitespace | Use original file only |
| `SHA256 matches but RIPEMD160 doesn't` | File corrupted during edit | Re-download, use clean editor |

---

## 🔐 Validation Format (OP_RETURN payload)
```text
<Validator_ID>-<Audit_meta_ID>|PASS|RIPEMD160(SHA256[validated_audit.md])


---

## 🔎 Troubleshooting Contact

For validation mismatch support:
📧 Dr. Fernando Telles – Dr.Telles@aihumansynergy.org
🔗 https://www.aihumansynergy.org

---

“Even a 1-byte difference is a violation.
The chain starts before validation – not after.”
— Sentinel Protocol v3.1

---
