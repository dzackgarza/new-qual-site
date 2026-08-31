---
schema: qual/card@1
id: P-DUVZD
kind: problem
title: Cycle type, order, and sign of $(4\,2\,1)(6\,1\,3\,2)$
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
- Let $\sigma = (4\, 2\, 1)(6\, 1\, 3\, 2) \in S_6$ in cycle notation.

  - Write $\sigma$ as a product of disjoint cycles.

  - Compute the order of $\sigma$.
    What is the general theorem about the order of cycles?

  - Determine if $\sigma$ is even or odd.
    What is the general theorem?
:::

::: {.solution}
<1>1. Disjoint cycle decomposition of $\sigma = (4\,2\,1)(6\,1\,3\,2)$:
<2>1. Evaluate the permutation on each element of $\{1, 2, 3, 4, 5, 6\}$ (applying operations from right to left):
- $1 \mapsto 3 \mapsto 3$,
- $3 \mapsto 2 \mapsto 1$,
- $2 \mapsto 6 \mapsto 6$,
- $6 \mapsto 1 \mapsto 4$,
- $4 \mapsto 4 \mapsto 2$,
- $5 \mapsto 5 \mapsto 5$.
::: {.proof}
composition of permutations.
:::
<2>2. Tracing the orbits:
- $1 \mapsto 3 \mapsto 1$, giving the 2-cycle $(1\,3)$.
- $2 \mapsto 6 \mapsto 4 \mapsto 2$, giving the 3-cycle $(2\,6\,4)$.
- $5$ is fixed.
Thus the disjoint cycle decomposition is:
\[
\sigma = (1\,3)(2\,6\,4).
\]
::: {.proof}
orbit decomposition of a finite set under permutation action.
:::

<1>2. Order of $\sigma$ and general theorem:
<2>1. **General Theorem:** Let $\pi \in S_n$ have disjoint cycle decomposition $\pi = c_1 c_2 \cdots c_k$, where each cycle $c_i$ has length $\ell_i$.
Because disjoint cycles commute and have disjoint supports, the order of $\pi$ in $S_n$ is:
\[
\operatorname{ord}(\pi) = \operatorname{lcm}(\ell_1, \ell_2, \dots, \ell_k).
\]
::: {.proof}
disjoint cycles generate mutually commuting cyclic subgroups with trivial intersection.
:::
<2>2. For $\sigma = (1\,3)(2\,6\,4)$, the lengths are $\ell_1 = 2$ and $\ell_2 = 3$.
Therefore:
\[
\operatorname{ord}(\sigma) = \operatorname{lcm}(2, 3) = 6.
\]
::: {.proof}
$\operatorname{lcm}(2, 3) = 6$.
:::

<1>3. Parity of $\sigma$ and general theorem:
<2>1. **General Theorem:** A $k$-cycle can be factored as a product of $k-1$ transpositions:
\[
(a_1 \, a_2 \, \dots \, a_k) = (a_1 \, a_k)(a_1 \, a_{k-1}) \cdots (a_1 \, a_2).
\]
Hence the signature of a $k$-cycle is $\operatorname{sgn}(c) = (-1)^{k-1}$.
For any permutation $\pi = c_1 \dots c_k$ with cycle lengths $\ell_1, \dots, \ell_k$, the sign is:
\[
\operatorname{sgn}(\pi) = \prod_{i=1}^k (-1)^{\ell_i - 1} = (-1)^{\sum_{i=1}^k (\ell_i - 1)}.
\]
::: {.proof}
sign homomorphism $\operatorname{sgn}: S_n \to \{\pm 1\}$.
:::
<2>2. For $\sigma = (1\,3)(2\,6\,4)$:
\[
\operatorname{sgn}(\sigma) = (-1)^{2-1} \cdot (-1)^{3-1} = (-1)^1 \cdot (-1)^2 = (-1) \cdot (+1) = -1.
\]
Thus $\sigma$ is an **odd permutation**.
::: {.proof}
evaluation of sign.
:::

<1>4. Conclusion:
$\sigma = (1\,3)(2\,6\,4)$, $\operatorname{ord}(\sigma) = 6$, and $\sigma$ is odd. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
