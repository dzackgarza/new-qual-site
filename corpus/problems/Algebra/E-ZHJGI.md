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

::: {.problem}
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

::: pf

::: {.pf-step #k-f-degree-le-2}
One has $[K:F]\le2$.

::: pf-proof
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

:::

::: {.pf-step #complex-conj-nontrivial}
Complex conjugation gives a nontrivial $F$-automorphism of $K$.

::: pf-proof
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

:::

::: {.pf-step #k-f-degree-eq-2}
Therefore $[K:F]=2$.

::: pf-proof
By step [](#complex-conj-nontrivial){.pf-ref}, the extension $K/F$ has at least two $F$-automorphisms, so it cannot have degree $1$. Combined with step [](#k-f-degree-le-2){.pf-ref}, this gives
\[
[K:F]=2.
\]
:::

:::

::: {.pf-step #k-q-degree-phi-n}
The cyclotomic extension satisfies
\[
[K:\QQ]=\varphi(n).
\]

::: pf-proof
The minimal polynomial of a primitive $n$th root of unity over $\QQ$ is the cyclotomic polynomial $\Phi_n$, whose degree is $\varphi(n)$. Hence
\[
[\QQ(\zeta_n):\QQ]=\varphi(n).
\]
:::

:::

::: pf-step
Hence
\[
[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]=\frac{\varphi(n)}2.
\]

::: pf-proof
By the tower law and steps [](#k-f-degree-eq-2){.pf-ref} and [](#k-q-degree-phi-n){.pf-ref},
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

:::

:::
