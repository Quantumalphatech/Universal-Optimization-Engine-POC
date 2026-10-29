# QαT OPU Global Exclusive Licensing — Final Application Window

**Issued by:** Quantum Alpha Technology Co., Ltd.

## 1. Technical Architecture and Core Value

Single core. Multi-task. Scalable.

QαT operates on a single universal core. Once a task completes, the core switches to the next without restart, reconfiguration, or reloading. This has been validated across 47+ NP-hard problem types in the public POC. 47+ is validation coverage, not an architectural limit, and not a claim that every problem type has been proven to a mathematical global optimum.

QαT is not 47 independent solvers. It is one core plus composable task modules. The core is fixed; tasks are composable. A future hardware mapping is intended to implement a selected configuration (core + required modules), not every validated task on every chip. Changing a configuration may still require hardware synthesis. That is not a redesign of the core search architecture.

The same core can support parallel replication and serial pipeline configurations to explore different throughput scaling paths. Multi-chip latency, power, area, and silicon-level performance are to be measured during actual hardware implementation. They are not current POC results.

Public results are led by SteinLib B+C 38/38, of which 4 matched official optima, and the CVRPLIB A+B 50/50 POC baseline. Fixed Seed=42. Results are signed with SHA-256 + Ed25519. Full architecture, task coverage, and verification methods are in the public repository README and related documents.

Within the scope of the evaluation agreement, the company is willing to present the QαT prototype as a packaged black-box on-site demonstration for evaluation. The evaluation fee buys controlled inspection of the existing implementation and verification baseline. It does not include taking the core or the implementation, and it is not a guarantee of returns. Subsequent optimization, task expansion, and hardware translation can use this baseline as a coordinate. Whether it is worth the fee is for the applicant to judge. After a global exclusive license is signed and paid, the software prototype is delivered under the license agreement. Delivery scope, version, and subsequent support are governed by that agreement.

## Article 1-1: OPU Compatible Interface Definition Rights

The global exclusive licensee shall have the right, as defined in the licensing agreement, to establish the OPU Compatible Interface Standard.

This right enables the licensee to define the deterministic decision interoperability standards between AI and the physical world, including but not limited to:

- Interoperability specifications between Central Processing Units (CPU) and OPU
- Interoperability specifications between Graphics Processing Units (GPU) and OPU
- Deterministic decision interfaces between AI accelerators and OPU
- Integration specifications between Embodied AI edge computing devices and OPU

The licensee may, pursuant to the licensing agreement, define, certify, license, and charge fees for the above compatibility standards. The specific scope, certification procedures, licensing terms, and fee structures shall be governed by the global exclusive licensing agreement.

The rights described in this article constitute one of the core commercial values of the global exclusive license, alongside OPU hardwarization, mass production, and deployment rights. The actual scope is governed by the final licensing agreement. This announcement does not claim that OPU hardware has been mass-produced or deployed.

## 2. Public Verification, Technical Ownership, and Commercial Rights

The public POC is for inspection of the existing implementation, test results, and verification baseline. Public verifiability is not public disclosure of the core. Evaluation rights are not commercial license rights, source code rights, or technology transfer rights.

Any commercial deployment, commercial use, mass production, sublicensing, or core technology transfer requires a separate written license. Public code and third-party packages remain under their original rights. This announcement does not claim rights beyond what the company actually owns or can license.

## 3. Final Application Window for Global Exclusive Licensing

Final deadline: 31 December 2026, 23:59 (Taiwan time, UTC+8).

After the deadline, no new licensing negotiation applications will be accepted, and the window will not be reopened. Cases that have formally entered substantive licensing negotiations before the deadline, and existing paid evaluation cases that have signed and whose evaluation fee has been received, are handled under the exceptions in Article 9. This is the company's final decision on this program.

"Global exclusive license" in this announcement means the territory, subject matter, use, and term expressly defined in the final license agreement. Actual rights are governed by the signed agreement.

## 4. Paid Strategic Technical Evaluation

### 4.1 Evaluation Fee

Strategic Technical Evaluation Fee: USD 5,000,000,000 (five billion United States dollars).

Non-refundable evaluation fee. This fee is a condition of participation in strategic technical evaluation. It is not a trial fee, a single demonstration fee, or a general consulting quote. Restricted technical disclosure and packaged black-box on-site demonstration do not begin until full payment is received.

### 4.2 Payment and Effectiveness

- An evaluation agreement must be signed before payment, stating scope, delivery, period, disclosure boundaries, and use restrictions.
- Full payment within five business days after the agreement is signed. Effectiveness is based on actual receipt into the designated account and confirmation of availability.
- The base currency is USD. Applicants may also pay in equivalent amounts of other major international currencies, with exchange rates based on internationally recognized rates on the date of payment. Specific currency, exchange rate benchmarks, and transfer fees shall be governed by the evaluation agreement.

### 4.3 Non-Refund and Credit

The evaluation fee is not refunded based on evaluation results, internal decisions, failure to reach a final transaction, or withdrawal by the applicant.

If a global exclusive license agreement is ultimately signed, the paid evaluation fee may be credited against the license consideration as expressly stated in that agreement. Until so stated, full or automatic credit is not presumed.

Non-refund does not relieve the company of demonstration obligations under the evaluation agreement, and does not exclude liability that applicable law does not allow to be excluded.

### 4.4 The Evaluation Fee Does Not Include

- Exclusive rights, global or regional.
- Commercial deployment, operation, or mass production.
- Delivery of the software prototype. Prototype delivery occurs only after a global exclusive license is signed and paid, under the license agreement.
- Core source code, full know-how, executables, scripts, task packages, the package itself, or a restorable package.
- Transfer of intellectual property ownership.
- Sublicensing.
- Unverified hardware performance, production results, or revenue guarantees.
- A right to require the company to complete a final transaction.

## 5. Content of the Paid Evaluation

Actual items are confirmed item by item in the evaluation agreement. The current deliverable scope is as follows.

- Technical briefing and meetings: architecture, task modules, existing verification results.
- Controlled technical disclosure: technical information not yet public, within the agreed scope. No takeaway implementation.
- Packaged black-box on-site demonstration of the software prototype: execution of agreed tasks and data in a company-controlled packaged environment. The raw prototype is not placed on site.
- Designated black-box verification: agreed tasks are demonstrated on site in a company-controlled packaged execution environment. The counterparty observes inputs, execution, and signature results, and may verify with the public key. The packaged environment is recovered after the demonstration. Executables, scripts, task packages, and the package itself are not delivered. Packaging is to prevent on-site acquisition of the raw implementation; it is not irreversible protection. Packaging Python into an executable is not a delivery method.
- Architecture and module explanation: fixed core, composable task modules, selected configuration — not every chip carrying every task.
- Software-to-hardware translation path discussion: algorithm optimization, code conversion, FPGA/ASIC direction. Latency, power, and area are not claimed as measured POC results.
- Industry and subsequent R&D discussion: applicable scenarios and R&D planning.

Where lawful, feasible, and separately agreed in writing, the paid evaluation may include the following registered tasks:

- `drone_swarm_flocking`: drone swarm coordination, including DRAGOON multi-formation mode.
- `tactical_swarm_defense_separate`: separate tactical defense. Radar-side WTA + Laser, plus drone-side DRAGOON.
- `weapon_target_assignment`: weapon-target assignment.
- `adaptive_optics_laser_defense`: adaptive optics laser defense.

These four are shown only in the paid evaluation, as packaged black-box on-site demonstrations within the agreement scope. They are not public product SKUs, and do not constitute certification or a deployed system. The agreement uses task keys, not spoken aliases. Items without a signature package or not written into the agreement are not included in the evaluation fee.

The evaluation agreement shall state start and end, number of sessions, test data, environment, on-site viewing scope, applicant cooperation, personnel who may be present, data retention, and close-out. Items not written into the agreement are not included in the evaluation fee.

The applicant may provide permitted written materials to necessary internal personnel within the agreement scope. Unless previously agreed in writing, materials may not be uploaded to third-party AI, cloud, or external models, may not be provided to unauthorized third parties, and may not be used for product development or competitive implementation outside the evaluation purpose.

What may be taken away is limited to the public key and the signature verification result of that session. The core, task implementation, executables, scripts, and package do not leave the company.

## 6. Multi-Party Evaluation and Competitive Licensing Negotiations

The company does not preset a global exclusive evaluation right. First contact, first signature, first payment, or first quote does not automatically confer priority.

Within confidentiality and the scope of any existing effective exclusivity agreement, the company may accept paid evaluations from multiple qualified enterprises at the same time, and conduct multi-party negotiations.

Comparison items may include: upfront and license consideration, payment capacity, R&D and hardwarization capability, global deployment, confidentiality and security, breach liability, and performance assurance.

The company reserves the right to choose the counterparty and terms. Paid evaluation or entry into negotiations does not create priority and does not guarantee a deal. Identities, quotes, and technical materials of the parties are confidential under the agreement.

## 7. Time-Limited Exclusivity

The company does not publish a fixed exclusivity price list. Paying the evaluation fee or entering negotiations does not automatically stop contact with other enterprises.

If an individual enterprise requires time-limited exclusivity, a separate written agreement is required, stating consideration, period, scope, mutual obligations, breach, and arrangements after expiry. Without a signed and effective exclusivity agreement, there is no exclusivity. When the exclusivity period expires without a final license, and without a valid extension, the company may resume other evaluations and negotiations.

## 8. Start of Formal Licensing Negotiations and CEO Personal Signature

Formal entry into negotiations requires all of the following:

- Paid evaluation qualification completed and full payment received.
- Participation in the agreed technical briefing and packaged black-box on-site demonstration.
- Clear expression of intent to conduct substantive negotiations for a global exclusive license.
- Personal signature by the counterparty's CEO on the "Confirmation of Start of Global Exclusive License Negotiations."

The confirmation shall state company identity, transaction intent, negotiation scope, contact window, and the CEO's signing authority. The company may require registration and authority proof. A general employee or project lead may not substitute for the CEO.

Entry into negotiations does not mean final terms have been accepted, and does not mean a transaction will necessarily close.

## 9. Final Acceptance Deadline and Exceptions for Existing Cases

Deadline: 31 December 2026, 23:59 (Taiwan time, UTC+8).

A. Cases that have formally entered substantive negotiations under Article 8 before the deadline may continue to close or termination, and are not automatically ended by the close of new applications.

B. Cases that have signed an evaluation agreement and whose evaluation fee has been fully received before the deadline may complete the evaluation under the original agreement. After completing the evaluation, briefing, and packaged black-box demonstration, and after the CEO signs the confirmation, they may enter negotiations after the deadline. This exception does not apply to new applications after the deadline or to those who have not completed payment.

C. After the deadline, no new applications are accepted, and the window is not reopened. Existing cases are handled under A and B. After existing cases are completed or terminated, the company formally ends this global licensing program.

## 10. Contact and Technical Verification

Issued by: Quantum Alpha Technology Co., Ltd.

Contact: jahua@quantum-alpha.tech

Public verification: https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC

Public items include Seed=42, Ed25519 signatures, 47+ task types, and SteinLib and CVRPLIB A/B. The actual verifiable scope is as stated in the public documents.

This announcement describes commercial positioning, paid evaluation conditions, and negotiation procedure. Actual rights are governed by the contracts signed by the parties.

Quantum Alpha Technology Co., Ltd.

---

# QαT OPU 全球獨家授權｜最終窗口公告

**公告發布單位：** 量子阿爾法科技有限公司（Quantum Alpha Technology Co., Ltd.）

## 一、技術架構與核心價值

單一核心、多任務、可擴展。

QαT 基於單一通用核心運作。任務完成後，核心即可切換至下一任務，無須重啟、重構或重新載入核心。此能力已在公開 POC 的 47+ 種 NP-hard 問題類型上驗證。47+ 是驗證覆蓋，不是架構上限，也不是每類問題都已證明數學全域最優。

QαT 並非 47 個彼此獨立的求解器，而是以單一核心搭配可組合的任務模組。核心固定，任務可組合。未來硬體映射預定實作選定組態（核心 + 所需模組），不是把每個已驗證任務都放進每一顆晶片。組態改變仍可能需要硬體合成，這不等於重設計核心搜尋架構。

同一核心可支援並聯複製與串聯管線，以探索不同的吞吐量擴展方式。多晶片延遲、功耗、面積及矽片級效能，於實際硬體實作階段量測，不列為目前 POC 成果。

公開成績以 SteinLib B+C 38/38、其中 4 個官方最優，以及 CVRPLIB A+B 50/50 的 POC 基準為主。固定 Seed=42，結果以 SHA-256 + Ed25519 簽章。完整架構、任務覆蓋與驗證方式見公開儲存庫 README 與相關文件。

公司願意在評估協議範圍內，拿出 QαT 原型以封裝黑盒現場展示供評估。對方支付評估費，換取的是對既有實作與驗證基準的受控檢視，不是帶走核心或實作，也不是收益保證。後續優化、任務擴展與硬體轉譯，可以此基準為座標。是否值得，由對方自行判斷。全球獨家授權簽約並完成付款後，依授權契約交付軟體原型。交付範圍、版本與後續支援，以該契約為準。

## 一之一、OPU 相容介面定義權

取得全球獨家授權之被授權方，得依授權契約定義 OPU 相容介面標準（OPU Compatible Interface Standard）。

此權利使被授權方得以定義 AI 與物理世界之間的確定性決策協同標準，涵蓋但不限於：

- 中央處理器（CPU）與 OPU 之協同運作規範
- 圖形處理器（GPU）與 OPU 之協同運作規範
- AI 加速器與 OPU 之確定性裁決介面
- 具身智能（Embodied AI）邊緣運算裝置與 OPU 之整合規範

被授權方得依授權契約，就上述相容標準進行定義、認證、授權及收費。相容標準之具體範圍、認證程序、授權條件與費用結構，以全球獨家授權契約為準。

取得全球獨家授權並完成付款後，被授權方將依授權契約取得軟體原型，據此開展硬體化（含 FPGA 驗證與 ASIC 流片）、量產、產業部署，以及本條所述之相容介面標準定義。

本條所述權利，構成全球獨家授權之核心商業價值之一，與 OPU 硬體化、量產及部署權利並列。實際權利範圍以最終簽署的授權契約為準。本公告不主張 OPU 硬體已完成量產或已部署。

## 二、公開驗證、技術所有權與商業權利

公開 POC 供檢視既有實作、測試結果與驗證基礎。公開可驗證，不代表公開核心。取得評估權，不代表取得商業授權、核心原始碼或技術移轉。

任何商業部署、商業使用、量產、再授權或核心技術移轉，均須另行書面授權。公開程式與第三方套件依其原有權利處理。本公告不主張超出公司實際擁有或可授權範圍的權利。

## 三、全球獨家授權最終申請窗口

最終截止時間：2026 年 12 月 31 日 23:59（台灣時間 UTC+8）。

截止後，不再接受新的授權談判申請，亦不重新開放申請。截止日前已正式進入實質授權談判的案件，以及已簽約且評估費實際到帳的既有付費評估案件，依第九條例外處理。此為公司對本計畫的最終決策。

本公告所稱全球獨家授權，指正式授權契約明確約定的地域、標的、用途與期間。實際權利範圍以最終簽署的契約為準。

## 四、付費戰略技術評估

### 4.1 評估費用

Strategic Technical Evaluation Fee：USD 5,000,000,000（美金五十億美元）。

非退還評估費。此費用是戰略技術評估的參與條件，不是試用費、單次展示費或一般顧問報價。未全額付款，不開始受限技術揭露或封裝黑盒現場展示。

### 4.2 付款與生效

- 付款前先簽署評估協議，載明範圍、交付、期間、揭露邊界與使用限制。
- 協議簽署後五個營業日內全額付款。以指定帳戶實際到帳並確認可支配為準。
- 基準幣別為美元。申請方亦得以等值之其他主要國際貨幣支付，匯率以付款日國際公認匯率為準。具體幣別、匯率基準與匯費，依評估協議約定。

### 4.3 非退還與抵扣

評估費不因評估結果、內部決議、未達最終交易或申請方退出而退還。

若最終簽署全球獨家授權契約，已付評估費得依該契約明文約定抵扣授權款。契約未明定前，不推定可全額或自動抵扣。

非退還不免除公司依評估協議應履行的展示義務，也不排除適用法律不得排除的責任。

### 4.4 評估費不包含

- 全球或任何地域的獨家權利。
- 商業部署、營運或量產。
- 軟體原型交付。原型交付僅發生於全球獨家授權簽約並完成付款之後，依授權契約辦理。
- 核心原始碼、完整技術訣竅、執行檔、腳本、任務包、封裝本體或可還原封裝。
- 智慧財產權所有權移轉。
- 再授權。
- 未實際驗證的硬體效能、量產成果或收益保證。
- 要求公司必須完成最終交易的權利。

## 五、付費評估的內容

實際項目以評估協議逐項確認。現階段可交付範圍如下。

- 技術簡報與面談：架構、任務模組、既有驗證結果。
- 受控技術揭露：協議範圍內、尚未公開的技術資訊。不交付可帶走的實作。
- 軟體原型封裝黑盒現場展示：於公司控制的封裝執行環境，依約定任務與資料執行。原始原型不放置於現場。
- 指定黑盒驗證：以公司控制的封裝執行環境現場展示協議指定任務。對方觀看輸入、執行與簽章結果，並可用公開金鑰核對。封裝環境於展示結束後收回，不交付執行檔、腳本、任務包或封裝本體。封裝用於防止現場取得原始實作，不作為不可還原的保護。Python 封裝成執行檔不作為交付方式。
- 架構與模組說明：核心固定、任務模組可組合、選定組態，不是每顆晶片承載全部任務。
- 軟硬體轉譯路徑討論：演算法優化、程式轉換、FPGA／ASIC 方向。延遲、功耗、面積不作為 POC 已量測成果。
- 產業與後續研發討論：適用情境與研發規劃。

在合法、可行且雙方另有書面同意時，付費評估得包含下列已註冊任務：

- `drone_swarm_flocking`：無人機群集協調。含 DRAGOON 多編隊模式（龍騎兵）。
- `tactical_swarm_defense_separate`：分離式戰術防禦。雷達端 WTA＋Laser，加上無人機端 DRAGOON。
- `weapon_target_assignment`：武器－目標分配。
- `adaptive_optics_laser_defense`：自適應光學雷射防禦。

此四項僅於付費評估中、依協議範圍以封裝黑盒現場展示，不列為公開產品料號，亦不構成認證或已部署系統。協議中寫任務鍵，不寫口語別名。未簽章、未寫入協議的，不算在評估費內。

評估協議應載明起迄、次數、測試資料、環境、現場觀看範圍、申請方配合事項、可接觸人員、資料保留與結案。未寫入協議的，不算在評估費內。

申請方得在協議範圍內，將允許的書面資料提供給內部必要人員。除事先書面同意外，不得上傳至第三方 AI、雲端或外部模型，不得提供給未授權第三方，不得用於評估目的以外的產品開發或競爭性實作。

可帶走的限於公開金鑰與當次簽章核對結果。核心、任務實作、執行檔、腳本與封裝本體不出公司。

## 六、多方評估與競爭性授權談判

公司不預設全球獨家評估權。不因最先聯繫、最先簽約、最先付款或最先報價而自動給予優先授權。

在保密與既有有效排他協議範圍內，公司得同時接受多家合格企業的付費評估，並進行多方談判。

比較項目得包括：預付款與授權金、付款能力、研發與硬體化能力、全球部署、保密與資安、違約責任與履約保障。

公司保留選擇交易對象與條件的權利。付費評估或進入談判，不構成優先權，也不保證成交。各方身分、報價與技術資料依協議保密。

## 七、限期排他權

公司不設固定排他價目表。支付評估費或進入談判，不自動停止與其他企業接觸。

個別企業如要求限期排他，須另行簽署書面協議，載明對價、期間、範圍、雙方義務、違約與期滿後恢復安排。沒有已簽署且生效的排他協議，就不構成排他權。排他期滿且未完成最終授權、亦未有效延長時，公司得恢復其他評估與談判。

## 八、正式授權談判的啟動與 CEO 親自簽署

正式進入談判須同時符合：

- 已完成付費評估資格及全額付款。
- 已參與約定的技術簡報與封裝黑盒現場展示。
- 已明確表示有意就全球獨家授權進行實質談判。
- 已由對方公司 CEO 親自簽署《全球獨家授權談判啟動確認書》。

確認書應載明公司身分、交易意向、談判範圍、聯絡窗口，以及 CEO 的簽署權限。公司得要求登記與授權證明。不接受一般員工或專案負責人取代 CEO 簽署。

進入談判不代表已接受最終條款，也不代表交易必然成立。

## 九、最終受理期限與既有案件例外

截止時間：2026 年 12 月 31 日 23:59（台灣時間 UTC+8）。

A. 截止前已依第八條正式進入實質談判的案件，得繼續至成交或終止，不因新申請截止而自動結束。

B. 截止前已簽署評估協議且評估費全額實際到帳的案件，得依原協議完成評估。完成評估、簡報與封裝黑盒現場展示，並由 CEO 簽署確認書後，得於截止後進入談判。此例外不適用於截止後的新申請或未完成付款者。

C. 截止後不再接受新申請，亦不重新開放。既有案件依 A、B 處理。既有案件完成或終止後，公司正式結束本全球授權計畫。

## 十、聯繫與技術驗證

公告單位：量子阿爾法科技有限公司（Quantum Alpha Technology Co., Ltd.）

聯絡：jahua@quantum-alpha.tech

公開驗證：https://github.com/Quantumalphatech/Universal-Optimization-Engine-POC

公開項目包括 Seed=42、Ed25519 簽章、47+ 任務類型，以及 SteinLib 與 CVRPLIB A/B。實際可驗證範圍以公開文件為準。

本公告說明商業定位、付費評估條件與談判程序。實際權利以雙方簽署的契約為準。

量子阿爾法科技有限公司
