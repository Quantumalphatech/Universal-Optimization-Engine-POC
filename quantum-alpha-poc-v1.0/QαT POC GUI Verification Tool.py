# -*- coding: utf-8 -*-
"""
QαT POC 公開驗證工具 V2.1（雙語 GUI + 詳細驗證輸出）
Quantum Alpha Technology Co., Ltd.

版本：V2.1 (2026-07-18)
更新重點：
- 恢復詳細的中英並列驗證說明文字（符合您偏好）
- 公鑰指紋顯示 + 完整內建/外部公鑰切換
- 動態 UI + 更好的錯誤處理
"""

import os
import sys
import json
import hashlib
import base64
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path

try:
    from cryptography.hazmat.primitives.serialization import load_pem_public_key
    from cryptography.exceptions import InvalidSignature
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False

# ==================== 內建公鑰 ====================
EMBEDDED_PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAHpruI48y7gop+3vqK7tcLgsmKYSRs9TjlF/HQiluv1A=
-----END PUBLIC KEY-----
"""
# =================================================

VERSION = "V2.1 (2026-07-18)"

# ========================= 雙語字串 =========================
LANG = {
    "zh": {
        "title": "QαT POC 公開驗證工具 V2.1",
        "subtitle": "SHA-256 完整性 + Ed25519 真偽驗證",
        "lang_btn": "English",
        "bin_file": "解檔 (.bin)",
        "use_embedded": "使用內建公鑰（推薦）",
        "pub_file": "外部公鑰檔案 (.pem)",
        "signature": "Ed25519 簽章 (Base64)",
        "sha256": "預期 SHA-256（可選）",
        "browse": "瀏覽…",
        "load_json": "從 JSON 載入",
        "verify": "開始驗證",
        "clear": "清除結果",
        "result": "驗證結果",
        "need_crypto": "請先安裝 cryptography：\npip install cryptography",
        "missing_bin": "請選擇 solution_*.bin 檔案",
        "embedded_not_set": "內建公鑰尚未設定！",
        "pubkey_not_selected": "請選擇外部公鑰檔案",
        "invalid_sig": "簽章 Base64 格式不正確",
        "sha_ok": "✅ SHA-256 一致（內容完整）",
        "sha_fail": "❌ SHA-256 不一致（檔案可能被竄改）",
        "sha_skip": "⏭ 未提供預期 SHA-256，僅顯示實際計算值",
        "sha_computed": "實際 SHA-256：",
        "ed_ok": "✅ Ed25519 驗簽通過（真偽與完整性成立）",
        "ed_fail": "❌ Ed25519 驗簽失敗（偽造、公鑰不符或檔案被改）",
        "ed_err": "❌ 驗簽過程錯誤：",
        "done_ok": "全部檢查通過！此結果可公開驗證。",
        "done_fail": "存在未通過項目，請檢查。",
        "company": "Quantum Alpha Technology Co., Ltd. | 私鑰僅由本公司持有",
        "hint": "建議：先按「從 JSON 載入」→ 確認公鑰設定 → 按「開始驗證」",
        "using_embedded": "使用【內建公鑰】進行驗證 / Verify using the built-in public key.",
        "using_external": "使用【外部公鑰】進行驗證 / Verify using external public key.",
        "fingerprint": "公鑰指紋",
    },
    "en": {
        "title": "QαT POC Public Verifier V2.1",
        "subtitle": "SHA-256 Integrity + Ed25519 Authenticity",
        "lang_btn": "中文",
        "bin_file": "Solution file (.bin)",
        "use_embedded": "Use embedded public key (recommended)",
        "pub_file": "External public key file (.pem)",
        "signature": "Ed25519 signature (Base64)",
        "sha256": "Expected SHA-256 (optional)",
        "browse": "Browse…",
        "load_json": "Load from JSON",
        "verify": "Verify",
        "clear": "Clear result",
        "result": "Result",
        "need_crypto": "Please install cryptography:\npip install cryptography",
        "missing_bin": "Please select a solution_*.bin file",
        "embedded_not_set": "Embedded public key is not set!",
        "pubkey_not_selected": "Please select external public key file",
        "invalid_sig": "Invalid signature Base64 format",
        "sha_ok": "✅ SHA-256 match (integrity OK)",
        "sha_fail": "❌ SHA-256 mismatch (file may be altered)",
        "sha_skip": "⏭ No expected SHA-256; showing computed value only",
        "sha_computed": "Computed SHA-256: ",
        "ed_ok": "✅ Ed25519 signature valid (authentic & intact)",
        "ed_fail": "❌ Ed25519 verification failed",
        "ed_err": "❌ Verification error: ",
        "done_ok": "All checks passed! This result is publicly verifiable.",
        "done_fail": "One or more checks failed.",
        "company": "Quantum Alpha Technology Co., Ltd. | Private key held only by the company",
        "hint": "Recommended: Load JSON first → Confirm key → Click Verify",
        "using_embedded": "Using embedded public key / 使用內建公鑰進行驗證",
        "using_external": "Using external public key / 使用外部公鑰進行驗證",
        "fingerprint": "Key Fingerprint",
    },
}


class QATVerifyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.lang = "zh"
        self.root.title(LANG["zh"]["title"])
        self.root.geometry("860x730")
        self.root.minsize(760, 630)

        self.var_bin = tk.StringVar()
        self.var_pub = tk.StringVar()
        self.var_sig = tk.StringVar()
        self.var_sha = tk.StringVar()
        self.var_use_embedded = tk.BooleanVar(value=True)

        self._build_ui()
        self._apply_lang()
        self._on_embedded_toggle()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 5}

        # 標題
        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, **pad)
        self.lbl_title = ttk.Label(top, font=("Segoe UI", 14, "bold"))
        self.lbl_title.pack(side=tk.LEFT)
        self.btn_lang = ttk.Button(top, width=10, command=self._toggle_lang)
        self.btn_lang.pack(side=tk.RIGHT)

        self.lbl_sub = ttk.Label(self.root, foreground="#555")
        self.lbl_sub.pack(anchor=tk.W, padx=10, pady=2)

        # 輸入區
        frm = ttk.LabelFrame(self.root, text="")
        frm.pack(fill=tk.X, padx=10, pady=8)

        # .bin
        self.lbl_bin = ttk.Label(frm)
        self.lbl_bin.grid(row=0, column=0, sticky=tk.W, padx=6, pady=4)
        ttk.Entry(frm, textvariable=self.var_bin, width=70).grid(row=0, column=1, sticky=tk.EW, padx=4)
        self.btn_bin = ttk.Button(frm, text="", command=self._browse_bin)
        self.btn_bin.grid(row=0, column=2, padx=4)

        # 內建公鑰
        self.chk_embedded = ttk.Checkbutton(
            frm, variable=self.var_use_embedded, command=self._on_embedded_toggle
        )
        self.chk_embedded.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx=6, pady=6)

        # 外部公鑰
        self.lbl_pub = ttk.Label(frm)
        self.lbl_pub.grid(row=2, column=0, sticky=tk.W, padx=6, pady=4)
        ttk.Entry(frm, textvariable=self.var_pub, width=70).grid(row=2, column=1, sticky=tk.EW, padx=4)
        self.btn_pub = ttk.Button(frm, text="", command=self._browse_pub)
        self.btn_pub.grid(row=2, column=2, padx=4)

        # signature
        self.lbl_sig = ttk.Label(frm)
        self.lbl_sig.grid(row=3, column=0, sticky=tk.W, padx=6, pady=4)
        ttk.Entry(frm, textvariable=self.var_sig, width=70).grid(row=3, column=1, sticky=tk.EW, padx=4)

        # sha256
        self.lbl_sha = ttk.Label(frm)
        self.lbl_sha.grid(row=4, column=0, sticky=tk.W, padx=6, pady=4)
        ttk.Entry(frm, textvariable=self.var_sha, width=70).grid(row=4, column=1, sticky=tk.EW, padx=4)

        frm.columnconfigure(1, weight=1)

        # 按鈕列
        bar = ttk.Frame(self.root)
        bar.pack(fill=tk.X, padx=10, pady=6)
        self.btn_json = ttk.Button(bar, command=self._load_json)
        self.btn_json.pack(side=tk.LEFT, padx=4)
        self.btn_verify = ttk.Button(bar, command=self._verify)
        self.btn_verify.pack(side=tk.LEFT, padx=4)
        self.btn_clear = ttk.Button(bar, command=self._clear)
        self.btn_clear.pack(side=tk.LEFT, padx=4)

        self.lbl_hint = ttk.Label(self.root, foreground="#666", wraplength=820)
        self.lbl_hint.pack(anchor=tk.W, padx=12, pady=4)

        # 結果區
        self.lbl_result = ttk.Label(self.root)
        self.lbl_result.pack(anchor=tk.W, padx=10)
        self.txt = scrolledtext.ScrolledText(self.root, height=22, font=("Consolas", 10), wrap=tk.WORD)
        self.txt.pack(fill=tk.BOTH, expand=True, padx=10, pady=6)

        self.lbl_company = ttk.Label(self.root, foreground="#888")
        self.lbl_company.pack(pady=4)

    def _on_embedded_toggle(self):
        enabled = not self.var_use_embedded.get()
        state = "normal" if enabled else "disabled"
        self.lbl_pub.config(state=state)
        self.btn_pub.config(state=state)
        if not enabled:
            self.var_pub.set("")

    def _t(self, key):
        return LANG[self.lang][key]

    def _apply_lang(self):
        t = self._t
        self.root.title(t("title"))
        self.lbl_title.config(text=f"{t('title')} {VERSION}")
        self.lbl_sub.config(text=t("subtitle"))
        self.btn_lang.config(text=t("lang_btn"))
        self.lbl_bin.config(text=t("bin_file"))
        self.chk_embedded.config(text=t("use_embedded"))
        self.lbl_pub.config(text=t("pub_file"))
        self.lbl_sig.config(text=t("signature"))
        self.lbl_sha.config(text=t("sha256"))
        self.btn_bin.config(text=t("browse"))
        self.btn_pub.config(text=t("browse"))
        self.btn_json.config(text=t("load_json"))
        self.btn_verify.config(text=t("verify"))
        self.btn_clear.config(text=t("clear"))
        self.lbl_result.config(text=t("result"))
        self.lbl_hint.config(text=t("hint"))
        self.lbl_company.config(text=t("company"))

    def _toggle_lang(self):
        self.lang = "en" if self.lang == "zh" else "zh"
        self._apply_lang()

    def _browse_bin(self):
        p = filedialog.askopenfilename(title=self._t("bin_file"),
                                       filetypes=[("BIN", "*.bin"), ("All", "*.*")])
        if p:
            self.var_bin.set(p)

    def _browse_pub(self):
        p = filedialog.askopenfilename(title=self._t("pub_file"),
                                       filetypes=[("PEM", "*.pem"), ("All", "*.*")])
        if p:
            self.var_pub.set(p)

    def _load_json(self):
        p = filedialog.askopenfilename(title="JSON", filetypes=[("JSON", "*.json"), ("All", "*.*")])
        if not p:
            return
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            messagebox.showerror(self._t("result"), f"JSON 讀取失敗 / Load failed: {e}")
            return

        if data.get("signature"):
            self.var_sig.set(data["signature"].strip())
        if data.get("sha256_hash"):
            self.var_sha.set(data["sha256_hash"].strip())

        bin_name = data.get("solution_bin_file") or data.get("signed_artifact")
        if bin_name:
            candidate = Path(p).parent / bin_name
            if candidate.is_file():
                self.var_bin.set(str(candidate))

        self._log(f"[JSON] 已載入：{os.path.basename(p)} / Loaded successfully")

    def _log(self, msg: str):
        self.txt.insert(tk.END, msg + "\n")
        self.txt.see(tk.END)

    def _clear(self):
        self.txt.delete("1.0", tk.END)

    def _sha256_file(self, path: str) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()

    def _get_pubkey_bytes(self):
        if self.var_use_embedded.get():
            if not EMBEDDED_PUBLIC_KEY_PEM.strip() or "BEGIN PUBLIC KEY" not in EMBEDDED_PUBLIC_KEY_PEM:
                raise ValueError(self._t("embedded_not_set"))
            self._log(self._t("using_embedded"))
            return EMBEDDED_PUBLIC_KEY_PEM.encode("utf-8")
        else:
            pub_path = self.var_pub.get().strip()
            if not pub_path or not os.path.isfile(pub_path):
                raise ValueError(self._t("pubkey_not_selected"))
            self._log(self._t("using_external"))
            with open(pub_path, "rb") as f:
                return f.read()

    def _verify(self):
        self._clear()
        t = self._t

        if not HAS_CRYPTO:
            messagebox.showerror(t("result"), t("need_crypto"))
            return

        bin_path = self.var_bin.get().strip()
        if not bin_path or not os.path.isfile(bin_path):
            messagebox.showwarning(t("result"), t("missing_bin"))
            return

        # 取得公鑰並顯示指紋
        try:
            pub_key_bytes = self._get_pubkey_bytes()
            fp = base64.b64encode(hashlib.sha256(pub_key_bytes).digest()[:8]).decode()[:12]
            self._log(f"{t('fingerprint')}: {fp}...")
        except Exception as e:
            messagebox.showerror(t("result"), str(e))
            return

        all_ok = True

        # SHA-256
        try:
            got = self._sha256_file(bin_path)
            self._log(t("sha_computed") + got)
            exp = self.var_sha.get().strip()
            if exp:
                if got.lower() == exp.lower():
                    self._log(t("sha_ok"))
                else:
                    self._log(t("sha_fail"))
                    all_ok = False
            else:
                self._log(t("sha_skip"))
        except Exception as e:
            self._log(f"SHA-256 計算錯誤: {e}")
            all_ok = False

        self._log("")

        # Ed25519
        try:
            sig_b64 = self.var_sig.get().strip()
            if not sig_b64:
                raise ValueError("缺少簽章 / Missing signature")
            signature = base64.b64decode(sig_b64)
            public_key = load_pem_public_key(pub_key_bytes)
            with open(bin_path, "rb") as f:
                data = f.read()
            public_key.verify(signature, data)
            self._log(t("ed_ok"))
        except base64.binascii.Error:
            self._log(t("invalid_sig"))
            all_ok = False
        except InvalidSignature:
            self._log(t("ed_fail"))
            all_ok = False
        except Exception as e:
            self._log(t("ed_err") + str(e))
            all_ok = False

        self._log("\n" + "=" * 55)
        if all_ok:
            self._log(t("done_ok"))
            messagebox.showinfo(t("result"), t("done_ok"))
        else:
            self._log(t("done_fail"))
            messagebox.showwarning(t("result"), t("done_fail"))

        self._log(t("company"))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    if not HAS_CRYPTO:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("缺少套件", "請先執行：pip install cryptography")
        sys.exit(1)
    QATVerifyGUI().run()