# Algebra subject branch: build proof

Manifest: `publications/algebra-guide.yaml`. Built and inspected at `03da02f8`.

`uv run qualc build` -> 8,213 cards and 327 wiki pages OK, 5,822 HTML pages, 18 Algebra guide routes.

## What the branch covers

2,368 cards carry `algebra`. 2,318 of them now carry topics; before this work 292 did, and 43 of those 292 carried only `algebra` itself, which is the area name repeated as a topic and which no study-guide panel can ask for.
Classification is what makes the branch traversable at all: a panel selects on topic, so a card with no topic, or with only the area name, is reachable from no section.

The manifest was four sections, 12 references and one panel, covering finite groups, actions and Sylow theory.
It is now seventeen sections, 404 references and 179 panels.

The 50 cards left unclassified are all `source` cards, and they are named rather than rounded off: `SRC-ALG-*` and `SRC-UGA-ALG-*`. A source card records a sitting -- an exam paper, a homework set, a contributed artifact -- and states no mathematics of its own; its body is a provenance remark.
There is no topic a section could file "UGA algebra Fall 2019" under, and a reader reaches it through the exam route instead.
No Algebra card that states mathematics is unclassified.

## Routes

Eighteen routes, one root and seventeen sections:

```
/guide/GUIDE-ALGEBRA.html
/guide/GUIDE-ALGEBRA/preliminaries.html
/guide/GUIDE-ALGEBRA/groups-and-subgroups.html
/guide/GUIDE-ALGEBRA/group-actions-and-counting.html
/guide/GUIDE-ALGEBRA/sylow-theory.html
/guide/GUIDE-ALGEBRA/permutation-groups.html
/guide/GUIDE-ALGEBRA/series-and-solvability.html
/guide/GUIDE-ALGEBRA/products-and-classification.html
/guide/GUIDE-ALGEBRA/rings-and-ideals.html
/guide/GUIDE-ALGEBRA/factorization-and-polynomials.html
/guide/GUIDE-ALGEBRA/commutative-algebra.html
/guide/GUIDE-ALGEBRA/modules.html
/guide/GUIDE-ALGEBRA/structure-theorem.html
/guide/GUIDE-ALGEBRA/fields-and-extensions.html
/guide/GUIDE-ALGEBRA/galois-theory.html
/guide/GUIDE-ALGEBRA/linear-algebra.html
/guide/GUIDE-ALGEBRA/canonical-forms.html
/guide/GUIDE-ALGEBRA/semisimplicity-and-representations.html
```

## Reachability

Every Algebra card that states mathematics -- 1,822 of them -- is reached by the guide, either named as a section reference or matched by a section's panel.
This is measured against the manifest and the corpus, not asserted: a card counts as reached when its id appears as a `ref` or when some panel's `(kind, topic)` pair is one the card carries.

The 496 occurrence cards and 50 source cards are deliberately outside the guide.
An occurrence records that a problem appeared at a named sitting and a source records the sitting; both already appear on the problem's own card page, and a study-guide section reading from theory to problems has nothing to do with them.

Two topics carry no panel: `convolution` and `function-spaces`. Both are carried only by cards that also carry `algebras` or `rings`, so no card is lost -- `P-25QBA`, `P-XZRST` and `P-Y4XPA` are all reached.
See the misfiling finding below for what those cards are.

## What was inspected

All eighteen routes were rendered in headless Chromium at 1440 wide and measured from the post-MathJax DOM. Four were screenshotted and read directly: the root, Preliminaries, Sylow Theory in full, Commutative Algebra, and the foot of Canonical Forms.

**MathJax.** `<mjx-merror>` is zero on all eighteen routes.
That is not the vacuous zero of a page that never typeset: the section pages carry 69 to 898 `<mjx-container>` elements each, the largest being Fields and Extensions at 898 and Groups and Subgroups at 714. The root carries none, correct for a page that is a lede and a list of links.

**Root.** Study path listing all seventeen sections with every label rendering in full, the lede, the ordered list 1 to 17, and `NEXT Preliminaries`.

**Sylow Theory.** Breadcrumb carries the whole chain, `Algebra / Preliminaries / Groups and Subgroups / Group Actions and Counting / Sylow Theory`. Fifteen titled blocks, each with its card id beside the heading, beginning `D-7TQ2M` for the definition and running through `T-4RADG`, `T-RRK4J`, `T-3X5FF` for the three theorems.
The statements typeset: `|G| = p^a m` with `p ∤ m`, the conjugacy statement, and the two Sylow-3 congruences.
Four panels return the classified Sylow and p-group problems and exercises, each linked and carrying its id.
Foot navigation reads `PREVIOUS Group Actions and Counting` / `NEXT Permutation Groups`.

**Commutative Algebra.** Breadcrumb `Algebra / Preliminaries / Rings and Ideals / Factorization and Polynomials / Commutative Algebra`. Thirty-two blocks; the localization construction, the field of fractions, the local ring and the regular ring all typeset, including the equivalence relation with its `∃u ∈ S` clause.

**Canonical Forms.** The panels return the whole run of canonical-form problems and exercises with their displayed matrices typeset, and the last panel returns the solution card `S-WTH5Z`.

**Narrow width.** All eighteen routes swept at 375x812 with `artifacts/issue-23/narrow-width-overflow`, the publisher lane's script, reused unchanged against the same emitted site:

```
pages_loaded: 18
mathjax_did_not_settle: 0
pages_overflowing_375px: 0
```

Zero is the whole result: no route has a document wider than the viewport, so there is no widest-element attribution to report.
Sylow Theory was also read at 375 by eye -- the study path collapses to a card above the article with every label wrapping in full, the five-step breadcrumb wraps to two lines, and the lede reflows.

## What this does not claim

The guide is not proved to be the only correct decomposition of the subject; the seventeen sections and their order are a reading judgment, and the section ledes say where that judgment was exercised.

Nothing here proves the mathematics on the cards is correct.
It proves the cards are classified, reachable, and rendered.
The findings below are what reading 2,073 previously unclassified cards turned up, and they are not fixed here.

Search, the generator, the exam routes, and hint and solution disclosure states were not exercised.

Only two widths were measured, 1440 and 375; nothing between or beyond them.

The 50 source cards are unclassified by decision, not by omission, and the decision is stated above rather than deferred.

## Findings: mathematics that is missing or wrong

These were found by reading, not by any check, and none of them is fixed by the manifest work this proof covers.

They were corrected afterwards, in `eee0d46d`, `8a4bc822`, `d58db4d3`, `fb546a5c`, `2d160bd2`, `205b5975` and `f00a577a`, each against a source cited in its commit body.
Three classes are not corrected and stay routed to issue #2: the cards with no mathematics, the wrong-area oral-exam cards, and the duplicate pairs, which are decisions about what to keep rather than about what is true.
Three items are recorded as unsettleable rather than guessed, and are named where they appear below.

### Statements that are false as written

`T-EN5H4` says S_n is solvable for n ≥ 4; it is solvable exactly for n ≤ 4. `E-AMD-5X2XEHTC`, `P-VAK32` ask to show a nilpotent operator is diagonalisable; only the zero operator is.
`E-AMD-O2OGRSJP`, `P-WI5OS` ask to show Z(S_n) is nontrivial for n ≥ 4, contradicting `E-AMD-74T5EHRR` and `P-JPTMN` in the same corpus.
`E-AMD-VGBOZDXZ`, `P-VX22R` say every normal subgroup of a p-group lies in the center; the true statement is its neighbour `E-AMD-TM3LMADH`. `E-AMD-DLD6LYAM`, `P-35P7L` conclude G ≅ A_4 from a normal subgroup of order 4 in a group of order 12; Z/12 has one too.
`E-AMD-EBIC3Z5S` concludes R is a UFD from spec(R) ⊆ maxspec(R). `E-AMD-J3YZ5TXF`, `P-KSSA7`, `P-S5JSR` say the Galois group of x^n − 2 is D_n; the group embeds in Z/n ⋊ (Z/n)^× and is dihedral exactly when φ(n) = 2, that is for n = 3, 4, 6. `P-AMD-2PFLAITV` says no group of order under 60 is simple; the cyclic groups of prime order are.
`P-AMD-AFCXP5C6` asks to show Q/Z ≅ C^×. `P-AMD-D4G4SW2S` asks for gPg⁻¹ ∈ Syl_p(H) where gPg⁻¹ ∩ H is meant; `E-AMD-DGMOEV2O` asks for P ∩ H ∈ Syl_p(H) given P ∈ Syl_p(H), which is trivial.
`E-AMD-LDJWILVY`, `P-B644L` conclude HK ≤ H. `E-AMD-E3UUQEAP` gives the splitting field of x³ − 2 as Q(∛2, ζ_2), and ζ_2 = −1. `P-SXM4Q` asks to prove ⟨s⟩ is normal in G rather than in C_G(s). `P-O2H7G` hypothesises H ∈ N_G(H). `P-3PD4W` asks for the center of a group of order pr with p prime; order 6 is a counterexample and p^r is presumably meant.
`E-AMD-5E2GZSH6` says "Prove Burnside's theorem" without saying which.

### Definitions that state the wrong thing

`D-GY7ZN` defines SO_n as {A : AA^t = I}, which is O_n, and equates it with a kernel that is SL_n. `D-J5AAX`, `D-LIIHP` define GL_n(R) as {A : A = Ā}. `D-3V3SP`, `D-DQPGU` define the symplectic group with a symmetric J. `D-KGGWK` defines transitivity as g·x = x. `D-JGYK4` defines primary with "and" where "or" is meant.
`D-QMVEB` calls the normal core the largest normal subgroup containing H; its own formula gives the largest contained in H. `D-JRPTK` characterises matrix equivalence by rank, invariant factors and JCF; the JCF is a similarity invariant and does not belong, while the invariant factors are the complete invariant over a PID and rank alone suffices only over a field.
`D-TGB4R` writes mSpec R = {0, m}. `D-AWSKI` defines a prime element by ab | p rather than p | ab.
`D-7563L`, `D-NQZUY` state the module axiom as (r+s)x = rs + sx.
`D-GXMDW` states ring morphisms as f(a(b+c)) = f(a)f(b) + f(a)f(c). `D-JQNJQ` writes the elementary divisor decomposition with the exponents transposed.
`FD-CD2FE` defines maximal without properness or strictness.
`FD-6WSIA`, `FD-OUWGL` quantify separability over α ∈ K rather than α ∈ L. `FD-GHY34` requires deg p > 1 for irreducibility, excluding the linear polynomials.
`FD-GHDF2` is self-contradictory about which cycles are odd.
`FD-S62UB` quantifies over an undefined X and omits x ≠ 0. `FD-CVEAI` defines free rank as a maximal independent set, true over a domain only.
`FD-LHLDU` states ⟨p⟩-primary as atm = m.

### Theorems and propositions stated wrongly

`T-4XKGD` states Frattini with P ∈ Syl_p(G) where Syl_p(H) is needed; `L-6QBOJ` writes Syl_p(H) with H undefined and concludes G = N_G(P)H. `T-YHH3M` states Schur as M ≅ Aut_G(M, M); Schur gives End_G(M) ≅ k. `T-6ABNR`, `FT-BC6S2` offer "F contains all roots of the minimal polynomial" as equivalent to diagonalisability, dropping distinctness.
`T-QBQLM` writes GF(p^n) ≅ F_p/(f) for F_p[x]/(f). `T-NLPZY` defines Gal(L/F) as {σ : σ(F) = F} and pairs F_1 ∩ F_2 with H_1H_2 rather than ⟨H_1, H_2⟩. `FT-3WWKN` says the fixed field of Aut(K/F) is K. `FT-BAV4D` omits gcd(a, n) = 1 from Euler's theorem.
`FT-7NMQR`, `T-YNKCZ` write the trivial intersection as ∅, and `FT-7NMQR` has no conclusion clause.
`PR-GV5CF` states commuting as equivalent to simultaneous diagonalisability without assuming each is diagonalisable.
`PR-OF7ZW` lists "dim V distinct eigenvalues" among conditions equivalent to min = char.
`PR-OODAV` presents "C projective" and "A injective" as equivalent to one given sequence splitting.
`PR-KX7L7` infers right-exactness of −⊗X from preservation of injections.
`PR-TLBPS` states f separable ⟺ f' ≢ 0 over any field, without irreducibility.
`PR-ASW5L` states an ideal is free iff principal, without a domain hypothesis.
`PR-2ZW5Z` sends the number-field norm to Z and gives a ∈ K^× ⟺ N(a) = ±1. `PR-24CPI` writes [DN] = 0 and [UN] = 0 for [S, N] = 0 and [S, U] = 0. `PR-3TYBE` concludes Gal(K/k) = G. `PR-SLWTB` writes the order-pq classification as S_q ⋊ S_p, with the factors reversed and S used for cyclic groups.
`PR-N6S6P` asserts C_{2^k}^× ≅ C_2 × C_{2^{k−2}} for all k ≥ 1. `PR-EDD7U`, `PR-FYXFF` state the rational roots test backwards.
`PR-LJE4C` is titled "Third Isomorphism Theorem" and states the correspondence theorem.
`FF-2AKVH`, `FF-ED3CD`, `FF-HAMDC` give the factorisation identities with wrong exponents, and the x^n + y^n forms hold only for odd n. `FF-CY5EA` defines an element to be torsion by tor(m) ≠ 0, where tor is defined on modules.
`FF-I6XN6` lists ⟨a,b,c | a², b², c², abc⟩ as the fifth group of order 12; that is the Klein four-group.
`FF-JKCAM` lists ⟨a,b,c | a⁵, b², c²⟩ as the fifth of order 20. `FF-MBUKG` gives two nonabelian groups of order 18 where there are three.
`FF-UYMWY` states the one-step submodule test with M for the candidate submodule.

### Solutions that are wrong

`P-45CLI`, `P-GYQLA` invert the parity case analysis for the Cayley representation -- k even is said to yield odd cycles -- and the conclusion contradicts the problem statement.
The solution carries its own warning that it was not checked.
`P-HXTMK` gives χ_A as (x−1)²(x²+2)² for a minimal polynomial (x−1)(x²+1)², and both expansions of the second invariant factor are wrong.
`P-DGAQM`, `P-ESUCT` assert x^n − 1 is irreducible over Q and (Z/20)^× ≅ Z/8, then list four subfields of Q(ζ_20) where there are eight.
`P-NNNLA` asserts (Z/8)^× ≅ Z/4 and concludes Q(ζ_8) has exactly one quadratic subfield; it has three.
`P-3Q2XT` offers ⟨2, x⟩ ⊂ C[x, y] as a non-principal ideal; 2 is a unit there.
`P-EVBF7` builds its counterexample from Q(ζ_2, ∛2)/Q(∛2)/Q, and ζ_2 = −1. `P-RR26L` proves Schur triangularisation by building a block-diagonal matrix.
`P-UMKJ4` asserts every PID is a Euclidean domain, and its two conditions on ℓ_1, ℓ_2 disagree.
`P-GRL4N` states the minimal polynomial exponent is the geometric multiplicity.
`P-CGBXN`, `P-VYZEN` interchange E and F throughout the tower argument.
`P-LO76D` concludes Q is a Sylow p-subgroup where the problem asks only that Q contain one.
`P-NNJHK` gives the identity of Hom under addition as `id` and the inverse as f⁻¹. `P-ZGEFJ` proves IS is a submodule by closing it under multiplication by module elements.
`P-CBN4I`, `P-EHPA5`, `P-67U4W`, `P-6TCYA` divide conjugacy-class sizes into |H| rather than |G|, and use H, N and G interchangeably.
`P-G6OTF`, `P-RZ2JV` take infinitely many elements outside H to give [G : H] infinite.
`P-JG7FM` writes σ_k(α) = σ_{φ(n)−k}(α) where n − k is meant.
`P-2GXZ2` gives [a/1] as its own inverse.
`P-AP4TX` argues ker φ_ev = 0 from A = ⟨1_A⟩, false for a general abelian group.
`P-BZMTE` argues from "every prime power is odd".
`E-2ZO7O`, `P-C2WAH`, `E-AMD-UEHZOJ3K` carry the same garbled Zorn's-lemma argument for the nilradical in three copies.
`P-7IYBS` writes x² − 1 = x(x − 1). `P-7Q1AX` computes ker φ as {x : x | m}. `P-QE3QK` states the order as 148 and factors 248, then divides by 7 where 37 is meant.
`P-PS4CG` interchanges n_p and n_q and counts Sylow p-subgroups with q − 1 elements each.
`P-P3GIM` writes V ≅ k[x]/m(x) for a module that need not be cyclic.
`P-OX3MY` argues two vectors of im(T) cannot be orthogonal.
`P-63TON` describes the monic linear polynomials over Z[2√2] as having no rational integer part.
Its fraction field Q[2√2] is correct, since 2√2 ∈ Q[2√2] gives √2 ∈ Q[2√2]. `P-M3BT5` names its target extension L in the conclusion and F everywhere else.

### Cards with no mathematics in them

`P-IC2GD`: the body is five Obsidian image links and no text.
`L-CD6QT`: carries a footnote marker whose body is empty; it renders as a bare "1." at the foot of the Canonical Forms page.
`E-AMD-CZJRDRNT`: "Show that Q(2^{1/3}) and Q(ζ_3 2^{1/3})" -- the sentence ends there.
`P-3BNEC` and `P-A4V62` are the two halves of one question, split mid-sentence.
`E-N626Y`, `E-F2PUE` keep the fill-in-the-blank slots as `$\quad$`. `P-UE7LL` ends at "we proceed by cases:". `P-GN4CE`'s solution ends at "Suppose toward a contradiction that {g_1, ..., g_M} were a finite generating set".
`P-GFO6Q` part (c), `P-UQ4GC` part (c), `P-OG5DJ` part (c) are "???" or "??". `P-VI6QM` carries "Part (b) not finished!"
and a "(???)". `P-PC6ZW` ends at "A more direct proof:". `P-J6BNQ` carries "Not sure if this works" and "(?)", and its part (b) claims elements of H_1H_2 commute.
`P-0221B`, `P-0T149`, `P-1DBO7`, `P-1IM1B`, `P-1P5M4`, `P-23M4O`, `P-2KDVB`, `P-2WRPV`, `E-FODKS` and many others are solution bodies filed as `problem` or `exercise` cards, with no statement of the problem they solve.
This was common enough across the area that it was not counted.
`E-TK5YY`, `P-USAQT`, `P-S5JSR`, `P-TO7DK`, `E-MSDCC`, `P-4MDI2`, `P-ETEJW` are aggregates: one card carrying a bulleted list of many separate exercises.

### Cards in the wrong area

`P-52WSU` (Toeplitz operators), `P-F2XQP` (polar decomposition on a Hilbert space), `P-MZIFW` (generalising the spectral theorem), `P-25QBA` and `P-XZRST` (translation-invariant subspaces of L¹ and its convolution algebra) carry `algebra` and state analysis.
They come from the oral-exam question lists, which mix subjects.
They are collected in Linear Algebra with a lede sentence saying so, rather than dropped.

### Title derivation

`E-23SLE` and `E-XUSHV` carry their entire worked solution in the card title, so the catalog panels render them as a wall of displayed mathematics.
`P-6HPKO`, `P-YCLOT`, `P-QJ7MD` have titles beginning "(Important)".

### Duplicates

Reading the whole area surfaced many pairs stating the same mathematics under two ids, which `audit.py`'s `duplicate-bodies` will not catch where the wording differs.
Among them: `D-3ZPR7`/`D-BAD4E`, `D-3V3SP`/`D-DQPGU`, `D-P5D3T`/`D-VWRBP`, `D-MCUTE`/`D-VXJUY`, `D-QZ2LQ`/`D-XQ3I5`, `D-J5AAX`/`D-LIIHP`, `D-BGNME`/`D-D7L4X`, `D-HJR7M`/`D-JY5KT`, `D-3T6O2`/`D-BVOUL`, `D-7563L`/`D-NQZUY`, `D-4KM4P`/`D-CRWZ7`, `D-JNCUB`/`D-O26OY`, `C-A6UAR`/`C-O7CP3`, `C-CM7ZS`/`C-HE5SL`, `C-HWX2P`/`C-XRC67`, `T-F4O3E`/`T-GJNT5`, `T-KANHW`/`T-QYDVH`, `FT-2P5VV`/`T-CF6S3`, `FT-OXN3Y`/`T-JEZZY`, `PR-EDD7U`/`PR-FYXFF`, `PR-5PDNQ`/`PR-BHUO6`, `PR-LPJLD`/`PR-O5YUI`, `PR-GXII2`/`PR-TGFTL`, `PR-K6MMW`/`PR-MGRGF`, `PR-5A2W4`/`PR-IV6RB`, `PR-E6VI4`/`PR-PADL7`. Where both members were readable the guide names one and lets the panel return the other; no merge was performed, because deciding two cards state the same mathematics is a reading decision this pass was not asked to make.

## Two things this pass changed on the way

**The area name was being used as a topic.** 43 cards carried `topics: [algebra]`, which is the `areas` value repeated.
No panel can select on it -- the guide's queries are already scoped to the area -- so those cards belonged to no section.
They were read and reclassified in `95154bdc`.

No Algebra-area card carries `algebra` as a topic any longer, and none carries `analysis` either.
That is measured over the whole topic list, not just over cards whose only topic it was: zero of 2,368. The `algebra` registry entry itself is left in place in `vocabularies/topics.yaml`; whether it is retired is a decision for the areas that still use it.

**The study path rail indents one level per section and does not cap.** Written as a chain of seventeen, the rail squeezed "The Structure Theorem over a PID" to "Th ... PID" and clipped four other labels.
The manifest now uses `parent` for the actual prerequisite rather than for "comes after", which makes the hierarchy a tree five deep and every label render in full.
The reading order is unaffected: it follows the order of the sections in the manifest, and the foot navigation still runs 1 to 17. The rail defect itself is untouched and still live for any guide that chains more than about a dozen sections.
