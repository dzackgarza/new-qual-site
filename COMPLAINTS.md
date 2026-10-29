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

### Duplicate finite-Galois card FD-4GFTY

- **Object and need:** `D-5JYEI` and `FD-4GFTY` in `corpus/theory/Algebra`. The canonical Galois card defines finite Galois extensions by normality and separability and proves the automorphism-count condition as an equivalent characterization; the flashcard restates that characterization as a second definition.

- **Observed evidence:** `D-5JYEI` item (5) states `$\size\Aut_F(K)=[K:F]_s=[K:F]$`; `FD-4GFTY` defines Galois by `$\abs{\Aut(K/F)}=[K:F]$`. The wiki and algebra guide displayed both.

- **Impact and owner:** the flashcard duplicates an equivalent condition already owned by the canonical card and creates a second defining surface.

- **Uncertainty:** none after reading both cards.

- **Repair:** a `CARD-04` repair moves the automorphism-count review prompt to `D-5JYEI`, removes duplicate reader-facing references, and deletes `FD-4GFTY`.

### Duplicate maximal-ideal cards D-7XH2R and FD-CD2FE

- **Object and need:** `D-7XH2R` and `FD-CD2FE` in `corpus/theory/Algebra`. Both define a proper ideal to be maximal when no proper strictly larger ideal exists.

- **Observed evidence:** the complete definitions are mathematically identical.
  `D-7XH2R` is the dependency used throughout the ideal and local ring theory; `FD-CD2FE` is a migrated flashcard and the wiki displayed it beside the canonical card.

- **Impact and owner:** the duplicate flashcard adds no mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-7XH2R`, removes the duplicate wiki link, and deletes `FD-CD2FE`.

### Duplicate prime-ideal cards D-5BM46 and FD-OSSYR

- **Object and need:** `D-5BM46` and `FD-OSSYR` in `corpus/theory/Algebra`. Both define a proper ideal `$\mathfrak p$` of a commutative ring to be prime when `$ab\in\mathfrak p$` implies `$a\in\mathfrak p$` or `$b\in\mathfrak p$`.

- **Observed evidence:** the definitions are identical.
  `D-5BM46` is the dependency used by the prime spectrum, quotient criterion, and height theorems; the wiki displayed `FD-OSSYR` immediately beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-5BM46`, removes the duplicate wiki link, and deletes `FD-OSSYR`.

### Sign homomorphism used incompatible codomains under one symbol

- **Object and need:** `D-BZ3KD`, `D-TMME3`, and the permutation/determinant cards using `\sgn`. The canonical sign map must have one type.

- **Observed evidence:** `D-BZ3KD` defined `$\sgn:S_n\to\ZZ/2$` by transposition parity, and `D-TMME3` therefore used `$\sgn(\sigma)=0$` for even permutations.
  `FD-GHDF2`, `FD-X4DBP`, and the determinant formulas use the conventional multiplicative sign `$\sgn:S_n\to\{\pm1\}$`.

- **Impact and owner:** the same notation had two incompatible codomains, so links to the canonical sign definition did not type-check against formulas using it multiplicatively.

- **Uncertainty:** none.
  The parity map and multiplicative sign are equivalent via `$k\bmod2\mapsto(-1)^k$`, but they are not the same typed map.

- **Repair:** a repair makes `D-BZ3KD` own the conventional multiplicative sign, updates `D-TMME3` to use sign `1` for even permutations, and links `FD-GHDF2` to the canonical definition.

### Duplicate alternating-group card FD-X4DBP

- **Object and need:** `D-TMME3` and `FD-X4DBP` in `corpus/theory/Algebra`. `D-TMME3` already defines even/odd permutations and the alternating group as the kernel of the sign homomorphism; `FD-X4DBP` repeats only the latter definition.

- **Observed evidence:** both complete cards state `$A_n=\ker(\sgn)=\{\sigma\in S_n:\sgn(\sigma)=1\}$`. The wiki and algebra guide displayed both cards adjacent to one another.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the kernel review prompt to `D-TMME3`, removes duplicate reader-facing references, and deletes `FD-X4DBP`.

### Duplicate even/odd-permutation card FD-PIVQZ

- **Object and need:** `D-TMME3` and `FD-PIVQZ` in `corpus/theory/Algebra`. `D-TMME3` already owns the definition of even permutations and the alternating group; `FD-PIVQZ` repeats evenness and adds oddness plus the parity characterization.

- **Observed evidence:** after the sign convention repair, both use the same multiplicative sign `$S_n\to\{\pm1\}$`. The wiki and algebra guide exposed both recall units, and `FD-X4DBP` linked to the flashcard for “even.”

- **Impact and owner:** the duplicated evenness definition splits a basic permutation concept; the odd terminology and parity statement can be preserved on the canonical alternating-group card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the prompt, odd definition, and parity remark to `D-TMME3`, redirects `FD-X4DBP`, removes duplicate reader-facing references, and deletes `FD-PIVQZ`.

### Duplicate Euclidean-domain cards D-NKRGN and FD-GXXBV

- **Object and need:** `D-NKRGN` and `FD-GXXBV` in `corpus/theory/Algebra`. Both define a Euclidean domain by a Euclidean function and the division-with-remainder inequality.

- **Observed evidence:** the only difference is that `D-NKRGN` defines the function on all of `$R$`, while `FD-GXXBV` defines it on `$R\setminus\{0\}$`; the Euclidean condition never requires a value at zero.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** the flashcard adds no mathematical distinction and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-NKRGN`, removes duplicate reader-facing references, and deletes `FD-GXXBV`.

### Duplicate lying-over/going-up cards FF-IBDAT and PR-RJ3P7

- **Object and need:** `FF-IBDAT` and `PR-RJ3P7`. Both state lying over for integral extensions and the going-up theorem for chains of prime ideals.

- **Observed evidence:** the Algebra card is exactly the two algebraic clauses already contained in the first theorem block of `PR-RJ3P7`; the latter also proves closedness and states going down.
  The Algebra wiki and guide pointed to `FF-IBDAT`, while the algebraic-geometry wiki pointed to `PR-RJ3P7`.

- **Impact and owner:** one standard theorem had two intrinsic addresses split by subject area, with no mathematical or source-appearance distinction.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the plain “What is going up?”
  prompt to `PR-RJ3P7`, redirects the Algebra wiki and guide, and deletes `FF-IBDAT`.

### Krull's maximal-ideal theorem had three intrinsic cards

- **Object and need:** `PR-UTFSY`, `T-QSTRJ`, and `FF-QELG7` in `corpus/theory/Algebra`. All three state that every proper ideal is contained in a maximal ideal.

- **Observed evidence:** `PR-UTFSY` gives the full Zorn proof for arbitrary unital rings; `T-QSTRJ` states the same theorem without proof; `FF-QELG7` repeats it for commutative rings with the same Zorn proof and contributes the review prompt.
  The wiki and algebra guide displayed all three together.

- **Impact and owner:** one standard theorem had three canonical-looking addresses, and a downstream Jacobson-radical proof linked to the flashcard duplicate.

- **Uncertainty:** none after reading all three complete cards.

- **Repair:** a `CARD-04` repair keeps `PR-UTFSY`, gives it the Krull title and review prompt, redirects all live references, and deletes `T-QSTRJ` and `FF-QELG7`.

### Duplicate Eisenstein theorem cards FT-2P5VV and T-CF6S3

- **Object and need:** `FT-2P5VV` and `T-CF6S3` in `corpus/theory/Algebra`. Both state Eisenstein's criterion for `$f\in\ZZ[x]$` and prove it by Gauss's lemma and reduction modulo `$p$`.

- **Observed evidence:** the hypotheses and proof are the same.
  `T-CF6S3` additionally records the primitive-polynomial consequence giving irreducibility in `$\ZZ[x]$`; `FT-2P5VV` contributes only the review prompt.
  The Galois-theory wiki and algebra guide displayed both.

- **Impact and owner:** one standard irreducibility criterion had two theorem addresses, while the richer card strictly contains the other.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `T-CF6S3`, redirects the remaining theorem link, removes duplicate reader-facing references, and deletes `FT-2P5VV`.

### Gauss's lemma was split across two theorem cards

- **Object and need:** `FT-OXN3Y` and `T-JEZZY` in `corpus/theory/Algebra`. Both are standard forms of Gauss's lemma rather than genuinely separate theorems.

- **Observed evidence:** `FT-OXN3Y` states that a factorization in the fraction field descends to `$R[x]$` with the same factor degrees; `T-JEZZY` gives the primitive-polynomial irreducibility equivalence and the sharper scalar rescaling statement.
  The wiki and algebra guide displayed both together.

- **Impact and owner:** one theorem was split between two addresses, and a Hartshorne collection card linked specifically to the weaker half.

- **Uncertainty:** none after reading both cards; the two forms are standard parts of the same Gauss lemma.

- **Repair:** a `CARD-04` repair merges both forms and the polynomial-UFD consequence onto `T-JEZZY`, moves the review prompt there, redirects all live references, and deletes `FT-OXN3Y`.

### Duplicate stabilizer card FD-IGEOR

- **Object and need:** `D-WYC7C` and `FD-IGEOR` in `corpus/theory/Algebra`. `D-WYC7C` already defines the stabilizer `$G_x$`; `FD-IGEOR` repeats that definition and adds only prompts plus the proof that `$G_x$` is a subgroup.

- **Observed evidence:** both complete cards use `$G_x=\{g\in G\mid g\cdot x=x\}$`. The canonical action card is the dependency used throughout orbit–stabilizer theory, while the wiki and algebra guide displayed the flashcard as an additional recall unit.

- **Impact and owner:** the duplicated definition splits a basic group-action concept, while the subgroup fact belongs naturally on the canonical card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the two prompts and subgroup proposition/proof to `D-WYC7C`, removes duplicate reader-facing references, and deletes `FD-IGEOR`.

### Duplicate subset-centralizer card FD-SSR6N

- **Object and need:** `D-PX64W` and `FD-SSR6N` in `corpus/theory/Algebra`. `D-PX64W` already defines the centralizer of an arbitrary subset; `FD-SSR6N` repeats the same condition with notation `$Z_G(S)$`.

- **Observed evidence:** both cards define the subgroup of `$g\in G$` that satisfy `$gsg^{-1}=s$` for every `$s\in S$`. The wiki displayed the flashcard beside the canonical centralizer card.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence for subset centralizers.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-PX64W`, removes the duplicate wiki link, and deletes `FD-SSR6N`.

### Duplicate transitive-action cards D-KGGWK and FD-KSKDG

- **Object and need:** `D-KGGWK` and `FD-KSKDG` in `corpus/theory/Algebra`. Both define transitivity of a group action by the condition that for every `$x,y\in X$` some `$g\in G$` satisfies `$g\cdot x=y$`.

- **Observed evidence:** the definitions are identical.
  `D-KGGWK` is the dependency used by transitive subgroups, covering-space theory, and the canonical group-action card; the wiki displayed `FD-KSKDG` beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-KGGWK`, removes the duplicate wiki link, and deletes `FD-KSKDG`.

### Duplicate generated-subfield card FD-QPNDA

- **Object and need:** `FD-J3HIA` and `FD-QPNDA` in `corpus/theory/Algebra`. Both define `$K(\alpha)$` as the smallest subfield of an ambient extension containing `$K$` and `$\alpha$`.

- **Observed evidence:** the definition bodies are identical.
  `FD-QPNDA` declared itself `variant-of: FD-J3HIA` and also repeated the already-false `variant-of: FD-3V3ZW` edge to the generated subring `$K[\alpha]$`. The wiki and algebra guide exposed both generated-subfield cards.

- **Impact and owner:** the duplicate adds no mathematics and reintroduces the subfield/subring conflation repaired on `FD-J3HIA`.

- **Uncertainty:** none after reading both complete generated-subfield cards.

- **Repair:** a `CARD-04` repair moves the additional review prompt to `FD-J3HIA`, removes duplicate reader-facing references, and deletes `FD-QPNDA`.

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

## Workflow and rendering papercuts

### Shared QC installation lacks its PR workflow and branch protection

- **Object and need:** the shared QC installation declared in `justfile`.

- **Observed evidence:** `ai-review-ci doctor --target . --json` on 2026-10-25 accepted the local recipe delegation but reported missing `.github/workflows/review-pr.yml` and an unprotected `main` branch.

- **Impact and owner:** Pages CI runs the project suite and build; the shared required PR acceptance contexts are not installed.
  The installation belongs to ai-review-ci.

- **Uncertainty:** this is the doctor's current installation result, not a failure of the Pages tests or build.

- **Repair:** reconcile the shared PR installation with `QUAL-09`'s direct-to-main workflow before changing branch protection.

