---
schema: qual/card@1
id: E-AMD-LJNBDMIP
kind: exercise
title: A permutation is odd iff it has an odd number of even cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that a permutation is odd iff it has an odd number of even cycles.
:::

::: solution
**Goal:** For $\sigma \in S_n$ written as a product of disjoint cycles, show $\operatorname{sgn}(\sigma) = -1$ if and only if the number of cycles of even length occurring in that decomposition is odd.

<1>1. Sign of a single cycle: *Proof:* <2>1. A cycle of length $\ell \ge 2$ factors into $\ell - 1$ transpositions: $$(a_1\, a_2\, \dots\, a_\ell) = (a_1\, a_\ell)(a_1\, a_{\ell-1}) \cdots (a_1\, a_2).$$ <2>2. Since $\operatorname{sgn}$ is a homomorphism sending every transposition to $-1$, $$\operatorname{sgn}\bigl((a_1\, \dots\, a_\ell)\bigr) = (-1)^{\ell - 1}.$$ <2>3. Hence a cycle is an odd permutation exactly when $\ell$ is even, and this also holds for $\ell = 1$, where the cycle is the identity and $(-1)^{0} = 1$.

<1>2. Sign of a product of disjoint cycles: *Proof:* <2>1. Write $\sigma = c_1 c_2 \cdots c_r$ as a product of disjoint cycles of lengths $\ell_1, \dots, \ell_r$.
<2>2. Multiplicativity of $\operatorname{sgn}$ and Step 1.2 give $$\operatorname{sgn}(\sigma) = \prod_{i=1}^r (-1)^{\ell_i - 1} = (-1)^{\sum_{i=1}^r (\ell_i - 1)}.$$

<1>3. Reduction to a count of even-length cycles: *Proof:* <2>1. Let $E = \{ i : \ell_i \text{ is even} \}$.
The term $\ell_i - 1$ is odd exactly when $\ell_i$ is even, that is, exactly when $i \in E$.
<2>2. A sum of integers is odd if and only if it has an odd number of odd terms, so $$\sum_{i=1}^r (\ell_i - 1) \equiv |E| \pmod 2.$$ <2>3. Substituting into Step 2.2: $$\operatorname{sgn}(\sigma) = (-1)^{|E|}.$$

<1>4. Conclusion: *Proof:* <2>1. $\sigma$ is odd $\iff \operatorname{sgn}(\sigma) = -1 \iff (-1)^{|E|} = -1 \iff |E|$ is odd.
<2>2. That is, $\sigma$ is odd if and only if it has an odd number of even-length cycles.
Q.E.D.
:::
