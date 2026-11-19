---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW3
kind: problem
title: Reduced versus non-reduced homology
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
What is the difference between the reduced homology and (non-reduced) homology?
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Ordinary singular homology is the homology of the complex $\cdots\to C_{1}(X)\xrightarrow{\partial_{1}}C_{0}(X)\to0$.

::: pf

::: {.pf-step #augmentation}
$\varepsilon\colon C_{0}(X)\to\ZZ$, $\varepsilon(\sum n_{i}x_{i})=\sum n_{i}$, is a chain map to the complex $\ZZ$ concentrated in degree $0$, so
$$
\cdots\to C_{1}(X)\xrightarrow{\partial_{1}}C_{0}(X)\xrightarrow{\varepsilon}\ZZ\to0
$$
is a chain complex.

::: pf-proof
A chain map requires $\varepsilon\partial_{1}=0$. A basis element of $C_{1}(X)$ is a singular $1$-simplex $\sigma\colon\Delta^{1}\to X$, and $\partial_{1}\sigma=\sigma(e_{1})-\sigma(e_{0})$ as a $0$-chain, whose image under $\varepsilon$ is $1-1=0$. Since $\partial_{1}$ is linear, $\varepsilon\partial_{1}=0$ on all of $C_{1}(X)$.
:::

:::

::: {.pf-step #define}
$\widetilde H_{n}(X)$ is the $n$-th homology of the augmented complex, and there is a long exact sequence
$$
\cdots\to \widetilde H_{n}(X)\to H_{n}(X)\to H_{n}(\ZZ)\to\widetilde H_{n-1}(X)\to\cdots
$$

::: pf-proof
The augmented complex is the mapping cone of the chain map $\varepsilon$ regarded as a map from $C_{*}(X)$ to the complex $\ZZ$ in degree $0$; homology of the cone sits in the long exact sequence of the pair (cone, base), giving the displayed sequence, where $H_{n}(\ZZ)$ is $\ZZ$ for $n=0$ and $0$ otherwise. This is the standard construction of reduced homology via the augmentation.
:::

:::

::: {.pf-step #higher}
$\widetilde H_{n}(X)\cong H_{n}(X)$ for $n\geq1$.

::: pf-proof
In the sequence of step [](#define){.pf-ref} the group $H_{n}(\ZZ)$ vanishes for $n\geq1$, so the terms
$$
\widetilde H_{n}(X)\to H_{n}(X)\to 0\quad\text{and}\quad 0\to\widetilde H_{n}(X)\to H_{n}(X)
$$
make the map an isomorphism for $n\geq1$.
:::

:::

::: {.pf-step #degreezero}
For $n=0$ the sequence reads $0\to\widetilde H_{0}(X)\to H_{0}(X)\xrightarrow{\ \varepsilon_{*}\ }\ZZ\to\widetilde H_{-1}(X)=0$, so $H_{0}(X)\cong\widetilde H_{0}(X)\oplus\ZZ$ when $X\neq\varnothing$.

::: pf-proof
$\widetilde H_{-1}=0$ by definition, so $\varepsilon_{*}\colon H_{0}(X)\to\ZZ$ is surjective; it is split by $\ZZ\to H_{0}(X)$, $1\mapsto$ the class of a point $x_{0}\in X$, which is defined when $X$ is nonempty and satisfies $\varepsilon_{*}[\{x_{0}\}]=1$. A surjection split by a section exhibits the source as the direct sum of the kernel and the image of the section.
:::

:::

::: {.pf-step #components}
If $X$ has $c$ path components ($c\geq1$), then $H_{0}(X)\cong\ZZ^{c}$ and $\widetilde H_{0}(X)\cong\ZZ^{c-1}$; in particular the reduced homology of a point vanishes in every degree.

::: pf-proof
$H_{0}(X)$ is free on the path components of $X$, so $H_{0}(X)\cong\ZZ^{c}$; then step [](#degreezero){.pf-ref} gives $\widetilde H_{0}(X)\cong\ZZ^{c-1}$. For $X$ a point, $c=1$ and $\widetilde H_{0}=0$, and the higher groups vanish by step [](#higher){.pf-ref} since $H_{n}(\mathrm{pt})=0$ for $n\geq1$.
:::

:::

::: {.pf-step}
Reduced and ordinary homology agree in positive degrees and differ by one copy of $\ZZ$ in degree $0$ for nonempty spaces.

::: pf-proof
Steps [](#higher){.pf-ref}, [](#degreezero){.pf-ref} and [](#components){.pf-ref}. The difference is exactly the summand recording the class of a point, which reduced homology discards.
:::

:::

:::

:::
