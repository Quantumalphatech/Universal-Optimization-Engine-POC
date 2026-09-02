# Universal Optimization Engine (QαT) - POC v1.1.1

**Company:** Quantum Alpha Technology Co., Ltd.
**Author:** Jahua Chang 
**Release Date:** July 19, 2026
**Status:** Public Proof of Concept Release

## Project Overview

This is a **compact, low-resource universal optimizer** for NP-hard combinatorial and engineering optimization problems using a single core architecture.

Key design principles:

* **Feasibility-first**: All solutions guarantee `true_conflicts = 0`
* **Deterministic & Verifiable**: 100% reproducible with cryptographic signatures
* **Three optimization modes**: Minimization, Maximization, and Balance
* **Hardware-friendly**: Designed for future logic circuit and ASIC implementation

The current reference implementation is about 11,000 lines of logic (~15,000 physical lines including blanks and comments). This scale formed during development rather than being trimmed for presentation, and remains compact enough to maintain, audit, and adapt.

## Core Achievements

* **Steiner Tree Benchmark** (SteinLib B & C sets): 38/38 instances solved with `true_conflicts = 0`
  * 4 instances achieved **optimal solution** (0% gap)
  * Specifically: B03 (25 terminals), B08 (19 terminals), B09 (38 terminals), and B18 (50 terminals) all hit the official optimal solutions in the international standard test
  * Strong performance on high terminal density instances (e.g. C05 +2.4%, C10 +3.5%)
* **Multi-mode Architecture**: Single core supports Minimization, Maximization, and Balance modes
* **Problem Coverage**: 47+ diverse optimization tasks — the current count reflects validation effort, not architectural capacity
* **Resource Efficiency**: Single-core, low power consumption, <6GB memory
* **Verifiability**: Every solution includes SHA-256 + Ed25519 digital signature
* **Reproducibility**: 100% deterministic with fixed Seed=42

All solutions are **feasible within their respective problem models** (`true_conflicts = 0`).

## Hardware Specifications

* **Minimum Requirements**:
  
  * CPU: Intel i5 12th Gen or equivalent (single-core sufficient)
  * Memory: **<6GB** RAM
  * Storage: ~10GB free space
  * GPU: Not required
* **Tested Performance**:
  
  * Single-core execution
  * Low power consumption design
  * CPU utilization: 10%–30%
  * Memory usage: typically 1.5–4.0GB, maximum <6GB

The engine runs efficiently on standard consumer laptops.

## Development & Runtime Environment

The current POC is implemented as a **pure, self-developed Python** stack and runs on **consumer-grade single-core CPUs with <6GB RAM**.

Its core development and execution flow does not rely on GPU acceleration, commercial EDA toolchains, or third-party cloud platforms as part of the core toolchain. Full verification can be completed on a consumer-grade standalone machine.

## Hardware Orientation

QαT was designed from the outset with future hardware mapping in mind.
The compact ~11,000-line logical structure, binary solution encoding, and deterministic rule-based evaluation are intentionally chosen to facilitate potential translation into logic circuits or dedicated accelerators (FPGA / ASIC).

This POC demonstrates that a wide range of NP-hard problem structures can be handled under strict single-core and low-memory constraints — a necessary foundation for exploring GPU-free, edge-oriented optimization hardware.

## Core + Task Modules

The engine is not 47 separate solvers.
It is one core plus task modules.

Validated task count is coverage, not product SKUs.
A future hardware mapping is intended to implement a selected configuration
(Core + required modules), not every validated task on every chip.

Changing a configuration may still require hardware synthesis work.
It should not require redesigning the core search architecture.

## Complementing AI with a Deterministic Layer  

This POC is designed to complement generative AI, not replace it.

AI is strong at open-ended interpretation (reading JSON or context, filling fields, proposing candidate encodings). It is weaker at identical reruns, hard constraint satisfaction, and independently verifiable outputs.

The intended pattern is:

**AI proposes → the deterministic engine searches under constraints → a hard gate (`true_conflicts = 0`) accepts or rejects → SHA-256 + Ed25519 signs what actually ran.**

This improves system-level reproducibility and constraint reliability. It does not claim that the model itself understands the world, or that a feasible in-model solution equals production safety.

If a future Optimization Processing Unit (OPU) is implemented in silicon, the same contract can continue: software remains the proposal layer; the engine/OPU remains the closed, verifiable decision layer.

See `HYBRID_DECISION_ARCHITECTURE.md` for the full explanation.

## Supported Tasks (47+)

The engine currently supports 47+ problem types across multiple domains. The current count reflects validation coverage, not the architectural limit of the engine. New task types can be added via modular structure design without rewriting the core.

**Tasks with established full verification pipeline**:

* Steiner Tree (international benchmark, 38/38 completed)
* Bin Packing (theoretical lower bound verifiable)
* EDA Routing (large-scale graph simulation)
* Graph Coloring

**Other Supported Domains**:

* Combinatorial Optimization (TSP, Knapsack, Job Shop, Cutting Stock, VRP, QAP)
* Additional CVRP results on CVRPLIB A & B benchmark instances (50/50):
  POC baseline — see `CVRPLIB_AB_BASELINE.md`
  (standard international instances; not a commercial VRP solver comparison)
* Network & Routing (Network Topology, Supply Chain, Smart Grid)
* Engineering Applications (Robot Kinematics, Thermal Dissipation)
* Autonomous Systems (Emergency motion planning under dynamic constraints)
* Emerging Fields (Zero-Knowledge Proof Circuit, Post-Quantum Crypto, etc.)

New tasks can be extended through the modular architecture (requires corresponding problem structure design).

## Key Advantages

* **Compact Codebase**: About 11,000 lines of logic (~15,000 physical lines) — easy to maintain, audit, and optimize
* **Low Power Consumption**: Efficient single-core design suitable for edge devices
* **Absolute Reproducibility**: 100% deterministic execution (fixed Seed=42)
* **Cryptographic Verifiability**: SHA-256 + Ed25519 signatures for every result
* **Three-Mode Generality**: Handles minimization, maximization, and balance within one core
* **Feasibility Guarantee**: All outputs satisfy `true_conflicts = 0`

## Verification

All results are cryptographically signed and independently verifiable:

* SHA-256 content integrity
* Ed25519 digital signature (public key provided)
* One-click GUI verifier included

See `VERIFICATION_GUIDE.md` for complete instructions.

## 📺 Real-Time Execution Demo

Watch unedited 14-minute single-core execution of SteinLib B01 (.stp & .json formats):

[

![QαT Engine RealTime Benchmark](https://img.youtube.com/vi/vsg6ljJ2U2M/0.jpg)

](https://youtu.be/vsg6ljJ2U2M)

*Single-core CPU monitoring, execution logs, and Ed25519 verified output shown in real time.*

## Commercial & Licensing

This public package is an **evaluation-stage Proof of Concept**.
It is released for technical assessment, independent verification of signed results, and research discussion only.

The core algorithm and internal search logic are protected as **trade secrets** of Quantum Alpha Technology Co., Ltd.
This repository does **not** grant rights to use the core engine in commercial products, services, or production systems.

**Preferred commercial model:** global exclusive licensing, to be negotiated under a formal written agreement.
Other structures (if any) would also require prior written authorization.

For licensing or partnership inquiries:
- Email: jahua@quantum-alpha.tech
- Serious commercial discussions typically proceed under NDA before deeper materials are shared.

See `LICENSE.md` for the evaluation-use terms that apply to this public release.

## Contact Information

**Company:** Quantum Alpha Technology Co., Ltd.

**Author:** Jahua Chang

**Email**: jahua@quantum-alpha.tech

* * *

**License**: Evaluation and research use only. Core algorithm protected as trade secret.**Repository**: [[GitHub - Quantumalphatech/Universal-Optimization-Engine-POC: Proof of Concept — Universal Optimization Engine (QαT) · GitHub](https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC)]

* * *

* * *

# Universal Optimization Engine (QαT) - POC v1.1.1（中文版）

**公司**：量子阿爾法科技有限公司 (Quantum Alpha Technology Co., Ltd.)
**作者**：張家華 (Jahua Chang)
**發布日期**：2026年7月19日
**狀態**：公開 POC 發布版本

## 項目概述

這是一個**精簡、低資源的通用優化引擎**，專注解決 NP-hard 組合優化與工程問題，使用單一核心架構。

核心設計原則：

* **可行性優先**：所有解皆保證 `true_conflicts = 0`
* **確定性與可驗證**：100% 可重現，並具備密碼學簽章
* **三種優化模式**：望小、望大、平衡
* **硬體友善**：從設計之初即考慮邏輯電路與 ASIC 實作

目前 reference implementation 約 1.1 萬行有效邏輯（含空行與註解約 1.5 萬實體行）。此規模是開發過程自然形成，而非為了展示而刻意刪減，仍足以維持精簡、可審核與可擴充。

## 核心成就

* **Steiner Tree 國際標準測試**（SteinLib B & C 組）：38/38 實例全部求解完成，且 `true_conflicts = 0`
  * 4 個實例達到**最優解**（0% 差距）
  * 具體為：B03（25 個 terminals）、B08（19T）、B09（38T）、B18（50T）均在國際標準測試中命中官方最優解
  * 高終端密度實例表現突出（C05 +2.4%、C10 +3.5%）
* **三模式架構**：單一核心同時支援望小、望大、平衡模式
* **問題涵蓋**：47 種以上不同類型的優化任務——當前數量反映的是驗證工作量，而非架構容量
* **資源效率**：單核、低功耗、<6GB 記憶體
* **可驗證性**：每個解皆包含 SHA-256 + Ed25519 數位簽章
* **可重現性**：固定 Seed=42 即可 100% 重現

所有解在其各自問題模型中皆為**可行解**（`true_conflicts = 0`）。

## 硬體規格

* **最低需求**：
  
  * CPU：Intel i5 第12代或同級（單核即可）
  * 記憶體：**<6GB** RAM
  * 儲存空間：約 10GB
  * GPU：無需
* **測試表現**：
  
  * 單核執行
  * 低功耗設計
  * CPU 使用率：10%–30%
  * 記憶體使用：通常 1.5–4.0GB，最高 <6GB

引擎可在一般消費級筆電上高效運行。

## 開發與執行環境

目前 POC 以**純 Python 自研**實作，並在**消費級單核 CPU、<6GB 記憶體**環境下執行。

核心開發與執行流程不依賴 GPU 加速、商業 EDA 工具鏈，或第三方雲端平台作為核心工具鏈。全部驗證可在消費級單機環境完成。

## 硬體導向設計

QαT 從設計之初即以未來硬體對應為目標。
約 1.1 萬行有效邏輯的精簡結構、二進位解編碼，以及確定性的規則導向評估，都是為了讓後續轉換成邏輯電路或專用加速器（FPGA / ASIC）更為可行。

本 POC 證明了在嚴格的單核與低記憶體限制下，仍可處理多種 NP-hard 問題結構——這是探索無 GPU、面向邊緣裝置的優化硬體時，必要的軟體基礎。

## 核心 + 任務模組

引擎不是 47 個獨立求解器，
而是一個核心加上任務模組。

已驗證任務數是覆蓋範圍，不是產品料號。
未來若對應硬體，預定實現的是選定組態
（核心 + 所需模組），不是每顆晶片都載入全部任務。

組態改變時，硬體端仍可能要重新做 synthesis。
這不等於核心搜尋架構需要重寫。

## 以確定性層補足 AI

本 POC 的設計是補足生成式 AI，而不是取代它。

AI 擅長開放端理解（讀取 JSON 或上下文、補齊欄位、提出候選編碼）。它較弱的是：同樣輸入能否重現、硬約束能否守住、結果能否獨立驗證。

預定結合方式是：

**AI 提案 → 確定性引擎在約束下搜尋 → 以 `true_conflicts = 0` 作為硬閘門決定接受或拒絕 → 以 SHA-256 + Ed25519 證明這次實際跑出什麼。**

這提升的是系統層的再現性與硬約束可靠性。它不宣稱模型本身已理解真實世界，也不把「模型內可行解」等同於產業安全解。

若未來 Optimization Processing Unit（OPU）做成矽晶，同一契約可以延續：軟體仍負責提案，引擎／OPU 仍負責封閉、可驗證的決策。

完整說明見 `HYBRID_DECISION_ARCHITECTURE.md`。

## 支援任務列表（47+）

目前已支援 47 種以上問題類型，涵蓋多個領域。當前數量反映的是驗證覆蓋範圍，而非引擎的架構上限。新任務類型可透過模組化結構設計加入，無需重寫核心。

**已建立完整驗證流程的任務**：

* Steiner Tree（國際 benchmark，38/38 完成）
* Bin Packing（理論下界可驗證）
* EDA Routing（大規模圖論模擬）
* Graph Coloring

**其他支援領域**：

* 組合優化（TSP、Knapsack、Job Shop、Cutting Stock、VRP、QAP）
* 另於 CVRPLIB A & B 國際標準測試集公布 CVRP 結果（50/50）：
  POC 基準成績，見 `CVRPLIB_AB_BASELINE.md`
  （題庫為國際公認實例；非商用 VRP 求解器比較）
* 網路與路由（Network Topology、Supply Chain、Smart Grid）
* 工程應用（Robot Kinematics、Thermal Dissipation）
* 動態約束下的緊急運動規劃（autonomous_emergency_motion）
* 新興領域（Zero-Knowledge Proof Circuit、Post-Quantum Crypto 等）

新任務可透過模組化架構進行擴展（需對應問題結構設計）。

## 核心優勢

* **精簡程式碼**：約 1.1 萬行有效邏輯（含空行與註解約 1.5 萬實體行），便於維護、審核與優化
* **低功耗設計**：單核高效運行，適合邊緣裝置
* **絕對可再現性**：固定 Seed=42，100% 確定性
* **密碼學可驗證**：每個結果皆有 SHA-256 + Ed25519 簽章
* **三模式通用性**：單一核心同時支援望大、望小、平衡
* **可行性保證**：所有輸出皆保證 `true_conflicts = 0`

## 驗證方式

所有結果皆經過密碼學簽章，可獨立驗證：

* SHA-256 內容完整性
* Ed25519 數位簽章（公開金鑰已提供）
* 內建一鍵 GUI 驗證工具

詳細說明請參考 `VERIFICATION_GUIDE.md`。

## 📺 即時執行演示

觀看未經剪輯的 14 分鐘單核心 SteinLib B01 執行演示

（.stp 和 .json 格式）：

[

![QαT 引擎即時基準測試](https://img.youtube.com/vi/vsg6ljJ2U2M/0.jpg)

](https://youtu.be/vsg6ljJ2U2M)

*即時顯示單核心 CPU 監控、執行日誌以及 Ed25519 驗證的輸出結果。 *

## 商業與授權

本公開包為**評估階段概念驗證（POC）**。
僅供技術評估、已簽章結果的獨立驗證，以及研究討論使用。

核心演算法與內部搜尋邏輯為量子阿爾法科技有限公司之**商業秘密**。
本儲存庫**不授予**將核心引擎用於商業產品、服務或生產系統的權利。

**偏好的商業模式：** 全球獨家授權，須以正式書面協議另行洽談。
其他形式的使用（如有）亦須事先取得書面授權。

授權或合作洽詢：
- Email: jahua@quantum-alpha.tech
- 正式商業討論通常在簽署 NDA 後，才提供更深入的評估資料。

公開包的評估用途條款見 `LICENSE.md`。

## 聯絡資訊

**公司:量子阿爾法科技有限公司**

**技術聯絡人**：張家華（Jahua Chang）

**Email**: jahua@quantum-alpha.tech

* * *

**授權方式**：評估與研究用途。核心演算法為商業機密。**儲存庫**：[GitHub - Quantumalphatech/Universal-Optimization-Engine-POC: Proof of Concept — Universal Optimization Engine (QαT) · GitHub](https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC)

* * *

**文件結束**
