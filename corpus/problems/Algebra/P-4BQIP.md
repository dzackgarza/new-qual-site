---
schema: qual/card@1
id: P-4BQIP
kind: problem
title: Groups of order $p^3$ are abelian or have $|Z(G)|=p$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group of order $p^3$ for some prime $p$.
Show that either $G$ is abelian, or $\left| Z(G) \right| = p$.
:::

::: {.solution}
Let $|G|=p^3$.

::: pf

::: {.pf-step #s1}

The center $Z(G)$ is nontrivial.

::: pf-proof

Every finite $p$-group has nontrivial center, by the class equation. Hence
\[
|Z(G)|\in\{p,p^2,p^3\}.
\]

:::

:::

::: {.pf-step #s2}

If $|Z(G)|=p^3$, then $G$ is abelian.

::: pf-proof

Then $Z(G)=G$, which is exactly the definition of an abelian group.

:::

:::

::: {.pf-step #s3}

If $|Z(G)|=p^2$, then $G/Z(G)$ is cyclic.

::: pf-proof

Its order is
\[
|G/Z(G)|=p,
\]
so it is cyclic.

:::

:::

::: {.pf-step #s4}

If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: pf-proof

Suppose $G/Z(G)=\langle gZ(G)\rangle$. Every element of $G$ can then be written as $g^a z$ with $z\in Z(G)$. For
\[
x=g^a z_1,\qquad y=g^b z_2,
\]
we have
\[
xy=g^{a+b}z_1z_2=g^{a+b}z_2z_1=yx,
\]
because $z_1,z_2$ are central. Thus all elements commute.

:::

:::

::: pf-step

Therefore either $G$ is abelian or $|Z(G)|=p$.

::: pf-proof

If $|Z(G)|=p^3$, use step [](#s2){.pf-ref}. If $|Z(G)|=p^2$, use steps [](#s3){.pf-ref} and [](#s4){.pf-ref}. Hence a nonabelian group cannot have center of order $p^2$ or $p^3$. By step [](#s1){.pf-ref} its center is nontrivial, so the only remaining possibility is
\[
|Z(G)|=p.
\]

:::

:::

:::

:::
