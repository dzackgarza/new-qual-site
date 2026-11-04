---
schema: qual/card@1
id: P-Q73UJ
kind: problem
title: A module vanishes if and only if all its localizations at maximal ideals vanish, and a nonzero module over a local ring with $M/\mathfrak mM=0$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $R$ be a commutative ring and $M$ be an $R$-module.

(a) Show that $M=0$ if and only if the localization $M_{\mathfrak m}=0$ for all maximal ideals $\mathfrak m$ of $R$.

(b) Find an example of a local ring $R$ with maximal ideal $\mathfrak m$ and a nonzero $R$-module $M$ such that $M/\mathfrak mM=0$.
:::

::: {.solution}
For an element $x\in M$ write $\operatorname{Ann}(x)=\{r\in R:rx=0\}$, an ideal of $R$; an element $x/1$ of $M_{\mathfrak m}$ vanishes exactly when $sx=0$ for some $s\notin\mathfrak m$.

::: pf

::: {.pf-step #part-a}
(a) $M=0$ if and only if $M_{\mathfrak m}=0$ for every maximal ideal $\mathfrak m$.

::: pf-proof
If $M=0$ then every localization is $0$.
Conversely suppose $M\ne0$ and choose $0\ne x\in M$.
Its annihilator is a proper ideal, since $1\notin\operatorname{Ann}(x)$, so it is contained in some maximal ideal $\mathfrak m$.
If $x/1=0$ in $M_{\mathfrak m}$ there would be $s\notin\mathfrak m$ with $sx=0$, that is $s\in\operatorname{Ann}(x)\subseteq\mathfrak m$, a contradiction; hence $x/1\ne0$ and $M_{\mathfrak m}\ne0$.
:::

:::

::: {.pf-step #part-b}
(b) $R=\ZZ_{(2)}$ with maximal ideal $\mathfrak m=2\ZZ_{(2)}$ and $M=\QQ$ is a nonzero module with $M/\mathfrak mM=0$.

::: pf-proof
The ring $\ZZ_{(2)}$ is local with maximal ideal $\mathfrak m=(2)$, and $\QQ$ is a module over it because $\ZZ_{(2)}\subseteq\QQ$.
The element $2$ is invertible in $\QQ$, so $\mathfrak m\QQ=\QQ$: every $q\in\QQ$ is $2\cdot\frac q2$ with $\frac q2\in\QQ$.
Hence $M/\mathfrak mM=\QQ/\QQ=0$, while $M=\QQ\ne0$.
:::

:::

:::
:::
