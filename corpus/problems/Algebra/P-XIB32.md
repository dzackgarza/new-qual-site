---
schema: qual/card@1
id: P-XIB32
kind: problem
title: Field homomorphisms from $\QQ(\alpha)$ into $\CC$, $\RR$, and $\overline{\QQ}$
  for a root $\alpha$ of $x^{17}-2$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
---

::: {.problem}
Suppose that $\alpha$ is a root in $\CC$ of $P(x) = x^{17} - 2$.
How many field homomorphisms are there from $\QQ (\alpha)$ to:

(a) $\CC$,

(b) $\RR$,

(c) $\overline{\QQ}$, the algebraic closure of $\QQ$?
:::

::: {.solution}

The polynomial $P$ is irreducible over $\QQ$ by Eisenstein's criterion at $2$, so it is the minimal polynomial of $\alpha$ and $[\QQ(\alpha):\QQ]=17$. Since the characteristic is $0$, $P$ is separable. A field homomorphism fixes the prime field $\QQ$, so a homomorphism from $\QQ(\alpha)\cong\QQ[x]/(P)$ into a field $L$ of characteristic $0$ is determined by the image of $\alpha$, which may be any root of $P$ in $L$.

::: pf

::: pf-step

(a) There are $\boxed{17}$ homomorphisms into $\CC$.

::: pf-proof

$\CC$ is algebraically closed, so it contains all $17$ distinct roots of $P$.

:::

:::

::: pf-step

(b) There is $\boxed{1}$ homomorphism into $\RR$.

::: pf-proof

The function $x\mapsto x^{17}$ is strictly increasing on $\RR$, so $P$ has exactly one real root, $2^{1/17}$.

:::

:::

::: pf-step

(c) There are $\boxed{17}$ homomorphisms into $\overline{\QQ}$.

::: pf-proof

$\overline{\QQ}$ is algebraically closed of characteristic $0$, so it contains all $17$ distinct roots of $P$.

:::

:::

:::

:::
