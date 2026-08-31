# Architecture Overview

**Universal Optimization Engine (QαT) - POC v1.1.1**

## Three-Layer Design

The engine adopts a clean, modular three-layer architecture that balances high generality with task-specific performance:

### 1. Core Engine Layer (Problem-Agnostic)

- Unified evolutionary search logic
- Shared protection and feasibility mechanisms (`true_conflicts = 0` gu  arantee)
- Common optimization strategies supporting three fundamental modes
- Three-mode support: Minimization, Maximization, and Balance

### 2. Task Adaptation Layer

- Modular task registration mechanism supporting new task extension (requires corresponding problem structure design)
- Task-specific decoders and evaluation functions
- Specialized handling for different problem structures

### 3. Interface & Verification Layer

- Human-readable summaries and executive summary
- Built-in cryptographic signing (SHA-256 + Ed25519)
- GUI verifier and command-line tools
- Deterministic execution with fixed seeds

**Total codebase size**: About **11,000 lines of logic** (~15,000 physical lines including blanks and comments) — naturally evolved during development, making it easy to maintain, optimize, and adapt for future hardware implementation.

This layered design enables the same core to handle 47+ diverse tasks while keeping the internal logic clean and extensible.

## Core + Composable Task Modules

The engine is not 47 separate solvers. It is one core plus task modules.

              Core A
                 |
        +--------+--------+
        |        |        |
      modules  modules  modules
      (subset) (subset) (subset)
        |        |        |
      config   config   config
        |        |        |
      FPGA     ASIC    RISC-V

The diagram is illustrative. It does not represent public SKUs or a numbered module catalog.

* Validated task count is **coverage**, not product count.
* A future hardware mapping is intended to implement a **selected configuration** (Core + required modules), not every validated task on every chip.
* Intended form: `Core A + {selected modules}`not: `Solver_1 + Solver_2 + … + Solver_n`
* Changing a configuration may still require hardware synthesis, area, memory, and timing work.
* That is **not** the same as rewriting the core search architecture.

The core does not scale by becoming a larger solver.It scales by composing more capabilities around the same computational core.

## Why Suitable for Circuit Implementation

The architecture is intentionally designed with future hardware (FPGA / ASIC / logic circuit) acceleration in mind:

- **Compact codebase** (~10,000 lines): Naturally concise structure significantly easier to audit, optimize, and translate into hardware.
- **Binary solution encoding**: Core operations use simple selection encoding (edge/node selection) that maps naturally toward digital logic.
- **Rule-based evaluation**: Local constraint checking structure is well-suited for future hardware parallelization.
- **Deterministic core**: Fixed-seed execution eliminates randomness issues common in hardware.
- **Built-in feasibility protection**: Hard constraint satisfaction (`true_conflicts = 0`) can be realized as dedicated hardware checkers.
- **Low power consumption**: Proven to run efficiently on single-core CPU with <6GB memory, indicating excellent scalability to dedicated silicon.

Compared to mathematical programming solvers that rely on complex floating-point iterations, this engine’s structure is significantly more hardware-friendly.

## Comparison with Traditional Solvers

| Aspect                         | QαT Engine                          | Traditional Solvers (Gurobi, CPLEX, OR-Tools) |
| ------------------------------ | ----------------------------------- | --------------------------------------------- |
| **Optimization Paradigms**     | Three modes in single core          | Usually single-direction (min or max)         |
| **Resource Requirement**       | Single-core, <6GB memory            | Medium-to-large problems often require multi-core servers, 16GB+ memory |
| **Feasibility Guarantee**      | Built-in `true_conflicts = 0`       | Requires manual constraint modeling           |
| **Verifiability**              | Cryptographic signatures per result | Usually no built-in digital signature         |
| **Reproducibility**            | 100% deterministic (fixed seed)     | Often non-deterministic or timing dependent   |
| **Task Switching**             | Same core, 46+ tasks                | Usually problem-specific modeling             |
| **Hardware Acceleration Path** | High (binary solution encoding + rule-based)   | Low (complex mathematical iterations)         |

**Key Differentiation**:  
QαT provides a **unified, compact, low-power, verifiable, and hardware-friendly** optimization framework that can be rapidly adapted across many problem domains.

---

---

# 架構簡介（中文版）

**通用優化引擎 (QαT) - POC v1.1.1**

## 三層架構設計

本引擎採用清晰的模組化三層架構，既保有高度通用性，又能維持特定任務的效能：

### 1. 核心引擎層（問題無關）

- 統一的演化搜尋邏輯
- 共用的保護與可行性機制（`true_conflicts = 0` 保證）
- 通用的優化策略，支援三種基礎模式
- 三模式支援：望小、望大、平衡

### 2. 任務適配層

- 模組化任務註冊機制，支援新任務擴展（需對應問題結構設計）
- 任務專屬解碼器與評估函數
- 針對不同問題結構的專門處理

### 3. 介面與驗證層

- 人類可讀摘要與執行摘要
- 內建密碼學簽章（SHA-256 + Ed25519）
- GUI 驗證工具與指令列工具
- 確定性執行（固定 Seed）

**總程式碼規模**：約 **1.1 萬行有效邏輯**（含空行與註解約 1.5 萬實體行）—— 在開發過程中自然形成，便於維護、優化與硬體實作。

這種分層設計讓同一個核心能夠處理 47 種以上不同任務，同時保持內部邏輯的乾淨與可擴展性。

## 核心 + 可組合任務模組

引擎不是 47 個獨立求解器，而是一個核心加上任務模組。

              核心 A
                 |
        +--------+--------+
        |        |        |
       模組     模組     模組
      （子集）  （子集）  （子集）
        |        |        |
       組態     組態     組態
        |        |        |
      FPGA     ASIC    RISC-V

上圖為結構示意，不是公開料號，也不是模組編號表。

* 已驗證任務數是**覆蓋範圍**，不是產品數量。
* 未來若對應硬體，預定實現的是**選定組態**（核心 + 所需模組），不是每顆晶片都載入全部任務。
* 預定形式：`核心 A + {選用模組}`而不是：`Solver_1 + Solver_2 + … + Solver_n`
* 組態改變時，硬體端仍可能要做 synthesis、面積、記憶體與時序。
* 這**不等於**核心搜尋架構需要重寫。

核心的擴展，不是把自己變成更大的 solver，而是在同一計算核心外圍組合更多能力模組。

## 為什麼適合電路化實作

本架構從設計之初就考慮到未來硬體加速（FPGA / ASIC / 邏輯電路）的可行性：

- **精簡程式碼規模**（約 10,000 行）：自然形成的精簡結構，大幅降低審核、優化與硬體轉譯難度。
- **二進位解編碼**：核心操作使用簡單的選擇編碼（edge/node selection），便於對應到數字邏輯。
- **規則導向評估**：局部約束檢查結構適合未來硬體並行化實作。
- **確定性核心**：固定 Seed 消除硬體常見的隨機性問題。
- **內建可行性保護**：硬性約束滿足（`true_conflicts = 0`）可實作為專用硬體檢查器。
- **低功耗特性**：已在單核、<6GB 記憶體下驗證，顯示良好的硬體可擴展性。

相較於依賴複雜數學迭代的傳統規劃求解器，本引擎的結構明顯更適合硬體實作。

## 與傳統求解器的對比

| 項目         | QαT 引擎                  | 傳統求解器（Gurobi、CPLEX、OR-Tools） |
| ---------- | ----------------------- | ---------------------------- |
| **優化模式**   | 同一核心支援三大模式              | 通常單一方向（最小化或最大化）              |
| **資源需求**   | 單核、<6GB 記憶體             | 中大型問題需多核心伺服器、16GB+ 記憶體       |
| **可行性保證**  | 內建 `true_conflicts = 0` | 需手動建模約束                      |
| **可驗證性**   | 每個結果皆有數位簽章              | 通常無內建數位簽章                    |
| **可重現性**   | 100% 確定性（固定 Seed）       | 常有隨機性或時序依賴                   |
| **任務切換**   | 同一核心支援 46+ 任務           | 通常需針對問題重新建模                  |
| **硬體加速潛力** | 高（二進制解編碼 + 基於規則）      | 低（複雜數學迭代）                    |

**核心差異化**：  
QαT 提供一個**統一、精簡、低功耗、可驗證、且適合硬體加速**的優化框架，能快速適應多種問題領域。

---

**文件結束**
