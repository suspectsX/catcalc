# CatCalc — 猫咪工具站（英文，面向海外用户）

纯静态网站，零服务器成本。`python3 build.py` 生成到 `docs/`，GitHub Pages / Cloudflare Pages 直接托管。

## 页面（共 48 页）
- 首页、猫咪年龄换算器、猫咪热量/喂食量计算器、猫名生成器
- 「Can cats eat…?」索引 + 41 个食物详情页（程序化 SEO，含 FAQ 结构化数据）
- About、Privacy（AdSense 审核需要）、404、sitemap.xml、robots.txt

## 变现开关（编辑 config.json 后重新 `python3 build.py`）
| 字段 | 作用 |
|---|---|
| adsense_publisher_id | 填 `ca-pub-…` 后自动插入 AdSense 自动广告脚本并生成 ads.txt |
| amazon_associates_tag | 填 `xxx-20` 后工具页出现亚马逊联盟推荐 |
| digital_product_url | Gumroad/Creem/Payhip 商品链接，出现在每页底部 |
| tiktok_url / douyin_url | 页脚社媒链接 |
| google_site_verification | Search Console 验证码 |

## 部署到 GitHub Pages
1. 在 GitHub 新建公开仓库 `catcalc`（账号 suspectsX）。
2. `git remote add origin https://github.com/suspectsX/catcalc.git && git push -u origin main`
3. 仓库 Settings → Pages → Source: Deploy from a branch → `main` / `/docs` → Save。
4. 约 1 分钟后访问 https://suspectsx.github.io/catcalc/
5. 在 Google Search Console 添加站点并提交 `sitemap.xml`。
