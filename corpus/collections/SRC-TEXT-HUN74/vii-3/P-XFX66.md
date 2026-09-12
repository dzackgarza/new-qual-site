---
schema: qual/card@1
id: P-XFX66
kind: problem
title: Alternating and skew-symmetric multilinear forms
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford VII.3.1 in an independent exercise reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $B$ be an $R$-module.
Show that if $r+r\neq 0$ for all $r\neq 0 \in R$, then an $n$-linear form $B^n\to R$ is alternating $\iff$ it is skew-symmetric.
:::


::: solution
Let \(f:B^n\to R\) be \(n\)-linear. Here “skew-symmetric” means that
interchanging two arguments multiplies the value by \(-1\), and “alternating”
means that \(f\) vanishes whenever two arguments are equal.

<1>1. Every alternating \(n\)-linear form is skew-symmetric.
::: proof
Fix all arguments except positions \(i<j\), and write \(x,y\in B\) in those
positions. Alternation gives
\[
0=f(\ldots,x+y,\ldots,x+y,\ldots).
\]
Expanding by multilinearity, the two terms with equal arguments vanish, leaving
\[
f(\ldots,x,\ldots,y,\ldots)
+f(\ldots,y,\ldots,x,\ldots)=0.
\]
Thus interchanging the two arguments changes the sign.
:::

<1>2. Under the hypothesis \(r+r\ne0\) for every \(0\ne r\in R\), every
skew-symmetric \(n\)-linear form is alternating.
::: proof
Suppose two arguments, say positions \(i<j\), are equal to \(x\). Skew-symmetry
under their transposition gives
\[
f(\ldots,x,\ldots,x,\ldots)
=-f(\ldots,x,\ldots,x,\ldots).
\]
Hence, with \(r=f(\ldots,x,\ldots,x,\ldots)\),
\[
r+r=0.
\]
By the stated hypothesis this forces \(r=0\). Therefore \(f\) vanishes whenever
two arguments coincide, so \(f\) is alternating.
:::

<1>3. Therefore the two notions are equivalent under the stated hypothesis.
::: proof
Combine <1>1 and <1>2.
:::
:::
