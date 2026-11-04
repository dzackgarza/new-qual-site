# findings-3-D — SRC-TEXT-HAT02 §3.D (The Cohomology of SO(n))

Cards in section: **3** (E-HAT-3.D-1 … 3). Book exercise block: AT.txt **line 15093** ("Exercises"),
statements at **15094–15099**. In-text pointer to exercise 1 at **14620–14622**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.D-1 | **statement matches.** Book 15094–15096: "1. Show that a topological group with a finite-dimensional CW structure is an ori-entable manifold. [Consider the homeomorphisms x ֏ gx or x ֏ xg for fixed g and varying x in the group.]" Card keeps both sentences and the bracketed hint. (Only rendering differs: the book's mapsto glyph "֏" is written `\mapsto`.) | unread (statement layer only) |
| E-HAT-3.D-2 | **statement matches.** Book 15097–15098: "2. Using the CW structure on SO(n) , show that π1 SO(n) ≈ Z2 for n ≥ 3 . Find a loop representing a generator, and describe how twice this loop is nullhomotopic." | unread |
| E-HAT-3.D-3 | **statement matches.** Book 15099: "3. Compute the Pontryagin ring structure in H∗ (SO(5); Z) ." | unread |

## Defects
None at the statement level. All three statements are faithful, including the bracketed hint on
exercise 1 (AT 15095–15096).

## Census
Cards already carrying `source-checked` + `solution-written` + `solution-reviewed` in frontmatter
(all three authored `gpt-5.6-sol`, dates 2026-09-09): 3/3. Those frontmatter events are therefore
not evidence of a `claude` review; the section is unread in the sense of the task.

## PROOF AUDIT (read in full)

- **E-HAT-3.D-1 — proof correct.** Key steps check out: the complement of a single top-dimensional
  cell is a subcomplex hence closed, so `e^d` is open and ≅ R^d (this is Hatcher's own point at AT
  14619–14623, that SO(n) is connected because it has a CW structure with a single 0-cell); left
  translation is a homeomorphism, so every point has a Euclidean d-neighbourhood. The orientation
  transport is right: the transition map is `L_h L_g^{-1}=L_{hg^{-1}}` and the path `L_{γ(t)}` is an
  isotopy from the identity, so orientation class is preserved. One step is informal — "transport it
  to g by L_g" presupposes path-independence, which the following two sentences then supply — but
  the argument is complete and valid.
- **E-HAT-3.D-2 — proof correct** (checked against AT 14620–14700 and 14787–14798). Cells are
  indexed by admissible sequences with cell dimension the sum of the entries (AT 14795–14797: "this
  product of spheres also has cells in one-to-one correspondence with admissible sequences"), so for
  n ≥ 3 the 2-skeleton has exactly e^0, e^1, e^2. The 2-cell of RP^{n-1} attaches to RP^1 by the
  double cover, giving ⟨a | a²⟩ = Z_2, and higher cells do not change π1. The geometric description
  of the generator (a 2-plane rotating through 0 ≤ θ ≤ 2π) and of the nullhomotopy of twice it (the
  characteristic map of e² traverses e¹ twice) is consistent with that attaching map.
- **E-HAT-3.D-3 — proof has a (minor) gap.** The additive answer is right: free Z in degrees
  0,3,7,10 and Z_2 in 1,3,4,5,6,8 is exactly what the book's own description gives — AT 15085–15091
  ("Thus SO(n) has the same homology and cohomology groups as the product space V3,2 × V5,2 × ··· "),
  combined with the table H_i(V_{2k+1,2};Z) = Z for i = 0,4k−1 and Z_2 for i = 2k−1 (AT 15080–15084).
  But the card *asserts* "The cellular complex of SO(5) is C^2⊗C^4" and then invokes the integral
  Künneth theorem on it. That isomorphism of chain complexes is nowhere established, and AT
  15086–15089 explicitly says SO(n) is *distinguished* from the product by its cup product
  structure, so the product's complex cannot simply be substituted for SO(5)'s. The Künneth
  computation of the groups is therefore unsupported (though its output is correct). Two further
  assertions are used without argument: that `bd` generates H_10(SO(5);Z), and that reduction mod 2
  is injective on each 2-torsion subgroup (true, but only for 2-groups). The mod-2 input the card uses
  ("exterior algebra on e^1,e^2,e^3,e^4") is correct: it is the Hopf-algebra dual of Theorem 3D.2's
  Z_2[β_i]/(β_i^{p_i}) (AT 14799–14801).
# findings-3-F — SRC-TEXT-HAT02 §3.F (Limits and Ext)

Cards in section: **9** (E-HAT-3.F-1 … 9). Book exercise block: AT.txt **line 15973**
("Exercises"), statements at **15974–16015** and **16021–16023**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.F-1 | **statement matches** (AT 15974–15979). Only orthography differs: book "glueing", card "gluing"; book prints ‘reverse mapping telescope’ in single quotes. | unread |
| E-HAT-3.F-2 | **statement matches** (AT 15981–15984). The book's lim with a superscript 1 is rendered `\varprojlim^1`. | unread |
| E-HAT-3.F-3 | **statement matches**, bracketed hint kept (AT 15985–15986). | unread |
| E-HAT-3.F-4 | **statement matches** (AT 15988–15991); "iff" expanded to "if and only if", same content. | unread |
| E-HAT-3.F-5 | **statement matches** (AT 15992–15995), including Ext(Z_{p^∞},Z) ≈ Ẑ_p. | unread |
| E-HAT-3.F-6 | **statement matches** (AT 15996). | unread |
| E-HAT-3.F-7 | **statement matches** (AT 15997–16003). | unread |
| E-HAT-3.F-8 | **statement matches** (AT 16005–16009). | unread |
| E-HAT-3.F-9 | **statement differs** — see defects 1 and 2. | unread |

## Defects (most serious first)

1. **E-HAT-3.F-9(a): an "iff" halved to "if".** Book, AT **16022**:
   "(a) Ext(A, Z) is divisible iff A is torsionfree."
   Card: "(a) $\operatorname{Ext}(A, \ZZ)$ is divisible if $A$ is torsionfree."
   The card states only one direction and drops "iff". Part (b) on the same lines keeps its "if …
   and the converse holds if", so the loss is not a house style.
2. **E-HAT-3.F-9: the displayed six-term sequence is not witnessed by AT.txt.** Book, AT **16014–16015**:
   "sequences 0→p A→A→pA→0 and 0→pA→A→Ap →0 can be spliced together to yield the exact sequence
   across the top of the following diagram", and AT **16021**: "where the map labeled ‘ p ’ is
   multiplication by p ." The sequence itself is printed as a *diagram*, which the extraction does
   not carry (AT 16016 is the page break to p.321 and 16017–16020 are blank). The card instead
   prints the formula
   `Hom(pA,Z) → Ext(A_p,Z) → Ext(A,Z) →^p Ext(A,Z) → Ext(_pA,Z) → 0`
   as if it were the book's text. The formula is the correct splicing of the two six-term sequences
   (naturality of the connecting map makes Ext(pA,Z)→Ext(A,Z) multiplication by p), but no line of
   AT.txt supports it verbatim, so this is an unverified reconstruction presented as source text.

## Census
Cards already carrying `source-checked`/`solution-written`/`solution-reviewed` in frontmatter
(9/9, all `gpt-5.6-sol`): the frontmatter claim "the stored statement matches" is false for
E-HAT-3.F-9(a) at minimum.

## PROOF AUDIT (read in full)

- **E-HAT-3.F-1 — proof correct.** Retracts each M_i onto its top copy X_{i+1}, schedules the
  collapses on [0,1/2], [1/2,3/4], [3/4,7/8], … so every t < 1 involves finitely many cylinders and
  every point is in X_0 at t = 1; continuity follows from the coherent (weak) topology of the union.
  The double-telescope case is then the same argument applied to the left-hand half plus the identity
  on T_{≥n}. Correct.
- **E-HAT-3.F-2 — proof correct.** Φ((g_i)) = (g_i − α_{i+1}(g_{i+1})) has kernel lim and cokernel
  lim¹; the Mittag-Leffler hypothesis makes I_i = im(G_j → G_i) stable, the bonding maps I_{i+1} → I_i
  are onto, and the displayed recursion solves Φ(g) = b exactly (each g_i − b_i lies in I_i, and
  α_{i+1}: I_{i+1} → I_i is onto). The quotient tower is pro-zero, a zero-bonding tower has Φ = id,
  and the six-term lim/lim¹ sequence of 0 → I_i → G_i → Q_i → 0 finishes. The passage to a cofinal
  subsequence is legitimate for lim¹ on a countable tower. Correct.
- **E-HAT-3.F-3 — proof correct**, but by a different route from the book's hint: it uses Baer's
  criterion (Q divisible ⇒ injective) and a free resolution, so Ext¹(A,Q) = coker(Hom(F_0,Q) →
  Hom(F_1,Q)) = 0. Valid. The card drops the book's hint, which is the statement defect recorded
  above.
# findings-3-H — SRC-TEXT-HAT02 §3.H (Local Coefficients)

Cards in section: **6** (E-HAT-3.H-1 … 6). Book exercise block: AT.txt **line 16834**
("Exercises"), statements at **16835–16863**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.H-1 | **statement matches** (AT 16835). | unread |
| E-HAT-3.H-2 | **statement matches** (AT 16836–16837). | unread |
| E-HAT-3.H-3 | **statement matches** (AT 16838–16842). Book prints ‘identity’ in single quotes; card uses plain quotes. | unread |
| E-HAT-3.H-4 | **statement matches** (AT 16843–16845). | unread |
| E-HAT-3.H-5 | **statement matches**, bracketed hint kept, including "compute H_c^n(X̃) as lim→ H^n(X̃, X̃ − T_i)" (AT 16846–16854). | unread |
| E-HAT-3.H-6 | **statement matches** (AT 16856–16863). | unread |

## Defects
None at the statement level.

## Census
6/6 cards carry `source-checked`/`solution-written`/`solution-reviewed` (`gpt-5.6-sol`,
2026-09-09).

## PROOF AUDIT (read in full)

- **E-HAT-3.H-1 — proof correct.** With monodromy −1 the twisted cellular differential is
  (−1) − 1 = −2 on the 1-cell: H_1 = ker(−2) = 0, H_0 = coker(−2) = Z_2; dually H^0 = 0, H^1 = Z_2.
  Both answers are right (sign conventions give ±2, same kernel and cokernel).
- **E-HAT-3.H-2 — proof correct.** Poincaré duality with local coefficients H_k(M;M_Z) ≅
  H^{n−k}(M;Z) is the right tool; H_1(N_g;Z) = Z^{g−1} ⊕ Z_2 and H_2 = 0 give H^0 = Z, H^1 = Z^{g−1},
  H^2 = Z_2 by the universal coefficient theorem; hence H_2 = Z, H_1 = Z^{g−1}, H_0 = Z_2. The
  independent cellular check (d_1(a_i) = −2e^0, d_2(e²) = Σ(1 + (−1))a_i = 0) agrees, including
  ker(d_1) = Z^{g−1} (coefficients summing to zero).
- **E-HAT-3.H-3 — proof correct.** Bundles of groups with fiber G over X ↔ monodromy
  π1(X) → Aut(G) up to conjugacy, and [X, BAut(G)] ≅ Hom(π1 X, Aut G)/Inn for X a CW complex; the
  pullback construction is the inverse. The disconnected case is handled componentwise.
- **E-HAT-3.H-4 — proof correct.** The lift of a homotopy equivalence between finite complexes is
  equivariant for the identification of deck groups by f_*; a compact subset of a universal cover
  meets only finitely many translates of a fundamental finite subcomplex, so inverse images of
  compacts are compact, and the same finite-fundamental-domain argument works uniformly in the
  homotopy parameter. Proper homotopy inverses follow.
- **E-HAT-3.H-5 — proof has a gap.** The final answer (Z for g = 1, countable free for g > 1) is
  right and matches the book (AT 16847–16848), but the key step is not justified: the card asserts
  "the maps H̃^0(X̃−T_i) → H̃^0(X̃−T_{i+1}) are split injections". Under the identification
  H^1(X̃, X̃−T_i) ≅ H̃^0(X̃−T_i) the transition map sends a function on components of X̃−T_i to the
  function on components of X̃−T_{i+1} that is constant on the descendants of each component — and
  that is *not* sum-zero preserving, so it is not even a map H̃^0 → H̃^0 as claimed. What the argument
  needs is the (true) statement that the colimit has countable rank; asserting split injectivity with
  a "distinguished descendant" does not supply it. Everything before that step is right:
  H^n(X̃,X̃−T_i) = 0 for n ≠ 1, and H^1 ≅ H̃^0(X̃−T_i) of rank c_i − 1.
- **E-HAT-3.H-6 — proof correct.** Local finiteness is preserved by ∂ (a neighbourhood meeting a
  face's image also meets its parent's), so C_*^{lf} is a complex; the relative locally finite
  homology of successive skeleta is ∏G in degree n and 0 elsewhere (product, not sum — correctly
  noted), and finite-dimensionality makes the skeletal comparison converge, giving the infinite
  cellular chain complex.
# findings-4-1b — SRC-TEXT-HAT02 §4.1, exercises **10–23** (unread part of the section)

Cards: **14** in the unread range (E-HAT-4.1-10 … 4.1-23); exercises 1–9 of §4.1 are already
read and are not audited here. Section directory holds 23 cards in total.
Book exercise block: AT.txt **line 17817** ("Exercises"), exercise 10 at **17861**, exercise 23
at **17913–17915**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.1-10 | **statement matches** (AT 17861–17862). | unread |
| E-HAT-4.1-11 | **statement matches**, including the sentence "An example is S^∞, or more generally the infinite suspension S^∞X …" (AT 17863–17865 with 17869–17870 across the page break). | unread |
| E-HAT-4.1-12 | **statement matches** (AT 17871). | unread |
| E-HAT-4.1-13 | **statement matches in substance** (AT 17872–17873: "Use the extension lemma to show that a CW complex retracts onto any contractible subcomplex."). The card *adds* an editorial gloss "(homotopy extension property for CW pairs)" and names the variables X, A; nothing of the book's content is lost, but the gloss is not book text. | unread |
| E-HAT-4.1-14 | **statement matches** (AT 17874–17875). | unread |
| E-HAT-4.1-15 | **statement differs** — part (c) drops a parenthetical instruction (defect 1). | unread |
| E-HAT-4.1-16 | **statement matches** (AT 17887–17889). | unread |
| E-HAT-4.1-17 | **statement matches** (AT 17890–17891). | unread |
| E-HAT-4.1-18 | **statement matches** (AT 17892–17893). | unread |
| E-HAT-4.1-19 | **statement differs** — "iff" halved to "if" (defect 2). | unread |
| E-HAT-4.1-20 | **statement matches** (AT 17898–17899). | unread |
| E-HAT-4.1-21 | **statement matches** (AT 17900–17906), including "so the notation X_m^n is unambiguous" and the range "m ≤ i ≤ n". | unread |
| E-HAT-4.1-22 | **statement differs** — "iff" halved to "if" and the bracketed hint dropped (defect 3). | unread |
| E-HAT-4.1-23 | **statement matches** (AT 17913–17915). | unread |

## Defects (most serious first)

1. **E-HAT-4.1-22: "iff" halved, and the hint dropped.** Book, AT **17907–17909**:
   "Show that a path-connected space X has a CW approximation with countably many cells iff πn (X)
   is countable for all n . [Use the results on simplicial approximations to maps and spaces in
   §2.C.]"
   Card: "Show that a path-connected space $X$ has a CW approximation with countably many cells if
   $\pi_n(X)$ is countable for all $n$."
   Both halves of the equivalence are lost (only ⇐ remains) and the whole bracketed pointer to §2.C
   is gone.
2. **E-HAT-4.1-19: "iff" halved.** Book, AT **17894–17896**:
   "Show that X ≃w Y iff X and Y have a common CW approximation."
   Card: "Show that $X \simeq_w Y$ if $X$ and $Y$ have a common CW approximation." — again only ⇐.
3. **E-HAT-4.1-15(c): parenthetical instruction dropped.** Book, AT **17886**:
   "(Use Gaussian elimination, for example.)" The card's (c) ends at "…the matrix of a reflection."
   The book prints this as an italic hint inside part (c); it is part of the printed exercise.

## Census
23 cards in the section; 14 in the unread range. Every card carries `source-checked` /
`solution-written` / `solution-reviewed` (`gpt-5.6-sol`, 2026-09-09), so frontmatter again gives no
evidence of the `claude` review that marks the read sections.

## PROOF AUDIT
All 14 proofs in exercises 10–23 are **unread** — only the statement layer was audited here.
# findings-4-2 — SRC-TEXT-HAT02 §4.2 (Elementary Methods of Calculation)

Cards in section: **39** (E-HAT-4.2-1 … 4.2-39). Book exercise block: AT.txt **line 19319**
("Exercises"), statements at **19320–19498**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.2-1 | **statement matches** (AT 19320). | unread |
| E-HAT-4.2-2 | **statement matches** (AT 19321–19322). | unread |
| E-HAT-4.2-3 | **statement matches** (AT 19323–19324). | unread |
| E-HAT-4.2-4 | **statement matches** (AT 19325–19328), including the product over k. | unread |
| E-HAT-4.2-5 | **statement differs** — the definition of the mapping torus is dropped (defect 6). | unread |
| E-HAT-4.2-6 | **statement matches** (AT 19337–19339). | unread |
| E-HAT-4.2-7 | **statement matches** (AT 19340–19341). | unread |
| E-HAT-4.2-8 | **statement matches** (AT 19342). | unread |
| E-HAT-4.2-9 | **statement matches** (AT 19343–19345). | unread |
| E-HAT-4.2-10 | **statement matches** (AT 19346–19351). | unread |
| E-HAT-4.2-11 | **statement matches** (AT 19352–19355). | unread |
| E-HAT-4.2-12 | **statement differs** — bracketed restatement in local coefficients dropped (defect 7). | unread |
| E-HAT-4.2-13 | **statement differs** — bracketed hint dropped (defect 9). | unread |
| E-HAT-4.2-14 | **statement differs** — bracketed hint dropped (defect 10). | unread |
| E-HAT-4.2-15 | **statement differs** — whole bracketed commentary dropped (defect 3). | unread |
| E-HAT-4.2-16 | **statement matches** (AT 19378–19380). | unread |
| E-HAT-4.2-17 | **statement matches** (AT 19381–19385), including "Deduce that CW complex K(G, n)'s are uniquely determined …". | unread |
| E-HAT-4.2-18 | **statement differs** — bracketed hint dropped (defect 8). | unread |
| E-HAT-4.2-19 | **statement matches** (AT 19391). | unread |
| E-HAT-4.2-20 | **statement matches** (AT 19392–19393). | unread |
| E-HAT-4.2-21 | **statement matches** (AT 19394–19398). | unread |
| E-HAT-4.2-22 | **statement differs** — bracketed construction dropped (defect 11). | unread |
| E-HAT-4.2-23 | **statement differs** — long bracketed argument dropped (defect 5). | unread |
| E-HAT-4.2-24 | **statement differs** — bracketed hint dropped (defect 4). | unread |
| E-HAT-4.2-25 | **statement matches** (AT 19420–19422). | unread |
| E-HAT-4.2-26 | **statement matches** (AT 19423–19427). | unread |
| E-HAT-4.2-27 | **statement differs** — the parenthetical "(This exercise should be in §4.1.)" dropped (defect 13). | unread |
| E-HAT-4.2-28 | **statement differs** — the entire "by filling in details of the following argument …" body dropped (defect 2). | unread |
| E-HAT-4.2-29 | **statement differs** — parts (a),(b),(c) with their hints dropped (defect 1). | unread |
| E-HAT-4.2-30 | **statement matches** (AT 19467–19468). | unread |
| E-HAT-4.2-31 | **statement matches** (AT 19469–19475); the two displayed isomorphisms are inlined, same content. | unread |
| E-HAT-4.2-32 | **statement differs** — bracketed hint dropped (defect 12). | unread |
| E-HAT-4.2-33 | **statement matches** (AT 19478–19480). | unread |
| E-HAT-4.2-34 | **statement matches** (AT 19481–19484). | unread |
| E-HAT-4.2-35 | **statement matches** (AT 19485–19487). | unread |
| E-HAT-4.2-36 | **statement matches** (AT 19488–19489). | unread |
| E-HAT-4.2-37 | **statement matches** (AT 19490). | unread |
| E-HAT-4.2-38 | **statement matches** (AT 19491–19493). | unread |
| E-HAT-4.2-39 | **statement matches** (AT 19494–19498). | unread |

## Defects (most serious first)

1. **E-HAT-4.2-29: three-part exercise reduced to its first sentence.** Book, AT **19436–19443** and
   **19444–19457**, **19461–19466**: after "… are homotopy equivalent if ℓ1 ··· ℓn ≡ ±kn ℓ1′ ··· ℓn′
   mod m for some integer k , **via the following steps:**" the book prints (a) "Reduce to the case
   k = 1 … [Rechoose the generator of the Zm action on S 2n−1 .]", (b) a construction of a map g with
   "degree k1 ··· kn + dm" and the hint "[Show first that a lift of g to the universal cover S 2n−1
   has this degree.]", and (c) the closing argument with "[For πi with i > 1 , consider a lift of g
   to the universal cover.]". The card keeps only the first sentence and drops "via the following
   steps" and all of (a),(b),(c). This is the largest single statement loss in the section: the
   card's "problem" is no longer the printed exercise.
2. **E-HAT-4.2-28: the argument the exercise asks you to fill in is deleted.** Book, AT **19430–19435**:
   "Show that the group Zp × Zp with p prime cannot act freely on any sphere S n , by filling in
   details of the following argument. Such an action would define a covering space S n →M with M a
   closed manifold. When n > 1 , build a K(Zp × Zp , 1) from M by attaching a single (n + 1) cell and
   then cells of higher dimension. Deduce that H n+1 (K(Zp × Zp , 1); Zp ) is Zp or 0 , a
   contradiction. (The case n = 1 is more elementary.)"
   The card is only "Show that the group $\ZZ_p \times \ZZ_p$ with $p$ prime cannot act freely on any
   sphere $S^n$." Everything that makes the exercise an exercise — the covering space, the cell
   attachment, the cohomology contradiction, and the n = 1 remark — is gone.
3. **E-HAT-4.2-15: the whole bracketed commentary dropped.** Book, AT **19371–19377**:
   "Show that a closed simply-connected 3 manifold is homotopy equivalent to S 3 . [Use Poincaré
   duality, and also the fact that closed manifolds are homotopy equivalent to CW complexes, from
   Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3 manifold
   is homeomorphic to S 3 is the Poincaré conjecture, finally proved by Perelman. The
   higher-dimensional analog, that a closed n manifold homotopy equivalent to S n is homeomorphic to
   S n , had been proved earlier for all n ≥ 4 .]"
   Card keeps the first sentence only.
4. **E-HAT-4.2-24: both hints dropped.** Book, AT **19415–19419**: "… iff H2 (K(G, 1); Z) = 0 .
   [Use the preceding problem. Build such an M(G, 1) from the 2 skeleton K 2 of a K(G, 1) by
   attaching 3 cells according to a basis for the free group H2 (K 2 ; Z) .] In particular, there is
   no M(Zn , 1) with fundamental group Zn , free abelian of rank n , if n ≥ 2 ." The card keeps the
   iff and the "In particular" sentence but drops the bracket. (Note: it does keep the iff — one of
   the few cards in the corpus that does.)
5. **E-HAT-4.2-23: the bracketed construction dropped.** AT **19408–19413**: "[Build a K(πn (X), n)
   from X by attaching cells of dimension n + 2 and greater, and then consider the homology sequence
   of the pair (Y , X) where Y is X with the (n + 2) cells of K(πn (X), n) attached. Note that the
   image of the boundary map Hn+2 (Y , X)→Hn+1 (X) coincides with the image of h , and Hn+1 (Y ) ≈
   Hn+1 (K(πn (X), n)) . The previous exercise is needed for the case n > 1 .]"
6. **E-HAT-4.2-5: the mapping-torus definition dropped.** Book, AT **19331–19332**: "Let X be the
   mapping torus of f , the quotient space of (Sα2 ∨ Sβ2 )× I under the identifications (x, 0) ∼
   (f (x), 1) ." The card reads "Let $X$ be the mapping torus of $f$." — a real loss, since the
   identification convention is what fixes the attaching data the exercise uses.
7. **E-HAT-4.2-12: bracketed restatement in local coefficients dropped.** AT **19359–19364**:
   "[The latter condition can be restated in terms of homology with local coefficients as saying that
   f∗ : H∗ (X; Z[π1 X])→H∗ (Y ; Z[π1 Y ]) is an isomorphism; see §3.H.]"
8. **E-HAT-4.2-18: bracketed hint dropped** — AT **19389–19390**: "[Use the Künneth formula.]"
9. **E-HAT-4.2-13: bracketed hint dropped** — AT **19366–19367**: "[Pass to universal covers and use
   homology.]"
10. **E-HAT-4.2-14: bracketed hint dropped** — AT **19369–19370**: "[Use the Hurewicz homomorphism.]"
11. **E-HAT-4.2-22: bracketed construction dropped** — AT **19399–19400**: "[Build a K(G, n) from a
    Moore space M(G, n) by attaching cells of dimension > n + 1 .]"
12. **E-HAT-4.2-32: bracketed hint dropped** — AT **19477**: "[Look at the long exact sequence of
    homotopy groups.]"
13. **E-HAT-4.2-27: printed parenthetical dropped** — AT **19429**: "(This exercise should be in
    §4.1.)"

## Census
39 cards; 13 of 39 statements differ from the printed text (33%). All 39 carry `source-checked` /
`solution-written` / `solution-reviewed` (`gpt-5.6-sol`), which is evidently wrong for the 13.

## PROOF AUDIT
All 39 proofs in this section are **unread** — only the statement layer was audited here.
# findings-4-3 — SRC-TEXT-HAT02 §4.3 (Connections with Cohomology)

Cards in section: **24** (E-HAT-4.3-1 … 4.3-24). Book exercise block: AT.txt **line 20754**
("Exercises"), statements at **20755–20830**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.3-1 | **statement matches** (AT 20755–20758), including "How is this consistent with the universal coefficient theorem?" | unread |
| E-HAT-4.3-2 | **statement matches** (AT 20759–20761). | unread |
| E-HAT-4.3-3 | **statement matches** (AT 20762–20764). | unread |
| E-HAT-4.3-4 | **statement matches** (AT 20765–20767). | unread |
| E-HAT-4.3-5 | **statement differs** — bracketed construction dropped (defect 4). | unread |
| E-HAT-4.3-6 | **statement matches** (AT 20770–20773). | unread |
| E-HAT-4.3-7 | **statement matches** (AT 20774–20776). | unread |
| E-HAT-4.3-8 | **statement matches** (AT 20777–20778). | unread |
| E-HAT-4.3-9 | **statement differs** — bracketed hint dropped (defect 5). | unread |
| E-HAT-4.3-10 | **statement matches** (AT 20781–20786). | unread |
| E-HAT-4.3-11 | **statement matches** (AT 20790–20792). | unread |
| E-HAT-4.3-12 | **statement matches** (AT 20793–20794). | unread |
| E-HAT-4.3-13 | **statement differs** — bracketed approach dropped (defect 2). | unread |
| E-HAT-4.3-14 | **statement differs** — bracketed cross-reference dropped (defect 3). | unread |
| E-HAT-4.3-15 | **statement matches** (AT 20802–20803). | unread |
| E-HAT-4.3-16 | **statement matches** (AT 20804–20806). | unread |
| E-HAT-4.3-17 | **statement matches** (AT 20807). | unread |
| E-HAT-4.3-18 | **statement matches** (AT 20808–20810), including the counts "except for the last three terms / abelian groups except for the last six terms". | unread |
| E-HAT-4.3-19 | **statement matches** (AT 20811–20816), including the improvement to "iff they are in the same orbit". | unread |
| E-HAT-4.3-20 | **statement matches** (AT 20817–20818). | unread |
| E-HAT-4.3-21 | **statement matches** (AT 20819–20820). | unread |
| E-HAT-4.3-22 | **statement matches** (AT 20821–20823). | unread |
| E-HAT-4.3-23 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.3-24 | **statement matches** (AT 20828–20830). | unread |

## Defects (most serious first)

1. **E-HAT-4.3-23: bracketed hint dropped.** Book, AT **20827**: "… then such a Y is unique up to
   homotopy equivalence. [Use Corollary 4.73 with W the mapping cylinder of X →Y .]" The card ends at
   "unique up to homotopy equivalence." The hint names the exact tool the uniqueness argument needs,
   and 4.73 is the only route the book supplies.
2. **E-HAT-4.3-13: bracketed approach dropped.** AT **20796–20797**: "[One approach is to use
   Corollary 0.21 to reduce to the case of deformation retractions.]"
3. **E-HAT-4.3-14: bracketed cross-reference dropped.** AT **20801**: "[See Exercises 11 and 13.]"
4. **E-HAT-4.3-5: bracketed construction dropped.** AT **20768–20769**: "[Build a K(Z, n) from S n by
   attaching cells of dimension ≥ n + 2 .]"
5. **E-HAT-4.3-9: bracketed hint dropped.** AT **20780**: "[Use the preceding problem.]"

## Census
24 cards; 5 of 24 statements differ (all by a dropped bracket, one of them the substantive hint in
4.3-23). All 24 carry `source-checked` / `solution-written` / `solution-reviewed` (`gpt-5.6-sol`).

## PROOF AUDIT
All 24 proofs in this section are **unread** — only the statement layer was audited here.
# findings-4-A — SRC-TEXT-HAT02 §4.A (Basepoints and Homotopy)

Cards in section: **5** (E-HAT-4.A-1 … 5). Book exercise block: AT.txt **line 21092**
("Exercises"), statements at **21093–21129**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.A-1 | **statement matches** (AT 21093–21095). | unread |
| E-HAT-4.A-2 | **statement differs** — the final "In particular …" sentence is dropped (defect 1). | unread |
| E-HAT-4.A-3 | **statement matches** (AT 21102–21106). | unread |
| E-HAT-4.A-4 | **statement differs** — the bracketed identification of GL_n(Z) is dropped (defect 2). | unread |
| E-HAT-4.A-5 | **statement matches** (AT 21114–21129); "(a) … 2 dimensional" is hyphenated in the card, no change of content. | unread |

## Defects (most serious first)

1. **E-HAT-4.A-2: a printed consequence of the exercise is dropped.** Book, AT **21100–21101**:
   "Deduce a bijection of [X, K(π , 1)] with the set of orbits of Hom(π1 (X), π ) under composition
   with inner automorphisms of π . **In particular, if π is abelian then [X, K(π , 1)] = hX, K(π , 1)i
   = Hom(π1 (X), π ) .**"
   The card stops after "… inner automorphisms of π." The dropped sentence is the special case the
   section actually uses.
2. **E-HAT-4.A-4: bracketed hint dropped.** AT **21113**: "[ GLn (Z) is the automorphism group of
   Zn ≈ πk (∨n S k ) ≈ Hk (∨n S k ) .]"

## Census
5 cards; 2 of 5 statements differ. All 5 carry `source-checked` / `solution-written` /
`solution-reviewed` (`gpt-5.6-sol`).

## PROOF AUDIT

- **E-HAT-4.A-1 — proof correct.** F(z,t) = H(z,t)·γ(t)^{-1} with γ(t) = H(z_0,t) a loop at x_0 is
  continuous, has the right two time slices, and satisfies F(z_0,t) = x_0 for all t.
- **E-HAT-4.A-2 — proof correct.** A loop-action homotopy H from f to γf yields, on composing with
  a: S^n → X, a homotopy from fa to (γf)a whose basepoint traces γ, so [(γf)a] = β_γ[fa] for all a,
  i.e. (γf)_* = β_γ f_*; in degree 1 β_γ is conjugation by γ, and free homotopy classes are orbits,
  giving [X,K(π,1)] ≅ Hom(π1X,π)/Inn(π).
- **E-HAT-4.A-3 — proof correct.** Φ: Aut(K(π,1)) → Out(π) is well defined (changing the path
  changes by an inner automorphism); conversely [K,K] ≅ Hom(π,π)/Inn(π) and a map is a homotopy
  equivalence iff its endomorphism of π is an automorphism (a map inducing f_*^{-1} is an inverse
  because the composites induce the identity outer automorphism and hence are freely homotopic to the
  identity). Hence Aut(K(π,1)) ≅ Out(π).
- **E-HAT-4.A-4 — proof unread.**
- **E-HAT-4.A-5 — proof unread.**
# findings-4-B — SRC-TEXT-HAT02 §4.B (The Hopf Invariant)

Cards in section: **2** (E-HAT-4.B-1, 4.B-2). Book exercise block: AT.txt **line 21215**
("Exercises"), statements at **21217–21223**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.B-1 | **statement matches** (AT 21217–21220), both H(gf) = (deg f)H(g) and H(gf) = (deg g)²H(f). | unread |
| E-HAT-4.B-2 | **statement differs** — the bracketed hint is dropped (defect 1). | unread |

## Defects

1. **E-HAT-4.B-2: bracketed hint dropped.** Book, AT **21223**: "… when n > 1 , H(p) = ±1 . [Show
   that Cp is a manifold and apply Poincaré duality.]" The card ends at "H(p) = ±1." The hint is the
   only indication of how the degree is to be computed; §4.D exercise 5 (AT 22161–22164) asks for the
   same result by a different route.

## Census
2 cards; 1 differs. Both carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.B-1 — proof correct.** With x_h ∈ H^n(C_h) the generator and x_h² = H(h)y_h: for
  g∘f the map C_{gf} → C_g is the identity on the bottom cell and has degree d on the top, so pulling
  back gives x_{gf}² = dH(g)y_{gf}, i.e. H(gf) = (deg f)H(g); in the other order the map
  C_f → C_{gf} is g on the bottom cell and degree 1 on the top, so x_{gf} pulls back to d x_f and
  d²H(f) = H(gf). Both computations are right, including the direction of pullback.
- **E-HAT-4.B-2 — proof correct.** m = n + k from local triviality; for n > 1 the base is simply
  connected, the fiber is not S^0, and π_n(S^m) → π_n(S^n) → π_{n−1}(S^k) with π_n(S^m) = 0 forces
  k ≤ n − 1, while k < n − 1 makes π_{k+1}(S^n) → π_k(S^k) → π_k(S^m) read 0 → Z → 0; so k = n−1,
  m = 2n−1 (and n = 1 forces k = 0, the double cover). Then C_p is a closed 2n-manifold (as the
  book's hint at AT 21223 prescribes), its middle cohomology is Z, and unimodularity of the
  intersection form forces H(p) = ±1. Only the orientability of C_p is stated rather than argued (it
  follows from simple connectivity of S^n, n > 1, which is available) — not a gap in substance.
# findings-4-D — SRC-TEXT-HAT02 §4.D (Cohomology of Fiber Bundles)

Cards in section: **10** (E-HAT-4.D-1 … 4.D-10). Book exercise block: AT.txt **line 22149**
("Exercises"), statements at **22150–22189**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.D-1 | **statement matches** (AT 22150–22154). | unread |
| E-HAT-4.D-2 | **statement matches** (AT 22155–22156). | unread |
| E-HAT-4.D-3 | **statement matches** (AT 22157–22158). | unread |
| E-HAT-4.D-4 | **statement matches** (AT 22159–22160). | unread |
| E-HAT-4.D-5 | **statement differs** — bracketed consequence dropped (defect 1). | unread |
| E-HAT-4.D-6 | **statement differs** — bracketed remark dropped (defect 2). | unread |
| E-HAT-4.D-7 | **statement matches** (AT 22170–22171). | unread |
| E-HAT-4.D-8 | **statement matches** (AT 22172–22176). | unread |
| E-HAT-4.D-9 | **statement differs** — bracketed hint dropped (defect 3). | unread |
| E-HAT-4.D-10 | **statement differs** — parenthetical remark dropped (defect 4). | unread |

## Defects (most serious first)

1. **E-HAT-4.D-10: the printed parenthetical is dropped.** Book, AT **22184–22186**: "(The usual
   argument over C involving roots of the characteristic polynomial does not work due to the lack of
   a good quaternionic determinant function.)" Nothing else in the book states why the exercise is
   not immediate.
2. **E-HAT-4.D-5: bracketed consequence dropped.** AT **22164**: "[Hence n = 1, 2, 4, 8 by Adams'
   theorem.]"
3. **E-HAT-4.D-9: bracketed hint dropped.** AT **22181–22182**: "[Hint: Diagonal matrices in U(n) are
   compositions of scalar multiplication in n lines in Cn , and CPn−1 is connected.]"
4. **E-HAT-4.D-6: bracketed remark dropped.** AT **22168–22169**: "[When n > 1 there are examples where
   M is not homeomorphic to CPn .]" — this is the remark that makes the converse worth proving.

## Census
10 cards; 4 of 10 statements differ. All 10 carry `source-checked` / `solution-written` /
`solution-reviewed` (`gpt-5.6-sol`).

## PROOF AUDIT
All 10 proofs in this section are **unread** — only the statement layer was audited here.
# findings-4-F — SRC-TEXT-HAT02 §4.F (Spectra and Homology Theories)

Cards in section: **3** (E-HAT-4.F-1 … 3). Book exercise block: AT.txt **line 22600**
("Exercises"), statements at **22601–22615**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.F-1 | **statement matches** (AT 22601–22603). | unread |
| E-HAT-4.F-2 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.F-3 | **statement matches** (AT 22612–22615); the book's lim→ with mapping telescopes is rendered `\operatorname{hocolim}`, same content. | unread |

## Defects

1. **E-HAT-4.F-2: bracketed hint dropped.** Book, AT **22610–22611**: "… these maps eventually become
   isomorphisms. [Use induction on the number of cells of X and the five-lemma.]" The card ends at
   "isomorphisms." The hint is the whole proof strategy; without it the statement is a different
   (harder) problem.

## Census
3 cards; 1 differs. All 3 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.F-1 — proof correct.** Direct limit ⇒ wedge: finite subcomplexes of a wedge are
  contained in finite sub-wedges, where the finite wedge axiom holds, and the filtered colimit of the
  finite-wedge decompositions is the direct sum. Converse for countable X: the telescope T ≃ X, the
  even/odd cover with Mayer–Vietoris and the wedge axiom gives ⊕ →^{1−s_*} ⊕ → h̃_n(T) → …, and
  1 − s_* on a direct sum is injective by inspecting the *first* nonzero coordinate (so coker = colim).
  This is exactly the exercise's content.
- **E-HAT-4.F-2 — proof correct**, and it is the book's own prescribed route (AT 22610–22611: "[Use
  induction on the number of cells of X and the five-lemma.]"). Base case is Freudenthal with
  connectivity of Σ^rY growing in r; the step uses the Puppe sequences of S^{q−1} → A → X → S^q and
  the five lemma, and ⟨Σ^rX, Σ^rY⟩ is a group for r large enough.
- **E-HAT-4.F-3 — proof correct.** π_j(hocolim) = colim π_j for a telescope (compactness of S^j,
  finite telescopes deformation retract on their last stage), and π_j(ΩZ_n) = π_{j+1}(Z_n), so both
  sides are colim_n π_{j+1}(Z_n) and κ_* is the identity on it.
# findings-4-G — SRC-TEXT-HAT02 §4.G (Gluing Constructions)

Cards in section: **4** (E-HAT-4.G-1 … 4). Book exercise block: AT.txt **line 22813**
("Exercises"), statements at **22815–22823**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.G-1 | **statement matches** (AT 22815–22817). | unread |
| E-HAT-4.G-2 | **statement matches** (AT 22818–22819). | unread |
| E-HAT-4.G-3 | **statement differs** — bracketed cross-reference dropped (defect 2). | unread |
| E-HAT-4.G-4 | **statement differs** — bracketed remark dropped (defect 1). | unread |

## Defects

1. **E-HAT-4.G-4: bracketed remark dropped.** Book, AT **22823**: "[CW complexes are paracompact; see
   [VBKT].]" The card gives the exercise with no indication of why the CW case holds.
2. **E-HAT-4.G-3: bracketed cross-reference dropped.** AT **22821**: "[See Lemma 2C.2.]"

## Census
4 cards; 2 differ. All 4 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT

- **E-HAT-4.G-1 — proof correct.** Successive deformation retractions M_n ↘ T_n, compatible in n,
  assemble on the union because the union is the colimit of the cofibrations M_n → M_{n+1}; the time-1
  map lands in ∪T_n and the telescope is fixed throughout.
- **E-HAT-4.G-2 — proof correct.** With all attaching maps homeomorphisms and Γ connected, all X_v,
  X_e are homeomorphic to one fiber F; over the interior of an edge p is X_e × (0,1) → (0,1); over the
  open star of a vertex, x ↦ f_{e,v}(x) identifies each half-edge product with X_v × [0,1/2), and the
  gluing at t = 0 is the identity. Local triviality over a basis of Γ gives a fiber bundle.
- **E-HAT-4.G-3 — proof correct.** st°(v_0) ∩ … ∩ st°(v_q) ≠ ∅ iff v_0,…,v_q span a simplex (a
  point of the interior of τ lies in st°(v) iff v is a vertex of τ), so the nerve is isomorphic to K.
  This is the answer Lemma 2C.2 is meant to suggest.
- **E-HAT-4.G-4 — proof correct in outline; one step asserted.** The diagram-of-intersections
  construction and the two reductions (p: ΔX_U → X a homotopy equivalence; then 4G.1 applied to the
  diagram of points) are the right ones and are what the exercise asks for. But "The homotopy gluing
  lemma therefore proves by cellular induction that p is a homotopy equivalence" is stated, not
  carried out: the card never verifies the induction (contractibility of the simplex of subcomplexes
  containing a given cell, compatibility on boundaries). The conclusion is true; the write-up leaves
  the induction to the reader.
# findings-4-H — SRC-TEXT-HAT02 §4.H (Eckmann–Hilton Duality)

Cards in section: **4** (E-HAT-4.H-1 … 4). Book exercise block: AT.txt **line 23110**
("Exercises"), statements at **23111–23121**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.H-1 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.H-2 | **statement differs** — the words "as at the right" are dropped, and the pushout diagram itself is not in AT.txt; the card also writes $B\cup_f X$ where AT 23114–23116 prints "B ⊔f X" (defects 2, 3). | unread |
| E-HAT-4.H-3 | **statement differs** — bracketed remark dropped (defect 4). | unread |
| E-HAT-4.H-4 | **statement matches** (AT 23120–23121). | unread |

## Defects (most serious first)

1. **E-HAT-4.H-1: bracketed hint dropped.** Book, AT **23112–23113**: "… the map Y X →Y A obtained by
   restriction of functions is a fibration. [If A ֓ X is a cofibration, so is A× Y ֓ X × Y for any
   space Y .]" The hint is the key step (it transports the cofibration to the product).
2. **E-HAT-4.H-2: reference to the printed diagram dropped.** Book, AT **23114–23115**: "Consider a
   pushout diagram as at the right, where B ⊔f X is B with X attached along A via f ." The diagram is a
   figure; the extraction (AT 23114–23116) carries none of it, so the card's paraphrase is unwitnessed
   as to the actual square printed. The card also silently drops "as at the right".
3. **E-HAT-4.H-2: symbol changed.** AT **23114–23116** prints "B ⊔f X" (the extraction's glyph for the
   pushout/attaching notation, consistent throughout AT.txt — 279 occurrences); the card prints
   `$B\cup_f X$`. Hatcher's attaching notation is ∪_f, and the extraction's ⊔ is an artefact of the
   OCR, but the card and the witness in this repository disagree on the symbol.
4. **E-HAT-4.H-3: bracketed remark dropped.** AT **23118–23119**: "[This is dual to Proposition 0.19.]"

## Census
4 cards; 3 differ. All 4 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.H-1 — proof correct.** Adjointing the data (f_0, g) of the lifting problem gives
  F_0: Z×X → Y and G: Z×I×A → Y; the hint's content ("if A ↪ X is a cofibration, so is
  A×Y ↪ X×Y") is exactly what makes Z×A ↪ Z×X a cofibration, so the partially defined map on
  (Z×X×{0}) ∪ (Z×A×I) extends; adjoint back. Note the card proves the hint instead of just citing it.
- **E-HAT-4.H-2 — proof correct.** Given (u, H) on B, put u_X = uq and h_A = H(f×id); HEP for
  A ↪ X extends to H_X, and the pushout universal property (P×I is the pushout of B×I and X×I over
  A×I) gives H̃ agreeing on the overlap because H(f(a),t) = H_X(i(a),t). Hence B ↪ B ⊔_f X is a
  cofibration.
- **E-HAT-4.H-3 — proof correct.** Adjust the ordinary inverse g to a fiber-preserving g' by lifting
  p_2fg ≃ p_2; the lemma (fiber-preserving u ≃ id over a fibration has a left homotopy inverse over B)
  is proved by lifting the base homotopy and a two-parameter square, and then ℓ = ag satisfies
  ℓf ≃_B id, and applying the same construction to ℓ gives m with mℓ ≃_B id, whence
  fℓ ≃_B mℓ ≃_B id. Both fiber homotopies are produced, so f is a fiber homotopy equivalence.
- **E-HAT-4.H-4 — proof correct.** The dual of M(f_1,…,f_n) is defined as tuples (φ_σ) with
  φ_σ: σ → X_{max σ} subject to φ_σ|_τ = f_{max σ,max τ} ∘ φ_τ; the conditions are closed and
  consistent, n = 1 gives the mapping path space E_{f_1}, and the passage to ∇X for a complex of
  spaces over Δ-complex Γ reverses the maps. As a definition-exercise the answer is coherent and the
  n = 1 check pins the variance.
# findings-4-I — SRC-TEXT-HAT02 §4.I (Stable Splittings of Spaces)

Cards in section: **3** (E-HAT-4.I-1 … 3). Book exercise block: AT.txt **line 23272**
("Exercises"), statements at **23273–23288**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.I-1 | **statement differs** — bracketed approach dropped (defect 1). | unread |
| E-HAT-4.I-2 | **statement differs** — final sentence dropped (defect 2). | unread |
| E-HAT-4.I-3 | **statement differs** — trailing clause dropped (defect 3). | unread |

## Defects (most serious first)

1. **E-HAT-4.I-1: bracketed approach dropped.** Book, AT **23274–23276**: "[One approach: Show the map
   Σr + Σq : ΣX →ΣA ∨ Σ(X/A) induces an isomorphism on homology, where r : X →A is the retraction and
   q : X →X/A is the quotient map.]"
2. **E-HAT-4.I-2: final sentence dropped.** Book, AT **23281–23282**: "Thus to determine stable
   splittings of K(Zn , 1) it suffices to do the case that n is a prime power, as in Proposition 4I.3."
   That sentence is the point of the exercise; the card keeps only the Künneth computation.
3. **E-HAT-4.I-3: trailing clause dropped.** Book, AT **23287–23288**: "… are chosen to have the
   minimum number of cells in each dimension, **as described in the remarks following the proof**."
   The dropped clause is the only pointer that fixes which cell structures count.

## Census
3 cards; 3 differ. All 3 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.I-1 — proof correct.** F = (j_A Σr) + (j_Q Σq): ΣX → ΣA ∨ Σ(X/A). Since r i = id, i_*
  splits, the LES of (X,A) breaks into split short exact sequences and (r_*,q_*) is an isomorphism;
  under the suspension isomorphism F_* is that map, so F is a homology isomorphism. Both sides are
  simply connected (suspensions of a connected complex), so the homology Whitehead theorem applies.
- **E-HAT-4.I-2 — proof correct.** Uses Σ(X×Y) ≃ ΣX ∨ ΣY ∨ Σ(X∧Y), which is Hatcher's Proposition
  4I.1 verbatim (AT 23143), plus K(G×H,1) ≃ K(G,1)×K(H,1). H̃_i(K(Z_m,1)) is Z_m in odd degrees and 0
  in positive even degrees, so every reduced homology group is m-torsion, likewise n-torsion, and for
  coprime m,n both ⊗ and Tor vanish by Bézout; the Künneth formula for X∧Y then gives H̃_*(X∧Y) = 0,
  and Σ(X∧Y), being simply connected with trivial reduced homology, is contractible.
- **E-HAT-4.I-3 — proof correct.** It follows the book's proof (AT 23225–23260): Xi is the telescope
  of the composite mi of the maps h_j = Σf − r^j·1, and the minimal cell model "a 0 cell and a k cell
  for each k congruent to 2i or 2i+1 mod 2p−2" is exactly AT 23258–23260. Cellular approximation gives
  a map of (2k+1)-skeleta, degreewise homology isomorphism plus vanishing above 2k+1 plus simple
  connectivity (no 1-cells) gives the homotopy equivalence. The phrase "dimension at least 2k" is
  safe: at dimension exactly 2k the (2k+1)-skeleton of ΣL is ΣL = Σ(L^{(2k)}).
# findings-4-K — SRC-TEXT-HAT02 §4.K (The Dold–Thom Theorem)

Cards in section: **6** (E-HAT-4.K-1 … 6). Book exercise block: AT.txt **line 24094**
("Exercises"), statements at **24095–24121**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.K-1 | **statement matches** (AT 24095–24096). | unread |
| E-HAT-4.K-2 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.K-3 | **statement matches** (AT 24102). | unread |
| E-HAT-4.K-4 | **statement matches** (AT 24104–24105). | unread |
| E-HAT-4.K-5 | **statement matches** (AT 24109–24118); the book's "non-pathconnected" is hyphenated in the card. | unread |
| E-HAT-4.K-6 | **statement matches** (AT 24119–24121). | unread |

## Defects

1. **E-HAT-4.K-2: bracketed hint dropped.** Book, AT **24099–24100**: "[Consider the cover of L by
   open stars of simplices and the cover of K by the preimages of these open stars.]" The hint is the
   only indication that a cover-based (nerve/Proposition 4G.2) argument is intended. Note the card also
   reproduces the book's own typo "contractible" correctly spelled; AT 24099 prints "contractible" with
   a line break, no issue.

## Census
6 cards; 1 differs. All 6 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT (read in full)

- **E-HAT-4.K-1 — proof correct.** Hypotheses as stated for Corollary 4K.2, restricted to
  subcomplexes; each f_J is a weak equivalence between CW complexes, hence (Whitehead) a homotopy
  equivalence; 4G.1 on the intersection diagrams plus the subcomplex-cover form of 4G.2 (Section 4.G
  exercise 4) give that f is a homotopy equivalence.
- **E-HAT-4.K-2 — proof correct.** Over the open-star covers, V_ρ (ρ spanned by the vertices) is
  contractible and U_ρ = f^{-1}(V_ρ) deformation retracts onto the contractible f^{-1}(x_ρ) — the
  barycentric-coordinate scaling is a legitimate retraction — so f: U_ρ → V_ρ is a weak equivalence
  and 4K.2 applies; simplicial complexes have CW type, so Whitehead upgrades to homotopy equivalence.
  The retraction is sketched rather than written out, but the construction given is the standard one.
- **E-HAT-4.K-3 — proof correct.** Monotone coordinates give a continuous bijection from the closed
  simplex-like region Q (compact) to SP_n(I) (Hausdorff), hence a homeomorphism, and
  (x) ↦ (y_0,…,y_n) = (x_1, x_2−x_1, …, 1−x_n) is an affine isomorphism onto Δ^n.
- **E-HAT-4.K-4 — proof correct.** Unoriented chords of S^1 ↔ (θ,s) with (θ,s) ~ (θ+π,−s), which is
  the Möbius band; |s| = 1 is the diagonal. The comparison with Example 4K.5 (n = 1: the unreduced
  suspension of RP^0 is an interval, and the mapping cone is the Möbius band) is consistent.
- **E-HAT-4.K-5 — proof correct in outline.** (i) ⇔ (ii) by comparing the exact sequences of
  (E,p^{-1}(b)) and (E_p,F_b); (iii) is the componentwise form. The extension of Lemma 4K.3 to
  non-path-connected bases is argued componentwise, with compactness handling (b). The five-lemma
  comparisons are invoked rather than written out, and the phrase "the corrected current hypothesis
  that every compact subset of B is contained in some B_n" is editorial residue in the statement of
  4K.3(b), but the mathematics is right.
- **E-HAT-4.K-6 — proof correct in outline.** Over a simplex p^{-1}(σ) is an iterated mapping
  cylinder, which collapses to X_{v_q}; fibers map to X_{v_q} by composites of edge maps, which are
  weak equivalences, so 4K.3(c) gives the quasifibration over each simplex and each face; the gluing
  over a finite subcomplex uses 4K.3(a) with collars; the passage to Γ uses 4K.3(b) and compactness.
# findings-4-L — SRC-TEXT-HAT02 §4.L (Steenrod Squares and Powers)

Cards in section: **5** (E-HAT-4.L-1 … 5). Book exercise block: AT.txt **line 25802**
("Exercises"), statements at **25803–25820**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-4.L-1 | **statement matches** (AT 25803–25804). | unread |
| E-HAT-4.L-2 | **statement matches** (AT 25805–25806). | unread |
| E-HAT-4.L-3 | **statement differs** — bracketed hint dropped (defect 1). | unread |
| E-HAT-4.L-4 | **statement differs** — bracketed hint dropped (defect 2). | unread |
| E-HAT-4.L-5 | **statement matches** (AT 25817–25820); the diagram the exercise refers to is a figure not in AT.txt, so "encoded in the following diagram" has no witness either way in the extraction. | unread |

## Defects (most serious first)

1. **E-HAT-4.L-3: bracketed hint dropped.** Book, AT **25809–25810**: "[The Gysin sequence can be used
   to determine the map on cohomology induced by the bundle projection HP5 →OP2 .]"
2. **E-HAT-4.L-4: bracketed hint dropped.** AT **25811–25813**: "[Compute the cohomology ring of the
   mapping cone of the projection S 23 →OP2 via Poincaré duality or the Thom isomorphism.]"

## Census
5 cards; 2 differ. All 5 carry `source-checked` / `solution-written` / `solution-reviewed`
(`gpt-5.6-sol`).

## PROOF AUDIT
All 5 proofs in this section are **unread** — only the statement layer was audited here.

## PROOF AUDIT

- **E-HAT-4.L-1 — proof correct.** Cohomology operations H^m(−;G) → H^n(−;H) are the classes in
  H^n(K(G,m);H). H^1(−;Z) ↔ H^n(S^1;Z), which vanishes for n > 1, so only u ↦ a·u survives;
  H^2(−;Z) ↔ H^n(CP^∞;Z) = Z for n = 2j, 0 for n odd, so the operations are u ↦ a·u^j;
  H^1(−;Z_p) ↔ H^n(K(Z_p,1);Z_p), which is Z_2[x] for p = 2 (giving u ↦ u^n in every degree) and
  Λ(x) ⊗ Z_p[y], y = βx, for odd p (giving (βu)^j in degree 2j and u(βu)^j in degree 2j+1). All
  three classifications are right, including the odd-prime Bockstein-generated basis.
- **E-HAT-4.L-2 — proof correct.** H̃^*(X;Z_2) ≅ H^*(S^1;Z_2) ⊗ H̃^*(CP^∞;Z_2), so H^3(X;Z_2) is
  spanned by u = a×x; the Cartan formula gives Sq^2(u) = a×Sq^2x = a×x^2 ≠ 0 because Sq^1a = a^2 = 0
  and Sq^2a = 0 by instability. In Y = S^3 × CP^∞ the degree-3 class is pr_1^*(ι_3) and
  Sq^2 of it vanishes because H^5(S^3;Z_2) = 0. Since the degree-3 group is one-dimensional on both
  sides, a homotopy equivalence would have to match these classes and their Sq^2's. Correct.
- **E-HAT-4.L-3 — proof correct.** The Gysin sequence for an S^4-bundle gives
  H^3(B) → H^8(B) → H^8(E) → H^4(B), and H^3(OP^2;Z_3) = H^4(OP^2;Z_3) = 0, so p^*y = x^2.
  P^1y = 0 because H^{12}(OP^2;Z_3) = 0, while P^1x = x^2 (restrict to CP^∞, where x = −u^2 and
  P^1(−u^2) = −2u^4 = u^4 = x^2 in Z_3) and hence P^1(x^2) = 2x^3 ≠ 0 by Cartan. Naturality gives
  0 = p^*(P^1y) = P^1(p^*y) = 2x^3, contradiction. The mod-3 arithmetic is right throughout
  (2 ≢ 0, −2 ≡ 1).
- **E-HAT-4.L-4 — proof unread** (only the opening Thom-isomorphism setup was read).
- **E-HAT-4.L-5 — proof unread.**
