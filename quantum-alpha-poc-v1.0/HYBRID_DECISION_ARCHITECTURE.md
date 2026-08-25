# From Proposal to Verifiable Decision

**A Hybrid Pattern for AI + Deterministic Optimization**

**Company:** Quantum Alpha Technology Co., Ltd. (Taiwan)  
**Author / Technical Contact:** Jahua Chang (`jahua@quantum-alpha.tech`)  
**Related release:** QαT POC v1.1.0  
**Status:** Architecture note for an evaluation-stage POC

---

## 1. Purpose

This note explains a design that already exists in the QαT POC:

- structured **API / JSON** input
- a **deterministic optimization core**
- a **hard feasibility gate** (`true_conflicts = 0`)
- **SHA-256 + Ed25519** signed artifacts

The question is not whether a language model can be made internally deterministic.  
The question is whether an AI system can be placed into a loop where:

1. open-ended interpretation is allowed
2. closed-end decisions are constrained
3. accepted outputs are reproducible and independently checkable

This document describes that pattern, its limits, and how the same contract can continue if a future Optimization Processing Unit (OPU) is implemented in silicon.

---

## 2. Three Different Kinds of Determinism

| Type | Meaning | Typical generative AI | QαT POC |
|------|---------|------------------------|---------|
| **Reproducible execution** | Same input + same seed → same output | Weak | Strong (fixed Seed=42, signed `.bin` / `.npy`) |
| **Constraint determinism** | Hard rules must hold (no collision, no overload, conflicts = 0) | Weak (rules often live in prompts) | Medium–strong (`true_conflicts` gate inside the model) |
| **World / semantic certainty** | The system truly understands the scene and is correct in reality | Not guaranteed | **Not guaranteed** (proxy encodings, not certified perception) |

The engine can strengthen the first two.  
The third does not appear automatically by attaching a solver.

---

## 3. Why a Hybrid Pattern

Generative models are useful at the open end:

- reading JSON or natural-language context
- inferring task type
- filling missing fields
- proposing candidate encodings or trajectories

They are weak at the closed end:

- identical reruns
- enforcing hard constraints as numeric gates
- producing artifacts that a third party can verify without trusting the model

A more reliable system therefore splits the work:

```text
Open / uncertain input
        ↓
AI proposes a candidate encoding or task JSON
        ↓
Deterministic engine (fixed seed, constrained search)
        ↓
Accept only if true_conflicts = 0
        ↓
Signed output (.bin / .npy + SHA-256 + Ed25519)
```

Plainly:

**AI proposes. The engine decides under constraints. The signature proves what ran.**

---

## 4. Mapping onto the Existing POC

The current software already has the skeleton of this loop.

| Layer | What exists now |
|-------|------------------|
| **Interface** | API + JSON-structured task input and result output |
| **Search** | Deterministic mode, default Seed=42 |
| **Feasibility gate** | `true_conflicts = 0` required for a solved / accepted result |
| **Proof** | SHA-256 content hash + Ed25519 signature + public key |
| **Scope label** | Human-readable notes that distinguish model-feasible from commercially certified |

The missing piece in most AI stacks is not “another model.”  
It is a backend that can **accept, reject, replay, and attest**.

---

## 5. What This Can Improve

- Same JSON + same seed can be rerun
- Hard constraints can be numeric gates, not prompt wording
- Failures can be classified (bad encoding, unresolved conflicts, timeout)
- Edge or safety-sensitive settings can move “must not collide / must not overload” from language into the objective and conflict functions

## 6. What This Cannot Automatically Provide

- If perception or task encoding is wrong, the engine can still find a feasible solution **inside the wrong model**
- `true_conflicts = 0` means zero conflicts under the current encoding and conflict function — not vehicle certification
- A 5.3-second CPU POC is not a measured millisecond closed-loop controller
- Model weights remain statistical; determinism lives in the **search + verification layer**, not inside the transformer

Accurate sentence:

> The algorithm does not make the generative model itself deterministic.  
> It places AI inside a propose → constrain → lock → attest loop, so the **decision chain** is more reproducible and more auditable than AI alone.

---

## 7. Example: Autonomous Emergency Motion

One validated task in POC v1.1.0 illustrates the closed end of the loop:

- Task: `autonomous_emergency_motion`
- Setting: 3 obstacles, 3 lanes, 512-D decision space
- Runtime: 5.2874 seconds on a single consumer-grade core
- Result: `true_conflicts = 0`
- Verification: SHA-256 + Ed25519

This is an evolutionary POC on a simplified kinodynamic proxy model.  
It is **not** a vehicle-certified ADAS / MPC stack.

Its value here is architectural: after a candidate problem is encoded, the engine can search, apply a hard gate, and emit a checkable artifact.

---

## 8. Continuity onto a Future OPU

If an Optimization Processing Unit is later realized in silicon, the intended continuity is:

| Stage | What stays | What changes |
|-------|------------|--------------|
| Software POC | Contract: propose → constrain → gate → sign | Seconds-scale CPU runtime |
| First OPU | Same API/JSON contract, same gates, same attestation idea | Latency and power |
| Later OPU + tighter task models | Same contract | Closer alignment to industrial constraints |

The chip would change the **carrier and delay**, not require a rewrite of the decision contract.

Industrial usefulness still needs a dual track:

- hardware optimization for latency and energy
- task-model and validation upgrades for physical, regulatory, and operational constraints

Faster silicon does not by itself equal production safety.

---

## 9. Honest Boundary

This note describes an **architectural possibility demonstrated in software**.

It does not claim:

- replacement of commercial solvers
- certified medical, financial, military, or automotive deployment
- that signed feasibility equals real-world correctness
- that an OPU already exists

The correct public position is:

> The POC shows that a deterministic, verifiable optimization layer can sit behind AI proposals.  
> A future OPU, if implemented, can carry the same contract to the edge.  
> Usefulness in industry will depend on both hardware progress and stricter task models.

---

## Related Documents

- `README.md`
- `ARCHITECTURE_OVERVIEW.md`
- `VERIFICATION_GUIDE.md`
- `LICENSE.md`
- GitHub: https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC

---
---

# 從提案到可驗證決策

**AI + 確定性優化的混合模式說明**

**公司：** 量子阿爾法科技有限公司（Quantum Alpha Technology Co., Ltd.，台灣）  
**作者 / 技術聯絡人：** 張家華（Jahua Chang，`jahua@quantum-alpha.tech`）  
**對應版本：** QαT POC v1.1.0  
**狀態：** 評估階段 POC 的架構說明

---

## 1. 目的

本文件說明 QαT POC 中已經具備的設計：

- 結構化的 **API / JSON** 輸入
- **確定性優化核心**
- **硬可行性閘門**（`true_conflicts = 0`）
- **SHA-256 + Ed25519** 簽章產出

重點不是「讓語言模型內部自己變確定」，  
而是能否把 AI 放進一條迴路：

1. 允許開放端理解
2. 封閉端決策必須受約束
3. 被接受的輸出可重現、可被第三方檢驗

本文說明這個模式、它的界限，以及若未來 Optimization Processing Unit（OPU）做成矽晶，同一契約如何延續。

---

## 2. 三種不同的確定性

| 類型 | 意思 | 典型生成式 AI | QαT POC |
|------|------|----------------|---------|
| **再現確定性** | 同樣輸入 + 同樣種子 → 同樣輸出 | 弱 | 強（固定 Seed=42，已簽章 `.bin` / `.npy`） |
| **約束確定性** | 硬規則必須成立（不撞、不超載、衝突=0） | 弱（規則常靠 prompt） | 中～強（模型內 `true_conflicts` 閘門） |
| **語意／世界確定性** | 系統真的理解場景並在現實中正確 | 不保證 | **不保證**（代理編碼，非認證感知） |

引擎能加強前兩種。  
第三種不會因為接上求解器就自動出現。

---

## 3. 為什麼需要混合模式

生成式模型適合開放端：

- 讀 JSON 或自然語言脈絡
- 判斷任務類型
- 補齊缺欄
- 提出候選編碼或軌跡

它在封閉端較弱：

- 同樣輸入能否重現
- 硬約束能否當成數字閘門
- 結果能否不靠「相信模型」而被驗證

較穩的系統因此分工：

```text
非確定／開放輸入
        ↓
AI 提出候選編碼或任務 JSON
        ↓
確定性引擎（固定種子、約束搜尋）
        ↓
僅在 true_conflicts = 0 時接受
        ↓
簽章輸出（.bin / .npy + SHA-256 + Ed25519）
```

一句話：

**AI 提案。引擎在約束下裁決。簽章證明這次實際跑了什麼。**

---

## 4. 對應到現有 POC

目前軟體已具備這條迴路的骨架。

| 層級 | 現況 |
|------|------|
| **接口** | API + JSON 結構化任務輸入與結果輸出 |
| **搜尋** | 確定性模式，預設 Seed=42 |
| **可行性閘門** | 接受結果需 `true_conflicts = 0` |
| **證明** | SHA-256 雜湊 + Ed25519 簽章 + 公開金鑰 |
| **範圍標示** | 人類可讀說明會區分「模型內可行」與「商用／車規認證」 |

多數 AI 系統缺的不是「再多一個模型」，  
而是一個能 **接受、拒絕、重跑、證明** 的後端。

---

## 5. 能提升什麼

- 同一 JSON、同一 seed 可重跑
- 硬約束可做成數字閘門，而不是提示詞
- 失敗可分類（編碼錯、衝突清不掉、超時）
- 可把「不准撞／不准超載」從語言層搬進目標函數與衝突函數

## 6. 不能自動得到什麼

- 感知或任務編碼若錯，引擎仍可能在**錯誤世界模型**裡求出可行解
- `true_conflicts = 0` 只代表目前編碼與衝突函數下零衝突，不是車規認證
- 單核 5.3 秒的 POC，不是已量測的毫秒級閉環控制器
- 模型權重仍是統計的；確定性在**搜尋與驗證層**，不在 transformer 內部

比較精確的句子：

> 演算法不能讓生成模型本身變成確定的。  
> 但它可以把 AI 放進「提案 → 約束求解 → 鎖定 → 證明」的迴路，  
> 讓**整條決策鏈**比單用 AI 更可重現、更可審計。

---

## 7. 實例：Autonomous Emergency Motion

POC v1.1.0 中的一個已驗證任務，可用來說明封閉端：

- 任務：`autonomous_emergency_motion`
- 設定：3 個障礙物、3 車道、512 維決策空間
- 時間：消費級單核 5.2874 秒
- 結果：`true_conflicts = 0`
- 驗證：SHA-256 + Ed25519

這是簡化動態約束模型上的演化式 POC，  
**不是**車規 ADAS／MPC 系統。

這裡的價值是架構性的：問題被編碼後，引擎可以搜尋、套用硬閘門，並產出可檢查的產物。

---

## 8. 如何延續到未來的 OPU

若未來 OPU 做成矽晶，預定延續方式是：

| 階段 | 不變的 | 改變的 |
|------|--------|--------|
| 軟體 POC | 契約：提案 → 約束 → 閘門 → 簽章 | CPU 上的秒級時間 |
| 初代 OPU | 同一 API／JSON 契約、同一閘門、同一證明思路 | 延遲與功耗 |
| 後續 OPU + 更嚴的任務模型 | 同一契約 | 更接近產業約束 |

晶片換的是**載體與延遲**，不是整套決策契約重寫。

產業實用仍需雙軌：

- 硬體優化負責時間與能耗
- 任務模型與驗證標準負責物理、法規與操作約束

算得比較快，不會自動等於可量產安全。

---

## 9. 誠實邊界

本文件描述的是**已在軟體中示範的架構可能性**。

它不宣稱：

- 已取代商用求解器
- 已通過醫療、金融、軍事或車用認證
- 已簽章的可行解等於現實正確
- OPU 已經存在

較正確的公開定位是：

> POC 顯示：確定性、可驗證的優化層可以接在 AI 提案之後。  
> 未來若實現 OPU，可以把同一契約帶到邊緣。  
> 能否用於產業，仍取決於硬體進展與更嚴格的任務模型。

---

## 相關文件

- `README.md`
- `ARCHITECTURE_OVERVIEW.md`
- `VERIFICATION_GUIDE.md`
- `LICENSE.md`
- GitHub: https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC
