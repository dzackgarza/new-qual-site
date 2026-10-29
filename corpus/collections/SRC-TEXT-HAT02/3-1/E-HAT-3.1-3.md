---
schema: qual/card@1
id: E-HAT-3.1-3
kind: problem
title: $\operatorname{Ext}^n_{\ZZ_4}(\ZZ_2,\ZZ_2)$ is nonzero for all $n$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the resolution and Hom-complex calculations directly from the definitions.
---

::: {.problem}
Regarding $\ZZ_2$ as a module over the ring $\ZZ_4$, construct a resolution of $\ZZ_2$ by free modules over $\ZZ_4$ and use this to show that $\operatorname{Ext}_{\ZZ_4}^n(\ZZ_2, \ZZ_2)$ is nonzero for all $n$.
:::

::: {.solution}
Regard $\ZZ_2$ as the quotient $\ZZ_4/(2)$. Consider the periodic free resolution
$$
\cdots\xrightarrow{\,2\,}\ZZ_4
\xrightarrow{\,2\,}\ZZ_4
\xrightarrow{\,2\,}\ZZ_4
\longrightarrow\ZZ_2\longrightarrow0.
$$

::: pf

::: pf-step

This sequence is exact.

::: pf-proof

For multiplication by $2$ on $\ZZ_4$,
$$
\ker(\times2)=\{0,2\}=\operatorname{im}(\times2).
$$
At the right end, the quotient map $\ZZ_4\to\ZZ_2$ has kernel $\{0,2\}$, again the image of multiplication by $2$. Every term before $\ZZ_2$ is free over $\ZZ_4$, so this is a free resolution.

:::

:::

::: {.pf-step #s2}

Applying $\operatorname{Hom}_{\ZZ_4}(-,\ZZ_2)$ gives the cochain complex
$$
0\longrightarrow\ZZ_2\xrightarrow{0}\ZZ_2
\xrightarrow{0}\ZZ_2\xrightarrow{0}\cdots .
$$

::: pf-proof

For every degree,
$$
\operatorname{Hom}_{\ZZ_4}(\ZZ_4,\ZZ_2)\cong\ZZ_2
$$
by evaluation at $1$. The coboundary is precomposition with multiplication by $2$. If $\varphi:\ZZ_4\to\ZZ_2$ is $\ZZ_4$-linear, then
$$
(\varphi\circ\times2)(1)=\varphi(2)=2\varphi(1)=0
$$
in the $\ZZ_4$-module $\ZZ_2$. Hence every coboundary is zero.

:::

:::

::: pf-step

Therefore
$$
\boxed{\operatorname{Ext}_{\ZZ_4}^{\,n}(\ZZ_2,\ZZ_2)\cong\ZZ_2}
$$
for every $n\ge0$.

::: pf-proof

The cohomology of the zero-differential cochain complex in step [](#s2){.pf-ref} is one copy of $\ZZ_2$ in each degree.

:::

:::

:::

In particular these Ext groups are nonzero in every degree.
:::
