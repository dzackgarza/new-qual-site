# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [review policy index](REVIEW_POLICY.md) supplies
named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact
  mathematical statement and hypotheses, or user action and expected behavior.
- **Observed evidence:** source page and passage, counterexample or proof gap,
  or actual action and result with the relevant path/revision.
- **Impact and owner:** affected parts or consumers, existing partial result,
  and the mathematical or tool boundary that must change.
- **Uncertainty:** distinguish a verified error from a source ambiguity or
  review candidate. State inspected scope and remaining questions. For absence
  claims supply Searched, Found, Conclusion, Confidence and Gaps.
- **Repair:** link the existing TODO task or issue when available and state
  the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question. An unsolved problem is
ordinary authoring work, not by itself a defect. A command that prevents reading
the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card. Preserve
concurrent entries. If the selected proof requires a repair, link that dependency
and resolve it before relying on the statement; recording it does not make the
proof valid. Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the
fixing commit; retain any unresolved portion. Put durable mathematical errata
on the owning card and durable policy in CONTRIBUTING. Keep process notes out
of public mathematical remarks.

## Mathematical issues and source questions

### Berkeley Fall 1981 harmonic-function problem is not harmonic as printed and its correction is underspecified

- **Object and evidence:** `P-BKF81-12` and `assets/attachments/Fall81.pdf`. The PDF prints $u(x,y)=(a^2+b^2+x^2-y^2)/((a-x)^2+(b-y)^2)$, asks to show that $u$ is harmonic and to find an entire function with real part $u$, then adds only: “Correction: $u$ cannot be the real part of an entire function. Why? Change $u$ slightly and do the problem.” Direct symbolic differentiation gives
  $$
  \Delta u=\frac{4(a^2+b^2+2ax-x^2-2by+y^2)}{((a-x)^2+(b-y)^2)^2},
  $$
  which is not identically zero.
- **Impact and owner:** the literal first request is already false, independently of the acknowledged impossibility of an entire harmonic conjugate. The card cannot be solved faithfully until the intended “slight” modification of $u$ is identified from a source or erratum rather than guessed.
- **Uncertainty:** the PDF and Markdown extraction agree on the displayed formula and correction. A repository-wide exact-formula search found no duplicate copy supplying the intended replacement; no correction formula has been verified.
- **Repair:** locate an authoritative erratum or source giving the intended modified $u$, then state that corrected problem explicitly and solve it. Until then, leave `P-BKF81-12` unsolved rather than silently substituting a plausible nearby harmonic formula.

### The 2003–2009 algebra packet has mixed subject metadata

- **June 2012 through June 2010 verified repairs:** the algebra source confirms `P-RE2VW`, `P-5JBRJ`, `P-LU2L3`, `P-3DGMZ`, `P-HU56P`, and `P-VUTDR`, each formerly filed solely under `prelim`. Commits `78a17ba87`, `9c8c210c5`, `afb50fe86`, `15264463f`, `484d9a8e0`, and `487db24fb` correct those classifications individually with complete solutions. PDF pages 11–14 were visually inspected; the five assertions on `P-5JBRJ` were also compared with the retained extraction before authorship. These dispositions do not cover unread classification candidates.

- **Further source-checked algebra classifications:** `P-CZFJJ`, `P-2TVO4`, `P-ZY76X`, and `P-OW6CS` had sole area `prelim`, contrary to their algebra source on visually inspected PDF pages 10, 12, 15, and 11, respectively. Commits `93e35bbb3`, `a40569998`, `020ae2741`, and `4c0c7b804` correct those areas individually with complete solutions. Page 10 also confirms degree three in the second quotient polynomial, where the retained extraction says degree eight; the already-correct polynomial on `P-CZFJJ` was preserved. These dispositions cover only the inspected cards.

- **July 2013 classification repairs:** `P-W5LVB` and `P-NGXAE` had sole area `prelim`, contrary to July 2013 Rings 2 in the retained extraction and Fields 1 on visually inspected PDF page 8. Commits `3d093c891` and `1d405a5b6` correct these areas to algebra and supply the complete classifications, including all ten module classes and every subgroup needed for the quartic subfield counts. These two verified defects are resolved; unread classification candidates are not covered by this disposition.

- **Summer 2014 source-checked repairs:** problems 1, 3, 4, and 6 in the retained 2010–2015 packet confirm `P-TNZTM`, `P-WC2SP`, `P-JHQKZ`, and `P-ZR3OT` as algebra, although each card had sole area `prelim`. Commits `22cb7e0f9`, `a4a9b4527`, `fd3e6433d`, and `2d22e4b57` correct those classifications and supply all requested proofs or counterexamples. The tensor-product card also moves the source's inline hint to a separate hint section and retains the noncommutative-ring hypothesis throughout the proof. These are dispositions of the inspected cards, not of other cards sharing the label.

- **July 2013 source-checked repairs:** visual inspection of PDF pages 6–8 confirms `P-XVV4O`, `P-IXED6`, `P-RP7WR`, and `P-ZG74L` as algebra, although each had sole area `prelim`. Commits `0150fd7f8`, `2a286da3a`, `3ec7685f5`, and `63d2c16c7` correct those classifications and supply complete solutions. The congruence card formerly referred to an unspecified earlier problem for the definition of ideal join; `2a286da3a` incorporates the definition from Rings 1 on the same source page, preserving the hypotheses and making the statement self-contained.

- **Same defect in the later packet:** June 2015 Groups 3, Rings 2, and Fields 2–3 in `algebra_2010-2015_prelims.md` verify `P-PCSZ2`, `P-HHX6V`, `P-U64DA`, and `P-VFB5V` as algebra, although each had sole area `prelim`. Commits `565de6d8f`, `761157381`, `ac07d741f`, and `dc8660316` repair those four classifications individually with complete proofs. The first also makes the source's identity-bijection qualification explicit in the title; the second replaces an unrelated Free Modules topic with Principal Ideal Domains. These four confirmed cases are resolved; they do not establish a disposition of unread classification candidates.

- **Additional source-checked repair:** page 5, Rings and modules 3, confirms `P-TB7BG` as algebra. Commit `8ed9d41e6` corrects that classification and replaces its invalid nilpotency argument with a complete invariant-complement proof. The two explicit algebraic counterexamples remain in the card's mathematical remark; its proof defect is resolved. Other classification candidates in this entry remain subject to individual source review.

- **Further verified repairs:** Summer 2007 Rings 1 and 3 confirm the algebra classifications of `P-PDAPQ` and `P-ZSFKA`, corrected in `fdfd7e73b` and `019c900b6`. The latter also resolves the signed-norm ambiguity by stating the absolute norm and proving Euclidean division, with the source convention explained on the card.

- **Object and need:** `SRC-ART-ALG-2003-2009-PRELIMS`; cards should be filed by the mathematical subject of the source rather than by the generic word “prelim.”
- **Observed evidence:** the original Summer 2009 Algebra Qualifying Exam, page 2, Rings 3–4, confirms algebra content for `P-CSEAZ` and `P-JH3BD`, but both cards had sole area `prelim`. Their source-backed solution edits correct those two areas. A subsequent `rg -l '^  - prelim$' corpus/collections/SRC-ART-ALG-2003-2009-PRELIMS` returned 11 other cards, including `P-3DS32`, `P-GW4KD`, `P-PDAPQ`, and `P-ZSFKA`.
- **Impact and owner:** subject-based browsing can file algebra questions under prelim. This collection owns source-backed classification repairs.
- **Uncertainty:** the original literal search was restricted to this collection and returned 11 review candidates. `P-TB7BG`, `P-PDAPQ`, and `P-ZSFKA` have since been individually source-checked and repaired; the other candidates are not individually verified defects in this entry. Rerun on 2026-09-16, the same search returns seven cards still filed solely under `prelim`: `P-Y5JK4`, `P-7B2CW`, `P-C6SRA`, `P-3GKGV`, `P-GWHUX`, `P-3DS32`, and `P-GW4KD`.
- **Repair:** read each remaining candidate with its source and correct confirmed subject mismatches, preserving any genuinely intended prelim classification rather than applying a bulk substitution.

### P-4IKKY is internally inconsistent as transcribed

- **Object and need:** `P-4IKKY` in `SRC-UGA-ALG-FALL-2012`; the card should state a nonvacuous structure theorem for an infinite-dimensional vector space equipped with a linear operator.
- **Observed evidence:** the card assumes that the infinite-dimensional $k$-vector space $U$ is generated by the finite set $\{u_1,\ldots,u_m,f^d(u_1),\ldots,f^d(u_m)\}$ for one fixed $d\in\NN$. Such a span has dimension at most $2m$, contradicting the hypothesis that $U$ is infinite-dimensional. The preserved Fall 2012 transcription on the project site reproduces the same wording.
- **Impact and owner:** the literal hypotheses have no models, so attaching the intended $k[x]$-module structure-theorem proof would require guessing missing quantifiers and invariance hypotheses. In particular, the likely intended family $\{f^d(u_i):d\ge0\}$ is not what the source currently states.
- **Uncertainty:** the mathematical inconsistency is decisive, but no independent copy of the Fall 2012 source has yet been recovered that supplies the missing quantification or clarifies the uniqueness clause.
- **Repair:** recover an independent source or erratum for Fall 2012 problem 5 and restore the quantification on the iterates, together with whatever $f$-invariance/module hypotheses are required, before attaching the intended proof.

### `P-MFVEZ` omits the orientation of the square boundary

- **Object and need:** `P-MFVEZ` in `SRC-UGA-PRELIM-SPRING-2003`; a line integral around a closed curve requires an orientation, and Green's theorem uses the positive orientation convention.
- **Observed evidence:** both `assets/attachments/extracted/grad_prelim_Spring03.md` and the authored card say only that $C$ is the boundary of the unit square in the first quadrant. They do not state clockwise or counterclockwise orientation. Direct computation gives $1/2$ counterclockwise and $-1/2$ clockwise.
- **Impact and owner:** the source question has two possible numerical answers unless the usual positive-orientation convention is understood implicitly. The card solution now states both values and performs both requested computations for the positive orientation.
- **Uncertainty:** the original PDF may have conveyed an arrow graphically that the Markdown extraction lost; this was not established from the textual extraction.
- **Repair:** preserve the source wording, but retain the orientation caveat in the mathematical solution unless the original PDF is visually checked and an orientation mark is confirmed.

### ag-notes migration omits substantive source content

**Assessment:** incomplete. The [ag-notes migration queue](queues/H-ag-notes-migration.md) owns the direct source-to-target comparison and remaining work. It identifies missing questions, proofs, hypotheses, examples and diagrams, with separate source-repair, reference and private-material dispositions.

**Source boundary:** the deployed `/var/www/ag_notes/` tree was compared with authored corpus and wiki content. The later `/var/www/Notes/Class_Notes/2022/Fall/Orals/` vault remains a separate, unreviewed revision. The queue records the source inventory and target revision.

**Owner and expected repair:** algebraic-geometry corpus curation. Complete the named mathematical items and resolve damaged source fragments before retiring their source. The queue records work; it does not perform the migration.

### Sheaf operations page overstates pullback and the scope of exceptional functors

- **Object:** [Operations and functoriality](wiki/algebraic-geometry/sheaves-of-modules/operations.md).
- **Evidence:** the page says module pullback is right exact and “preserves everything”, then presents extension by zero and exceptional inverse image as functors on sheaves of sets for a general continuous map.
- **Mathematical defect:** tensor pullback need not preserve kernels. For the map from the closed point to `Spec Z`, tensoring multiplication by a prime with its residue field destroys injectivity. Extension by zero for module or abelian sheaves cannot be transferred unchanged to arbitrary sheaves of sets, which lack a distinguished zero section. The exceptional-functor assertions require an appropriate category and hypotheses.
- **Expected repair:** state the actual exactness properties and give the categories and hypotheses for each operation. This is an independent exposition defect encountered during the source comparison; repair remains open here. Rechecked 2026-09-16: line 23 of the page still says pullback is “right exact and preserves everything”.

## Workflow and rendering papercuts

### `parse_cards` cannot be used from a stdin Python script under the forkserver start method

- **Object and evidence:** the final read-only measurement over the assigned collection range imported `qualc.model.parse_cards` from `.venv/bin/python - <<'PY' ...`. Its process pool used the forkserver start method, whose child process tried to reopen the main module at `/home/dzack/gitclones/new-qual-site/<stdin>` and failed with `FileNotFoundError`, followed by `ConnectionResetError` in the parent.
- **Impact:** direct one-process measurement code cannot call `parse_cards` when the driver is supplied on standard input, even though the same code is otherwise valid. No corpus content was changed by the failed measurement.
- **Repair:** run the measurement from a temporary real `.py` file with an `if __name__ == '__main__'` guard. The workaround succeeded; the later full-range retry reported 53 assigned collections, 2,963 unique cards, and 150 distinct unsolved cards concentrated in eight Berkeley collections, confirming that the failure was only the stdin/forkserver launch mode.

### Direct `.venv` authoring commands can see an unsupported host Pandoc

- **Object and evidence:** during the final read-only sweep of the assigned range, `.venv/bin/python -m qualc.authoring unsolved <collection>` failed inside `qualc.pandoc_batch` because the process found host Pandoc 3.1.3 while the repository requires Pandoc 3.10 or newer. The same authoring command succeeds through the repository's normal login-shell `uv run` route.
- **Impact:** invoking the repository interpreter directly is insufficient for authoring commands that depend on the repository's Pandoc toolchain; a seemingly valid local environment therefore fails before reading any card content. No corpus file was changed by the failed sweep.
- **Rechecked 2026-09-16:** `/usr/bin/pandoc` is still 3.1.3 and `~/.local/bin/pandoc` is 3.10.2; `qualc.pandoc_batch` resolves `pandoc` from `PATH`, so a direct invocation whose `PATH` lacks `~/.local/bin` still reaches the unsupported executable.
- **Repair:** use the repository's documented `just`/`uv run` authoring entry points for Pandoc-dependent commands, or make the supported Pandoc executable available inside direct `.venv` invocations if that route is meant to be supported.

### The repository virtual environment does not include SymPy

- **Object and evidence:** while checking the explicit rational form for `E-HK-72-9`, a read-only `python` calculation using `sympy` failed with `ModuleNotFoundError: No module named 'sympy'`. The system Sage installation was available and supplied the needed exact matrix checks.
- **Impact:** minor verification friction only; no corpus content depended on the failed command.
- **Rechecked 2026-09-16:** `.venv/bin/python -c 'import sympy'` still raises `ModuleNotFoundError`.
- **Repair:** use the repository's available exact-arithmetic stack (here system Sage) for such checks rather than assuming SymPy is installed.

### Stale Git sequencer metadata can block unrelated card commits

- **Object and evidence:** while committing `E-HK-102-9` on 2026-09-11, the prose-only card commit path reported that a cherry-pick was in progress. Inspection showed no `CHERRY_PICK_HEAD` and no active cherry-pick process, while `.git/sequencer/head` and `.git/sequencer/abort-safety` both pointed to `94c14cf30`, a September 9 revision, and `.git/sequencer/todo` still listed eight UCSD Spring 2019 picks. Current `HEAD` had advanced to `8864bf13d`, thousands of commits later.
- **Impact:** Git refused an otherwise unrelated explicit-path card commit until the stale repository-wide sequencing state was cleared, which can wedge any direct-main authoring stream sharing the clone.
- **Uncertainty:** none about this instance being stale: the sequencing metadata was two days old, `CHERRY_PICK_HEAD` was absent, no sequencing process existed, and later commits had already advanced `HEAD` far beyond the recorded sequencer head.
- **Repair:** after those checks, `git cherry-pick --quit` removed only the stale sequencer metadata and preserved the working tree; subsequent card commits succeeded. The same stale state also blocked the `qualc.authoring commit` prose route for that card. On 2026-09-16 `.git/sequencer/` is absent, so no stale state is currently present. The remaining papercut is that the authoring commit path reports the generic cherry-pick state without distinguishing this stale-metadata case from an active sequence.

### A narrow patch also removed an unrelated trailing blank line

- **Fall 2010 complex-pair reconciliation:** each of the four native patches removing May 2011 M–P membership also stripped the unrelated final blank line of `index.md`. The complete diffs exposed it, and that line was restored before `a5a88e5de`, `a03115797`, `34a0da3fc`, and `17d6c1e50`. No content was lost, but the helper still changed bytes outside its selected hunks.

- **May 2011 membership reconciliation:** the native patch removing only `P-JHUMAY11ANI` from the collection also deleted its final blank line. The full diff exposed this unrelated deletion; restoring that byte before `038c91e49` left only the intended membership change. The helper's trailing-line normalization remains reproducible.

- **Object and need:** patches to the JHU collection's source membership should leave unrelated bytes unchanged.
- **Observed evidence:** twice in this continuation a native `apply_patch` changing only the collection's middle section also removed the last blank line of `index.md`. Both complete diffs showed the extra end-of-file deletion, which was restored before commits `a1d6f19ef` and `5ff8e48f5`.
- **Impact and owner:** this is patch-helper output normalization rather than an authored content decision. No mathematical content was lost; the full-file diff was needed to detect the incidental change.
- **Uncertainty and repair:** the helper's implementation was not inspected. Preserve trailing bytes outside the selected hunks; the two repository diffs have been corrected, but the helper behavior remains unmodified.

### Continuation tool responses were not available for verification

- **JHU verification recovered, 2026-09-10:** fresh native file reads and Git status returned the complete pending `P-JHUU67CA1` proof. Its source and whole diff were reread, single-card parsing and whitespace checks returned success, and `10a845da3` committed the unchanged proof on `main`. Later source-order authoring also returned complete command results. This establishes recovery of the JHU checkpoint, not the cause of the earlier missing responses or a permanent repair of result delivery.

- **JHU resumption, 2026-09-10:** fresh connector reads of `P-JHUU67CA1`, Git branch/history/status, and a recording search returned only `Skipped ... messages` to this authoring context. Separate local shell and Python output probes were likewise unavailable. This does not establish a connector outage or command failure. The prior attempt left a completed-card check pending for `P-JHUU67CA1`; inspect its actual current contents and Git state before repeating a patch or commit. No new mathematical edit or commit was issued during these diagnostic attempts.

- **Object and need:** verify the Emory continuation's file edits and commits from actual repository reads.
- **Observed evidence:** this continuation received only "Skipped ... messages" in place of later tool results, including narrow Git-history and status requests. The unavailable responses do not establish whether the underlying commands executed successfully or failed.
- **Impact and owner:** the authoring stream cannot verify its final repository state or safely infer which attempted changes need to be repeated. This is a tool-response delivery problem, not evidence of a mathematical or repository-check failure.
- **Uncertainty:** command execution and persistence of the attempted writes remain unverified until actual results are available.
- **Repair:** restore tool-result delivery, then inspect Git history and the Emory card paths before reapplying any attempted edits or commits.

### Single-card validation accepts duplicate YAML mapping keys

- **Undated JHU reproduction, 2026-09-10:** `P-JHU4547A5` acquired another complete proof between the initial read and this stream's write. The resulting card contained two top-level `audit` mappings and two solution sections, yet `qualc.authoring check P-JHU4547A5` reported success. Both proofs were mathematically correct; commit `abef71ec0` amends the accidental combined commit to retain one stronger Vieta-based proof. This is another concrete instance of the same parser diagnostic gap and same-range authoring overlap.

- **July 2013 reproduction:** `just check-card` reported schema and Markdown parsing OK for `P-W13IN` while the immediately following diff contained two top-level `audit` keys and two complete coset-action proofs. Both versions were read and found mathematically correct. A subsequent external edit removed the duplicate; `f2c54e941` contains the retained single proof and audit list. This resolves the card collision, not the parser's missing duplicate-key diagnostic.

- **Object and need:** `qualc.authoring check` must reject ambiguous duplicate mapping keys in card front matter, rather than reporting that the card parses correctly.
- **Observed evidence:** on 2026-09-10, `just check-card P-T4WCS` reported schema and Markdown parsing OK while the card had two top-level `audit` keys and two independently authored solution sections. Commit `cc3b2e722` preserves that exact duplicate-key example.
- **Impact and owner:** a syntactically accepted card can contain conflicting audit histories without a diagnostic. This entry concerns the card parser; the separate same-range ownership collision is recorded below.
- **Uncertainty:** this establishes a missed duplicate-key diagnostic in the single-card command, not the behavior of every loader or the full build. Multiple deliberately authored solutions are not themselves an error.
- **Rechecked 2026-09-16:** `tools/qualc/model.py` still reads front matter with `yaml.safe_load`, which returns `{'a': 2}` for `a: 1\na: 2` without an error.
- **Repair:** reject duplicate mapping keys in card front matter. The particular card was reconciled in `f5f68b2db` after reading both correct proofs; the shorter support-and-transitivity argument was retained, with both original versions preserved in history. That content repair does not repair the parser.

### Supposedly disjoint collection streams collided on consecutive cards

- **September/May 2006 resumption, 2026-09-10:** `P-JHUFA06ANA` acquired another writer's complete proof between the source-order read and the exact-context patch; that patch was rejected, the retained proof was reviewed, and `57c12967d` committed it. `agents.status` returned `WORKER_IDENTITY_LOST`, so no addressable owner was supplied. On `P-JHUMAY06ANA`, two concurrent versions produced two top-level `audit` keys and two equivalent logarithmic-derivative proofs; single-card parsing nevertheless reported success. Both proofs were read. This continuation removed its own redundant version, preserved the other complete proof, and committed the single-proof card in `56ef5c96d`. This is another reproduction of the ownership overlap and duplicate-key diagnostic gap, not a reason to create branches or worktrees.

- **September/May 2006 continuation:** the `P-JHUFA06ANA` commit request raced with `57c12967d`, which had already banked exactly the reviewed proof. Fresh reads found complete external proofs on C and D, retained in `c13693447` and `0152ecf9a`. On `P-JHUMAY06ANA`, the first post-edit diff contained two audit keys and two equivalent proofs despite a successful parser result; a subsequent read found the other writer had removed its redundant version, leaving this stream's proof committed in `56ef5c96d`. That single-proof card was reread and reparsed. Exact-context patches for May B, D, E and F were rejected after external proofs appeared; the complete retained proofs were reviewed, and only B's source-punctuation repair was added in `47bb8a4d4`. A fresh `agents.status` again returned `WORKER_IDENTITY_LOST`. No sequencer or index lock was removed; the content is banked, but same-collection ownership and the duplicate-key diagnostic remain unresolved.

- **May 2009 continuation:** `P-JHUMAY09ANA` acquired another writer's complete coefficient classification after the checkpoint read. The fresh repository worklist skipped it and selected B, but that card also acquired a complete proof before this stream's exact-context patch; the patch failed without mutation. Both retained proofs were read in full and preserved in `4eab4ff9e` and `ce62536c3`. The still-unsolved Fourier-integral card D was then completed in `b0470ce1d`. This is further same-collection overlap, not evidence of disjoint authorship.

- **Further May 2011/May 2010 overlap:** the exact-context patch for `P-JHUMAY11AND` was also rejected after a complete external proof appeared; that proof and the earlier C proof were read and preserved in `935ee8149` and `36cbff308`. On `P-JHUMAY10ANC`, a subsequent exact-context patch met the same condition; the complete retained Bergman proof was independently read, parsed and committed as `f5dbb1a83`. No duplicate proof or audit mapping was appended. These repeat the same unresolved ownership overlap.

- **May 2011/Fall 2010 reconciliation:** while this stream reviewed the four real-analysis duplicate pairs, another writer completed `P-JHUMAY11ANM` in `31519c36a` and repaired its Fall 2010 counterpart in `ea896131c`. Both full proofs and clean committed paths were read before reconciliation; both use the correct quadratic root counts. The attempted reconciliation patch then found M already deleted in `a5a88e5de`; fresh reads confirmed the complete proof survived on its actual Fall 2010 card, with no partial edit left by the rejected patch. The concurrent reconciliations of N, O and P were likewise checked against both versions and retained. A fresh `agents.status` call again returned `WORKER_IDENTITY_LOST`, supplying no addressable owner. This is same-interval overlap, not a conflict with other disjoint ranges. The complete authored Bergman proof on `P-JHUMAY10ANC` was also banked by the concurrent writer in `f5dbb1a83` before this stream's one-line clarification in `96839ff46`; its reviewed mathematics was preserved throughout.

- **May 2011 continuation, 2026-09-10:** the live source-order query selected `P-JHUMAY11ANC`, and a native read showed the original unsolved card. Before this stream's exact-context patch, another writer supplied a complete iteration/Cauchy-estimate proof; the patch was rejected without changes. The retained proof was read in full and preserved. `agents.status` again returned `WORKER_IDENTITY_LOST`, so it supplied no addressable owner. New commits through `ee9348949` also showed that earlier cards had advanced beyond this conversation's previous checkpoint; those committed solutions were not overwritten. This is renewed overlap within the assigned collection, not a reason to create branches or worktrees.

- **Emory source-order overlap, 2026-09-10:** this stream's new query found `P-EMAG7` and `P-EMAG9` already completed by another writer, and `P-EMAL3` acquired that writer's source-check entry before this stream selected it. The three complete proofs were subsequently read and preserved in `e6b24d9f4`, `d9e0fd6aa`, and `b72dd5479`; no second proof or duplicate audit block was appended. These are additional same-interval edits, not a conclusion that the overall assignment is disjoint.

- **Emory continuation, 2026-09-10:** the resumed read-only worklist returned `P-EMAG4` without a solution, but a fresh read found another writer's complete proof and Git marked the path modified. That proof was read and preserved. Later, a full-context patch for `P-EMAF1` was rejected without changes after another writer supplied the complete correction and proof; both it and the newly authored `P-EMAF2` were read in full and preserved. The native `agents.status` request again returned `WORKER_IDENTITY_LOST`, so this tool supplied no addressable owner for resolving the overlap. The direct-to-main policy is now recorded in `7757a6177`; that documentation change does not establish disjoint card ownership.

- **June 2012 Fields 3 reproduction, 2026-09-10:** this stream's full-card patch to `P-F2Y4F` succeeded, but the following diff showed another complete proof in its place plus the dangling fragment "he same cubic factor-degree argument now proves its" and two extra closing fences. A subsequent native read showed that the fragment had already been removed. Both complete proofs were read and have valid irreducibility, splitting, and degree arguments; the clean retained version is committed in `8eef0a5d1`. Later full-context patches for `P-RE2VW`, `P-5JBRJ`, `P-LU2L3`, and `P-VUTDR` were rejected without changes after another writer supplied complete solutions. Those retained proofs were independently read and preserved in `78a17ba87`, `9c8c210c5`, `afb50fe86`, and `487db24fb`. A fresh native `agents.status` call returned `WORKER_IDENTITY_LOST`, preventing addressable coordination. These are same-range collisions, not conflicts with disjoint UCSD or UGA cards.

- **June 2012 continuation, 2026-09-10:** `P-X5M5Q` acquired another writer's complete cubic correction and proof after this stream's initial read; the full-context patch was rejected without changing it, and the retained proof was read in full. On the next card, `P-F2Y4F`, the first post-edit diff showed an externally appended fragment beginning `he same cubic factor-degree argument` and two surplus closing fences after this stream's complete solution. A fresh read confirmed the fragment; an exact-context patch removed only those four extraneous lines, and `8eef0a5d1` records the clean proof. Later full-context patches for `P-P1PID` and `P-T3ZMZ` were likewise rejected after another writer supplied complete proofs; those proofs were read and preserved in `1fb679c5b` and `de4eb627c`. The new source-check entry on `P-2TVO4` was left to its active writer, and its subsequently completed proof was reviewed in full and preserved in `a40569998`. A fresh `agents.status` again returned `WORKER_IDENTITY_LOST`, so no addressable owner was supplied for coordination. Single-card parsing had reported success despite the stray trailing fragment; mathematical and diff review, rather than that parser result, detected it.

- **Fields continuation, 2026-09-10:** the initial checkout inspection found an existing uncommitted `P-IXED6` proof inside the assigned interval; it was preserved. A fresh native `agents.status` request again returned `WORKER_IDENTITY_LOST`, leaving no addressable owner available through that tool. `P-NGXAE` was independently reread as unsolved before its selection.

- **July 2013 reproduction:** while this stream authored `P-W13IN`, a second writer independently appended the same coset-action proof and an additional top-level `audit` key. A fresh read later showed only this stream's visually source-checked proof; the other writer had removed its duplicate before the attempted commit. Both versions were independently reviewed. Later full-context source-check patches for `P-W5LVB` and `P-NGXAE` were rejected without changes after another writer had supplied complete proofs. Those proofs were read in full, checked against the source and the required exhaustive classifications, and preserved in commits `3d093c891` and `1d405a5b6`. Native `agents.status` again returned `WORKER_IDENTITY_LOST`, so the tool still supplied no addressable owner for coordination.

- **July 2003 reproduction, 2026-09-10:** `P-ARTALG-JU03-5` and `P-ARTALG-JU03-8` were each read without solutions and acquired another writer's complete solution before this stream's exact-context patch. Both patches were rejected without changes. The resulting proofs were read in full and preserved; this stream instead completed the still-unwritten lattice and solvability cards. The overlapping ownership therefore persists beyond the July 2006 section.

- **July 2003 reproduction, 2026-09-10:** `P-ARTALG-JU03-6` acquired a complete source-checked proof while this stream was rendering its missing diagram; it was read and retained. An exact-context patch for `P-ARTALG-JU03-9` was then rejected because another writer had inserted a source-check entry after the initial read. No part of that patch applied. Another `agents.status` request returned `WORKER_IDENTITY_LOST`, so no addressable owner could be reached through that tool. These are further same-range collisions, not conflicts with the disjoint UCSD or UGA edits elsewhere in the checkout.

- **Further reproduction, 2026-09-10:** a live source-order query returned `P-ARTALG-JU06-6` without a solution; the subsequent native read found a newly authored 157-line card, and Git reported that path as modified. This stream had not edited it and left the other writer's proof untouched. Later exact-context patches for `P-ARTALG-JU06-9` and `P-ARTALG-JU06-12` likewise failed after another writer added complete proofs between the read and patch; those proofs were independently checked and preserved, with no overwrite. A further native `agents.status` request returned `WORKER_IDENTITY_LOST`. The overlap therefore persists in the July 2006 section. `AGENTS.md` and `CONTRIBUTING.md` then still told streams to use separate worktrees; `7757a6177` replaced that guidance with direct-to-main authorship under `QUAL-09`, which does not by itself resolve same-range ownership.

- **Additional reproduction:** the next card `P-T4WCS` received two independently correct proofs and duplicate audit keys in `cc3b2e722`; `f5f68b2db` reconciles them after full comparison. A further pair of native `agents.status` attempts both returned `WORKER_IDENTITY_LOST`, so this stream could not obtain an addressable owner for coordination either.

- **Later same-range collision:** `P-ARTALG-JU06-7` was read without a solution, then acquired another writer's complete proof before the prepared patch could apply. Exact-context matching rejected the patch without replacing that proof. Commit `0762b3011` contains the retained solution, independently reviewed for the Frobenius-order and inseparable-basis arguments. The ownership overlap therefore persisted beyond the earlier cards.

- **Object and need:** direct-to-main authorship for the assigned interval `SRC-ALG-ART-HEACCB` through `SRC-TEXT-SMI`; each card must have one active writer so a completed proof can be reviewed and committed without overwriting another author's work.
- **Observed evidence:** on 2026-09-10, `P-I5GAL` was read as an unsolved card with no audit entries. Before the prepared patch was applied, another writer added an audit and a complete proof. The patch failed its exact-context check and changed nothing. A subsequent read showed the new proof, and Git then recorded it in `7a51eaba1`. The immediately following source-order card, `P-RK2VH`, also acquired an external edit while this stream had not touched it. This establishes actual overlap inside `SRC-ART-ALG-2003-2009-PRELIMS`, not merely unrelated changes elsewhere in the shared checkout; attribution of the two external edits to the same conversation was not established.
- **Impact and owner:** the stated file-disjointness assumption does not hold for this interval. Advancing both writers through the same ordered worklist risks repeated collisions and lost or duplicated proofs; the live card edits were preserved.
- **Uncertainty:** the other writer's identity and upstream assignment were not established. Two native worker-status requests returned `WORKER_IDENTITY_LOST`. A recording search for `P-I5GAL` returned only unattributed session buckets, so it supplied no addressable conversation owner.
- **Repair:** restore one active writer for this interval and working conversation identity for worker coordination, while retaining the already committed proofs and the current writer's uncommitted card. Do not resolve the collision by overwriting the live card or moving this stream outside its assigned range.

### A read-only connector command was rejected before execution

- **Spring 2002 JHU authoring, 2026-09-10:** a combined request to write, check, diff, and commit `P-JHUSP02CAC` was blocked before execution with the safety-status message. A subsequent status and file read confirmed the card was unchanged. The same reviewed proof is being applied through smaller operations; this is a connector-screening failure, not a repository or mathematical check failure.

- **September/May 2006 review, 2026-09-10:** an empty-input poll of session `46836`, containing the `P-JHUFA06ANA` single-card parse and diff review, was rejected with the safety-status message. The identical retry returned exit zero and the complete successful review output. A later guarded request to validate and conditionally commit the reconciled `P-JHUMAY06ANA` was also blocked before execution; separate Git reads confirmed `56ef5c96d`, and a subsequent standalone check passed on the single-proof card. The latter request included a conditional write, not only a read. Neither rejection was a failed repository check, and no specific screening cause was supplied.

- **September 2006 resumption, 2026-09-10:** a combined request to read the TODO authoring section and obtain the current JHU unsolved list was rejected before execution with the safety-status message. Separate TODO and `.venv/bin/python -m qualc.authoring unsolved SRC-JHU-ANALYSIS-EXAMS` requests returned usable results; the latter starts at `P-JHUFA06ANA`, not the Fall 2015 checkpoint claimed in the previous conversation reply. Current Git history, rather than that stale reply, determines the continuation. The screening cause is unspecified; no repository check failed and no queue file was regenerated.

- **Final JHU verification and cleanup:** a combined request to compare the twelve reviewed source cards with their commits and remove only this continuation's temporary Git-index selections and TSV measurements was rejected before execution with the safety-status message. Separate Git verification and cleanup calls succeeded. The JHU subtree has no pending edits, and only the four explicitly named temporary paths were removed; retained PDF page images were untouched. This reproduces request screening, not a failed repository check.

- **Single-card transport screening:** the guarded request to move the already reviewed `P-JHUMAY11ANN` content to its existing, unsolved Fall 2010 counterpart was blocked before execution with the safety-status message. This request included an intended one-card write, not merely a read. Native `apply_patch` with an explicit move and ID change succeeded; subsequent full-file review and parsing verified the result before `a03115797`. The rejected request did not modify either file, and no repository gate failed.

- **Limaçon source review:** a combined Git status/history and page-render request was rejected before execution with the safety-status message. Separate Git and `mutool draw` calls succeeded. The higher-resolution PDF page 27 confirms the denominator `(z+5i)^3`; the existing integrand was preserved rather than changed from a low-resolution visual impression.

- **Fall 2015 JHU polling, 2026-09-10:** the empty-input poll of session `72126`, running the `P-O3LYK` single-card parser and diff review, was blocked with the safety-status message. The identical retry returned exit zero, successful parsing and the complete diff; `2256b9bd0` committed the reviewed proof. This concerns result retrieval, not a failed repository check; the screening cause remains unspecified.

- **JHU final measurement, 2026-09-10:** a read-only request that invoked `qualc.authoring unsolved`, captured its TSV output, and counted rows was rejected before execution with the safety-status message. The separate `just unsolved-in SRC-JHU-ANALYSIS-EXAMS` request returned exit zero and the full ordered list, beginning with `P-O3LYK`. This is another request-screening failure, not a corpus-parser failure; its cause was not supplied.

- **JHU continuation, 2026-09-10:** combined read-only requests for the live `SRC-JHU-ANALYSIS-EXAMS` unsolved list and `P-RGBUN` source context, and later for `P-8XT21` parsing and diff review, were rejected with the safety-status message before execution. Separate repository-tool and Git invocations returned the requested results. These were connector-screening interruptions, not failed corpus checks; no specific reason for rejection was supplied. Separately, this author's full-context patch for `P-7QJS2` failed because the copied old conclusion inserted an extra word absent from the file; a fresh read confirmed the file was unchanged, and corrected narrow hunks succeeded. That context error was not a concurrent edit.

- **Double-dual, unit-group, and Frobenius card polling, 2026-09-10:** empty-input polls of sessions `96018`, `84268`, and `13500`, containing the single-card parser and diff reviews for `P-EMAL3`, `P-HCAO2`, and `P-HGRO44`, were blocked before retrieval with the safety-status message. In each case the identical retry returned exit zero and the complete diff. All parser and whitespace checks succeeded; these are reproduced connector-screening failures, not failed repository checks.

- **Emory review and commit requests, 2026-09-10:** a combined request for `P-MMAQ-YRTGM662ZN` single-card parsing, whitespace checking, and a Git diff was rejected before execution with the safety-status message. Separate parser and Git requests succeeded and returned the complete reviewed proof, committed in `91576982f`. Later, a combined commit/status/read request for `P-EMAF3` was rejected before execution; the separate commit request succeeded in `642b5b992`. These were connector-screening failures, not failed repository checks or missing files.

- **June 2010 commit polling, 2026-09-10:** an empty-input poll of the `P-3DGMZ` commit session `3501` was blocked by request screening with the safety-status message. The identical immediate retry returned exit zero and commit `15264463f`. This obstructed retrieval of an already-running command's result; it was not a failed repository check or commit.

- **Resumed-authoring reproduction, 2026-09-10:** an empty-input poll of session `51021`, running the read-only `just unsolved-in SRC-ART-ALG-2010-2015-PRELIMS`, was rejected by request screening. The identical subsequent poll succeeded with exit zero and returned 19 unsolved appearances. Later empty-input polls of collection-query session `9169` and single-card review session `8942` were also rejected. Native card reads and separate whitespace checks remained usable, and `de4eb627c` committed the reviewed tensor card. These rejections do not establish failed repository checks, and no queue file was regenerated.

- **July 2013 check and inventory requests:** the combined `P-XVV4O` single-card check, whitespace check, and diff read was rejected before execution with the safety-status message. Separate `just check-card` and `just diff-card` requests succeeded, followed by a successful whitespace check and commit `0150fd7f8`. A later combined Git-status/complaint-diff request and read-only `Corpus`/`parse_cards` inventory request was also rejected before execution; the separate complaint diff and native `just unsolved-in` invocation were usable. These rejections do not establish failed repository checks.

- **Range-continuation reproduction, 2026-09-10:** the read-only ordered scan of `SRC-ALG-ART-HEACCB` through `SRC-TEXT-SMI` using `Corpus` and `parse_cards` was rejected before execution. An empty-input poll of session `56826` was also rejected; the identical later poll succeeded and returned the five `just unsolved-in` results. These observations concern request screening, not failed repository commands.

- **Completion-query reproduction, 2026-09-10:** a read-only `Corpus`/`parse_cards` measurement of the two algebra packets was rejected before execution after the June 2015 proofs were committed. Separate calls to the existing `just unsolved-in` recipe remain the source-order measurement route; the rejected request supplies no evidence of a parser or corpus failure.

- **Commit-poll reproduction, 2026-09-10:** an empty-input `write_stdin` poll of the `P-ARTALG-AL04-9` commit session was rejected with the same safety-status message. A separate read-only Git check confirmed commit `c672be69b` and a clean card path. The rejection therefore obstructed reading the result; it did not mean the commit failed or repository access was unavailable.

- **Additional reproduction, 2026-09-10:** a batched read-only request for Git status/history, TODO text, and authoring-command discovery was rejected with the same safety-status message. Separate native file reads and a smaller Git-status command succeeded. No requested mutation or repository check was involved.

- **Selection-query reproduction:** a read-only multi-collection query using the repository's `Corpus` and `parse_cards` APIs was later rejected before execution. The separate `just unsolved-in SRC-ART-ALG-2003-2009-PRELIMS` command succeeded and returned the remaining cards in source order. The first native patch request recording this occurrence was also rejected before execution. These rejections did not establish a repository-parser failure.

- **Object and need:** source-ordered authoring in the `SRC-ALG-ART-HEACCB` through `SRC-TEXT-SMI` range; reading a selected card, finding its retained source, and inspecting a Git diff should work without mutation.
- **Observed evidence:** on 2026-09-10 a combined `just read-card P-CSEAZ`, `find assets/attachments ...`, and `git diff -- COMPLAINTS.md` invocation was blocked with “we couldn't determine the safety status of the request.” Running the same read-only operations in separate calls succeeded. Later, two empty-input polls of the running `just read-card P-JH3BD` session received the same rejection; the native connector read succeeded for the card. The first image-view request for the rendered June 2008 Rings page was also rejected, while an identical retry displayed it successfully.
- **Impact and owner:** connector request screening interrupted source reading before any command ran. This is connector-owned, not a corpus validation failure.
- **Uncertainty:** the rejections did not identify an offending operation. Both a compound read-only command and empty-input session polling were affected; no causal distinction was supplied.
- **Repair:** expose the specific rejected operation and permit harmless read-only execution and polling. Alternate read calls restored source access but do not repair the screening defect.

### The required Zotero bibliography service is not listening

- **Object and need:** adding an external mathematical reference during `P-CSEAZ` solution authorship; `vocabularies/references.bib` is generated and `tools/sync_bibliography.py` requires the local Zotero/Better BibTeX service rather than hand-authored entries.
- **Observed evidence:** on 2026-09-10 `curl --max-time 5 http://127.0.0.1:23119/api/users/0/items?q=SmallGrp\&format=json\&limit=5` failed immediately with connection refused. Inspection of `tools/sync_bibliography.py` confirmed that its export endpoint uses the same host and port. Integration discovery returned no available Zotero connector.
- **Impact and owner:** new bibliography entries cannot be imported through the documented path while the desktop service is unavailable. Existing citations and independently proved mathematics remain usable; the generated bibliography was left unchanged.
- **Uncertainty:** this establishes local endpoint unavailability at the time of the request, not loss of the Zotero library or the absence of the work from that library.
- **Rechecked 2026-09-16:** a request to `http://127.0.0.1:23119/` is still refused.
- **Repair:** restore the documented Zotero/Better BibTeX export service, then add and export new references through that service.

### Primary local repository connector can silently become unavailable

- **Transient native-read failure, 2026-09-10:** a native read of `P-HU56P` and `P-2TVO4` returned HTTP 502 with `Upstream or external service errors`. An identical immediate retry returned both complete cards successfully. This establishes an intermittent read failure, not missing source files or a repaired upstream service; its cause was not exposed by the error.

- **Object and need:** local-repository work through the Chat On Steroids connector; repository reads and terminal commands should remain available while a scoped authoring stream is active.
- **Observed evidence:** on 2026-09-09, the first attempt to read `AGENTS.md`, `CONTRIBUTING.md`, git status, and git history failed before executing with `Tunnel-client has not been seen for 300 seconds. Ensure tunnel-client is running and connected.` The secondary local connector was available and executed the same commands successfully.
- **Impact and owner:** repository work is blocked when no secondary connector is available; with a secondary connector, the failure still adds avoidable recovery work and makes the primary connection state misleading. This is tooling/infrastructure-owned rather than corpus-owned.
- **Uncertainty:** verified for one primary-connector call in this session; the duration and root cause of the disconnect were not observable from the repository side.
- **Repair:** make connector liveness visible before invocation or transparently fail over to an available local connector, so repository reads do not fail solely because one tunnel has aged out.

### Commit history carries Claude session-provenance trailers

- **Object and need:** this repository's public git history; commit messages should carry no
  agent-session provenance URLs or trailers, per the same policy the fleet's other
  repositories state explicitly.
- **Observed evidence:** on 2026-09-10, `git log --all --grep='Claude-Session'` returns 172
  commits carrying a `Claude-Session: https://…` trailer, the earliest dated 2026-08-27.
  171 of them are reachable from `origin/main`, i.e. already published; exactly one is local
  and unpushed.
- **Impact and owner:** published history exposes session URLs indefinitely, and every future
  agent-authored commit will keep adding them until the commit path stops emitting the
  trailer. Two separable pieces of work: (a) stop new trailers at their source — whatever
  composes commit messages for agent sessions in this repo — and (b) decide the disposition of
  the 171 published commits, which can only be cleaned by rewriting published history and
  force-pushing, a repository-owner decision.
- **Uncertainty:** the emitting component was not identified from the repository side; the
  count is exact as of 2026-09-10. Rechecked 2026-09-16: `git log --all --grep='Claude-Session'` returns 192 commits, all reachable from `origin/main`; the newest is dated 2026-09-11, and no later commit carries the trailer. Whether (a) was repaired at its source or new sessions simply stopped emitting it is not established.
- **Repair:** land (a) first so the count stops growing, then record an explicit decision on
  (b) rather than leaving published history in an unreviewed state.

### Concurrent branch consolidation reset a live worker's tree and lost authored work

- **Object and need:** branch consolidation in a shared checkout that live authoring sessions
  are working in; merging must never disturb another session's index or working tree.
- **Observed evidence:** on 2026-09-10 two consolidation runs executed concurrently. One used
  porcelain `git merge` with `git merge --abort` on conflict in the shared checkout; its abort
  reset the tree under a live worker, and commit `81373e972` records the recovery — "restore
  21 authored solutions lost from the shared worktree — 962 lines … existed only in the
  worktree and in no commit when the tree was reset under a live worker during branch
  consolidation." The concurrent run using `git merge-tree` + `git commit-tree` +
  compare-and-swap `git update-ref`, never touching the shared index, completed 20 merges
  across 44 branches with no such loss.
- **Impact and owner:** any future consolidation in this repository can repeat the loss. The
  work is only recoverable while it still exists in a worktree; nothing in the repository
  prevents the reset.
- **Uncertainty:** whether other authored files were lost and not noticed was not established;
  only the 21 files named in the rescue commit are confirmed.
- **Current state, 2026-09-16:** `QUAL-09` forbids creating branches, and the TODO consolidation section records that every branch was merged by the out-of-tree method and that porcelain merge must not be used while sessions are live. Forty-four merged branches still exist; no repository gate enforces a single consolidation owner.
- **Repair:** make the safe method the repository's documented consolidation procedure —
  compute merges out of tree, advance `main` by compare-and-swap ref update, sync only
  merge-changed paths, and skip any branch whose changed paths intersect the checkout's dirty
  set — and require a single consolidation owner at a time so two runs cannot race.

### `apply_patch` is unavailable in the repository shell

- **Object and need:** single-card authored edits in the local repository shell; a patch utility should support narrow, reviewable edits without rewriting unrelated content.
- **Observed evidence:** on 2026-09-10, invoking `apply_patch` from `/home/dzack/gitclones/new-qual-site` failed with `zsh:1: command not found: apply_patch` before changing `P-SP3SP`.
- **Impact and owner:** repository authoring must fall back to whole-file writes or lower-level text tools, increasing the chance of incidental edits. This is environment/tooling-owned, not corpus-owned.
- **Uncertainty:** only this shell environment was tested; `apply_patch` may exist in other harnesses.
- **Rechecked 2026-09-16:** `command -v apply_patch` still finds nothing in the repository shell.
- **Repair:** provide the patch helper consistently in repository shells, or document the supported narrow-edit command for this environment.

### Direct-to-`main` streams can globally block unrelated card commits with Git sequencer state

- **May 2010 contour commit race:** `qualc.authoring commit` for the reviewed `P-JHUMAY10ANB` returned `Cherry-pick currently in progress` and no pending card change. Immediate Git inspection showed `04cd387e6` had already committed the same reviewed text, a clean card path, and no remaining `CHERRY_PICK_HEAD`. The result was a concurrent successful commit, not lost authorship or a mathematical-check failure. No sequencer state was aborted or altered.

- **JHU prose-commit contention, 2026-09-10:** reviewed commits for `P-7QJS2` and `P-8XT49` failed with exit 128 because `.git/index.lock` existed. Immediate process inspections found unrelated normal commits for `P-PJA4A` (PID 975127) and `P-RXKJR` (PID 1122290), with running pre-commit hooks after approximately one and two minutes respectively. A two-minute wait for the first repair expired while subsequent UGA card commits acquired the index; a later wait allowed `7a07b8064` to commit the unchanged reviewed proof. The JHU edits remained on disk throughout. No lock was deleted and no process was interrupted; these are shared-index failures, not failed mathematical or parsing checks.

- **Emory shared-index contention, 2026-09-10:** reviewed commits for `P-MMAQ-FSI2OIIHX5` and `P-MMAQ-VE5GUZV5YG` each failed with exit 128 because `.git/index.lock` existed. Fresh process reads found separate active `git commit --only queues/E-pdf-attachments.md` operations, PIDs 3366438 and 3420023, with running pre-commit hooks; the second was observed after three minutes thirty seconds. No lock was removed and no process was stopped. Waiting for the active operations to finish allowed the unchanged card proofs to commit in `6b5f8b61e` and `5ab44372e`, preserving the staged `queues/01-corpus-defects.md`. These were shared-index failures, not failed mathematical or card checks. Subsequent card commits used the documented prose-only route.

- **Index-lock contention, 2026-09-10:** the prose-only `just commit-card` for `P-NGXAE` failed with exit 128 because `.git/index.lock` already existed. The next Git read showed another card committed and the lock absent; no lock was deleted. Concurrent commits contend for the shared index even without sequencer state, so inspect the current state and retry after the active operation finishes rather than removing a live lock.

- **Hoffman--Kunze continuation reproduction, 2026-09-10:** the reviewed prose-only commit for `E-HK-68-5` failed with exit 128 because `.git/index.lock` existed. Immediate inspection found the lock already gone and another stream actively running `qualc.authoring diff P-RA19J5`; no lock was deleted and no process was interrupted. The `E-HK-68-5` edit remained intact and had already passed the single-card parser, so the correct recovery is to retry the same explicit-path commit after the transient shared-index holder exits.

- **July 2013 reproduction:** the `just commit-card` attempt for `P-W13IN` returned exit 1 with `Cherry-pick currently in progress` and no pending change to that card. Immediate inspection found `f2c54e941` already committed on `main`, a clean card path, and no remaining `CHERRY_PICK_HEAD`. Thus this attempt raced with another stream's successful commit, rather than exposing a failed mathematical or schema check. No sequencer state was aborted or otherwise modified by this stream.

- **Object and need:** concurrent file-disjoint solution streams committing directly to `main`; one stream's commit operation should not prevent another stream from banking an unrelated card.
- **Observed evidence:** on 2026-09-10, `just commit-card P-S04DG` and later `just commit-card P-S05X3` each failed because the shared checkout was temporarily in `Cherry-pick currently in progress`, even though the concurrently edited card was in a disjoint collection. In both cases the intended prelim card later appeared as a clean committed path after the foreign sequencer operation completed.
- **Impact and owner:** Git sequencer state is checkout-global, so file-disjointness does not make direct-to-main porcelain operations independent; unrelated card commits can fail or be delayed despite no content-path collision.
- **Uncertainty:** the other stream's exact wrapper was not identified; the observed state was standard Git cherry-pick sequencer state in the shared checkout.
- **Repair:** use a commit path that constructs commits without checkout-global sequencer state, or serialize operations that invoke cherry-pick/rebase while preserving file-disjoint authorship on `main`.

### The worktree-per-stream instruction filled the host volume

- **Object and need:** this repository's own authoring instructions and commit gate. A stream reading `AGENTS.md` must not be told to open a second checkout, and a stream that opens one anyway must find out at its next commit rather than when the volume fills.
- **Observed evidence:** the `# Worktrees` chapter of `AGENTS.md` instructed each stream to open an isolated worktree, and streams followed it. Each worktree is a second checkout of the whole tracked corpus — roughly 420 MB, of which 353 MB is `assets/` — carrying a handful of edited Markdown files; the accumulated set held about a megabyte of authored prose between them. On 2026-09-10 the host volume reached 100% with 12 MB free. A full volume presents as killed processes and dying exec sessions rather than as a disk error, so builds and exec sessions died across every repository on the host for most of a day before anyone read `df`. The recorded counts differ by the moment each was taken: `AGENTS.md` says twenty-seven at the failure, holding forty-four changed files; [TODO.md](TODO.md) says twenty-five remained after nine were retired for 3.7 GB; the fleet-level report says twenty-seven to thirty-eight. The replacement rule — commit directly to `main`, no worktrees and no branches — had already been restated twice at fleet level and ignored twice, because it lived only in a fleet document that no worker in this repository reads.
- **Impact and owner:** repository-owned, in the surfaces workers actually read and the gate they actually pass through: `AGENTS.md` and `CONTRIBUTING.md` for the instruction, `just test-commit` and `just commit-card` for the gate. This is not a corpus defect and not an environment condition. The instruction produced the checkouts and no check in the repository refused them, so a third restatement would have changed nothing.
- **Uncertainty:** the peak worktree count is not settled by these sources, only bounded by them. Whether any authored prose went with the retired worktrees was not established here; the separate loss recorded above under concurrent branch consolidation is a different event. Whether the volume had other contributors was not measured. `git worktree list` reports one entry, and the TODO retirement item was closed on 2026-09-13; whether each worktree was retired through the three `QUAL-09` readings rather than simply removed is not established here.
- **Repair:** `7757a6177` replaced the `# Worktrees` chapter with `# One checkout, one branch` in `AGENTS.md` and added `QUAL-09` to `CONTRIBUTING.md`, keeping the three readings that establish the state of a worktree this stream did not create and the retirement they permit. `a35065545` added the private `_no-worktrees` recipe and made `just test-commit` depend on it. `just commit-card` is not gated: on 2026-09-16 its recipe has no `_no-worktrees` dependency and `qualc.authoring commit` performs no worktree check before committing with `--no-verify` when the problem block is unchanged, so card authoring, the population that built the worktrees, bypasses the check. Two further pieces remain unowned. `git commit --no-verify` invoked directly under the prose-only exemption in `AGENTS.md` is ungateable by construction and is covered by documentation alone. Acceptance: `git worktree list` in this clone reports exactly one entry; `AGENTS.md`, `CONTRIBUTING.md` and `TODO.md` contain no instruction to create a worktree or a branch; and with a throwaway worktree added, `just test-commit` and `just commit-card` both refuse with the `QUAL-09` message and neither produces a commit. Remove this entry when all three hold.

### Flowmark refuses to format the complaints document

- **Observed:** the commit hook at `78ef136f4` reports `reformatting would change what pandoc reads (block 49: BulletList content differs)` for `COMPLAINTS.md` and leaves the file unchanged.
- **Reproduced 2026-09-16:** the hook for `b0c3380a1` refused again, now at block 47 with the same `BulletList content differs` message.
- **Owner:** the structured-text formatter. Reproduce against this revision and preserve the parsed list content when correcting the formatter. The refusal leaves this document unformatted; it does not establish a defect in the mathematical corpus.

### MinerU Flash extraction requests fail against the remote service

- **Fall 2007 and September 2005 page inspection:** `mutool draw` rendered PDF pages 36 and 43 successfully and again reported missing ICC support. Native image views showed the full monochrome pages legibly, including the polynomial signs, annular domain wording and the explicit right-half-plane inequalities. This was rendering only, not text extraction or OCR; color-profile fidelity was not tested.

- **September 2011 JHU visual review, 2026-09-10:** the main `.venv` has neither PDFium's Python wrapper nor Pillow. The installed `mutool draw` rendered retained PDF page 22 successfully without extraction, OCR or environment overrides. It emitted `warning: ICC support is not available`; the displayed monochrome mathematical page was legible. This does not establish color-profile fidelity or repair the separately unavailable extraction service.

- **Image-view boundary, 2026-09-10:** native `view_image` rejected `/tmp/newqual-july2013-fields-proof.png` because `/tmp` is outside the connector's approved roots, although terminal rendering there succeeded. Moving that rendered page to the ignored repository path `.tmp-july2013-fields-proof.png` allowed inspection of PDF page 8. Keep inspection images inside an approved root; this was an image-path restriction, not a rendering or source-file failure.

- **July 2013 Fields continuation, 2026-09-10:** opening the public raw PDF again returned `Internal Error`, without a PDF reference usable by the web screenshot tool. The already-rendered local `assets/attachments/intermediate/w13-source-review-hpowvjoz/page-8.png` displayed successfully and verified all four Fields questions; no new extraction or OCR was performed.

- **July 2013 symbol recovery:** the retained extraction drops the divisibility symbol in Groups 1(b). Visual inspection of PDF page 6 confirms `p` does not divide `q-1`, exactly as stated on `P-W13PQ`. The web reader returned an internal error for the public raw PDF and a non-retryable rejection for the CDN URL, so neither yielded a PDF that its screenshot tool could inspect. Rendering the retained PDF with the installed system PDFium and inspecting the resulting page image succeeded without OCR or a new text extraction. The card's hypothesis needed no correction.

- **July 2003 lattice recovery:** `P-ARTALG-JU03-6` replaced its essential diagram with the undefined phrase “a specific diamond shape.” Native inspection of PDF page 45 shows exactly four incomparable middle vertices, plus top and bottom. Commit `6b1b83169` restores that complete order relation and proves all five decisions, including realization over the specified base field. For this inspection, `UV_NO_SYNC=1 uv run python` lacked `pypdfium2`; `/usr/bin/python3` already had it and rendered the retained source successfully without installing packages or running OCR. PDF page 44 contains problem 5, not the required diagram.

- **Object and need:** source verification for `P-ARTALG-AL04-3` exposed an unavailable configured PDF extraction command and subsequent remote-service failures. The installed source-reading workflow should be usable without guessing numeric hypotheses from extracted text.
- **Observed evidence:** on 2026-09-10, `command -v mineru-open-api` returned no executable, and `UV_NO_SYNC=1 uv run mineru-open-api --help` failed with `No such file or directory`. `AGENTS.md` names this command as the sole permitted PDF extraction method.
- **Execution attempts:** the official Linux binary runs from `/tmp/qual-mineru.XhPQVW/mineru-open-api` and reports version `v0.5.9`. A page-29-only `flash-extract` request timed out uploading the PDF. Separate URL-input requests using the public GitHub copy and a jsDelivr copy both returned error `-60007`, reporting that the model service was temporarily unavailable. Both public copies were verified byte-identical to the repository PDF before submission. All three requests targeted page 29; none returned source content.
- **Source verification, 2026-09-10:** direct PDFium rasterization of the retained PDF and native image inspection succeeded. Page 29 contains only Groups 1; the actual Groups 3 statement is on PDF page 30 (printed page 2) and says the integer `72`, with no superscript and no abelian hypothesis. The PDF SHA-256 is `956dd5e3735e66d75eb0bed9af4f0c544015016fcf48fec8f10eeab98a06393b`. No new text extraction or OCR was used. Commit `83522c224` retains order 72 and proves the full fifty-class classification, including the executable exact action-orbit enumeration.
- **Additional tool friction:** web retrieval of the public raw PDF returned `DisabledError`, alternative PDF URLs were rejected, and a combined read-only repository request was rejected before execution. Native reads and local rendering restored source access. The installed PDFium wrapper also rejected the context-manager form with `TypeError`; constructing `PdfDocument` directly succeeded. A later combined request for `P-ARTALG-JU03-9` single-card parsing and diff review was also rejected before execution; the two separated operations succeeded, so the rejection was not a failed repository check.
- **Additional source defect repaired:** visual inspection of PDF page 32 (printed page 4), Rings 2, showed that `P-ARTALG-AL04-6` omitted part (a), the rational canonical form of the matrix with rows `(2,3)` and `(7,1)`. Commit `7db3ccc00` restores and proves both parts on that source item; the garbled matrix in the extraction was not evidence that the original paper omitted it.
- **Additional proof defect repaired:** the former `P-ARTALG-AL04-10` proof inferred that a group is abelian from a normal abelian subgroup and a cyclic quotient; that implication is false, as `S3` with its normal `C3` shows. The order-specific action argument needed there was absent. Commit `d79880a9b` replaces it with the index-three coset action. PDF page 37 also prints `[K:F]=105` with `F` undefined; the already-authored card explicitly states `[K:Q]=105`, and that is the hypothesis proved rather than an assertion about an unspecified field `F`.
- **Additional collection omission repaired:** PDF page 38 (printed page 10) contains 2004 Fields 4, asking for all subfield orders of a field of order `5^20` and uniqueness of its subfield of order 25. The 2004 section listed only ten items, ending with Fields 3 on `P-ARTALG-AL04-10`; its four Groups, three Rings, and three Fields cards omitted this final source problem. A corpus-wide literal search for `5^{20}`, `5^20`, and `more than one subfield of order` returned no matches. Commit `420c00019` restores the item as `P-ARTALG-AL04-11`, its ordered membership, and the complete existence-and-uniqueness proof. Zero unsolved listed cards had not established complete source coverage.
- **Rechecked 2026-09-16:** `mineru-open-api` is now installed at `~/.local/bin/mineru-open-api`, so the missing-command half of this entry no longer reproduces. The service half persists: [Queue E](queues/E-pdf-attachments.md) records eleven sources left open on 2026-09-14 because Flash uploads timed out awaiting response headers or required split page ranges.
- **Impact and owner:** the source ambiguity is resolved and no longer blocks this card. The missing configured command and remote-service failures remain setup/tooling issues; successful local rendering does not establish that those services were repaired.
- **Uncertainty:** the printed numeric hypothesis is now visually verified. The generic API errors do not establish a bad PDF, a credential failure, or a specific service-side cause.
- **Repair:** restore reliable service access for the installed extraction command. Source inspection of this card is complete; future page-specific requests must use the verified PDF page rather than the section's starting page.
