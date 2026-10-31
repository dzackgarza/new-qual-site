# Proof artifacts

Machine-checked certificates for mathematical corrections made to corpus cards.
Each file states the card it belongs to and what it checks. A finite sample of cases, as in
$\RP^n/\RP^m$ below, is a finite check and not a proof of a general case table.

A source transcription check proves what the source prints; it does not prove the
source's theorem. A counterexample refutes the printed claim but does not establish
the replacement. A correction is marked settled on its card only when a file here
certifies it.

| File | Card | What it certifies |
| --- | --- | --- |
| `cards/FieldHomework1.lean` | `P-FHW1-01` | The printed hypothesis of problem 1(a) holds with $L=\bot$ for every $\alpha$ (the refutation), and both directions of the corrected statement with $L\ne 0$. |
| `cards/DeltaComplexHomology.sage` (run on the Sage development image: 11.0.beta5, Python 3.14.10, source HEAD `b0cd7d86e2`) | `E-HAT-2.1-4`, `-5`, `-6`, `-9`, `E-HAT-2.2-11`, `-19` | The stated chain complexes built with Sage's `ChainComplex` (`degree=-1`, which checks $d^2=0$) and their homology read from `ChainComplex.homology`: parachute, Klein bottle, the collapsed complex with $H_1=\ZZ/2^n$ for $n\le6$, the collapsed $\Delta^n$ for $n\le8$, the cube complex's abelianization, and $\RP^n/\RP^m$ for the sampled range $m\le4$, $n\le8$. |
| `cards/SubgroupFiniteness.lean` | `E-HAT-1.A-8` | A group with a finite generating family has finitely many subgroups of a given nonzero index: `finite_hom` (homs into a finite monoid are determined by their values on generators) and `subgroup_eq_stabilizer_comap` (a subgroup of index $m$ is the stabilizer of a point under its coset action on the set `Fin m`). |
| `cards/NormExtension.lean` | `P-TAMURAS15-10` | For a closed subspace $Y$ of a real normed space and $x\notin Y$: a functional of norm at most one vanishing on $Y$ with $\varphi x\ne0$, built from the normed quotient, `exists_dual_vector` and `Submodule.Quotient.norm_mk_le`. |
| `cards/Tamuras15_10.lean` | `P-TAMURAS15-10` | The corrected statement in full: for a second norm on a closed subspace with the two comparison inequalities, `sup {|φ x| : φ ∈ S}` is nonnegative, definite, homogeneous, subadditive, agrees with the second norm on the subspace, and satisfies `K⁻¹‖x‖ ≤ sup ≤ K‖x‖`. The `x ∈ Y` case is `exists_mem_S`, by Hahn--Banach against the second norm on `Y` and extension with `exists_extension_norm_eq`. |

## Checking

Lean 4.33.1 with the Mathlib on `LEAN_PATH`, and Sage for the integer linear algebra:

```sh
lean proofs/cards/FieldHomework1.lean
sage proofs/cards/DeltaComplexHomology.sage
```

`#print axioms` at the end of each file must show only `propext`,
`Classical.choice` and `Quot.sound`; any appearance of `sorryAx` means the
certificate is not a proof.

## Not yet certified

Nothing is outstanding here. Both card corrections are certified in Lean, and the six Sage
homology checks were rerun on the supported Sage development image (Sage 11.0.beta5, Python
3.14.10, source HEAD `b0cd7d86e2`), all passing.
