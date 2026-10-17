# TruLeaf Landscapes — static site

A plain static website: HTML, one CSS file, local images, local fonts. No build
step, no framework, no database, no JavaScript framework. It can be dropped onto
any static host (GitHub Pages, Netlify, Cloudflare Pages, an S3 bucket) and it
will work.

This is the production version of the design POC in `../design-poc/`. The POC was
a single inlined file with base64 images so it could be handed over as one
artifact; that is not how a site that gets edited every week should be built.
Everything here is a separate file.

---

## File layout

```
site/
├── index.html                    Home page
├── lawn-mowing-lawn-care.html    Service page (Lawn Mowing & Lawn Care)
├── styles.css                    ALL styles for the whole site
├── README.md                     This file
└── assets/
    ├── logo-header.png           Logo for the header (deep-teal background baked in)
    ├── logo-footer.png           Logo for the footer (dark-teal background baked in)
    ├── emblem.jpg                Small mark — favicon
    ├── logo-transparent.png      Transparent logo, spare
    ├── fonts/
    │   ├── spectral-400.woff2
    │   ├── spectral-500.woff2
    │   ├── spectral-600.woff2     ← headings use this
    │   ├── spectral-700.woff2
    │   ├── libre-franklin-var.woff2      (variable, weights 300–800)
    │   └── libre-franklin-400-italic.woff2
    └── img/                      Real job photography only
        ├── hero-bush-retreat.jpg
        ├── lawn-mowing.jpg
        ├── garden-maintenance.jpg
        ├── hedging-pruning.jpg
        ├── garden-design-turf.jpg
        ├── retaining-walls-paving.jpg
        ├── property-cleanups.jpg
        ├── area-kangaroo-valley.jpg
        ├── area-shoalhaven.jpg
        ├── work-wide.jpg
        ├── work-tall.jpg
        ├── work-lawn-hedge.jpg
        ├── work-lawn.jpg
        ├── work-driveway.jpg
        └── work-before.jpg
```

**There are no other files.** No minified copies, no `dist/`, no source maps.
What you see is what ships.

---

## Editing the site

### Change a word
Open the `.html` file, find the sentence, change it. Save. That is the whole job.
Every sentence on the page is visible in the HTML — nothing is hidden in a
template or generated at runtime.

### Change a photo
1. Put the new image in `assets/img/`.
2. Give it a short lowercase name with hyphens, e.g. `my-new-job.jpg`.
3. Find the `<img src="assets/img/...">` you are replacing and change the `src`.
4. **Update the `alt` text.** Every image needs alt text that says what the photo
   actually shows. Do not leave the old alt on a new photo.
5. Update `width` and `height` to the real pixel size of the new file (open the
   image, look at its properties). These two numbers stop the page jumping around
   while it loads. They do not control how big the photo displays — CSS does that.

### Resize a photo before you upload
Photos straight off a phone are 4–12 MB each and will make the site slow. Before
putting one in `assets/img/`:

- Make it **no wider than 1600px** (1920px for the hero only).
- Save as **JPEG, quality 78–82**.
- A service card or gallery image should land around **200–400 KB**.
- The hero can be larger — around **700 KB**.

The photos currently in `assets/img/` are already done this way.

### Add a new page
Copy an existing page, rename it, and change the content. Then add a link to it
in the header (`<nav class="main-nav">`) or in the footer (`<h4>Explore</h4>`).
Keep the same header and footer block as every other page — they are identical on
purpose, so a change to the header is made once per page.

---

## Design rules — do not break these

These are the committed design system. They were decided deliberately and are not
aesthetic preferences that can be refreshed later.

### Colour
| Role | Value | Where |
|---|---|---|
| Deep teal | `#0C3D4E` | header, trust band, recent-work band |
| Footer teal | `#07202C` | footer only |
| Cool off-white | `#F2F4F2` | page background |
| Near-white | `#FAFBFA` | alternate light section |
| Tint | `#E7EEEC` | "Meet Mathew" section |
| Burnt orange | `#C2511E` | buttons + the CTA band only (hover `#A64515`) |
| Gold | `#F4D03F` | 1px rules and tiny accents only |

- **Never cream, beige or warm-white backgrounds.** The warmth comes from the
  orange accent and the photography.
- **Never near-black** (`#000`, `#050505`) as a background.
- **Gold is decoration, never emphasis.** No gold body text, no gold gradients.
- **Orange is small-area only.** The only full-width orange block is the CTA band.
- **No gradients except the hero scrim.**

### Type
- **Spectral** (serif) for all headings `h1`–`h3`.
- **Libre Franklin** (sans) for all body copy, buttons, nav, captions.
- Banned: Inter, Playfair Display, Instrument, and any lookalike. Do not swap
  these for something "similar".
- Body copy is never set in the serif. Headings are never set in the sans.
- Fonts are self-hosted in `assets/fonts/` — there is **no CDN or Google Fonts
  link**, and there must not be one.

### Motion
One scroll-reveal family only: rise 16px + fade, 550ms, gated behind a `.js`
class, disabled under `prefers-reduced-motion`. Buttons get `:active` scale(.97).
Images get the 420ms hover zoom. **No marquees, no parallax, no scroll
listeners, no auto-playing carousels, no animated counters.**

### Structure
- Sticky header: logo left, nav centre-left, phone + "Text a photo" right.
  On screens **narrower than 561px** the header call to action moves into the
  hamburger menu — there is not enough room on one 320px line for the logo, the
  menu button and a labelled button. The hero and the orange CTA band both still
  carry it, so it is never more than one tap away.
- Hero: full-bleed photograph, directional deep-teal scrim, left-weighted type.
- Services: a **3 × 3 grid of exactly nine cards**. Three are solid deep-teal
  text-only cards carrying a "Photo coming soon" tag — those are the honest
  photo gaps, not a design flourish. Do not replace them with stock photos.
- Recent work: an **asymmetric 6-column** gallery (wide + tall + row + panorama
  strip), deliberately uneven. Not a uniform bento grid.
- Section rhythm alternates: cool paper → deep teal → cool paper → tint → deep
  teal → burnt orange.
- The tagline *"Perfecting nature, one leaf at a time."* is in the **footer
  only**. Never in the header.

---

## Content rules — these are hard constraints

Breaking any of these is a defect, not a stylistic choice.

1. **No prices anywhere.** No prices, no "from $X", no rates, no hourly figures —
   not in copy, not in metadata, not in alt text, not in filenames. The business
   is quote-only.
2. **No years-of-experience claim in any form.** Not "17 years", not "18+ years",
   not "over 18 years", not "decades of experience", not a range, not an implied
   duration. Not in a heading, not in body copy, not in metadata, not in alt text.
   **No exceptions.**
3. **No solo-operator language.** Never "no subcontractors", "one person",
   "I do everything myself". The business is hiring. Write in **first-person
   plural ("we")** everywhere except the **"Meet Mathew"** section, which is the
   only first-person ("I") section on the site.
4. **No enquiry, contact or quote form.** Not a form, not an embedded form, not
   a "request a quote" box. The only call to action is **"Text a photo"**, linking
   to `sms:0423325989`. Phone shows as **0423 325 989**.
5. **No reviews, testimonials, ratings, star scores or "what clients say".**
6. **No photographs of Mathew's son.** The "Meet Mathew" portrait slot is a
   marked placeholder. Do not put another photo in it, and do not put a child in
   it.
7. **Never publish:** anything about the Friendly Inn, Pete Thomson, the paving
   job rate, how the business started, former business names, or Mathew's
   personal history. That material is private background. It shapes strategy; it
   never appears in output.
8. **Do not invent.** No client names, no job counts, no statistics, no awards,
   no certifications, no team members, no "trusted by" logos, no memberships.
   If a fact cannot be traced to something real, leave it out.
9. **Real job photography only.** Every image in `assets/img/` is a real TruLeaf
   job. If a service genuinely has no photo, it gets the "Photo coming soon"
   treatment. **Never substitute stock imagery.**
10. **Shoalhaven is not a typo.** Kangaroo Valley is inside the Shoalhaven
    region. Both terms stay.

### The voice
Copy is written in Mathew's voice, and it has to stay that way. The rules:

- **Long, claused sentences** joined by *and*, *so*, *because*. He rarely stops
  at a full stop. A short punchy rewrite would be wrong.
- **Plain tradesperson register.** No hype, no ceremony, no marketing language.
- **Concrete specifics over abstractions.** Exact details, plain words.
- **He is honest about his own limits**, and that reads as trustworthy. Copy that
  admits a boundary is stronger than copy that claims everything.
- **Never:** "passionate about", "committed to", "dedicated to", "your trusted",
  "transforming outdoor spaces", "bring your vision to life", "one team for the
  whole property", "with years of experience", exclamation marks, or any attempt
  at enthusiasm.
- **No sentence should be able to appear unchanged on a competitor's site.** If
  it could, it is filler.

---

## Contact details used on the site

| What | Value |
|---|---|
| Business | TruLeaf Landscapes |
| Owner | Mathew McLean |
| Location | Kangaroo Valley, NSW |
| Service area | Kangaroo Valley and the wider Shoalhaven region |
| Phone | `0423 325 989` displayed · `tel:0423325989` in links |
| Text CTA | "Text a photo" → `sms:0423325989` |
| Email | mathew.gardensolutions@gmail.com |
| Privacy | https://www.truleaflandscapes.com/about-4 |

**`/about-4` is frozen.** It is the registered privacy policy URL for the
TruLeaf Jobs Google Calendar app. Do not rename or move it.

---

## Deploying

Because it is plain static files, any static host works.

**GitHub Pages** (what this is set up for): push the `site/` folder's contents to
the repo root or a `docs/` folder, enable Pages, done. Atlas handles deployment —
do not push from here.

No environment variables, no API keys, no secrets, no server-side code. Nothing
in this folder needs to be kept private except the source photographs, and even
those are already public on the live site.

---

## Known open items

1. **The "Meet Mathew" portrait is still a placeholder.** Mathew is supplying
   the photograph. The slot is sized and marked for it — when the real photo
   arrives, drop it in as `assets/img/mathew.jpg`, replace the
   `.about-photo--placeholder` block in `index.html` with a normal
   `<img>`, and keep the figcaption.
2. **Three services have no photograph yet** (Irrigation & Drainage, Ponds &
   Water Features, Stump Grinding). They correctly show the "Photo coming soon"
   tag. Do not fill them with stock images — wait for real job photos.
3. **The header and footer logos have their background colour baked in.**
   `logo-header.png` is keyed to `#0C3D4E` (the header) and `logo-footer.png` to
   `#07202C` (the footer). They will look seamless as long as those two colours
   do not change. If the header or footer colour is ever changed, the logos must
   be re-keyed, or swapped for `logo-transparent.png`.
4. **Every photograph was audited for competitor branding before use.** This
   matters more than it sounds. Three photos in the approved set were rejected
   because they show **another company's branded vehicle** in frame — a white
   van reading "Clancy's" (photo 077), a ute reading "DAIKIN / PROFIXAIR
   SOLUTIONS" (photo 045), and a venue signpost reading "CATHEDRAL / OFFICE"
   (photo 082). A client's own skip-bin hire number (photo 027) and a mulch
   product bag (photo 035) were judged acceptable. **Before adding any new
   photograph, look at it for vehicles, signage and watermarks first** — a
   competitor's logo on the hero image is the single most damaging thing this
   site could carry, and it is invisible to a grep.
