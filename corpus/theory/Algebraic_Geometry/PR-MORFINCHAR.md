---
schema: qual/card@1
id: PR-MORFINCHAR
kind: proposition
title: Finite equals proper plus quasi-finite
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Proper Morphisms
  - Quasi-finite Morphisms
relations:
- kind: uses
  target: D-MORFIN
- kind: uses
  target: D-8XX95
review: draft
prompts:
- Give a criterion for a morphism to be finite.
- How are finite, proper, and projective related?
---

::: {.proposition}
Let $\pi \colon X \to Y$ be a morphism of schemes.

1. $\pi$ is finite if and only if it is integral and locally of finite type.

2. If $\pi$ is finite, then it is quasi-finite: every fibre is a finite discrete set.

3. If $\pi$ is finite, then $X \cong \operatorname{\mathbf{Proj}}_Y \mathcal{S}$ over $Y$ for a quasicoherent graded $\OO_Y$-algebra $\mathcal{S}$ generated in degree $1$ by the finite type module $\mathcal{S}_1$; in particular $\pi$ is projective in the sense of [[D-SCHRELSPECPROJ]], and proper.

4. A morphism of locally Noetherian schemes is finite exactly when it is proper and quasi-finite, equivalently proper with finite fibres.
Without Noetherian hypotheses: finite exactly when proper, locally of finite presentation, and with finite fibres.
:::

::: {.proof}
All four statements are local on $Y$, so let $Y = \Spec B$ and, in parts 1–3, $X = \Spec A$ with $A$ a $B$-algebra.

1. If $A$ is a finite $B$-module, each $a \in A$ is integral over $B$ by the determinant trick applied to multiplication by $a$ on a finite generating set, and $A$ is a finitely generated $B$-algebra.
   Conversely, if $A = B[a_1, \ldots, a_n]$ with $a_i$ a root of a monic polynomial of degree $d_i$ over $B$, then every power $a_i^{e}$ with $e \geq d_i$ is a $B$-combination of $1, a_i, \ldots, a_i^{d_i - 1}$, so the monomials $a_1^{e_1} \cdots a_n^{e_n}$ with $0 \leq e_i < d_i$ generate $A$ as a $B$-module.

2. The fibre over $\mathfrak{q} \in \Spec B$ is $\Spec R$ with $R = A \otimes_B \kappa(\mathfrak{q})$, a finite-dimensional $\kappa(\mathfrak{q})$-algebra.
   For a prime $\mathfrak{p}$ of $R$, $R/\mathfrak{p}$ is a domain of finite dimension over a field, hence a field, since multiplication by a nonzero element is an injective, hence surjective, linear map.
   So every prime of $R$ is maximal, hence minimal, and the Noetherian ring $R$ has finitely many minimal primes ([[PR-DIVZEROPOLE]], step <1>1); the fibre is finite and discrete.

3. Let $S = \bigoplus_{n \geq 0} S_n$ with $S_0 = B$, $S_n = A$ for $n \geq 1$, and multiplication $S_m \times S_n \to S_{m+n}$ given by multiplication in $A$ (through $B \to A$ when a factor has degree $0$).
   $S$ is generated in degree $1$ by $S_1 = A$, a finite $B$-module.
   For $f \in S_1 = A$, the map $(S_f)_0 \to A_f$, $g/f^k \mapsto g/f^k$ for $g \in S_k = A$, is an isomorphism: every $a/f^m \in A_f$ is represented by $a \in S_m$, and $g/f^k = g'/f^{k'}$ in $S_f$ exactly when $f^N(g f^{k'} - g' f^k) = 0$ in $A$ for some $N$, which is equality in $A_f$.
   So $D_+(f) \cong \Spec A_f$ compatibly with restrictions, and since $1 \in S_1$ with $D_+(1) = \Proj S$, $\Proj S \cong \Spec A_1 = \Spec A$ over $\Spec B$.
   Globally $\mathcal{S}_0 = \OO_Y$ and $\mathcal{S}_n = \pi_* \OO_X$ for $n \geq 1$.
   Projective morphisms are proper.

4. Finite morphisms are proper by part 3 and quasi-finite by part 2. The converse, that a proper quasi-finite morphism of locally Noetherian schemes is finite, is a consequence of Zariski's main theorem ([[T-MORZMT]]).
:::

::: {.remark}
This is the characterisation to quote, because it converts a condition on modules into two conditions one can see.
The implications to keep straight run
\[
\text{finite} \implies \text{projective} \implies \text{proper} \implies \text{universally closed},
\]
with none of them reversible: $\PP^1_k \to \Spec k$ is projective and not finite, and the standard non-projective proper example is a complete non-projective threefold, which is worth naming but not constructing.

The converse direction, proper plus finite fibres giving finite, is the one that does real work: it is how one knows the normalisation of a variety is a finite morphism, and how a proper morphism with zero-dimensional fibres is recognised as an affine one.
:::
