---
schema: qual/card@1
id: P-DUKEBA14-11
kind: problem
title: Taylor expansion separates two logarithmic series
classification:
  areas: [real-analysis]
  topics: [Series, Taylor Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 5 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Use Taylor's theorem to prove that
\[
\sum_{k=1}^\infty \log(1+k^{-2/3})
\]
diverges, while
\[
\sum_{k=1}^\infty
\left[\log(1+k^{-2/3})-k^{-2/3}\right]
\]
converges.
:::

::: solution
<1>1. Obtain uniform Taylor estimates near $0$.
::: proof
For $0\le x\le1$, Taylor's theorem for $\log(1+x)$ at $0$ gives
\[
\log(1+x)=x-\frac{x^2}{2}+R_3(x),
\]
where
\[
|R_3(x)|\le Cx^3
\]
for some absolute constant $C$ on $[0,1]$.
In particular, after decreasing the neighborhood of $0$ if necessary,
\[
\log(1+x)\ge \frac{x}{2}.
\]
:::

<1>2. Prove divergence of the first series.
::: proof
Put $x_k=k^{-2/3}$. Then $x_k\to0$, so for all sufficiently large $k$,
\[
\log(1+x_k)\ge\frac{x_k}{2}
=\frac1{2k^{2/3}}.
\]
Since $\sum k^{-2/3}$ diverges, the comparison test gives
\[
\sum_{k=1}^\infty\log(1+k^{-2/3})=\infty.
\]
:::

<1>3. Prove convergence after subtracting the linear term.
::: proof
Taylor's formula gives
\[
\log(1+x)-x=-\frac{x^2}{2}+R_3(x).
\]
Hence, for $0\le x\le1$,
\[
|\log(1+x)-x|
\le C' x^2
\]
for some constant $C'$. Therefore
\[
\left|
\log(1+k^{-2/3})-k^{-2/3}
\right|
\le C'k^{-4/3}.
\]
Since $\sum k^{-4/3}$ converges, the second series converges absolutely.
:::
:::
