---
schema: qual/card@1
id: P-7YAGM
kind: problem
title: $[\QQ(\zeta+\zeta^{-1}):\QQ]=\phi(n)/2$
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $n>2$ and let $\zeta$ be a primitive $n$th root of unity. Prove that
\[
[\QQ(\zeta+\zeta^{-1}):\QQ]=\frac{\varphi(n)}2.
\]
:::

::: {.solution}
Set
\[
K=\QQ(\zeta),\qquad F=\QQ(\zeta+\zeta^{-1}).
\]

::: pf

::: {.pf-step #s1}

One has $[K:F]\le2$.

::: pf-proof

The element $\zeta$ satisfies
\[
T^2-(\zeta+\zeta^{-1})T+1=0
\]
over $F$. Since $K=F(\zeta)$, this gives $[K:F]\le2$.

:::

:::

::: {.pf-step #s2}

Complex conjugation is a nontrivial $F$-automorphism of $K$.

::: pf-proof

Complex conjugation sends $\zeta$ to $\zeta^{-1}$ and fixes $\zeta+\zeta^{-1}$, so it fixes $F$ pointwise. Because $n>2$, a primitive $n$th root of unity satisfies $\zeta\ne\zeta^{-1}$; otherwise $\zeta^2=1$, contradicting its order. Hence conjugation is nontrivial on $K$.

:::

:::

::: pf-step

Therefore $[K:F]=2$.

::: pf-proof

By step [](#s2){.pf-ref}, $K/F$ has a nontrivial automorphism, so $K\ne F$. Combined with step [](#s1){.pf-ref}, this forces $[K:F]=2$.

:::

:::

::: pf-step

The cyclotomic extension has degree $[K:\QQ]=\varphi(n)$.

::: pf-proof

The minimal polynomial of a primitive $n$th root of unity over $\QQ$ is the cyclotomic polynomial $\Phi_n$, whose degree is $\varphi(n)$.

:::

:::

::: pf-step

Hence
\[
[F:\QQ]=\frac{\varphi(n)}2.
\]

::: pf-proof

The tower law gives
\[
\varphi(n)=[K:\QQ]=[K:F][F:\QQ]=2[F:\QQ].
\]
Dividing by $2$ gives the result.

:::

:::

:::

:::
