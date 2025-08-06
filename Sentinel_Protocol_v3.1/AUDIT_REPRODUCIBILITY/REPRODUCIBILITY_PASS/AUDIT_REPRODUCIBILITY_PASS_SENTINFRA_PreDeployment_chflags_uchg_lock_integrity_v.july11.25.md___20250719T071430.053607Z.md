# AUDIT_REPRODUCIBILITY_PASS_SENTINFRA_PreDeployment_chflags_uchg_lock_integrity_v.july11.25.md

**Auditor:** Luba Levina-Telles
**Document Version:** v1.0      
**Protocol:** Sentinel Protocol v3.1 ABSOLUTE MODE
**System:**  AI-Human Synergy™
**Audit Type:** REPRODUCIBILITY    
**Status:** PASS  
**Audit ID:** AUDIT_REPRODUCIBILITY_PASS_SENTINFRA_PreDeployment_chflags_uchg_lock_integrity_v.july11.25.md
**Audit Date:** July 11, 2025 
**Claim Class:** [Protocol | Credential | Infrastructure]   
**Linked Files:**  
Audit records listed individually below.
**Verification Method:** `chflags` + `uchg` with /frozen executed under `auditlogger.py` `session_logger.py` and `batch_dualhasher.py`
**Outcome:**   
- ✅ Local immutability of source `.json` files confirmed under `auditlogger.py`
- ✅ Local immutability of source `.json` files confirmed under `session_logger.py` 
- ✅ Local immutability of source files confirmed under `batch_dualhasher.py` for multiple source formats `.json` `.md` `.csv` `.py` `.pdf` `.png` `.pptx` `.xlsx` `.docx`  
- 🔒 Audit trail `chmod 444` and `chflags uchg` built-in protections functional


---

## 🧪 Test Criteria

| Test # | Action (Operator-Level)                      | Expected Behavior                                                                                                                                  |
|--------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1️⃣     | Double-click file to open (e.g. in TextEdit) | ✅ File opens in read-only mode                                                                                                                     | 
| 2️⃣     | Attempt to copy contents (Cmd+A, Cmd+C)      | ✅ Contents can be copied                                                                                                                           |
| 3️⃣     | Attempt to edit contents and save            | ❌ Save is **blocked** or prompts warning (eg. Failed to save '<filename>': File is read-only. Select 'Overwrite' to attempt to make it writeable.) | 
| 4️⃣     | Attempt to overwrite warning                 | ❌ Forced to create **new or sudo file** (eg. Failed to save '<filename>': File is read-only. Select 'Overwrite as Sudo' to retry as superuser.)    | 

### ✅ PASS CONDITION:
- File **cannot be edited or saved over** by default GUI tools  
- **Reproducibility (`.hash`, `.2ha`) remains valid** after non-destructive viewing or copying  
**Purpose:** Prevent accidental audit trail tampering via GUI tools (e.g., TextEdit, Finder)
> Files are locally protected by `chmod 444` + `chflags uchg`, which prevents accidental editing and overwrites via GUI tools or non-privileged user actions. However, this is not cryptographic immutability, macOS allows locked files to be moved to Trash via GUI after a warning prompt. True reproducibility is enforced by dual-hash verification (`sha256` + `ripemd160`) and timestamp anchoring (`.ots`, OP_RETURN, ordinal). These layers together form Sentinel’s audit chain.

---

## /OPTIMISATION02/auditlogger.py_July09.25  
**Location:** `<path>/frozen_sources/`  
**Filename Convention:** `audit_log_<meta_id>_<timestamp>.json` 
**Lock Protocol:** `chmod 444` + `chflags uchg`

### Audit Record
**Filename:** `audit_log_OPTMZ2-SR001_20250709T023343.365390Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record

**Filename:** `audit_log_OPTMZ2-SR008_20250709T025024.085862Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record

**Filename:** `audit_log_OPTMZ2-SR009_20250709T053527.591402Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

## /OPTIMISATION02/batch_dualhasher.py_July11.25
**Location:** `<path>/frozen_files/`  
**Filename Convention:** `<source file name>` 
**Lock Protocol:** `chmod 444` + `chflags uchg`

### Audit Record

**Filename:** `ADD JACC CVI REVIEWER ROLE.pdf`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`


---

### Audit Record
**Filename:** `anchor_log_MVP1-SR033_20250620T012012.872478Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `batch_dualhasher.py`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `C0.9_Execution_AIThread_Protocol.md`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `C5.2.7_RetrievalIntegrityMetrics_v.july11.25.md`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `C5.7_CredentialAudit_Doctrine_v1.0.md`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `DeepAudit_CSV001_HumanAudit_LLM3LLM4_titles_and_abstracts_001_Combined.csv`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `Final_Figures_supplement.pptx`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `Final_Tables.xlsx`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `Final_TelleMA_manuscript_word.docx`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `Screenshot 2025-07-11 at 10.41.03 am.png`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

## /OPTIMISATION02/session_logger.py_July11.25
**Location:** `<path>/frozen_sources/`  
**Filename Convention:** `session_log_<meta_id>_<timestamp>.json` 
**Lock Protocol:** `chmod 444` + `chflags uchg`

### Audit Record
**Filename:** `session_log_OPTMZ-SESS001_20250709T023626.543281Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `session_log_OPTMZ-SESS005_20250709T025037.058926Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---

### Audit Record
**Filename:** `session_log_OPTMZ-SESS009_20250709T053543.889521Z.json`
**File opens in read-only mode:** `Confirmed`
**Contents can be copied:** `Confirmed`
**Attempt to edit contents and save:** `Unable`
**Attempt to overwrite warning:**  `Unable`

---