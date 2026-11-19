# What a student hits on the live Qual Corpus site: defect classes, 2026-11-19

Read in the order the task gives it: the CI corpus report (`BACKLOG.md`, `queues/`) and a
`qualc check` of the whole corpus; the rendered pages of the README's problem-list and
subject-guide links; then the reader findings of 2026-11-18 14:52Z and 16:21Z on issue #2.

Each section below is one defect class, written as it would be filed under ledger #83.
Ranked by what a student loses, highest first. The first one is repaired in this commit.

**Filing blocked:** the connected GitHub repository grants reads, branch fetch/push, PR
creation and PR labels; it does not grant issue creation, so these four filings could not be
opened as sub-issues of #83 and are recorded here instead. Nothing else about them is blocked.

---

## 1. The README's "Browse sources" link is a dead page (repaired here)

`README.md:14` points at `https://dzackgarza.github.io/new-qual-site/exams.html`. The site
renamed that page to `sources.html`; the emitter writes `sources.html`
(`tools/qualc/emit.py:2127`), the site's own navigation links `sources.html`
(`tools/qualc/static_site.py:958`), and `tests/test_static_site.py:504` asserts that
`exams.html` is *not* emitted. The README was never updated.

Measured on the live site:

- `GET /exams.html` → `404`, body "Page not found".
- `GET /sources.html` → `200`.

So the one documented entry point to all 504 source collections returns the 404 page.
Nothing checks the README, which is why it rotted.

Affected cards: none. Affected document: `README.md`.

Repaired: the link now names `sources.html`, and `tests/test_readme_links.py` fails when a
README link names a path the site does not build (routes: the four standard pages, the wiki
index, and one page per guide manifest).

---

## 2. The deployed site is stale, because any corpus diagnostic stops the build

The live site reports its own revision in `revision.txt` and in every page footer:

- `GET /revision.txt` → `b85685cd0344c953bcfcb986da99f466c9fd02b4`
- footer → "Generated 2026-11-18 11:38 UTC"

That commit is **1605 commits behind `main`**. Every repair made since 2026-11-18 11:20 is
invisible to a student: including all 29 repairs to the #2 review findings below.

The cause is the gate, not the deployer. `build` in `tools/qualc/cli.py` runs the same
`load()` as `check` and returns 1 on *any* diagnostic before it emits a page
(`tools/qualc/cli.py:181-190`), and the workflow's build step is plain `uv run qualc build`
(`.github/workflows/development.yml:41`). In run 44437330383 the `build` job failed at exactly
that step, so `deploy` was skipped, and every run after it was superseded in the `pages`
concurrency group before it could build.

**Status while this was being read (2026-11-19 02:25 UTC):** that gate is now clear. A
`qualc check` of the whole tree, run against `main` at `6928b4b1f391`, printed
"14394 cards and 341 wiki pages OK" with no diagnostics, so the undefined-macro and
dropped-TeX class is closed and the next build that actually runs should deploy. The site a
student reads is still the 2026-11-18 11:38 build until it does. So this entry is not a
repair request: it is the reason the 1605-commit backlog is invisible, and the check that the
backlog went live is `GET /revision.txt` naming a current commit.

Affected: the site as a whole.

---

## 3. Source links a browser refuses

`BACKLOG.md` "dead-provenance-hrefs" gives seven. Verified individually:

- `SRC-GATHMANN-AG`: `https://www.mathematik.uni-kl.de/~gathmann/class/alggeom-2019/alggeom-2019-c1.pdf`
  fails TLS: the server presents `CN=wta-web.rhrk.uni-kl.de`, whose SANs do not include
  `www.mathematik.uni-kl.de` (curl exit 60). A student following the source link gets a
  certificate interstitial, not the exercise sheet. The same host also serves the
  collection directory, so the whole host is affected, not the one file.
- The six `search.worldcat.org/isbn/...` entries are `429` in the report and `308` to a
  working page under `curl -L`. They are rate-limited, not dead: **not** a defect, and they
  should not be "repaired" by changing the URLs.

Affected: `SRC-GATHMANN-AG`. Fix: repoint at a URL that loads (or at the archived copy the
collection already records in its own provenance), after checking the new target by hand.

---

## 4. Study sources with no provenance at all

`BACKLOG.md` "empty-provenance (29)" names 29 collections whose index carries no source
document, so the Sources page for each shows no way back to the exam, textbook or sheet the
problems came from:

`SRC-AG-HOMEWORK`, `SRC-AGX-MISC-AG-PROBLEMS`, `SRC-CH10-HOMOMORPHISM-SOLUTION-OUTLINES`,
`SRC-CH10A-HOMOMORPHISM-SOLUTION-OUTLINES`, `SRC-CH11-ABELIAN-GROUP-SOLUTION-OUTLINES`,
`SRC-CH12-RING-SOLUTION-OUTLINES`, `SRC-CH13-RING-SOLUTION-OUTLINES`,
`SRC-CH14-IDEAL-SOLUTION-OUTLINES`, `SRC-CH15-RING-HOMOMORPHISM-SOLUTION-OUTLINES`,
`SRC-CH16-POLYNOMIAL-RING-SOLUTION-OUTLINES`, `SRC-CH17-POLYNOMIAL-SOLUTION-OUTLINES`,
`SRC-CH20-FIELD-SOLUTION-OUTLINES`, `SRC-CH7-GROUP-SOLUTION-OUTLINES`,
`SRC-CH8-DIRECT-PRODUCT-SOLUTION-OUTLINES`, `SRC-CH9-FACTOR-GROUP-SOLUTIONS`,
`SRC-MALONE-HOUSLEY-TOPOLOGY-PRELIM-ANSWERS-2007`, `SRC-MATH504-FINAL-AUTUMN-2003`,
`SRC-PRELIM-CALCULUS-I-WEEK1`, `SRC-PRELIM-CALCULUS-II-WEEK2`,
`SRC-PRELIM-PRACTICE-WEEK3-2020`, `SRC-PRELIM-PRACTICE-WEEK4-2020`,
`SRC-PRELIM-PRACTICE-WEEK5-2020`, `SRC-PRELIM-PRACTICE-WEEK6-2020`,
`SRC-UGA-CA-COMPILATION`, `SRC-UNSORTED-ALGEBRA`, `SRC-UNSORTED-COMPLEX-ANALYSIS`,
`SRC-UNSORTED-PRELIM`, `SRC-UNSORTED-REAL-ANALYSIS`, `SRC-UNSORTED-TOPOLOGY`.

This is authored-content work (open the document, record where it is), not a code fix, so it
is filed and not repaired here. Note that the five `SRC-UNSORTED-*` collections are
compilations of unknown origin: whether their provenance exists at all is a reading decision.

---

## Not filed

- **Reader findings on #2: none outstanding.** All 29 cards named in the two comments
  (2026-11-18 14:52Z: 16 findings; 16:21Z: 13 findings) were last committed on 2026-11-18,
  after both comments, and each now carries a repair note for its finding. Reading the cited
  passage in each card, none still reads as the finding describes it. Confirmed in detail:
  `E-F8ETH` (the false "R³ minus a compact set is path connected" is gone,
  replaced by a tube construction), `P-L8LEM` (now cites Theorem 27.4), `E-4WQEM` (p. 239),
  `P-X7AK4` (algebraic closure chosen to contain L), `P-BFLEH` (method requirement restored),
  `P-8CA22` (boundary `(-∞,-1]∪[1,∞)` plus the semicircle), `E-I61EM` (`[0,x)` and `a_0`),
  `E-ZYJGG` (p. 223, Theorem 34.3), `P-4GMLL` (factor 1/8), `P-EP64S` (index-two argument),
  `P-CC3DW` (rational canonical form), `P-52WSU` (index sign), `P-WC3HY` (conjugacy, not
  equality), `E-PWXIV` (columns 8-10 and the Lindelöf clause), `E-X04YN` (the 77.4
  relabelling), `E-POA5M` and `E-FGRFM` (retained solutions cited). So there is no
  unrepaired false statement or wrong proof in that material to file.
- **Orphan cards (27)** in `BACKLOG.md`: a reachability measurement. A card no collection and
  no guide lists is reachable by search and by the tag page; no student-facing page breaks.
- **Rendered-page structure.** 120 random live card pages and the four guide pages checked for
  broken in-page anchors, missing `<h1>`, unbalanced math delimiters and empty bodies: none.
  The 13 figure references in `corpus/theory` all resolve (`assets/...`, `200`). All 33
  `tikzcd` diagrams render as SVG on their live pages. `$...$` written inside card titles and
  link text is typeset, not shown literally, because `$` is an inline delimiter in the site's
  MathJax configuration and every such text node carries an even number of them.
