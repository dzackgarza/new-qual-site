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
  Nothing waits on the sheet's author.

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
  **Conclusion:** no examination paper for these twenty problems exists in the repository or in the reachable archive; the dataset is the only witness.
  **Confidence:** high for absence from retained bytes and from that archive; high for the dataset's identity, which the hash fixes.
  **Gaps:** nothing establishes where the dataset's own metadata came from. Its `Complex_Analysis` rows carry question numbers 4–8 twice over, so the label merges two sittings whose papers are not separated anywhere.

- **Impact and owner:** every statement in the two collections, and the site's claim that these are NUS 1970 papers.
  The statements themselves are unaffected: all twenty were read against the dataset and agree with it, apart from the two garbles repaired on `P-R623W` and `P-MMAQ-RML5AHHINX`.

- **Uncertainty:** the year. `tools/qualc/model.py` described `year: 1970` as a sentinel under which a real season is hidden, and `TermOnly` exists on that account.
  The dataset does not bear this out: its unknown-year marker is `year: 0`, which appears on 191 rows and never once beside a real season, while `1970` appears only on these 20 rows and always beside one, exactly as 2005–2019 do on the sittings that really happened.
  So 1970 is read here as a recorded year, and `TermOnly` is corrected to say that no collection uses it.
  A reader who disbelieves the dataset's year has nothing to replace it with.

- **Repair:** both collections now carry a `provenance:` href pinning the dataset at that revision, and `source.date` records the academic term the dataset gives (spring 1970) instead of `unknown`.
  Where a card renumbers the source's parts, its entry carries the source letters as a comment, and the two repaired statements carry `source-corrected` audit notes naming the garbled bytes.
  Nothing further is recoverable without the papers themselves.

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

