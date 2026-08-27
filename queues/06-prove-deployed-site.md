# Queue 6: Prove the deployed site

Source: `TODO.md` §4 "Prove the deployed site"
Owner: [issue #30](https://github.com/dzackgarza/new-qual-site/issues/30) (COMPLETED 2026-08-26)

## Open items

- [ ] 6.1 Verify the route and catalog manifests.
  - Validity: UNVERIFIED. Build directory has no wiki pages to verify routes against. `build/quarto/_site/` has `tag/` (8812 card pages) but no `wiki/` directory.

- [ ] 6.2 Visit every subject branch root and terminal route.
  - Validity: NOT DONE. No wiki pages in build to visit.

- [ ] 6.3 Exercise search, filters, disclosures, diagrams, citations, and generation.
  - Validity: PARTIALLY DONE. `DESIGN_TODO.md` exercised search (defect 24: no ranking — though a fix exists in working tree) and disclosures (defects 1, 2). Diagrams, citations, generation not exercised against a live build.

- [ ] 6.4 Inspect widths of 375, 768, 1024, and 1440 CSS pixels.
  - Validity: PARTIALLY DONE. `DESIGN_TODO.md` rendered at 540/1440/375px and found width-dependent defects (defect 10: measure too wide, defect 18: TOC disappears below 1024px, defect 22: sticky header ghosting). The four-width sweep was done; defects remain.

- [ ] 6.5 Inspect browser console and network results.
  - Validity: NOT DONE. `DESIGN_TODO.md` does not record console or network inspection.

- [ ] 6.6 Confirm that local and deployed artifacts use the same revision.
  - Validity: NOT DONE. No evidence of local-vs-deployed comparison in issue comments.

- [ ] 6.7 Record every unexercised path and nonclaim.
  - Validity: NOT DONE. `DESIGN_TODO.md` records 25 defects but does not enumerate unexercised paths or nonclaims.

## Verification (2026-08-27)

Issue #30 closed COMPLETED: "The complete site is published through GitHub Pages." Reopened once ("prior closure did not verify this issue against the current repository and rendered artifact") then re-closed.

`DESIGN_TODO.md` IS a rendered verification, performed after the re-closure. It found 25 defects. The current build directory has no wiki pages — the build is stale or was cleaned. Items 6.1, 6.2, 6.5, 6.6, 6.7 need a rebuild and inspection to verify.