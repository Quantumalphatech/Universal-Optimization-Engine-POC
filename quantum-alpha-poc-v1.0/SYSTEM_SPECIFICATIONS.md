# System Specifications

**Universal Optimization Engine (QαT) - POC v1.0**

## Hardware Requirements

**Minimum Requirements**:

- **CPU**: Intel i5 12th Gen or equivalent (single-core sufficient)
- **Memory**: **<6GB** RAM (tested and confirmed across all instances including C20)
- **Storage**: ~10GB free space
- **GPU**: Not required

**Recommended Configuration**:

- Intel i5 12th Gen or better
- 6GB+ RAM (DDR4 or above)
- SSD storage

**Tested Environment**:

- Intel i5 12th Gen laptop
- Single-core execution only
- Maximum memory footprint: <6GB (even on largest C set instances)

The engine is designed for **consumer-grade hardware** with no special infrastructure required.

## Performance Metrics by Scale

| Scale                          | CPU Peak | Memory Usage | Typical Runtime                                  | Notes                     |
| ------------------------------ | -------- | ------------ | ------------------------------------------------ | ------------------------- |
| B set (50–100 nodes)           | <10%     | ~1.5 GB      | 100–600 seconds (B01 ~349 s, B18 ~525 s)         | Light, fast convergence   |
| C set small (625 edges)        | 10–19%   | 1.5–2.0 GB   | 100–2000 seconds                                 | Stable throughput         |
| C set medium (1000–2500 edges) | 15–25%   | 2.0–3.7 GB   | 1000–5000 seconds (C10 ~2415 s, C15 ~3875 s)     | Dynamic memory allocation |
| C set large (12500 edges)      | 20–30%   | <6 GB        | 5000–28000+ seconds (C20 ~16464 s, C19 ~28183 s) | Memory self-regulates     |

All tests were performed on a single core with no GPU acceleration.

## Deterministic Execution Details

- **Fixed Seed**: Default Seed=42 (100% reproducible results)
- **Alternative Seeds**: Supported (e.g., 666, 8888)
- **Random Mode**: Available for exploration (non-deterministic)
- **Reproducibility Guarantee**: Same input + same seed always produces identical `.bin` / `.npy` output
- **Verification**: Every result includes SHA-256 hash + Ed25519 digital signature

## Multi-mode Architecture (Min/Max/Balance)

The engine supports three fundamental optimization paradigms within the **same core**:

1. **Minimization Mode (望小模式)**  
   
   - Goal: Minimize cost, distance, conflicts, energy, time  
   - Status: Highly mature  
   - Example tasks: Steiner Tree, Graph Coloring, Bin Packing, VRP

2. **Maximization Mode (望大模式)**  
   
   - Goal: Maximize coverage, profit, utility, selected items  
   - Status: Core functions complete, continuously expanding  
   - Example tasks: Knapsack, Maximum Cut, Portfolio Optimization

3. **Balance Mode (平衡模式)**  
   
   - Goal: Trade-off between multiple objectives with adaptive weighting  
   - Status: Recently stabilized, expanding  
   - Example tasks: bipedal_humanoid_balance (primary)

**Key Advantage**: The same search engine and protection mechanisms are shared across all three modes, demonstrating high abstraction level and true generality.

## Core Engine Properties

- **Problem Coverage**: 46+ diverse optimization tasks
- **Feasibility Guarantee**: All solutions enforce `true_conflicts = 0`
- **Solution Encoding**: Binary selection (edge/node selection) — hardware circuit friendly
- **Modularity**: Core engine + task-specific decoder/fitness layers
- **Cryptographic Verifiability**: Built-in SHA-256 + Ed25519 signing
- **Portability**: Cross-platform (Windows/Linux/macOS), standard Python environment
- **Hardware Pathway**: Designed with future logic circuit / ASIC implementation in mind

---

---

# 系統規格說明（中文版）

**通用優化引擎 (QαT) - POC v1.0**

## 硬體需求

**最低需求**：

- **CPU**：Intel i5 第12代或同級（單核即可）
- **記憶體**：**<6GB** RAM（所有實例包含 C20 皆已驗證）
- **儲存空間**：約 10GB 可用空間
- **GPU**：無需

**建議配置**：

- Intel i5 第12代以上
- 6GB+ RAM（DDR4 或以上）
- SSD 儲存

**測試環境**：

- Intel i5 12th Gen 筆電
- 單核執行
- 最大記憶體使用量：<6GB

引擎專為**消費級硬體**設計，無需特殊基礎設施。

## 各規模效能指標

| 規模                 | CPU 使用率 | 記憶體使用量     | 典型執行時間                                          | 備註      |
| ------------------ | ------- | ---------- | ----------------------------------------------- | ------- |
| B 組（50–100 節點）     | <10%    | ~1.5 GB    | 100–600 秒（B01 約 349 秒，B18 約 525 秒）              | 輕量，快速收斂 |
| C 組小型（625 邊）       | 10–19%  | 1.5–2.0 GB | 100–2000 秒                                      | 穩定吞吐    |
| C 組中型（1000–2500 邊） | 15–25%  | 2.0–3.7 GB | 1000–5000 秒（C10 約 2415 秒，C15 約 3875 秒）          | 動態記憶體分配 |
| C 組大型（12500 邊）     | 20–30%  | <6 GB      | 5000–28000 秒以上（C20 實測約 16464 秒，C19 實測約 28183 秒） | 記憶體自我調節 |

所有測試均在單核、無 GPU 環境下完成。

## 確定性執行細節

- **固定 Seed**：預設 Seed=42（100% 可重現）
- **其他 Seed**：支援（例如 666、8888）
- **隨機模式**：可用於探索（非確定性）
- **可重現性保證**：相同輸入 + 相同 Seed 必定產生完全相同的 `.bin` / `.npy` 輸出
- **驗證機制**：每個結果皆包含 SHA-256 + Ed25519 數位簽章

## 三模式架構（望大 / 望小 / 平衡）

同一核心支援三種基礎優化模式：

1. **望小模式（Minimization）**  
   
   - 目標：最小化成本、距離、衝突、能量、時間  
   - 成熟度：高度成熟  
   - 範例任務：Steiner Tree、Graph Coloring、Bin Packing

2. **望大模式（Maximization）**  
   
   - 目標：最大化覆蓋率、利潤、效用  
   - 成熟度：基礎功能完整，持續擴展中  
   - 範例任務：Knapsack、Maximum Cut

3. **平衡模式（Balance）**  
   
   - 目標：在多目標間取得動態平衡  
   - 成熟度：已穩定，正在擴展  
   - 範例任務：bipedal_humanoid_balance（主要）

**核心優勢**：三種模式共用同一搜尋引擎與保護機制，展現高度抽象能力與真正的通用性。

## 核心引擎特性

- **問題涵蓋**：46 種以上不同優化任務
- **可行性保證**：所有解皆確保 `true_conflicts = 0`
- **編碼方式**：二進位選擇（edge/node selection），有利於硬體電路化
- **模組化設計**：核心引擎 + 任務特化 Decoder / Fitness 層
- **密碼學可驗證**：內建 SHA-256 + Ed25519 簽章
- **可攜性**：跨平台（Windows/Linux/macOS），標準 Python 環境
- **硬體化潛力**：從設計之初即考慮邏輯電路 / ASIC 實作

---

**文件結束**  

