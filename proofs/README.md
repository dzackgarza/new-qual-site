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
| `cards/TorReductions.lean` | `E-HAT-3.A-6` | The presentation-level `Tor` and the parts of Hatcher's Proposition 3A.5 that Mathlib supplies: the free case of (3) (`torKernel_eq_bot_of_subsingleton`), the group in (5) (`torsionBy_eq_ker`), the torsion-free-is-flat hypothesis of (3) (`flat_of_torsionFree`, Mathlib's Dedekind-domain instance), and the flatness form of (6) (`rTensor_injective_of_flat`, Mathlib's `Module.Flat.rTensor_preserves_injective_linearMap`); and, for the step that needs the *$p$-primary* hypothesis rather than torsion-freeness, item (5) in full: `lid_rTensor_mulByInt` and `map_torKernel_mulByInt`, that the kernel of $(n\cdot\mathrm{id})\otimes\mathrm{id}_B$ inside $\ZZ\otimes B$ is carried by $\ZZ\otimes B\cong B$ onto $B[n]$ — that is, $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ for this resolution — together with `eq_zero_of_pow_smul_eq_zero`, `torsionBy_pow_eq_bot_of_no_p_torsion` (no $p$-torsion gives $C[p^k]=0$) and `mem_of_p_smul_mem_of_pPrimary` ($B_p$ is saturated for multiplication by $p$, i.e. $B/B_p$ has no $p$-torsion). **Not** certified: that the presentation-level kernel computes $\operatorname{Tor}$ for an arbitrary resolution (Lemma 3A.2), additivity (2), and commutation with direct limits (Exercise 4), which is what carries the cyclic case to an arbitrary $p$-primary group. |

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
4) are cited, and the file records why: Mathlib's `CategoryTheory.Tor` has no long exact
sequence or comparison API to reuse.

## 5. Outstanding obligations

Repairs made to a stored proof whose mathematical content no file here certifies. Each is a
claim of the form "this argument proves the stored statement", and none may be reported as
settled until a file here covers it:

- `E-HAT-2.2-16`, third step: the repaired argument needs three things that no file here
  proves — the augmented exactness $\ker\varepsilon=\operatorname{im}\partial_1$, the
  agreement of the $k$-skeleton's differentials with the simplex's in degrees at most $k$,
  and hence $\widetilde H_i=0$ for $i<k$. `cards/ChainLevelSteps.lean` supplies Pascal's
  identity, the properness of the augmentation kernel, the non-triviality of the *ordinary*
  $H_0$, and the transport of exactness across an isomorphism of three-term complexes; it
  does not supply the simplex's chain complex itself, so the card's implication is still not
  completed.
- `E-HAT-3.A-6` and `E-HAT-3.A-2`, additivity (Proposition 3A.5(2)) and the filtered
  colimit step (Exercise 4): not certified. `cards/TorReductions.lean` records how far the
  additivity went — the tools are `TensorProduct.prodLeft`, `prodLeft_tmul` and
  `LinearMap.ker_prodMap`, and the commutation `prodLeft ∘ ((f₁ ⊕ f₂) ⊗ id) = ((f₁ ⊗ id) ⊕
  (f₂ ⊗ id)) ∘ prodLeft` fails to be provable there because after `LinearMap.comp_apply` the
  goal shows the coerced application of `prodLeft` while `prodLeft_tmul` is stated for the
  uncoerced one, and no coercion lemma in this Mathlib rewrites between them. The
  filtered-colimit step needs the same additivity plus commutation of `⊗` with filtered
  colimits of abelian groups.
- `E-HAT-3.A-6`, passage from cyclic summands to a general $p$-primary group: the identity
  $\operatorname{Tor}(\ZZ/p^k,C)\cong C[p^k]$ is certified at the presentation level and
  the hypothesis "$B/B_p$ has no $p$-torsion" is certified, but additivity (2) and
  Exercise 4's direct limits, which carry that to every $p$-primary $A_p$, are cited.
- `E-HAT-3.A-2`: the restored direction "torsion-free implies $\operatorname{Tor}(A,B)=0$
  for all $B$" is a citation of exercise 5 of the same section. Two of its three
  ingredients are certified in `cards/TorReductions.lean` — a finitely generated
  torsion-free $\ZZ$-module is free (`free_of_finite_torsionFree`, Mathlib's
  principal-ideal-domain result) and the presentation-level $\operatorname{Tor}$ of a free
  presentation vanishes (`torKernel_eq_bot_of_subsingleton`); the third, that
  $\operatorname{Tor}$ commutes with the filtered colimit of the finitely generated
  subgroups, is exercise 4 of the same section and is not formalized.
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

## Checking

Lean 4.33.1 with the Mathlib on `LEAN_PATH`, and Sage for the integer linear algebra:

```sh
lean proofs/cards/MooreSpaceExactness.lean
lean proofs/cards/TorTorsion.lean
lean proofs/cards/TorReductions.lean
lean proofs/cards/FieldHomework1.lean
sage proofs/cards/DeltaComplexHomology.sage
```

`#print axioms` at the end of each file must show only `propext`, `Classical.choice` and
`Quot.sound`; any appearance of `sorryAx` means the certificate is not a proof.
