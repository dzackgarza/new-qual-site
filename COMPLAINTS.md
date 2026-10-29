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

### Second duplicate Burnside card FF-OL75S

- **Object and need:** `C-HE5SL` and `FF-OL75S` in `corpus/theory/Algebra`. Both state Burnside's orbit-counting formula for a finite group acting on a finite set.

- **Observed evidence:** the displayed formulas are identical after the notational substitution `$X^g=\Fix(g)$`; `FF-OL75S` adds only the review prompt and the standard double-counting proof.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** a second flashcard-derived address remained for the same theorem after the earlier `C-CM7ZS` duplicate was removed.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt and double-counting proof to `C-HE5SL`, removes duplicate reader-facing references, and deletes `FF-OL75S`.

### Duplicate class-equation cards C-A6UAR, C-O7CP3, and FD-L2TEC

- **Object and need:** `C-A6UAR`, `C-O7CP3`, and `FD-L2TEC` in `corpus/theory/Algebra`. They are intrinsic cards for the same class equation (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** after reading all three complete cards, they have the same title, hypotheses, centralizer notation, choice of noncentral conjugacy-class representatives, and class-equation formula.
  Their only substantive source difference is presentation syntax (`\#` versus the repository's `\size` macro).
  `FD-L2TEC` later restated the same theorem and added its standard conjugation-action proof.
  The wiki and algebra guide exposed the duplicate theorem beside `C-O7CP3`.

- **Impact and owner:** retaining the duplicates gives multiple canonical-looking addresses for one theorem and splits guide references.
  `C-O7CP3` is already the wiki-facing statement and uses the current notation convention.

- **Uncertainty:** none after reading all three complete cards; no distinct source appearance or mathematical variant was found.

- **Repair:** a `CARD-04` repair redirects the algebra guide to `C-O7CP3`, moves the review prompt and proof from `FD-L2TEC` onto `C-O7CP3`, removes duplicate reader-facing references, and deletes `C-A6UAR` and `FD-L2TEC`.

### Duplicate coset-counting cards C-HWX2P and C-XRC67

- **Object and need:** `C-HWX2P` and `C-XRC67` in `corpus/theory/Algebra`. They state the same coset-counting formula and therefore violate the single-owner expectation for standard statements (`CARD-04`, `SOURCE-02`).

- **Observed evidence:** both complete cards have the same title, hypotheses, definition of the index, and equations `$\size G=[G:H]\,\size H$` and `$[G:H]=\size G/\size H$`, differing only by `\size` versus `\#` presentation syntax.
  `C-XRC67` also declares itself `variant-of: C-HWX2P`. The wiki and algebra guide both reference `C-HWX2P`; no reader-facing surface references `C-XRC67`.

- **Impact and owner:** retaining `C-XRC67` creates a second intrinsic address for the same theorem without a source or mathematical distinction.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair removes `C-XRC67` and retains `C-HWX2P` as the canonical statement.

### Zero-divisor definition was wrong for noncommutative rings and duplicated

- **Object and need:** `D-4I3SL` and `FD-S62UB` in `corpus/theory/Algebra`. `D-GURUB` defines rings without commutativity, but `D-4I3SL` defined a zero divisor by requiring one nonzero element to annihilate the given element on both the left and the right.
  `FD-S62UB` separately gave the standard commutative definition.

- **Observed evidence:** `D-4I3SL` quantified over an arbitrary ring and required `$ar=ra=0$`; `FD-S62UB` quantified over a commutative ring and required a nonzero `$x$` with `$rx=0$`. Current uses of the zero-divisor card in the domain, primary-ideal, and Noetherian-ring material are in the commutative setting.
  The wiki and algebra guide exposed both definitions side by side.

- **Impact and owner:** the canonical card misstated the noncommutative notion and duplicated a second card for the commutative notion.
  In a noncommutative ring, left and right zero divisors need not coincide; the simultaneous two-sided condition is not the standard generic definition.

- **Uncertainty:** none about the defect.
  The corpus currently needs the commutative notion; noncommutative left/right variants can be introduced separately if needed later.

- **Repair:** a `CARD-04` repair restricts `D-4I3SL` to commutative rings, uses the standard annihilator definition, preserves the review prompt there, removes duplicate reader-facing references to `FD-S62UB`, and deletes the duplicate card.

### D-5JYEI delegated the separable-degree statement to an opaque screenshot

- **Object and need:** `D-5JYEI`, Galois extension and Galois group.
  The closing remark states that separable degree counts embeddings but then shows only a legacy image with filename alt text instead of the formula.

- **Observed evidence:** the card ended with `![figures/2021-08-09_22-29-40.png](../../assets/figures/...)`; no surrounding prose stated the embedding set or explained how the Galois automorphism count follows.

- **Impact and owner:** the card's last mathematical claim was inaccessible to text readers and dependent on an unexplained asset.
  The relevant formula is intrinsic to the theorem and should be authored as mathematics on the card.

- **Uncertainty:** none; for a finite extension, the separable degree is the number of `$k$`-embeddings into a fixed algebraic closure.

- **Repair:** a repair replaces the screenshot with the formula `$[L:k]_s=\size\Hom_{k\text{-alg}}(L,\bar k)$` and explains why normality identifies these embeddings with `\Gal(L/k)` in the Galois case.

### Duplicate UFD cards D-INULL and FD-25SUQ

- **Object and need:** `D-INULL` and `FD-25SUQ` in `corpus/theory/Algebra`. Both cards gave the full definition of a unique factorization domain, including existence and uniqueness up to order and associates.

- **Observed evidence:** the complete statements are mathematically identical; `D-INULL` is the dependency used by the UFD theorems and polynomial-ring material, while `FD-25SUQ` came from the flashcard migration.
  The wiki and algebra guide displayed both adjacent to one another.

- **Impact and owner:** the duplicate flashcard creates a second defining occurrence and splits review/navigation without adding mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the flashcard review prompt to `D-INULL`, removes duplicate reader-facing references, and deletes `FD-25SUQ`.

### Duplicate indecomposable-module cards D-4HEUB and FD-2EUYX

- **Object and need:** `D-4HEUB` and `FD-2EUYX` in `corpus/theory/Algebra`. `D-4HEUB` already defines decomposable and indecomposable modules; `FD-2EUYX` repeats the indecomposable definition.

- **Observed evidence:** both complete statements say that a nonzero module is indecomposable exactly when it cannot be written as a direct sum of two nonzero submodules.
  The wiki and algebra guide displayed both adjacent to one another.

- **Impact and owner:** the flashcard duplicate adds no mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-4HEUB`, removes duplicate reader-facing references, and deletes `FD-2EUYX`.

### Duplicate cyclic-module cards D-HY7UU and FD-S2W5E

- **Object and need:** `D-HY7UU` and `FD-S2W5E` in `corpus/theory/Algebra`. Both define a cyclic module as a module generated by one element.

- **Observed evidence:** the definition blocks are identical.
  `FD-S2W5E` additionally proves the standard characterization `$M\cong R/I$` for a left ideal `$I$`. The wiki and algebra guide displayed both cards.

- **Impact and owner:** the duplicate definition splits the recall unit, while the quotient characterization is useful and should be retained on the canonical card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the prompt and quotient characterization/proof to `D-HY7UU`, removes duplicate reader-facing references, and deletes `FD-S2W5E`.

### Duplicate torsion-free-module card FD-U6KUJ

- **Object and need:** `D-ZJJ7G` and `FD-U6KUJ` in `corpus/theory/Algebra`. `D-ZJJ7G` already defines torsion-free modules; `FD-U6KUJ` restates the integral-domain special case as vanishing of the torsion submodule.

- **Observed evidence:** over an integral domain the torsion set on `D-ZJJ7G` is exactly the torsion submodule of `FD-BPUNZ`, so `$M_t=\{0\}$` and `$\tor(M)=0$` are the same condition.
  The wiki and algebra guide exposed both definitions.

- **Impact and owner:** the flashcard adds no distinct mathematics and splits the definition of torsion-free modules.

- **Uncertainty:** none after reading the canonical torsion card, the domain-specific torsion-submodule card, and `FD-U6KUJ`.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-ZJJ7G`, removes duplicate reader-facing references, and deletes `FD-U6KUJ`.

### Duplicate composition-series cards D-FYX4I and FD-PLAEO

- **Object and need:** `D-FYX4I` and `FD-PLAEO` in `corpus/theory/Algebra`. They define the same finite normal series, with `D-FYX4I` descending by maximal proper normal subgroups and `FD-PLAEO` ascending with simple successive quotients.

- **Observed evidence:** those conditions are equivalent, since `$N_i\normal N_{i+1}$` is maximal proper exactly when `$N_{i+1}/N_i$` is simple.
  `FD-PLAEO` additionally names the successive simple quotients as composition factors.
  The wiki and algebra guide exposed both cards, and `FD-T7IQV` linked to the flashcard duplicate.

- **Impact and owner:** two cards owned one definition, while the composition factor terminology belongs naturally on the canonical series card.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the prompt and composition-factor terminology to `D-FYX4I`, redirects `FD-T7IQV`, removes duplicate reader-facing references, and deletes `FD-PLAEO`.

### FD-T7IQV restated solvability as a definition instead of a finite-group criterion

- **Object and need:** `D-DFIDP` and `FD-T7IQV` in `corpus/theory/Algebra`. `D-DFIDP` canonically defines solvable groups by a finite normal series with abelian quotients; `FD-T7IQV` independently defined finite-group solvability via abelian composition factors.

- **Observed evidence:** the latter condition is an equivalent theorem for finite groups, not a second definition owner.
  No other card states this composition-factor criterion.

- **Impact and owner:** keeping the card as a definition duplicated the term, while deleting it would lose a useful finite-group characterization.

- **Uncertainty:** none; the equivalence follows because subgroups and quotients of solvable groups are solvable and a simple solvable group is abelian.

- **Repair:** a repair converts `FD-T7IQV` to the proposition “Solvability via composition factors,” links it to the canonical solvability and composition-series cards, and adds the proof of the equivalence.

### Duplicate finite-Galois card FD-4GFTY

- **Object and need:** `D-5JYEI` and `FD-4GFTY` in `corpus/theory/Algebra`. The canonical Galois card defines finite Galois extensions by normality and separability and proves the automorphism-count condition as an equivalent characterization; the flashcard restates that characterization as a second definition.

- **Observed evidence:** `D-5JYEI` item (5) states `$\size\Aut_F(K)=[K:F]_s=[K:F]$`; `FD-4GFTY` defines Galois by `$\abs{\Aut(K/F)}=[K:F]$`. The wiki and algebra guide displayed both.

- **Impact and owner:** the flashcard duplicates an equivalent condition already owned by the canonical card and creates a second defining surface.

- **Uncertainty:** none after reading both cards.

- **Repair:** a `CARD-04` repair moves the automorphism-count review prompt to `D-5JYEI`, removes duplicate reader-facing references, and deletes `FD-4GFTY`.

### Duplicate finite-Galois characterization theorem FT-3WWKN

- **Object and need:** `D-5JYEI` and `FT-3WWKN` in `corpus/theory/Algebra`. Both list equivalent characterizations of a finite Galois extension.

- **Observed evidence:** `FT-3WWKN` lists separable splitting field, fixed field, full automorphism count, and normal-plus-separable.
  `D-5JYEI` already contains all four and additionally the irreducible separable splitting-field characterization and the separable-degree equality.

- **Impact and owner:** the flashcard theorem duplicates a strictly richer canonical card; one downstream example still linked to the duplicate.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair adds a characterization review prompt to `D-5JYEI`, redirects the downstream link, removes duplicate reader-facing references, and deletes `FT-3WWKN`.

### Duplicate fundamental-theorem-of-Galois-theory cards

- **Object and need:** `FT-GJ6NR` and `T-NLPZY` in `corpus/theory/Algebra`. Both state the subgroup/intermediate-field anti-isomorphism and its standard consequences.

- **Observed evidence:** the field/subgroup bijection, inclusion reversal, degree formulas, normal-subgroup criterion, and compositum/intersection formulas agree exactly.
  `T-NLPZY` additionally records the normalizer of an intermediate field and distinguishes `$\langle H_1,H_2\rangle$` from the product set `$H_1H_2$`; `FT-GJ6NR` contributes only the review prompt.

- **Impact and owner:** the same major theorem had two intrinsic addresses in the Galois wiki and algebra guide.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `T-NLPZY`, removes duplicate reader-facing references, and deletes `FT-GJ6NR`.

### Duplicate prime-element cards D-AWSKI and FD-S52W7

- **Object and need:** `D-AWSKI` and `FD-S52W7` in `corpus/theory/Algebra`. Both define a nonzero nonunit `$p$` to be prime when `$p\divides ab$` implies `$p\divides a$` or `$p\divides b$`.

- **Observed evidence:** the definition bodies are mathematically identical.
  `D-AWSKI` is the dependency used by the prime-versus-irreducible theorem and factorization wiki; the wiki displayed `FD-S52W7` beside it.

- **Impact and owner:** the flashcard adds no distinct mathematics and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-AWSKI`, removes the duplicate wiki link, and deletes `FD-S52W7`.

### FD-R4K7Z was a second irreducible-element duplicate with a false variant edge

- **Object and need:** `FD-R4K7Z` in `corpus/theory/Algebra`. The card defines irreducible elements of a commutative ring, which is already owned by `D-TO3IY`, but declared itself `variant-of: FD-GHY34`, a polynomial irreducibility card.

- **Observed evidence:** its body is the same ring-element condition as `D-TO3IY`: a nonzero nonunit `$p$` with every factorization `$p=ab$` having a unit factor.
  `FD-GHY34` instead quantifies over polynomials in `$K[x]$`.

- **Impact and owner:** the card both duplicated the canonical definition and asserted a variant relation between different levels of generality/objects.

- **Uncertainty:** none after reading all three cards.

- **Repair:** a `CARD-04` repair removes the duplicate wiki link and deletes `FD-R4K7Z`; `D-TO3IY` already carries the equivalent review prompt.

### Duplicate irreducible-polynomial cards D-BVMTZ, FD-GHY34, and FD-KPW3H

- **Object and need:** `D-BVMTZ`, `FD-GHY34`, and `FD-KPW3H` in `corpus/theory/Algebra`. All three define irreducibility of a polynomial over a field by absence of a factorization into two positive-degree factors.

- **Observed evidence:** the definitions are equivalent; `FD-GHY34` added the observation that degree-one polynomials are irreducible, while `FD-KPW3H` restates the same condition as “no factorization into two strictly lower-degree factors.”
  `D-BVMTZ` is the dependency used throughout Galois and factorization theory.
  The wiki exposed the flashcard definitions beside the canonical card.

- **Impact and owner:** the flashcard duplicates the defining occurrence while its small useful remark can live on the canonical card.

- **Uncertainty:** none after reading all three complete cards.

- **Repair:** `FD-KPW3H` is merged into `D-BVMTZ`. A `CARD-04` repair moves the prompt and linear-polynomial remark from `FD-GHY34` to `D-BVMTZ` and deletes `FD-GHY34`.

### Duplicate projective-module cards D-RHJMK and FD-6XJ7D

- **Object and need:** `D-RHJMK` and `FD-6XJ7D` in `corpus/theory/Algebra`. Both define projective modules by the lifting property and prove that projective modules are exactly direct summands of free modules.

- **Observed evidence:** `D-RHJMK` contains the same lifting diagram and direct-summand proof and additionally records splitting of short exact sequences and exactness of `\Hom_R(P,-)`. The wiki and algebra guide displayed both cards.

- **Impact and owner:** the flashcard duplicates a strictly richer canonical card without preserving distinct mathematics.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-RHJMK`, removes duplicate reader-facing references, and deletes `FD-6XJ7D`.

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

### Duplicate characteristic-polynomial cards had inconsistent coefficient scope

- **Object and need:** `D-QFYAC` and `FD-GOB47` in `corpus/theory/Algebra`. Both define `$\det(xI-A)$`, but the canonical card unnecessarily restricted to matrices over a field while the flashcard used the correct commutative-ring scope.

- **Observed evidence:** the determinant definition makes sense over any commutative ring.
  The only field-specific content on `D-QFYAC` is its later Smith-normal-form remark over `$k[x]$`. The wiki and algebra guide displayed both definitions.

- **Impact and owner:** retaining both split a standard definition and made the canonical card less general than the duplicate.

- **Uncertainty:** none; characteristic polynomials are defined over arbitrary commutative coefficient rings, while Smith normal form here requires the field hypothesis.

- **Repair:** a `CARD-04` repair broadens `D-QFYAC` to a commutative ring, scopes its SNF remark to the field case, moves the review prompt there, removes duplicate reader-facing references, and deletes `FD-GOB47`.

### Duplicate characteristic cards D-JNCUB and FD-LXZIW

- **Object and need:** `D-JNCUB` and `FD-LXZIW` in `corpus/theory/Algebra`. Both define the characteristic of a ring as the least positive `$n$` with `$n\cdot1_R=0$`, or `0` when no such integer exists.

- **Observed evidence:** the definitions are identical.
  `FD-LXZIW` adds the useful characterization as the nonnegative generator of the kernel of `$\ZZ\to R$`; `D-JNCUB` is the canonical dependency used by the field and separability theory.
  One problem card and a wiki page still linked to the flashcard duplicate.

- **Impact and owner:** the duplicate splits a basic ring invariant while the useful kernel characterization belongs naturally on the canonical card.

- **Uncertainty:** none after reading both complete cards; the older candidate `D-O26OY` is absent from the live tree.

- **Repair:** a `CARD-04` repair moves the review prompt and kernel characterization to `D-JNCUB`, redirects the problem-card reference, removes the duplicate wiki entry, and deletes `FD-LXZIW`.

### Duplicate Euclidean-domain cards D-NKRGN and FD-GXXBV

- **Object and need:** `D-NKRGN` and `FD-GXXBV` in `corpus/theory/Algebra`. Both define a Euclidean domain by a Euclidean function and the division-with-remainder inequality.

- **Observed evidence:** the only difference is that `D-NKRGN` defines the function on all of `$R$`, while `FD-GXXBV` defines it on `$R\setminus\{0\}$`; the Euclidean condition never requires a value at zero.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** the flashcard adds no mathematical distinction and creates a second defining occurrence.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the review prompt to `D-NKRGN`, removes duplicate reader-facing references, and deletes `FD-GXXBV`.

### Duplicate elementary-divisor card FD-H764S

- **Object and need:** `D-JQNJQ` and `FD-H764S` in `corpus/theory/Algebra`. `D-JQNJQ` defines the elementary-divisor decomposition for all finitely generated abelian groups; `FD-H764S` restates the finite special case and names the same prime-power factors.

- **Observed evidence:** `FD-H764S` explicitly invokes `D-JQNJQ` and then reproduces the decomposition with free rank zero.
  The wiki and algebra guide displayed both cards.

- **Impact and owner:** the finite flashcard adds no distinct mathematics and creates a second definition of elementary divisors.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** a `CARD-04` repair moves the finite-group review prompt to `D-JQNJQ`, removes duplicate reader-facing references, and deletes `FD-H764S`.

### Duplicate matrix-power counterexamples

- **Object and need:** `FE-ISVDM`, `FE-W56LS`, and later `FF-VKYM3` in `corpus/theory/Algebra`. They answer the same prompt about whether `$A^n=B^n$` forces `$A=B$`.

- **Observed evidence:** `FE-ISVDM` and `FE-W56LS` both use `$M=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$`, `$M^2=I$`, and `$M\ne I$`; `FE-W56LS` already declares itself `variant-of: FE-ISVDM`. `FF-VKYM3` gives the same claim with another square-root-of-`$-I$` example.
  All three examples only treated `$n=2$`, even though their body copy said “for `$n\ge2$`.”

- **Impact and owner:** one intrinsic counterexample question had multiple addresses, and the displayed witnesses did not justify the universal `$n\ge2$` wording.

- **Uncertainty:** none after reading both complete cards.

- **Repair:** `FE-W56LS` is merged into `FE-ISVDM`. A `CARD-04` repair replaces the `FE-ISVDM` witness by the rotation matrix through `$2\pi/n$`, which works for every `$n\ge2$`, redirects the remaining guide and wiki references, and deletes `FF-VKYM3`.

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

### UNL Math 872 assignment cards retain lost TeX escapes

- **Object and need:** cards for assignments 10.B.1–3, 10.C.1–4 and 11.B.1–2, 11.C.1 in `SRC-UNL-MATH872-SPRING-2014-PROBLEM-SETS` must preserve readable mathematical notation.

- **Observed evidence:** while repairing control bytes rejected by the push gate, reading these cards showed additional transport damage: `P-UNL872S14-10-B-3` has `operatorname{Homeo}`, `Fcirc q_G` and bare `[` display delimiters; `P-UNL872S14-10-C-4` has `ho:G` where the command prefix was lost.
  Restoring backspace, vertical-tab and form-feed bytes does not repair the missing escapes elsewhere.

- **Impact and owner:** the authored cards need a source-faithful notation repair; a successful corpus parse does not establish that their rendered formulas are correct.

- **Uncertainty:** the listed byte and text defects were inspected directly.
  The original sources have not been reread for a complete repair, and the remaining affected population has not been established beyond these ten cards.

- **Repair:** TODO.md section 7 / issue #2. Read each retained source, restore the intended notation without changing the mathematical claims, and inspect the rendered result at the normal publication boundary.

