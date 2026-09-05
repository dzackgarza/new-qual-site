---
schema: qual/card@1
id: P-5JYOH
kind: problem
title: Classification of compact connected closed surfaces with $\chi(M)\ge -2$
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Spring 2007 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Applied the closed-surface classification together with chi(M_g)=2-2g and
    chi(N_k)=2-k. The inequality leaves orientable genera 0,1,2 and
    nonorientable genera 1,2,3,4. Hatcher, Algebraic Topology, Section 2.2,
    records these Euler-characteristic formulas.
---

::: problem
Describe the topological classification of all compact connected surfaces $M$ without boundary having Euler characteristic $\chi(M )\geq -2$.

No proof is required.
:::

::: {.solution}
By the classification theorem for compact connected surfaces without boundary, every such surface is homeomorphic to exactly one of the following types:

- an orientable surface $M_g$, the connected sum of $g$ tori, with
  \[
  \chi(M_g)=2-2g,
  \]
  where $g\ge0$;

- a nonorientable surface $N_k$, the connected sum of $k$ projective planes, with
  \[
  \chi(N_k)=2-k,
  \]
  where $k\ge1$.

<1>1. The orientable possibilities are
\[
M_0=S^2,
\qquad
M_1=T^2,
\qquad
M_2=T^2\#T^2.
\]
::: {.proof}
The inequality
\[
2-2g\ge-2
\]
is equivalent to $g\le2$.
Since $g\ge0$, one has $g=0,1,2$.
:::

<1>2. The nonorientable possibilities are
\[
N_1=\RP^2,
\qquad
N_2=K,
\qquad
N_3=\#^3\RP^2,
\qquad
N_4=\#^4\RP^2,
\]
where $K$ is the Klein bottle.
::: {.proof}
The inequality
\[
2-k\ge-2
\]
is equivalent to $k\le4$.
Since $k\ge1$, one has $k=1,2,3,4$.
:::

<1>3. These seven surfaces are exactly the required classification.
::: {.proof}
<1>1 and <1>2 exhaust the two alternatives in the classification theorem.
Orientability distinguishes the two families, and within each family the genus is a complete invariant.
:::
:::
