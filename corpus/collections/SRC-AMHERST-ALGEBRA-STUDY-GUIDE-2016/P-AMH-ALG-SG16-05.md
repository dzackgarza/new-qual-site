---
schema: qual/card@1
id: P-AMH-ALG-SG16-05
kind: problem
title: Subgroups containing all commutators are normal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Suppose that $H\subseteq G$ is a subgroup with the property that for every $x,y\in G$, we have $xyx^{-1}y^{-1}\in H$.
Prove that $H$ is a normal subgroup of $G$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
Conjugates of elements of $H$ remain in $H$.

::: pf-proof
Let
$$
g\in G,
\qquad
h\in H.
$$
By hypothesis, the commutator
$$
ghg^{-1}h^{-1}
$$
lies in $H$. Since also $h\in H$ and $H$ is closed under multiplication,
$$
(ghg^{-1}h^{-1})h=ghg^{-1}\in H.
$$
Thus every conjugate of every element of $H$ lies in $H$.
:::

:::

::: pf-step
Therefore
$$
\boxed{H\trianglelefteq G}.
$$

::: pf-proof
Step [](#s1-1){.pf-ref} shows that
$$
gHg^{-1}\subseteq H
$$
for every $g\in G$. Replacing $g$ by $g^{-1}$ gives the reverse inclusion, so
$$
gHg^{-1}=H
$$
for every $g\in G$.
:::

:::

:::

:::
