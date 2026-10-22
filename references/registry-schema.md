# sources.json 输入约定

`schema_version: 1`，`sources` 与 `notes` 均为数组。编号由本项目真实资料产生；以下是字段说明，不是可直接引用的虚拟文献。

## sources 每条

- `id`：如 S001，稳定唯一来源号。
- `kind`：book/article/law/regulation/judicial_interpretation/normative_document/case/data/online 等真实类型。
- `title`、`creator`：核对后的题名与作者/机关。
- `access`：METADATA / ABSTRACT / EXCERPT / FULLTEXT。
- `status`：VERIFIED / PARTIAL / LEAD_ONLY / UNUSABLE，按当前用途人工判断，不由脚本自动升级。
- `location`：真实原文件位置或实际读取的网址。
- `verified_at`：YYYY-MM-DD，真实核验日。
- `file`、`sha256`：可选本地文件及其 SHA-256；相对路径以 sources.json 所在目录为基准。`--check-files` 才检查。
- 规范类另有 `version`、`valid_at`、`legal_identity`；案例另有 `case_number`、`court`、`decision_date`、`document_type`。

## notes 每条

- `key`：Markdown 脚注出现 key，例如 N001，不含 `[^ ]`。
- `supports`：数组，每条含 `source_id`、`locator`（当前命题精确定位）、`claim`（支持的主张）、`support_scope`（证明上限）、`support_checked`（人工确已回读相关原文才填 true）。一条脚注可对应多来源。
- 作者自己的补充推理注可用 `author_note: true` 与 `reasoning`，不应同时挂外部 supports；不能借此隐藏来源性主张。

`audit --final` 检查必需字段与登记状态；所有 “VERIFIED / support_checked” 仍是记录者的声明。脚本不能验证记录是否诚实，不能检查引文原文是否真的支持命题，不能代替人工和法源在线核验。

只含参考文献编号 `[n]` 的稿件用 toolbox 的数字式检查，而非把该 schema 自动视为现成映射。格式转换、导入题录都不自动生成 VERIFIED 状态。
