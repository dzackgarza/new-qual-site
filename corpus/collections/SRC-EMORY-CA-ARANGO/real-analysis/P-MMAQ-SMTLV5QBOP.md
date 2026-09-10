---
schema: qual/card@1
id: P-MMAQ-SMTLV5QBOP
kind: problem
title: $\lim_{p\to 0^+}\|f\|_p$ exists for $f\in L^1([0,1])$ and is zero if $m\{f=0\}>0$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 4 in both preserved Arango Emory qualifying-problem compilations. The prior solution used an invalid interchange of limsup and supremum; the card is repaired using log-convexity of p -> integral |f|^p.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $f\in L^1([0,1])$.
Show that

1. The limit $\lim_{p\to 0^+} \| f \|_p$ exists.
2. If $m\{x:f(x)=0\}>0$, then this limit is zero.
:::

::: solution
<1>1. The quantities $\|f\|_p$ are finite for $0<p\le1$.
::: proof
For $t\ge0$ and $0<p\le1$,
\[
t^p\le 1+t.
\]
Hence
\[
\int_0^1 |f|^p\le 1+\|f\|_1<\infty.
\]
Thus $\|f\|_p=(\int|f|^p)^{1/p}$ is well defined and finite for every $0<p\le1$.
:::

<1>2. The logarithm of the $p$th moment is convex.
::: proof
Assume first that $f$ is not zero almost everywhere and define
\[
A(p)=\int_0^1 |f(x)|^p\,dx,
\qquad
F(p)=\log A(p),
\qquad 0<p\le1.
\]
For $0<p,q\le1$ and $0<\theta<1$, Hölder's inequality gives
\[
\begin{aligned}
A((1-\theta)p+\theta q)
&=\int |f|^{(1-\theta)p}|f|^{\theta q}\\
&\le A(p)^{1-\theta}A(q)^\theta.
\end{aligned}
\]
Taking logarithms shows
\[
F((1-\theta)p+\theta q)
\le (1-\theta)F(p)+\theta F(q).
\]
Thus $F$ is convex on $(0,1]$.
:::

<1>3. Compute the zeroth-moment limit.
::: proof
Let
\[
\alpha=m\{x:f(x)\ne0\}\in(0,1].
\]
For almost every $x$,
\[
|f(x)|^p\longrightarrow \mathbf1_{\{f\ne0\}}(x)
\qquad(p\downarrow0).
\]
For $0<p\le1$ we have $|f|^p\le1+|f|$, and $1+|f|$ is integrable on $[0,1]$. Dominated convergence therefore gives
\[
A(p)\longrightarrow\alpha.
\]
Hence
\[
F(p)\longrightarrow\log\alpha.
\]
:::

<1>4. If the zero set has positive measure, the limit is zero.
::: proof
If $m\{f=0\}>0$, then $\alpha<1$. By Step 3,
\[
F(p)\longrightarrow\log\alpha<0.
\]
Therefore
\[
\log\|f\|_p=\frac{F(p)}p\longrightarrow-\infty,
\]
and so
\[
\boxed{\|f\|_p\longrightarrow0.}
\]
If $f=0$ almost everywhere, this conclusion is immediate because every $\|f\|_p=0$.
:::

<1>5. If $f\ne0$ almost everywhere, the limit still exists.
::: proof
Now suppose $\alpha=1$. Step 3 gives $F(p)\to0$, so define $F(0)=0$. The resulting function is convex on $[0,1]$.

For $0<p<q\le1$, convexity at
\[
p=\frac pq q+\left(1-\frac pq\right)0
\]
gives
\[
F(p)\le \frac pq F(q).
\]
Thus
\[
\frac{F(p)}p\le\frac{F(q)}q.
\]
Consequently the function
\[
p\longmapsto \frac{F(p)}p=\log\|f\|_p
\]
is nondecreasing on $(0,1]$. Hence it has a limit as $p\downarrow0$, equal to its infimum, possibly $-\infty$ but never $+\infty$ because
\[
\frac{F(p)}p\le F(1)=\log\|f\|_1.
\]
Exponentiating, $\|f\|_p$ therefore has a limit in $[0,\infty)$.
:::

<1>6. Conclude both assertions.
::: proof
If $f=0$ almost everywhere, the limit is $0$. If the zero set has positive but not full measure, Step 4 gives limit $0$. If $f\ne0$ almost everywhere, Step 5 proves existence of the limit. These cases exhaust all possibilities, proving both claims.
:::
:::
