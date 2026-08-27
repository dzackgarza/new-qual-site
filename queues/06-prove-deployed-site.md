# Queue 6: Prove the deployed site

Source: `TODO.md` §4 "Prove the deployed site"
Owner: [issue #30](https://github.com/dzackgarza/new-qual-site/issues/30) (COMPLETED 2026-08-26)

## Open items

- [ ] 6.1 Verify the route and catalog manifests.
- [ ] 6.2 Visit every subject branch root and terminal route.
- [ ] 6.3 Exercise search, filters, disclosures, diagrams, citations, and generation.
- [ ] 6.4 Inspect widths of 375, 768, 1024, and 1440 CSS pixels.
- [ ] 6.5 Inspect browser console and network results.
- [ ] 6.6 Confirm that local and deployed artifacts use the same revision.
- [ ] 6.7 Record every unexercised path and nonclaim.

## Verification (2026-08-27)

Issue #30 closed COMPLETED: "The complete site is published through GitHub Pages. Later defects belong to their affected reader or content surface." It was reopened once ("prior closure did not verify this issue against the current repository and rendered artifact") then re-closed.

`DESIGN_TODO.md` (2026-08-27) IS a rendered verification, performed after the re-closure. It found:
- Defects visible at 540px and 1440px and 375px (items 6.4 not done — the inspection happened and found width-dependent defects).
- Search has no ranking (defect 24) — item 6.3 (exercise search) not done.
- 25 defects total — item 6.7 (record every unexercised path and nonclaim) not done.

Items 6.1, 6.2, 6.5, 6.6 unverified against current build.