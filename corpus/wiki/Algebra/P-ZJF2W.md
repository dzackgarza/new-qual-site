---
schema: qual/card@1
id: P-ZJF2W
kind: problem
title: When the Galois group of a polynomial is contained in $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
If we think of the Galois group of a polynomial as contained in $S_n$, when is it contained in $A_n$?
:::

::: {.solution}
**Goal.** Characterize when the Galois group of a polynomial of degree $n$ is contained in $A_n$.

<1>1. The Galois group acts on the $n$ roots, giving an embedding $G \hookrightarrow S_n$.
Proof: $G$ permutes the roots of the polynomial, and this action is faithful.

<1>2. $G \subseteq A_n$ iff the discriminant is a square in the base field.
<2>1. The discriminant $\Delta = \prod_{i < j} (r_i - r_j)^2$ is fixed by $G$.
Proof: $\Delta$ is a symmetric polynomial in the roots, hence lies in the base field.
<2>2. The square root $\sqrt\Delta = \prod_{i<j}(r_i - r_j)$ is fixed by $\sigma \in G$ iff $\sigma$ is an even permutation.
Proof: $\sigma$ acts on $\sqrt\Delta$ by $\operatorname{sgn}(\sigma)$, so $\sigma(\sqrt\Delta) = \operatorname{sgn}(\sigma)\sqrt\Delta$; this equals $\sqrt\Delta$ iff $\operatorname{sgn}(\sigma) = 1$.
<2>3. Hence $G \subseteq A_n$ iff $\sqrt\Delta$ is fixed by all of $G$ iff $\sqrt\Delta$ lies in the base field iff $\Delta$ is a square in the base field.
Proof: an element of the splitting field is fixed by $G$ iff it lies in the base field (Galois correspondence).

<1>3. Q.E.D.
Proof: <1>2.3 is the criterion: $G \subseteq A_n$ iff the discriminant is a square.
:::
