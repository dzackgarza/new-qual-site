---
schema: qual/card@1
id: P-Z6MHZ
kind: problem
title: Kummer extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
What is a Kummer extension?
:::

::: {.solution}
Let $K$ be a field, let $n\ge2$ be an integer with $\operatorname{char}K\nmid n$, and suppose $K$ contains the group $\mu_n$ of $n$th roots of unity. For $a\in K^\times$, write $\sqrt[n]{a}$ for a chosen root of $x^n-a$ in an algebraic closure of $K$.

::: pf

::: pf-step

A Kummer extension of exponent dividing $n$ is a finite extension of the form $L=K\bigl(\sqrt[n]{a_1},\ldots,\sqrt[n]{a_r}\bigr)$ with $a_1,\ldots,a_r\in K^\times$.

:::

::: {.pf-step #galois}

Such an extension $L/K$ is Galois.

::: pf-proof

The roots of $x^n-a_i$ are $\zeta\sqrt[n]{a_i}$ for $\zeta\in\mu_n\subseteq K$, so each $x^n-a_i$ splits over $L$, and $L$ is the splitting field of $\prod_i(x^n-a_i)$; hence $L/K$ is normal. Since $\operatorname{char}K\nmid n$ and $a_i\ne0$, the derivative $nx^{n-1}$ shares no root with $x^n-a_i$, so these polynomials are separable and $L/K$ is Galois.

:::

:::

::: pf-step

$\operatorname{Gal}(L/K)$ is abelian of exponent dividing $n$.

::: pf-proof

By step [](#galois){.pf-ref}, every $\sigma\in\operatorname{Gal}(L/K)$ sends $\sqrt[n]{a_i}$ to another root of $x^n-a_i$, so $\sigma\bigl(\sqrt[n]{a_i}\bigr)=\zeta_i(\sigma)\sqrt[n]{a_i}$ with $\zeta_i(\sigma)\in\mu_n$. Since $\mu_n\subseteq K$ is fixed by $\sigma$, the map $\sigma\mapsto(\zeta_i(\sigma))_i$ is a homomorphism $\operatorname{Gal}(L/K)\to\mu_n^r$, and it is injective because the $\sqrt[n]{a_i}$ generate $L$. A subgroup of $\mu_n^r$ is abelian of exponent dividing $n$.

:::

:::

::: pf-step

Conversely, every finite abelian Galois extension $L/K$ whose Galois group has exponent dividing $n$ is a Kummer extension of exponent dividing $n$.

::: pf-proof

This is the main theorem of Kummer theory, under the same hypotheses on $K$.

:::

:::

:::

:::
