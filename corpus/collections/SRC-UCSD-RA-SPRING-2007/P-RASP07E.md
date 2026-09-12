---
schema: qual/card@1
id: P-RASP07E
kind: problem
title: "Completeness of L^2"
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
  note: Checked against Problem 5 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Prove that $L^2(X, \mu)$ is complete.
This is stated and proved in Folland, but you are being asked to give a proof here.
For this, you may use without proof the following: A normed vector space $X$ is complete if and only if every absolutely convergent series in $X$ converges.
:::


::: solution
<1>1. Start with an absolutely convergent series in $L^2$.
::: proof
Suppose
\[
\sum_{n=1}^\infty \|f_n\|_2<\infty.
\]
For $N\ge1$, set
\[
G_N:=\sum_{n=1}^N |f_n|.
\]
By the triangle inequality in $L^2$,
\[
\|G_N\|_2
\le \sum_{n=1}^N\|f_n\|_2
\le \sum_{n=1}^\infty\|f_n\|_2=:M.
\]
Hence
\[
\int_X G_N^2\,d\mu\le M^2
\]
for every $N$.
:::

<1>2. Show that the series converges absolutely almost everywhere.
::: proof
The sequence $(G_N)$ is increasing, so
\[
G_N^2\uparrow G^2,
\qquad
G:=\sum_{n=1}^\infty|f_n|.
\]
By the Monotone Convergence Theorem,
\[
\int_X G^2\,d\mu
=\lim_{N\to\infty}\int_XG_N^2\,d\mu
\le M^2<\infty.
\]
Thus $G\in L^2(X,\mu)$ and in particular $G(x)<\infty$ for almost every $x$. Therefore
\[
\sum_{n=1}^\infty f_n(x)
\]
converges absolutely for almost every $x$. Define
\[
f(x):=\sum_{n=1}^\infty f_n(x)
\]
on that full-measure set, and define $f$ arbitrarily on the null exceptional set. Since $|f|\le G$, we have $f\in L^2$.
:::

<1>3. Prove convergence in the $L^2$ norm.
::: proof
For $N<M$,
\[
\left\|\sum_{n=N+1}^M f_n\right\|_2
\le \sum_{n=N+1}^M\|f_n\|_2.
\]
Letting $M\to\infty$, the partial sums converge pointwise almost everywhere to $f$, while
\[
\left|f-\sum_{n=1}^Nf_n\right|
\le \sum_{n=N+1}^\infty|f_n|.
\]
Applying Fatou to the squared tails gives
\[
\left\|f-\sum_{n=1}^Nf_n\right\|_2
\le \sum_{n=N+1}^\infty\|f_n\|_2
\longrightarrow0.
\]
Thus every absolutely convergent series in $L^2(X,\mu)$ converges in $L^2$.

By the criterion stated in the problem, this proves that
\[
\boxed{L^2(X,\mu)\text{ is complete}.}
\]
:::
:::
