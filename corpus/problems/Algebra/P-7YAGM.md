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

<1>1. One has $[K:F]\le2$.
::: {.proof}
The element $\zeta$ satisfies
\[
T^2-(\zeta+\zeta^{-1})T+1=0
\]
over $F$. Since $K=F(\zeta)$, this gives $[K:F]\le2$.
:::

<1>2. Complex conjugation is a nontrivial $F$-automorphism of $K$.
::: {.proof}
Complex conjugation sends $\zeta$ to $\zeta^{-1}$ and fixes $\zeta+\zeta^{-1}$, so it fixes $F$ pointwise. Because $n>2$, a primitive $n$th root of unity satisfies $\zeta\ne\zeta^{-1}$; otherwise $\zeta^2=1$, contradicting its order. Hence conjugation is nontrivial on $K$.
:::

<1>3. Therefore $[K:F]=2$.
::: {.proof}
By <1>2, $K/F$ has a nontrivial automorphism, so $K\ne F$. Combined with <1>1, this forces $[K:F]=2$.
:::

<1>4. The cyclotomic extension has degree $[K:\QQ]=\varphi(n)$.
::: {.proof}
The minimal polynomial of a primitive $n$th root of unity over $\QQ$ is the cyclotomic polynomial $\Phi_n$, whose degree is $\varphi(n)$.
:::

<1>5. Hence
\[
[F:\QQ]=\frac{\varphi(n)}2.
\]
::: {.proof}
The tower law gives
\[
\varphi(n)=[K:\QQ]=[K:F][F:\QQ]=2[F:\QQ].
\]
Dividing by $2$ gives the result.
:::
:::
