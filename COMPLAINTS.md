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

### UCSD Spring 2011 Algebra solutions were stored with literal newline escapes

- **Object and need:** `P-ALGS11E`, `P-ALGS11F`, `P-ALGS11G`, and `P-ALGS11H`; authored solution blocks must be valid Markdown fences so repository tooling recognizes them as solved cards.
- **Observed evidence:** each card already contained a complete reviewed solution introduced by commit `79efcea62` or the same authoring pass, but the solution tail was serialized with literal `\n` text instead of line breaks, beginning with text such as `\n\n::: {.solution}\n`. Consequently `just unsolved-in SRC-UCSD-ALG-SPRING-2011` reported the cards as unsolved even though the proof text was present.
- **Impact and owner:** the malformed serialization made existing solutions invisible to the card parser and generated false unsolved-queue entries. This was content serialization in the four owning cards, not missing mathematics.
- **Uncertainty:** the four Spring 2011 cards named above were inspected and repaired; no broader claim is made here about other cards.
- **Repair:** commits `bdd20392f`, `fecdef52e`, `4806cdb36`, `77204966e`, and `842c029cd` restored real line breaks and valid solution fences while preserving the proof content; all four cards now pass `just check-card` and the Spring 2011 collection reports no unsolved cards.

### `parse_cards` cannot be used from a stdin Python script under the forkserver start method

- **Object and evidence:** the final read-only measurement over the assigned collection range imported `qualc.model.parse_cards` from `.venv/bin/python - <<'PY' ...`. Its process pool used the forkserver start method, whose child process tried to reopen the main module at `/home/dzack/gitclones/new-qual-site/<stdin>` and failed with `FileNotFoundError`, followed by `ConnectionResetError` in the parent.
- **Impact:** direct one-process measurement code cannot call `parse_cards` when the driver is supplied on standard input, even though the same code is otherwise valid. No corpus content was changed by the failed measurement.
- **Repair:** run the measurement from a temporary real `.py` file with an `if __name__ == '__main__'` guard. The workaround succeeded; the later full-range retry reported 53 assigned collections, 2,963 unique cards, and 150 distinct unsolved cards concentrated in eight Berkeley collections, confirming that the failure was only the stdin/forkserver launch mode.

### Smith 8000e Noetherian-rings problem 7 must start from a proper ideal

- **Object and evidence:** `E-SMI-8000E-NR7`; the PDF and extraction literally ask to prove that “every ideal $I$ of $R$ is contained in a maximal ideal.” This is false for $I=R$, since a maximal ideal is proper and cannot contain the whole ring.
- **Impact:** Zorn's lemma applies to the poset of proper ideals containing a given **proper** ideal. Without that qualification the statement has an immediate counterexample.
- **Uncertainty:** none; the wording is present in the PDF source itself.
- **Repair:** add the minimal hypothesis that $I$ is proper, and use the union-of-chains result from problem 6 to verify the Zorn upper-bound condition.

### Smith 8000e finitely-generated-modules problem 1 uses the wrong variable in both primary-subspace definitions

- **Object and evidence:** `E-SMI-8000E-FG1`; both the PDF text layer and the Markdown extraction define `V(2)={x in V: ...}` and `V(3)={x in V: ...}` but then write `(t-2)^r v=0` and `(t-3)^r v=0`. The bound variable is `x`; `v` is otherwise undefined there.
- **Impact:** the primary-subspace definitions are malformed literally, although the intended generalized-eigenspace conditions are unambiguous.
- **Uncertainty:** none; the typo is present in the source PDF itself.
- **Repair:** replace the two occurrences of `v` by the bound variable `x`, retain the source provenance, and classify the resulting primary modules by partitions of 3 and 4.

### `P-EXTME` locally reverses the underdetermined homogeneous-system corollary

- **Object and evidence:** the current `P-EXTME` transcription ends part 4 with “nontrivial solution iff rank A < m and in particular n < m.” For an $n\times m$ coefficient matrix, `rank(A)<m` does not imply `n<m`; for example, the zero $2\times2$ matrix has rank $0<2$ but $n=m=2$. The standard forced corollary is the converse implication: if $n<m$, then `rank(A) <= n < m`, hence a nontrivial homogeneous solution exists.
- **Impact:** the literal last clause is false. Part 3 also needs the uniqueness criterion read conditionally on consistency: once a solution exists, it is unique iff `rank(A)=m`.
- **Uncertainty:** the repository does not contain an independent local copy of this Hungerford exercise, and the available web search did not establish whether the reversed wording belongs to the book or to extraction. This is therefore recorded as a local source/transcription defect rather than attributed to the printed source.
- **Repair:** state the augmented-rank criterion explicitly, make uniqueness conditional on consistency, and replace the reversed final clause with “in particular, if $n<m$, then a nontrivial solution exists.”

### `P-SH5P6` drops the splitting-field context and the coefficient $v_0$

- **Object and evidence:** `P-SH5P6` transcribes Hungerford V.4.1 as though an arbitrary field $F$ merely contains a splitting of $f$, but the section context uses $F$ as the splitting field of $f$ over $K$. The card also writes $g=\sum_{i=1}^k v_i x^i$, omitting the constant coefficient, whereas the source names all coefficients $v_0,\ldots,v_k$.
- **Impact:** without the splitting-field hypothesis, conclusion (1) can fail because $F$ may contain extra elements not generated by the roots. Omitting $v_0$ also changes the defined coefficient field $E$.
- **Uncertainty:** none; an independent source reproduction of Exercise V.4.1 gives the coefficients as $v_0,\ldots,v_k$, and the section convention identifies $F$ as the splitting field attached to $f$.
- **Repair:** make the splitting-field hypothesis explicit on the card, restore all coefficients of $g$, and prove the splitting-field, Galois, and automorphism-group assertions from that corrected statement.

### The authoring CLI name for collection-scoped unsolved traversal is easy to misremember

- **Object and evidence:** during the `SRC-TEXT-HK71` continuation, invoking `python -m qualc.authoring unsolved-in SRC-TEXT-HK71` failed because the supported subcommand is `unsolved`, not `unsolved-in`. The built-in `--help` output immediately resolved the issue.
- **Impact:** this is minor command-discovery friction only; no corpus content was changed by the failed invocation.
- **Repair:** use `python -m qualc.authoring unsolved <collection>` for subsequent collection-scoped traversal. No tooling change is required unless an alias is desired.

### Stale Git sequencer metadata can block unrelated prose commits

- **Object and evidence:** while committing `E-HK-102-9` on 2026-09-11, `qualc.authoring commit` refused because Git reported a cherry-pick in progress. There was no `CHERRY_PICK_HEAD` and no active `git cherry-pick`/`git revert` process; `.git/sequencer/` instead contained a September 9 todo beginning from `94c14cf30` while `HEAD` had advanced to `8864bf13d`.
- **Impact:** the stale sequencer state blocked otherwise valid explicit-path card commits even though no sequencing operation was active.
- **Repair:** after verifying the stale head, absent `CHERRY_PICK_HEAD`, and absence of an active sequencing process, `git cherry-pick --quit` cleared only the sequencer metadata and left the working tree unchanged. A repository-side cleanup or authoring-tool diagnostic could make this failure mode easier to distinguish from a live cherry-pick.

### Direct `.venv` authoring commands can see an unsupported host Pandoc

- **Object and evidence:** during the final read-only sweep of the assigned range, `.venv/bin/python -m qualc.authoring unsolved <collection>` failed inside `qualc.pandoc_batch` because the process found host Pandoc 3.1.3 while the repository requires Pandoc 3.10 or newer. The same authoring command succeeds through the repository's normal login-shell `uv run` route.
- **Impact:** invoking the repository interpreter directly is insufficient for authoring commands that depend on the repository's Pandoc toolchain; a seemingly valid local environment therefore fails before reading any card content. No corpus file was changed by the failed sweep.
- **Repair:** use the repository's documented `just`/`uv run` authoring entry points for Pandoc-dependent commands, or make the supported Pandoc executable available inside direct `.venv` invocations if that route is meant to be supported.

### The repository virtual environment does not include SymPy

- **Object and evidence:** while checking the explicit rational form for `E-HK-72-9`, a read-only `python` calculation using `sympy` failed with `ModuleNotFoundError: No module named 'sympy'`. The system Sage installation was available and supplied the needed exact matrix checks.
- **Impact:** minor verification friction only; no corpus content depended on the failed command.
- **Repair:** use the repository's available exact-arithmetic stack (here system Sage) for such checks rather than assuming SymPy is installed.

### Stale Git sequencer metadata can block unrelated card commits

- **Object and evidence:** while committing `E-HK-102-9` on 2026-09-11, the prose-only card commit path reported that a cherry-pick was in progress. Inspection showed no `CHERRY_PICK_HEAD` and no active cherry-pick process, while `.git/sequencer/head` and `.git/sequencer/abort-safety` both pointed to `94c14cf30`, a September 9 revision, and `.git/sequencer/todo` still listed eight UCSD Spring 2019 picks. Current `HEAD` had advanced to `8864bf13d`, thousands of commits later.
- **Impact:** Git refused an otherwise unrelated explicit-path card commit until the stale repository-wide sequencing state was cleared, which can wedge any direct-main authoring stream sharing the clone.
- **Uncertainty:** none about this instance being stale: the sequencing metadata was two days old, `CHERRY_PICK_HEAD` was absent, no sequencing process existed, and later commits had already advanced `HEAD` far beyond the recorded sequencer head.
- **Repair:** after those checks, `git cherry-pick --quit` removed only the stale sequencer metadata and preserved the working tree; subsequent card commits succeeded. The remaining papercut is that the authoring commit path reports the generic cherry-pick state without distinguishing this stale-metadata case from an active sequence.

### The strip-bound proof states an open-disk inclusion that its argument does not give

- **Object and evidence:** step 2 of the completed `P-JHUFA01CAE` says that `g(z)` belongs to `F(D_|z|)`, but Schwarz's lemma yields only the closed disk at the pointwise radius. Taking `g=F` and any nonzero z gives a counterexample to that heading because F is injective. The displayed argument already uses the correct closed disk. PDF page 55 also supplies the definition of `D_r(0)` and the preceding subordination result, which should be available locally rather than through an unlinked problem number.
- **Repair:** correct the heading to the closed-disk inclusion, define the local disk notation and state the preceding subordination result before applying it. Preserve the valid strip biholomorphism and its exact power-series estimate.

### Spring 2001 JHU Gauss--Lucas statement omits nonconstancy

- **Object and need:** `P-JHUSP01CAF`, Spring 2001 Complex Analysis question 6; Gauss--Lucas must be stated for a nonconstant polynomial.
- **Observed evidence:** the retained source says only “Let P(z) be a polynomial. Show that all zeros of P'(z) lie in the convex hull of the zeros of P(z).” For a constant polynomial, `P'` is the zero polynomial and the claimed zero-set containment is not a valid instance of the theorem.
- **Impact and owner:** the owning card needs the standard nonconstant hypothesis before a proof can quantify over the roots of `P`.
- **Uncertainty:** none about the printed omission; the retained source text is explicit. Degree one is harmless because `P'` has no zeros.
- **Repair:** state `P` nonconstant and prove the Gauss--Lucas containment, treating multiple roots separately.

### Spring 2002 JHU disk-map inequality omits the normalization at zero

- **Object and need:** `P-JHUSP02CAD`, Spring 2002 Complex Analysis question 4; the claimed estimate `|f(z)+f(-z)| <= 2|z|^2` requires `f(0)=0`.
- **Observed evidence:** the retained PDF page 52 and extraction both state only that `f` maps the unit disk into itself. At `z=0` the asserted inequality would force `2|f(0)|<=0`; the constant disk map `f\equiv 1/2` is an explicit counterexample to the printed statement. Even after adding `f(0)=0`, the printed phrase “if equality holds for some z” must exclude `z=0`, where equality is automatic for every normalized map; for example `f(z)=z` is then a counterexample to the printed equality conclusion.
- **Impact and owner:** the literal source theorem is false. The owning card must expose the erratum rather than silently prove an unstated normalization.
- **Uncertainty:** none about the two omissions: the original page image was visually inspected. The repairs `f(0)=0` and “equality at some nonzero z” are forced respectively by the inequality at zero and by the otherwise-vacuous equality case.
- **Repair:** add `f(0)=0` and require equality at a nonzero point, with a mathematical erratum remark; then prove the corrected normalized statement and its equality case.

### P-VVXKF omits the proper-subgroup qualification

- **Object and need:** June 2012 Groups 1(b), `P-VVXKF`, asks that a nonabelian simple group have no subgroup of index at most four.
- **Observed evidence:** the card, retained extraction, and visually inspected PDF page 9 all say "no subgroup" without "proper". The subgroup `H=G` has index one, including for `G=A5`, so the literal statement is false. The source's permitted smallest-simple-group fact supplies the intended proof for proper subgroups.
- **Impact and owner:** the card must exclude the whole group rather than silently using properness in its proof. It also had sole area `prelim` despite the algebra exam heading.
- **Uncertainty:** the original page image confirms the omission; the index-one counterexample establishes the defect independently of the extraction.
- **Repair:** the card now says "proper subgroup", retains the mathematical qualification in a remark, and proves the corrected assertion through its faithful coset action; its area is corrected to algebra. Remove this resolved entry when the reviewed card is committed, retaining the source issue and repair in that commit's message.

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
- **Uncertainty:** the original literal search was restricted to this collection and returned 11 review candidates. `P-TB7BG`, `P-PDAPQ`, and `P-ZSFKA` have since been individually source-checked and repaired; the other candidates are not individually verified defects in this entry.
- **Repair:** read each remaining candidate with its source and correct confirmed subject mismatches, preserving any genuinely intended prelim classification rather than applying a bulk substitution.

### P-4IKKY is internally inconsistent as transcribed

- **Object and need:** `P-4IKKY` in `SRC-UGA-ALG-FALL-2012`; the card should state a nonvacuous structure theorem for an infinite-dimensional vector space equipped with a linear operator.
- **Observed evidence:** the card assumes that the infinite-dimensional $k$-vector space $U$ is generated by the finite set $\{u_1,\ldots,u_m,f^d(u_1),\ldots,f^d(u_m)\}$ for one fixed $d\in\NN$. Such a span has dimension at most $2m$, contradicting the hypothesis that $U$ is infinite-dimensional. The preserved Fall 2012 transcription on the project site reproduces the same wording.
- **Impact and owner:** the literal hypotheses have no models, so attaching the intended $k[x]$-module structure-theorem proof would require guessing missing quantifiers and invariance hypotheses. In particular, the likely intended family $\{f^d(u_i):d\ge0\}$ is not what the source currently states.
- **Uncertainty:** the mathematical inconsistency is decisive, but no independent copy of the Fall 2012 source has yet been recovered that supplies the missing quantification or clarifies the uniqueness clause.
- **Repair:** recover an independent source or erratum for Fall 2012 problem 5 and restore the quantification on the iterates, together with whatever $f$-invariance/module hypotheses are required, before attaching the intended proof.

### P-MMAQ-WV7QEYSPXM omits the infinite-cyclic injectivity hypothesis

- **Object and need:** `P-MMAQ-WV7QEYSPXM`, Dummit--Foote §5.5 Exercise 6; the local statement must retain every hypothesis needed for the semidirect-product isomorphism.
- **Observed evidence:** the local card states the result for an arbitrary cyclic group $K$. Dummit--Foote's exercise adds: if $K$ is infinite, assume both $\varphi_1$ and $\varphi_2$ are injective. The same wording is independently reproduced in University of Utah Math 6320 Exercise 4 (DF-5.5.6-7).
- **Impact and owner:** without injectivity in the infinite case, conjugate finite cyclic images can be generated by different powers while the corresponding power map $K\to K$ is not an automorphism, so the requested construction is not justified. The problem card owns the repair.
- **Uncertainty:** the omitted clause is verified against two reproductions of the source exercise; no ambiguity remains about the intended hypothesis.
- **Repair:** restore the infinite-case injectivity clause on `P-MMAQ-WV7QEYSPXM` before attaching a proof.

## Workflow and rendering papercuts

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

### Unmatched shell globs and guessed extraction paths interrupt source discovery

- **May 2006 Cesaro repair:** the first exact-context patch for `P-JHUMAY06ANL` omitted the leading equals sign from its copied norm identity. The patch was rejected without mutation, and a fresh read showed the original timestamp and content. Correcting that one copied character allowed the reviewed repair, committed in `d31547388`. This was an author-supplied patch-context error, not a concurrent edit.

- **Object and need:** discover the existing authoring commands and retained source for `P-NGXAE` without changing corpus content.
- **Observed evidence:** on 2026-09-10, the command-discovery request included `tools/sample*`; zsh rejected the unmatched glob before `rg` ran. A later search guessed `assets/attachments/algebra_2010-2015_prelims.md`, whereas `find` located the actual file under `assets/attachments/extracted/`. The first complaint patch placed its hunks out of file order and was rejected without changes.
- **Impact and owner:** these were command-construction mistakes in this authoring stream, not failed repository checks or missing source bytes.
- **Uncertainty:** the causes were established directly by the error messages and subsequent successful reads.
- **Repair:** use actual discovered paths and source-ordered patch hunks. Explicit reads of `tools/qualc/authoring.py` and the discovered extraction succeeded; this observation is resolved and may be removed in the commit recording that correction.

### The configured PDF extraction command is missing and service requests failed

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
- **Impact and owner:** the source ambiguity is resolved and no longer blocks this card. The missing configured command and remote-service failures remain setup/tooling issues; successful local rendering does not establish that those services were repaired.
- **Uncertainty:** the printed numeric hypothesis is now visually verified. The generic API errors do not establish a bad PDF, a credential failure, or a specific service-side cause.
- **Repair:** restore and document the configured extraction command and service. Source inspection of this card is complete; future page-specific requests must use the verified PDF page rather than the section's starting page.

### Single-card validation accepts duplicate YAML mapping keys

- **Undated JHU reproduction, 2026-09-10:** `P-JHU4547A5` acquired another complete proof between the initial read and this stream's write. The resulting card contained two top-level `audit` mappings and two solution sections, yet `qualc.authoring check P-JHU4547A5` reported success. Both proofs were mathematically correct; commit `abef71ec0` amends the accidental combined commit to retain one stronger Vieta-based proof. This is another concrete instance of the same parser diagnostic gap and same-range authoring overlap.

- **July 2013 reproduction:** `just check-card` reported schema and Markdown parsing OK for `P-W13IN` while the immediately following diff contained two top-level `audit` keys and two complete coset-action proofs. Both versions were read and found mathematically correct. A subsequent external edit removed the duplicate; `f2c54e941` contains the retained single proof and audit list. This resolves the card collision, not the parser's missing duplicate-key diagnostic.

- **Object and need:** `qualc.authoring check` must reject ambiguous duplicate mapping keys in card front matter, rather than reporting that the card parses correctly.
- **Observed evidence:** on 2026-09-10, `just check-card P-T4WCS` reported schema and Markdown parsing OK while the card had two top-level `audit` keys and two independently authored solution sections. Commit `cc3b2e722` preserves that exact duplicate-key example.
- **Impact and owner:** a syntactically accepted card can contain conflicting audit histories without a diagnostic. This entry concerns the card parser; the separate same-range ownership collision is recorded below.
- **Uncertainty:** this establishes a missed duplicate-key diagnostic in the single-card command, not the behavior of every loader or the full build. Multiple deliberately authored solutions are not themselves an error.
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

- **Further reproduction, 2026-09-10:** a live source-order query returned `P-ARTALG-JU06-6` without a solution; the subsequent native read found a newly authored 157-line card, and Git reported that path as modified. This stream had not edited it and left the other writer's proof untouched. Later exact-context patches for `P-ARTALG-JU06-9` and `P-ARTALG-JU06-12` likewise failed after another writer added complete proofs between the read and patch; those proofs were independently checked and preserved, with no overwrite. A further native `agents.status` request returned `WORKER_IDENTITY_LOST`. The overlap therefore persists in the July 2006 section. `AGENTS.md` still says streams use separate worktrees (lines 648–650), as does `CONTRIBUTING.md` (lines 41–45), despite the current explicit direct-to-main assignment; align that guidance with the actual workflow when repairing ownership coordination.

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
  count is exact as of 2026-09-10.
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
- **Repair:** make the safe method the repository's documented consolidation procedure —
  compute merges out of tree, advance `main` by compare-and-swap ref update, sync only
  merge-changed paths, and skip any branch whose changed paths intersect the checkout's dirty
  set — and require a single consolidation owner at a time so two runs cannot race.

### `apply_patch` is unavailable in the repository shell

- **Object and need:** single-card authored edits in the local repository shell; a patch utility should support narrow, reviewable edits without rewriting unrelated content.
- **Observed evidence:** on 2026-09-10, invoking `apply_patch` from `/home/dzack/gitclones/new-qual-site` failed with `zsh:1: command not found: apply_patch` before changing `P-SP3SP`.
- **Impact and owner:** repository authoring must fall back to whole-file writes or lower-level text tools, increasing the chance of incidental edits. This is environment/tooling-owned, not corpus-owned.
- **Uncertainty:** only this shell environment was tested; `apply_patch` may exist in other harnesses.
- **Repair:** provide the patch helper consistently in repository shells, or document the supported narrow-edit command for this environment.

### `P-MFVEZ` omits the orientation of the square boundary

- **Object and need:** `P-MFVEZ` in `SRC-UGA-PRELIM-SPRING-2003`; a line integral around a closed curve requires an orientation, and Green's theorem uses the positive orientation convention.
- **Observed evidence:** both `assets/attachments/extracted/grad_prelim_Spring03.md` and the authored card say only that $C$ is the boundary of the unit square in the first quadrant. They do not state clockwise or counterclockwise orientation. Direct computation gives $1/2$ counterclockwise and $-1/2$ clockwise.
- **Impact and owner:** the source question has two possible numerical answers unless the usual positive-orientation convention is understood implicitly. The card solution now states both values and performs both requested computations for the positive orientation.
- **Uncertainty:** the original PDF may have conveyed an arrow graphically that the Markdown extraction lost; this was not established from the textual extraction.
- **Repair:** preserve the source wording, but retain the orientation caveat in the mathematical solution unless the original PDF is visually checked and an orientation mark is confirmed.

### `just unsolved-in` can hang indefinitely while scanning the corpus

- **Additional measurement, 2026-09-10:** `UV_NO_SYNC=1 just unsolved-in SRC-ALG-ART-HEACCB` produced no output for at least 46 seconds, then completed successfully with zero unsolved appearances. This run used `qualc.authoring`, not `tools/unsolved_queue.py`; it confirms a long delay, not an indefinite hang or a diagnosed deadlock.

- **Object and need:** `just unsolved-in <collection>` during source-ordered solution authoring; it should return the unsolved appearances for one collection promptly without regenerating `queues/C-unsolved-cards.md`.
- **Observed evidence:** on 2026-09-10, `just unsolved-in SRC-UGA-PRELIM-SPRING-2004` remained running for more than two minutes in `tools/unsolved_queue.py` without producing output; the invocation was terminated before any authored edit.
- **Impact and owner:** collection-by-collection solution work stalls on the repository's designated selection command. This is tooling-owned rather than mathematical-content-owned.
- **Uncertainty:** the host is under concurrent fleet load, so the delay may be performance-sensitive rather than a deterministic deadlock.
- **Repair:** make `unsolved-in` use the already-built catalog or otherwise bound the collection-scoped scan so one source lookup does not require an unbounded whole-corpus pass.

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
- **Uncertainty:** the peak worktree count is not settled by these sources, only bounded by them. Whether any authored prose went with the retired worktrees was not established here; the separate loss recorded above under concurrent branch consolidation is a different event. Whether the volume had other contributors was not measured. As of this reading `git worktree list` reports one entry and `.worktrees/` is empty, but `TODO.md` still carries the retirement item unchecked, so it is not established from this reading that each worktree was retired through the three `QUAL-09` readings rather than simply removed.
- **Repair:** `7757a6177` replaced the `# Worktrees` chapter with `# One checkout, one branch` in `AGENTS.md` and added `QUAL-09` to `CONTRIBUTING.md`, keeping the three readings that establish the state of a worktree this stream did not create and the retirement they permit. `a35065545` added the private `_no-worktrees` recipe and made `just test-commit` depend on it. This entry's commit makes `just commit-card` depend on it as well: the prose-only route commits with `--no-verify`, so the hook never runs, and card authoring is exactly the population that built the worktrees. Two pieces remain unowned. `git commit --no-verify` invoked directly under the prose-only exemption in `AGENTS.md` is ungateable by construction and is covered by documentation alone. `TODO.md` still carries the unchecked retirement item for the worktrees themselves. Acceptance: `git worktree list` in this clone reports exactly one entry; `AGENTS.md`, `CONTRIBUTING.md` and `TODO.md` contain no instruction to create a worktree or a branch; and with a throwaway worktree added, `just test-commit` and `just commit-card` both refuse with the `QUAL-09` message and neither produces a commit. Remove this entry when all three hold and the retirement item is checked.

### `P-VHLIU` reverses the Jordan similarity formula

The source card asks for a Jordan matrix $J$ with $B=JPJ^{-1}$ where $P$ is invertible. The intended change-of-basis relation is $B=PJP^{-1}$; as written, $P$ is not the conjugating matrix and the statement does not express that $J$ is a Jordan form of $B$. The card has been repaired to use the standard similarity formula.

### `P-ZLNVG` labels both parts as “a.”

The Fall/Spring 2012 source card for groups of order $70$ labels both requested parts “a.”. This is a minor transcription/presentation defect; the second part has been relabeled “b.” so the solution can refer to the two parts unambiguously.

### `P-RXKJR` forgets to exclude the zero vector

The card asks to prove that “there does not exist any vector $v$” with $Tv=v$, but $v=0$ always satisfies that equation. The intended eigenvector claim requires $v\ne0$; the corresponding existence statement for $T^2w=w$ is likewise clearer with $w\ne0$. The card has been repaired to say “nonzero vector” in both places.

### `P-3UTDH` is false for the squarefree positive integer `n=1`

Part (a) says that $\sqrt n\notin E$ for every squarefree positive integer $n$. Under the standard convention, $1$ is squarefree, but $\sqrt1=1\in\mathbb Q\subset E$. The intended statement is true for squarefree $n>1$; the card has been repaired accordingly.

### `P-SDO43` drops “Let” at the start of the problem

The card begins “$R$ be a commutative ring with identity...” rather than “Let $R$ be...”. This is a transcription/presentation defect and has been repaired.


### `P-OK5P3` has the wrong arc endpoint and resulting title

- **Object and need:** `P-OK5P3` in `SRC-UGA-PRELIM-SPRING-2007`; the card must reproduce the exam path before a line integral can be solved.
- **Observed evidence:** the preserved Spring 2007 exam extraction says the counterclockwise circle arc runs from `(2,0)` to `(0,2)`. The card instead said `(0,-2)`, and its title consequently described a three-quarter-circle path rather than the source's first-quadrant quarter-circle path.
- **Impact and owner:** the wrong endpoint changes the curve and therefore the line integral. The problem card owns the source-faithful correction.
- **Uncertainty:** none in the retained textual extraction; it explicitly names `(0,2)`.
- **Repair:** corrected the endpoint and title on `P-OK5P3` and solved the resulting positively oriented quarter-disk integral.

### `P-MMAQ-F2ZJO265HN` had a truncated non-mathematical title

- **Object and need:** `P-MMAQ-F2ZJO265HN` in `SRC-UW-ALG-2005`; the card title should name the finite-field counting problem rather than repeat an incomplete source stem.
- **Observed evidence:** the title was `For each prime number $p$ and each positive integer $n$, how many`, while the retained 2005 UW exam asks for the number of $\alpha\in\mathbb F_{p^n}$ with $\mathbb F_p(\alpha)=\mathbb F_{p^6}$.
- **Impact and owner:** the old title did not identify the mathematical content of the card. The problem card owns the title repair.
- **Uncertainty:** none; the retained exam extraction contains the complete statement.
- **Repair:** retitled the card to `Generators of $\mathbb F_{p^6}$ inside $\mathbb F_{p^n}$` while preserving the source statement verbatim.

### `P-IH6FO` had a truncated source-stem title

- **Object and need:** `P-IH6FO` in `SRC-UW-ALG-2006`; the title should name the classification problem rather than stop mid-sentence.
- **Observed evidence:** the card title was `There are five nonisomorphic groups of order 8. For`, while the retained UW 2006 exam asks for the least $n$ admitting an injection of each group of order $8$ into $S_n$.
- **Impact and owner:** the old title did not identify the mathematical task. The problem card owns the title repair.
- **Uncertainty:** none; the retained source extraction contains the complete statement.
- **Repair:** retitled the card to `Minimal faithful permutation degrees of the groups of order $8$` without changing the source-authored problem statement.

### `P-PLFQZ` reversed the representation-dimension bound

- **Object and need:** `P-PLFQZ` in `SRC-UW-ALG-2008`; the card must reproduce the source theorem before solution authorship.
- **Observed evidence:** the retained UW 2008 exam says every irreducible $\mathbb CG$-module has dimension **at most** $\sqrt{|G|}$, while the card title and statement said **at least**. The latter is false for every nontrivial finite group because the trivial representation is irreducible of dimension $1$.
- **Impact and owner:** the reversed inequality changes the theorem into a false statement. The problem card owns the source-faithful correction.
- **Uncertainty:** none; the retained source extraction explicitly says `at most`.
- **Repair:** corrected the title and statement to `at most`, recorded a source check, and supplied the regular-representation proof plus the sharp $S_3$ example.

### `P-APAF21A` omits idempotence in the orthogonal-projection criterion

- **Object and need:** `P-APAF21A`, Fall 2021 Applied Algebra, Question 1(c); the claimed equivalence must characterize orthogonal projections among projections, not among arbitrary matrices.
- **Observed evidence:** the official UCSD Fall 2021 PDF prints “Prove that $A$ is an orthogonal projection if and only if $A$ is Hermitian, i.e., $A=A^H$.” This is false for arbitrary $A$: for example $2I$ is Hermitian but is not a projection. The PDF was checked directly on page 2 on 2026-09-10.
- **Impact and owner:** the source-authored statement is mathematically false as printed. The corpus card has been repaired by adding the standard missing hypothesis $A^2=A$.
- **Uncertainty:** no official erratum was found; the intended hypothesis is inferred from the standard theorem that an idempotent is an orthogonal projection exactly when it is self-adjoint.
- **Repair:** `P-APAF21A` now states the criterion for a projection $A$ satisfying $A^2=A$.

### `P-APAF21I` does not specify the Cayley-graph connection set

- **Object and need:** `P-APAF21I`, Fall 2021 Applied Algebra, Part C Question 1(b); a Cayley graph is determined by a group together with a connection/generating set, so its spectrum is not determined by the group alone.
- **Observed evidence:** the official UCSD Fall 2021 PDF says only “State the definition of the Cayley graph of $C(d)$, and find its eigenvalues and eigenvectors,” with no subset $S\subset C(d)$ specified. Different choices of $S$ give different adjacency spectra.
- **Impact and owner:** the source question is underspecified. The solution treats a general Cayley graph $\operatorname{Cay}(C(d),S)$ and then records the standard cycle specialization $S=\{\gamma,\gamma^{-1}\}$.
- **Uncertainty:** the course may have used a fixed convention in lectures, possibly the cycle graph generated by $\gamma^{\pm1}$; that convention is not stated in the exam PDF.
- **Repair:** retain the source wording, but make the dependence on $S$ explicit in the solution and give the standard cycle case separately.

### `P-APAS04F` has two incompatible symmetric-group labels in the source

- **Object and need:** `P-APAS04F`, UCSD Applied Algebra Spring 2004, Problem 3; the representation and Young subgroup must be well-defined under the exam's own partition convention.
- **Observed evidence:** the official UCSD PDF declares partitions in decreasing order, but Problem 3(a) prints `A^(1,4)` for an irreducible of `S_5`; the only corresponding partition is `(4,1)`. In part (b), it calls `S_3 x S_2` a Young subgroup of `S_5` but then says its permutations lie in `S_6`, while the displayed action only involves `{1,2,3,4,5}`.
- **Impact and owner:** taken literally, `(1,4)` is not one of the indexed partitions and the subgroup description is inconsistent. The problem card owns the mathematical correction.
- **Uncertainty:** none as to the typographical nature of the two labels; both intended corrections are forced by the surrounding definitions and displayed sets.
- **Repair:** corrected `(1,4)` to `(4,1)` and `S_6` to `S_5`, preserving the rest of the source statement, and supplied the character/restriction computation.

### `P-APAS06B` falsely claims uniqueness of the isometric polar factor for rank-deficient matrices

- **Object and need:** `P-APAS06B`, UCSD Applied Algebra Spring 2006, Question 1.2; the rectangular polar factorization must distinguish uniqueness of the positive factor from uniqueness of the isometric factor.
- **Observed evidence:** the official UCSD Spring 2006 PDF states that for every $A\in M_{m,n}$ with $m\ge n$ there is a unique $U\in M_{m,n}$ with orthonormal columns and a unique Hermitian positive semidefinite $H$ such that $A=UH$. Taking $A=0$ gives $H=0$, while every $m\times n$ matrix with orthonormal columns gives a valid factorization, so $U$ is not unique. The PDF was fetched from the collection's recorded provenance URL and checked directly on 2026-09-10.
- **Impact and owner:** the source-authored theorem is false as printed. The positive factor $H=(A^*A)^{1/2}$ is unique for every $A$, but the orthonormal-column factor is unique exactly when $A$ has full column rank.
- **Uncertainty:** none about the counterexample or the corrected uniqueness criterion; the source itself contains no full-rank hypothesis.
- **Repair:** preserve the source statement on the card, expose the counterexample in the solution, and prove the corrected polar-factorization theorem including the full-column-rank uniqueness criterion.

### `P-APASP07I` mistranscribed the first Gröbner-basis generator

- **Object and need:** `P-APASP07I`, UCSD Applied Algebra Spring 2007, Problem 7; the polynomial generators must match the official exam before computing a Gröbner basis or variety.
- **Observed evidence:** the card stated the first generator as $x^3-y^2+1$. The official UCSD Spring 2007 PDF shows an exponent $2$ on the first $x$, i.e. $x^2-y^2+1$; the PDF's positioned-text extraction separately records the superscript `2` immediately after that first $x$. The second generator remains $x^3+y^2+z^2-1$.
- **Impact and owner:** changing $x^2$ to $x^3$ changes both the Gröbner basis and the variety, so the old card stated a different problem from the source.
- **Uncertainty:** none; the source PDF distinguishes the exponents positionally, and the corrected system has been recomputed exactly with Singular.
- **Repair:** corrected only the first exponent to $2$, supplied the reduced lexicographic Gröbner basis for the source-faithful ideal, and solved its complex variety explicitly.

### `P-APASP07J` dropped an eigenvalue from the diagonal action

- **Object and need:** `P-APASP07J`, UCSD Applied Algebra Spring 2007, Problem 8; the invariant ring depends on both weights of the two-dimensional $C_3$-representation.
- **Observed evidence:** the card stated diagonal entries $1,\theta$. The official UCSD Spring 2007 PDF states diagonal entries $\theta,\theta^{-1}$, with $\theta=e^{2\pi i/3}$. The printed request for a nontrivial relation among generators is also consistent with the latter action: its invariant ring is generated by $x^3,xy,y^3$ with relation $(xy)^3=x^3y^3$.
- **Impact and owner:** the mistranscribed action changes the invariant ring and Hilbert series and makes part (c) anomalous for the natural minimal generators.
- **Uncertainty:** none after direct inspection of the official PDF.
- **Repair:** corrected the two diagonal entries to $\theta,\theta^{-1}$ and supplied the source-faithful invariant-ring computation, Hilbert series, defining relation, and elimination procedure.

### `P-APASP08K` does not specify whether composition coordinates may vanish

- **Object and need:** `P-APASP08K`, UCSD Applied Algebra Spring 2008, GB.1; the lower bounds on the Diophantine variables determine whether the generating function has a constant term.
- **Observed evidence:** the official PDF says only that the sum is over “compositions $p=(p_1,p_2,p_3,p_4)$” solving the displayed homogeneous system. It does not state $p_i\ge0$ or $p_i>0$. The equations force $p=(a,b,b,a)$, so the two conventions give respectively $1/((1-x_1x_4)(1-x_2x_3))$ and $x_1x_2x_3x_4/((1-x_1x_4)(1-x_2x_3))$.
- **Impact and owner:** the printed wording does not uniquely determine the constant/lowest-degree terms of the requested generating function.
- **Uncertainty:** the Guoce Xin partition-analysis context strongly suggests nonnegative integer solutions, but the exam does not explicitly state that convention.
- **Repair:** preserve the source statement and give the nonnegative partition-analysis answer first, while recording the strictly-positive alternative explicitly.

### `P-APAS11A` omits irreducibility in the central-element scalar claim

- **Object and need:** `P-APAS11A`, UCSD Applied Algebra Spring 2011, Problem 1(c); Schur's scalar-action conclusion requires irreducibility (or the scalar-commutant hypothesis), not merely centrality of the group element.
- **Observed evidence:** the official Spring 2011 PDF states only that $A:G\to\mathrm{GL}(n,\mathbb C)$ is a representation and asks to show that every central $g$ satisfies $A(g)=cI_n$. Taking $G=C_2$ and $A(s)=\operatorname{diag}(1,-1)$ gives a direct counterexample: $s$ is central but $A(s)$ is not scalar.
- **Impact and owner:** part (c) is false as printed. The intended Schur-lemma statement becomes true after adding that $A$ is irreducible, or after assuming the scalar-commutant condition.
- **Uncertainty:** none; the official PDF was checked directly and contains no irreducibility hypothesis for part (c).
- **Repair:** preserve the printed problem, expose the counterexample in the solution, and prove the corrected irreducible version by Schur's lemma.

### Harvard Math 21b Practice Final 6 Problem 8 has an incorrect supplied eigensolution

- **Object and need:** `assets/attachments/solution6.pdf`, Harvard Math 21b Spring 2018 Practice Final 6, Problem 8; source intake must not turn an incorrect source-provided solution into an authored corpus solution.
- **Observed evidence:** the PDF asks for the eigenvalues and an orthonormal eigenbasis of $A=\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}$, but its printed solution says $A-I_3$ has a two-dimensional kernel and gives eigenvalues $1$ and $3$. Direct calculation gives $A=2I+J$, hence eigenvalue $5$ on $\operatorname{span}(1,1,1)$ and eigenvalue $2$ on its orthogonal complement.
- **Impact and owner:** the source statement is sound, but the supplied answer is mathematically wrong. Queue-E intake owns preserving the problem statement while declining to import that answer as a local solution; later solution authorship should use the correct spectrum $\{5,2,2\}$.
- **Uncertainty:** none; both the displayed matrix and the erroneous answer were checked in the vendored PDF text, not inferred from the OCR inventory.
- **Repair:** repaired `P-HM21B18-PF6-08` with the correct decomposition $A=2I+J$, spectrum $\{5,2,2\}$, and an explicit orthonormal eigenbasis; the card also records that the source-provided eigensolution is incorrect.

### `E-PER08-15.5` overstates the relation between integral and mod-p orientations

- **Object and need:** `E-PER08-15.5`, Perutz *Algebraic Topology I* Exercise 15.5; the exercise must be interpreted consistently with Definitions 15.2--15.3 immediately preceding it.
- **Observed evidence:** the retained notes define an \(R\)-orientation at \(x\) to be an actual \(R\)-module isomorphism \(H_n(M,M\setminus\{x\};R)\to R\). For \(R=\mathbb F_p\), an oriented local homology line therefore has \(p-1\) possible orientations, while over \(\mathbb Z\) it has only two. For \(p=5\), \(2\bar\eta\) is a valid mod-5 orientation but is not the reduction of either \(\eta\) or \(-\eta\).
- **Impact and owner:** the printed claim that a \(\mathbb Z/p\)-orientation “determines, and is determined by” a \(\mathbb Z\)-orientation is false literally for \(p>3\). The correct invariant statement is equivalence of \(\mathbb Z/p\)-orientability and integral orientability when \(p\) is odd.
- **Uncertainty:** none under the definitions printed in the same notes; the issue disappears only if “orientation” in the exercise is read informally as “orientability”.
- **Repair:** preserve the printed statement on `E-PER08-15.5`, exhibit the \(p=5\) counterexample, and prove the corrected orientability equivalence using the \(\{\pm1\}\)-valued orientation monodromy.

### Compact proof fences could terminate solution disclosures during parsing

- **Object and need:** semantic fenced divs in problem cards, first observed on `P-4E6U3`; every authored solution must remain one semantic solution block, with nested proofs inside it and hidden behind the solution disclosure.
- **Observed evidence:** before repair, the built catalog contained 41,385 literal `:::` AST tokens across 3,844 cards. `P-4E6U3` parsed only the beginning of its solution as `solution`; the first generated `::: {.proof}` was read as paragraph text because it followed a Lamport step without a block boundary, and the next bare `:::` closed the solution. The corpus also contained 537 proof openers indented into Markdown's code-block column and 79 cards with genuinely unbalanced semantic fence syntax.
- **Impact and owner:** answers were rendered outside the collapsed solution block, proof labels/fences appeared as source text or code, and the section index undercounted affected solutions and proofs. The defect is in the corpus-reader boundary plus malformed authored fence pairs, not in the disclosure CSS.
- **Repair:** normalize compact and indented fenced-div syntax before Pandoc reads a card, reject genuinely unbalanced fences, repair the existing unbalanced sources, and regression-test that compact nested proofs remain inside one rendered solution disclosure. A rebuilt-catalog audit must contain no literal colon-fence tokens or fence-bearing code blocks.


### `P-BERK84S-03` lost the map arrow and inequality range during extraction

- **Object and need:** `P-BERK84S-03`, Berkeley Preliminary Exam Summer 1984, Problem 3; the statement must identify the codomain of $f$ and the full indexed system of inequalities.
- **Observed evidence:** the retained extraction read `f : R^m  R^n` with no arrow and ended the range as `i=1,...,n_i`, while the same sentence defines $f(v)=(f_1(v),\ldots,f_n(v))$ and states `rank n-1` in $\mathbb R^n$. The only coherent source-faithful reconstruction is $f:\mathbb R^m\to\mathbb R^n$ with inequalities indexed by $i=1,\ldots,n$.
- **Impact and owner:** both losses make the authored statement malformed and obscure the hyperplane geometry used by the problem. The problem card owns the transcription repair.
- **Uncertainty:** the extractor lost the glyphs, so the repair is reconstructed from the source sentence's own notation rather than from the damaged markdown token itself.
- **Repair:** restored the map arrow and the range $i=1,\ldots,n$ on `P-BERK84S-03`, then supplied the complete alternative-theorem proof.

### ag-notes migration omits substantive source content

**Assessment:** incomplete. The [ag-notes migration queue](queues/H-ag-notes-migration.md) owns the direct source-to-target comparison and remaining work. It identifies missing questions, proofs, hypotheses, examples and diagrams, with separate source-repair, reference and private-material dispositions.

**Source boundary:** the deployed `/var/www/ag_notes/` tree was compared with authored corpus and wiki content. The later `/var/www/Notes/Class_Notes/2022/Fall/Orals/` vault remains a separate, unreviewed revision. The queue records the source inventory and target revision.

**Owner and expected repair:** algebraic-geometry corpus curation. Complete the named mathematical items and resolve damaged source fragments before retiring their source. The queue records work; it does not perform the migration.

### Sheaf operations page overstates pullback and the scope of exceptional functors

- **Object:** [Operations and functoriality](wiki/algebraic-geometry/sheaves-of-modules/operations.md).
- **Evidence:** the page says module pullback is right exact and “preserves everything”, then presents extension by zero and exceptional inverse image as functors on sheaves of sets for a general continuous map.
- **Mathematical defect:** tensor pullback need not preserve kernels. For the map from the closed point to `Spec Z`, tensoring multiplication by a prime with its residue field destroys injectivity. Extension by zero for module or abelian sheaves cannot be transferred unchanged to arbitrary sheaves of sets, which lack a distinguished zero section. The exceptional-functor assertions require an appropriate category and hypotheses.
- **Expected repair:** state the actual exactness properties and give the categories and hypotheses for each operation. This is an independent exposition defect encountered during the source comparison; repair remains open here.

### Flowmark refuses to format the complaints document

- **Observed:** the commit hook at `78ef136f4` reports `reformatting would change what pandoc reads (block 49: BulletList content differs)` for `COMPLAINTS.md` and leaves the file unchanged.
- **Owner:** the structured-text formatter. Reproduce against this revision and preserve the parsed list content when correcting the formatter. The refusal leaves this document unformatted; it does not establish a defect in the mathematical corpus.

### Berkeley Summer 1978 Problem 9 has false nearest-point hypotheses

- **Object and need:** `P-BERK78S-09`, Berkeley Preliminary Exam Summer 1978, Problem 9; source intake must preserve the printed metric-space problem without silently adding hypotheses.
- **Observed evidence:** the retained PDF states that if `X={x}` and `Y` is closed in an arbitrary metric space, then `d(x,Y)` is attained, and repeats the claim with `X` compact and `Y` closed. Both assertions are false in general. For example, take points `x,y_1,y_2,...` with `d(x,y_n)=1+1/n` and `d(y_n,y_m)=d(y_n,x)+d(x,y_m)` for `n!=m`; then `Y={y_n}` is closed, `X={x}` is compact, and `d(X,Y)=1` is not attained.
- **Impact and owner:** the source statement itself is defective, not the extraction. The problem card preserves all three printed parts and records the defect; a later solution must not attempt to prove Parts 1--2 without supplying an additional properness/compactness hypothesis.
- **Uncertainty:** none; the relevant PDF page was inspected directly.
- **Repair:** source wording preserved on `P-BERK78S-09` with an audit note documenting the missing hypothesis.

### Berkeley Summer 1978 Problem 11 has an impossible n=0 coefficient inequality

- **Object and need:** `P-BERK78S-11`, Berkeley Preliminary Exam Summer 1978, Problem 11.
- **Observed evidence:** the source indexes both power series from `n=0` and then requires the strict inequality `|b_n| < n^2 |a_n|` "for all n". At `n=0` this reads `|b_0|<0`, so no sequence can satisfy it.
- **Impact and owner:** the literal source condition makes the problem vacuous. The intended radius-of-convergence comparison only needs the estimate for positive indices.
- **Uncertainty:** none about the printed contradiction; the intended `n>=1` repair is forced by the surrounding series statement.
- **Repair:** `P-BERK78S-11` states the coherent condition for `n>=1` and records the source defect in its audit note.

### Berkeley Spring 1983 Problem 4 is missing its defining diagram in the retained PDF

- **Object and need:** `P-BKS83-4`, Berkeley Preliminary Exam Spring 1983, Problem 4; the problem asks for the Euclidean symmetry group of a depicted triangular network.
- **Observed evidence:** the retained PDF does not contain the network figure. In the exact place where the diagram should appear, the PDF prints `../Fig/Pr/Sp83-4.ps not found`.
- **Impact and owner:** the mathematical statement is incomplete in the retained source itself. The four named points `(0,0)`, `(1,0)`, `(0,1)`, `(1,1)` do not determine the omitted infinite triangular network, so reconstructing a diagram would invent source content.
- **Uncertainty:** the lost PostScript figure may exist in an upstream TeX source or archival copy, but it is not present in the retained PDF or extraction.
- **Repair:** `P-BKS83-4` preserves the readable statement and explicitly records that the defining diagram is unavailable; no guessed network was authored.

### Spring 1982 retained extraction does not match PDF Problems 2--9

- **Object and need:** `assets/attachments/extracted/Spring82.md` versus `assets/attachments/Spring82.pdf`; PDF source intake must recover the actual exam statements rather than trusting stale extraction text.
- **Observed evidence:** the PDF page for Problems 2--9 contains, in order, an uncountable-subset accumulation problem, a Hilbert--Schmidt trace inequality, a directional-derivative question, an Arzela--Ascoli-style second-derivative compactness problem, polynomial value/jet normalization, a two-generator group presentation, a contour integral of `cos x/(x^4+1)`, and a real Jordan-form problem. The retained markdown instead gives eight different statements (beginning with a rational integral and distinct linear functionals). Problems 10 onward agree substantially with the PDF.
- **Impact and owner:** automated use of the retained extraction would ingest the wrong mathematics under Spring 1982 provenance. This is not a Unicode-formatting defect detectable by `extraction-detector`; it is content substitution/misalignment.
- **Uncertainty:** the mismatched markdown may have been sourced from another historical prelim during migration, but identifying that source is not required to recover Spring 1982 correctly.
- **Repair:** `SRC-BERKELEY-PRELIM-SPRING-1982` was transcribed against the retained PDF itself for all 20 positions, with Problems 2--9 explicitly source-checked from the PDF page.

### Berkeley Spring 1981 Problem 11 loses its contour figure in the retained extraction

- **Object and need:** `P-BKS81-11`, Berkeley Preliminary Exam Spring 1981, Problem 11; evaluating the contour integral requires the closed curve that the exam says is "shown below".
- **Observed evidence:** `assets/attachments/extracted/Spring81.md` contains the integral `(e^z-1)/(z^2(z-1))` and the sentence referring to the curve, but no figure or geometric description follows. No duplicate problem or legacy Spring 1981 figure asset is present in the repository. The repository-mandated `mineru-open-api` extractor is not installed on this host, so a prohibited substitute extractor was not used.
- **Impact and owner:** the problem can be indexed and preserved with the source PDF as provenance, but the authored card cannot make the winding data self-contained without inventing a contour. Source intake owns preserving the gap explicitly rather than guessing it.
- **Uncertainty:** the contour may remain embedded in `Spring81.pdf` even though it is absent from the retained markdown extraction; recovering that figure requires the permitted extraction path or an archival source asset.
- **Repair:** `P-BKS81-11` preserves the integral and explicitly points to the source curve. No contour geometry or numerical answer was reconstructed.

### Berkeley Spring 1980 Problem 9 loses part of its displayed matrix in extraction

- **Object and need:** `P-BKS80-9`, Berkeley Preliminary Exam Spring 1980, Problem 9; the problem asks for the centralizer of a particular displayed real two-by-two matrix.
- **Observed evidence:** `assets/attachments/extracted/Spring80.md` preserves only a malformed fragment of the display before the statement that every commuting real matrix has form `sI+tA`. The surviving OCR is insufficient to determine all four entries without inference. The archival Berkeley problem compilation reproduces the same Spring 1980 problem but its searchable text also omits the matrix display.
- **Impact and owner:** guessing the fourth entry would manufacture source mathematics. The problem card therefore cannot be self-contained until the display is recovered from a permitted source representation.
- **Uncertainty:** the complete matrix is expected to remain visible in the retained PDF, but the repository-mandated `mineru-open-api` extractor is unavailable on this host and no prohibited substitute extractor was used.
- **Repair:** `P-BKS80-9` preserves the centralizer question and explicitly refers to the matrix displayed in the source exam; no matrix entry or numerical specialization was invented.
