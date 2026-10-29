---
schema: qual/card@1
id: P-ZNZ4X
kind: problem
title: The radical of an ideal is an ideal, and $I(Z(I))=\sqrt{I}$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $k$ be an algebraically closed field and $R=k[x_1,\ldots,x_n]$.
Define the "radical" of an ideal $I\trianglelefteq R$ and prove it is an ideal.
Prove that the ideal of all polynomials vanishing on the zero set of $I$ is $\sqrt{I}$.
:::

::: {.solution}
Let $Z(I)=\{a\in k^n:h(a)=0\text{ for every }h\in I\}$, and let $I(Z(I))$ be the ideal of polynomials vanishing on $Z(I)$.

::: pf

::: pf-step

The radical of $I$ is $\sqrt I\coloneqq\{f\in R:f^m\in I\text{ for some }m\ge1\}$, and it is an ideal.

::: pf-proof

Let $f^m\in I$, $g^n\in I$, and $r\in R$. Each term of the binomial expansion of $(f+g)^{m+n}$ is a multiple of $f^ig^{m+n-i}$, and either $i\ge m$ or $m+n-i>n$, so the term lies in $I$; hence $f+g\in\sqrt I$. Also $(rf)^m=r^mf^m\in I$, so $rf\in\sqrt I$, and $0\in\sqrt I$.

:::

:::

::: {.pf-step #easy}

$\sqrt I\subseteq I(Z(I))$.

::: pf-proof

If $f^m\in I$ and $a\in Z(I)$, then $f(a)^m=0$, so $f(a)=0$.

:::

:::

::: {.pf-step #hard}

$I(Z(I))\subseteq\sqrt I$.

::: pf-proof

Let $f\in I(Z(I))$; if $f=0$ there is nothing to prove. In $k[x_1,\ldots,x_n,y]$ consider $J=IR[y]+(1-yf)$. A common zero $(a,b)$ of $J$ would have $a\in Z(I)$, hence $f(a)=0$, and $1-bf(a)=0$, which is impossible. By the weak Nullstellensatz, $J=(1)$, so
$$
1=\sum_i a_ih_i+b(1-yf),\qquad h_i\in I,\ a_i,b\in k[x_1,\ldots,x_n,y].
$$
Apply the homomorphism $k[x_1,\ldots,x_n,y]\to R_f$ with $y\mapsto f^{-1}$; the last term vanishes and $1=\sum_i a_i(x,f^{-1})h_i$. Multiplying by a power $f^N$ that clears the denominators gives $f^N\in I$, so $f\in\sqrt I$.

:::

:::

::: pf-step

$\boxed{I(Z(I))=\sqrt I}$.

::: pf-proof

Combine steps [](#easy){.pf-ref} and [](#hard){.pf-ref}.

:::

:::

:::

:::
