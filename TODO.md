# TODO

Remediation list for the open issues.
Each item names the site and the fix.
The issue holds the reasoning; this file holds the action.

## Blocked on a decision

- [ ] **#35 — `topics:` conjunction.** `tools/qualc/emit.py:645` `run_query` adds one join per topic, so several topics needs one card carrying all of them.
  Choose: `topics:` means *any*; or add `topics_any:` beside it; or keep AND and let sections use explicit `ref:`. No manifest passes more than one topic today, so any choice is free to make now.

- [ ] **#43 — empty bodies group as duplicates.** `tools/import_mmaq.py:76` `loose()` normalises an empty body to `""`, so all 59 empty-bodied cards are "equal" and `tools/collapse_duplicates.py` would merge them onto one survivor.
  Add the floor: a normal form that is empty, or only a todo marker, never groups.

- [ ] **#43 — two duplicate definitions.** `collapse_duplicates` groups loosely (59), `tools/audit.py` digests exactly (11). Decide which one is authoritative and make the other defer to it.

- [ ] **#41 — bibliography.** 21 literal `[@key]` tokens reach the built site and no `csl-entry` is emitted anywhere.
  Either resolve citations against `vocabularies/textbooks.yaml`, or stop the tokens reaching a page.

## Code

- [ ] **#42 — macros used only in `wiki/` render red.** `tools/sync_macros.py:95` walks `corpus/` alone, but `_macros.html` is included in every emitted document.
  32 macros render as red literal text.
  Walk `wiki/` alongside `corpus/`. An undefined macro emits no `mjx-merror`, so add a check that does not rely on one.

- [ ] **#2 — `\qed` cannot render.** `vocabularies/macros.json:228` expands `\qed` to `\hfill\blacksquare`; MathJax has no `\hfill`. 63 cards affected.
  Drop the `\hfill`.

- [ ] **#2 — `\too` and `\closure`.** 68 bare uses of `\too`, which needs an argument.
  `\closure` is undefined.

- [ ] **#41 — `/problems.html` lies about itself.** `tools/qualc/emit.py:1134` and `:1537` print "the URL is the query"; the URL never changes and `?q=` is inert.
  Wire filter state into the URL or delete the sentence.

- [ ] **#41 — 93 figcaptions across 22 pages are raw vault paths** (`_attachments/Pasted image 20211031235625.png`). Images resolve; the captions need descriptions.

- [ ] **#24 — Prelims subject branch.** Five branches are published; Prelims is not one.

- [ ] **flowmark#34** — a footnote definition inside a fenced div aborts the run, so `corpus/wiki/P-ULHPN.md` cannot pass the formatter.
  The fix lands in `dzackgarza/flowmark`, whose own gate is red.

## Content, authoring calls

Issue #2 holds the full list.
Not correctable by code.

- [ ] `D-5MX7E` says colimit and states a limit.

- [ ] `D-VP4LC`'s title contradicts its classification.

- [ ] Four `#todo` bodies.

- [ ] 72 titled statements with empty bodies, 64 in Topology — concentrated in CW Complex, Singular Homology, Excision, Universal Cover, Fundamental Group.

- [ ] 15 statements that are mathematically wrong.

- [ ] No Laurent expansion theorem, no homeomorphism definition.

## Proof not yet taken

- [ ] **#30 replay on the deployed host.** Search, filters, occurrence links, problem disclosure and statements-only generation were never exercised there.
  Screenshots exist at 1440 and 375; #30 names four widths.

- [ ] **Closeout M4/M5** want a sign-off from someone who did not do the migrating.

## Untouched

#5, #6, #7, #8, #9, #10, #11, #14 have had no work this round.

#23, #26, #27, #29, #30 may be complete and merely unclosed — check each against its proof in `artifacts/` before closing.

## Accepted, not defects

19 documented orphans, and 17 titles the audit names as unfixable by titling: cards whose whole statement is a scan, is empty, or is an exam date.
