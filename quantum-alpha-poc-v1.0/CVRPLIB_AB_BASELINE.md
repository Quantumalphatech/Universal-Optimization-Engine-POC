# CVRPLIB A & B Series: Universal-Core Baseline Validation

**50 instances (27 A-series + 23 B-series) | N = 30–79 | K = 5–10**

- **Engine**: QαT Universal Optimization Engine (POC v1.1.1)
- **Problem**: Capacitated Vehicle Routing Problem (CVRP)
- **Environment**: Deterministic single-thread CPU, Seed = 42
- **Verification**: SHA-256 integrity + Ed25519 signature (`qat-poc-ed25519-v1`)

> **Disclaimer**: This document records POC baseline performance. It is not a comparison with commercial VRP solvers, and it is not an official optimality or official feasibility certificate.

---

## Feasibility as used in this report

1. **`true_conflicts = 0`**: vehicle count is at least the theoretical lower bound \(\lceil \sum d_i / Q \rceil\). Per-route loads, missed customers, and official integer-distance audits were **not** independently certified.
2. **`customers_served`**: counted from encoding length, not an independent service proof.
3. **Distance**: decoder Euclidean floats; official UB is CVRPLIB integer distance. **Gaps are indicative only.**

---

## Architecture

Shared search core **plus VRP-specific decode and neighborhoods** (including 2-opt and Relocate). The same core is used on Steiner Tree, Bin Packing, and other tasks, with different objectives and decoders.

---

## A Series — 27 Instances

| Instance      | N   | K   | Cap. util.* | Official UB | POC distance | Gap vs UB  | Time   |
|:------------- |:---:|:---:|:-----------:|:-----------:|:------------:|:----------:|:------:|
| **A-n32-k5**  | 31  | 5   | 82.00%      | 784         | **900.28**   | +14.83%    | 184.9s |
| **A-n33-k5**  | 32  | 5   | 89.20%      | 661         | **796.82**   | +20.55%    | 130.3s |
| **A-n33-k6**  | 32  | 6   | 90.17%      | 742         | **791.32**   | **+6.65%** | 102.1s |
| **A-n34-k5**  | 33  | 5   | 92.00%      | 778         | **893.88**   | +14.89%    | 110.7s |
| **A-n36-k5**  | 35  | 5   | 88.40%      | 799         | **895.22**   | +12.04%    | 118.3s |
| **A-n37-k5**  | 36  | 5   | 81.40%      | 669         | **827.95**   | +23.76%    | 252.5s |
| **A-n37-k6**  | 36  | 6   | 95.00%      | 949         | **1082.02**  | +14.02%    | 109.7s |
| **A-n38-k5**  | 37  | 5   | 96.20%      | 730         | **806.45**   | +10.47%    | 125.3s |
| **A-n39-k5**  | 38  | 5   | 95.00%      | 822         | **985.42**   | +19.88%    | 191.1s |
| **A-n39-k6**  | 38  | 6   | 87.67%      | 831         | **1040.65**  | +25.23%    | 125.5s |
| **A-n44-k6**  | 43  | 6   | 95.00%      | 937         | **1124.69**  | +20.03%    | 138.8s |
| **A-n45-k6**  | 44  | 6   | 98.83%      | 944         | **1207.99**  | +27.96%    | 184.4s |
| **A-n45-k7**  | 44  | 7   | 90.57%      | 1146        | **1328.77**  | +15.95%    | 192.0s |
| **A-n46-k7**  | 45  | 7   | 86.14%      | 914         | **1078.99**  | +18.05%    | 140.6s |
| **A-n48-k7**  | 47  | 7   | 89.43%      | 1073        | **1298.43**  | +21.01%    | 148.9s |
| **A-n53-k7**  | 52  | 7   | 94.86%      | 1010        | **1356.53**  | +34.31%    | 217.2s |
| **A-n54-k7**  | 53  | 7   | 95.57%      | 1167        | **1493.76**  | +28.00%    | 182.6s |
| **A-n55-k9**  | 54  | 9   | 93.22%      | 1073        | **1535.68**  | +43.12%    | 157.8s |
| **A-n60-k9**  | 59  | 9   | 92.11%      | 1354        | **1739.94**  | +28.50%    | 184.5s |
| **A-n61-k9**  | 60  | 9   | 98.33%      | 1034        | **1532.64**  | +48.22%    | 191.3s |
| **A-n62-k8**  | 61  | 8   | 91.63%      | 1288        | **1764.78**  | +37.02%    | 393.7s |
| **A-n63-k9**  | 62  | 9   | 97.00%      | 1616        | **2131.78**  | +31.92%    | 191.9s |
| **A-n63-k10** | 62  | 10  | 93.20%      | 1314        | **1836.56**  | +39.77%    | 221.1s |
| **A-n64-k9**  | 63  | 9   | 94.22%      | 1401        | **1833.80**  | +30.89%    | 209.2s |
| **A-n65-k9**  | 64  | 9   | 97.44%      | 1174        | **1709.73**  | +45.63%    | 200.8s |
| **A-n69-k9**  | 68  | 9   | 93.89%      | 1159        | **1797.21**  | +55.07%    | 313.3s |
| **A-n80-k10** | 79  | 10  | 94.20%      | 1763        | **2445.31**  | +38.70%    | 377.8s |

\*Capacity util. = instance total demand / (K×Q), not the fill rate of this solution.

**A-series summary**: 27/27 meet this engine’s feasibility rule. Tightest gap vs UB: **A-n33-k6 (+6.65%)**. Mean gap ≈ 26.9%.

---

## B Series — 23 Instances

| Instance      | N   | K   | Cap. util.* | Official UB | POC distance | Gap vs UB  | Time   |
|:------------- |:---:|:---:|:-----------:|:-----------:|:------------:|:----------:|:------:|
| **B-n31-k5**  | 30  | 5   | 82.40%      | 672         | **702.89**   | +4.60%     | 106.7s |
| **B-n34-k5**  | 33  | 5   | 91.40%      | 788         | **797.16**   | **+1.16%** | 125.1s |
| **B-n35-k5**  | 34  | 5   | 87.40%      | 955         | **1059.14**  | +10.91%    | 110.1s |
| **B-n38-k6**  | 37  | 6   | 85.33%      | 805         | **893.68**   | +11.02%    | 124.3s |
| **B-n39-k5**  | 38  | 5   | 88.00%      | 549         | **732.56**   | +33.43%    | 143.1s |
| **B-n41-k6**  | 40  | 6   | 94.50%      | 829         | **1015.08**  | +22.45%    | 117.9s |
| **B-n43-k6**  | 42  | 6   | 86.83%      | 742         | **902.71**   | +21.66%    | 140.9s |
| **B-n44-k7**  | 43  | 7   | 91.57%      | 909         | **1061.42**  | +16.77%    | 124.4s |
| **B-n45-k5**  | 44  | 5   | 97.20%      | 751         | **825.17**   | +9.88%     | 177.0s |
| **B-n45-k6**  | 44  | 6   | 98.67%      | 678         | **834.43**   | +23.07%    | 328.3s |
| **B-n50-k7**  | 49  | 7   | 87.00%      | 741         | **1104.66**  | +49.08%    | 264.0s |
| **B-n50-k8**  | 49  | 8   | 91.88%      | 1312        | **1556.22**  | +18.61%    | 153.5s |
| **B-n51-k7**  | 50  | 7   | 97.71%      | 1032        | **1474.34**  | +42.86%    | 262.0s |
| **B-n52-k7**  | 51  | 7   | 86.57%      | 747         | **1162.63**  | +55.64%    | 304.0s |
| **B-n56-k7**  | 55  | 7   | 88.00%      | 707         | **1073.18**  | +51.79%    | 214.0s |
| **B-n57-k7**  | 56  | 7   | 99.57%      | 1153        | **1541.76**  | +33.72%    | 339.7s |
| **B-n57-k9**  | 56  | 9   | 89.22%      | 1598        | **2001.65**  | +25.26%    | 248.8s |
| **B-n63-k10** | 62  | 10  | 92.20%      | 1496        | **2111.16**  | +41.12%    | 188.6s |
| **B-n64-k9**  | 63  | 9   | 97.56%      | 861         | **1326.03**  | +54.01%    | 211.4s |
| **B-n66-k9**  | 65  | 9   | 95.67%      | 1316        | **1695.10**  | +28.81%    | 260.1s |
| **B-n67-k10** | 66  | 10  | 90.70%      | 1032        | **1695.60**  | +64.30%    | 212.2s |
| **B-n68-k9**  | 67  | 9   | 93.00%      | 1272        | **1762.66**  | +38.57%    | 246.9s |
| **B-n78-k10** | 77  | 10  | 93.70%      | 1221        | **1898.28**  | +55.47%    | 349.8s |

\*Capacity util. = instance total demand / (K×Q), not the fill rate of this solution.

**B-series summary**: 23/23 meet this engine’s feasibility rule. Tightest gap vs UB: **B-n34-k5 (+1.16%)**. Mean gap ≈ 32.2%.

---

## Combined view (all 50 instances)

| Gap range   | Count | Share | Note                                              |
|:-----------:|:-----:|:-----:|:------------------------------------------------- |
| **< 5%**    | 2     | 4.0%  | A few small instances near the UB (e.g. B-n34-k5) |
| **5%–15%**  | 8     | 16.0% | Acceptable on small–medium instances              |
| **15%–35%** | 24    | 48.0% | Most instances fall here                          |
| **> 35%**   | 16    | 32.0% | Mostly larger N and more routes                   |

- **Scale**: gaps of a few to ~15% are more common for \(N < 40\). For \(N > 60\), gaps widen to about 35–65%, as expected from a general search plus light neighborhoods—not LKH-3 / HGS-class dedicated solvers.
- **Comparison rule**: all 50 gaps are positive. Floating-point tours are **not** claimed to beat official integer UBs.

---

## Scope (not a roadmap claim)

These results are a deterministic **CPU POC baseline**. Gap reduction can be pursued via decode and neighborhood modules. **This document does not claim verified ASIC/FPGA results, and does not claim a drop-in replacement for enterprise VRP solvers.**

---

## Verification and signing

- **Seed**: 42
- **Artifact**: `solution_*.bin` (SHA-256 integrity)
- **Signature**: Ed25519 (`qat-poc-ed25519-v1`), public key `public_key.pem`
- **Authority**: Quantum Alpha Technology Co., Ltd. / Jahua Chang

---

---

# CVRPLIB A & B 系列：通用核心基準驗證

**50 題（A 系列 27 + B 系列 23）｜ N = 30–79 ｜ K = 5–10**

- **引擎**：QαT Universal Optimization Engine（POC v1.1.1）
- **問題**：容量限制車輛路徑問題（CVRP）
- **環境**：確定性單執行緒 CPU，Seed = 42
- **驗證**：SHA-256 完整性 ＋ Ed25519 簽署（`qat-poc-ed25519-v1`）

> **聲明**：本文件紀錄 POC 基準表現，不是商用 VRP 求解器比較，也不是官方最優或官方可行性證明。

完整實例表見上方英文段（數字相同，不重複排版）。

## 本報告中的「可行」定義

1. **`true_conflicts = 0`**：車數不低於理論下限 \(\lceil \sum d_i / Q \rceil\)。未另做官方規格的逐車載重、漏點、整數距離獨立檢核。
2. **`customers_served`**：依編碼長度計，非獨立服務證明。
3. **里程定義**：里程為解碼器浮點歐氏距離；官方 UB 為 CVRPLIB 整數距離。Gap 僅供對照。

## 架構說明

採用**共用搜尋核心 ＋ VRP 專用解碼與鄰域**（含 2-opt、Relocate）。與 Steiner Tree、Bin Packing 等任務共用核心，但目標與解碼不同。

**A 系列小結**：27/27 達本引擎可行定義；相對 UB 最緊為 **A-n33-k6 (+6.65%)**；平均 Gap 約 26.9%。

**B 系列小結**：23/23 達本引擎可行定義；相對 UB 最緊為 **B-n34-k5 (+1.16%)**；平均 Gap 約 32.2%。

## 合併觀察（50 題整體分佈）

- **< 5%**：2 題（4.0%）
- **5%–15%**：8 題（16.0%）
- **15%–35%**：24 題（48.0%）
- **> 35%**：16 題（32.0%）

小規模（約 \(N < 40\)）較容易出現個位數到十餘百分比 gap。當 \(N > 60\) 時，gap 拉寬到約 35–65%，符合「通用搜尋 ＋ 輕量鄰域」、而非 LKH-3 / HGS 等級專用求解器的預期。50 題均為正 gap；不以浮點里程宣稱優於官方整數 UB。

## 範圍

本結果是 CPU 上的確定性 POC 基準。壓縮 gap 可透過解碼與鄰域模組調整，**不在本文件主張 ASIC／FPGA 已驗證，亦不主張可直接取代企業專用 VRP 求解器**。

## 驗證與簽署

- **Seed**：42
- **Artifact**：`solution_*.bin`（SHA-256 完整性檢查）
- **Signature**：Ed25519（`qat-poc-ed25519-v1`），公鑰 `public_key.pem`
- **簽署主體**：Quantum Alpha Technology Co., Ltd. ／ Jahua Chang
