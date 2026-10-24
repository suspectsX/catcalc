# Illustration placeholders and product image provenance

The eight illustrations are original geometric placeholders drawn with Pillow by
`scripts/prepare_images.py`. They are intentionally simple, contain no medical
approval marks, and are not finished commissioned art. Their English alt text and
placement follow review section 3.2. The source JPG product previews remain the
original supplied assets; they are drafts and are not verified against a final PDF.

Imagegen was used solely to propose the replacement sales badge on the cover.
Prompt: Replace only “Instant download” with “Coming soon”, preserving the preview.
Because generative editing can redraw page content, **none of its rendered PDF
pages are used**. Only the badge rectangle is retained in
`scripts/assets/cover-status-label.png`; `prepare_images.py` pastes that rectangle
into the original JPG below the page content, then makes JPG/WebP derivatives.
Original `src/img/01-cover.jpg` is preserved and excluded from public assets.

Before sales, manually check the real PDFs, food-risk statements in the draft
preview, preview-to-PDF consistency, readable smaller exports, and sales/delivery
terms. No new preview pages or veterinary credentials were fabricated.
