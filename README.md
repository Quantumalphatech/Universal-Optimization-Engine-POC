# Universal Optimization Engine (QαT) - POC v1.0

**Company:** Quantum Alpha Technology Co., Ltd.**Author:** Jahua Chang **Release Date:** July 19, 2026**Status:** Public Proof of Concept Release

## Project Overview

This is a **compact, low-resource universal optimizer** for NP-hard combinatorial and engineering optimization problems using a single core architecture.

Key design principles:

* **Feasibility-first**: All solutions guarantee `true_conflicts = 0`
* **Deterministic & Verifiable**: 100% reproducible with cryptographic signatures
* **Three optimization modes**: Minimization, Maximization, and Balance
* **Hardware-friendly**: Designed for future logic circuit and ASIC implementation

The entire engine naturally evolved to approximately **10,000 lines** during development, making it easy to maintain, optimize, and adapt.

## Core Achievements

* **Steiner Tree Benchmark** (SteinLib B & C sets): 38/38 instances solved with `true_conflicts = 0`
  * 4 instances achieved **optimal solution** (0% gap)
  * Specifically: B03 (25 terminals), B08 (19 terminals), B09 (38 terminals), and B18 (50 terminals) all hit the official optimal solutions in the international standard test
  * Strong performance on high terminal density instances (e.g. C05 +2.4%, C10 +3.5%)
* **Multi-mode Architecture**: Single core supports Minimization, Maximization, and Balance modes
* **Problem Coverage**: 46+ diverse optimization tasks
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

## Supported Tasks (46+)

The engine currently supports 46 problem types across multiple domains:

**Tasks with established full verification pipeline**:

* Steiner Tree (international benchmark, 38/38 completed)
* Bin Packing (theoretical lower bound verifiable)
* EDA Routing (large-scale graph simulation)
* Graph Coloring

**Other Supported Domains**:

* Combinatorial Optimization (TSP, Knapsack, Job Shop, Cutting Stock, VRP, QAP)
* Network & Routing (Network Topology, Supply Chain, Smart Grid)
* Engineering Applications (Robot Kinematics, Thermal Dissipation)
* Emerging Fields (Zero-Knowledge Proof Circuit, Post-Quantum Crypto, etc.)

New tasks can be extended through the modular architecture (requires corresponding problem structure design).

## Key Advantages

* **Compact Codebase**: Approximately 10,000 lines — easy to maintain and optimize
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

## Contact Information

**Quantum Alpha Technology Co., Ltd.**Technical Contact: Jahua ChangEmail: jahua@quantum-alpha.tech

* * *

**License**: Evaluation and research use only. Core algorithm protected as trade secret.**Repository**: [GitHub link will be added upon release]

* * *

* * *

# Universal Optimization Engine (QαT) - POC v1.0（中文版）

**公司**：量子阿爾法科技有限公司 (Quantum Alpha Technology Co., Ltd.)**作者**：張家華 (Jahua Chang)**發布日期**：2026年7月19日**狀態**：公開 POC 發布版本

## 項目概述

這是一個**精簡、低資源的通用優化引擎**，專注解決 NP-hard 組合優化與工程問題，使用單一核心架構。

核心設計原則：

* **可行性優先**：所有解皆保證 `true_conflicts = 0`
* **確定性與可驗證**：100% 可重現，並具備密碼學簽章
* **三種優化模式**：望小、望大、平衡
* **硬體友善**：從設計之初即考慮邏輯電路與 ASIC 實作

整個引擎在開發過程中自然形成約 **10,000 行** 的規模，便於維護、優化與後續開發。

## 核心成就

* **Steiner Tree 國際標準測試**（SteinLib B & C 組）：38/38 實例全部求解完成，且 `true_conflicts = 0`
  * 4 個實例達到**最優解**（0% 差距）
  * 具體為：B03（25 個 terminals）、B08（19T）、B09（38T）、B18（50T）均在國際標準測試中命中官方最優解
  * 高終端密度實例表現突出（C05 +2.4%、C10 +3.5%）
* **三模式架構**：單一核心同時支援望小、望大、平衡模式
* **問題涵蓋**：46 種以上不同類型的優化任務
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

## 支援任務列表（46+）

目前已支援 46 種問題類型，涵蓋多個領域：

**已建立完整驗證流程的任務**：

* Steiner Tree（國際 benchmark，38/38 完成）
* Bin Packing（理論下界可驗證）
* EDA Routing（大規模圖論模擬）
* Graph Coloring

**其他支援領域**：

* 組合優化（TSP、Knapsack、Job Shop、Cutting Stock、VRP、QAP）
* 網路與路由（Network Topology、Supply Chain、Smart Grid）
* 工程應用（Robot Kinematics、Thermal Dissipation）
* 新興領域（Zero-Knowledge Proof Circuit、Post-Quantum Crypto 等）

新任務可透過模組化架構進行擴展（需對應問題結構設計）。

## 核心優勢

* **精簡程式碼**：約 10,000 行，便於維護與優化
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

## 聯絡資訊

**量子阿爾法科技有限公司**技術聯絡人：張家華（Jahua Chang）Email: jahua@quantum-alpha.tech

* * *

**授權方式**：評估與研究用途。核心演算法為商業機密。**儲存庫**：發布後將提供 GitHub 連結

* * *

**文件結束**
