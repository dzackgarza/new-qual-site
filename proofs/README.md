# Proof artifacts

Machine-checked certificates for mathematical corrections made to corpus cards, kept in
three separate categories. They are not interchangeable.

1. **Group lemmas proved in Lean** — statements about groups, linear maps and tensor
   products, proved here with no `sorryAx`.
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

## 1. Group lemmas proved in Lean

| File | Card | What it proves |
| --- | --- | --- |
| `cards/FieldHomework1.lean` | `P-FHW1-01` | The printed hypothesis of problem 1(a) holds with $L=\bot$ for every $\alpha$ (the refutation), and both directions of the corrected statement with $L\ne 0$. |
| `cards/SubgroupFiniteness.lean` | `E-HAT-1.A-8` | A group with a finite generating family has finitely many subgroups of a given nonzero index: `finite_hom` and `subgroup_eq_stabilizer_comap`. |
| `cards/NormExtension.lean` | `P-TAMURAS15-10` | For a closed subspace $Y$ of a real normed space and $x\notin Y$: a functional of norm at most one vanishing on $Y$ with $\varphi x\ne0$. |
| `cards/Tamuras15_10.lean` | `P-TAMURAS15-10` | The corrected statement in full, including the `x ∈ Y` case `exists_mem_S` by Hahn--Banach. |
| `cards/MooreSpaceExactness.lean` | `E-HAT-2.3-1` | The group data behind the two exactness failures: $\ZZ/m$ is nontrivial for $m\ge2$ and torsion; a sequence with trivial ends cannot be exact at $\ZZ/m$; multiplication by $m\ge2$ on $\ZZ$ is injective but not surjective. |
| `cards/TorTorsion.lean` | `E-HAT-3.A-6` | The coordinate step of the converse and the refutation of the inference it replaces: `ratchet_le`, `exact_order_smul`, `exists_coord`, `zmod_two_no_exact_order_eight`, `zmod_eight_order_four`. |
| `cards/FamilyQuotient.lean` | `E-HAT-2.3-2` | The precise implication the dimension step needs: if the family $(f_i)_{i\in\ZZ}$ of groups is carried by a `Finset` (every group outside it is trivial), then the canonical map $\bigoplus_i f_i\to\prod_i f_i$ is **surjective**, so the quotient $\prod_i f_i\big/\bigoplus_i f_i$ is trivial; stated as `directSumToPi_surjective_of_finite_support` and `quotient_subsingleton_of_finite_support`, with the point case (all groups trivial) and the $S^0$ case (exactly one nonzero index) as corollaries. It does **not** assert that the sum and the product are isomorphic, and says nothing for a family with infinite support — there the map is not surjective in general, which is why the candidate fails the wedge axiom. The identification of the $f_i$ with reduced homology groups is not formalized. |
| `cards/ChainLevelSteps.lean` | `E-HAT-2.2-16` | The degree-zero and skeleton steps of the repair, but not the enumeration of the simplex's chains: `choose_rank_step` (Pascal's identity), `ker_ne_top_of_surjective_to_int` (a surjection onto $\ZZ$ has proper kernel), `not_subsingleton_ordinary_homology` (with $\ker\varepsilon=\operatorname{im}\partial_1$ and $\varepsilon$ onto $\ZZ$, the ordinary $C_0/\operatorname{im}\partial_1\cong\ZZ$ is not trivial, so $Z_0/B_0$ cannot stand in for $\widetilde H_0$), and `ker_eq_range_of_comm_iso` (exactness transports across an isomorphism of three-term complexes, which is how the $k$-skeleton inherits exactness in the degrees where its differentials agree with the simplex's). **Not** certified: that the simplex's augmented complex is exact, that its chains are the barycentric ones, and hence $\widetilde H_i((\Delta^n)^k)=0$ for $i<k$ as a statement about the simplex. |
| `cards/BarySign.lean` | `E-HAT-2.1-25` | The **all-`n` counting and sign algebra** behind the corrected subdivision formula. `card_pairSet`: the pairs `i < j` in `Fin N` number `N(N-1)/2`, via `Finset.card_sigma`, `Fin.card_Iio`, `Fin.sum_univ_eq_sum_range` and `Finset.sum_range_id`. `noninv_add_inv`: inversions and noninversions partition those pairs, via `Finset.card_filter_add_card_filter_not`. `sign_eq_neg_one_pow_inv`: `π.sign = (-1)^{inv π}` in `ℤˣ`, from the maintained `Equiv.Perm.sign_eq_prod_prod_Iio` (`GroupTheory/Perm/Fin.lean`) together with `Finset.prod_sigma'`, an induction over the pair set, `Finset.card_insert_of_notMem` and `pow_succ`. Axioms `propext`, `Classical.choice`, `Quot.sound`. It also proves the **deletion-index correspondence**: `delSum π = Σ_j #{i ∈ Iic j : π i < π j}` is the recursion's exponent, since the step `F_j → F_{j-1}` deletes `π j`; `filter_Iic_eq_filter_Iio` kills the diagonal, `filter_pairSet` filters the sigma set, and `delSum_eq_noninv` concludes `delSum π = noninv π`; `pow_delSum_eq_global_mul_sign` then gives the all-`n` identity `(-1)^{delSum π} = (-1)^{N(N-1)/2} sgn(π)`. **What this file is not:** it is the sign algebra of the corrected formula, not the recursion. The recursion itself is modelled, with every coefficient computed, in `cards/BarySubdiv.lean` (next row). The two files cannot import each other, so the recursion file restates these theorems, with these proofs, before applying them (`cards/BarySubdiv.lean`, section 8). What no file does is identify either with Hatcher's operator on singular chains. The pinned tree has the raw material — `AlgebraicTopology.singularChainComplexFunctor` (`AlgebraicTopology/SingularHomology/Basic.lean`), `SSet.ιChainComplex_d` and `SSet.chainComplex_hom_ext` (`SSet/Homology/Basic`) — and the missing step is the definition of the subdivision operator on that complex together with `S λ = b_λ (S ∂λ)`, which is not built. |
| `cards/BarySubdiv.lean` | `E-HAT-2.1-25` | **Hatcher's recursion itself, modelled, with its coefficients computed.** In `FreeAbelianGroup (List (Finset (Fin N)))`, `N = n+1`: `deletionPos` is the position of a vertex in a face and `stepExp`/`stepSign` the exponent and sign the boundary contributes along a peeling order, with `stepSign_eq_pow_stepExp`; `stepExp_eq_pairCount` proves the accumulated exponent depends only on the peeling order and not on the intermediate faces — it is the number of pairs `i < j` of that order with `l_j < l_i`, the deletion-index identity. `subdiv` is `S λ = b_λ (S ∂λ)` with the apex prepended; `coeff_subdiv` computes **every** coefficient of it and `coeff_subdiv_chainOf` shows the coefficient of the chain of a peeling order is exactly the recursion's `stepSign` there (`coeff_subdiv_chainOf_eq_pow` reads it as a power of `−1`). Permutation side: `deletionPos_univ` (at the top face the deletion position of a vertex is its value — the outermost deletion's factor), `peel π = (π n, …, π 0)` (the order the recursion deletes in) with `coeff_subdiv_peel` for the chain it builds. Geometric side: `baryWeight`/`baryWeight_mem` (a face's barycentre as a point of `stdSimplex`), `affineMap`/`affineMap_mem`/`affineMap_single` (the affine map spanned by an ordered vertex list, and the listed vectors are its vertices), `descFace`/`descVertex` with `descVertex_zero` — the descending barycentric vertex list of `π` begins at the barycentre of the whole simplex, which is the vertex the cone prepends. **The coefficient theorem, for every `π`:** `pairCount_ofFn` (a list count over `List.ofFn g` is the `Fin`-indexed count of pairs `i < j` with `g j < g i`, with `length_filter_ofFn`, `card_filter_pos` and `card_filter_succ_lt` carrying a filtered list length to a `Fin`-indexed cardinal), `pairCount_peel_eq_delSum` (the peeling order `peel π = (π (N-1), …, π 0)` has deletion-position count exactly the permutation's deletion sum `delSum π = Σ_j #{i ≤ j : π i < π j}`), the sign algebra restated here and applied (`pow_delSum_eq_global_mul_sign`, `pow_delSum_eq_global_mul_sign_int`), and therefore `coeff_subdiv_peel_sign`: for every `N` and every `π`, the recursion's coefficient of the descending chain of `π` is exactly `(−1)^{N(N-1)/2} sgn(π)` — the number the card displays, derived from the recursion rather than assumed. **The whole chain, not only its coefficients:** `chainCoeff_exists_chainOf` (support exhaustion: a chain with nonzero predicted coefficient is `chainOf F l` for a `Nodup` `l` enumerating `F`, by induction along `chainCoeff`'s recursion) and `chainOf_injective` (nonduplication: two peeling orders enumerating `F` and giving the same chain are equal, by strong induction on `F`, the head of the chain forcing the erased vertex) give, with `exists_perm_peel` (every `Nodup` enumeration of `univ` is some `peel π`) and `chainOf_peel_injective`, the identity `subdiv_univ_eq_sum_perm`: `subdiv univ` **equals** `Σ_π (−1)^{N(N-1)/2} sgn(π) • of (chainOf univ (peel π))` in the free abelian group on chains of faces — one summand per permutation, nothing else in the support (`ext_coeff` compares all coefficients). **Transport side, proved:** `chainOf_getElem?_take` (the `k`-th face of a chain is `F` with the first `k` peeled vertices removed), `descFace_antitone` (the descending flags are nested), and with `descVertex_zero`/`descVertex_last` the descending barycentric vertex list runs from the barycentre of the whole simplex to the vertex `π 0` itself; `affineMap_mem`/`affineMap_single` give the affine simplex spanned by such a list. **The flags, and the transport to vertex lists:** `chainOf_peel_eq_ofFn_descFace` identifies the recursion's chain for `π` with the list of prefix faces (`peel_take_toFinset`, `rev_image_Iio`, `sdiff_image_of_bijective`, `univ_sdiff_Ioi`, `peel_take_face`, `chainOf_length`); `map_baryWeight_chainOf_peel` reads those faces as their barycentres and gets exactly the descending vertex list; `map_subdiv_univ_bary` is the linear extension of that reading over the free abelian group, carrying the whole recursion to the signed sum of the descending vertex lists; `affineMap_cons_apply` is the coordinate form of Hatcher's prepend (the apex enters with its own barycentric coordinate `x 0`), and `continuous_affineMap` with `affineMap_mem` and `affineMap_single` makes that list a continuous affine map of the standard simplex with exactly those vertices. **Hatcher's operator formula:** `chainAffineMap` reads a chain of faces geometrically (vertex `k` is the barycentre of the `k`-th face), `barySimplex` is `Δ̄_π` on the descending barycentric vertex list, `chainAffineMap_chainOf_peel` proves the chain of `π` **is** its `Δ̄_π`, and `hatcher_formula` states, for an arbitrary continuous `σ` out of the standard `n`-simplex, `map (c ↦ σ ∘ (chain c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • of (σ ∘ Δ̄_π)` — the left side being Hatcher's `S σ` defined from `S λ = b_λ (S ∂λ)`, the right side the displayed closed formula. **Into degree `n` of the maintained chain complex:** `barySimplexOn`/`barySimplexSingular` package `Δ̄_π` through `TopCat.toSSetObjEquiv` as an honest singular `M`-simplex of the standard simplex (`toSSetObjEquiv_barySimplexSingular` shows the packaging is faithful); the degree-`M` group of `X.chainComplex (ModuleCat.of ℤ ℤ)` is *definitionally* the coproduct of one copy of `ℤ` per singular `M`-simplex (checked by `rfl`), so `singularChainIota` is the coprojection with no extra identification, and `singular_chain_formula` states the recursion pushed through `chainSingular`/`barySingular` and the coprojections: `lift (c ↦ ι (chainSingular c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • ι (Δ̄_π)`. **For an arbitrary singular simplex:** `chainVertex`/`chainAffineOn` corestrict each chain's affine map to the standard-simplex subtype with `affineMap_mem` (fixed-vertex junk fallback, so the map is total on chains), `chainAffineOn_chainOf_peel` makes it `Δ̄_π` on the recursion's chains, `chainSigma`/`barySigma` package `σ ∘ (·)` as singular `M`-simplices of `X` through `TopCat.toSSetObjEquiv` (read back by `toSSetObjEquiv_barySigma` / `toSSetObjEquiv_chainSigma`), and `hatcher_formula_arbitrary` states, for `σ : Δⁿ → X` arbitrary, `lift (c ↦ ι (chainSigma σ c)) (subdiv univ) = Σ_π (−1)^{n(n+1)/2} sgn(π) • ι (barySigma σ π)` — the left side the transported prepend-cone recursion, the right side the closed formula with the descending parametrisation. Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; 58 printed theorems, `exit 0`. **Boundary, stated:** the chain-map property `∂ ∘ S = S ∘ ∂` is not claimed — the exercise asks for the coefficient formula, which is what is proved. |
| `cards/bary_regression.py` | `E-HAT-2.1-25` | **A bounded regression, not a certificate.** For `n = 1, 2, 3` only, with executable assertions (the operator must equal `(-1)^{n(n+1)/2}` times the descending formula and must differ from the ascending formula and from its negative), it computes in the free abelian group on vertex tuples (i) Hatcher's recursive subdivision operator `S(lambda) = b_lambda(S partial lambda)`, (ii) the ascending barycentric formula the card used to carry, and (iii) the descending one it now carries. It confirms `S = (-1)^{n(n+1)/2}` times the descending formula for those three dimensions and refutes the ascending formula, including the exact failure in dimension `1` (`[b,v_1] - [b,v_0]` against `[v_0,b] - [v_1,b]`, different generators of `C_1`). It does **not** prove the identity for `n >= 4`: that rests on the induction written out in the card, which is not formalized, and the all-`n` identity in Lean remains an open obligation. |

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
state, after `cards/BarySubdiv.lean`, is the following.

1. **The deletion-index identity.** *Formalized for all `n` and all `π`:* `stepExp_eq_pairCount` proves that the sum of the deletion positions along a peeling order is the number of pairs `i < j` of that order with `l_j < l_i`; `deletionPos_univ` gives the outermost factor as the peeled vertex's value; `pairCount_ofFn` and `pairCount_peel_eq_delSum` carry that list count to the permutation-indexed sum `Σ_j #{i ≤ j : π i < π j}`; and `coeff_subdiv_peel_sign` concludes the coefficient `(−1)^{n(n+1)/2} sgn(π)` for the recursion's descending chain at every `π`.
2. **The prepend-cone recursion.** *Formalized:* `subdiv` is the recursion and `coeff_subdiv` computes all of its coefficients, so the sign at each stage is proved to be the position of the deleted vertex in the current face, not assumed; combined with 1 this gives the coefficient of every `π` (`coeff_subdiv_peel_sign`); and the exhaustive, nonduplicated indexing of the recursion's support by `S_{N}` is proved (`chainCoeff_exists_chainOf`, `chainOf_injective`, `subdiv_univ_eq_sum_perm`), so the single identity `subdiv univ = Σ_π (−1)^{N(N−1)/2} sgn(π) • of (chainOf univ (peel π))` holds in the free abelian group on chains of faces. *Not yet formalized:* the geometric reading of those chains as the singular simplices `σ ∘ Δ̄_π`, i.e. the transport to singular chains of `Δ^n`.

| `cards/LensDegree.lean` | `E-HAT-3.E-2` | The local-degree bookkeeping of the angular extension `(r,θ) ↦ (r, k_j θ)` on `S^{2n-1}`, which is what the card's sign count needs: `det_angDeriv` (the frame derivative is `diag(1,k)`, determinant `k`), `orientation_iff` (the coordinate map preserves orientation exactly when `k>0`), `natAbs_mul_orientation` (one coordinate contributes `|k|·sgn(k)=k`) and `prod_natAbs_mul_orientation` (the product over the coordinates). Scope, stated precisely: this certifies **arithmetic only** — the determinant of `diag(1,k)`, the orientation criterion, and `|k|·sgn(k)=k` with its product over the coordinates. It does **not** certify that the angular extension `f~` has that derivative, that its local degree is `sgn(k_j)`, or `deg f~ = k_1⋯k_n`; those three are named inputs from the lens-space discussion in §3.E, and the degree of `f` follows from them by the covering square `p' f~ = f p`. Written because an earlier repair of the card wrongly explained the sign by the holomorphic power `z ↦ 1/z^{|k|}`, which is conformal with local degree `+1`; the angular extension is a different map when `k<0`. |
| `cards/SimplexChains.lean` | `E-HAT-2.2-16` | **The standard simplex's chain complex is acyclic in positive degrees**, from maintained API and nothing bespoke: `SSet.Augmented.StandardSimplex.extraDegeneracy` transports along the free `ℤ`-module functor (`ExtraDegeneracy.map`), and `ExtraDegeneracy.homotopyEquiv` then gives `chainsHomotopyEquiv`, a homotopy equivalence of the alternating face map complex of the free simplicial group on `Δ^m` with the complex supported in degree `0`. Consequences, both with axioms `propext, Classical.choice, Quot.sound` and no `sorryAx`: `isZero_homology` (`H̃_i(Δ^m) = 0` for `i ≠ 0`, i.e. exactness of the augmented complex above degree zero) and `homologyZeroIso` (`H_0` of the complex is the augmentation's target, which is the form `ker ε = im ∂_1` takes). Scope: this is the **unnormalized** alternating-face-map model; it does **not** compare that model with the normalized/Moore one, does not touch the `k`-skeleton maps, and says nothing about barycentric chains, so it discharges the first of the three things §5 lists for `E-HAT-2.2-16` and no more. |
| `cards/TorStages.lean` | `E-HAT-3.A-6`, `E-HAT-3.A-2` | The genuine stage construction for a presented group, **completed for a free middle term**. The stage: `stageRel` (its relations inside `F'`), `map_stageRel` (they are the relations of the sub-presentation `comap f F' → F'`), `stageMap` (`A' → A`, by `Submodule.mapQ`) and `stageMap_injective`, so the stage is a subgroup `A' ≤ A`. Its own presentation: `stageRelMap` with `range_stageRelMap` (the cokernel is `A'`) and `subtype_comp_stageRelMap`. The directed system: `stageIncl` with `stageIncl_refl` and `stageIncl_comp` (a functor on the poset of submodules of `F`), `stageMap_comp_stageIncl` (the triangles `A' → A'' → A` and `A' → A` commute) and `stageIncl_injective`. The filtered-colimit step, with its hypothesis isolated and sharp: `rTensor_subtype_injective_of_retraction` (a retraction of `F' ↪ F` makes `F' ⊗ B → F ⊗ B` injective), `rTensor_subtype_not_injective` (**certified counterexample**: `F' = 2ℤ ⊆ F = ℤ`, `B = ℤ/2`, so a submodule that is not a direct summand breaks the step even though `F` is free), `exists_stage_witness_of_retraction` (descent for such a stage). Then the choice of stage for free `F`: `coordProj`/`coordSpan`/`coordRetract` with `coordRetract_comp_subtype` (a span of finitely many basis vectors is a direct summand), `coordSpan_fg`, `exists_fg_summand` (every finitely generated `P ≤ K` lies in a finitely generated direct summand), and `exists_stage_of_free`: **every element of `torKernel f` is carried by the `Tor` of a stage whose middle term is a finitely generated direct summand**, and already vanishes there. **Not** proved: Hatcher's Lemma 3A.2, which identifies this presentation-level `Tor` with `\operatorname{Tor}(A,B)`; and, because of it, the torsion statement for a finitely generated stage, see section 5b. The identifications the cards make about the stage itself are proved rather than assumed: `stage_range_fg` (a stage of a finitely generated `F'` is a **finitely generated subgroup** of `A`, since `stageMap` is injective with range the image of `F'`), `stage_finite` (its group is a finitely generated `Z`-module, the hypothesis the structure theorem consumes) and `exists_stage_containing` (**the stages cover `A`**: every element lies in the image of the stage of some finitely generated `F'`, taking `span {x}` for a lift `x`; a covering stage need not be a direct summand, which is why `exists_fg_summand` is a separate statement). |
| `cards/TorReductions.lean` | `E-HAT-3.A-6` | The presentation-level `Tor` and the parts of Hatcher's Proposition 3A.5 that Mathlib supplies: the free case of (3) (`torKernel_eq_bot_of_subsingleton`), the group in (5) (`torsionBy_eq_ker`), the torsion-free-is-flat hypothesis of (3) (`flat_of_torsionFree`, Mathlib's Dedekind-domain instance), and the flatness form of (6) (`rTensor_injective_of_flat`, Mathlib's `Module.Flat.rTensor_preserves_injective_linearMap`); and, for the step that needs the *$p$-primary* hypothesis rather than torsion-freeness, item (5) in full: `lid_rTensor_mulByInt` and `map_torKernel_mulByInt`, that the kernel of $(n\cdot\mathrm{id})\otimes\mathrm{id}_B$ inside $\ZZ\otimes B$ is carried by $\ZZ\otimes B\cong B$ onto $B[n]$ — that is, $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ for this resolution — together with `eq_zero_of_pow_smul_eq_zero`, `torsionBy_pow_eq_bot_of_no_p_torsion` (no $p$-torsion gives $C[p^k]=0$) and `mem_of_p_smul_mem_of_pPrimary` ($B_p$ is saturated for multiplication by $p$, i.e. $B/B_p$ has no $p$-torsion). Additivity (2) is now proved as `prodLeft_comp_rTensor` and `map_prodLeft_torKernel`: the presentation of a direct sum is the direct sum of the presentations, so `torKernel (f₁ ⊕ f₂)` is carried by `TensorProduct.prodLeft` onto `torKernel f₁ × torKernel f₂`. The proof avoids `prodLeft.symm` on arbitrary elements by rewriting the kernel as a `comap` and mapping forward through `Submodule.map_comap_eq_self`. **Not** certified: that the presentation-level kernel computes $\operatorname{Tor}$ for an arbitrary resolution (Lemma 3A.2) and commutation with filtered colimits (Exercise 4), which is what carries the cyclic case and the summand-by-summand case to an arbitrary $p$-primary or torsion-free group. |

| `cards/TorBridge.lean` | `E-HAT-3.A-6`, `E-HAT-3.A-2` | **`Tor₁` is the homology of the tensored projective resolution**, proved: `torOneIsoHomology` gives `((tensorLeft B).leftDerived 1).obj A ≅ H₁(P.complex ⊗ B)` for every projective resolution `P` of `A`, by `ProjectiveResolution.isoLeftDerivedObj` at degree one, with the tensored complex and its degree-1 differential named (`resolutionTensor`, `tensorDiffOne`). Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`. **Also proved:** the two-term step, `homologyIsoKernelOfZero`, `homologyOneIsoKernelOfD`, `homologyOneIsoKernel` and `tensor_d_two_one_eq_zero`, giving `torOneIsoKernel`: for a projective resolution with `IsZero (P.complex.X 2)`, `Tor₁(A,B) ≅ kernel((resolutionTensor B P).d 1 0)`, plus `torOneIsoKerLinear` composed with `ModuleCat.kernelIsoKer`. The map-level content is `resolutionTensor_d` (the tensored differential is the tensor of the resolution's differential). **Also proved:** the orientation `ker_rTensor_eq_comap_ker_lTensor` (`ker (f.rTensor N)` is the `comm`-preimage of `ker (f.lTensor N)`, by `LinearMap.lTensor_comm`), the pinned kernel module `kerModule` with `kernelIsoKerModule` (the `ℤ`-module instance diamond resolved at that boundary), and `tensor_d_hom_eq_lTensor` (the tensored differential is the resolution differential with `B` on the left). **Open:** the single packaging step that composes the two-term bridge with the `comm`-transport into one isomorphism naming `kerModule` of `f.hom.rTensor ↥B`. See section 5b. |
| `cards/ColimitTensor.lean` | `E-HAT-3.A-6`, `E-HAT-3.A-2` | Exercise 4 of §3.A, the `⊗` half, completely: `tensorLeft_preserves_colimits` (for `B : ModuleCat ℤ`, `tensorLeft B` preserves colimits, Mathlib's instance `instPreservesColimitsTensorLeft`) and `tensorLeft_colim_iso`, the comparison `B ⊗ colim F ≅ colim (B ⊗ F ·)` for any `F : J ⥤ ModuleCat ℤ` with `HasColimitsOfShape J (ModuleCat ℤ)`, built from `PreservesColimit.preserves` (which yields `Nonempty (IsColimit _)`, extracted with `Classical.choice`) and `IsColimit.coconePointUniqueUpToIso`. Axioms: propext, Classical.choice, Quot.sound. **Not** certified: the `Tor` half. |
| `cards/TorTorsionClass.lean` | `E-HAT-3.A-6` | **`Tor` of a torsion module is torsion, by the torsion-class route instead of a free resolution.** `prop_homology` (a property closed under subobjects and quotients passes from a complex term to its homology in the same degree) and `prop_leftDerived_obj` (if an additive functor sends projectives into such a class, every left derived functor does) are proved for a general abelian setting; `AddCommGrpCat.isTorsion` is the class of torsion abelian groups with its `IsClosedUnderSubobjects` and `IsClosedUnderQuotients` instances; `isAddTorsion_tensorProduct_left` (tensoring a torsion monoid is torsion, no flatness, no finite generation); and `isAddTorsion_Tor_left`: for `M`, `N` in `ModuleCat R` over **any** commutative ring, `IsAddTorsion M → IsAddTorsion (((Tor (ModuleCat R) n).obj M).obj N)`, with the `ℤ` form `isAddTorsion_tor_int`. Axioms `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`; `exit 0`. **Provenance:** this is a **port**, not new mathematics — the four lemmas are copied from the Tau Ceti project at commit `67e852853c5192ec69775bb7ef417fc199e4190e` (Apache-2.0), see section 7. **No node obligation attaches to this file**: `Tor(A,B)` is torsion is not a corrected claim, so `certify-card-corrections` does not reach it, and the card is discharged by citing the upstream theorem with its hypotheses (§7c). It is kept as a supplement, not as a card requirement. **What it does not cover:** the card's statement is about **all** `A`, and this file proves the case where `A` is torsion — the reduction `Tor(A,B) ≅ Tor(T(A),B)` is §7b's named residual; the second half of the card (an element of order `n` in `Tor(A,B)` iff in both `A` and `B`), which no located formalization proves; and it says nothing about `Tor'`, the other orientation. It does not need — and does not supply — Hatcher's Lemma 3A.2 or a finite-stage witness, because the left-derived-functor definition of `Tor` is already resolution-independent. |

## 2. Chain-level checks in Sage

`cards/DeltaComplexHomology.sage`, run on the Sage development image (11.0.beta5, Python
3.14.10, source HEAD `b0cd7d86e2`; reproduced with `proot -R $HOME/sage-image/rootfs ...`):

| Card | Chain complex checked | Parameter range |
| --- | --- | --- |
| `E-HAT-2.1-4`, `-5`, `-6`, `-9` | the displayed $\Delta$-complex complexes: parachute, Klein bottle, the collapsed complex with $H_1=\ZZ/2^n$, the collapsed $\Delta^n$ | $n\le6$, $n\le8$ |
| `E-HAT-2.2-11` | the cube complex | one case |
| `E-HAT-2.2-19` | $\RP^n/\RP^m$ | $m\le4$, $n\le8$ |
| `E-HAT-2.3-1` | the Moore complex $d_1=0$, $d_2=m$, and the Smith form of $(m)$ on $\ZZ$ | $m\in\{2,3,4,5,6,12\}$ |

Every entry is a finite check of the chain-level statement for the listed parameters. None
of them is a statement about a space, and none settles the corresponding uniform claim.

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
with direct limits. `cards/TorReductions.lean` formalizes the parts of (3), (5) and (6) that
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
for a genuine free resolution, which is what the cards need; the identification
`Tor 1 A B ≅ ker (f.rTensor B)` for an arbitrary two-term resolution remains the open item, with
`ProjectiveResolution.isoLeftDerivedObj` as the maintained bridge.

## 5. Outstanding obligations

Repairs made to a stored proof whose mathematical content no file here certifies. Each is a
claim of the form "this argument proves the stored statement", and none may be reported as
settled until a file here covers it:

- `E-HAT-2.2-16`, third step: the repaired argument needs three things, of which **the first is now
  certified**. `cards/SimplexChains.lean` proves the augmented exactness for the standard simplex:
  `H̃_i(Δ^m) = 0` for `i ≠ 0` (`isZero_homology`) and `H_0` equal to the augmentation's target
  (`homologyZeroIso`, the form `ker ε = im ∂_1` takes), by transporting the standard simplex's
  extra degeneracy along the free `ℤ`-module functor and applying
  `ExtraDegeneracy.homotopyEquiv` — axioms `propext, Classical.choice, Quot.sound`, no `sorryAx`.
  Open still, and stated as such on the file: it works in the **unnormalized**
  alternating-face-map model, so the comparison with the normalized/Moore model is made nowhere in
  this directory; and it establishes nothing about the $k$-skeleton's differentials agreeing with
  the simplex's in degrees at most $k$, hence nothing yet about $\widetilde H_i((Δ^m)^k)=0$ for
  $i<k$. The three-things sentence below is the original statement of the obligation, kept for its
  wording: the augmented exactness $\ker\varepsilon=\operatorname{im}\partial_1$, the
  agreement of the $k$-skeleton's differentials with the simplex's in degrees at most $k$,
  and hence $\widetilde H_i=0$ for $i<k$. `cards/ChainLevelSteps.lean` supplies Pascal's
  identity, the properness of the augmentation kernel, the non-triviality of the *ordinary*
  $H_0$, and the transport of exactness across an isomorphism of three-term complexes; it
  does not supply the simplex's chain complex itself, so the card's implication is still not
  completed.
- `E-HAT-3.A-6` and `E-HAT-3.A-2`, the filtered-colimit passage (Exercise 4 of §3.A). The
  `⊗` half is closed: `ColimitTensor.tensorLeft_colim_iso` gives `B ⊗ colim F ≅ colim (B ⊗ F ·)`,
  built from `PreservesColimit.preserves` with `PreservesColimits (tensorLeft B)` obtained
  explicitly from `ModuleCat.monoidalCategory` and `ModuleCat.monoidalClosed`. The `Tor` half
  is now reduced to two things, both recorded in section 5b: the choice of the stages among
  the direct summands of `F`, and Hatcher's Lemma 3A.2 (presentation-independence), which is a
  citation on top and is not formalized.
- `E-HAT-3.A-2`: the restored direction "torsion-free implies $\operatorname{Tor}(A,B)=0$
  for all $B$" is a citation of exercise 5 of the same section. Two of its three
  ingredients are certified in `cards/TorReductions.lean` — a finitely generated
  torsion-free $\ZZ$-module is free (`free_of_finite_torsionFree`, Mathlib's
  principal-ideal-domain result) and the presentation-level $\operatorname{Tor}$ of a free
  presentation vanishes (`torKernel_eq_bot_of_subsingleton`); the third, that
  $\operatorname{Tor}$ commutes with the filtered colimit of the finitely generated
  subgroups, is exercise 4 of the same section and is not formalized.
## 5b. The two card applications that stay open, and why

These are the applications that the group lemmas do not reach. They are stated here with the
obstruction named, so that neither is closed by a name check against the pinned source: each
requires a construction, not a citation.

- **the resolution bridge is split, and only half is closed.** `cards/TorBridge.lean` proves
  `torOneIsoHomology`: for every abelian group `A`, `B` and **every** projective resolution `P` of
  `A`, `Tor₁(A,B) = ((tensorLeft B).leftDerived 1).obj A ≅ H₁(P.complex ⊗ B)`, by
  `ProjectiveResolution.isoLeftDerivedObj` applied to `tensorLeft B` at degree one — the
  derived-functor half, unconditional in the resolution. **The two-term step is now closed:** 
  `homologyOneIsoKernelOfD` (`K.d 2 1 = 0`) and `homologyOneIsoKernel` (`IsZero (K.X 2)`) identify
  that homology with `kernel (K.d 1 0)` via `HomologicalComplex.homologyIsoSc'` and
  `ShortComplex.LeftHomologyData.ofHasKernel` (whose homology object is definitionally the kernel),
  `tensor_d_two_one_eq_zero` supplies the vanishing differential from the shape by `eq_of_src`, and
  `torOneIsoKernel` composes: `Tor₁(A,B) ≅ kernel ((resolutionTensor B P).d 1 0)` with `P` a
  projective resolution and `IsZero (P.complex.X 2)` the only extra hypothesis. The map-level check is
  `resolutionTensor_d` — the tensored differential *is* `(tensorLeft B).map` of the resolution's
  differential. **The orientation glue is proved:** `ker_rTensor_eq_comap_ker_lTensor` states exactly
  `ker (f.rTensor N) = (ker (f.lTensor N)).comap (TensorProduct.comm ℤ M N)`, by
  `LinearMap.lTensor_comm` — not by an assumed equality — and `tensor_d_hom_eq_lTensor` identifies the
  tensored complex's differential map with `(P.complex.d 1 0).hom.lTensor ↥B` on the `ModuleCat` side.
  **The instance diamond is resolved at the boundary:** `kerModule` pins the kernel's `ℤ`-module
  structure (`letI := f.hom.ker.module`) and `kernelIsoKerModule` is `ModuleCat.kernelIsoKer` stated
  over that pinned module, so the categorical kernel and the linear-map kernel are identified without a
  diamond. **The symmetry on the kernels is now a map-level equivalence at an explicitly ascribed boundary:**
  in a section whose tensor products carry `TensorProduct.instModule` built from the given structures —
  `tensorMod`, `tensorModPN`, `tensorModNM`, `tensorModNP`, declared as inherited local instances —
  `kerCommEquiv` gives `ker (f.rTensor N) ≃ₗ ker (f.lTensor N)` with `comm` and `comm.symm` as its two
  maps and both inverse identities checked, and the orientation equality is restated under those same
  instances (`ker_rTensor_eq_comap_ker_lTensor'`), which is what the earlier attempts lacked: the lemma
  and the maps now mention *one* tensor module structure. The remaining mismatch is one level further
  in, on the kernel subtypes: `ModuleCat.ofHom (e : p ≃ₗ q)` synthesizes
  `AddCommGroup.toIntModule ↥p` where `ModuleCat.of` (via `submoduleModule`, which pins `p.module`)
  infers `p.module`, with the compiler reporting
  "'synthesized type class instance is not definitionally equal to expression inferred by typing rules'
  — synthesized `AddCommGroup.toIntModule ↥p`, inferred `p.module`". Pinning the subtype structures the
  same way is what the earlier passes tried and did not settle.
  **The packaging step is now proved, and it is closed by not going through subtypes at all.**
  `TorBridge.torOneIsoTorKernel` composes `torOneIsoKernel` with `kernel.mapIso` transported across
  the tensor symmetry, and names `torOne A B ≅ Limits.kernel (diffRight P)`: the kernel of the
  **right-tensored** differential `X₁ ⊗ B → X₀ ⊗ B`, which is what the presentation-level
  `torKernel f` of `cards/TorReductions.lean` is. Every object in that statement is a *bundled*
  `ModuleCat ℤ`, so no submodule module structure is synthesized anywhere in it; the ambient tensor
  instances are ascribed in the section, so both sides of the two `comm` isomorphisms mention the same
  one; and the commuting square `kernel.mapIso` asks for is `LinearMap.lTensor_comm` and nothing else
  (`diff_square`). Axioms `propext, Classical.choice, Quot.sound`; no `sorryAx`, on the pinned
  baseline. The subtype route through `kerCommEquiv` stays in the file and stays correct — it is
  simply no longer needed for the composition, and its two instance diamonds (on the kernel subtype
  and on the ambient tensor) are recorded above as what the bundling avoids.

  Hatcher's Lemma 3A.2 as the cards use it is the *unrestricted* application: it needs that kernel
  step **together with** the finite-stage descent already proved in `cards/TorStages.lean`
  (`exists_stage_of_free`, `stageMap_injective`, the directed system). The flat-cokernel lemma
  (`torKernel_eq_bot_of_flat_cokernel`) and the finite-stage lemmas are unchanged and still stand.

- **both card applications are pending.** The lemmas `exists_fg_stage` and
  `lTensor_subtype_injective_of_flat` are proved and useful, but they are not the implication
  the cards need, and the record must not conflate the two.

  `exists_fg_stage` holds `F` and `B` fixed and restricts only `K`: it produces a finitely
  generated `P ≤ K` and a class `t ∈ P ⊗ B` mapping to `x` with `(f|_P ⊗ id_B) t = 0`. It does
  **not** produce a finitely generated subgroup `A_α ≤ A = coker(f)` with a compatible
  presentation, and the stage it does produce need not embed in `A`: with `f = id_ℤ`, `K = F = ℤ`
  and `P = 2ℤ`, the stage's cokernel is `ℤ/2` while `A = coker(id_ℤ) = 0`. Nothing in the lemma
  gives the class, order or transition maps the cards use.

  `lTensor_subtype_injective_of_flat` gives injectivity *given* a submodule `B' ≤ B`; it does
  not produce a finitely generated `B'` and does not lift an element.

  The stage construction of `cards/TorStages.lean` is that second route, and it is now
  complete. For `A = coker(f)` and `F_α ⊆ F` finitely generated and a *direct summand*,
  `K_α = K ∩ f^{-1}(F_α)` presents `A_α ≅ F_α/(F_α ∩ f(K))` by `K_α → F_α`, the inclusion
  `A_α ↪ A` is injective (`stageMap_injective`), the transition maps commute with the maps
  into `A` (`stageMap_comp_stageIncl`), and — `exists_stage_of_free` — every element of
  `torKernel f` is carried by one such stage and already vanishes there.

  The one subtlety, and it is not the flatness step one would first try: vanishing in
  `F ⊗ B` descends to `F_α ⊗ B` only when `F_α` is a direct summand of `F`. It is false for a
  general submodule, and `TorStages.rTensor_subtype_not_injective` certifies the failure with
  `F = ℤ`, `F_α = 2ℤ`, `B = ℤ/2`: `2ℤ ⊗ ℤ/2 → ℤ ⊗ ℤ/2` kills the nonzero generator `2 ⊗ 1`,
  even though `F` is free. `TorStages.rTensor_subtype_injective_of_retraction` is the right
  hypothesis, and for a free `F` the summands are produced from finite sets of basis vectors
  (`coordSpan`, `coordRetract`, `exists_fg_summand`).

  What stays open for the two cards is therefore no longer the colimit passage: it is Hatcher's
  Lemma 3A.2, which identifies this presentation-level `Tor` with `\operatorname{Tor}(A,B)`
  (a citation, not formalized), and with it the torsion statement for one finitely generated
  stage.

  The obstruction is not the structure theorem: that theorem is in Mathlib at the pinned
  revision as `Module.equiv_free_prod_directSum` (a finitely generated module over a PID is
  `(Fin n -> R) x (direct sum of R / R * (p i ^ e i))`), and it is not rebuilt here. Nor is the
  obstruction the choice of an "arbitrary presentation" in the sense of a redundant generating
  set for a resolution: what matters is whether the relation map *is* the one of a free
  resolution. The presentation-level kernel is computed from `f : K -> F` and does not depend on
  `A = coker f` alone: with `f = (u,v) |-> 2u` from `Z x Z` to `Z` and `B = Z` the cokernel is
  `Z/2`, yet `(f (x) id) ((0,1) (x) 1) = 0` while `(0,1) (x) 1` is killed by no nonzero integer,
  so the kernel is not torsion. That `f` is **not** injective (its kernel is `0 x Z`), so
  `0 -> Z x Z -> Z -> Z/2 -> 0` is not exact and this example says nothing about Lemma 3A.2; it
  says that the kernel of `f (x) id` is only `Tor` when `f` is the relation map of a free
  resolution. The application therefore has to instantiate an **injective** `K -> F` coming from a
  genuine free resolution of `A`, check the hypotheses the stage lemmas need (`F'` a finitely
  generated direct summand, `P <= comap f F'` finitely generated, the class already vanishing at
  the stage), and only then invoke 3A.2 and the structure theorem of the finite stage. Proved and
  reusable for that: `map_torKernel_mulByInt` (the cyclic case), `map_prodLeft_torKernel`
  (additivity over a binary sum), `stage_range_fg` and `stage_finite` (the stage is a finitely
  generated subgroup and a finitely generated `Z`-module), `stageMap_injective`,
  `stageMap_comp_stageIncl` with `stageIncl_refl`/`stageIncl_comp`, `exists_fg_summand` (a
  finitely generated `P` lies in a finitely generated direct summand of a free `F`),
  `rTensor_subtype_injective_of_retraction`, `exists_stage_witness_of_retraction` and
  `exists_stage_of_free` (every class of `torKernel f` descends to such a stage).
  Missing, and named as such: the free-resolution instantiation itself and Lemma 3A.2. The
  example above is prose, not certified.

- the simplex chain-model comparison for `E-HAT-2.2-16`, instantiating
  `ker_eq_range_of_comm_iso` with the barycentric chains of `Δ^n` and the skeleton maps. Its
  acyclicity input is now proved (`cards/SimplexChains.lean`, unnormalized model); what remains is
  the instantiation itself — the barycentric chains, the skeleton maps, and the comparison with the
  normalized model — which no file here supplies.

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
| **Tau Ceti** | `67e852853c5192ec69775bb7ef417fc199e4190e` | `TauCeti/AlgebraicTopology/Singular/Subdivision/Basic.lean`: `BarycentricSubdivision.vertex` (`π k ↦` barycentre of the face spanned by `π k, …, π n`), `sum_sign_face_succ_eq_zero`, `sum_sign_face_zero`, **`sum_sign_boundary`**, `singularSubdivisionX`, **`singularSubdivisionChainMap`** (`∂S = S∂` as a chain map), `singularSubdivision` (natural in `X`). `…/Subdivision/Homotopy.lean`: `AffineChain.prism`, **`boundary_prism_add_prism_boundary`** (`∂P + P∂ = 1 − S`), `singularSubdivisionHomotopy`, `homologyMap_singularSubdivisionChainMap`. Also `Small/Basic.lean` and `Twisted/Subdivision.lean`. | Apache-2.0 | **Strictly stronger than `cards/BarySubdiv.lean`.** Stated for a preadditive category `C` with coproducts and any `n`, on the maintained singular chain complex, and it includes the chain-map property our file explicitly does not claim. Its `vertex π k` is the same descending-barycentre model our `chainOf`/`descVertex` builds by hand; `sum_sign_boundary` is our pair-cancellation plus facet reindexing in about 40 lines. |
| **qinz1yang/differential-geometry** | `fd2f07fba4c6c102ba626c59153ad98da8f0d442` | `DifferentialGeometry/External/CanonicalTopology/Topology/Homology/SingularSubdivisionBoundary.lean`: `integralSingularSubdivision_boundary_simplex` (the formula for one `(n+1)`-simplex), `integralSingularSubdivision_boundary` (chain level, same carrier), `integralSingularSubdivisionChainMap`. Plus `SingularSubdivision.lean`, `UniversalSubdivisionFaces.lean`, `UniversalHomotopyBoundary.lean`. | Apache-2.0 | Independent second Lean 4 formalization of the same identity, in an `integralSingularChains` API of its own. (`Topology/Homology/Subdivision/Basic.lean` returned `404` at this commit; the live files are under `External/CanonicalTopology/`.) |
| **Isabelle** | corpus snapshot `isabelle-prover__mirror-isabelle` | `src/HOL/Homology/Simplices.thy`: `simplicial_subdivision`, `singular_subdivision`, `chain_boundary_simplicial_subdivision`, `naturality_singular_subdivision`, `singular_chain_singular_subdivision`. | BSD-style | Cross-prover reference; the Tau Ceti Lean development follows this file's shape. |
| **HOL Light** | `31fe213ce4f7ee7296366511335998ebeb956900` | `Multivariate/homology.ml`: `simplicial_subdivision` (l. 1716), `singular_subdivision` (l. 2031), `CHAIN_BOUNDARY_SIMPLICIAL_SUBDIVISION` (l. 1797), `CHAIN_BOUNDARY_SINGULAR_SUBDIVISION` (l. 2293), `CHAIN_HOMOTOPIC_SINGULAR_SUBDIVISION` (l. 2598). Verbatim hypotheses: `chain_boundary p (singular_subdivision p c) = singular_subdivision (p-1) (chain_boundary p c)` for `singular_chain (p,s) c`; and `?h` additive in `c`, sending `frag_0` to `frag_0`, raising degree by one, with `chain_boundary (p+1) (h p c) + h (p-1) (chain_boundary p c) = singular_subdivision p c - c` for `singular_chain (p,top) c`. | HOL Light BSD-style (`LICENSE`, © University of Cambridge 1998, John Harrison and others) | The original machine-checked statement of both facts. Vendored verbatim in `CakeML__candle` at the same path. |

**Routing.** Mathlib fails, and Tau Ceti is not a Lake dependency of this repository (nor of the
pinned image), so the gate's route 3 applies: cite, do not re-derive. Consequence for the
deliverable: `cards/BarySubdiv.lean` is an **independent re-derivation in an explicit coefficient
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
| **Mathlib (ours)** | `db584cd6…` | `CategoryTheory/Monoidal/Tor.lean`: `Tor`, `Tor'`, `isZero_Tor_succ_of_projective`, and the file's own note "we have almost nothing to say about it". `CategoryTheory/Abelian/LeftDerived.lean`: `ProjectiveResolution.isoLeftDerivedObj`, `Functor.isZero_leftDerived_obj_projective_succ`. `CategoryTheory/ObjectProperty/{Basic,EpiMono,ClosedUnderIsomorphisms}.lean`: `inverseImage`, `IsClosedUnderSubobjects`, `IsClosedUnderQuotients`, `prop_of_mono`, `prop_of_epi`, `prop_of_iso`. `RingTheory/TensorProduct/Finite.lean`: **`Submodule.exists_fg_le_eq_rTensor_inclusion`**. `RingTheory/Finiteness/Basic.lean`: **`Submodule.fg_iff_compact`**. | Apache-2.0 | The primitives are all here; the *closed-under-left-derived-functors* lemma and every `Tor`-specific vanishing statement are not. Crucially, the finite-generation step that `cards/TorStages.lean` constructs by hand is a **library lemma** in this pin: `exists_fg_le_eq_rTensor_inclusion` says that for `x : I ⊗ M` there is a finitely generated `J ≤ I` with `x` in the image of `J ⊗ M`, and `fg_iff_compact` turns "finitely generated" into compactness of the submodule lattice. |
| **Tau Ceti** | `67e852853c…` | `CategoryTheory/ObjectProperty/Homology.lean`: `prop_homology`, **`prop_leftDerived_obj`**. `AlgebraicTopology/SerreClass/Torsion.lean`: `AddCommGrpCat.isTorsion` + `IsSerreClass` instance. `AlgebraicTopology/SerreClass/TensorTor.lean`: **`isAddTorsion_Tor_left`**, `isKilledBySomePower_Tor_left`. `LinearAlgebra/TensorProduct/Torsion.lean`: `isTorsionBy_tensorProduct_left`, `isAddTorsion_tensorProduct_left`. `CategoryTheory/Monoidal/Tor.lean`: **`ShortExact.torOneIsoKernel`**, `isZero_Tor_add_two`, naturality in `X` and in maps of presentations, `Tor'` additivity. `CategoryTheory/Abelian/LeftDerived.lean`: `leftDerivedOneIsoKernel`, **`Functor.isZero_leftDerived_succ`**, `NatTrans.leftDerived_add`, `ShortExact.projectiveResolution`, `isZero_leftDerived_add_two`. `Algebra/Category/ModuleCat/Monoidal/Tor.lean`: `isZero_Tor_succ_of_flat` (**flat ⇒ `Tor`-acyclic**), **`isZero_Tor_succ_quotient_iSup`** (`Tor` of a quotient by a directed union vanishes when it vanishes at every stage), `isZero_Tor_X₂`, `isZero_Tor_succ_X₃`, `isZero_Tor_one_X₃`, `isZero_Tor_prod`, `isZero_Tor_restrictScalars_iff`. | Apache-2.0 | **Part of the card's first claim, already proved, in general form**: `isAddTorsion_Tor_left` is `Tor_n(M,N)` torsion whenever `M` *is* torsion, for any `N` over any commutative ring. It uses no free resolution, no finite stage and no Lemma 3A.2, because `Tor` is *defined* as a left derived functor and `isoLeftDerivedObj` already gives resolution-independence. It is **not** the card's statement, which quantifies over all `A`: see the residual named below. Independently, `isZero_Tor_succ_quotient_iSup` is what the direct-limit step of Hatcher's proof needs, and `isZero_Tor_succ_of_flat` is our `torKernel_eq_bot_of_flat_cokernel` in categorical form. |
| **facebookresearch/atlas-lean** | corpus snapshot | `v1/Atlas/AlgebraicTopologyI/code/{Section12,Section13,SubdivisionSmall,LocalityPrinciple}.lean` | (not read) | Located, not inspected in this pass. Recorded so the next pass does not have to rediscover it. |

**Routing, and what changed.** `cards/TorTorsionClass.lean` is a **port** of the four Tau Ceti
lemmas on the route above and compiles on the canonical baseline with no `sorryAx`. It proves the
torsion case of `E-HAT-3.A-6`'s first claim — *a step, not the claim*: the card says `Tor(A,B)` is
torsion for **all** `A`, and what is proved is the case where `A` is torsion. It carries **no node
obligation**; §7c explains why, and what the card is actually discharged by.

**What is genuinely missing, and whether it is scheduled work:**

- **The reduction `A ↦ T(A)` in the first claim of `E-HAT-3.A-6`. Not scheduled.** Over `ℤ` it
  needs `Tor_n(A,B) ≅ Tor_n(T(A),B)` for `n ≥ 1`, from `0 → T(A) → A → A/T(A) → 0` with `A/T(A)`
  torsion-free, hence flat. Two pieces, both already in the located source and neither ours:
  flat ⇒ `Tor`-acyclic (Tau Ceti `isZero_Tor_succ_of_flat`, itself `Functor.isZero_leftDerived_succ`
  — neither is in the pin) and the long exact sequence of `Tor`
  (Tau Ceti `isZero_Tor_X₂`, `isZero_Tor_succ_X₃`, `isZero_Tor_one_X₃`, built on
  `shortExact_tensorResolutionShortComplex` with `tensorResolution`/`isZero_Tor_iff`, also not in the
  pin). It is a port of perhaps 150 lines rather than research, and it is the price of an
  *executable local* proof of a claim that is neither corrected nor required by a node — so it waits
  until a card needs `Tor`-acyclicity or the long exact sequence inside Lean for its own sake.
- **The second half of `E-HAT-3.A-6`** (an element of order `n` in `Tor(A,B)` iff in both `A` and
  `B`). No located source proves it. `cards/TorTorsion.lean` certifies only its group-theoretic core.
  It still needs `Tor(\ZZ/n, B) ≅ B[n]` — for which `cards/TorReductions.lean` has the kernel
  computation for one resolution, and the ported `torOneIsoKernel` would give it for any projective
  presentation — and the primary decomposition of `\operatorname{Tor}`.
- **The packaging step in `cards/TorBridge.lean`** (composing `torOneIsoKernel` with the orientation
  transport) is *not* card-specific. `ShortExact.torOneIsoKernel` upstream states the same
  isomorphism in a general monoidal abelian category, with naturality in both variables; the honest
  route is to port that statement rather than to keep fighting the `ModuleCat ℤ` instance diamonds in
  section 5b. Any repair attempted there should first ask whether the general statement makes the
  special one unnecessary.

### 7c. What these findings discharge, and what they do not oblige

The repository's acceptance criterion is narrow, and this is the point at which that matters.
`certify-card-corrections` ([#111](https://github.com/dzackgarza/new-qual-site/issues/111)) says: *"A mathematical correction to a card is settled only
with a Lean formalization or an exact Sage proof/certificate **of the corrected claim**, published
under `proofs/`."* `AGENTS.md` §"Data issues" ranks *incorrect data* — statements, titles,
classifications — as the most urgent class and says completion of solutions is "a very low priority
concern and is NOT a data issue".

| Card | What was corrected on it | What the node requires | Discharged by |
| --- | --- | --- | --- |
| `E-HAT-3.A-6` | The printed `iff` restored (the card carried only the "if" half); the proof step that read `B/B_p` as torsion-free replaced by the absence of `p`-torsion | A certificate **of the corrected claims** | The `iff` is settled by the source: Hatcher §3.A Exercise 6 prints it, and the card now matches. The `p`-torsion step is certified by `cards/TorReductions.lean` (`torsionBy_pow_eq_bot_of_no_p_torsion`, `mem_of_p_smul_mem_of_pPrimary`, `map_torKernel_mulByInt`), and the converse's group-theoretic core by `cards/TorTorsion.lean`. |
| `E-HAT-2.1-25` | The displayed formula corrected from the ascending to the descending barycentric parametrisation, with the sign `(-1)^{n(n+1)/2}` | A certificate of the corrected formula | `cards/BarySubdiv.lean` (`hatcher_formula_arbitrary`), plus the bounded regression `cards/bary_regression.py`. |

Two consequences, stated because the opposite was assumed earlier in this session.

1. **The statement "`Tor(A,B)` is a torsion group" is not a corrected claim.** It is what the card
   already said, and `certify-card-corrections` does not reach it. A local formalization of it is
   therefore **not** an obligation of any node, and `cards/TorTorsionClass.lean` is a **supplement**
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

Lean 4.33.1 with the Mathlib on `LEAN_PATH`, and Sage for the integer linear algebra:

On the canonical baseline (the shared research image, section "Toolchain" below) every file
in `proofs/cards/` is elaborated by

```sh
ROOT=$HOME/sage-image/rootfs; REPO=$PWD
for f in proofs/cards/*.lean; do
  $HOME/.udocker/bin/proot-x86_64 -R $ROOT -b /proc -b /dev -b $REPO:/work \
    -w /repos/lean-categories /bin/sh -c "lake env lean /work/$f"
done
```

The Sage check is run inside the same image as recorded in section 2; its entry point is the
image's own (the image has no `sage` on `PATH`, so the command used is the one recorded
there, not a path invented here).

`#print axioms` at the end of each file must show only `propext`, `Classical.choice` and
`Quot.sound`; any appearance of `sorryAx` means the certificate is not a proof.

## Toolchain: what these certificates were elaborated with, and the shared-image block

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
status 0 each, most recently re-run when `cards/TorStages.lean` gained the stage presentation,
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
`ker_eq_range_of_comm_iso` still has no instantiation. That identification is the open part
of the $2.2$-$16$ obligation recorded above.

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
of the augmented complex that `ker_eq_range_of_comm_iso` consumes. Two steps remain, and
neither is a formality:

1. the card's chain model for `Δ^n` is the simplicial one on **nondegenerate** simplices,
   while `AlternatingFaceMapComplex` is the unnormalised complex; passing between them needs
   the normalisation comparison, which is not cited yet;
2. the `k`-skeleton maps have to be built and shown to commute with the differentials in
   degrees at most `k`, which is the hypothesis of `ker_eq_range_of_comm_iso`.

Until both exist, `ker_eq_range_of_comm_iso` still has no instantiation and the card's
vanishing statement stays uncertified.
