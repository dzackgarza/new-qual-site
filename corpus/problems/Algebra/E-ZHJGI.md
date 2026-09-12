---
schema: qual/card@1
id: E-ZHJGI
kind: problem
title: $[\mathbb{Q}(\zeta_{n}+\zeta_{n}^{-1}):\mathbb{Q}]=\varphi(n)/2$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Number Theory
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

::: problem
22. For $n>2$, let $\zeta_n$ be a primitive $n$th root of unity. Prove that
\[
[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]=\frac{1}{2}\varphi(n),
\]
where $\varphi$ is Euler's totient function.
:::


::: {.solution}
Set
\[
K=\QQ(\zeta_n),
\qquad
F=\QQ(\zeta_n+\zeta_n^{-1}).
\]

<1>1. One has $[K:F]\le2$.
::: {.proof}
Put
\[
a=\zeta_n+\zeta_n^{-1}\in F.
\]
Then $\zeta_n$ satisfies
\[
T^2-aT+1=0
\]
over $F$, because
\[
\zeta_n^2-a\zeta_n+1
=\zeta_n^2-(\zeta_n+\zeta_n^{-1})\zeta_n+1=0.
\]
Since $K=F(\zeta_n)$, it follows that $[K:F]\le2$.
:::

<1>2. Complex conjugation gives a nontrivial $F$-automorphism of $K$.
::: {.proof}
Complex conjugation sends
\[
\zeta_n\longmapsto\zeta_n^{-1}
\]
and fixes
\[
\zeta_n+\zeta_n^{-1}.
\]
Thus it fixes $F$ pointwise. Because $n>2$, a primitive $n$th root of unity is not equal to its inverse: otherwise $\zeta_n^2=1$, forcing its order to divide $2$. Hence complex conjugation is nontrivial on $K$.
:::

<1>3. Therefore $[K:F]=2$.
::: {.proof}
By <1>2, the extension $K/F$ has at least two $F$-automorphisms, so it cannot have degree $1$. Combined with <1>1, this gives
\[
[K:F]=2.
\]
:::

<1>4. The cyclotomic extension satisfies
\[
[K:\QQ]=\varphi(n).
\]
::: {.proof}
The minimal polynomial of a primitive $n$th root of unity over $\QQ$ is the cyclotomic polynomial $\Phi_n$, whose degree is $\varphi(n)$. Hence
\[
[\QQ(\zeta_n):\QQ]=\varphi(n).
\]
:::

<1>5. Hence
\[
[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]=\frac{\varphi(n)}2.
\]
::: {.proof}
By the tower law and <1>3--<1>4,
\[
\varphi(n)
=[K:\QQ]
=[K:F][F:\QQ]
=2[F:\QQ].
\]
Therefore
\[
[F:\QQ]=\frac{\varphi(n)}2.
\]
:::
:::
