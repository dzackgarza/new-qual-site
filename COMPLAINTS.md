# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or site use under [QUAL-05](CONTRIBUTING.md#named-policies).
Include findings outside the selected card.
This file owns observations; the [issue tree](https://github.com/dzackgarza/new-qual-site/issues/83) owns selected repair tasks and their order.
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

- **Repair:** link the existing issue when available and state the result that would resolve the observation.

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

### May's p.169 chart chain does not prove boundary-orientation compatibility

- **Object and need:** J. P. May, *A Concise Course in Algebraic Topology*, §21.4, pp.169--170, formerly used to complete `E-HAT-3.3-31`; the needed result is $\partial_*[M]=[\partial M]$ for a compact $R$-orientable manifold.

- **Observed evidence:** the first displayed identification on p.169 is false for May's stated chart. For $M=[0,1]$, $x=0$, $U=[0,\epsilon)$, $V=\{0\}$, and $y\in(0,\epsilon)$, the pair $(M^\circ,M^\circ-U^\circ)=((0,1),[\epsilon,1))$ has contractible total space and subspace, hence zero $H_1$, while $H_1((0,1),(0,1)-\{y\};R)=R$. The closed-half-disk variant has the same defect. The printed inclusion $(M-U^\circ)-\{x\}\to M-U$ also has the wrong direction because its source contains $V-\{x\}$ but its target does not. On p.170, the injectivity argument assumes $H_n(M^\circ)=0$ although closed components of $M$ are not excluded. The retained `tmp/sources/may-concise-errata.pdf` has no p.169 entry; Michael Paluch's Lecture 39, pp.111--112, repeats the same chart chain rather than repairing it.

- **Impact and owner:** the May-based solution installed in `3ce2e79ef9` was not a proof of the exercise. The boundary-class theorem itself is not counterexampled. This entry records a verified defect in the cited argument, not an ambiguity in Hatcher's statement.

- **Uncertainty:** the counterexample and the reversed inclusion were checked directly against the retained revised May PDF, printed p.169. No correction to May's chain is claimed here; the absence statement is limited to the one-page official errata file actually inspected.

- **Repair:** `E-HAT-3.3-31` now uses Glen E. Bredon, *Topology and Geometry*, Chapter VI, §9, Lemma 9.1, printed pp.356--357. Bredon's triple $(M,A\cup B,B)$ proves the compatibility one boundary component at a time; the card supplies the mod-2 and coefficient-change steps for arbitrary $R$ and treats closed components separately. This resolves the card's missing proof without asserting a repaired version of May's chart chain.

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
  The *replacement* is not certified: no Lean or Sage artifact establishes statements (i)–(iii) with closedness, so the card marks it proposed and the certification obligation is [#111](https://github.com/dzackgarza/new-qual-site/issues/111).

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
  The dataset does not bear that out: its unknown-year marker is `year: 0`, which appears on 191 rows and never once beside a real season, while `1970` appears only on these 20 rows and always beside one, exactly as 2005–2019 do on the sittings that really happened.
  **Revised 2026-11-01: `1970` is treated as an unverified imported label, not an attested examination date.** Being unlike the `0` sentinel shows only that a contributor typed a year here; it does not show the year is right, and nothing in the dataset or its products attests it (see the provenance trace appended below). `TermOnly` still correctly records that no collection uses it.
  A reader who disbelieves the dataset's year has nothing to replace it with, so the label stays and is marked as a label.

- **Repair:** both collections now carry a `provenance:` href pinning the dataset at that revision, and `source.date` records the academic term the dataset gives (spring 1970) instead of `unknown`.
  Where a card renumbers the source's parts, its entry carries the source letters as a comment, and the two repaired statements carry `source-corrected` audit notes naming the garbled bytes.
  The source question stays open as `ad-source-gaps-nus` ([#109](https://github.com/dzackgarza/new-qual-site/issues/109)): recovering the papers, or else marking both collections as imported-only, is what would close it. A pinned dataset is not a substitute.
  **2026-11-01:** the imported-only branch is now carried out -- both collection titles say the label is an unverified imported one, and both `provenance` lists carry the dataset's own per-university file as well as the combined one.

**Provenance trace, 2026-11-01: what the dataset actually records, and what it does not.**

*Verified.* The direct upstream files are `Questions/Complex_Analysis/NUS/NUS_Complex_Analysis.yaml` (2223 bytes) and `Questions/Real_Analysis/NUS/NUS_Real_Analysis.yaml` (6611 bytes) at the pinned revision `6190e0eeaf93ac471a2450444d0b70872b7b9dfa`; both were retrieved and both are now listed in the two collections' `provenance`. Their entries carry exactly seven fields -- `year`, `season`, `exam`, `number`, `university`, `tags`, `question` -- and **no source document, URL, paper identifier or sitting identifier**. The dataset's own `README.md` at that revision states that "the only *required* fields are year, exam, and question, and you can enter 0 for the year if it's not applicable", and its generated `Combined_Questions.md` numbers questions globally (`## Question 107`, `## Question 108`, ...) with no university, year or source attached. So these are contributor-entered metadata fields, and **the dataset names no original source**: there is nothing further to follow inside it.

*Recorded values, which are labels and not findings.* The Complex Analysis file's eight NUS rows carry `year: 1970`, `exam: Complex_Analysis`, question numbers 4, 5, 6, 6, 7, 7, 8, 8, and `season: Spring` on six rows and `spring` on two. The Real Analysis file's twelve NUS rows carry `year: 1970`, `exam: Real_Analysis`, and question numbers `1abch`, `1de`, `1fg`, 2, 3, 1, 2, 3, 4, 4, 4, 5. `sources/mmaq-reconciliation.jsonl` rows 108-115 and 194-205 tie each card to one of those rows.

*What those values do not establish, and are not used for here.* Repeated question numbers and mixed `Spring`/`spring` spellings are properties of imported metadata, not of any examination. They do not fix the date of the original examination, they do not show which institution set it or under what name, and they do not determine how many papers the statements came from: `number` is not a required field, so it may be inconsistent for reasons that have nothing to do with the underlying papers. Accordingly this entry makes no claim about the original year, institution, sitting or paper count, and no card's mathematics is adjusted on the strength of any of them.

*Access limit, for the database actually examined.* NUS Libraries' Examination Papers Database was examined through its library guide: the guide describes it as holding examination papers "of the National University of Singapore that were released by the Faculties/Schools", states that "access to the database is restricted to staff and students of NUS only", and lists an FAQ asking "Why is there only 5 years of exam papers in the database?". It could not be searched from here because of that restriction. No wider claim is made about the existence of copies elsewhere.

*Remaining obstacle.* **The original source is unidentified.** The dataset supplies no source identifier of any kind, so identifying the examination behind these twenty statements requires an external document that names it -- an examination paper, a university calendar or an examination-results notice held in a library or archive -- and that document has not been located or inspected. Until one is, both collections carry the dataset's values as an explicitly unverified imported label.

*Where the marking lives, and its limit.* The collection schema has one exam variant, `source_kind: university-exam`, and no free-text note field, so `source.date`, `source.institution` and `source.area` necessarily carry the dataset's values and cannot themselves say "unverified". The marking is therefore carried by the `title`, which says the label is an imported and unverified one and names the dataset's values, and by `provenance`, which points at the dataset's own files rather than at an examination. A structured imported/unverified variant would take a model change in `tools/qualc/model.py`; that is recorded here as the accurate fix for this class of collection and is not attempted in this pass.

*Upstream inspection, 2026-11-01: the history behind the two files, and where it ends.* The dataset's own git history was followed at the pinned revision rather than stopping at the seven fields, and it yields no source.

- **No source asset was ever committed for these two files.** At the pin, `Questions/Complex_Analysis/NUS/` and `Questions/Real_Analysis/NUS/` each contain exactly one file, the YAML; the same is true in `9c023922296e`, the commit that created both. The convention elsewhere in the same tree shows what a source asset would look like: `Questions/Complex_Analysis/Harvard/` carries `Complex Analysis.pdf` and `Questions/Complex_Analysis/UGA/` carries `AllQuestions.pdf` and `AllQuestions.md`. For NUS there is no PDF, no TeX, no scan.
- **The history cannot carry a provenance note.** Both files were created in a single commit, `9c023922296e` of 2020-05-19T16:23:00Z, which added 93 lines of `NUS_Complex_Analysis.yaml` and 186 of `NUS_Real_Analysis.yaml` together with an edit to `Questions/Complex_Analysis/UGA/Questions.yaml`. Its message is `Save`, and so is every other message on both paths (four commits for the complex file, eight for the real one). That is structural, not reticence: the repository's `Makefile` has an `update` target that runs `git add *; git commit -am "Save"; git push`, so automatic "Save" snapshots are how this tree was maintained. The `.sparkleshare` marker in the tree is consistent with that.
- **No script or template supplies a default year.** `make_md_doc.py` filters on `exam` and numbers questions `i+1` within each subject, `Makefile`'s `json` target concatenates the YAMLs, and `Webtool/app.py` samples them for the web tool. None touches `year`, `season` or `university`, and none has a fallback value. The README's only documented "not applicable" convention is `year: 0`.
- **The generated products attribute nothing.** `Combined_Questions.md` numbers `## Question 1..n` per subject; `Webtool/Frontend/AllQuestions.json` is a merge of the YAMLs; `Webtool/Frontend/Complex_Analysis.json` and `Real_Analysis.json` are both zero bytes.
- **Nothing else in the tree holds NUS material.** `Questions/Archive/` contains only Emory (`main.md`, `main.tex`, `main.pdf`); the notebook at `.ipynb_checkpoints/Untitled-checkpoint.ipynb` holds 593 characters of code with no URL and no mention of NUS, Singapore or 1970; there is a single branch (`master`) and the repository has zero issues and zero pull requests, so no contribution record exists to consult.
- **No cross-label lead inside the dataset.** Not one of the twenty NUS questions occurs elsewhere among the 508 rows, and no non-NUS row carries `year: 1970`.

*What this settles, and what it does not.* There is **no original filename and no URL anywhere in the inspected upstream record**, and there is **no evidence that `1970` is a placeholder or a default**: the documented placeholder is `0`, no code path produces `1970`, and the value is simply one a contributor entered in a file created on 2020-05-19. That is the whole of what the record supports. It does not tell us whether 1970 is right, which institution set the questions, or how many papers they came from. This is the inspected dead end: further progress on the source needs a document from outside the dataset.

*Text-search pass on the statements themselves, 2026-11-01.* A second bounded route was tried: search distinctive exact wording from the two pinned files against public university and author archives, selecting statements by their mathematics rather than by the `NUS`/`1970`/`Spring` labels. Every query below was run as an exact-phrase or near-exact search; card ids are from `sources/mmaq-reconciliation.jsonl`.

| Statement searched (card) | What the search returned |
| --- | --- |
| `P-3T5VY`, CA 4: "number of zeroes, counting multiplicities, of $2z^5-6z^2-z+1$ in the annulus $1\le|z|\le 2$" | The same question on several *US* qualifying exams, but printed with $+z$: University of Iowa, Analysis Qualifying Exam, Friday 12 January 2024 (`math.uiowa.edu/.../Spring-2024_0.pdf`), Problem C-3; UC Irvine Complex Analysis Qualifying Exam, June 2013 (`math.uci.edu/.../Qual%20Complex%20June%202013.pdf`), Problem 5; UC Irvine, September 2012 (`.../Complex-qulifying-sept-2012.pdf`), Problem 4; Johns Hopkins analysis-exam compilation (`math.jhu.edu/gradexam/analysisexams.pdf`), Question 7 — and a Mathematics Stack Exchange thread. **Conflicting wording recorded, not resolved:** every published version found has $+z$, the corpus has $-z$. |
| `P-BCFIC`, CA 5: analytic isomorphism from the region between $|z|=1$ and $|z-\frac12|=\frac12$ to the upper half plane | Quoted as a question, verbatim, on Mathematics Stack Exchange (`math.stackexchange.com/questions/1600536`); no examination paper. |
| `P-F2QGV`, CA 6: analytic isomorphism from between $x=1$ and $x=3$ to the upper half unit disk | Quoted as a question, verbatim, on Mathematics Stack Exchange (`.../questions/3315348`); no examination paper. |
| `P-MMAQ-S7C4CCIUTP`, CA 6: "Use Green theorem or otherwise to prove the Cauchy theorem" | **No exact hit.** The results were generic treatments of deriving Cauchy's theorem from Green's theorem (MathWorld; a Purdue course note; a PRIMUS article). |
| `P-MMAQ-TCJZEHD655`, RA 1: "$\limsup a_n\le l$ implies $\limsup\sum_{i=1}^n a_i/n\le l$" | Quoted as a question, verbatim, on Mathematics Stack Exchange (`.../questions/1468865`), where the asker describes it only as "a PhD qualifying exam of a certain school" — **the asker does not name the school**. |
| `P-Y3TRT`, RA 3: the recurrence $f_n(x)=\int_0^{x-1/n} g(t,f_n(t))\,dt$ on $[0,1]$ | No match; results were unrelated sequences of functions. |
| the parenthetical "You may leave your result as a composition of functions", which appears on CA 5 and CA 6 and so is an instructor's fingerprint | **No exact hit.** University of Michigan papers use the different wording "You may write your solution as a composition of simpler maps". |

*Corroboration against the full papers, 2026-11-01.* Each concrete candidate was then downloaded and read, not trusted from a snippet, so that the item could be checked in place with its sign and its neighbouring questions. The retained item is `P-3T5VY`, CA 4: "Find the number of zeroes, counting multiplicities, of the polynomial $f(z)=2z^5-6z^2-z+1=0$ in the annulus $1\le|z|\le 2$."

| Paper | Verified retrieval | Where the item sits | Sign printed | Annulus printed | Verdict |
| --- | --- | --- | --- | --- | --- |
| University of Iowa, Analysis Qualifying Exam, Friday 12 January 2024 | `https://math.uiowa.edu/sites/math.uiowa.edu/files/2026-04/Spring-2024_0.pdf`, HTTP 200, 22 pages | Part II (Complex Analysis), **Problem C-3**, PDF page 16 | $+z$ | "the annulus ann(0; 1, 2) of radii 1 and 2 centered at the origin" | **related, not exact, for the polynomial**: wording "Determine the number of zeros of $p$ (counting multiplicities) inside the annulus", and the sign differs. **Separately, the same paper's C-1 on page 12 is an exact match at the level of the mathematical item retained as CA 8**: it prints $\int_0^\infty x^2/((x^2+1)(x^2+4))\,dx$, identical integrand and limits, under the different instruction "Use complex analysis methods to calculate" |
| UC Irvine, Complex Analysis Qualifying Exam, Tuesday 18 June 2013 | direct URL `.../files/Qual%20Complex%20June%202013.pdf` now **HTTP 404**; read from `http://web.archive.org/web/20250207043933/https://www.math.uci.edu/sites/math.uci.edu/files/Qual%20Complex%20June%202013.pdf`, HTTP 200 | **Problem 5** of 8, PDF page 6 | $+z$ | "$1\le|z|\le 2$" (closed) | **related, not exact**: "Determine the number of roots, counted with multiplicity, of the equation … inside the annulus" |
| UC Irvine, Complex Qualifying Examination, 20 September 2012 | direct URL `.../files/Complex-qulifying-sept-2012.pdf` now **HTTP 404**; read from `http://web.archive.org/web/20250207054613/https://www.math.uci.edu/sites/math.uci.edu/files/Complex-qulifying-sept-2012.pdf`, HTTP 200 | **Problem 4** of 9 (choose 8), PDF page 5 | $+z$ | "$A(0,1,2)=\{z: 1<|z|<2\}$" (open) | **related, not exact** |
| Johns Hopkins, Analysis Qualifying Exam **Spring 2016** | direct URL `https://math.jhu.edu/gradexam/analysisexams.pdf` now **HTTP 403**; read from `http://web.archive.org/web/20240604033928/https://math.jhu.edu/gradexam/analysisexams.pdf`, HTTP 200, 57 pages | **Question 7** of that exam, PDF page 11 of the compilation | $+z$ | "$1\le|z|\le 2$" (closed) | **related, not exact**: "Determine the number of zeroes of the polynomial … $=0$", with no "counting multiplicities" |

*Verdict of the corroboration step.* Every one of the four papers prints $+z$; the retained text prints $-z$. **This is a verified conflict between the corpus and four page-checked witnesses, and it is recorded as a conflict, not used to correct the corpus**: no paper here is established as the source of the retained item, so the corpus may equally be reproducing a source that printed $-z$, and the rule against correcting a statement from a related exam holds. The sign must stay as the corpus has it until an original is identified or the transcription's own history is traced.

*What the sequence comparison does, and what it does not show.* None of the four documents carries the whole retained complex-analysis sequence: Iowa's complex part is C-1 to C-4 with either/or sub-problems C-2A/C-2B and C-4A/C-4B; UC Irvine 2013 has eight numbered problems; UC Irvine 2012 has nine, choose eight; Johns Hopkins Spring 2016 has seven questions mixing real and complex analysis. Those surrounding items of the retained list are also absent from all four: the string "Green" does not occur, "divergence theorem" does not occur, and neither the retained isomorphism pair, nor the $\int_0^{\pi/2} dx/(3+\sin^2 x)$ residue item, nor "Use Cauchy's theorem to prove the argument principle" appears. The single "Argument Principle" occurrence, at question 7 of a *different* exam inside the Johns Hopkins compilation, is a different exercise ("use the Argument Principle to show $f^{-1}(Q)$ contains at least two points"), related in name only.

*Chronology, which limits which papers could be a source at all.* The import file was created in commit `9c023922296e` on 2020-05-19T16:23:00Z, and each paper's date is printed on its own first page: Iowa, Friday 12 January 2024; UC Irvine, 18 June 2013 and 20 September 2012; Johns Hopkins, Spring 2016. **The Iowa 2024 paper postdates the import by nearly four years, so it cannot be the source of any row in it**; at most it is a later witness to the same exercise, or shares an earlier source with whatever the row came from. The other three predate the import and are therefore not excluded on chronological grounds.

**That absence does not identify a source at the collection level, and it does not exclude any of the papers that predate the import as a contributing source for an individual imported row** — the Iowa paper being set aside on chronology alone, not on content. The comparison is about the collection as a whole, and the retained labels and question numbers are contributor-entered metadata that need not preserve any paper's ordering, so a single row could have been taken from any of the documents that predate the import, without leaving a traceable sequence. Conversely, none of the four is *shown* to be the source of even one row: a shared statement in differing wording, with the opposite sign, is a related problem, not a recovered original. The same caution applies to the search failures: absence from these four documents is not evidence about where the twenty rows came from.

*What this pass establishes, and what it does not.* It establishes that these are circulating course and qualifying-exam statements without an attributed home: three of the twenty are quoted verbatim as questions in public threads whose askers name no source, and one recurs on four identifiable US qualifying exams in differing wording, with a closed or open annulus and the opposite sign. It establishes **no** original paper. It does record **one exact match at the level of an individual mathematical item** -- the improper integral $\int_0^\infty x^2\,dx/((x^2+1)(x^2+4))$, retained as CA 8 and printed at Iowa C-1, page 12, with identical integrand and limits and different surrounding instruction -- and that match attributes nothing: the integral is a standard exercise, and an exact match of one item is not an identification of where a collection came from. Everywhere else in these four documents there is no exact match, of wording or of the mathematical item. The original source remains unidentified, and no common source is inferred for the twenty rows from witnesses that disagree with them.

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

- **Repair:** the vertex symbol and the twelve spans are fixed in place.
  The check this entry said did not exist now does: `tools/check_macros.py` extracts every `\word`
  from named files and reports those in neither `vocabularies/macros.json` nor MathJax's command set.
  Run over all 14 362 tracked card files on 2026-11-02 it flagged 724 of them, all but four of them
  falsely, and the same day the checker was fixed to read the dialect the site actually supports
  rather than a widened allowlist: it now reads each card through `qualc.tex.checkable_tex`, which
  rewrites the one supported prose command `\dfn{term}` out with the pipeline's own parser
  (`mark_definienda`), blanks code spans and tikzcd environments (compiled to SVG by the emitter,
  skipped by `unrenderable_tex` too), and strips the YAML front matter exactly as
  `qualc.authoring check` does, so YAML escapes such as `"Rouch\xE9"` and note prose such as `X\C`
  are never scanned. The four residual flags were all of that last class: `\xE` in `P-BKF80-18`,
  `\O` in `P-T06Q2-2`, `\C` in `P-T17Q1-3`, `\H` in `P-AMD-MU3IE25C`, each in front matter, none
  a mathematics defect. One further refinement, same day: rendered metadata is scanned with the body,
  because the site typesets it -- `title`, `slogan` and `prompts` are Markdown per
  `model.typeset_dashes`, which preserves their `$...$` spans -- so `title: '$\undefinedword$'` on an
  otherwise valid card fails the check, while audit notes stay unscanned and the front matter is read
  through the YAML loader, so `"Rouch\xE9"` decodes before the scan. The corpus-wide run is now clean:
  0 of 14 362 files flagged, with the glued (`\mapstov_1`), undefined (`\q`) and rendered-metadata
  detections pinned by `tests/test_check_macros.py`.

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

**Closed 2026-11-02.** The citation is now to the source consulted — Fukasawa, arXiv:2108.00650v3, §1 — whose hypotheses were checked against the step; the primary reference is kept as an alternate and is not claimed to have been read. See item 4 of the numbered list at the end of this file.

## The five `ad-text-*` nodes that cannot be read: their books are not in the repository

- **Object and need:** the `ad-text-hart77` ([#102](https://github.com/dzackgarza/new-qual-site/issues/102)), `ad-text-hun74` ([#103](https://github.com/dzackgarza/new-qual-site/issues/103)),
  `ad-text-smi` ([#104](https://github.com/dzackgarza/new-qual-site/issues/104)), `ad-text-mun00` ([#106](https://github.com/dzackgarza/new-qual-site/issues/106)) and `ad-text-hk71-locators`
  ([#108](https://github.com/dzackgarza/new-qual-site/issues/108)) work units, each of which requires reading every card of its
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
## What the audit campaigns installed, and what is still open

Recorded so that "swarm ended solved" and "queue 0" are not read as "the collection is verified".
The audits covered `SRC-TEXT-HAT02` §3.D, §3.F, §3.H, §4.1 (ex. 10–23), §4.2, §4.3, §4.A/§4.B/§4.D/
§4.F/§4.G/§4.H/§4.I/§4.K/§4.L, and `SRC-TEXT-SS03` for completeness and statement fidelity, plus the
nine printed SS03 items that had no card.

**Installed and gated.** Statement restorations on 40+ cards (dropped printed hints, pointers,
parentheticals and printed sentences; one halved "iff" in `E-HAT-4.3-22`, one in `E-HAT-3.F-9(a)`, one
in `E-HAT-4.1-19`, one in `E-HAT-4.1-22`); proof repairs in `E-HAT-3.F-2/3/7` and `E-HAT-3.H-2/4/5`;
a full replacement proof for `E-HAT-4.3-24`, which had none; solutions for `E-SS3.PR-3/4/5`,
`E-SSA.PR-1/2/3/4/5`; the Airy label correction on `E-SSA.PR-3`.

**Explicitly open — not completion, not oversight.**

1. **`E-SSA.PR-5` final sentence — closed by citation, 2026-11-01.** The exercise's closing claim is
   Rademacher's theorem. §4 of that card now states the exact formula with Dedekind-sum coefficients,
   his remainder bound ($|A_k^*(n)|<2k^{1/3}$, remainder $O(n^{-1/4})$ uniformly for
   $N\ge\lfloor\sqrt n\rfloor$), and cites Rademacher, PNAS **23** (1937) 78–84
   (doi:10.1073/pnas.23.2.78) and Trans. AMS **43** (1938) 271–295 (doi:10.2307/1990043), with Lehmer,
   J. London Math. Soc. **12** (1937) 171–176 for the divergence of the Hardy–Ramanujan series. It
   distinguishes the three series explicitly: the asymptotic one with $N$ coupled to $n$ (divergent to
   infinity), Rademacher's with $N$ decoupled (convergent, equal to $p(n)$), and the book's single-term
   shape whose coefficient is constant only at $q=1$. Checked: the $q=1$ reduction to the book's
   Theorem 4.1(ii), and the finite check that truncating at $N=\lfloor\sqrt n\rfloor$ and rounding gives
   $p(n)$ for $n\le12$. **Not claimed:** a re-proof of Rademacher's theorem — that is the book's
   omission, and it is cited, not reproduced.
2. **97 proofs never read.** The statement layer of all 137 previously unread HAT02 cards was audited,
   but 97 of their proofs were marked unread, not correct: §3.F 4–9, §4.A-4, §4.A-5, §4.1 10–23,
   §4.2 (39), §4.3 (24), §4.D (10), §4.L-4, §4.L-5. The known defects inside that set are the ones
   reported and repaired above; the rest is unaudited.
3. **`E-HAT-3.C-16`, the mod-$p$ classification: RESOLVED, on a consolidated development (2026-11-01).**
   The exercise is read from the source — Hatcher, printed p.292 (PDF page 301). The card now carries one
   numbered development, replacing four contradictory audit notes and their superseded numbering.
   **Lemma 1:** a graded basis-to-basis map $\phi(\bar x_n)=u_n\bar y_n$ is an isomorphism iff both the
   product equations $\bar m'_{ij}u_iu_j=\bar m_{ij}u_{i+j}$ and the coproduct equations
   $\bar c'_{ij}u_{i+j}=\bar c_{ij}u_iu_j$ hold; both are needed, since where $\bar m_{ij}=0$ the first is
   vacuous and the second need not be. **Lemma 2:** which of the two bites, in the three cases
   $e_{ij}=0$, $0<e_{ij}=f_{ij}$, $0<e_{ij}<f_{ij}$ (the last vacuous on both sides). **Theorem 3:** if
   $v_p(m_{ij})=v_p(m'_{ij})$ for all $i,j$ then the reductions are isomorphic, with the explicit
   $\phi(\bar x_n)=\omega_n\bar y_n$, $\omega_n$ the unit part of $q_n/q'_n$ — the three case computations
   were re-verified by hand. **Theorem 4:** an isomorphism forces the two bits $[v_p(m_{ij})>0]$ and
   $[v_p(m_{ij})=v_p(b_{ij})]$ to agree. **Corollary 5:** reductions are isomorphic iff the flags
   $(\delta,\varepsilon)$ agree *and the least degrees $d$ agree*. **Four of my own claims are retracted:**
   that the reductions are *not* determined by the valuations (they are); that for $p=2$ the support
   classifies them; that the product system "may be unsolvable"; and, new here, that the flag alone
   classifies across different $d$ — the polynomial forms with $d=1$ and $d=2$ have identical flags, by
   Kummer's formula applied to both coefficient families, yet $B_1=\ZZ/2$ versus $B_1=0$. Three further
   defects were found and fixed in the same pass: the polynomial form's second flag bit is
   $[p\nmid b_{ij}]$, not identically zero; the divided-power form exists only for $d$ even; and
   Lemma 2(a)'s "both equations reduce to the same thing" fails where $b_{ij}\equiv0\bmod p$.
   **Not claimed, and stated as such on the card:** no realisation theorem for every flag pattern (only
   that a realisable one determines the class, plus the two extreme families and the
   $m_{ij}=p^{e_{ij}}$ family), and no decision procedure — the flags are infinitely many bits, so
   Corollary 5 is a criterion, not an algorithm.
4. **`P-AGH467MULTISECANTS` — closed 2026-11-02 on the consulted restatement (was: attribute misidentified, body unread).**
   The step `#tangent-char-zero` needs Kaji's characteristic-zero theorem. The abstract quoted for it
   originally was the *2014 sequel's*, not the 1986 paper's — the 1986 Crossref deposit has no abstract,
   Waseda's 1986 record has none while its 2014 record carries exactly that text, and that text names
   Esteves–Homma, whose method is the 2014 paper's own reference [3]. That is corrected on the card and
   stands corrected here. What the card now cites is the source actually consulted and read: Fukasawa,
   *A generalization of Esteves–Homma's example of tangentially degenerate curves*,
   arXiv:2108.00650v3, §1, which states the definition (irreducible $C\subset\PP^N$, $N\ge3$, not in a
   plane, over an algebraically closed field) and Kaji's result in the form "for the case where $p=0$
   and the morphism $X\to\PP^N$ induced by the normalization $\phi\colon X\to C$ is unramified, the
   nonexistence of such curves was proved by Kaji [6] in 1986". Each hypothesis was checked against the
   step, where $X$ is a smooth nonplanar curve in $\PP^3$ over $\CC$, so the normalization is an
   isomorphism and hence unramified. Kaji's original, J. London Math. Soc. (2) **33** (1986) 430–440,
   is kept as the primary reference and is not claimed to have been read; the access attempts are on
   record and are not a blocker. Unchanged and still open on that card: steps `s1`–`s13` are not
   re-derived.

5. **Starred markers — Stein–Shakarchi only, and checked.** No `SRC-TEXT-SS03` card records which
   printed items carry the difficulty asterisk; reports this week put the number of starred printed
   items between 26 and 28 and only `E-SS2.PR-5` mentions its star. For `SRC-TEXT-HAT02` the question
   is closed: Hatcher marks no exercise with an asterisk. The PDF text layer of `tmp/hat/AT.pdf`
   contains 2085 occurrences of `∗` and all of them are the join `X ∗ Y` or the same symbol inside a
   formula — no line begins `N.∗`, and the pattern `d.∗` occurs nowhere. So absence of a star on a
   Hatcher card is correct, not a defect, and nothing was invented in its place.
6. **Five `ad-text-*` nodes** stay blocked on books absent from the repository, as recorded above.

7. **Published-solution coverage gaps — open, 2026-11-07.** These are source obligations, not claims that the displayed mathematics is false. `E-HAT-3.3-21` has a checked degree-two counterexample, but Eda–Kawamura and Wiegold are supporting theorems, not a complete published solution to Hatcher's bracketed question; that complete solution has not been located. `E-HAT-2.B-3` and `E-HAT-2.B-4` also need complete published solutions; MSE 4771220 does not supply the full homeomorphism/deformation argument for 2.B-4(a). `E-HAT-2.B-5` is source-covered at the argument level: the MSE 4773641 pair/excision construction is now checked step by step in the card — the auxiliary `ell` an open half-sized `k`-disk, the excision closure condition verified inside `X = S^n - D'`, `D` acyclic by star-shapedness and `X` acyclic by Hatcher Proposition 2B.1(a) after the coordinate chart is used to show `D'` is a `k`-manifold with boundary so that Putman's generalized Schoenflies theorem applies. That thread is an unreviewed user answer, not a peer-reviewed publication, so the card records verification of the argument and does not accept the source by attribution. Its checked Alexander-intersection proof and `k = n` case are retained, and no source defect is claimed based on the retracted interior-of-A-minus-Z condition. `E-HAT-2.B-7` has no identified published analysis of the doubled block. Finally, `E-HAT-2.B-9` and `E-HAT-2.C-6` are specializations of general published results, not found complete exercise solutions; their source obligations also remain open. Book pages carrying only statements do not discharge the #105 transcription contract. Preserve all correct proofs without calling those obligations closed. The same cause leaves two `SRC-TEXT-HART77` items open. `P-AGH359NONPROJ` (III.5.9) still needs a published solution: no retained set supplies the computation $\delta(\OO(1))\ne0$ — the Saglam–Chris solutions cover 5.1, 5.2b, 5.3a, 5.4, 5.5b, 5.7ab and 5.10 on pp. 133–138 and leave 5.6, 5.8 and 5.9 blank; Egbert p. 177 states "The only part of the hint which is not clear is that δ(O(1)) ≠ 0" and stops at the Čech complex `0 → k[t_0,t_1,t_2]_(t)`; Park proves only 5.6 (pp. 20–23); Stein covers only 4.8, 4.9 and 5.6 of Chapter III; and Sam, Cais, Lomont, Cutrone–Marshburn and Borcherds reach no III.5 exercise at all (Sam's text layer is mirrored and had to be reversed before searching, and it stops at Chapter IV). The online argument in MathOverflow question 96177 was read through the Stack Exchange API rather than dismissed for lacking pages: its accepted answer, `/a/96178` (Will Sawin), settles only that the extension splits on each $U_{ij}$ and explicitly defers the cocycle computation ("I will think about how to do that"), and the asker's own answer `/a/96274` reproduces McKernan's lift and 2-cocycle. Judging that answer by its mathematics rather than by its author's confidence leaves a specific missing implication: the lift is asserted as $\phi(\beta_0)=x_2/x_1+\eta_{12}(x_0/x_1)d(x_2/x_0)\wedge d(x_1/x_0)$ with no derivation, while the cocycle it is meant to lift is $\alpha=(x_1/x_0,\,x_2/x_1,\,x_0/x_2)$ on $U_{01},U_{12},U_{20}$ respectively, so the nilpotent part carries the index $12$ where the chart is $U_{01}$ and the identity cannot be checked as written; the derivation attributed to $\xi_{ij}$ is displayed only for $(i,j)=(0,1)$, and the answer does not say how the other overlaps reduce to it. With that step supplied the argument does finish, and the class it produces is the nonzero one, a unit multiple of the $1/(x_0x_1x_2)$ computed in the card's step; the source does not supply the step. McKernan's primary notes were searched for and not located: his 18.726 course page (math.mit.edu/~mckernan/Teaching/11-12/Spring/18.726/18.726.html) lists no exercise solutions, and no other copy was found. That gap is now supplied by a complete published proof, so the III.5.9 obligation is closed. Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry*, Chapter III §5 Exercise 5.9, release PDF pp. 154–156, source revision `6c627eed7b0226249df79b8777f5ac450f17885a` (`src/03-05-the-cohomology-of-projective-space.tex`), gives the exact sequence of Čech complexes, the gluing matrix with $d(-)\wedge\xi_{ij}$, the product of the three lifted transition units and the Laurent-cokernel computation isolating $e_{12}+e_{23}+e_{31}$, hence $\delta(\OO(1))\neq0$ and $\Pic X'=0$. Its local slips are recorded on the card rather than treated as gaps: coordinates written $x_1,x_2,x_3$ for $x_0,x_1,x_2$, a $1$ printed as $0$ in the multiplicative pair, and a cyclic $e_{12},e_{23},e_{31}$ convention for the wedges. The earlier MathOverflow thread (question 96177, answers `/a/96178` and `/a/96274`) is cited on the card only for the construction, since its final displayed coefficient $-\eta/v$ extends over $U_{02}$ and its frame is not stated. McKernan's own notes were not located and his 18.726 course page lists no solutions.

### III.7.4(b), (d) have no complete published solution in the sets inspected

**Object and need.** `P-AGH374COHOMCLASS` (Hartshorne III, Ex. 7.4, printed pp. 249–250, starred) needs a published proof of (b) $\eta(Y)=(\deg Y)\cdot1$ for $X=\PP^n$ and of (d) $\eta(Y)=c(\mathcal L(Y))$ for $p=1$, to meet the standing published-solution requirement independently of the card's own derivation.

**Observed evidence.** Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry*, Chapter III §7 Exercise 7.4, release PDF p. 170, revision `6c627eed7b0226249df79b8777f5ac450f17885a`, proves (a) and (c) and writes `\todo{todo}` in place of (b) and (d) in the authored source `src/03-07-the-Serre-duality-theorem.tex`. A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*, III.7.4, **p. 187**, carries the single word `MISS`: his preface states that starred questions were skipped. The Stein notes contain only III.7.1 and III.7.3; Saglam–Chris, Park, Cais, Sam, Lomont, Cutrone–Marshburn and Borcherds contain no III.7 exercise (their Chapter III coverage stops earlier), and the Wikibooks set lists III.7 with solution 3 only.

**Impact and owner.** The card's own proof of (b) and (d) is complete and was read; what is missing is a published argument to check it against. The III.7 section is therefore not source-complete on this item, and no claim to the contrary is made.

**Uncertainty.** Searched: the ten retained sets and Kim's authored source; the release PDF for each exercise head. Found: (a) and (c) only. Conclusion: no complete published solution for (b) and (d) among them. Confidence: high for these sets. Gaps: a published argument may exist outside them; it has not been located.

**Repair.** A source supplying (b) and (d) checked against the book, or the owner's direction to accept the agent-authored derivation for these parts.

### IV.1.8(c) — no complete published solution in the supplied collection

**Object and need.** `P-AGH418ARITHGENUSSINGULAR` (Hartshorne IV, Ex. 1.8, part (c), starred): δ_P depends only on the analytic isomorphism class of the singularity, with δ_P = 1 for an ordinary cusp and for a node.

**Observed evidence.** The card's own proof is complete: completion commutes with normalization for an excellent reduced 1-dimensional local ring, giving δ_P = length_Â((Â̄/Â)), and the explicit computations k[[t]]/k[[t²,t³]] ≅ k·t and (k[[x]]×k[[y]])/Â for the node. What is missing is a published proof to check it against.

- A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*, IV.1.8 pp. 208–209, proves only the genus formula of (a) and the nonsingularity of (b); he does not supply (c). His stated practice is to skip starred questions, and his Table of Contents carries no entry for the starred part of 1.8.
- Jinhyun Park, *Solutions to Hartshorne's Algebraic Geometry*, Chapter IV Section 1, p. 1, contains only IV.1.1–IV.1.3 and passes directly to Chapter V.
- Lomont, *Solutions to Hartshorne's Algebraic Geometry*, Chapter IV Section 1, likewise covers 1.1–1.5 only, not the starred 1.8(c).
- Kim covers Chapters I–III only and has no Chapter IV section.
- The remaining retained sets: Saglam–Chris, Sam, Borcherds and Stein contain no Chapter IV exercise; Cais covers IV.1.1–1.7 and 1.10 and Cutrone–Marshburn covers IV.1.1–1.8(a),(b), so neither supplies 1.8(c).

**Impact and owner.** The other IV.1 exercises have published arguments in the retained sets (Park and Lomont for 1.1–1.3, Egbert elsewhere, including the singular-curve Riemann–Roch of IV.1.9); IV.1.5 and IV.1.10 assert their decisive step, which is recorded in the IV.1–IV.3 entry below. IV.1.8(c) lacks any published proof. It remains an open obligation under #102, together with III.7.4(b),(d).

**Uncertainty.** Searched: all ten retained solution sets plus Kim. Found: nothing for IV.1.8(c). Conclusion: no published coverage among them. Confidence: high. Gaps: a published treatment may exist outside these sets; it has not been located.

**Repair.** A published proof of Hartshorne IV, Ex. 1.8(c), checked against the card's analysis.

### IV.1–IV.3 — the parts whose retained entries assert the decisive step

**Object and need.** Cards of `SRC-TEXT-HART77` IV.1–IV.3 whose cited published entry does not prove the exercise: `P-AGH415DIMLEQDEG` (IV.1.5), `P-AGH4110PICOFARITHGENUSONE` (IV.1.10), `P-AGH422GENUSTWOMODULI` (IV.2.2), `P-AGH423DUALCURVE` (IV.2.3(h)), `P-AGH434RATIONALNORMALCURVE` (IV.3.4(a)), `P-AGH4312NODALCURVESEXIST` (IV.3.12). IV.1.8(c) and IV.3.11(a) are recorded in their own entries above.

**Observed evidence.** The retained sets covering Chapter IV are Park (Chapter IV §1 only, exercises 1.1–1.3), Lomont (Chapter IV §1, exercises 1.1–1.5), Cais (Chapter 4 §1, exercises 1.1–1.7 and 1.10), Cutrone–Marshburn (Chapter 4 §1, exercises 1.1–1.8) and Egbert; no retained set covers IV.2 or IV.3 except Egbert.

- IV.1.5, Egbert printed **p. 207** and Lomont **p. 4**: "Note that equality holds when $h^0(K-D)=h^0(K)$ so when $D=0$ or $g=0$" — the characterization is asserted. Cutrone–Marshburn, Chapter 4 §1 exercise 5, argues "Conversely, suppose that $h^0(K-D)=h^0(K)=g$ and $g>0$. Then $h^0(K-D)=h^0(K)$ so $D\sim0$", which does not follow: equal dimensions give only $L(K-D)=L(K)$, and the standard consequence is $\ell(P)=2$ for $P\in\operatorname{Supp}D$, hence $X\cong\PP^1$. The card's steps 5–7 supply that argument.
- IV.1.10, Egbert printed **pp. 209–210** and Cais Chapter 4 §1: Egbert concludes "$\dim|D+P_0|=0$" and leaves the bijection at that; Cais (exercise 1.10) gets $(f)+D+P_0=P$ for some point and then says $P$ is "necessarily in $X_{\mathrm{reg}}$ as $D$ is supported in $X_{\mathrm{reg}}$", which is not argued (that $P$ is regular needs $\OO_{X,P}/(a)\cong k$, hence a principal maximal ideal). The card's step 6 supplies it.
- IV.2.2, Egbert printed **p. 210** and pp. 211: parts (a) and (b) are argued, part (c) is "Each case is given in Rudin 14.3", part (d) is "nothing to do here. Are you trying to make me do group theory?" and part (e) is "Clear from parts a–d". The $\Sigma_6$-action of (d) and the bijection of (e), which are the exercise's conclusion, have no proof.
- IV.2.3, Egbert printed **p. 212** and following: parts (a)–(g) are argued, part (d) as a printout of a symbolic root-finder, but part (h) — the quartic count with a four-fold contact tangent, the one case the printed statement singles out — has no entry.
- IV.3.4, Egbert printed **p. 219**: part (a) is one line, "Since $\PP^1$ is projectively normal, then d-uple is projectively normal. If $\theta$ is the corresponding ring homomorphism, then the kernel is generated by quadrics"; projective normality of the $d$-uple embedding and quadratic generation of its ideal are what the exercise asks to be shown. Part (b) is argued.
- IV.3.12, Egbert printed **p. 224**, headed "just explain the advanced method": a six-step recipe (write the singularity at $(0,0,1)$, expand in $z$, require $z^{d-2}f_2$ nonzero, check the discriminant, then "check for genus in Sage easily … c…"), with no curve built and no proof.

**Impact and owner.** Every card listed has its own complete proof: IV.1.5 by the nested section spaces $L(K-D)\subseteq L(K-P)\subseteq L(K)$ and the resulting $\ell(P)=2$; IV.1.10 by the exact sequence with $\OO_Z(E)$ and the principal-maximal-ideal criterion for regularity; IV.2.2 by Hurwitz, by the uniqueness of the degree-two morphism, and by the explicit $\Sigma_6$-action on triples; IV.2.3 by the $E_6$ cusp computation $\delta=3$ at a hyperflex so that $b+h=28$; IV.3.4 by the monomial straightening and dimension count $\dim(R/J)_m=md+1$; IV.3.12 by the maximally nodal rational curve, $H^1(\mathcal I_N(d))=0$ and independent smoothing of nodes. The published-solution obligation stays open under #115 for these six, and no card's proof is a transcription of a published one.

**Uncertainty.** Searched: all retained sets in `tmp/sources` that reach Chapter IV — Park, Lomont, Cais, Cutrone–Marshburn, Egbert (Dongryul Kim stops at Chapter III; Borcherds, Sam, Stein, Troiani, Saglam–Chris, Okamoto have no Chapter IV exercise). Found the passages quoted. Conclusion: no complete published solution of these parts among them. Confidence: high for these sets; the Egbert pages were read in the `pdftotext -layout` extraction, whose table of contents fixes the printed pages. Gaps: Chapter IV of the twenty-odd sets *not* retained was not searched; Rudin's *Real and Complex Analysis* 14.3 was not consulted.

**Repair.** A complete published solution of each part, or the owner's direction to accept the card's derivation.

### IV.4.22 and IV.6.9 — no complete published solution in the supplied sets

**Object and need.** `P-AGH4422FAMILYOVERAFFINELINE` (Hartshorne IV, Ex. 4.22, printed as `\*4.22`, starred) and `P-AGH469NONSINGULARSURFACECONTAININGACURVE` (IV, Ex. 6.9, printed as `\*6.9`, starred).

**Observed evidence.**
- A. Egbert, *Solutions to Hartshorne's Algebraic Geometry*, IV.6.9: the entry on doc p. 253 consists of the heading followed by the single word `skip.`, so there is no argument at all.
- For IV.4.22 Egbert has entries `4.4.22 b.` and `4.4.23 c.` (doc p. 237) which consist of citations — "by Silverman, thm 6.2, (page 52??)" and "This is theorem VI.5.5 Silverman since integral means a finitely generated module contained in Q(τ)" — not the triviality argument the exercise asks for. The printed hint's route (2-torsion points forming an étale cover of $\AA^1_\CC$, hence trivial as $\AA^1_\CC$ is simply connected, so $\lambda$ is defined and the map to $\AA^1\setminus\{0,1\}$ is constant) is not carried out there.
- The other sets give no coverage: park, lomont, sam, cais, stein, borcherds, saglam-chris and cutrone-marshburn contain no treatment of either exercise (keyword searches for the degree-$m$ surface and the family triviality return only unrelated Chapter II/V material).
- Kim's source stops with Chapter III and covers no Chapter IV exercise.

**Impact and owner.** Both cards carry complete multi-step proofs of their own (IV.4.22 in 7 steps following the printed hint, IV.6.9 in 8 steps via the blow-up of $X$ in $\PP^3$ and a general hyperplane containing no exceptional fibre). What is missing is a published argument to check against, so these are open published-solution obligations under #102 alongside III.7.4(b),(d) and IV.1.8(c). The remaining Chapter IV exercises do have published treatments in Egbert (ss. 4.1–4.21, 5.1–5.7, 6.1–6.8) and Park/Lomont for the earlier sections.

**Uncertainty.** Searched: all ten retained solution sets plus Kim's chapter sources. Found: nothing beyond the citations noted for IV.4.22, and an explicit `skip.` for IV.6.9. Conclusion: no complete published solution among them. Confidence: high for these sets. Gaps: a published treatment may exist outside them; it has not been located.

**Repair.** A complete published solution of IV.4.22 following the printed hint, and of IV.6.9, checked against the cards.

### IV.3.11(a) — published sources cite Shafarevich instead of proving it

**Object and need.** `P-AGH4311PROJECTIONCLOSEDIMMERSION`, Hartshorne IV Ex. 3.11(a): for a nonsingular variety $X\subseteq\PP^n$ of dimension $r$ with $n>2r+1$, exhibit $O\notin X$ whose projection induces a closed immersion into $\PP^{n-1}$.

**Observed evidence.** A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.11, printed p. 223 (entry 4.3.20), gives the whole of part (a) as "This is Shafarevich Algebraic Geometry 1, theorem 9, page 136" — a citation, not an argument. His entry 4.3.21 then proves part (b), the Veronese secant-variety computation, in full. Park and Lomont do not reach IV.3; the remaining retained sets contain no IV.3 exercise.

**Impact and owner.** The card's own proof of (a) is complete: separate points and tangent vectors by a projection center outside the corresponding proper closed loci, the dimension count $n>2r+1$ guaranteeing the center exists, then (II, 7.3) for the closed immersion. That derivation is not a published solution, so the obligation stays open under #102 alongside III.7.4(b),(d), IV.1.8(c), IV.4.22 and IV.6.9.

**Uncertainty.** Searched: Egbert, Park, Lomont, Saglam–Chris, Cais, Sam, Cutrone–Marshburn, Borcherds, Stein, Kim (Chapters I–III only). Found: the Shafarevich citation, and Egbert's full treatment of (b). Conclusion: no complete published proof of (a) among them. Confidence: high. Gaps: Shafarevich's Theorem 9 itself was not consulted; it is a reference in another book, not an exercise solution.

**Repair.** A complete published solution of IV.3.11(a), or the owner's direction to accept the card's derivation for that part.

### Chapter V: exercises whose Egbert entry is a citation, a stub or an unfinished computation

**Object and need.** Cards of V.4 and V.5 whose cited published solution does not contain a complete argument: V.4.3 ordinary singularities, V.4.4(b) the group law, V.4.7 the sharp genus maximum, V.4.8 (starred) irreducible classes, V.4.9 the minimal genus, V.4.10 the numerical inequality, V.4.11 the Weyl groups, V.4.12 Kodaira vanishing, V.4.13(b) the two quadrics, V.4.14 the space curves, V.4.15 general position and the $56/240$ count, V.4.16 the equations of the 27 lines and the automorphism group, V.5.1 separating the zeros of $f$ from its poles, V.5.4 contracted curves and negative definiteness, V.5.5 elementary transformations of ruled surfaces, V.5.6 valuation rings, V.5.7 curves contracted to a point, V.6.1 the exceptional complete intersections, V.6.2 the Chern--Griffiths bound, V.5.8(c) the eight-blow-up resolution.

**Observed evidence.** A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013):
- V.4.3, printed **p. 286**, is the whole entry "See Algebraic Curves over Finite Fields by Hirschfeld, Theorem 3.27" — a citation in another book, not an exercise solution.
- V.4.4, printed **pp. 286–287**: part (a) is argued through Cayley–Bacharach, but the entry `5.4.5 b.` for the group law is "See Tate, Silverman: Rational Points. It's in the first chapter" — again a citation.
- V.4.7, printed **pp. 288–290**: the upper bound is argued by a coordinate computation (the change of variables to $(a,b_1,\ldots,b_6)$, the function $F_d(r)$, its maximisation by calculus at $r=\frac23d$), but the sharpness half is unusable as printed: the existence paragraph reads "Choose $a\le d$ such that $a>d+2$. (since $d\ge8$, this is easy)" and "Let $b_6^2=3$", and the two quoted five-squares claims are proved only with the placeholders "We need ? integers $\alpha_i$" and "we need ?? integers $x_i$".
- V.4.8, printed **p. 290**: the entry consists of the two bullets "Existence" and nothing further, so the starred exercise has no written argument there.
- V.4.9, printed **p. 290**: the entry is an abandoned manipulation of the genus formula, printed with its working notes ("move $2.5\sum b_i$ here", "schwarz won't help", "let's evict $\frac12$", "hmm move 2.5 bi here"), which never states the bound $g\ge\frac12(d-6)$, $\frac12(d-5)$ nor derives it; the following "Existence" paragraph is a separate sum-of-five-squares construction that does not meet the exercise's classes.
- V.4.10, printed **p. 291**: the whole entry is "No algebraic geometry here. If your interested, see Nagata Rational Surfaces I, and proceed by cases" — a citation and no argument.
- V.4.11, printed **pp. 291–292**: parts (a) and (b) have no entry at all, the page carries "I don't care about group theory", and the starred part (c) is the entry `5.4.12 b.` reading "see above".
- V.4.12, printed **pp. 292–293**: the entry computes on $\PP^2$ ("Recall $X\approx\PP^2$ which has known cohomology", $H^2(X,\OO_X)=H^0(X,\OO_X(-3))=p_g$) although the cubic surface is $\PP^2$ with six points blown up, so the dimensions it lists are those of $\PP^2$ and the sequence is the wrong one; the closing step then invokes V.4.11 to exclude an effective $-D$, which is not what (4.11) says.
- V.4.13, printed **pp. 292–293**: part (a) is complete (the 16 classes and the Schwarz count $4a^2-6a-4\le0$). Part (b) stops at "Now use ?." after the dimension count $15-13=2$; the degree comparison that identifies $X$ with the complete intersection is missing.
- V.4.14, printed **p. 294**: the entry lists which degree–genus pairs remain after V.4.7, then says "For these remaining rest, I use the method of exc V.4.9 (Read that exercise solution first or this will be nonsense!)", works one case ($d=8$, $g=6$) and ends "Solve for this using sum of 5 squares as in exc V.4.9 and the rest follow similarly". No class is exhibited for the other eight pairs, and the cited method is the V.4.9 entry above.
- V.4.15, printed **pp. 294–295**: parts (a) and (b) have no entry; part (c) is argued (`5.4.18 c.`); part (d) is the sketch `5.4.19 d.` counting $14+42=56$ and listing eight families for $r=8$ without proving that no other negative curves exist; the starred part (e) is `5.4.17 b.`, "This is Nagata, Rational Surfaces II, corollary to proposition 9, and use (a) of this problem" — a citation.
- V.4.16, printed **p. 296**: the entry records a parametrization and the blowup description of the 27 lines but no equations of the lines in the Fermat coordinates (the exercise asks for the equations and the incidence relations), and its answer to the automorphism question is "Automorphism group? $E_6$. A proof is in Hirschfeld Finite projective spaces in three dimensions 20.3.1" — the group of the 27-line configuration, not the surface's automorphism group, and a citation.
- V.5.1, printed **p. 297**: the entry applies (3.9) and then asserts the decisive step: "Now how will further blowing-up make the resulting curves disjoint? Ok, further blowing up will make the curves disjoint because you have simple normal crossings to start. Now the blowing-up surface separates tangent directions at the node." Nothing shows that the blowups terminate, which is the only content beyond the printed hint.
- V.5.4, printed **p. 298**: for part (a) the entry proves only $Y^2\le0$, and does so by asserting that "pullback of ample is ample" together with $(f^*H)^2=0$; the pullback of an ample divisor under a birational morphism is nef and big but not ample (it meets every contracted curve in zero), and $(f^*H)^2=H^2>0$ because $f$ is birational, so the displayed vanishing is false. It says nothing about $Y\cong\PP^1$. For part (b) the printed text is a garbled string ("Then for each $j$, $\sum_i\langle m_iE_i, m_jE_j\rangle=-\langle H_1,m_jE_j\rangle\le0$ ... By Zariski's Main theorem, we can't split the $Y_i$'s into two groups ... Since we have already proved indefiniteness, these two facts give negative definite") that does not establish negative definiteness.
- V.5.5, printed **p. 299**: the whole entry is "Consequence of my proof of exc V.2.5.a" — a cross-reference to the author's own work, with none of the three steps of the printed hint carried out.
- V.5.6, printed **p. 299**: the trichotomy is stated and types (1) and (2) are identified through the centre and its successive blowups, but the decisive assertion of case (3) — that every $f\in R$ lies in some $\OO_{X_i,x_i}$, so that the union $R_0$ is all of $R$ — is not proved; the entry says "in the later case we repeat and get a type (3) of exc II.4.12" and cites another book ("see Vaqiue Valuations and local uniformization, remark 1.14") for the value-group claim.
- V.5.7, printed **p. 300**: the whole entry is "The answer from 5.4 applies since at beginning of surfaces chapter, we assume that X is nonsingular (maybe X0 isn't)" — a cross-reference to the V.5.4 entry above, with the printed hint not carried out.
- V.6.1, printed **p. 303**: the entry samples cases only ("If $n=3$, then ... we could pick $d_1=2$ or $d_1=3$ to have $K$ be negative multiple of ample so by 6.1, $|12K|=\emptyset$ ... We could pick $n=4$ to have $K_X\equiv0$ (so by 6.3, $X$ is K3)" ... "If $n=6$ ... it will always be general type"), with no complete list: the K3 case $(3;4)$ and the del Pezzo case $(4;2,2)$ are missing, and nothing shows that the sampled cases are exhaustive.
- V.6.2, printed **p. 303**: the entry is a garbled sketch. It opens "Let $X$ span $\PP^{n+1}$ of degree $d\le2n$ since it's not in a hyperplane", although degree and codimension are unrelated; it then assumes "F is not ruled", invokes "thms V.6.2, 6.3" for an effective multiple of $K_X$, uses "$H-K$ is ample by Nakai Moishezon" before $K$ is known, and ends "we get that $p_a(X)=1$ so by thm V.6.3, $X$ is K3. On the other hand, $X$ is ruled." — a non sequitur after the K3 conclusion.
- V.5.8, printed **p. 300**: entries for parts (a) and (b) only. The printed part about resolving the singularity by eight successive blowings-up with the stated dual graph has no entry.

**Impact and owner.** Our cards carry their own complete proofs of all of these (V.4.3 by repeated quadratic transformation creating only ordinary singularities; V.4.4 by Cayley–Bacharach with the reduced, multiplicity and specialization cases separated; V.4.8 by the blow-up model; V.4.7 by the Hodge index, the adjunction parity and the three equality families $mH$, $mH+L$, $mH+Q$; V.4.9 by contraction to $X_2$ plus an effectivity/nef argument in the $X_r$ case; V.4.10 by an elementary lemma on six positive reals; V.4.11 by the coset count for $\mathbf A_n$, the 72 sixes and the 72 roots; V.4.12 by the divisor sequence with a smooth member of $|D|$; V.4.13(b) by the degree comparison; V.4.14 by nine explicit classes; V.4.15 by the degree-decreasing classification of negative curves; V.4.16 by the three line families and the Hessian/unitary computation; V.5.1 by the Euclidean-algorithm measure on zero--pole crossings; V.5.4 by factorization into point blowups and the Hodge-index complement of $f^*H$; V.5.5 by the length-one elementary modifications of the defining rank-two bundle; V.5.6 by resolving $[f:1]$ and comparing centres; V.5.7 by the same positive-square pullback under a dominant $f$; V.6.1 by the adjunction computation $K_X=(\sum d_i-n-1)H$ and the six exceptional tuples; V.6.2 by a general hyperplane section with Clifford's theorem; V.5.8(c) by the eight blowings-up). Those derivations are not published solutions, so the published-solution obligation stays open under #116 for these cards, and no card's proof is being represented as a transcription of Egbert.

**Uncertainty.** Searched: every retained set in `tmp/sources` — Borcherds (Chapter 1), Cais (Chapters 2–4), Cutrone–Marshburn (Chapters 1–4), Dongryul Kim (Chapters II–III), Lomont (Chapters 1–3, plus a bare `Chapter V Solutions / 5.1` heading with no text), Park (Chapters I and IV, and V.5.8 only), Saglam–Chris (Chapter II), Sam (Chapter 1), Stein (a homework selection), Troiani (Chapter I), Okamoto (II.9) — none of which contains a §V.4 exercise, and Egbert's pages quoted above. Found: the citations, the stubs and the unfinished computations. The two §V.5 entries not listed above are complete and were read against the cards: V.5.2 (printed p. 297) really constructs $\mathcal M=\OO_X(mH+kY)$ with $m=-Y^2$, $k=H\cdot Y$, proves $H^1(\OO_X(mH+iY))=0$ for $0\le i\le k$ and makes $\mathcal M$ globally generated, and V.5.3 (printed p. 298) really computes $\Omega_{\widetilde X/X}\cong\Omega_E$ and the cohomology sequence, only with a labelling slip in its last paragraph. Conclusion: no complete published solution of the exercises listed above among the retained sets. Confidence: high for these sets; the Egbert entries were read in the `pdftotext -layout` extraction of the retained PDF, whose TOC fixes the printed pages. Gaps: Hirschfeld Theorem 3.27, Silverman–Tate, Nagata *Rational Surfaces I*/*II* and Hirschfeld §20.3.1 were not consulted; they are references in other books, not exercise solutions.

**Repair.** A complete published solution of each, or the owner's direction to accept the card's derivation.
