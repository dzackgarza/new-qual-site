---
schema: qual/card@1
id: P-BKS03-4A
kind: problem
title: Chebyshev polynomials with integer coefficients
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Prove that for every integer $n\ge0$ there is a polynomial $T_n(x)\in\mathbb Z[x]$ such that
\[
2\cos(nz)=T_n(2\cos z)
\]
for every $z$.
:::

::: {.solution}
Put $q=e^{iz}$, so $2\cos z=q+q^{-1}$, and $2\cos nz=q^n+q^{-n}$. Then the problem is to find $T_n$ such that $T_n(q+q^{-1})=q^n+q^{-n}$. We have

$$
(q+q^{-1})^n=\sum_{k=0}^n\binom nk q^{2k-n}
=q^n+q^{-n}+\sum_{\substack{0<j<n\\ n-j\text{ even}}}\binom{n}{(n-j)/2}(q^j+q^{-j})
+\begin{cases}\binom{n}{n/2}&\text{if }n\text{ is even},\\ 0&\text{otherwise.}\end{cases}
$$

We can assume we have found $T_j$ for $j<n$ by induction.
Then

$$
T_n(x)=x^n-\sum_{\substack{0<j<n\\ n-j\text{ even}}}\binom{n}{(n-j)/2}T_j(x)
-\begin{cases}\binom{n}{n/2}&\text{if }n\text{ is even},\\ 0&\text{otherwise}\end{cases}
$$

has the required property.
:::
