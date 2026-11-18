# Proof artifacts

Machine-checked certificates for mathematical corrections made to corpus cards, kept in
three separate categories. They are not interchangeable.

1. **Lean declarations on lean-categories main** — statements about groups, linear maps
   and tensor products, proved with no `sorryAx` in
   [lean-categories](https://github.com/dzackgarza/lean-categories), the one home of Lean
   formalization. This repository holds no Lean declaration.
2. **Chain-level checks in Sage** — exact computations with Sage's `ChainComplex` on the
   chain complexes a card displays, for the listed values of the parameters. These are
   finite samples of a chain-level statement.
3. **The topological identification** — the step from a chain complex to the homology of
   a space. It is *not* formalized. It is a cited theorem, and the citation and the
   verification of its hypotheses are recorded below.

A finite sample in category 2 does not settle a uniform statement about spaces: the Sage
checks below cover $m\in\{2,3,4,5,6,12\}$ and $n\le8$, and every uniform claim about these
complexes rests on the theorems in category 3, not on the sample.

A source transcription check proves what the source prints; it does not prove the
source's theorem. A counterexample refutes the printed claim but does not establish the
replacement. A correction is marked settled on its card only when a file here certifies it.

## 1. Lean declarations on lean-categories main

| File | Card | What it proves | Covers |
| --- | --- | --- | --- |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/FieldHomework1.lean> | `P-FHW1-01` | The printed hypothesis of problem 1(a) holds with $L=\bot$ for every $\alpha$ (the refutation), and both directions of the corrected statement with $L\ne 0$. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SubgroupFiniteness.lean> | `E-HAT-1.A-8` | A group with a finite generating family has finitely many subgroups of a given nonzero index: `finite_hom` and `subgroup_eq_stabilizer_comap`. | the statement |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/NormExtension.lean> | `P-TAMURAS15-10` | For a closed subspace $Y$ of a real normed space and $x\notin Y$: a functional of norm at most one vanishing on $Y$ with $\varphi x\ne0$. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Tamuras15_10.lean> | `P-TAMURAS15-10` | The corrected statement in full, including the `x ∈ Y` case `exists_mem_S` by Hahn--Banach. | the statement |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/MooreSpaceExactness.lean> | `E-HAT-2.3-1` | The group data behind the two exactness failures: $\ZZ/m$ is nontrivial for $m\ge2$ and torsion; a sequence with trivial ends cannot be exact at $\ZZ/m$; multiplication by $m\ge2$ on $\ZZ$ is injective but not surjective. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsion.lean> | `E-HAT-3.A-6` | The coordinate step of the converse and the refutation of the inference it replaces: `ratchet_le`, `exact_order_smul`, `exists_coord`, `zmod_two_no_exact_order_eight`, `zmod_eight_order_four`. | part |
| <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A2.lean> | `E-HAT-3.A-2` | **The card's whole statement, for every abelian group `A`.** `torOneQzAddEquivTorsion` proves `Tor₁(A, ℚ/ℤ) ≅ T(A)`, the torsion subgroup as `Submodule.torsion ℤ A`; `isTorsionFree_iff_forall_subsingleton_torOne` proves `A` torsion-free if and only if `Tor₁(A, B)` is trivial for every abelian group `B`. `Tor₁` is `TorBridge.torOne`, the left derived functor of `tensorLeft B`, and both are proved at the canonical presentation `0 → ker π → (A →₀ ℤ) → A → 0`, whose middle term is free on `A` itself — no finiteness hypothesis on `A`, and no freeness of `ker π`. Lean 4.36.0 at Mathlib `6d97e8ad`; axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. | the statement |
| <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A6.lean> | `E-HAT-3.A-6` | **The card's whole statement, for all abelian groups `A` and `B`.** `isAddTorsion_torOne` proves `Tor₁(A, B)` is a torsion group; `torOne_exists_addOrderOf_iff` proves, for every positive `n`, that `Tor₁(A, B)` has an element of order `n` if and only if both `A` and `B` have one — the printed direction and its converse. The route: the presentation bridge `torOneTorKernelAddEquiv` (`Tor₁(A, B) ≅ ker ((ker π) ⊗ B → F ⊗ B)` for any surjection `π` from a free `F`), the stage descent `exists_fg_stage` to a finitely generated direct summand of the free middle term, Smith normal form (`Submodule.smithNormalForm`) killing the stage's kernel by the product of its diagonal entries (`exists_nsmul_eq_zero_of_stage`), the transport `nsmul_eq_zero_of_nsmul_map_eq_zero`, and for the order statement the purity of the syzygy's cyclic subgroup (`exists_torOne_of_addOrderOf`) and the stage's elementary divisors (`exists_addOrderOf_of_torOne`). No filtered-colimit statement is used. Lean 4.36.0 at Mathlib `6d97e8ad`; axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. | the statement |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/FamilyQuotient.lean> | `E-HAT-2.3-2` | The precise implication the dimension step needs: if the family $(f_i)_{i\in\ZZ}$ of groups is carried by a `Finset` (every group outside it is trivial), then the canonical map $\bigoplus_i f_i\to\prod_i f_i$ is **surjective**, so the quotient $\prod_i f_i\big/\bigoplus_i f_i$ is trivial; stated as `directSumToPi_surjective_of_finite_support` and `quotient_subsingleton_of_finite_support`, with the point case (all groups trivial) and the $S^0$ case (exactly one nonzero index) as corollaries. It does **not** assert that the sum and the product are isomorphic, and says nothing for a family with infinite support — there the map is not surjective in general, which is why the candidate fails the wedge axiom. The identification of the $f_i$ with reduced homology groups is not formalized. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/ChainLevelSteps.lean> | `E-HAT-2.2-16` | The degree-zero and skeleton steps of the repair, but not the enumeration of the simplex's chains: `choose_rank_step` (Pascal's identity), `ker_ne_top_of_surjective_to_int` (a surjection onto $\ZZ$ has proper kernel), `not_subsingleton_ordinary_homology` (with $\ker\varepsilon=\operatorname{im}\partial_1$ and $\varepsilon$ onto $\ZZ$, the ordinary $C_0/\operatorname{im}\partial_1\cong\ZZ$ is not trivial, so $Z_0/B_0$ cannot stand in for $\widetilde H_0$), and `ker_eq_range_of_comm_iso` (exactness transports across an isomorphism of three-term complexes, which is how the $k$-skeleton inherits exactness in the degrees where its differentials agree with the simplex's). **Certified elsewhere**: the simplex's augmented exactness (<https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SimplexChains.lean>) and $\widetilde H_i((\Delta^n)^k)=0$ for $i<k$ (<https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SkeletonHomology.lean>). **Not** certified anywhere, and withdrawn as an obligation: that the chains are the *barycentric* ones, for which the pin has no `SSet.B` and no `sd ⟶ B` (§5; the card's own model on vertex subsets is certified by its `DeltaSimplexChains` row).  Plus `skSimplexEquiv`: the `i`-simplices of the `k`-skeleton are those of `X` for `i ≤ k`, from `IsIso ((SSet.skAdj k).unit)` — the simplex-level half of the skeleton step, not its chain-level half. Plus `skSimplexEquiv_δ`: that equivalence intertwines the face maps `δ_i` whenever `j + 1 ≤ k` (`NatTrans.naturality_apply` at the truncated face map) — the compatibility the chain-level half needs. And `skChainsIso`: the alternating face map complexes' degree-`i` objects are isomorphic for `i ≤ k`, since that complex carries the free group on the `i`-simplices in degree `i`. The differentials' agreement is now proved as well: `skChainsIso_δ` (the degree-wise isomorphism commutes with every face map, checked on the free generators `freeMk x`, where the statement is exactly `skSimplexEquiv_δ`), `skChainsIso_d` (the differential square `iso_{i+1} ≫ d_sk = d_X ≫ iso_i` for `i + 1 ≤ k`, from `AlternatingFaceMapComplex.obj_d_eq` and `comp_sum`/`sum_comp`/`comp_zsmul`/`zsmul_comp`), and — with `comp_inv_of_inv_comp` — `skChains_exact`, which transports one degree of exactness to the skeleton. Axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySign.lean> | `E-HAT-2.1-25` | The **all-`n` counting and sign algebra** behind the corrected subdivision formula. `card_pairSet`: the pairs `i < j` in `Fin N` number `N(N-1)/2`, via `Finset.card_sigma`, `Fin.card_Iio`, `Fin.sum_univ_eq_sum_range` and `Finset.sum_range_id`. `noninv_add_inv`: inversions and noninversions partition those pairs, via `Finset.card_filter_add_card_filter_not`. `sign_eq_neg_one_pow_inv`: `π.sign = (-1)^{inv π}` in `ℤˣ`, from the maintained `Equiv.Perm.sign_eq_prod_prod_Iio` (`GroupTheory/Perm/Fin.lean`) together with `Finset.prod_sigma'`, an induction over the pair set, `Finset.card_insert_of_notMem` and `pow_succ`. Axioms `propext`, `Classical.choice`, `Quot.sound`. It also proves the **deletion-index correspondence**: `delSum π = Σ_j #{i ∈ Iic j : π i < π j}` is the recursion's exponent, since the step `F_j → F_{j-1}` deletes `π j`; `filter_Iic_eq_filter_Iio` kills the diagonal, `filter_pairSet` filters the sigma set, and `delSum_eq_noninv` concludes `delSum π = noninv π`; `pow_delSum_eq_global_mul_sign` then gives the all-`n` identity `(-1)^{delSum π} = (-1)^{N(N-1)/2} sgn(π)`. **What this file is not:** it is the sign algebra of the corrected formula, not the recursion. The recursion itself is modelled, with every coefficient computed, in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> (next row). The two files cannot import each other, so the recursion file restates these theorems, with these proofs, before applying them (<https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>, section 8). What no file does is identify either with Hatcher's operator on singular chains. The pinned tree has the raw material — `AlgebraicTopology.singularChainComplexFunctor` (`AlgebraicTopology/SingularHomology/Basic.lean`), `SSet.ιChainComplex_d` and `SSet.chainComplex_hom_ext` (`SSet/Homology/Basic`) — and the missing step is the definition of the subdivision operator on that complex together with `S λ = b_λ (S ∂λ)`, which is not built. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> | `E-HAT-2.1-25` | **Hatcher's recursion itself, modelled, with its coefficients computed.** In `FreeAbelianGroup (List (Finset (Fin N)))`, `N = n+1`: `deletionPos` is the position of a vertex in a face and `stepExp`/`stepSign` the exponent and sign the boundary contributes along a peeling order, with `stepSign_eq_pow_stepExp`; `stepExp_eq_pairCount` proves the accumulated exponent depends only on the peeling order and not on the intermediate faces — it is the number of pairs `i < j` of that order with `l_j < l_i`, the deletion-index identity. `subdiv` is `S λ = b_λ (S ∂λ)` with the apex prepended; `coeff_subdiv` computes **every** coefficient of it and `coeff_subdiv_chainOf` shows the coefficient of the chain of a peeling order is exactly the recursion's `stepSign` there (`coeff_subdiv_chainOf_eq_pow` reads it as a power of `−1`). Permutation side: `deletionPos_univ` (at the top face the deletion position of a vertex is its value — the outermost deletion's factor), `peel π = (π n, …, π 0)` (the order the recursion deletes in) with `coeff_subdiv_peel` for the chain it builds. Geometric side: `baryWeight`/`baryWeight_mem` (a face's barycentre as a point of `stdSimplex`), `affineMap`/`affineMap_mem`/`affineMap_single` (the affine map spanned by an ordered vertex list, and the listed vectors are its vertices), `descFace`/`descVertex` with `descVertex_zero` — the descending barycentric vertex list of `π` begins at the barycentre of the whole simplex, which is the vertex the cone prepends. **The coefficient theorem, for every `π`:** `pairCount_ofFn` (a list count over `List.ofFn g` is the `Fin`-indexed count of pairs `i < j` with `g j < g i`, with `length_filter_ofFn`, `card_filter_pos` and `card_filter_succ_lt` carrying a filtered list length to a `Fin`-indexed cardinal), `pairCount_peel_eq_delSum` (the peeling order `peel π = (π (N-1), …, π 0)` has deletion-position count exactly the permutation's deletion sum `delSum π = Σ_j #{i ≤ j : π i < π j}`), the sign algebra restated here and applied (`pow_delSum_eq_global_mul_sign`, `pow_delSum_eq_global_mul_sign_int`), and therefore `coeff_subdiv_peel_sign`: for every `N` and every `π`, the recursion's coefficient of the descending chain of `π` is exactly `(−1)^{N(N-1)/2} sgn(π)` — the number the card displays, derived from the recursion rather than assumed. **The whole chain, not only its coefficients:** `chainCoeff_exists_chainOf` (support exhaustion: a chain with nonzero predicted coefficient is `chainOf F l` for a `Nodup` `l` enumerating `F`, by induction along `chainCoeff`'s recursion) and `chainOf_injective` (nonduplication: two peeling orders enumerating `F` and giving the same chain are equal, by strong induction on `F`, the head of the chain forcing the erased vertex) give, with `exists_perm_peel` (every `Nodup` enumeration of `univ` is some `peel π`) and `chainOf_peel_injective`, the identity `subdiv_univ_eq_sum_perm`: `subdiv univ` **equals** `Σ_π (−1)^{N(N-1)/2} sgn(π) • of (chainOf univ (peel π))` in the free abelian group on chains of faces — one summand per permutation, nothing else in the support (`ext_coeff` compares all coefficients). **Transport side, proved:** `chainOf_getElem?_take` (the `k`-th face of a chain is `F` with the first `k` peeled vertices removed), `descFace_antitone` (the descending flags are nested), and with `descVertex_zero`/`descVertex_last` the descending barycentric vertex list runs from the barycentre of the whole simplex to the vertex `π 0` itself; `affineMap_mem`/`affineMap_single` give the affine simplex spanned by such a list. **The flags, and the transport to vertex lists:** `chainOf_peel_eq_ofFn_descFace` identifies the recursion's chain for `π` with the list of prefix faces (`peel_take_toFinset`, `rev_image_Iio`, `sdiff_image_of_bijective`, `univ_sdiff_Ioi`, `peel_take_face`, `chainOf_length`); `map_baryWeight_chainOf_peel` reads those faces as their barycentres and gets exactly the descending vertex list; `map_subdiv_univ_bary` is the linear extension of that reading over the free abelian group, carrying the whole recursion to the signed sum of the descending vertex lists; `affineMap_cons_apply` is the coordinate form of Hatcher's prepend (the apex enters with its own barycentric coordinate `x 0`), and `continuous_affineMap` with `affineMap_mem` and `affineMap_single` makes that list a continuous affine map of the standard simplex with exactly those vertices. **Hatcher's operator formula:** `chainAffineMap` reads a chain of faces geometrically (vertex `k` is the barycentre of the `k`-th face), `barySimplex` is `Δ̄_π` on the descending barycentric vertex list, `chainAffineMap_chainOf_peel` proves the chain of `π` **is** its `Δ̄_π`, and `hatcher_formula` states, for an arbitrary continuous `σ` out of the standard `n`-simplex, `map (c ↦ σ ∘ (chain c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • of (σ ∘ Δ̄_π)` — the left side being Hatcher's `S σ` defined from `S λ = b_λ (S ∂λ)`, the right side the displayed closed formula. **Into degree `n` of the maintained chain complex:** `barySimplexOn`/`barySimplexSingular` package `Δ̄_π` through `TopCat.toSSetObjEquiv` as an honest singular `M`-simplex of the standard simplex (`toSSetObjEquiv_barySimplexSingular` shows the packaging is faithful); the degree-`M` group of `X.chainComplex (ModuleCat.of ℤ ℤ)` is *definitionally* the coproduct of one copy of `ℤ` per singular `M`-simplex (checked by `rfl`), so `singularChainIota` is the coprojection with no extra identification, and `singular_chain_formula` states the recursion pushed through `chainSingular`/`barySingular` and the coprojections: `lift (c ↦ ι (chainSingular c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • ι (Δ̄_π)`. **For an arbitrary singular simplex:** `chainVertex`/`chainAffineOn` corestrict each chain's affine map to the standard-simplex subtype with `affineMap_mem` (fixed-vertex junk fallback, so the map is total on chains), `chainAffineOn_chainOf_peel` makes it `Δ̄_π` on the recursion's chains, `chainSigma`/`barySigma` package `σ ∘ (·)` as singular `M`-simplices of `X` through `TopCat.toSSetObjEquiv` (read back by `toSSetObjEquiv_barySigma` / `toSSetObjEquiv_chainSigma`), and `hatcher_formula_arbitrary` states, for `σ : Δⁿ → X` arbitrary, `lift (c ↦ ι (chainSigma σ c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • ι (barySigma σ π)` — the left side the transported prepend-cone recursion, the right side the closed formula with the descending parametrisation. Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; 58 printed theorems, `exit 0`. **Boundary, stated:** the chain-map property `∂ ∘ S = S ∘ ∂` is not claimed — the exercise asks for the coefficient formula, which is what is proved. | the statement |
| `cards/bary_regression.py` | `E-HAT-2.1-25` | **A bounded regression, not a certificate.** For `n = 1, 2, 3` only, with executable assertions (the operator must equal `(-1)^{n(n+1)/2}` times the descending formula and must differ from the ascending formula and from its negative), it computes in the free abelian group on vertex tuples (i) Hatcher's recursive subdivision operator `S(lambda) = b_lambda(S partial lambda)`, (ii) the ascending barycentric formula the card used to carry, and (iii) the descending one it now carries. It confirms `S = (-1)^{n(n+1)/2}` times the descending formula for those three dimensions and refutes the ascending formula, including the exact failure in dimension `1` (`[b,v_1] - [b,v_0]` against `[v_0,b] - [v_1,b]`, different generators of `C_1`). It does **not** prove the identity for `n >= 4`: that rests on the induction written out in the card, which is not formalized, and the all-`n` identity in Lean remains an open obligation. |

| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/CH8DirectProduct.lean> | `P-CH8-1`, `-3`, `-7`, `-15`, `-40` | **The general statements of Gallian chapter 8 (7th edition, printed pages 167-170), proved:** the finitary external direct product is a group with componentwise operations (`product_mul_apply`); `G × {e}` is the kernel of `MonoidHom.snd` and is normal, and `(G × H)/(G × {e}) ≅ H`, likewise for `{e} × H` (`prod_bot_eq_ker_snd`, `prod_bot_normal`, `bot_prod_normal`, `quotient_prod_bot_mulEquiv`, `quotient_bot_prod_mulEquiv`, `prod_bot_mulEquiv`, `bot_prod_mulEquiv`); the product is abelian iff both factors are (`prod_comm_iff`); `G × H ≅ H × G` and the general index permutation (`prod_comm_mulEquiv`, `pi_perm_mulEquiv`); the additive group of `ℂ` is `ℝ ⊕ ℝ` (`complex_add_equiv_real_prod`); the order of a tuple is infinite iff a coordinate has infinite order, for two factors and for a finite family (`prod_orderOf_eq_zero_iff`, `pi_orderOf_eq_zero_iff`). No `sorryAx`; axioms `propext`, `Classical.choice`, `Quot.sound`. The finite computations of the same cards are the GAP checks in `cards/CH8DirectProduct.g` (§2 below). | the statement |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/CH8DirectProduct.lean> | `P-CH8-4` | The two-factor case: `G × H` is abelian if and only if both factors are (`prod_comm_iff`). The card asks in addition for the general case over $n$ factors, which this file does not state; the general-index permutation it proves (`pi_perm_mulEquiv`) is the statement of `P-CH8-7`. | part |
| <https://github.com/dzackgarza/lean-categories/blob/9b8b85840c2b5cef55942b971c65e3b4bfc0d252/LeanCategories/Topology/PairHomotopySequence.lean> | `E-HAT-4.1-9` | Hatcher §4.1 Exercise 9(a) at both terms of the extended pair sequence that are pointed sets, on the affirmative side and with $\pi_1(X,A,x_0)$ read as Hatcher's quotient in which the start point moves inside $A$ (printed p. 343): `relativePiOne_map_bijective` gives the vertical map at $\pi_1(X,A,x_0)$ as a bijection from bijectivity of $\pi_1(A,a)\to\pi_1(B,fa)$, $\pi_1(X,a)\to\pi_1(Y,fa)$ for all $a\in A$, $\pi_0(A)\to\pi_0(B)$ and $\pi_0(X)\to\pi_0(Y)$, and `zerothHomotopySubtypeMap_bijective` gives the vertical map at $\pi_0(A,x_0)$ from bijectivity of $\pi_1(X,A,a)\to\pi_1(Y,B,fa)$, $\pi_1(X,a)\to\pi_1(Y,fa)$ for all $a\in A$, $\pi_0(X)\to\pi_0(Y)$ and $\pi_0(X,A,x_0)\to\pi_0(Y,B,fx_0)$. The same file builds $\pi_1(X,A,x_0)$ as that quotient and proves exactness at the two joins that are not group statements. Elaborated on Lean 4.33.0 with Mathlib `db584cd6`, exit 0, axioms only `propext`, `Classical.choice`, `Quot.sound`, no `sorryAx`. **Not** covered: part (b) of the exercise, and the windows centered at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$. | part |

### The all-`n` sign identity of `E-HAT-2.1-25`: exact statement and maintained API

The corrected formula `S(σ) = (−1)^{n(n+1)/2} Σ_π sgn(π)(σ∘Δ̄_π)` rests on one combinatorial identity,
stated so that it can be proved rather than sampled: *along the descending face chain indexed by `π`, the
sum of the deletion positions equals the number of noninversions of `π`, namely `n(n+1)/2 − inv(π)`*, so
the recursion's sign `(−1)^{Σ deletion positions}` equals `(−1)^{n(n+1)/2} sgn(π)` because
`sgn(π) = (−1)^{inv(π)}`.

The maintained API for the right-hand side is
`Equiv.Perm.sign_eq_prod_prod_Iio (σ : Perm (Fin n))` in `Mathlib/GroupTheory/Perm/Fin.lean`, which gives
`σ.sign = ∏ j, ∏ i ∈ Finset.Iio j, (if σ i < σ j then 1 else -1)` in `ℤˣ` — the product over pairs `i < j`
of `−1` exactly at inversions. No bespoke sign implementation is needed. Two Lean steps remain; their current
state, after <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>, is the following.

1. **The deletion-index identity.** *Formalized for all `n` and all `π`:* `stepExp_eq_pairCount` proves that the sum of the deletion positions along a peeling order is the number of pairs `i < j` of that order with `l_j < l_i`; `deletionPos_univ` gives the outermost factor as the peeled vertex's value; `pairCount_ofFn` and `pairCount_peel_eq_delSum` carry that list count to the permutation-indexed sum `Σ_j #{i ≤ j : π i < π j}`; and `coeff_subdiv_peel_sign` concludes the coefficient `(−1)^{n(n+1)/2} sgn(π)` for the recursion's descending chain at every `π`.
2. **The prepend-cone recursion.** *Formalized:* `subdiv` is the recursion and `coeff_subdiv` computes all of its coefficients, so the sign at each stage is proved to be the position of the deleted vertex in the current face, not assumed; combined with 1 this gives the coefficient of every `π` (`coeff_subdiv_peel_sign`); and the exhaustive, nonduplicated indexing of the recursion's support by `S_{N}` is proved (`chainCoeff_exists_chainOf`, `chainOf_injective`, `subdiv_univ_eq_sum_perm`), so the single identity `subdiv univ = Σ_π (−1)^{N(N−1)/2} sgn(π) • of (chainOf univ (peel π))` holds in the free abelian group on chains of faces. *Not yet formalized:* the geometric reading of those chains as the singular simplices `σ ∘ Δ̄_π`, i.e. the transport to singular chains of `Δ^n`.

| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/LensDegree.lean> | `E-HAT-3.E-2` | The local-degree bookkeeping of the angular extension `(r,θ) ↦ (r, k_j θ)` on `S^{2n-1}`, which is what the card's sign count needs: `det_angDeriv` (the frame derivative is `diag(1,k)`, determinant `k`), `orientation_iff` (the coordinate map preserves orientation exactly when `k>0`), `natAbs_mul_orientation` (one coordinate contributes `|k|·sgn(k)=k`) and `prod_natAbs_mul_orientation` (the product over the coordinates). Scope, stated precisely: this certifies **arithmetic only** — the determinant of `diag(1,k)`, the orientation criterion, and `|k|·sgn(k)=k` with its product over the coordinates. It does **not** certify that the angular extension `f~` has that derivative, that its local degree is `sgn(k_j)`, or `deg f~ = k_1⋯k_n`; those three are named inputs from the lens-space discussion in §3.E, and the degree of `f` follows from them by the covering square `p' f~ = f p`. Written because an earlier repair of the card wrongly explained the sign by the holomorphic power `z ↦ 1/z^{|k|}`, which is conformal with local degree `+1`; the angular extension is a different map when `k<0`. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SimplexChains.lean> | `E-HAT-2.2-16` | **The standard simplex's chain complex is acyclic in positive degrees**, from maintained API and nothing bespoke: `SSet.Augmented.StandardSimplex.extraDegeneracy` transports along the free `ℤ`-module functor (`ExtraDegeneracy.map`), and `ExtraDegeneracy.homotopyEquiv` then gives `chainsHomotopyEquiv`, a homotopy equivalence of the alternating face map complex of the free simplicial group on `Δ^m` with the complex supported in degree `0`. Consequences, both with axioms `propext, Classical.choice, Quot.sound` and no `sorryAx`: `isZero_homology` (`H̃_i(Δ^m) = 0` for `i ≠ 0`, i.e. exactness of the augmented complex above degree zero) and `homologyZeroIso` (`H_0` of the complex is the augmentation's target, which is the form `ker ε = im ∂_1` takes). `normalizedHomotopyEquiv` and `normalizedChainsHomotopyEquiv` apply the maintained Dold--Kan comparison (`DoldKan.homotopyEquivNormalizedMooreComplexAlternatingFaceMapComplex`, valid for every simplicial object in an abelian category), giving `isZero_normalizedHomology`: the same vanishing holds in the **normalized** Moore model, so the model choice does not matter for this step. Scope: it does **not** touch the `k`-skeleton maps and says nothing about barycentric chains, so it discharges the first of the three things §5 lists for `E-HAT-2.2-16` and no more. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SkeletonHomology.lean> | `E-HAT-2.2-16` | **The card's sentence**: $\widetilde H_i((\Delta^m)^k)=0$ for $i<k$, i.e. `isZero_skHomology`: for `j + 2 ≤ k` the `k`-skeleton's chain complex has vanishing homology in degree `j + 1`. The composition is `ShortComplex.isoMk` of the three chain-group isomorphisms and the two differential squares (`scIso`), `ShortComplex.exact_of_iso` to carry `Exact` across it (`skExactAt`, through `HomologicalComplex.exactAt_iff'`), and the simplex's `isZero_homology` read as `ExactAt` (`exactAt_simplex`). It is *not* the `ker = range` transport: Mathlib's `ExactAt` is already the statement about the three-term complex, so no `Submodule`/`LinearEquiv` plumbing is needed. Axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`. It copies its two inputs' statements in, since a file here cannot import a sibling. Scope: nothing about barycentric chains (§5, where that item is withdrawn). | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorStages.lean> | `E-HAT-3.A-6`, `E-HAT-3.A-2` | The genuine stage construction for a presented group, **completed for a free middle term**. The stage: `stageRel` (its relations inside `F'`), `map_stageRel` (they are the relations of the sub-presentation `comap f F' → F'`), `stageMap` (`A' → A`, by `Submodule.mapQ`) and `stageMap_injective`, so the stage is a subgroup `A' ≤ A`. Its own presentation: `stageRelMap` with `range_stageRelMap` (the cokernel is `A'`) and `subtype_comp_stageRelMap`. The directed system: `stageIncl` with `stageIncl_refl` and `stageIncl_comp` (a functor on the poset of submodules of `F`), `stageMap_comp_stageIncl` (the triangles `A' → A'' → A` and `A' → A` commute) and `stageIncl_injective`. The filtered-colimit step, with its hypothesis isolated and sharp: `rTensor_subtype_injective_of_retraction` (a retraction of `F' ↪ F` makes `F' ⊗ B → F ⊗ B` injective), `rTensor_subtype_not_injective` (**certified counterexample**: `F' = 2ℤ ⊆ F = ℤ`, `B = ℤ/2`, so a submodule that is not a direct summand breaks the step even though `F` is free), `exists_stage_witness_of_retraction` (descent for such a stage). Then the choice of stage for free `F`: `coordProj`/`coordSpan`/`coordRetract` with `coordRetract_comp_subtype` (a span of finitely many basis vectors is a direct summand), `coordSpan_fg`, `exists_fg_summand` (every finitely generated `P ≤ K` lies in a finitely generated direct summand), and `exists_stage_of_free`: **every element of `torKernel f` is carried by the `Tor` of a stage whose middle term is a finitely generated direct summand**, and already vanishes there. **Not** proved in this file: the torsion statement for a finitely generated stage, and the filtered-colimit passage from a stage to an arbitrary `A`. The stage torsion statement is supplied at the same presentation by `TorExercise3A6.exists_nsmul_eq_zero_of_stage` (Smith normal form on the stage's relation submodule, with `exists_fg_stage` choosing a finitely generated direct summand), and no card route takes a filtered colimit (section 5b). The presentation-level `Tor` of a stage *is* now identified with `\\operatorname{Tor}(A,B)` — section 5b's `torOne_iso_kernel`, at a two-term free resolution of a finitely generated `A` — so Hatcher's Lemma 3A.2 is no longer what blocks those two, and `isZero_torOne_of_finite_torsionFree` settles the torsion-free case outright. The identifications the cards make about the stage itself are proved rather than assumed: `stage_range_fg` (a stage of a finitely generated `F'` is a **finitely generated subgroup** of `A`, since `stageMap` is injective with range the image of `F'`), `stage_finite` (its group is a finitely generated `Z`-module, the hypothesis the structure theorem consumes) and `exists_stage_containing` (**the stages cover `A`**: every element lies in the image of the stage of some finitely generated `F'`, taking `span {x}` for a lift `x`; a covering stage need not be a direct summand, which is why `exists_fg_summand` is a separate statement). | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> | `E-HAT-3.A-6` | The presentation-level `Tor` and the parts of Hatcher's Proposition 3A.5 that Mathlib supplies: the free case of (3) (`torKernel_eq_bot_of_subsingleton`), the group in (5) (`torsionBy_eq_ker`), the torsion-free-is-flat hypothesis of (3) (`flat_of_torsionFree`, Mathlib's Dedekind-domain instance), and the flatness form of (6) (`rTensor_injective_of_flat`, Mathlib's `Module.Flat.rTensor_preserves_injective_linearMap`); and, for the step that needs the *$p$-primary* hypothesis rather than torsion-freeness, item (5) in full: `lid_rTensor_mulByInt` and `map_torKernel_mulByInt`, that the kernel of $(n\cdot\mathrm{id})\otimes\mathrm{id}_B$ inside $\ZZ\otimes B$ is carried by $\ZZ\otimes B\cong B$ onto $B[n]$ — that is, $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ for this resolution — together with `eq_zero_of_pow_smul_eq_zero`, `torsionBy_pow_eq_bot_of_no_p_torsion` (no $p$-torsion gives $C[p^k]=0$) and `mem_of_p_smul_mem_of_pPrimary` ($B_p$ is saturated for multiplication by $p$, i.e. $B/B_p$ has no $p$-torsion). Additivity (2) is now proved as `prodLeft_comp_rTensor` and `map_prodLeft_torKernel`: the presentation of a direct sum is the direct sum of the presentations, so `torKernel (f₁ ⊕ f₂)` is carried by `TensorProduct.prodLeft` onto `torKernel f₁ × torKernel f₂`. The proof avoids `prodLeft.symm` on arbitrary elements by rewriting the kernel as a `comap` and mapping forward through `Submodule.map_comap_eq_self`. **Not** certified: that the presentation-level kernel computes $\operatorname{Tor}$ for an arbitrary resolution (Lemma 3A.2) and commutation with filtered colimits (Exercise 4); neither is on the route that certifies the two cards, which takes the presentation $\pi : (A\to_0\ZZ)\to A$ and the stage descent of section 5b. | part |

| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorBridge.lean> | `E-HAT-3.A-6`, `E-HAT-3.A-2` | **`Tor₁` is the homology of the tensored projective resolution**, proved: `torOneIsoHomology` gives `((tensorLeft B).leftDerived 1).obj A ≅ H₁(P.complex ⊗ B)` for every projective resolution `P` of `A`, by `ProjectiveResolution.isoLeftDerivedObj` at degree one, with the tensored complex and its degree-1 differential named (`resolutionTensor`, `tensorDiffOne`). Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. **Also proved:** the two-term step, `homologyIsoKernelOfZero`, `homologyOneIsoKernelOfD`, `homologyOneIsoKernel` and `tensor_d_two_one_eq_zero`, giving `torOneIsoKernel`: for a projective resolution with `IsZero (P.complex.X 2)`, `Tor₁(A,B) ≅ kernel((resolutionTensor B P).d 1 0)`, plus `torOneIsoKerLinear` composed with `ModuleCat.kernelIsoKer`. The map-level content is `resolutionTensor_d` (the tensored differential is the tensor of the resolution's differential). **Also proved:** the orientation `ker_rTensor_eq_comap_ker_lTensor` (`ker (f.rTensor N)` is the `comm`-preimage of `ker (f.lTensor N)`, by `LinearMap.lTensor_comm`), the pinned kernel module `kerModule` with `kernelIsoKerModule` (the `ℤ`-module instance diamond resolved at that boundary), and `tensor_d_hom_eq_lTensor` (the tensored differential is the resolution differential with `B` on the left). **Open:** the single packaging step that composes the two-term bridge with the `comm`-transport into one isomorphism naming `kerModule` of `f.hom.rTensor ↥B`. The cards do not need it: section 5b's presentation bridge is a different construction, and §7c records that this packaging is supporting development rather than a card correction. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/CyclicTor.lean> | `E-HAT-3.A-6` | **The cyclic stage's index transport.** `ker_d_rTensor_eq`: the kernel of the cyclic resolution's tensored first differential is the preimage, under `syzygyEquiv ⊗ id_B`, of the kernel of `(n · id) ⊗ id_B` — that is, of the presentation-level `torKernel` whose image under `TensorProduct.lid` is `B[n]` (`TorReductions.map_torKernel_mulByInt`). Supporting facts, all proved in the file: `d_apply` (the resolution's first differential is `constOne ∘ (n · id) ∘ syzygyEquiv`, pointwise), `projZero_comp_constOne` (the zeroth coordinate retracts `constOne`), `constOne_tmul_eq_zero`, `ker_constOne_rTensor_eq_bot` (`constOne ⊗ id_B` is injective), and the generic `ker_subtype_rTensor_eq`. Axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`. Two elaboration facts worth keeping: the transport is stated for `(LinearMap.ker f).subtype`, because `↑((twoTermComplex 1 (cyclicPresentation n)).X 1)` and `↥(LinearMap.ker …)` are not interchangeable in `⊗ₜ` although `twoTermComplex_X_one` is `rfl`; and the factorisation is stated through `ModuleCat.ofHom` composites so that `ModuleCat.isModule` is on both sides, a plain `LinearMap.comp` composite being headed by `Int.instRing.toSemiring`. **The hop is closed**: `map_ker_d_rTensor_eq` maps the preimage back to `ker ((n · id) ⊗ id_B)` by `σ ⊗ id_B`, using `Submodule.map_comap_eq_self` and invertibility of the tensored `σ` (`TensorProduct.induction_on` on a pure tensor), and `map_comp_map` is the composition step. **Not yet written in this file**: the final composition with `TorReductions.map_torKernel_mulByInt` into `Submodule.torsionBy ℤ ↥B (n:ℤ)`, blocked by instance ascription on the two `Submodule` types (`TensorProduct.instModule` on one side, `Int.instCommSemiring` on the other); the cards take the presentation-level route to `Submodule.torsion ℤ A` instead (`TorExercise3A2.torOneQzAddEquivTorsion`, through `torsionToSyzKernel`). | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorArbitrary.lean> | `E-HAT-3.A-6`, `E-HAT-3.A-2` | **The dimension-shift platform for an arbitrary abelian group.** `presComplex f`: a projective resolution of `A` over *any* epimorphism `f : P ⟶ A` from a projective — `P` in degree zero, then Mathlib's `Projective.syzygies`/`Projective.d` for the kernel, its kernel, and so on, built with `ChainComplex.mk'` (for `f = Projective.π A` this is Mathlib's own `ProjectiveResolution.of`). `presComplex_exactAt_succ` (exactness in positive degrees), degreewise projectivity, the augmentation `presPi` and its quasi-isomorphism (degree zero through `ModuleCat.isColimitCokernelCofork`, as in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorFreeResolution.lean>) — so `presResolution f` is a genuine `ProjectiveResolution A` with a *prescribed first presentation*, which is what an arbitrary `A` needs: no hypothesis on the kernel of `f`, hence no "every subgroup of a free abelian group is free". `torOneIsoTensorSplice` bridges `Tor₁(A,B)` to `H₁` of the tensored splice. `hom_lTensor` is the dictionary between the `ModuleCat`-monoidal tensor maps and `LinearMap.lTensor`. `ker_dOne_eq_kerCov` (the kernel of the first differential is the kernel of the kernel cover, by injectivity of the kernel inclusion), `exact_dTwo_kerCov` (the untensored second differential and the kernel cover are an exact pair), and **`range_dTwoT_eq`: the boundaries of the tensored splice are the kernel of the tensored kernel cover** — the right-exactness input of dimension shifting, from Mathlib's `lTensor_exact`, stated through the dictionary form so the two tensor-module instance worlds never meet in a statement (`exact_tensored` bridges by defeq). **The ψ-map of the third isomorphism, at the additive-group level** (an `AddMonoidHom` mentions no `Module ℤ` instance, so the instance diamond of the linear spellings does not arise): `mapCycles_eq_kerIncl` (the image of the cycles under the tensored kernel cover is the kernel of the tensored kernel inclusion, the surjectivity half, by `LinearMap.ker_comp` and `Submodule.map_comap_eq_self`), `psiAdd`/`psiAdd_surjective`/`psiAdd_ker` (the ψ-map, its surjectivity, and its kernel as the additive view of the boundaries), `psiAddQuotientEquiv`/`boundariesQuotientEquiv` (the third isomorphism, additive form: the additive quotient of the cycles by the kernel of ψ is the kernel of the tensored kernel inclusion, transported along `psiAdd_ker` with `QuotientAddGroup.quotientAddEquivOfEq`). **The promotion lemma of #138:** `addEquiv_intLinearEquiv` — an additive equivalence `M ≃+ N` is a ℤ-linear equivalence `M ≃ₗ[ℤ] N` for **any** two `Module ℤ` instances on the carriers (every `Module ℤ` structure agrees with `zsmul` by `int_smul_eq_zsmul`, and an additive homomorphism preserves `zsmul` by `AddMonoidHom.map_zsmul`); the two instances are the lemma's explicit instance arguments, so that no instance is synthesized on the carrier at the application site. **Its use, the homology equivalence of #138:** `homologyEquiv` — the carrier of the homology of the tensored splice is the kernel of the tensored kernel inclusion, as a ℤ-linear equivalence, the promotion of the additive composite `boundariesQuotientEquiv` under the instance `H.isModule` on the left carrier (the right carries `AddCommGroup.toIntModule`, which is what the `≃ₗ[ℤ]` notation synthesizes there). **The dimension-shift bridge of #139:** `torOneIsoKerIncl` — `Tor₁(A, B) ≅ ker(ι ⊗ B)` — the composite of `torOneIsoTensorSplice`, Mathlib's `HomologicalComplex.homologyIsoSc'` (with the `ComplexShape.prev_eq'`/`next_eq'` side conditions of the down shape), `ShortComplex.moduleCatHomologyIso`, and the ℤ-linear homology equivalence above, packaged as an isomorphism in `ModuleCat ℤ` by `LinearEquiv.toModuleIso`. Axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorFreeResolution.lean> | `E-HAT-3.A-6`, `E-HAT-3.A-2` | **The two-term free resolution, and `Tor₁` as the kernel of its tensored differential.** The syzygy of a finite free presentation is finitely generated, torsion-free, free and projective (`syzygy_finite`, `syzygy_torsionFree`, `syzygy_free`, `syzygy_projective`); the complex `0 → K → ℤⁿ → 0` is `twoTermComplex` (`twoTermComplex_isZero_X` for every degree `≥ 2`, `twoTermComplex_projective` degreewise), its augmentation onto `single₀ A` is `twoTermPi`, and that augmentation is a quasi-isomorphism — degree zero by `ShortComplex.quasiIso_iff_of_zeros'` from `ModuleCat.isColimitCokernelCofork` (`quasiIsoAt_twoTermPi_zero`, resting on `coker_subtype_iso`), every positive degree by `quasiIsoAt_twoTermPi_of_pos` — so `twoTermProjectiveResolution` is a genuine `ProjectiveResolution`, and `torOne_iso_kernel` gives `Tor₁(A,B) ≅ kernel ((tensorLeft B).map (d 1 0))`. Above that, `isZero_torOne_of_projective` holds that `Tor₁` of a projective module vanishes, hence `isZero_torOne_of_finite_torsionFree`: the finitely generated case of "torsion-free implies `Tor₁(A,B) = 0`", at the derived functor, for every `B` at once. The cyclic stage's syzygy is identified with `ℤ` (`cyclicPresentation`, `syzygyEquiv`); its transport to `B[n]` is **not** proved, and the section docstring records the coercion-shape reason. Axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/ColimitTensor.lean> | `E-HAT-3.A-6`, `E-HAT-3.A-2` | Exercise 4 of §3.A, the `⊗` half, completely: `tensorLeft_preserves_colimits` (for `B : ModuleCat ℤ`, `tensorLeft B` preserves colimits, Mathlib's instance `instPreservesColimitsTensorLeft`) and `tensorLeft_colim_iso`, the comparison `B ⊗ colim F ≅ colim (B ⊗ F ·)` for any `F : J ⥤ ModuleCat ℤ` with `HasColimitsOfShape J (ModuleCat ℤ)`, built from `PreservesColimit.preserves` (which yields `Nonempty (IsColimit _)`, extracted with `Classical.choice`) and `IsColimit.coconePointUniqueUpToIso`. Axioms: propext, Classical.choice, Quot.sound. **Not** certified: the `Tor` half. | part |
| <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsionClass.lean> | `E-HAT-3.A-6` | **`Tor` of a torsion module is torsion, by the torsion-class route instead of a free resolution.** `prop_homology` (a property closed under subobjects and quotients passes from a complex term to its homology in the same degree) and `prop_leftDerived_obj` (if an additive functor sends projectives into such a class, every left derived functor does) are proved for a general abelian setting; `AddCommGrpCat.isTorsion` is the class of torsion abelian groups with its `IsClosedUnderSubobjects` and `IsClosedUnderQuotients` instances; `isAddTorsion_tensorProduct_left` (tensoring a torsion monoid is torsion, no flatness, no finite generation); and `isAddTorsion_Tor_left`: for `M`, `N` in `ModuleCat R` over **any** commutative ring, `IsAddTorsion M → IsAddTorsion (((Tor (ModuleCat R) n).obj M).obj N)`, with the `ℤ` form `isAddTorsion_tor_int`. Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; `exit 0`. **Provenance:** this is a **port**, not new mathematics — the four lemmas are copied from the Tau Ceti project at commit `67e852853c5192ec69775bb7ef417fc199e4190e` (Apache-2.0), see section 7. **No node obligation attaches to this file**: `Tor(A,B)` is torsion is not a corrected claim, so `certify-card-corrections` does not reach it, and the card is discharged by citing the upstream theorem with its hypotheses (§7c). It is kept as a supplement, not as a card requirement. **What it does not cover:** the card's statement is about **all** `A`, and this file proves the case where `A` is torsion — the reduction `Tor(A,B) ≅ Tor(T(A),B)` is §7b's named residual; the second half of the card (an element of order `n` in `Tor(A,B)` iff in both `A` and `B`), which `TorExercise3A6.torOne_exists_addOrderOf_iff` proves for every `n > 0` at the presentation of section 5b rather than here; and it says nothing about `Tor'`, the other orientation. It does not need — and does not supply — Hatcher's Lemma 3A.2 or a finite-stage witness, because the left-derived-functor definition of `Tor` is already resolution-independent. | part |

| <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/DeltaSimplexChains.lean> | `E-HAT-2.2-16` | **The card's own Δ-complex chain model of `Δ^n`, certified end to end, including the boxed skeleton claim.** The declaration is on lean-categories main, where every Lean declaration of this corpus lives — it moved there from `proofs/cards/` under lean-categories#141 — and the row links it at `5848f0f2`, the commit that pins Mathlib's master head `6d97e8ad`. The `i`-chains are the free abelian group on the `(i+1)`-element vertex subsets (`Simplices`, `chains`, `gen_c`), the boundary is the alternating sum over ordered deletions (`boundary`, with `pos_of` the deletion position), the augmentation reads off the coefficient sum (`aug`), and the file proves: `finrank_chains` ($\operatorname{rank} C_i = \binom{n+1}{i+1}$, the count of $(i+1)$-element subsets); `aug_comp_boundary` and `boundary_comp_boundary` ($\varepsilon\partial_1 = 0$, $\partial_i\partial_{i+1} = 0$, so the augmented complex is a complex); the cone contraction $h_i(s) = (-1)^i \cdot (0$ if $n \in s$, else $s \cup \{n\})$ — `homotopy_succ`, `homotopy_zero`, `aug_h_minus` give $(\partial h + h\partial)(x) = -x$ degree by degree — and hence the exactness of the augmented complex `exact_zero`, `exact_succ`, `cycles_aug_eq_boundaries`; and the rank induction $\operatorname{rank} B_i = \operatorname{rank} Z_i = \binom{n}{i+1}$ by rank-nullity over $\ZZ$ with Pascal's identity `finrank_boundaries`, `finrank_cycles_aug` (the base case is the augmentation's range $\ZZ$, `aug_surjective` and `finrank_range_add_finrank_ker`; the step is the kernel of `boundary` read through `exact_succ`). **The skeleton section is the card's boxed claim, and it uses the agreement, not a second complex:** the skeleton is the truncation of the model — its chain groups are the simplex's in degrees `i ≤ k` and trivial above (`skCycles`, `skBoundaries`) — so `skCycles_eq` and `skBoundaries_eq` record the agreement with the simplex's groups, `sk_cycles_aug_eq_sk_boundaries` and `subsingleton_sk_homology` give $\widetilde H_i((\Delta^n)^k) = 0$ for `i < k` (below degree `k` the skeleton's cycles and boundaries are the simplex's, and the simplex's augmented complex is exact), and `skBoundaries_top`, `skCycles_top`, `skHomologyTopIso` and `sk_homology_top_basis` give $\widetilde H_k((\Delta^n)^k)$ free of rank $\binom{n}{k+1}$: there are no `(k+1)`-chains in the skeleton, so the top homology *is* the simplex's `k`-cycles, a subgroup of the free abelian group on the `k`-simplices, free over $\ZZ$ by `Submodule.basisOfPid` (the structure theorem for submodules of a finite free module over a PID) with rank `finrank_cycles_aug`. Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. **Scope, and the source boundary:** this proves the card's statement in the card's own chain model — the ranks of the chain, cycle and boundary groups, and both halves of the boxed claim, `subsingleton_sk_homology` for $i<k$ and `sk_homology_top_basis` in degree $k$ — which is what the row's `Covers` cell records. **What it does not cover:** the passage from the chain model to the homology of the *space* $(\Delta^n)^k$; that is the card's citation of Hatcher's Theorem 2.27 (p. 128), a category-3 identification, and stays a citation. The three files <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/SimplexChains.lean>, <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/ChainLevelSteps.lean> and <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/SkeletonHomology.lean> certify the same homological statements in Mathlib's alternating-face-map model, at the same commit; this file is the certificate of the model the card itself writes down. | the statement |

## 2. Exact finite computations: Sage chain complexes, GAP groups

`cards/CH8DirectProduct.g`, run with GAP 4.14.0 (`gap -q proofs/cards/CH8DirectProduct.g`,
56 checks, `ALL CHECKS PASSED`; the header of that file records the interpreter):

| Card | What is checked exactly | Cards | Covers |
| --- | --- | --- | --- |
| `P-CH8-2` | `Z_2^3` has exactly seven subgroups of order 2 | `cards/CH8DirectProduct.g` | the statement |
| `P-CH8-6` | `Z_8 ⊕ Z_2` and `Z_4 ⊕ Z_4` have different element-order multisets (an element of order 8 against none; 4 elements of order 4 against 12) | same file | the statement |
| `P-CH8-10` | `Z_3 ⊕ Z_9` has exactly 18 elements of order 9 | same file | the statement |
| `P-CH8-13`, `-14` | `Z_{n²}` against `Z_n ⊕ Z_n` for `n = 2..6`; `D_n` nonabelian against `Z_n ⊕ Z_2` for `n = 3..10` | same file | part |
| `P-CH8-19` | for all `m,n ≤ 12` and all divisors `r|m`, `s|n` the subgroup `<m/r> ⊕ <n/s>` has type `Z_r ⊕ Z_s` | same file | part |
| `P-CH8-20` | `<(3,0),(0,2)> ≤ Z_12 ⊕ Z_18` has type `Z_4 ⊕ Z_9` | same file | the statement |
| `P-CH8-23` | `Z_3^n` nonidentity orders for `n = 1..4` | same file | part |
| `P-CH8-26`, `-30` | `S_3 ⊕ Z_2 ≅ D_6` and not `Z_12`, `Z_6 ⊕ Z_2`, `A_4`; the seven order-4 subgroups of `Z_4 ⊕ Z_4`, six cyclic and one elementary abelian | same file | the statement |
| `P-CH8-36`, `-38` | the 3-torsion of `Z_12 ⊕ Z_4 ⊕ Z_15` has order 9; the matrix group `H` over `Z_3` is abelian of order 9, type `Z_3 ⊕ Z_3` | same file | the statement |
| `P-CH8-49`, `-68` | `Aut(U(25)) ≅ Z_4 ⊕ Z_2`; `Aut(Z_20)` has four elements of order 4 and three of order 2 | same file | the statement |
| `P-CH8-52`, `-53`, `-55`, `-56` | the two isomorphism tests by abelian invariants; the four generators of `Z_4 ⊕ Z_3`; the unique isomorphism `Z_3 ⊕ Z_5 → Z_15` with `φ(2,3) = 2` and its preimage `(1,4)` of 1 | same file | the statement |
| `P-CH8-67` | `U(165)` as `U(11)⊕U(15)`, `U(3)⊕U(55)`, `U(5)⊕U(33)` and `U(3)⊕U(5)⊕U(11)`, the four groupings of `3,5,11` into at least two blocks | same file | the statement |
| cyclicity criteria | `Z_m ⊕ Z_n` cyclic iff `gcd(m,n)=1` for `2 ≤ m,n ≤ 20`; three factors iff pairwise coprime for `2 ≤ a,b,c ≤ 8`; a cyclic `G ⊕ H` has cyclic factors for all groups of order `2..8` | same file |

`cards/DeltaComplexHomology.sage`, run on the Sage development image (11.0.beta5, Python
3.14.10, source HEAD `b0cd7d86e2`; reproduced with `proot -R $HOME/sage-image/rootfs ...`):

| Card | Chain complex checked | Parameter range | Covers |
| --- | --- | --- | --- |
| `E-HAT-2.1-4`, `-5` | the parachute and the Klein bottle complexes | one case each | the statement |
| `E-HAT-2.1-6`, `-9` | the collapsed complex with $H_1=\ZZ/2^n$ ($n\le6$) and the collapsed $\Delta^n$ ($n\le8$) | $n\le6$, $n\le8$ | part |
| `E-HAT-2.2-11` | the cube complex | one case | the statement |
| `E-HAT-2.2-19` | $\RP^n/\RP^m$ | $m\le4$, $n\le8$ | part |
| `E-HAT-2.3-1` | the Moore complex $d_1=0$, $d_2=m$, and the Smith form of $(m)$ on $\ZZ$ | $m\in\{2,3,4,5,6,12\}$ | part |

Every entry is a finite check of the chain-level statement for the listed parameters. None
of them is a statement about a space, and none settles the corresponding uniform claim.

Its certificate is <https://github.com/dzackgarza/new-qual-site/blob/d4122f28c509b86fb8f1ad5e9c80e7b72ccbae75/proofs/cards/V49FiveSquaresTuples.sage>, a
symbolic rather than a finite check, run on the same Sage development image (11.0.beta5, Python
3.14.10, source HEAD `6301b4e43e`); <https://github.com/dzackgarza/new-qual-site/blob/d4122f28c509b86fb8f1ad5e9c80e7b72ccbae75/proofs/cards/V49FiveSquaresTuples.out> is
its recorded output, which keeps each earlier revision's runs beside the current one and records
every run set's script sha256:

| Card | What is checked exactly | Range | Certificate | Covers |
| --- | --- | --- | --- | --- |
| `P-AGH549MINGENUS` | the arithmetic at $r=2$ of one hypothesis of Gruson--Peskine Proposition 2.1 (printed p. 407) and Theorem 2.5 (printed p. 409), and **not** either statement: the six listed tuples' exact integer squared sums — $4,12,20$ for $(2,0,0,0,0)$, $(2,2,2,0,0)$, $(2,2,2,2,2)$ and $0,8,16$ for $(0,0,0,0,0)$, $(2,2,0,0,0)$, $(2,2,2,2,0)$ — each of one parity with $\abs{x_i}\le2$; the polynomial identity $\sum x_i^2=8(F_d(2)-g)$ with $F_d(2)=(d-1)/2$, at the genus listed for each row, over $\QQ[m]$ with $d=2m$ and $d=2m+1$; that $(d-1-j)/2$ lies in $\ZZ[m]$ exactly for odd $j$ when $d=2m$ and even $j$ when $d=2m+1$, the rows' sums being the corresponding $4j$ — an arithmetic statement about those integers, not a classification of the tuples a curve can carry; that the representative odd tuple $(1,1,1,1,1)$ has squared sum $5$ and $8F_d(2)=4(d-1)$ is divisible by $4$ while $5$ is not — two divisibility facts, not an enumeration of the odd tuples; and the corrected $8$ against $16$: $(2,2,0,0,0)$ equals $8(F_d(2)-g)$ at $(d-3)/2$ and not at $(d-5)/2$, while $16$ is the value at $(d-5)/2$ and the squared sum of $(2,2,2,2,0)$. **Not** certified, and untouched by the computation: that a smooth connected curve of the stated degree and genus exists on a smooth cubic surface, its smoothness, connectedness or irreducibility, either statement as a whole with its hypotheses ($\CC$ and $g>0$, $0\le r\le2d/3$, the window $F_d(r-1)<g\le F_d(r)$, $g\le1+d(d-3)/6$, $r$ the least such integer, the three printed triples $(9,1,2)$, $(23,22,4)$, $(27,28,4)$), the minimum-genus bound of Exercise V.4.9 and the closedness of its range, and the attribution $r(\OO_S(C))=2$; this row closes neither [#111](https://github.com/dzackgarza/new-qual-site/issues/111) nor [#121](https://github.com/dzackgarza/new-qual-site/issues/121). | every degree of both families; no degree is sampled | <https://github.com/dzackgarza/new-qual-site/blob/d4122f28c509b86fb8f1ad5e9c80e7b72ccbae75/proofs/cards/V49FiveSquaresTuples.sage> | part |

## 3. The topological identification (cited, hypotheses verified)

For `E-HAT-2.3-1` the passage from the cellular chain complex to the homology of the Moore
space $X=S^1\cup_m e^2$ and of the pair $(X,A)$ with $A=S^1$ is made by three theorems of
Hatcher, whose hypotheses are checked here rather than assumed:

| Theorem | Statement used | Hypotheses, checked |
| --- | --- | --- |
| Theorem 2.35 | $H_n^{CW}(X)\cong H_n(X)$ | $X$ is a CW complex. $X=S^1\cup_m e^2$ has the finite CW structure with one cell in dimensions $0,1,2$. |
| Cellular Boundary Formula (pp. 140--141) | $d_n(e^n_\alpha)=\sum_\beta d_{\alpha\beta}e^{n-1}_\beta$ with $d_{\alpha\beta}$ the degree of the composite attaching map | $X$ is a CW complex with a set cell structure. With one $0$-cell and one $1$-cell, $d_1=0$; the $2$-cell is attached by a degree $m$ map, so $d_2=m$. |
| Proposition 2.22 | for good pairs, $q_*:H_n(X,A)\cong \widetilde H_n(X/A)$ | $(X,A)$ is a good pair: $A$ is a closed subspace that is a deformation retract of a neighbourhood. $A=S^1$ is a subcomplex of the CW complex $X$, so the pair is a good pair, and $X/A\cong S^2$. |

Nothing in category 1 or 2 establishes these; they are the uniform statement, cited from
the source being audited (`pi.math.cornell.edu/~hatcher/AT/AT.pdf`, the same file the
card's source checks use).

## 4. Cited, not formalized

For `E-HAT-3.A-6` the card now cites Hatcher's own Proposition 3A.5 by item number instead
of adverting to standard theory: (2) additivity, (3) vanishing for free or torsion-free
groups, (4) the reduction to the torsion subgroup, (5) $\operatorname{Tor}(\ZZ_n,B)\cong
B[n]$, and (6) the long exact sequence; together with Exercise 4 of §3.A for commutation
with direct limits. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> formalizes the parts of (3), (5) and (6) that
are statements about torsion, flatness and tensor products; the comparison theorem (Lemma
3A.2), additivity (2), the torsion reduction (4) and the direct-limit statement (Exercise
4) are cited. An earlier version of this note said that Mathlib's `CategoryTheory.Tor` has no comparison
API; that was wrong, and it was wrong because it came from searching the `Tor` namespace alone. The
pinned tree (`db584cd6`) has, with exact names:

- `Mathlib/CategoryTheory/Abelian/Projective/Resolution.lean`: `ProjectiveResolution.lift`
  (`def lift`, l.92) with `lift_commutes` (l.100), the homotopies `liftHomotopy` (l.162),
  `liftIdHomotopy` (l.168), `liftCompHomotopy` (l.173), and **`homotopyEquiv` (l.180)**, which
  states that two projective resolutions of the same object are homotopy equivalent — the engine
  of Lemma 3A.2.
- `Mathlib/CategoryTheory/Abelian/LeftDerived.lean`: `Functor.leftDerived` (l.107) and
  `ProjectiveResolution.isoLeftDerivedObj` (l.111) with its naturalities
  `isoLeftDerivedObj_hom_naturality` (l.123) and `isoLeftDerivedObj_inv_naturality` (l.138),
  computing the derived functor from *any* chosen projective resolution; plus
  `Functor.leftDerived_map_eq` (l.161). `homotopyEquiv` sits in the same file at l.180 with
  `homotopyEquiv_hom_π` / `homotopyEquiv_inv_π` immediately after it, which give the compatibility
  with the augmentation `pi` that a comparison of resolutions needs.
- `Mathlib/CategoryTheory/Monoidal/Tor.lean`: `Tor` (l.44) and `Tor'` (l.50), defined as the left
  derived functor of the tensor product.
- `Mathlib/RingTheory/Flat/Basic.lean`: `Module.Flat.rTensor_exact` (l.340),
  `rTensor_preserves_injective_linearMap` (l.120), `iff_rTensor_exact` (l.393).

So resolution independence is not what is missing, and neither is the flat case, which a `Tor`
namespace search had also missed: `Mathlib/RingTheory/Flat/Equalizer.lean` provides
`LinearMap.lTensor_injective_of_exact_of_flat`, which for `M --g→ N --f→ P` with `P` flat, `f`
surjective, `g` injective and `Exact g f`, gives `Injective (g.lTensor A)` for every `A`. With
`g` the relation map `K → F` of a two-term free resolution, `f` the quotient map `F → F ⧸ range f`
and `P` that quotient, this *is* the kernel-zero case of the cards' vanishing direction — no
connecting map and no snake lemma needed, only `LinearMap.lTensor_inj_iff_rTensor_inj`
(`RingTheory/Flat/Basic.lean`) to move to the factor order the presentation-level `torKernel`
uses. So `E-HAT-3.A-2`'s "torsion-free `A` implies `Tor(A,B) = 0`" is formalizable today for a
genuine free resolution, given the injectivity of the relation map.

What remains missing is therefore narrower than this note previously said: the identification
`Tor 1 A B ≅ ker (f.rTensor B)` for a two-term resolution (a `ProjectiveResolution` instance built
from `0 → K → F → 0` plus the degree-1 homology computation), and — for `E-HAT-3.A-6` — the
structure of a finite f.g. stage. Neither requires reimplementing comparison or exactness theory:
`ProjectiveResolution.homotopyEquiv` and `LinearMap.lTensor_injective_of_exact_of_flat` are the
maintained constructions to use.

**The identification, with the API and the pitfalls fixed.** `CategoryTheory/Abelian/LeftDerived.lean`
provides `ProjectiveResolution.isoLeftDerivedObj (P) (T) (n) : (T.leftDerived n).obj X ≅ H_n (T
applied to P.complex)`. The plan is therefore: (1) build `P : ProjectiveResolution A` from the
two-term complex `0 → K → F → 0`; (2) apply the isomorphism with `T = Tor`-side functor; (3) compute
the degree-1 homology of `T P.complex` and identify it with `ker (f.rTensor B)`.

Three things must be discharged explicitly, and each has bitten before:

- **Orientation.** `CategoryTheory/Monoidal/Tor.lean` resolves the *second* argument for `Tor` and the
  *first* for `Tor'`. Resolving `A` with `(- ⊗ B)` computes `Tor' A B`; using `(B ⊗ -)` computes
  `Tor B A`. The card's statement is symmetric, but the Lean statement is not, and the two must not
  be identified silently: no balancing theorem is being invoked here.
- **Projectivity of `K`.** A two-term projective resolution needs `K` projective. `Module.Projective.of_free`
  (`Algebra/Module/Projective.lean`, l.161) turns `Module.Free` into it, and in a *free* resolution `K`
  is free by construction, so the bridge should carry `[Module.Free ℤ K]` (or `Module.Projective ℤ K`)
  as a hypothesis rather than derive it. Deriving it from `K ↪ F` with `F` free would need "a submodule
  of a free module over a PID is free", which this audit did not locate in the pinned tree — a search of
  `LinearAlgebra/FreeModule/`, `RingTheory/Flat/TorsionFree.lean` and `Algebra/Module/Submodule/` found no
  such statement, and for infinite rank it is not a triviality. So the projectivity hypothesis belongs in
  the statement, not in a side lemma.
- **The kernel identification itself.** An unmatched one-shot isomorphism between the degree-1
  homology of the two-term complex after the tensor functor and `ker (f.rTensor B)`; the incoming
  differential at degree 1 is zero, so this is `ker/im` with `im = 0`.

Nothing above requires resolution comparison or flat-cokernel injectivity: those are maintained.

**Now proved, not pending.** `TorReductions.rTensor_injective_of_flat_cokernel`: for
`f : K →ₗ[ℤ] F` injective with `[Module.Flat ℤ (F ⧸ LinearMap.range f)]`, the map `rTensor B f` is
injective for every `B` — hence `TorReductions.torKernel_eq_bot_of_flat_cokernel`, the kernel
vanishes. The proof applies the maintained
`LinearMap.lTensor_injective_of_exact_of_flat` to `0 → K → F → F ⧸ range f → 0` (the quotient map
as the surjection, exactness from `Submodule.mkQ_apply` and `LinearMap.mem_range`) and moves from
`lTensor` to the `rTensor` factor order by `LinearMap.lTensor_inj_iff_rTensor_inj`. Axioms
`propext`, `Classical.choice`, `Quot.sound`. This settles the vanishing direction of `E-HAT-3.A-2`
for a genuine free resolution, which is one route to it; the identification
`Tor 1 A B ≅ ker (f.rTensor B)`, which this route stops short of, is closed for every surjection from
a free module — hence for every abelian group `A` — by
`TorExercise3A6.torOneTorKernelAddEquiv`, and section 5b records how.

## 5. Outstanding obligations

**None.** Every entry this section has carried is withdrawn below, each into a certificate that
settles the claim without the step it named, and the route each certificate takes is recorded in
section 5b. Nothing here is a repair awaiting a certificate.

The form an entry takes, so that a new one is written the same way, is a repair made to a stored
proof whose mathematical content no file here certifies: a claim of the form "this argument proves
the stored statement", which may not be reported as settled until a file here covers it.

- ~~`E-HAT-3.A-6` and `E-HAT-3.A-2`, the filtered-colimit passage (Exercise 4 of §3.A)~~ —
  **withdrawn: both cards are certified without it, for every abelian group `A`.** The certificates
  take the presentation `π : (A →₀ ℤ) → A`, whose middle term is free on the whole group `A`, so
  neither a filtered colimit nor a descent through the finitely generated subgroups is on the route:
  `TorExercise3A6.torOneTorKernelAddEquiv` is the identification of `Tor₁(A, B)` with the kernel of
  the right-tensored syzygy inclusion for *any* such `π`, and that kernel is killed by a product of
  Smith-normal-form diagonal entries (`exists_fg_stage`, `exists_nsmul_eq_zero_of_stage`,
  `nsmul_eq_zero_of_nsmul_map_eq_zero`). The `⊗` half recorded here still stands —
  `ColimitTensor.tensorLeft_colim_iso` gives `B ⊗ colim F ≅ colim (B ⊗ F ·)` — and is simply no
  longer needed (§1's rows).
- ~~`E-HAT-3.A-2`: the restored direction "torsion-free implies $\operatorname{Tor}(A,B)=0$ for all
  $B$"~~ — **withdrawn: proved for arbitrary `A`.**
  `TorExercise3A2.isTorsionFree_iff_forall_subsingleton_torOne` is the full biconditional at
  `TorBridge.torOne` for every abelian group `A`: forward, a torsion-free `ℤ`-module is flat, so the
  syzygy inclusion stays injective after tensoring with `B`
  (`TorReductions.rTensor_injective_of_flat_cokernel`) and `Tor₁(A, B)` is trivial; backward,
  `B = ℚ/ℤ` and the first statement. The finitely generated half recorded here
  (`isZero_torOne_of_finite_torsionFree`) stands and is no longer the end of the argument.

With both entries withdrawn this section names no outstanding obligation of the two cards; the
route each certificate takes is recorded in section 5b.

## 5b. The card applications: what closed them

The applications the group lemmas did not reach, recorded with the obstruction each named so that
none could be closed by a name check against the pinned source. All three are closed, and by a
route that avoids every obstruction this section used to name.

- **The presentation bridge is closed, and it is not the projective-resolution route.**
  <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A6.lean>'s
  `torOneTorKernelAddEquiv` states, for **every** abelian group `A`, every **surjection**
  `π : F →ₗ[ℤ] A` from a free `F` and every abelian group `B`,

  `Tor₁(A, B) ≃+ ker ((ker π).subtype.rTensor B : ker π ⊗ B → F ⊗ B)`,

  `Tor₁` being `TorBridge.torOne`, the left derived functor of `tensorLeft B`. Nothing is assumed of
  `ker π`: it need not be free, finitely generated or projective, so the upstream gap recorded in the
  provider requests below ("every subgroup of a free abelian group is free") is not on this route and
  no resolution of an arbitrary `A` is built. The map is
  `TorArbitrary.torOneIsoKerIncl`'s dimension-shift isomorphism (Weibel, *An Introduction to
  Homological Algebra*, Exercise 2.4.3) transported to the presentation-level kernel through
  `HomologicalComplex.homologyIsoSc'` and `ModuleCat.kernelIsoKer`.
- **The descent, the torsion statement and the order statement are closed at the stage, not at a
  colimit.** `exists_fg_stage` carries a vanishing class to a finitely generated direct summand `F'`
  of the free middle term (`TorStages.exists_stage_of_free`), and `exists_nsmul_eq_zero_of_stage`
  puts that stage's relation submodule into Smith normal form (`Submodule.smithNormalForm`); the
  diagonal entries' product then kills every element of the stage's kernel, and
  `nsmul_eq_zero_of_nsmul_map_eq_zero` transports the killing integer back along the bridge. That is
  `isAddTorsion_torOne`: `Tor₁(A, B)` is a torsion group for all `A` and `B`. The order statement is
  `torOne_exists_addOrderOf_iff` for every positive `n`, assembled from the prime-power core
  `torOne_prime_pow_iff`: its forward half `exists_addOrderOf_of_torOne` reads `p ^ k` off an
  elementary divisor of the stage, and its backward half `exists_torOne_of_addOrderOf` uses that the
  cyclic subgroup `ℤ z` generated by the syzygy element is **pure** in `ker (pres A)` — so the
  quotient is torsion-free, hence flat, and `ℤ z ⊗ B → ker (pres A) ⊗ B` is injective — giving an
  element of `Tor₁(A, B)` of order `p ^ k` from elements of that order in `A` and in `B`.
- **What the earlier record held open, and why none of it is needed.** The filtered-colimit passage
  (Exercise 4), the construction of a free resolution of an arbitrary `A`, and Hatcher's Lemma 3A.2
  as presentation-independence: none of the three is invoked by either certificate. The finitely
  generated resolution <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorFreeResolution.lean>
  remains a valid separate route to `IsZero (Tor₁(A, B))` for a finitely generated torsion-free `A`,
  and is not a step of the arbitrary-`A` argument. Axioms for every declaration named above:
  `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; elaborated on Lean 4.36.0 at Mathlib
  `6d97e8ad`, the head `lake-manifest.json` of lean-categories main pins.

- ~~the simplex chain-model comparison for `E-HAT-2.2-16`: identifying the chains the card writes down
  with the barycentric ones~~ — **withdrawn: the obligation it named is discharged.**
  <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/DeltaSimplexChains.lean> certifies the chains the card writes down — free abelian groups on
  the `(i+1)`-element vertex subsets — in their own model, end to end: acyclicity, the ranks, the
  vanishing below `k` and the top homology's rank (§1's row). No identification with the barycentric
  ones is needed for that card. The upstream facts recorded here remain true, and remain Mathlib's
  own TODO: the pin has no `SSet.B` (the nerve of the poset of nondegenerate simplices) and no
  natural transformation `SSet.sd ⟶ SSet.B`; the place they would live is
  `Mathlib/AlgebraicTopology/SimplicialSet/Subdivision.lean`, whose own TODO at lines 19--23 names
  exactly these two declarations.

### Provider requests, stated so that they can be accepted or refused

*(Re-verified against the master head `c9f80237` on 2026-11-11, by reading the named files:
both still-wanted items below are still absent there. Item 1 is no longer needed by the
dimension-shift route of <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorArbitrary.lean>, which prescribes the first presentation
of the resolution and therefore never asks for a projective kernel; items 3 and 4 are
withdrawn because the work was done without them.)*

Four statements were wanted from the pinned library rather than from this directory; two are still
wanted, and the third and fourth are withdrawn below because the work was done without them. None is a request to
relax anything above: where a proof needed one of them, the claim was restricted to the case that
could be certified, and the restricted case is what is proved. Each absence was re-checked against
`db584cd6` in the pass that wrote this paragraph, by reading the named file rather than by searching
for a name.

1. **`Module.Free R ↥N` for `N : Submodule ℤ (ι → ℤ)` with `ι` arbitrary** — equivalently, every
   subgroup of a free abelian group is free. Present only for finite `ι`:
   `Submodule.nonempty_basis_of_pid` and `Submodule.basisOfPid`
   (`LinearAlgebra/FreeModule/PID.lean:272`, `:295`) both carry `[Finite ι]`, and the only general
   `Module.Free`-on-a-submodule instance is the lattice case (`Algebra/Module/Lattice.lean:173`).
   *Needed by:* nothing in this directory any more. The two Tor cards take the presentation
   `π : (A →₀ ℤ) → A`, whose middle term is free by construction, so neither a resolution of an
   arbitrary `A` nor freeness of its kernel is required (section 5b); the finitely generated
   two-term resolution needs the freeness only for a finitely generated `A`, supplied by the
   principal-ideal-domain result. The absence is still true, and still the reason the unrestricted
   Lemma 3A.2 has no formal counterpart.
2. **`Tor` commutes with filtered colimits** (§3.A exercise 4): for a filtered diagram
   `A : J ⥤ ModuleCat ℤ`, `Tor₁(colim A, B) ≅ colim Tor₁(A ·, B)`. Absent in any formulation tried:
   `CategoryTheory/Abelian/LeftDerived.lean` carries no filtered-colimit result at all, and
   `CategoryTheory/Monoidal/Tor.lean` supplies no comparison. *Needed by:* nothing in this directory
   any more: both cards are certified for arbitrary `A` without a filtered-colimit statement, by the
   stage argument of section 5b. The absence stands and is recorded here for whoever asks next.
3. ~~**`SSet.B`**, the functor sending `X` to the nerve of its partially ordered type of nondegenerate
   simplices, **together with a natural transformation `sd ⟶ B`**~~ — **withdrawn.** The
   `E-HAT-2.2-16` identification it was wanted for is no longer an obligation:
   <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/DeltaSimplexChains.lean> certifies the card's own chain model directly, so no barycentric
   chain model is needed for that card. The absence is still true and still Mathlib's own TODO at
   `AlgebraicTopology/SimplicialSet/Subdivision.lean:19-21`, in exactly those words; it is simply no
   longer in the way.
4. ~~**Truncation of a chain complex above a degree**, `truncLE k`~~ — **withdrawn.** The skeleton
   comparison of `E-HAT-2.2-16` needed no truncation functor: `K.exactAt_iff'` already states
   exactness at a degree as exactness of the three-term complex `K.sc' (j+2) (j+1) j`, so comparing
   three degrees and two differentials is enough, and <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SkeletonHomology.lean> does exactly that.
   The absence recorded here (only `ChainComplex.truncate`, `Algebra/Homology/Augment.lean:31`,
   which deletes degree `0` and shifts down) is still true; it is simply no longer in the way.

They are recorded here because this section is where the directory's upstream dependencies are
audited. They are **not** filed against the library: the connected GitHub scope is this repository,
so this text is what a filing would quote.

The name-by-name check against `db584cd6` is a check, not acceptance: what is written above is
what the files prove on the canonical baseline, and nothing more.

## 6. Chapter 1 step repairs: expository, with the backing theorem checked

These repairs were made to stored proofs but assert no theorem beyond the source's own
argument. They are listed here with the theorem that backs each, so that nothing is hidden
and nothing is claimed as certified. No machine certificate exists for any of them.

| Card | What the repair does | Backing |
| --- | --- | --- |
| `E-HAT-1.1-17` | replaces "standard computation" by an explicit use of $\pi_1(X\vee Y)=\pi_1X*\pi_1Y$ and spells out the degrees of the retractions | Hatcher Example 1.21 (wedge sums), whose hypotheses — path-connected, nondegenerately based spaces — hold for the two circles |
| `E-HAT-1.2-12`, `-14`, `-16` | rewrite closing steps so that the presentation, the eight words and the generator counts are multiplied out rather than named | the source's own computation; the cube complex of `-14` is the one whose abelianization is checked in `cards/DeltaComplexHomology.sage` |
| `E-HAT-1.2-22` | renames the subcomplex $X_0$, corrects it to two-dimensional, and replaces the $1$-skeleton claim by a collapse and a retraction of the strips | Hatcher Proposition 0.17 (quotient by a contractible subcomplex of a pair with the homotopy extension property is a homotopy equivalence): $(X_0,T)$ is a CW pair, so it has the HEP, and $T$ is a rectangle, hence contractible. The remaining step, that each strip's image retracts to a circle, is a picture-level check, not formalized |
| `E-HAT-1.A-8` | rewritten twice; certified in Lean, see the table above | — |
| `E-HAT-1.A-9`, `-12` | closing steps state why the intersection of the conjugates is normal of finite index, and list the three conclusions | the source's own argument |

A `solution-reviewed` note on a card records that the proof was read and what was checked;
it is a review record, not a certificate.

## 7. Reuse audit: what the formalization corpus already owns

Run before any further authorship of the two §3.A and §2.1 developments, through the formalization
corpus (the live OpenAPI contract at `https://formalization-corpus.dzackgarza.com/api/openapi.json`,
version 1.1.0, operations `POST /api/search`, `POST /api/search/batch`, `POST /api/list`). Every row
below was checked by opening the upstream repository at a pinned commit; the corpus is a discovery
index and its snapshots are not commit-pinned evidence.

Access note, recorded factually. The earlier report of a `403` from this API is not explained by
this pass, so its cause is not asserted. What was observed: `POST /api/search` with a JSON body over
`curl` returned **HTTP 200** throughout; `POST /api/search/batch` sent from Python 3.12's
`urllib.request` with its default user agent raised `HTTPError 403` (response body not read at the
time); the same endpoint over `curl` with a well-formed body returned **HTTP 400** with body
`{"Error":"Field required; Field required"}`, because the batch schema requires `{ID, Request}` items
rather than bare search requests; and after correcting the body it returned **HTTP 200**. These are
status codes and clients, nothing more. They do not establish *why* the 403 occurred, and no refusal
is labelled here as authorized or unauthorised. No query below depends on the batch endpoint: every
source and declaration recorded was retrieved by opening the upstream repository at the pinned commit
shown, and the one endpoint that answered for every request in this pass was `/api/search`.

### 7a. Barycentric subdivision of singular chains (`E-HAT-2.1-25`)

| Source | Pin | Path / declarations | Licence | Comparison |
| --- | --- | --- | --- | --- |
| **Mathlib (ours)** | `db584cd6d46c92f209a44c0f1c829460d327499d` | `AlgebraicTopology/SimplicialSet/Subdivision.lean`: `SSet.sd`, `SSet.ex`, `sdExAdjunction`. `AlgebraicTopology/SingularHomology/Basic.lean` has the singular chain functor but **no** subdivision, and no `∂S = S∂`. | Apache-2.0 | Route 1 fails: the only subdivision in the pin is the simplicial-**set** subdivision functor `sd`, not the barycentric subdivision of singular chains. |
| **Tau Ceti** | `67e852853c5192ec69775bb7ef417fc199e4190e` | `TauCeti/AlgebraicTopology/Singular/Subdivision/Basic.lean`: `BarycentricSubdivision.vertex` (`π k ↦` barycentre of the face spanned by `π k, …, π n`), `sum_sign_face_succ_eq_zero`, `sum_sign_face_zero`, **`sum_sign_boundary`**, `singularSubdivisionX`, **`singularSubdivisionChainMap`** (`∂S = S∂` as a chain map), `singularSubdivision` (natural in `X`). `…/Subdivision/Homotopy.lean`: `AffineChain.prism`, **`boundary_prism_add_prism_boundary`** (`∂P + P∂ = 1 − S`), `singularSubdivisionHomotopy`, `homologyMap_singularSubdivisionChainMap`. Also `Small/Basic.lean` and `Twisted/Subdivision.lean`. | Apache-2.0 | **Strictly stronger than <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean>.** Stated for a preadditive category `C` with coproducts and any `n`, on the maintained singular chain complex, and it includes the chain-map property our file explicitly does not claim. Its `vertex π k` is the same descending-barycentre model our `chainOf`/`descVertex` builds by hand; `sum_sign_boundary` is our pair-cancellation plus facet reindexing in about 40 lines. |
| **qinz1yang/differential-geometry** | `fd2f07fba4c6c102ba626c59153ad98da8f0d442` | `DifferentialGeometry/External/CanonicalTopology/Topology/Homology/SingularSubdivisionBoundary.lean`: `integralSingularSubdivision_boundary_simplex` (the formula for one `(n+1)`-simplex), `integralSingularSubdivision_boundary` (chain level, same carrier), `integralSingularSubdivisionChainMap`. Plus `SingularSubdivision.lean`, `UniversalSubdivisionFaces.lean`, `UniversalHomotopyBoundary.lean`. | Apache-2.0 | Independent second Lean 4 formalization of the same identity, in an `integralSingularChains` API of its own. (`Topology/Homology/Subdivision/Basic.lean` returned `404` at this commit; the live files are under `External/CanonicalTopology/`.) |
| **Isabelle** | corpus snapshot `isabelle-prover__mirror-isabelle` | `src/HOL/Homology/Simplices.thy`: `simplicial_subdivision`, `singular_subdivision`, `chain_boundary_simplicial_subdivision`, `naturality_singular_subdivision`, `singular_chain_singular_subdivision`. | BSD-style | Cross-prover reference; the Tau Ceti Lean development follows this file's shape. |
| **HOL Light** | `31fe213ce4f7ee7296366511335998ebeb956900` | `Multivariate/homology.ml`: `simplicial_subdivision` (l. 1716), `singular_subdivision` (l. 2031), `CHAIN_BOUNDARY_SIMPLICIAL_SUBDIVISION` (l. 1797), `CHAIN_BOUNDARY_SINGULAR_SUBDIVISION` (l. 2293), `CHAIN_HOMOTOPIC_SINGULAR_SUBDIVISION` (l. 2598). Verbatim hypotheses: `chain_boundary p (singular_subdivision p c) = singular_subdivision (p-1) (chain_boundary p c)` for `singular_chain (p,s) c`; and `?h` additive in `c`, sending `frag_0` to `frag_0`, raising degree by one, with `chain_boundary (p+1) (h p c) + h (p-1) (chain_boundary p c) = singular_subdivision p c - c` for `singular_chain (p,top) c`. | HOL Light BSD-style (`LICENSE`, © University of Cambridge 1998, John Harrison and others) | The original machine-checked statement of both facts. Vendored verbatim in `CakeML__candle` at the same path. |

**Routing.** Mathlib fails, and Tau Ceti is not a Lake dependency of this repository (nor of the
pinned image), so the gate's route 3 applies: cite, do not re-derive. Consequence for the
deliverable: <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> is an **independent re-derivation in an explicit coefficient
model** (`FreeAbelianGroup (List (Finset (Fin N)))`, every coefficient computed), not the first
formalization of the formula, and the card's notes must say so. The decision not to develop
`∂S = S∂` locally is now backed by prior art rather than by an argument from scope: that identity
is already proved in Lean 4 twice (Tau Ceti `singularSubdivisionChainMap`; qinz1yang
`integralSingularSubdivisionChainMap`) and in HOL Light and Isabelle. Nothing about the card's claim
is missing from the literature; what our file adds is a coefficient-level model, which is the part
the card displays.

**Genuinely task-specific glue that no located source provides:** none for this card. The card asks
for the coefficient formula and it is formalized, three times over, in three systems.

### 7b. `Tor` over `ℤ` (`E-HAT-3.A-6`, `E-HAT-3.A-2`)

| Source | Pin | Path / declarations | Licence | Comparison |
| --- | --- | --- | --- | --- |
| **Mathlib (ours)** | `db584cd6…` | `CategoryTheory/Monoidal/Tor.lean`: `Tor`, `Tor'`, `isZero_Tor_succ_of_projective`, and the file's own note "we have almost nothing to say about it". `CategoryTheory/Abelian/LeftDerived.lean`: `ProjectiveResolution.isoLeftDerivedObj`, `Functor.isZero_leftDerived_obj_projective_succ`. `CategoryTheory/ObjectProperty/{Basic,EpiMono,ClosedUnderIsomorphisms}.lean`: `inverseImage`, `IsClosedUnderSubobjects`, `IsClosedUnderQuotients`, `prop_of_mono`, `prop_of_epi`, `prop_of_iso`. `RingTheory/TensorProduct/Finite.lean`: **`Submodule.exists_fg_le_eq_rTensor_inclusion`**. `RingTheory/Finiteness/Basic.lean`: **`Submodule.fg_iff_compact`**. | Apache-2.0 | The primitives are all here; the *closed-under-left-derived-functors* lemma and every `Tor`-specific vanishing statement are not. Crucially, the finite-generation step that <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorStages.lean> constructs by hand is a **library lemma** in this pin: `exists_fg_le_eq_rTensor_inclusion` says that for `x : I ⊗ M` there is a finitely generated `J ≤ I` with `x` in the image of `J ⊗ M`, and `fg_iff_compact` turns "finitely generated" into compactness of the submodule lattice. |
| **Tau Ceti** | `67e852853c…` | `CategoryTheory/ObjectProperty/Homology.lean`: `prop_homology`, **`prop_leftDerived_obj`**. `AlgebraicTopology/SerreClass/Torsion.lean`: `AddCommGrpCat.isTorsion` + `IsSerreClass` instance. `AlgebraicTopology/SerreClass/TensorTor.lean`: **`isAddTorsion_Tor_left`**, `isKilledBySomePower_Tor_left`. `LinearAlgebra/TensorProduct/Torsion.lean`: `isTorsionBy_tensorProduct_left`, `isAddTorsion_tensorProduct_left`. `CategoryTheory/Monoidal/Tor.lean`: **`ShortExact.torOneIsoKernel`**, `isZero_Tor_add_two`, naturality in `X` and in maps of presentations, `Tor'` additivity. `CategoryTheory/Abelian/LeftDerived.lean`: `leftDerivedOneIsoKernel`, **`Functor.isZero_leftDerived_succ`**, `NatTrans.leftDerived_add`, `ShortExact.projectiveResolution`, `isZero_leftDerived_add_two`. `Algebra/Category/ModuleCat/Monoidal/Tor.lean`: `isZero_Tor_succ_of_flat` (**flat ⇒ `Tor`-acyclic**), **`isZero_Tor_succ_quotient_iSup`** (`Tor` of a quotient by a directed union vanishes when it vanishes at every stage), `isZero_Tor_X₂`, `isZero_Tor_succ_X₃`, `isZero_Tor_one_X₃`, `isZero_Tor_prod`, `isZero_Tor_restrictScalars_iff`. | Apache-2.0 | **Part of the card's first claim, already proved, in general form**: `isAddTorsion_Tor_left` is `Tor_n(M,N)` torsion whenever `M` *is* torsion, for any `N` over any commutative ring. It uses no free resolution, no finite stage and no Lemma 3A.2, because `Tor` is *defined* as a left derived functor and `isoLeftDerivedObj` already gives resolution-independence. It is **not** the card's statement, which quantifies over all `A`: see the residual named below. Independently, `isZero_Tor_succ_quotient_iSup` is what the direct-limit step of Hatcher's proof needs, and `isZero_Tor_succ_of_flat` is our `torKernel_eq_bot_of_flat_cokernel` in categorical form. |
| **facebookresearch/atlas-lean** | corpus snapshot | `v1/Atlas/AlgebraicTopologyI/code/{Section12,Section13,SubdivisionSmall,LocalityPrinciple}.lean` | (not read) | Located, not inspected in this pass. Recorded so the next pass does not have to rediscover it. |

**Routing, and what changed.** <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsionClass.lean> is a **port** of the four Tau Ceti
lemmas on the route above and compiles on the canonical baseline with no `sorryAx`. It proves the
torsion case of `E-HAT-3.A-6`'s first claim — *a step, not the claim*: the card says `Tor(A,B)` is
torsion for **all** `A`, and what is proved is the case where `A` is torsion. It carries **no node
obligation**; §7c explains why, and what the card is actually discharged by.

**What stood missing, and what stands there now:**

- **The reduction `A ↦ T(A)` in the first claim of `E-HAT-3.A-6`. Not scheduled, and not on the
  certificate's route.** `TorExercise3A6.isAddTorsion_torOne` proves the first claim for every `A`
  without it, by the stage descent of section 5b, so no card obligation waits on this port; it
  stays recorded because the categorical route below is the one that would need it. Over `ℤ` it
  needs `Tor_n(A,B) ≅ Tor_n(T(A),B)` for `n ≥ 1`, from `0 → T(A) → A → A/T(A) → 0` with `A/T(A)`
  torsion-free, hence flat. Two pieces, both already in the located source and neither ours:
  flat ⇒ `Tor`-acyclic (Tau Ceti `isZero_Tor_succ_of_flat`, itself `Functor.isZero_leftDerived_succ`
  — neither is in the pin) and the long exact sequence of `Tor`
  (Tau Ceti `isZero_Tor_X₂`, `isZero_Tor_succ_X₃`, `isZero_Tor_one_X₃`, built on
  `shortExact_tensorResolutionShortComplex` with `tensorResolution`/`isZero_Tor_iff`, also not in the
  pin). It is a port of perhaps 150 lines rather than research, and it is the price of an
  *executable local* proof of a claim that is neither corrected nor required by a node — so it waits
  until a card needs `Tor`-acyclicity or the long exact sequence inside Lean for its own sake.
- ~~**The second half of `E-HAT-3.A-6`** (an element of order `n` in `Tor(A,B)` iff in both `A` and
  `B`)~~ — **closed: proved for every `n > 0`.** `TorExercise3A6.torOne_exists_addOrderOf_iff`
  states the biconditional at `TorBridge.torOne` for all abelian groups `A` and `B`, at the
  canonical presentation `π : (A →₀ ℤ) → A` that section 5b describes, assembled from the
  prime-power core `torOne_prime_pow_iff`: forward from an elementary divisor of the stage
  (`exists_addOrderOf_of_torOne`), backward from the purity of the syzygy's cyclic subgroup
  (`exists_torOne_of_addOrderOf`). The two inputs the earlier record named as still needed are
  inside that file rather than cited: `Tor(\ZZ/n, B) ≅ B[n]` through the presentation bridge
  `torOneTorKernelAddEquiv`, and the primary decomposition through `torOne_prime_pow_iff`. No
  located published source proves this half, so the proof is the declaration and not a
  transcription; §1's
  <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A6.lean>
  row is the one that covers the card's statement.
- **The packaging step in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorBridge.lean>** (composing `torOneIsoKernel` with the orientation
  transport) is *not* card-specific. `ShortExact.torOneIsoKernel` upstream states the same
  isomorphism in a general monoidal abelian category, with naturality in both variables; the honest
  route is to port that statement rather than to keep fighting the `ModuleCat ℤ` instance diamonds
  that section 1's `TorArbitrary.lean` row records. Any repair attempted there should first ask
  whether the general statement makes the special one unnecessary.

### 7c. What these findings discharge, and what they do not oblige

The repository's acceptance criterion is narrow, and this is the point at which that matters.
`certify-card-corrections` ([#111](https://github.com/dzackgarza/new-qual-site/issues/111)) says: *"A mathematical correction to a card is settled only
with a Lean formalization or an exact Sage proof/certificate **of the corrected claim**, published
under `proofs/`."* `AGENTS.md` §"Data issues" ranks *incorrect data* — statements, titles,
classifications — as the most urgent class and says completion of solutions is "a very low priority
concern and is NOT a data issue".

| Card | What was corrected on it | What the node requires | Discharged by |
| --- | --- | --- | --- |
| `E-HAT-3.A-6` | The printed `iff` restored (the card carried only the "if" half); the proof step that read `B/B_p` as torsion-free replaced by the absence of `p`-torsion | A certificate **of the corrected claims** | The `iff` is settled by the source: Hatcher §3.A Exercise 6 prints it, and the card now matches. The `p`-torsion step is certified by <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> (`torsionBy_pow_eq_bot_of_no_p_torsion`, `mem_of_p_smul_mem_of_pPrimary`, `map_torKernel_mulByInt`), and the converse's group-theoretic core by <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsion.lean>. |
| `E-HAT-2.1-25` | The displayed formula corrected from the ascending to the descending barycentric parametrisation, with the sign `(-1)^{n(n+1)/2}` | A certificate of the corrected formula | <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/BarySubdiv.lean> (`hatcher_formula_arbitrary`), plus the bounded regression `cards/bary_regression.py`. |

Two consequences, stated because the opposite was assumed earlier in this session.

1. **The statement "`Tor(A,B)` is a torsion group" is not a corrected claim.** It is what the card
   already said, and `certify-card-corrections` does not reach it. A local formalization of it is
   therefore **not** an obligation of any node, and <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsionClass.lean> is a **supplement**
   with no card obligation attached, kept because it is committed and it compiles, not because a
   node demanded it. What the card requires is a correct sourced solution, and that is supplied by
   citation — the source is `TauCeti.isAddTorsion_Tor_left` in
   `https://github.com/TauCetiProject/TauCeti/blob/67e852853c5192ec69775bb7ef417fc199e4190e/TauCeti/AlgebraicTopology/SerreClass/TensorTor.lean`
   (Apache-2.0), whose exact statement is: for a commutative ring `R`, `M N : ModuleCat R` and
   `IsAddTorsion M`, every `n : ℕ` satisfies `IsAddTorsion (((Tor (ModuleCat R) n).obj M).obj N)`.
   Note what that hypothesis is and is not — it asks `M` itself to be torsion, and the card's
   `Tor(A,B)` is torsion for unrestricted `A`; the citation covers the reduction target, not the
   card as printed, and the card says so.
2. **The 150-line port described in §7b is not scheduled work.** It is the price of an *executable*
   local proof of a fact that is already formalized upstream and is not a corrected claim here. It
   becomes justified only if a future card needs `Tor`-acyclicity of flat modules or the long exact
   sequence of `Tor` *inside Lean* for its own sake. Until then the reference is the citation.

This also settles how the two §7b residuals should be read. `TorBridge.lean`'s packaging step is not
a card correction either: it is supporting development, and its honest resolution is to cite
`CategoryTheory.ShortComplex.ShortExact.torOneIsoKernel` (Tau Ceti,
`https://github.com/TauCetiProject/TauCeti/blob/67e852853c5192ec69775bb7ef417fc199e4190e/TauCeti/CategoryTheory/Monoidal/Tor.lean`,
exact statement: for a short exact sequence `S` with `S.X₁`, `S.X₂` projective, `Tor₁(X, S.X₃) ≅
kernel (X ◁ S.f)`, natural in `X` and in maps of presentations) rather than to keep maintaining a
special case of it.

## Checking

The proof-artifact entry point is `proofs/justfile`. Run it from the repository root:

```
just --justfile proofs/justfile check
```

It checks two things and elaborates nothing.

- `registry` — `python -m qualc.proofs`, the registry check `qualc check` runs (a row naming a
  card the corpus does not carry, a link whose target is not there, a row that does not say
  whether it covers the card's statement or a part of one, a row in a section no reader of the
  registry treats as a certificate) read without the pandoc build, together with the recipe
  checked against the tree: every artifact `proofs/justfile` invokes is present, it invokes no
  Lean file, and every artifact under `proofs/cards/` is invoked by it. The first four of those
  are `certificate.registry_errors`; `qualc check` calls the same function, so the two entry
  points cannot disagree. A lean-categories row is confirmed over HTTPS, so on a machine with no
  network each such row is reported as a missing target: that is the check's own message, and it
  names the network rather than a moved file.
- `artifacts` — the exact Sage, GAP and Python computations retained in `proofs/cards/`. Each
  exits non-zero on a failed assertion, and section 2 records the interpreter and the output its
  published run carried. The interpreters are `sage` and `gap` on `PATH` by default; the shared
  research image has no `sage` on `PATH`, so there the recipe is run as
  `SAGE=/sage/.venv/bin/sage just --justfile proofs/justfile check`, that being the interpreter
  section 2's recorded runs used.

Lean declarations are validated in lean-categories, where they live, not here: the `.lean`
files, the lake project (`lakefile.toml`, `lake-manifest.json`, `lean-toolchain`) and the Lake
lines of `.gitignore` left this repository under issue #141. Each row of section 1 is a link to
the file at commit `16c09abaa4` of this repository, which stays readable, or to the declaration
on `dzackgarza/lean-categories` main, where lean-categories#141 ported it. `qualc check` follows
each link and fails when its target is not there, so a row is correct in either of the two
forms. Four rows of section 1 name the second form: the two `Tor` rows and
`E-HAT-2.2-16`'s at `5848f0f2`, and `E-HAT-4.1-9`'s at `9b8b8584`. The rest still name
the file at `16c09abaa4`, and the movement of a row from one form to the other is a link
correction, not a change of what the row says it proves.

For a Lean certificate, `#print axioms` on the declaration the row names must show only
`propext`, `Classical.choice` and `Quot.sound`; any appearance of `sorryAx` means the
certificate is not a proof. That check is run in lean-categories, and the elaboration each row
records is the one its author ran there.

## Toolchain: what these certificates were elaborated with, and the shared-image block

The certificates themselves left this repository (issue #141) and are readable at commit
`16c09abaa4`; this section records where they were elaborated while they lived here, and
nothing below is a recipe for re-elaborating them in this tree.

### Current baseline (2026-11-11): the `proofs/` lake project at the Mathlib master head

Standing rule for this repository's Lean artifacts: the lakefile requires `mathlib` at `master`
and the manifest pins the master head the tree was last moved to. `proofs/lakefile.toml`,
`proofs/lean-toolchain` (`leanprover/lean4:v4.36.0-rc2`, master's own pin at the time of the
move) and `proofs/lake-manifest.json` (Mathlib `c9f80237cb8abbd41e5443d1ab83ec88d2a5f9ce`)
implement it; `lake exe cache get` fetches the official oleans, so no Mathlib is built locally
and the shared research image is not on the elaboration path. A Mathlib change that breaks a
file is repaired in that file; the repairs of the move to `c9f80237` are recorded in the
commit history (trailing `rfl`s after `Functor.map_zero`-rewrites; `coordSpan`
noncomputable; `BarySubdiv`'s singular packaging migrated to `Convexity.StdSimplex`, the
structure that master's `TopCat.toSSetObjEquiv` is stated through).

Re-verified absences at the master head `c9f80237` (by reading the named files, not by name
search alone): `CategoryTheory/Monoidal/Tor.lean` still carries no filtered-colimit comparison
and no balancing (its own docstring: "For now we have almost nothing to say about it");
`AlgebraicTopology/SimplicialSet/Subdivision.lean` still carries `SSet.B` and `sd ⟶ B` as its
own TODO; `Module.Free R ↥N` for a submodule of an arbitrary-rank free module is still absent
(`LinearAlgebra/FreeModule/PID.lean` requires a finite index) — and the dimension-shift route
of <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorArbitrary.lean> is built so that it does not need that fact. What master *did*
add since the old pin, and what these certificates now use: functorial projective
resolutions (`ProjectiveResolution.of`, `Projective.syzygies`/`Projective.d`), the
`ChainComplex.mk'` constructor with its exactness lemmas, `Mathlib/LinearAlgebra/TensorProduct/
RightExactness.lean` (`lTensor_exact`, `lTensor_surjective`), and the `Convexity.StdSimplex`
refactor of the topological simplices.

### The shared research image: provisioned, and the baseline for the certificates before the move

### The shared research image: provisioned, and the baseline for these certificates

The image owner's provisioning script was run inside the shared rootfs through the same
launcher the Sage checks use, and it is the same implementation the image build runs, not a
local installer:

```
proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev \
  -b provision-script.sh:/opt/provision-lean-packages.sh -w / \
  /bin/bash /opt/provision-lean-packages.sh /repos
```

- Artifact bytes: `sha256 47b2953961fcdc19b5b0c5b75dedae8b627ffab98bb8413d59654b477d750f33`,
  7651 bytes, from Sage fork local commit `e4ae7ac79c5172711d48ed69d94b816a5289ba56`. The
  delivered attachment carried a 1093-byte instruction preamble ahead of `#!/usr/bin/env bash`;
  the hash is of the script bytes, and those bytes are what was bound and run.
- Outcome: toolchain `leanprover/lean4:v4.33.0` already installed; Mathlib retrieved from the
  official cache and built, `Build completed successfully (8705 jobs)`. No new toolchain, no
  second Mathlib source.
- **Reported, not fixed:** `lean_categories` is pinned at `eea5c7f3bce7a1d2fdfbd58840c4d4bd75c9a8bc`
  by `lean-cas-dsl` and at `82d1370de372a00a86391b74fc2566c9547dfcb6` by
  `lean-cas-dsl-leaf-contracts`, both resolving `/.local/share/lean/v4.33.0/packages`. The
  script reports it, links neither revision, and exits 1; `lean-cas-dsl-leaf-contracts` then
  fails its own manifest check. That project is **not** fixed and is not claimed to be.

Baseline these certificates now rest on: `/repos/lean-categories`, Lean `4.33.0`
(commit `d8b18978322de05a8f3dba51ef03cf5461676c17`) resolved by elan's directory override from
that checkout's `lean-toolchain`, Mathlib `db584cd6d46c92f209a44c0f1c829460d327499d`. Verified:
`lake env lean` there imports `Mathlib` and sees `TensorProduct.prodLeft` with the same
signature the proofs use.

**All eleven files in `proofs/cards/` re-elaborate on that baseline**, with zero occurrences of
`sorryAx` and axiom lists only `propext`, `Classical.choice`, `Quot.sound` — so these
certificates are shared-image acceptance, not merely this VM's `/opt` provision: 11 files, exit
status 0 each, most recently re-run when <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorStages.lean> gained the stage presentation,
the transition maps and the direct-summand counterexample. The applications in section 5b
remain open, on this baseline.

### Where the certificates were first produced (superseded by the section above)

They were originally elaborated by this VM's `/opt/lean/bin/lean` (4.33.1, commit
`819816b2e0`) against `/opt/mathlib` (image Mathlib commit `0df444a36`), image
`base_sha256 4908fb59`. That is superseded: the canonical run above reproduces every file.

### Where the certificates below actually come from

They were elaborated by this VM's own provision, with `/opt/lean/bin/lean` (Lean 4.33.1,
commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`) against `/opt/mathlib`
(image-recorded Mathlib commit `0df444a360eaa60ab8c11dca51a86af692955474`), image
`base_sha256 4908fb59ccd4e87ae4e8e973b7ef56f535448eacb24a87fd787270c0048987bc`
(`/opt/environment.json`). `/opt/mathlib` is a directory inside that rootfs on the same `ext4`
filesystem as `/`, not a bind mount or symlink; it has no git metadata of its own.

That is **not** the shared research image. These are acceptance for this VM's `/opt` provision
only, and they must be re-run on the shared baseline once its Mathlib is built. Note also that
the guides quoted for the shared image and for the reference snapshot disagree with each other
on the Lean version (4.33.0 versus 4.27.0), so no name in this directory should be assumed to
carry over without a check on the target baseline.

### Simplicial contraction infrastructure, verified in this tree

- `SSet.Augmented.StandardSimplex.extraDegeneracy : (Δ : SimplexCategory) →
  CategoryTheory.SimplicialObject.Augmented.ExtraDegeneracy (SSet.Augmented.stdSimplex.obj Δ)`
  — present.
- `CategoryTheory.SimplicialObject.Augmented.ExtraDegeneracy.homotopyEquiv : X.ExtraDegeneracy →
  HomotopyEquiv (AlternatingFaceMapComplex.obj (Augmented.drop.obj X))
  ((ChainComplex.single₀ C).obj (Augmented.point.obj X))` — present.
- `SSet.Augmented.ExtraDegeneracy.map` does **not** exist in this tree under that name.

These give the contraction of the *alternating face map* complex of the standard simplex,
which is not yet the card's chain model: `E-HAT-2.2-16` needs the barycentric/simplicial
chain complex of $\Delta^n$ and the skeleton maps that commute with the differentials, so
`ker_eq_range_of_comm_iso` still has no instantiation. *(That gap is historical: the
card's own model is now certified directly by <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/DeltaSimplexChains.lean>, which does
not go through the alternating face map complex at all.)*

### Simplex chain model (for `E-HAT-2.2-16`): route fixed against the pinned API

Verified in the pinned tree, as the maintained inputs:

- `SSet.Augmented.StandardSimplex.extraDegeneracy : (Δ : SimplexCategory) →
  CategoryTheory.SimplicialObject.Augmented.ExtraDegeneracy (SSet.Augmented.stdSimplex.obj Δ)`
  — present, `AlgebraicTopology/ExtraDegeneracy.lean`.
- `CategoryTheory.SimplicialObject.Augmented.ExtraDegeneracy.homotopyEquiv : X.ExtraDegeneracy →
  HomotopyEquiv (AlternatingFaceMapComplex.obj (Augmented.drop.obj X))
  ((ChainComplex.single₀ C).obj (Augmented.point.obj X))` — present.

That yields a chain homotopy contraction of the *alternating face map* complex of the standard
simplex onto a single copy of the coefficients in degree `0`, which is exactly the exactness
of the augmented complex that `ker_eq_range_of_comm_iso` consumes. Two steps stood between it
and the card, and neither was a formality:

1. the card's chain model for `Δ^n` is the simplicial one on **nondegenerate** simplices,
   while `AlternatingFaceMapComplex` is the unnormalised complex; passing between them needs
   the normalisation comparison, which was not cited in this tree;
2. the `k`-skeleton maps have to be built and shown to commute with the differentials in
   degrees at most `k`, which is the hypothesis of `ker_eq_range_of_comm_iso`.

Both were proved afterwards in the alternating-face-map model — the same vanishing in the
normalised Moore model is `isZero_normalizedHomology`, and the skeleton transport is
`skChains_exact` — and the card needs neither, because its boxed claim is certified in its own
Δ-complex chain model by
<https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/DeltaSimplexChains.lean>:
`subsingleton_sk_homology` for $i<k$ and `sk_homology_top_basis` in degree $k$. The vanishing
statement is therefore certified, and no step of this section is an open obligation of
`E-HAT-2.2-16` as of 2026-11-17. *(Historical note, superseded: the normalisation comparison
and the skeleton transport are both proved in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SimplexChains.lean>,
<https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/ChainLevelSteps.lean> and <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/SkeletonHomology.lean> in the alternating-face-map
model, and the card's own model is certified outright by <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/DeltaSimplexChains.lean>.)
