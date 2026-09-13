---
schema: qual/card@1
id: P-BERK80S-16
kind: problem
title: Subsequence convergence for oscillatory functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 16 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the bounded and unbounded parameter subsequences and locally uniform convergence to a continuous limit in every case.
---

::: {.problem}
Let $\left( a _ { n } \right)$ be a sequence of nonzero real numbers.
Prove that the sequence of functions $f _ { n } : \mathbb { R } \to \mathbb { R }$

$$
f _ { n } ( x ) = { \frac { 1 } { a _ { n } } } \sin ( a _ { n } x ) + \cos ( x + a _ { n } )
$$

has a subsequence converging to a continuous function.
:::

::: {.solution}
Let
\[
f_n(x)=\frac{\sin(a_nx)}{a_n}+\cos(x+a_n),
\qquad a_n\ne0.
\]
We distinguish whether $(a_n)$ has a bounded subsequence.

<1>1. If $(a_n)$ has a bounded subsequence, then $(f_n)$ has a locally uniformly convergent subsequence.
::: {.proof}
By Bolzano--Weierstrass, after passing to a subsequence we may assume
\[
a_n\to a\in\mathbb R.
\]

If $a\ne0$, then for each compact interval $K\subset\mathbb R$,
\[
\frac{\sin(a_nx)}{a_n}\longrightarrow \frac{\sin(ax)}a
\]
uniformly for $x\in K$, because the function
\[
(t,x)\longmapsto \frac{\sin(tx)}t
\]
is continuous near $\{a\}\times K$.
Also
\[
\cos(x+a_n)\longrightarrow\cos(x+a)
\]
uniformly in $x$ because cosine is Lipschitz.
Hence
\[
f_n(x)\longrightarrow \frac{\sin(ax)}a+\cos(x+a)
\]
locally uniformly.

If $a=0$, write
\[
\frac{\sin(a_nx)}{a_n}
=x\,\frac{\sin(a_nx)}{a_nx},
\]
with the quotient interpreted as $1$ at $x=0$.
On every compact interval, $a_nx\to0$ uniformly, so
\[
\frac{\sin(a_nx)}{a_n}\longrightarrow x
\]
uniformly there.
Also
\[
\cos(x+a_n)\longrightarrow\cos x
\]
uniformly.
Thus
\[
f_n(x)\longrightarrow x+\cos x
\]
locally uniformly.

In either case the limit is continuous.
:::

<1>2. If $(a_n)$ has no bounded subsequence, then $(f_n)$ has a uniformly convergent subsequence.
::: {.proof}
If $(a_n)$ has no bounded subsequence, then after passing to a subsequence we may assume
\[
|a_n|\to\infty.
\]
Therefore
\[
\sup_{x\in\mathbb R}\left|\frac{\sin(a_nx)}{a_n}\right|
\le \frac1{|a_n|}\longrightarrow0.
\]

The points $e^{ia_n}$ lie on the compact unit circle, so after passing to a further subsequence,
\[
e^{ia_n}\to e^{i\theta}
\]
for some real $\theta$.
Then for every $x$,
\[
\begin{aligned}
|\cos(x+a_n)-\cos(x+\theta)|
&=\left|\Re\left(e^{ix}(e^{ia_n}-e^{i\theta})\right)\right|\\
&\le |e^{ia_n}-e^{i\theta}|,
\end{aligned}
\]
and the right-hand side is independent of $x$ and tends to $0$.
Hence
\[
\cos(x+a_n)\longrightarrow\cos(x+\theta)
\]
uniformly on $\mathbb R$.
Combining the two terms,
\[
f_n\longrightarrow \cos(x+\theta)
\]
uniformly, and the limit is continuous.
:::

Thus every sequence $(a_n)$ has a subsequence for which the corresponding functions converge to a continuous function.
:::
