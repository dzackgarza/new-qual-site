---
schema: qual/card@1
id: P-XT3LV
kind: problem
title: $[\QQ(\zeta+\zeta^{-1}):\QQ]=\varphi(n)/2$ for a primitive $n$th root of unity
  $\zeta$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

::: {.problem}
Let $n>2$ and let $\zeta_n$ be a primitive $n$th root of unity. Prove
\[
[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]
=\frac{\varphi(n)}2.
\]
:::

::: {.solution}
Set
\[
K=\QQ(\zeta_n+\zeta_n^{-1}).
\]
The element $\zeta_n$ satisfies
\[
x^2-(\zeta_n+\zeta_n^{-1})x+1=0,
\]
so
\[
[\QQ(\zeta_n):K]\le2.
\]

Because $n>2$, the primitive root $\zeta_n$ is nonreal. On the other hand,
\[
\zeta_n+\zeta_n^{-1}=2\cos(2\pi/n)\in\RR,
\]
so
\[
K\subseteq\RR.
\]
Therefore $\zeta_n\notin K$, and the extension is proper. Hence
\[
[\QQ(\zeta_n):K]=2.
\]

The cyclotomic degree is
\[
[\QQ(\zeta_n):\QQ]=\varphi(n).
\]
By the tower law,
\[
\varphi(n)
=[\QQ(\zeta_n):K][K:\QQ]
=2[K:\QQ].
\]
Therefore
\[
[K:\QQ]=\frac{\varphi(n)}2.
\]
:::
