---
schema: qual/card@1
id: P-TQGAM
kind: problem
title: Stabilizers need not be normal
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Normal Subgroups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that the stabilizer of an element need not be a normal subgroup?
:::

::: {.solution}
<1>1. Let $G = S_3$ act on the set $\{1, 2, 3\}$ by the natural permutation action.
Proof: choose a concrete group action.

<1>2. The stabilizer of $1$ is $G_1 = \{e, (23)\}$.
Proof: the permutations fixing $1$ are the identity and the transposition $(23)$.

<1>3. $G_1$ is not normal in $S_3$.
<2>1. Conjugate $(23)$ by $(12)$: $(12)(23)(12)^{-1} = (13)$.
Proof: direct computation of the conjugate.
<2>2. $(13) \notin G_1$.
Proof: $(13)$ does not fix $1$.
<2>3. Hence $G_1$ is not closed under conjugation, so it is not normal.
Proof: <2>1 and <2>2.

<1>4. Therefore the stabilizer of an element need not be a normal subgroup.
Proof: <1>3 gives a counterexample.

<1>5. Q.E.D.
Proof: <1>4.
:::
