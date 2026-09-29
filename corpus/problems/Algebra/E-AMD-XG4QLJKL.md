---
schema: qual/card@1
id: E-AMD-XG4QLJKL
kind: problem
title: Localization at a prime ideal is a local ring
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Local Rings
  - Prime Ideals
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

::: {.exercise}
Show that localizing a ring at a prime ideal produces a local ring.
:::


::: {.solution}
Let $S=R\setminus\mathfrak p$, so $R_{\mathfrak p}=S^{-1}R$.

::: pf

::: {.pf-step #extension-proper}
The extended ideal $\mathfrak pR_{\mathfrak p}$ is proper.

::: pf-proof
Suppose $1\in\mathfrak pR_{\mathfrak p}$. Then $1=a/s$ for some $a\in\mathfrak p$ and $s\notin\mathfrak p$. Equality in the localization implies that for some $t\notin\mathfrak p$,
\[
t(s-a)=0.
\]
Hence $ts=ta\in\mathfrak p$. Since $\mathfrak p$ is prime while $t,s\notin\mathfrak p$, this is impossible. Thus $\mathfrak pR_{\mathfrak p}$ is proper.
:::

:::

::: {.pf-step #fraction-in-pRp-iff}
A fraction $a/s\in R_{\mathfrak p}$ lies in $\mathfrak pR_{\mathfrak p}$ if and only if $a\in\mathfrak p$.

::: pf-proof
If $a\in\mathfrak p$, then $a/s\in\mathfrak pR_{\mathfrak p}$. Conversely, suppose $a/s\in\mathfrak pR_{\mathfrak p}$. Then $a/s=b/u$ for some $b\in\mathfrak p$ and $u\notin\mathfrak p$. Thus for some $t\notin\mathfrak p$,
\[
t(au-bs)=0,
\]
so $tau=tbs\in\mathfrak p$. Since $t,u\notin\mathfrak p$ and $\mathfrak p$ is prime, it follows that $a\in\mathfrak p$.
:::

:::

::: {.pf-step #outside-pRp-is-unit}
Every element outside $\mathfrak pR_{\mathfrak p}$ is a unit.

::: pf-proof
Let $a/s\notin\mathfrak pR_{\mathfrak p}$. By step [](#fraction-in-pRp-iff){.pf-ref}, $a\notin\mathfrak p$, so $a\in S$. Therefore $s/a$ is a valid element of $R_{\mathfrak p}$ and
\[
\frac{a}{s}\frac{s}{a}=1.
\]
Thus $a/s$ is a unit.
:::

:::

::: pf-step
Therefore $R_{\mathfrak p}$ is local with unique maximal ideal $\mathfrak pR_{\mathfrak p}$.

::: pf-proof
By step [](#extension-proper){.pf-ref}, $\mathfrak pR_{\mathfrak p}$ is proper. By step [](#outside-pRp-is-unit){.pf-ref}, every element outside it is a unit. Hence every proper ideal is contained in $\mathfrak pR_{\mathfrak p}$, so this ideal is maximal and is the unique maximal ideal.
:::

:::

:::

:::
