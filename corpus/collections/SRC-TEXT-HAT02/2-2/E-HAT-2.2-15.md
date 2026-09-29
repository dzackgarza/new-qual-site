---
schema: qual/card@1
id: E-HAT-2.2-15
kind: problem
title: $H_n(X^n)$ is free as kernel of cellular boundary map
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
  - Cellular Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 15; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked via cellular homology, covering spaces, and degree.
---

::: {.problem}
Show that if $X$ is a CW complex then $H_n(X^n)$ is free by identifying it with the kernel of the cellular boundary map $H_n(X^n, X^{n-1}) \to H_{n-1}(X^{n-1}, X^{n-2})$.
:::

::: {.solution}
Consider the cellular boundary map
\[
d_n:
H_n(X^n,X^{n-1})
\longrightarrow
H_{n-1}(X^{n-1},X^{n-2}).
\]
It is the composite of the connecting map for $(X^n,X^{n-1})$ with the natural map into the relative group:
\[
H_n(X^n,X^{n-1})
\xrightarrow{\partial}
H_{n-1}(X^{n-1})
\xrightarrow{j}
H_{n-1}(X^{n-1},X^{n-2}).
\]

::: pf

::: {.pf-step #s1}

The map
\[
j:H_{n-1}(X^{n-1})\to H_{n-1}(X^{n-1},X^{n-2})
\]
is injective.

::: pf-proof

The long exact sequence of the pair $(X^{n-1},X^{n-2})$ contains
\[
H_{n-1}(X^{n-2})
\longrightarrow H_{n-1}(X^{n-1})
\xrightarrow{j}H_{n-1}(X^{n-1},X^{n-2}).
\]
Since $X^{n-2}$ has dimension at most $n-2$,
\[
H_{n-1}(X^{n-2})=0.
\]
Thus $j$ is injective.

:::

:::

::: {.pf-step #s2}

The natural map
\[
H_n(X^n)\to H_n(X^n,X^{n-1})
\]
is injective and identifies $H_n(X^n)$ with $\ker d_n$.

::: pf-proof

The long exact sequence of $(X^n,X^{n-1})$ begins in this range as
\[
0=H_n(X^{n-1})
\longrightarrow H_n(X^n)
\longrightarrow H_n(X^n,X^{n-1})
\xrightarrow{\partial}H_{n-1}(X^{n-1}).
\]
Hence $H_n(X^n)$ injects into the relative group with image $\ker\partial$. By step [](#s1){.pf-ref}, $j$ is injective, so
\[
\ker d_n=\ker(j\partial)=\ker\partial.
\]
Therefore
\[
\boxed{H_n(X^n)\cong\ker d_n.}
\]

:::

:::

::: pf-step

The group $H_n(X^n)$ is free abelian.

::: pf-proof

The relative group
\[
H_n(X^n,X^{n-1})
\]
is free abelian with basis the $n$-cells of $X$. By step [](#s2){.pf-ref}, $H_n(X^n)$ is a subgroup of this free abelian group. Every subgroup of a free abelian group is free abelian. Hence $H_n(X^n)$ is free.

:::

:::

:::

:::
