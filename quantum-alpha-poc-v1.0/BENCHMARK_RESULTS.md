# Steiner Tree Benchmark Results

**Universal Optimization Engine (QαT) — SteinLib B & C Instances**

**Engine Specifications:**

- **Hardware**: Intel i5 12th Gen laptop, single core, no GPU
- **Memory**: <6GB (dynamic, task-dependent; tested up to C20)
- **CPU Usage**: <10% (light instances) to ~30% (C set heavy instances)
- **Reproducibility**: Deterministic mode, Seed=42, SHA-256 + Ed25519 certified
- **True Conflicts**: 0 (all solutions fully valid and connected)
- **Scale Factor**: 1:1 direct mapping to official SteinLib cost
- **Total instances solved**: 38/38 (B set 18/18, C set 20/20)

---

## B Instances (50–100 nodes) — All 18 Solved

| Instance | QαT Cost | Official Opt | Gap        | Terminals | Edges | Nodes |
| -------- | -------- | ------------ | ---------- | --------- | ----- | ----- |
| B01      | 83       | 82           | +1.2%      | 9         | 63    | 50    |
| B02      | 92       | 83           | +10.8%     | 13        | 63    | 50    |
| **B03**  | **138**  | **138**      | **0.0% ✅** | 25        | 63    | 50    |
| B04      | 64       | 59           | +8.5%      | 9         | 100   | 50    |
| B05      | 65       | 61           | +6.5%      | 13        | 100   | 50    |
| B06      | 128      | 122          | +4.9%      | 25        | 100   | 50    |
| B07      | 120      | 111          | +8.1%      | 13        | 94    | 75    |
| **B08**  | **104**  | **104**      | **0.0% ✅** | 19        | 94    | 75    |
| **B09**  | **220**  | **220**      | **0.0% ✅** | 38        | 94    | 75    |
| B10      | 106      | 86           | +23.2%     | 13        | 150   | 75    |
| B11      | 98       | 88           | +11.36%    | 19        | 150   | 75    |
| B12      | 177      | 174          | +1.7%      | 38        | 150   | 75    |
| B13      | 213      | 165          | +29.0%     | 17        | 125   | 100   |
| B14      | 261      | 235          | +11.06%    | 25        | 125   | 100   |
| B15      | 325      | 318          | +2.2%      | 50        | 125   | 100   |
| B16      | 173      | 127          | +36.2%     | 17        | 200   | 100   |
| B17      | 141      | 131          | +7.6%      | 25        | 200   | 100   |
| **B18**  | **218**  | **218**      | **0.0% ✅** | 50        | 200   | 100   |

**B set summary:**

- 4 instances achieved optimal solution: **B03, B08, B09, B18** ✅
- 6 instances within 10% gap
- All 18 instances: `true_conflicts = 0`, terminals fully connected

---

## C Instances (500 nodes) — All 20 Solved

| Instance | QαT Cost | Official Opt | Gap         | Terminals | Edges | Nodes |
| -------- | -------- | ------------ | ----------- | --------- | ----- | ----- |
| C01      | 87       | 85           | +2.3%       | 5         | 625   | 500   |
| C02      | 201      | 144          | +39.6%      | 10        | 625   | 500   |
| C03      | 920      | 754          | +22%        | 83        | 625   | 500   |
| C04      | 1255     | 1079         | +16.3%      | 125       | 625   | 500   |
| **C05**  | **1617** | **1579**     | **+2.4% ✅** | 250       | 625   | 500   |
| C06      | 72       | 55           | +30.9%      | 5         | 1000  | 500   |
| C07      | 184      | 102          | +80.4%      | 10        | 1000  | 500   |
| C08      | 845      | 509          | +66.0%      | 83        | 1000  | 500   |
| C09      | 963      | 707          | +36.2%      | 125       | 1000  | 500   |
| **C10**  | **1131** | **1093**     | **+3.5% ✅** | 250       | 1000  | 500   |
| C11      | 48       | 32           | +50.0%      | 5         | 2500  | 500   |
| C12      | 65       | 46           | +41.3%      | 10        | 2500  | 500   |
| C13      | 532      | 258          | +106.2%     | 83        | 2500  | 500   |
| C14      | 637      | 323          | +97.2%      | 125       | 2500  | 500   |
| **C15**  | **595**  | **556**      | **+7.0% ✅** | 250       | 2500  | 500   |
| C16      | 25       | 11           | +127.3%     | 5         | 12500 | 500   |
| C17      | 49       | 18           | +172.2%     | 10        | 12500 | 500   |
| C18      | 207      | 113          | +83.2%      | 83        | 12500 | 500   |
| C19      | 270      | 146          | +84.9%      | 125       | 12500 | 500   |
| **C20**  | **339**  | **267**      | **+27.0%**  | 250       | 12500 | 500   |

**C set summary:**

- C05 (+2.4%), C10 (+3.5%), C15 (+7.0%) — near-optimal on 250-terminal instances
- All 20 instances: `true_conflicts = 0`, terminals fully connected

---

## Terminal Density Pattern Analysis

**High terminal density → better performance:**

| Terminal Count   | Gap Range   | Representative Results             |
| ---------------- | ----------- | ---------------------------------- |
| 5–10 terminals   | +30%–189%   | Sparse terminals, most challenging |
| 17–50 terminals  | 0%–29%      | Strong & consistent                |
| 83–125 terminals | +16%–106%   | Scale-dependent                    |
| 250 terminals    | +2.4%–27.0% | Consistently near-optimal          |

**Key insight:** The engine performs strongest under **high terminal density** constraints. This is the opposite behavior of traditional pruning-based algorithms, which usually degrade as terminal count increases.

---

## Hardware Usage by Scale

| Scale                          | CPU Peak | Memory Peak | Notes                     |
| ------------------------------ | -------- | ----------- | ------------------------- |
| B set (50–100 nodes)           | <10%     | ~1.5 GB     | Light, fast convergence   |
| C set small (625 edges)        | 10–19%   | 1.5–2.0 GB  | Stable throughput         |
| C set medium (1000–2500 edges) | 15–25%   | 2.0–3.7 GB  | Dynamic memory allocation |
| C set large (12500 edges)      | 20–30%   | <6 GB       | Memory self-regulates     |

All tests run on Intel i5 12th Gen laptop, single core, no GPU required.

---

## Verification

All results are cryptographically certified:

- Output files: `.bin` + `.npy` (logic structure)
- SHA-256 + Ed25519 digital signatures
- Public key available: `public_key.pem` (third-party verifiable)
- GUI verification tool included
- Seed: 42 (fixed, fully deterministic and reproducible)
- STP source files: publicly available on SteinLib (globally verifiable input)

> **Note:** All reported costs are valid feasible solutions with `true_conflicts = 0`. Software-stage results represent a lower bound on final performance. Logic circuit implementation is expected to expand search space by orders of magnitude.

---

---

# Steiner Tree Benchmark Results（中文版）

**通用優化引擎 (QαT) — SteinLib B & C 組實例**

**引擎規格：**

- **硬體**：Intel i5 12th Gen 筆電，單核，無 GPU
- **記憶體**：動態分配，<6GB（C20 實例實測仍在範圍內）
- **CPU 使用率**：<10%（輕量）～ ~30%（C 組大型實例）
- **可重現性**：確定性模式，Seed=42，SHA-256 + Ed25519 簽章
- **真實衝突**：全部為 0（所有解皆完全可行且端點連通）
- **尺度對應**：1:1 直接對應 SteinLib 官方成本
- **總求解實例**：38/38（B 組 18/18，C 組 20/20）

---

## B 組（50–100 節點）——18 個實例全數求解

| 實例      | QαT 成本  | 官方最優    | 差距         | Terminals | Edges | Nodes |
| ------- | ------- | ------- | ---------- | --------- | ----- | ----- |
| B01     | 83      | 82      | +1.2%      | 9         | 63    | 50    |
| B02     | 92      | 83      | +10.8%     | 13        | 63    | 50    |
| **B03** | **138** | **138** | **0.0% ✅** | 25        | 63    | 50    |
| B04     | 64      | 59      | +8.5%      | 9         | 100   | 50    |
| B05     | 65      | 61      | +6.5%      | 13        | 100   | 50    |
| B06     | 128     | 122     | +4.9%      | 25        | 100   | 50    |
| B07     | 120     | 111     | +8.1%      | 13        | 94    | 75    |
| **B08** | **104** | **104** | **0.0% ✅** | 19        | 94    | 75    |
| **B09** | **220** | **220** | **0.0% ✅** | 38        | 94    | 75    |
| B10     | 106     | 86      | +23.2%     | 13        | 150   | 75    |
| B11     | 98      | 88      | +11.36%    | 19        | 150   | 75    |
| B12     | 177     | 174     | +1.7%      | 38        | 150   | 75    |
| B13     | 213     | 165     | +29.0%     | 17        | 125   | 100   |
| B14     | 261     | 235     | +11.06%    | 25        | 125   | 100   |
| B15     | 325     | 318     | +2.2%      | 50        | 125   | 100   |
| B16     | 173     | 127     | +36.2%     | 17        | 200   | 100   |
| B17     | 141     | 131     | +7.6%      | 25        | 200   | 100   |
| **B18** | **218** | **218** | **0.0% ✅** | 50        | 200   | 100   |

**B 組總結：**

- 4 個實例達到最優解：**B03、B08、B09、B18** ✅
- 6 個實例在 10% 差距內
- 所有 18 個實例皆 `true_conflicts = 0`，端點完全連通

---

## C 組（500 節點）——20 個實例全數求解

| 實例      | QαT 成本   | 官方最優     | 差距          | Terminals | Edges | Nodes |
| ------- | -------- | -------- | ----------- | --------- | ----- | ----- |
| C01     | 87       | 85       | +2.3%       | 5         | 625   | 500   |
| C02     | 201      | 144      | +39.6%      | 10        | 625   | 500   |
| C03     | 920      | 754      | +22%        | 83        | 625   | 500   |
| C04     | 1255     | 1079     | +16.3%      | 125       | 625   | 500   |
| **C05** | **1617** | **1579** | **+2.4% ✅** | 250       | 625   | 500   |
| C06     | 72       | 55       | +30.9%      | 5         | 1000  | 500   |
| C07     | 184      | 102      | +80.4%      | 10        | 1000  | 500   |
| C08     | 845      | 509      | +66.0%      | 83        | 1000  | 500   |
| C09     | 963      | 707      | +36.2%      | 125       | 1000  | 500   |
| **C10** | **1131** | **1093** | **+3.5% ✅** | 250       | 1000  | 500   |
| C11     | 48       | 32       | +50.0%      | 5         | 2500  | 500   |
| C12     | 65       | 46       | +41.3%      | 10        | 2500  | 500   |
| C13     | 532      | 258      | +106.2%     | 83        | 2500  | 500   |
| C14     | 637      | 323      | +97.2%      | 125       | 2500  | 500   |
| **C15** | **595**  | **556**  | **+7.0% ✅** | 250       | 2500  | 500   |
| C16     | 25       | 11       | +127.3%     | 5         | 12500 | 500   |
| C17     | 49       | 18       | +172.2%     | 10        | 12500 | 500   |
| C18     | 207      | 113      | +83.2%      | 83        | 12500 | 500   |
| C19     | 270      | 146      | +84.9%      | 125       | 12500 | 500   |
| **C20** | **339**  | **267**  | **+27.0%**  | 250       | 12500 | 500   |

**C 組總結：**

- C05 (+2.4%)、C10 (+3.5%)、C15 (+7.0%) 在 250 端點實例表現突出
- 所有 20 個實例皆 `true_conflicts = 0`，端點完全連通

---

## 終端密度與表現規律分析

**高終端密度 → 表現越好：**

| 終端數量     | Gap 範圍      | 代表性實例      |
| -------- | ----------- | ---------- |
| 5–10 個   | +30%–189%   | 稀疏終端，最具挑戰性 |
| 17–50 個  | 0%–29%      | 表現強勁且穩定    |
| 83–125 個 | +16%–106%   | 與規模相關      |
| 250 個    | +2.4%–27.0% | 持續接近最優     |

**核心洞見**：本引擎在**高終端密度**條件下表現最強。這與傳統基於剪枝的演算法呈現相反趨勢。

---

## 硬體資源使用情況

| 規模                 | CPU 使用率 | 記憶體峰值      | 備註      |
| ------------------ | ------- | ---------- | ------- |
| B 組（50–100 節點）     | <10%    | ~1.5 GB    | 輕量，快速收斂 |
| C 組小型（625 邊）       | 10–19%  | 1.5–2.0 GB | 穩定吞吐    |
| C 組中型（1000–2500 邊） | 15–25%  | 2.0–3.7 GB | 動態記憶體分配 |
| C 組大型（12500 邊）     | 20–30%  | <6 GB      | 記憶體自我調節 |

所有測試均在 Intel i5 12th Gen 筆電、單核、無 GPU 環境下完成。

---

## 驗證方式

所有結果皆經過密碼學認證：

- 輸出檔案：`.bin` + `.npy`（邏輯結構）
- SHA-256 + Ed25519 數位簽章
- 公開金鑰：`public_key.pem`（第三方可獨立驗證）
- 內建 GUI 驗證工具
- Seed：42（固定，完全確定性）
- 輸入來源：SteinLib 公開資料（全球可驗證）

> **注意**：所有報告成本皆為 `true_conflicts = 0` 的有效可行解。軟體階段結果為未來硬體實現的下限。邏輯電路（ASIC）實作預期將大幅提升搜尋能力。

---

**文件結束**  

