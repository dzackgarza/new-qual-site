---
schema: qual/card@1
id: P-RASP11E
kind: problem
title: "Carleson's theorem: Fourier partial sums converge a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Spring 2011 real-analysis qualifying exam. The requested subsequence conclusion follows from standard L2 Fourier convergence and does not require the full Carleson theorem.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^2([0, 2\pi])$, and set $S_N f(x) = \sum_{n=-N}^{N} \hat{f}(n) e^{inx}$ to be the $N$th symmetric partial sum of its Fourier series.
Here $\hat{f}(n) = (2\pi)^{-1} \int_0^{2\pi} e^{-inx} f(x)\,dx$.
Show that there exists a subsequence $N_k \to \infty$ so that $S_{N_k} f \to f$ a.e. with respect to Lebesgue measure on $[0, 2\pi]$.
:::

::: solution
<1>1. The symmetric partial sums converge to $f$ in $L^2$.
::: proof
Let
\[
V_N=\operatorname{span}\{e^{inx}:-N\le n\le N\}.
\]
The function $S_Nf$ is the orthogonal projection of $f$ onto $V_N$ in $L^2([0,2\pi])$.

The union of the spaces $V_N$ is the set of trigonometric polynomials. Trigonometric polynomials are uniformly dense in the continuous $2\pi$-periodic functions by Stone--Weierstrass, and continuous functions are dense in $L^2([0,2\pi])$. Hence
\[
\overline{\bigcup_{N\ge0}V_N}^{\,L^2}=L^2([0,2\pi]).
\]
Therefore the orthogonal projections satisfy
\[
\|S_Nf-f\|_2\longrightarrow0.
\]
:::

<1>2. Extract a subsequence converging almost everywhere.
::: proof
Choose integers
\[
N_1<N_2<\cdots
\]
so that
\[
\|S_{N_k}f-f\|_2^2<2^{-3k}
\]
for every $k$. Set
\[
E_k=\{x:|S_{N_k}f(x)-f(x)|>2^{-k}\}.
\]
By Chebyshev's inequality,
\[
m(E_k)
\le 2^{2k}\|S_{N_k}f-f\|_2^2
<2^{-k}.
\]
Thus
\[
\sum_{k=1}^\infty m(E_k)<\infty.
\]
By the first Borel--Cantelli lemma, almost every $x$ belongs to only finitely many $E_k$. For such $x$,
\[
|S_{N_k}f(x)-f(x)|\le2^{-k}
\]
for all sufficiently large $k$, and therefore
\[
\boxed{S_{N_k}f(x)\to f(x)\quad\text{for a.e. }x.}
\]
:::
:::
