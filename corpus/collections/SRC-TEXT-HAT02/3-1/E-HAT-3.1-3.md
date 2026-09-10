---
schema: qual/card@1
id: E-HAT-3.1-3
kind: problem
title: Hatcher Section 3.1 Exercise 3
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

# E-HAT-3.1-3

Regarding $\mathbb{Z}_2$ as a module over the ring $\mathbb{Z}_4$, construct a resolution of $\mathbb{Z}_2$ by free modules over $\mathbb{Z}_4$ and use this to show that $\operatorname{Ext}_{\mathbb{Z}_4}^n(\mathbb{Z}_2, \mathbb{Z}_2)$ is nonzero for all $n$.

::: {.solution}
Regard $\mathbb Z_2$ as the quotient $\mathbb Z_4/(2)$. Consider the periodic free resolution
\[
\cdots\xrightarrow{\,2\,}\mathbb Z_4
\xrightarrow{\,2\,}\mathbb Z_4
\xrightarrow{\,2\,}\mathbb Z_4
\longrightarrow\mathbb Z_2\longrightarrow0.
\]

<1>1. This sequence is exact.
::: {.proof}
For multiplication by $2$ on $\mathbb Z_4$,
\[
\ker(\times2)=\{0,2\}=\operatorname{im}(\times2).
\]
At the right end, the quotient map $\mathbb Z_4\to\mathbb Z_2$ has kernel $\{0,2\}$, again the image of multiplication by $2$. Every term before $\mathbb Z_2$ is free over $\mathbb Z_4$, so this is a free resolution.
:::

<1>2. Applying $\operatorname{Hom}_{\mathbb Z_4}(-,\mathbb Z_2)$ gives the cochain complex
\[
0\longrightarrow\mathbb Z_2\xrightarrow{0}\mathbb Z_2
\xrightarrow{0}\mathbb Z_2\xrightarrow{0}\cdots .
\]
::: {.proof}
For every degree,
\[
\operatorname{Hom}_{\mathbb Z_4}(\mathbb Z_4,\mathbb Z_2)\cong\mathbb Z_2
\]
by evaluation at $1$. The coboundary is precomposition with multiplication by $2$. If $\varphi:\mathbb Z_4\to\mathbb Z_2$ is $\mathbb Z_4$-linear, then
\[
(\varphi\circ\times2)(1)=\varphi(2)=2\varphi(1)=0
\]
in the $\mathbb Z_4$-module $\mathbb Z_2$. Hence every coboundary is zero.
:::

<1>3. Therefore
\[
\boxed{\operatorname{Ext}_{\mathbb Z_4}^{\,n}(\mathbb Z_2,\mathbb Z_2)\cong\mathbb Z_2}
\]
for every $n\ge0$.
::: {.proof}
The cohomology of the zero-differential cochain complex in <1>2 is one copy of $\mathbb Z_2$ in each degree.
:::

In particular these Ext groups are nonzero in every degree.
:::
