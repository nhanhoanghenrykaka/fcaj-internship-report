# FCAJ Internship Report — Shopsflow

This Hugo project contains the bilingual internship report for the Shopsflow AWS deployment.

## Main corrections

- Part 2 contains one architecture diagram instead of four repeated diagrams.
- Part 5 contains one screenshot for each distinct AWS resource or configuration step.
- Duplicate copies from the reference-report folders were removed.
- Markdown images are rendered with Hugo `relURL`, so GitHub Pages automatically uses the actual repository subpath.
- Home-page and event images use the `report-image` shortcode for the same reason.
- GitHub Actions checks every generated local image path before publishing the site.

## Run locally

```bash
hugo server -D
```

## Deploy

Push the project contents to the `main` branch. The workflow in `.github/workflows/hugo.yml` builds and publishes the `public` directory with GitHub Pages.
