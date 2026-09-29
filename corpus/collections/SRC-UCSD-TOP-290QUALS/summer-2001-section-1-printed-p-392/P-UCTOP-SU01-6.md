---
schema: qual/card@1
id: P-UCTOP-SU01-6
kind: problem
title: Homotopy equivalence of CP^{2n} is orientation-preserving
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Show that any homotopy equivalence from $\mathbb{CP}^{2n}$ to itself is orientation-preserving, i.e. has degree +1. Is this true for $\mathbb{CP}^{2n+1}$?
:::

::: {.solution}

::: pf

::: pf-step
Let $x\in H^2(\mathbb{CP}^m;\mathbb Z)$ be the standard generator, so
$$
H^*(\mathbb{CP}^m;\mathbb Z)\cong\mathbb Z[x]/(x^{m+1}),
\qquad |x|=2.
$$

::: pf-proof
The top class $x^m$ is the cohomological orientation class for the complex orientation.
:::

:::

::: pf-step
If $f:\mathbb{CP}^m\to\mathbb{CP}^m$ is a homotopy equivalence, then
$$
f^*(x)=\varepsilon x
$$
for some $\varepsilon\in\{1,-1\}$.

::: pf-proof
A homotopy equivalence induces an automorphism of $H^2\cong\mathbb Z$, and the only automorphisms of $\mathbb Z$ are multiplication by $\pm1$.
:::

:::

::: {.pf-step #degree-formula}
The degree of $f$ is $\varepsilon^m$.

::: pf-proof
By multiplicativity of the cup product,
$$
f^*(x^m)=(f^*x)^m=(\varepsilon x)^m=\varepsilon^m x^m.
$$
The coefficient by which $f^*$ multiplies the top cohomology generator is the degree.
:::

:::

::: pf-step
For $m=2n$, every self-homotopy equivalence has degree $+1$.

::: pf-proof
By step [](#degree-formula){.pf-ref},
$$
\deg f=\varepsilon^{2n}=1.
$$
Thus every homotopy equivalence of $\mathbb{CP}^{2n}$ preserves orientation.
:::

:::

::: pf-step
The analogous statement is false for $\mathbb{CP}^{2n+1}$.

::: pf-proof
Complex conjugation
$$
[z_0:\cdots:z_{2n+1}]\longmapsto[\overline z_0:\cdots:\overline z_{2n+1}]
$$
is a homeomorphism and sends the degree-$2$ generator $x$ to $-x$. Hence by step [](#degree-formula){.pf-ref} its degree is
$$
(-1)^{2n+1}=-1.
$$
So it reverses orientation.
:::

:::

:::

:::

