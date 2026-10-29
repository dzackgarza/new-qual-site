---
schema: qual/card@1
id: P-XT3LV
kind: problem
title: $[\QQ(\zeta+\zeta^{-1}):\QQ]=\varphi(n)/2$ for a primitive $n$th root of unity
  $\zeta$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

::: {.problem}
Let $n>2$ and let $\zeta_n$ be a primitive $n$th root of unity. Prove
$$
[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]
=\frac{\varphi(n)}2.
$$
:::

::: {.solution}
Regard $\zeta_n$ as a complex number, and let $K=\QQ(\zeta_n+\zeta_n^{-1})$.

::: pf

::: {.pf-step #upper}
$[\QQ(\zeta_n):K]\le2$.

::: pf-proof
$\zeta_n$ is a root of $x^2-(\zeta_n+\zeta_n^{-1})x+1\in K[x]$.
:::

:::

::: {.pf-step #proper}
$[\QQ(\zeta_n):K]=2$.

::: pf-proof
Since $\abs{\zeta_n}=1$, we have $\zeta_n^{-1}=\overline{\zeta_n}$, so $\zeta_n+\zeta_n^{-1}=2\operatorname{Re}\zeta_n\in\RR$ and $K\subseteq\RR$.
Because $n>2$, the only real roots of unity $\pm1$ are not primitive $n$th roots, so $\zeta_n\notin\RR$ and $\zeta_n\notin K$.
Combine with step [](#upper){.pf-ref}.
:::

:::

::: pf-step
$[K:\QQ]=\varphi(n)/2$.

::: pf-proof
The cyclotomic degree is $[\QQ(\zeta_n):\QQ]=\varphi(n)$, so by the tower law and step [](#proper){.pf-ref}, $\varphi(n)=[\QQ(\zeta_n):K][K:\QQ]=2[K:\QQ]$.
:::

:::

:::

:::
