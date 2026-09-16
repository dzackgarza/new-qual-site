---
schema: qual/card@1
id: P-RVG47
kind: problem
title: A Lie group with no faithful finite-dimensional representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Do you know a Lie group that has no faithful finite-dimensional representation?
:::

::: {.solution}
A standard example is the universal covering group
\[
G=\widetilde{\operatorname{SL}_2(\mathbb R)}.
\]
Let
\[
p:G\to\operatorname{SL}_2(\mathbb R)
\]
be the covering homomorphism. Its kernel is infinite cyclic and central:
\[
\ker p\cong\pi_1(\operatorname{SL}_2(\mathbb R))\cong\mathbb Z.
\]

Let $\rho:G\to\operatorname{GL}(V)$ be a finite-dimensional continuous representation. Its differential
\[
d\rho:\mathfrak{sl}_2(\mathbb R)\to\mathfrak{gl}(V)
\]
complexifies to a finite-dimensional representation of $\mathfrak{sl}_2(\mathbb C)$. Every such representation integrates to the simply connected complex group $\operatorname{SL}_2(\mathbb C)$. Restricting the resulting group representation to the real subgroup $\operatorname{SL}_2(\mathbb R)$ and then pulling back along $p$ gives a representation of $G$ with differential $d\rho$.

Because $G$ is connected and simply connected, a finite-dimensional Lie-group representation is uniquely determined by its differential. Hence $\rho$ is exactly that pullback. Therefore
\[
\ker p\subseteq\ker\rho.
\]
Since $\ker p\ne1$, no finite-dimensional representation of $G$ is faithful.

Thus
\[
\boxed{\widetilde{\operatorname{SL}_2(\mathbb R)}}
\]
is a connected Lie group with no faithful finite-dimensional representation.
:::
