# Illustration placeholders and product image provenance

The eight illustrations are final flat-style art featuring Pumpkin (orange tabby,
knitted pumpkin hat; palette #E8772E / #F7C99B / outline #4A3428), generated with an
image model and checked by eye for artifacts and stray text. Full-size sources live in
`scripts/assets/illustrations/<name>.jpg`; `scripts/prepare_images.py` crops them to
2:1 (home-cat-tools, 600/1200) or 16:9 (others, 480/960) and writes the WebP files
here. If a source is missing, the script falls back to a Pillow geometric placeholder. Their English alt text and
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
