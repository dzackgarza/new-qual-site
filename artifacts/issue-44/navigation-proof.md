# Wiki navigation proof

## Defect

The published wiki page had no hierarchy navigation.
`before-published.png` shows only page content and an `On this page` list.

## Required behavior

Every authored wiki page shows the complete wiki tree.
The tree opens the current page's ancestor directories, marks the current page, and links to other branches.

## Evidence

- `after-index-1440.png` shows the corrected wiki index with the full tree beside the page.

- `after-375.png`, `after-768.png`, `after-1024.png`, and `after-1440.png` show a nested page at each responsive breakpoint.
  Each image was inspected.
  The tree and page content remain readable without horizontal overflow.

- `after-accessibility-tree.txt` records the `Wiki` navigation region, directory disclosure controls, and page links from the rendered browser accessibility tree.

- `wiki-navigation-test.xml` records the real publication build proof.
  The test reads the emitted page and verifies the open current branch, current-page link, and cross-branch target.

- `after-navigation-trace.json.gz` is the browser navigation trace for the corrected local page.
