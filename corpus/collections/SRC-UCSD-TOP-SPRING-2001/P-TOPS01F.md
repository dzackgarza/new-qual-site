---
schema: qual/card@1
id: P-TOPS01F
kind: problem
title: "Every self-homotopy equivalence of CP^{2n} is orientation-preserving"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Projective Spaces
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(1) Show that any self-homotopy equivalence $f: \mathbb{CP}^{2n} \to \mathbb{CP}^{2n}$ is orientation-preserving, i.e. has degree $+1$.
(2) Is this necessarily true for $\mathbb{CP}^{2n+1}$?
:::

::: {.solution}

::: pf

::: pf-step
For every $m\ge1$,
$$
H^*(\mathbb{CP}^m;\mathbb Z)
\cong \mathbb Z[x]/(x^{m+1}),
\qquad |x|=2,
$$
and $x^m$ generates the top cohomology $H^{2m}(\mathbb{CP}^m;\mathbb Z)$.
:::

::: pf-step
Let $f:\mathbb{CP}^m\to\mathbb{CP}^m$ be a homotopy equivalence.

::: pf-proof

::: pf-step
Since $f^*:H^2\to H^2$ is an automorphism of $\mathbb Z$, there is an $\varepsilon\in\{\pm1\}$ such that
$$
f^*(x)=\varepsilon x.
$$
:::

::: pf-step
Therefore
$$
f^*(x^m)=(f^*x)^m=\varepsilon^m x^m.
$$
By the definition of degree, this means
$$
\deg(f)=\varepsilon^m.
$$
:::

:::

:::

::: pf-step
For $m=2n$, the exponent is even, so
$$
\deg(f)=\varepsilon^{2n}=1.
$$
Thus every self-homotopy equivalence of $\mathbb{CP}^{2n}$ preserves orientation.
:::

::: pf-step
The analogous statement is false for $\mathbb{CP}^{2n+1}$.

::: pf-proof

::: pf-step
Complex conjugation
$$
c([z_0:\cdots:z_{2n+1}])=[\overline z_0:\cdots:\overline z_{2n+1}]
$$
is a homeomorphism and satisfies $c^*(x)=-x$.
:::

::: pf-step
Hence
$$
\deg(c)=(-1)^{2n+1}=-1,
$$
so $c$ is an orientation-reversing self-homotopy equivalence.
:::

:::

:::

:::
:::
