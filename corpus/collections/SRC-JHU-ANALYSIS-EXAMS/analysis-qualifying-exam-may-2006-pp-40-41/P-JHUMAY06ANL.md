---
schema: qual/card@1
id: P-JHUMAY06ANL
kind: problem
title: "Cesaro means of an orthonormal sequence converge to zero a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 12 of the preserved JHU Analysis Qualifying Exam, May 2006, collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_j)$ be an orthonormal sequence in $L^2([0,1])$. Prove that the Cesaro means
\[
S_n=\frac1n\sum_{j=1}^n f_j
\]
converge to $0$ almost everywhere.
:::

::: {.solution}
Because the $f_j$ are orthonormal,
\[
\|S_n\|_2^2
=\frac1{n^2}\sum_{j=1}^n\|f_j\|_2^2
=\frac1n.
\]

<1>1. The square subsequence converges to $0$ almost everywhere.
::: {.proof}
For $n=k^2$,
\[
\sum_{k=1}^\infty \|S_{k^2}\|_2^2
=\sum_{k=1}^\infty\frac1{k^2}<\infty.
\]
Hence, for every $\varepsilon>0$, Chebyshev gives
\[
\sum_{k=1}^\infty m\{|S_{k^2}|>\varepsilon\}
\le \frac1{\varepsilon^2}\sum_{k=1}^\infty\|S_{k^2}\|_2^2<\infty.
\]
By Borel--Cantelli, $S_{k^2}(x)\to0$ for almost every $x$.
:::

<1>2. The oscillation between consecutive squares tends to $0$ almost everywhere.
::: {.proof}
Fix $k$ and put $m=k^2$. For $m<n\le(k+1)^2$, orthogonality gives
\[
S_n-S_m
=\left(\frac1n-\frac1m\right)\sum_{j=1}^m f_j
+\frac1n\sum_{j=m+1}^n f_j,
\]
with the two sums orthogonal. Therefore
\[
\|S_n-S_m\|_2^2
=m\left(\frac1n-\frac1m\right)^2+\frac{n-m}{n^2}.
\]
Since $n-m\le2k+1$, $m=k^2$, and $n\ge k^2$, there is an absolute constant $C$ such that
\[
\|S_n-S_{k^2}\|_2^2\le\frac{C}{k^3}
\]
for all sufficiently large $k$ and all $k^2<n\le(k+1)^2$.

For $\varepsilon>0$, a union bound and Chebyshev give
\[
\begin{aligned}
m\left\{\max_{k^2<n\le(k+1)^2}|S_n-S_{k^2}|>\varepsilon\right\}
&\le\sum_{n=k^2+1}^{(k+1)^2}m\{|S_n-S_{k^2}|>\varepsilon\}\\
&\le\frac1{\varepsilon^2}\sum_{n=k^2+1}^{(k+1)^2}\|S_n-S_{k^2}\|_2^2\\
&\le\frac{C'}{\varepsilon^2k^2},
\end{aligned}
\]
because the block contains $2k+1$ indices. The right-hand side is summable in $k$. Another application of Borel--Cantelli yields
\[
\max_{k^2<n\le(k+1)^2}|S_n(x)-S_{k^2}(x)|\longrightarrow0
\]
for almost every $x$.
:::

<1>3. Conclude for the full sequence.
::: {.proof}
Outside the union of the two null exceptional sets from <1>1 and <1>2, if $k^2<n\le(k+1)^2$, then
\[
|S_n(x)|
\le |S_{k^2}(x)|+|S_n(x)-S_{k^2}(x)|.
\]
Both terms tend to $0$ as $k\to\infty$. Hence
\[
S_n(x)\longrightarrow0
\]
for almost every $x\in[0,1]$.
:::
:::
