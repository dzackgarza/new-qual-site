---
schema: qual/card@1
id: P-BKF94-4
kind: problem
title: A subgroup contained in every nontrivial subgroup is central
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied the hypothesis to every nontrivial cyclic subgroup <g>; since
    H is contained in <g>, each element of H commutes with g.
---

::: {.problem}
Suppose a group $G$ has a nontrivial subgroup $H$ contained in every nontrivial subgroup of $G$. Prove that $H\subseteq Z(G)$.
:::

::: {.solution}
<1>1. If $g\in G$ is nonidentity, then
$$
H\subseteq\langle g\rangle.
$$

::: {.proof}
The cyclic subgroup $\langle g\rangle$ is nontrivial. By hypothesis, $H$ is
contained in every nontrivial subgroup of $G$, hence in $\langle g\rangle$.
:::

<1>2. Every $h\in H$ commutes with every $g\in G$.

::: {.proof}
Fix $h\in H$. If $g=1$, then $hg=gh$ trivially. If $g\neq1$, step <1>1
gives
$$
h\in\langle g\rangle.
$$
The cyclic group $\langle g\rangle$ is abelian, so
$$
hg=gh.
$$
Thus $h$ commutes with every element of $G$.
:::

<1>3. One has
$$
H\subseteq Z(G).
$$

::: {.proof}
By step <1>2, every element of $H$ commutes with every element of $G$,
which is exactly the defining condition for membership in the center.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
