---
schema: qual/card@1
id: P-3BNEC
kind: problem
title: Algebraic, normal, and separable extensions over intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: problem
Let $K\subseteq E\subseteq F$. If $F/K$ is algebraic, normal, or separable, respectively, must $F/E$ have the same property? Answer this question in each of the three cases.
:::

::: {.solution}
All three answers are yes.

<1>1. Algebraicity passes from $F/K$ to $F/E$.
::: {.proof}
Let $\alpha\in F$. Since $F/K$ is algebraic, some nonzero $f\in K[x]$ satisfies $f(\alpha)=0$. Because $K\subseteq E$, the same polynomial lies in $E[x]$. Hence $\alpha$ is algebraic over $E$.
:::

<1>2. Separability passes from $F/K$ to $F/E$.
::: {.proof}
Let $p_K$ and $p_E$ be the minimal polynomials of $\alpha\in F$ over $K$ and $E$. Since $p_K(\alpha)=0$, minimality over $E$ gives
\[
p_E\mid p_K
\]
in $E[x]$. If $F/K$ is separable, then $p_K$ has no repeated roots, so neither does its divisor $p_E$. Thus $F/E$ is separable.
:::

<1>3. Normality passes from $F/K$ to $F/E$.
::: {.proof}
With the same notation, $p_E\mid p_K$ in $E[x]$. If $F/K$ is normal, then $p_K$ splits completely over $F$. Hence $p_E$ also splits completely over $F$. Therefore every minimal polynomial over $E$ of an element of $F$ splits in $F$, so $F/E$ is normal.
:::
:::
