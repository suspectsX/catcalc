# CatCalc

英文猫咪工具静态站，正式域名：[vonsoh.com](https://vonsoh.com/)。源码仓库：[suspectsX/catcalc](https://github.com/suspectsX/catcalc)。

## 页面与内容

共 **52 个常规页面 + 1 个 404**：首页、年龄计算器、热量/食量计算器、猫名生成器、食物索引、41 个食物详情、Planner 预览、About、Contact、Terms、Privacy、Refund Policy。sitemap 只收录 52 个常规页面。

- 食物页用逐项风险标签、简短结论、准备/处理建议和来源；毒性、机械伤害、营养限制和证据有限分别表达。内容未经过兽医审核，不能替代个体诊疗。
- 年龄为非临床近似换算；生命阶段定义单独引用 AAHA/AAFP。热量为 RER 起点估算，零食计入每日总量。
- Planner 目前统一为 **Coming soon / not yet available**，无购买或预订功能，Product 数据不包含 Offer。预览内页仍须与真实 PDF 和更新后的食品风险文字核对。
- FAQ 为可见内容和语义标记保留，不把富媒体展示或流量作为收益承诺。

## 构建与本地检查

生成器只使用 Python 标准库；先修改 `build.py`、`src/`，再生成 `docs/`。**构建会删除并重建整个 docs 目录，不要只编辑生成文件。**

```powershell
python build.py
python scripts/check_site.py
node --check src/tools.js
python -m http.server 8765 --directory docs --bind 127.0.0.1
```

Windows 若 `python` 不可用，用 `py -3` 或本机可用解释器的完整路径。用浏览器打开 http://127.0.0.1:8765/。

`check_site.py` 解析全部 HTML，检查唯一 title/description、H1、站内链接、JSON-LD、图片与 srcset、商品状态、sitemap 日期，并统计来自其他食物页的不同入链来源（每页至少 3 个）。另须实际操作浏览器验证输入、Enter、错误提示、窄屏和短视口。

## 图片与日期维护

响应式图片已提交，普通构建不需要 Pillow。需要重新导出时：

```powershell
python -m pip install --user pillow
python scripts/prepare_images.py
python build.py
```

- 八幅插图为简单几何占位 WebP，源文件在 `src/img/illustrations/`；首页主图为 600×300 / 1200×600，工具图为 480×270 / 960×540，按审查报告 3.2 的尺寸接入。
- 商品图为 480/800/1200 正方形 WebP，JPG 回退及原图查看入口保留。原封面 `src/img/01-cover.jpg` 保留作为源档，不复制到公开目录；只在底部销售徽标区域贴上 Coming soon，内页像素来自原 JPG。徽标来源和图片限制见 `src/img/illustrations/README.md`。
- `src/content_dates.json` 记录固定内容日期；仅实质内容修改时手动更新对应项。食物通配日期表示本次共同修订；未来单页日期可以用精确路径覆盖。缺少可靠日期时可省略 lastmod。政策条文没改就不要改日期。

## 配置与部署

`config.json` 保留站点域名、联系邮箱、AdSense 发布商 ID 和已有变现配置；本次没有修改它。AdSense 自动广告脚本保留，已取消无用的手动空广告 div。广告区域排除、地区同意管理和性能需在真实 AdSense 后台及浏览器中确认。

GitHub Pages 既定发布目录为 `main` 分支 `/docs`；自定义域名由 `config.json` 生成 `docs/CNAME`。仓库使用根相对链接，旧的 GitHub 子路径不是当前发布入口。合并和推送后由仓库配置部署；本次只在 `codex-optimize` 本地提交，不 push，不改 DNS 或证书。

项目当前状态与下一步见 [项目交接.md](项目交接.md)。
