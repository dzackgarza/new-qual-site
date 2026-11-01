# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or site use under [QUAL-05](CONTRIBUTING.md#named-policies).
Include findings outside the selected card.
This file owns observations; [TODO.md](TODO.md) owns selected repair tasks and dependencies.
Keep existing GitHub issue links rather than copying their live status.
The [corpus review patterns](CONTRIBUTING.md#corpus-review-patterns) supply named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact mathematical statement and hypotheses, or user action and expected behavior.

- **Observed evidence:** source page and passage, counterexample or proof gap, or actual action and result with the relevant path/revision.

- **Impact and owner:** affected parts or consumers, existing partial result, and the mathematical or tool boundary that must change.

- **Uncertainty:** distinguish a verified error from a source ambiguity or review candidate.
  State inspected scope and remaining questions.
  For absence claims supply Searched, Found, Conclusion, Confidence and Gaps.

- **Repair:** link the existing TODO task or issue when available and state the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question.
An unsolved problem is ordinary authoring work, not by itself a defect.
A command that prevents reading the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card.
Preserve concurrent entries.
If the selected proof requires a repair, link that dependency and resolve it before relying on the statement; recording it does not make the proof valid.
Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the fixing commit; retain any unresolved portion.
Put durable mathematical errata on the owning card and durable policy in CONTRIBUTING. Keep process notes out of public mathematical remarks.

## Mathematical issues and source questions

### Field Homework 1, problem 1(a): the invariant subspace must be nonzero

- **Object and need:** `P-FHW1-01` in `SRC-FIELDS-HOMEWORK-1`, whose provenance is `assets/attachments/fields-homework-1.pdf`.
  The sheet asks: $\alpha\in F$ is algebraic over $K$ if and only if $F$ contains a finite-dimensional $K$-subspace $L$ with $\alpha L\subseteq L$.

- **Observed evidence:** `assets/attachments/fields-homework-1_extracted.md`, problem 1(a), reads "if and only if F contains a finite-dimensional K-vector subspace L such that $\alpha\cdot L\subset L$", and the page image of the scan agrees; no nonvanishing hypothesis is stated.
  The subspace $L=\{0\}$ is finite-dimensional and satisfies $\alpha L\subseteq L$ for every $\alpha\in F$, so the converse implication fails as written: taking $F=K(t)$ and $\alpha=t$, no nonzero finite-dimensional $K$-subspace of $K(t)$ is stable under multiplication by $t$, since such an $L$ would make $t$ algebraic over $K$ by the very argument the problem asks for in the forward direction.

- **Impact and owner:** the statement of `P-FHW1-01`, and any solution of it: part (a) is false without the hypothesis, and part (b) refers back to part (a)'s hypothesis, so its minimal polynomial statement inherits the same gap.

- **Uncertainty:** verified error, not a source ambiguity.
  The sheet is a scan with a machine extraction, but the missing words are absent from the page image, not lost by the extraction; every other problem on the sheet was read against the image at the same time.
  A reader who insists the sheet means "nonzero" by implication is reading in a hypothesis the page does not print.

- **Repair:** the card now requires $L\ne0$, with a `source-corrected` audit note pointing here; the solution proves both directions of the corrected statement.
  The correction is certified: `proofs/cards/FieldHomework1.lean` proves that `L = ⊥` satisfies the printed hypothesis for every $\alpha$, and proves both directions of the corrected statement, with `#print axioms` showing no `sorryAx`.

### TAMU Spring 2015 problem 10 states (i) without the closedness of $Y$

- **Object and need:** `P-TAMURAS15-10` in `SRC-TAMU-RA-SPRING-2015`, whose source is `assets/attachments/j15.pdf`.
  The problem asks, for a normed space $X$, a subspace $Y$, a norm $\norm{\cdot}_1$ on $Y$ with $\frac1K\norm y_1\le\norm y\le K\norm{y}_1$, and
  $S=\{\varphi\in X^*:\abs{\varphi(y)}\le\norm y_1\ (y\in Y),\ \abs{\varphi(x)}\le K\norm x\ (x\in X)\}$, that $\norm x_2=\sup_{\varphi\in S}\abs{\varphi(x)}$ be a norm.

- **Observed evidence:** statement (i) fails when $Y$ is not closed.
  Take $X=C[0,1]$ with the sup norm, $Y$ the polynomials, and $\norm{y}_1=2\norm y$, so the bracket holds with $K=2$.
  Every $\varphi\in S$ is bounded with $\abs{\varphi(x)}\le2\norm x$ on $X$ and vanishes on the dense subspace $Y$, hence is the zero functional; so $S=\{0\}$ and $\norm x_2=0$ for every $x$, including $x\ne0$.
  The source prints only "with a subspace $Y$" (`j15.pdf`, problem 10), so the defect is in the source, not the transcription.
  With $Y$ closed the statement is true, and the card's proof of (i) uses closedness exactly at the point where it needs $\operatorname{dist}(x,Y)>0$.

- **Impact and owner:** statement (i) of `P-TAMURAS15-10`; parts (ii) and (iii) hold either way, since their arguments use only Hahn--Banach on $Y$ and the equivalence of the two norms on $Y$.

- **Uncertainty:** verified, with the counterexample above; the remaining question is only whether the exam intended the closed case, which the printed text does not say.

- **Repair:** the card's statement now says "a closed subspace $Y$", with a `source-corrected` audit note carrying the counterexample, and the card is solved.
  The *replacement* is not certified: no Lean or Sage artifact establishes statements (i)–(iii) with closedness, so the card marks it proposed and `TODO.md` carries an open certification node.

### UCSD covering-spaces subgroup matching card holds no recoverable posed task

- **Object and need:** `P-O2J6S` in `SRC-UNSORTED-TOPOLOGY`.

- **Observed evidence:** the card body lists five subgroups of $\langle a,b\rangle$ and five images of covering diagrams, but no posed question.
  The card was intaken from the vendored compilation `assets/Topology/650_UCSD_Qual_Questions/Quals/Topology Problems (Solutions).pdf` (with its checked-in extraction), whose "Covering Spaces" section reads only "Generators of the subgroups:" followed by the same list and the same images: those bytes are the author's answer material, recorded without the question, because the compilation assumes the reader has the original course sheet.

- **Searched:** the vendored compilation and its extraction, `UCSD_290_F14_sheet*` extractions, `UCSD_Topology_Qual_Problems_2020-05-29`, `UCSD_290_Qualifying_Exams`, and the `qual-wiki` UCSD finals.
  **Found:** the subgroup list and images only.
  **Conclusion:** the posed task is not recoverable from any retained source.
  **Confidence:** high for absence from retained bytes.
  **Gaps:** the original UCSD 290 covering-spaces homework sheet that posed the question is not in this repository or the sibling clones; the vendored compilation is owner-authored notes and so is also not a valid `provenance:` oracle, which is why the collection's provenance list stays empty.

- **Impact and owner:** the card is not a self-contained problem; a solution cannot be authored without inventing the task.
  The five covering diagrams in `assets/Topology/650_UCSD_Qual_Questions/Quals/assets/` are the only record of the covers.

- **Uncertainty:** the intended task (presumably matching each subgroup with the corresponding cover of $S^1\vee S^1$) is a plausible reconstruction, not a reading of any source.

- **Repair:** blocked on recovering the original UCSD 290 covering-spaces sheet; until then the card stays unauthored rather than being given an invented statement.

### NUS 1970 collections rest on a dataset, not on an examination paper

- **Object and need:** `SRC-NUS-CA-1970-SPRING` and `SRC-NUS-RA-1970-SPRING`, 20 problem cards between them.
  The opened question was the missing source document for both collections.

- **Observed evidence:** the collections were intaken from make-me-a-qual, and `sources/mmaq-source.yaml` records that file's identity: `Combined_Questions.yaml` at revision `6190e0eeaf93ac471a2450444d0b70872b7b9dfa`, sha256 `63845aa447e86bdd9a32f02dd83d9f21ca823b250aebe1fcc0468b2758d49176`.
  The recorded path `assets/ws9/make-me-a-qual/Combined_Questions.yaml` is not in this repository, but the file at that revision of `dzackgarza/make-me-a-qual` hashes to exactly that value, so the witness is recoverable byte for byte rather than merely cited.
  Its 20 `university: NUS` rows carry `exam` `Complex_Analysis` or `Real_Analysis`, `year: 1970`, `season: Spring` (two rows lowercase `spring`), and question numbers 4, 5, 6, 8, 6, 7, 8, 7 (complex) and `1abch`, `1de`, `1fg`, 2, 3, 1, 2, 3, 4, 4, 4, 5 (real); `sources/mmaq-reconciliation.jsonl` rows 108–115 and 194–205 tie each card to one of those rows.

- **Searched:** the repository for a NUS or Singapore document (`grep -a -ril singapore assets wiki corpus`, `find . -iname '*singapore*' -o -iname '*nus*1970*'`), the attachment ledger, and the public NUS qualifying-exam archive at `zr9558.com/nationaluniversityofsingapore/phd-qe-papers/analysis/`.
  **Found:** the dataset rows only, and a public archive whose complex- and real-analysis papers begin with the 2000–2001 academic year.
  **Conclusion:** no examination paper for these twenty problems exists in the repository or in the reachable archive. The dataset is the provenance of the imported statements, which is a different thing from an examination source: it answers what the import said, not what the examination asked.
  **Confidence:** high for absence from retained bytes and from that archive; high for the dataset's identity, which the hash fixes.
  **Gaps:** nothing establishes where the dataset's own metadata came from, and no document attests that the twenty statements were ever set as an examination at NUS in 1970. Its `Complex_Analysis` rows carry question numbers 4–8 twice over, so the label merges two sittings whose papers are not separated anywhere.

- **Impact and owner:** every statement in the two collections, and the site's claim that these are NUS 1970 papers.
  The statements themselves are unaffected: all twenty were read against the dataset and agree with it, apart from the two garbles repaired on `P-R623W` and `P-MMAQ-RML5AHHINX`.

- **Uncertainty:** the year. `tools/qualc/model.py` described `year: 1970` as a sentinel under which a real season is hidden, and `TermOnly` exists on that account.
  The dataset does not bear this out: its unknown-year marker is `year: 0`, which appears on 191 rows and never once beside a real season, while `1970` appears only on these 20 rows and always beside one, exactly as 2005–2019 do on the sittings that really happened.
  So 1970 is read here as a recorded year, and `TermOnly` is corrected to say that no collection uses it.
  A reader who disbelieves the dataset's year has nothing to replace it with.

- **Repair:** both collections now carry a `provenance:` href pinning the dataset at that revision, and `source.date` records the academic term the dataset gives (spring 1970) instead of `unknown`.
  Where a card renumbers the source's parts, its entry carries the source letters as a comment, and the two repaired statements carry `source-corrected` audit notes naming the garbled bytes.
  The source question stays open as `ad-source-gaps-nus` in TODO: recovering the papers, or else marking both collections as imported-only, is what would close it. A pinned dataset is not a substitute.

## Workflow and rendering papercuts

### A fresh VM cannot run three of the suite's tests without four local prerequisites

- **Object and need:** `just test` (= `uv run --group dev pytest -q`), the local counterpart of the `test-ci` tier that `development.yml` gates on at `enforcement: correctness`.
  Three tests fail on a machine provisioned only with the repository and a Python toolchain.

- **Observed evidence:** on 2026-10-31, in a clean checkout at `90114787db`, `pytest -q` reported 3 failed, 271 passed, each failure a missing executable or package rather than a wrong assertion:
  `test_static_site.py::test_a_search_excerpt_is_never_cut_inside_mathematics` runs `node -e`, and the VM has no `node`;
  `test_display_math.py::test_a_commutative_diagram_is_a_block_not_a_paragraph` and `test_card_git_validation.py::test_staged_header_errors_cannot_be_hidden_by_a_valid_worktree` compile a `tikzcd` block through `~/.pandoc/filters/tikzcd.lua`, which needs the pandoc-config clone, `pdf2svg`, and the two TeX packages `dzg-preamble` loads beyond a basic scheme (`bbm`, `luahyperbolic`).
  `ci/_ci-setup` covers only the pandoc-config clone, `pdf2svg`, and a scheme-full TeX Live, and relies on the runner's preinstalled Node.

- **Impact and owner:** anyone verifying a card locally, and every agent session that reports the suite's state.
  The three tests are legitimate gates — they catch a search excerpt cut inside mathematics and a diagram silently dropped from the page — so the repair belongs in the environment, not in the tests.

- **Uncertainty:** verified, and now repaired on this VM without touching a test: pandoc-config cloned to `$HOME/.pandoc` per `_ci-setup`; a portable Node under the project's ignored `tmp/`; a `pdf2svg` shim over `pdftocairo -svg`; and `bbm` plus `luahyperbolic` installed into `$HOME/texmf`.
  With those in place the whole suite passes, so the failures were prerequisites and not regressions.
  A scheme-full TeX Live makes the two TeX packages unnecessary, which is what CI does.

- **Repair:** no repository change is required for CI, which already has all four.
  A local `_local-setup` recipe naming the four would save the next session the diagnosis; this entry is the record until one exists.

### A glued math control word passes `qualc check`

- **Object and need:** card statements and solutions in `SRC-TEXT-HAT02`, and `qualc check`, the gate that validates every card's Markdown and mathematics.

- **Observed evidence:** while comparing §2.1's statements with the book I found four cards (`E-HAT-2.1-1`, `-2`, `-6`, `E-HAT-2.2-16`) writing the simplex vertices as the Greek letter `\nu_0` where Hatcher writes `v_0`, 114 occurrences in all.
  Renaming them exposed a second problem: TeX reads `\mapsto\nu_1` as `\mapsto` followed by `\nu_1`, but the renamed `\mapstov_1` is a single undefined control word, so the repair introduced twelve broken spans that `qualc check` accepted without complaint — it validates YAML, div structure and the Lamport filter, not whether a control word exists.
  A reader's MathJax would have shown those spans as errors.

- **Impact and owner:** any card whose mathematics contains an undefined control word; the site renders it as a MathJax error rather than failing the build.

- **Uncertainty:** verified on the four cards above, and the twelve glued spans were separated again (`\mapsto v_1` and so on).
  I did not survey the whole corpus for glued control words, so other instances may remain.

- **Repair:** the vertex symbol and the twelve spans are fixed in place. A check over the corpus for control words that are neither defined in `vocabularies/macros.json` nor standard TeX would catch this class; none exists, and this entry is the record until one does.

## Queue head passed over, not blocked

- **Object and need:** `E-SS10.PR-6` ("Eight squares from an Eisenstein series"), the first card in
  `queues/C-unsolved-cards.md`. It asks for a six-part proof that `r_8(n) = 16 σ_3^*(n)`, passing
  through `θ(τ)^8 = 48π^{-4} E_4^*(τ)`, the identity `E_4^* = E_4 - 2^{-4}E_4((τ-1)/2)`, the
  periodicity `E_4^*(τ+2) = E_4^*(τ)`, the transformation law `E_4^*(τ) = τ^{-4}E_4^*(-1/τ)`, and two
  asymptotic statements.

- **Observed evidence:** the prerequisite is present. The book is in the repository at
  `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages), and Chapter 10
  "Applications of Theta Functions" begins at the page whose text is extracted in this session, so the
  card is **not** covered by the standing "source PDFs are not in the repository" note that applies to
  the `ad-text-*` reading nodes. While checking the statement I verified part (b) outright: with
  `l = m`, `k = 2n - m`, the substitution `n + m(τ-1)/2 = ((2n-m) + mτ)/2` is a bijection from
  `Z^2 \ {0}` onto the pairs `k ≡ l (mod 2)`, not both zero, so `2^{-4}E_4((τ-1)/2)` is the sum over
  the *same*-parity pairs and `E_4^*`, the sum over opposite-parity pairs, is the difference. Part (c)
  is the same substitution `(m,n) ↦ (m, n+2m)`.

- **Impact and owner:** the queue's head remains unsolved. I did not attempt the full six-part
  write-up in this pass, and this entry exists so that the pass-over is on the record as a choice
  rather than as a blocked prerequisite. It is not a claim that the card is hard for anyone in
  particular, and it is not a deferral granted by the queue.

- **Uncertainty:** verified — parts (b) and (c) as above, and that the source is present. Not
  established: whether parts (a), (d), (e), (f) follow entirely from Chapter 10 as developed there.
  In particular (d) does **not** follow from the modularity `E_4(-1/τ) = τ^4 E_4(τ)` alone, since
  `-(τ+1)/(2τ)` is not `γτ` for any `γ ∈ SL_2(Z)` (matching coefficients forces `d = 0`, `c = 2b`,
  hence `det = -2b^2 ≠ 1`); it has to come from `θ(-1/τ)^8 = τ^4 θ(τ)^8` together with (a). That is
  the structure I would expect, but I did not carry it through.

- **Repair:** **resolved on 2026-11-01.** The card is solved: all six parts are proved and then
  assembled through the book's own maximum-principle criterion (Chapter 10, Theorem 3.4), and the
  identity is checked numerically for $n\le8$ by brute force. The paragraph above is kept because
  its structural observation stands and was used: part (d) cannot be obtained from the modularity of
  $E_4$ alone, and in the solution it is proved directly from the defining series by the bijection
  $(m,n)\mapsto(n,-m)$, which needs no modularity at all. The next card in this queue was `E-SS2.PR-5`,
  also now solved.

## P-AGH467MULTISECANTS: recorded dependencies verified, one cited input not checked

- **Object and need:** `P-AGH467MULTISECANTS` (Hartshorne IV.6.7 and its converse). Its solution
  block was moved into place on 2026-11-01; the question is whether the card's completion criteria and
  dependencies are actually met, as opposed to whether the container is now correct.

- **Observed evidence:** all four internal dependencies of the card resolve —
  `[[P-AGH434RATIONALNORMALCURVE]]`, `[[P-AGH436CURVESOFDEGREEFOUR]]`, `[[T-CRVCAST]]` and
  `[[T-DIVMAPPN]]` each exist as a card in `corpus/`. The previously open tangent-contact implication
  now has its own step, `#tangent-char-zero`, and the characteristic-$p$ failure is a separate step,
  `#positive-char-counterexample`; `pf-qed` names which steps carry which claim.

- **Impact and owner:** one input remains unverified. Step `#tangent-char-zero` invokes "Kaji's
  theorem on tangentially degenerate curves" through a DOI link
  (`10.1112/jlms/s2-33.3.430`) to conclude that the tangent line at a general point of a smooth
  nonplanar curve does not meet the curve again. The exact statement and hypotheses of that theorem
  were **not** checked against the paper in this pass — the article is not in the repository and the
  publisher page is not reachable from here — so the step's citation is recorded as used but
  unchecked.

- **Uncertainty:** verified — the dependency links, the block structure, and the second half of the
  step (contact order at least three at the generic point forces $X$ onto a line in characteristic
  zero, by the two-coordinate argument given in the step). Not verified — the Kaji citation, and
  steps `s1`--`s13`, which were not re-derived here; the mathematical review of those remains the
  earlier auditors' record in the card's audit trail, and no event in this pass supersedes it.

- **Repair:** **partly resolved on 2026-11-01.** The paper's own abstract was retrieved from a
  bibliographic index (the full text is behind a publisher paywall and was not obtained): it defines a
  curve to be tangentially degenerate when *"a tangent line to $X$ at a general point $P$ meets $X$
  again at a point other than $P$"*, and states that *"if $X$ is tangentially degenerate in
  characteristic zero, then $X$ is contained in a 2-plane under a certain condition on singularities
  of $X$"*. For a smooth curve the singularity condition is vacuous, so the contrapositive is exactly
  what `tangent-char-zero` uses. Recorded on the card as a `source-checked` event. Still open: the
  precise singularity condition (irrelevant for smooth $X$) and the body of the paper, and — separately
  — the re-derivation of steps `s1`--`s13`, which no event in this pass supersedes.
## The five `ad-text-*` nodes that cannot be read: their books are not in the repository

- **Object and need:** the `ad-text-hart77`, `ad-text-hun74`, `ad-text-smi`, `ad-text-mun00` and
  `ad-text-hk71-locators` nodes of `TODO.md`, each of which requires reading every card of its
  collection against the printed book.

- **Observed evidence:** the repository holds full text for exactly two of the textbooks the corpus
  is drawn from. `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR'd) and
  `tmp/hat/AT.pdf` with its extracted text `tmp/hat/AT.txt` (8.1 MB / 1.8 MB). For Hartshorne,
  Hungerford, Smith, Munkres and Hilton–Kirby there is no book: a search of `assets/attachments` for
  PDFs over 1 MB returns no title matching any of them, and the only Hartshorne file present is
  `Hartshorne_Solutions.pdf`, 29 pages of worked solutions, which is not the book and cannot certify
  that a card matches a printed statement.

- **Impact and owner:** the five nodes stay open for a reason that is not effort. Reading
  "against the book" is the whole required result, and a card cannot be checked against a page that
  is not there. `audited-deployment` depends on all five.

- **Uncertainty:** verified for this checkout — the searches above are reproducible and the file list
  is complete. Not verified: whether the books exist elsewhere on this machine outside the project
  (the owner's rule is that the project's own assets are the source of record, and copying a
  personal library into the repository is a decision for the owner, not for an agent). This entry
  does not claim the books are unavailable anywhere, only that they are absent here.

- **Repair:** obtain the five books, or make a decision that those nodes are read against a
  different witness (a solutions manual, a table of contents plus a statement database) and say so in
  the node. The two nodes whose books *are* present — `ad-text-hat02` and `ad-text-ss03-gaps` — have
  been started here and are executable.
## A numeric refutation of mine that was wrong, and the rule it breaks

- **Object and need:** a proposed correction to the printed Airy series in
  `E-SSA.PR-3` (`SRC-TEXT-SS03`, Appendix A §5 problem 3). The proposal was that the series printed
  for $\operatorname{Ai}(-x)$ needs a factor $(-1)^n$.

- **Observed evidence:** I tested it by summing $\frac1\pi\sum_n \frac{x^n}{n!}\sin\frac{2\pi(n+1)}{3}
  3^{n/3-2/3}\Gamma(\frac n3+\frac13)$ twice — once as printed, once "with $(-1)^n$" — and concluded
  that the printed series is $\operatorname{Ai}(x)$ (correct) but that the proposed fix gives
  $-\operatorname{Ai}(x)$, hence was also wrong. **The second half of that was my error:** the test
  multiplied every term by the constant $(-1)$ instead of by $(-1)^n$, so it computed $-S(1)$ rather
  than $S(-1)$. Redone correctly, $S(z)=\operatorname{Ai}(z)$ to $10^{-31}$ at $z=\pm0.5,\pm1,\pm2$,
  so $(-1)^n$ does give $\operatorname{Ai}(-x)$ and the proposal was right.

- **Impact and owner:** I rejected a correct submission on the strength of it, and wrote the wrong
  conclusion into a commit message (`c1ccb13fdc`). The card has since been corrected: its statement
  now reads $\operatorname{Ai}(x)=S(x)$, with a `source-corrected` event recording the printed line,
  the numeric agreement and the ODE proof ($S''=zS$, matching initial values, so $S=\operatorname{Ai}$
  by uniqueness). The swarm member was told plainly that the rejection was mine to own.

- **Uncertainty:** verified — the corrected numerics, the ODE identity, and the printed text at PDF
  p.360 (printed p.341), which shows the label `Ai(−x)` over a series in $x^n$, so the print's own
  two sides disagree. Not verified: whether the printed book carries a minus sign that the OCR layer
  dropped; the extraction shows `xn` with the superscript inline and no sign, which is why the card
  records the disagreement rather than asserting a typo.

- **Repair:** done in the card, and here is the rule it establishes, which belongs with the other
  audit rules rather than in a session's memory: **a numeric refutation must be re-derived from the
  formula as stated by the person making the claim.** Substituting a "corrected" version by hand and
  evaluating that is not a check of their claim, it is a check of mine, and the two differ by exactly
  the correction under discussion. Where a claim is about a formula, the refutation must evaluate the
  claim's own expression, printed out, preferably symbolically rather than by transcription.
