# 发布版验证记录

版本：1.0.1 · 日期：2026-10-22 · 维护：lyyrebecca · 微信：shirebeccaha。

## 当前已执行

| 检查 | 结果 | 说明 |
|---|---|---|
| 技能格式校验 | PASS | name、description、YAML frontmatter 与技能命名通过本地 quick_validate |
| 总工作流回归 | 30 / 30 PASS；0 skipped | macOS，Python 3.9.6；含 python-docx / lxml 的实际 DOCX 测试 |
| Python 源码解析 | 33 个文件 PASS | 总入口和内置参考脚本均可解析；不表示每个深度工具已执行 |
| 发布文件与来源哈希 | PASS | 由 scripts/check_release.py 检查 SHA-256、字节数和文件集合 |
| 身份清理机械复查 | PASS | 检查已知历史账号、个人绝对路径、安装/商店元数据及重复 .skill 归档 |
| 唯一技能入口 | PASS | 根目录只有一个名为 SKILL.md 的发现入口 |

## 回归实际覆盖

1. 课程与长篇项目初始化，非空目录防覆盖。
2. 来源表格式、稳定来源身份、用途登记、精确位置与核验状态。
3. 缺失/重复/无主脚注、代码块内示例、占位与待核标记保留。
4. 法源版本字段、案例身份字段、文件内容漂移。
5. 多条题录去重、标点副本、参考文献重排不改原稿。
6. DOCX 正文与表内真实脚注的 OpenXML 结构及存在性。
7. 不适用格式拒绝转换，避免脚注静默丢失。
8. 审稿任务包保留待核，匿名版清理显式身份字段而不删除学术姓名。
9. 结构变化契约，拒绝把只换词宣称为真实重构。
10. 十组发布版参考资料的文件完整性与哈希。

## 可重现

```bash
python3 -m pip install -r requirements-docx.txt
python3 scripts/test_workflow.py
python3 scripts/check_release.py
```

`.github/workflows/validate.yml` 在 Python 3.11 / 3.12 上自动运行总回归与发布检查，具体云端状态以 GitHub Actions 为准。修改发布文件后应先重建清单，再复验：

```bash
python3 scripts/build_manifests.py
python3 scripts/test_workflow.py
python3 scripts/check_release.py
```

## 未评估或不能据此推断

- 未用真实完整论文做独立法学专家盲评，没有成绩、录用率或效果提升统计。
- 未逐条在线核查来源资料中全部法条、案例、论文或期刊信息。
- 未执行全部上游深度脚本，也未验收每一种客户端。
- 本次 Word 测试检查文件结构，不包含论文级 Word/PDF 逐页视觉验收。
- 隐私复查是可重现的已知特征扫描加人工检视，不宣称能发现所有隐含身份。
- 测试不验证第三方授权；版权和许可范围见 THIRD_PARTY_NOTICES.md。
