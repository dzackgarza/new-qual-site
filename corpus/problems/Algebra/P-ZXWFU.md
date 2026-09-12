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

::: problem
What is the maximal real subfield in a cyclotomic extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$?
:::

::: solution
Let
\[
K=\mathbb Q(\zeta_n).
\]
Complex conjugation acts by
\[
\zeta_n\longmapsto\zeta_n^{-1}.
\]
Therefore the maximal real subfield is the fixed field
\[
K^+=K^{\langle c\rangle}=K\cap\mathbb R.
\]
The element
\[
\zeta_n+\zeta_n^{-1}=2\cos\frac{2\pi}{n}
\]
is fixed by conjugation, and $\zeta_n$ satisfies
\[
x^2-(\zeta_n+\zeta_n^{-1})x+1=0
\]
over $\mathbb Q(\zeta_n+\zeta_n^{-1})$. For $n>2$, $K$ is not real, so
\[
[K:K^+]=2.
\]
Hence
\[
\boxed{K^+=\mathbb Q(\zeta_n+\zeta_n^{-1})}
\]
and
\[
[K^+:\mathbb Q]=\frac{\varphi(n)}2.
\]
Since
\[
\operatorname{Gal}(K/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^\times
\]
and complex conjugation corresponds to $-1$, for $n>2$,
\[
\operatorname{Gal}(K^+/\mathbb Q)
\cong(\mathbb Z/n\mathbb Z)^\times/\{\pm1\}.
\]
For $n=1,2$, the cyclotomic field is already $\mathbb Q$.
:::
