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

::: pf

::: {.pf-step #s1}

If $g\in G$ is nonidentity, then
$$
H\subseteq\langle g\rangle.
$$

::: pf-proof

The cyclic subgroup $\langle g\rangle$ is nontrivial. By hypothesis, $H$ is
contained in every nontrivial subgroup of $G$, hence in $\langle g\rangle$.

:::

:::

::: {.pf-step #s2}

Every $h\in H$ commutes with every $g\in G$.

::: pf-proof

Fix $h\in H$. If $g=1$, then $hg=gh$ trivially. If $g\neq1$, step [](#s1){.pf-ref}
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

:::

::: {.pf-step #s3}

One has
$$
H\subseteq Z(G).
$$

::: pf-proof

By step [](#s2){.pf-ref}, every element of $H$ commutes with every element of $G$,
which is exactly the defining condition for membership in the center.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
