---
schema: qual/card@1
id: P-ZXWFU
kind: problem
title: Maximal real subfield of $\QQ(\zeta_n)$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the maximal real subfield in a cyclotomic extension $\QQ(\zeta_n)/\QQ$?
:::

::: {.solution}
Let $\zeta_n=e^{2\pi i/n}$, $K=\QQ(\zeta_n)\subset\CC$, and $n>2$; for $n=1,2$, $K=\QQ$ is already real. Complex conjugation $c$ restricts to the automorphism $\zeta_n\mapsto\zeta_n^{-1}$ of $K$.

::: pf

::: {.pf-step #fixed}

The maximal real subfield of $K$ is $K^+\coloneqq K\cap\RR=K^{\langle c\rangle}$, and $[K:K^+]=2$.

::: pf-proof

An element of $K$ is real exactly when $c$ fixes it. Since $n>2$, $\zeta_n\notin\RR$, so $c\ne1$ on $K$ and $\langle c\rangle$ has order $2$.

:::

:::

::: pf-step

$K^+=\boxed{\QQ(\zeta_n+\zeta_n^{-1})}$, and $[K^+:\QQ]=\varphi(n)/2$.

::: pf-proof

$\zeta_n+\zeta_n^{-1}=2\cos(2\pi/n)$ is real, so $F\coloneqq\QQ(\zeta_n+\zeta_n^{-1})\subseteq K^+$. Since $\zeta_n$ is a root of $x^2-(\zeta_n+\zeta_n^{-1})x+1\in F[x]$, $[K:F]\le2$. By step [](#fixed){.pf-ref}, $[K:K^+]=2$, so $F=K^+$, and $[K^+:\QQ]=[K:\QQ]/2=\varphi(n)/2$.

:::

:::

::: pf-step

$\Gal(K^+/\QQ)\cong(\ZZ/n\ZZ)^\times/\{\pm1\}$.

::: pf-proof

Under $\Gal(K/\QQ)\cong(\ZZ/n\ZZ)^\times$, $a\mapsto(\zeta_n\mapsto\zeta_n^a)$, the conjugation $c$ corresponds to $-1$. The group is abelian, so $\langle c\rangle$ is normal and $\Gal(K^+/\QQ)\cong\Gal(K/\QQ)/\langle c\rangle$.

:::

:::

:::

:::
