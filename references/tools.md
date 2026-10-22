# 工具与运行约定

以本 skill 真实目录为 `SKILL_ROOT`，命令中的变量由助手解析；不依赖 HERMES_SKILL_DIR、原 WorkBuddy 安装路径或某机器的已装库。正常方法指导只需读 Markdown。

## 新统一入口

`python3 "$SKILL_ROOT/scripts/project.py" init <新目录> --title <题名> [--profile longform] [--date YYYY-MM-DD]`

创建轻量项目/长篇附加模板，拒绝覆盖非空目录。

`python3 "$SKILL_ROOT/scripts/project.py" audit <正文.md> [--registry <sources.json>] [--final] [--check-files] [--format json]`

只读检查 Markdown 脚注引用/定义、重复/无主定义、占位、稳定来源号、当前用途登记与可选文件哈希。支持 N key→S 来源映射，不能证明实体法/文献真实性或语义支持。退出码 0=未发现所检查问题，1=发现问题，2=输入/格式错误；`--final` 增加严格登记门槛，但仍不等于最终学术验收。

`python3 "$SKILL_ROOT/scripts/toolbox.py" <任务> ...`

包装所附原脚本，生成类任务拒绝覆盖；修改类先复制到新目标再执行，读取不改原稿。选择命令前查看 `--help`。下列是封装过的常用任务：

| 子命令 | 作用 | 输出/依赖/注意 |
|---|---|---|
| parse-cnki | RefWorks/EndNote→TSV | `输入... --out 新.tsv`；标准库，元数据未自动核验 |
| format-refs | TSV→law/gbt 工作条目 | `输入 --out 新.md --style law/gbt`；保留已有字段，不补观点页 |
| validate-refs | 脚注或顺序编号结构检查 | `稿件 --mode auto/footnote/journal`；原 S09 数字键约束见下 |
| health | 冗余/长句/版本体检 | `稿件...`；只作诊断线索 |
| language-signals | 原词表式表达扫描 | `稿件`；不等于 AI 来源鉴定，原稿体裁偏好不作门禁 |
| privacy | 文件/目录线索扫描 | `目录`；须人工判断是否真是身份信息 |
| normalize | 标点转换 | `稿件 --out 新.md`；先读原脚本规则；引用、外文和 URL 复核 |
| renumber | 数字式文末参考文献重排 | `稿件 --out 新.md`；仅 `[n]` 格式，不能用于 N/S 稳定键 |
| review-packet | 总包审稿副本与任务书 | `稿件 --out 新目录 [--round 1] [--anonymize]`；保留显式与注释内待核，人工检查匿名 |
| docx | Markdown→Word | `稿件 --out 新.docx --profile footnote/journal`；总包独立实现，python-docx+lxml；不自动改标点 |
| pdf-text | PDF→分页文本 | `文件/目录... --out 新目录`；PyMuPDF 或 pypdf，可提示 OCR |
| structure-check | 真实目录节点变化检查 | `案例.json`；标准库，不判断实体法或语义 |
| legal-signals | 原 S04 正则检查 | `稿件`；旧法/术语/缺口提示不是当前法源验证 |

完整语法以封装 `--help` 为准。新统一脚注审查与导出支持 `[^N001]`；原 S09 `validate-refs --mode footnote` 主要按数字脚注实现，N key 稿优先 project audit。总包新导出器处理标题、简单段落/表格、粗体斜体与稳定脚注 key；复杂图片、代码、公式等拒绝转换以免静默丢失。外部链接输出为标签加网址，脚注定义内部的复杂富文本不作无损排版承诺。

`docx --cn-font "字体名"` 可指定课程要求且当次已安装的中文字体；默认 macOS 用 Songti SC，其他平台用 SimSun，仅作工作参数，仍须渲染。`structure-check` 以实际 accepted 结果设退出码，不把原测试夹具的“预期失败得到验证”混成“修改方案被接受”。

## 深度工具的保留与边界

原脚本在 `references/source-library/` 逐套保留，不在无关任务自动运行。S01：草案引用转换与测试。S04：阶段清单、正则审稿。S06：目录提取、词汇表构建、静态语料导出、结构声明校验。S08：原生专著初始化/校验/剥离/图表/合并。S09：题录/PDF/格式/编号/健康/标点/隐私/审稿包/真脚注 Word。原作者维护测试也保留；只有实际运行并记入验收报告的，才声称测试通过。

深度脚本使用前读代码、头部、参数与输入 schema，特别检查写入/覆盖/重建目录及路径。先在副本/临时目录试跑；不要对真实论文直接用 `--force`、删除未引用文献或清待核。S08 用独立原格式见 longform.md，不能直接套总项目模板。

## 结构语料

S06 静态路由不需要 Python。语料重建才读 extract_toc/build_toc_vocabulary；HTML/DOCX层级可提供结构依据，PDF/TXT启发式提取必须人工复核，不根据编号外观虚报 A1/A2 阅读量。词频的分母、去重和来源级别分开。`export_public_data.py` 是维护工具，不自动导出用户论文。

## 依赖与失败

标准库足够初始化/统一审核和多数文本工具。PDF/Word/图表依赖当次检查；Codex 优先发现 bundled runtime，不在调用 skill 时自动安装整套环境。无依赖可给中间 Markdown、结构化 TSV 与缺口清单，不虚称完成文件转换。Word 生成后另做结构与视觉验收，见 delivery.md。
