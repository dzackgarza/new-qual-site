---
schema: qual/card@1
id: P-EMRA4
kind: problem
title: "Limit of L^p norm as p -> 0+"
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
  note: Checked against Real Analysis Problem 4 in the preserved Emory qualifying-exam compilation collected by Santiago Arango.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1([0,1])$.
Show that

(a) The limit $\lim_{p \to 0^+} \|f\|_p$ exists.

(b) If $m\{x : f(x) = 0\} > 0$, then the above limit is zero.
:::

::: {.solution}
<1>1. The quantity $\|f\|_p$ is finite for every $0<p\le1$.
::: {.proof}
For $t\ge0$ and $0<p\le1$,
\[
t^p\le 1+t.
\]
Hence
\[
\int_0^1 |f|^p\le 1+\|f\|_1<\infty.
\]
Thus
\[
\|f\|_p:=\left(\int_0^1|f|^p\right)^{1/p}
\]
is well-defined for $0<p\le1$.
:::

<1>2. If $f\ne0$ almost everywhere, then $\lim_{p\downarrow0}\|f\|_p$ exists.
::: {.proof}
Set
\[
I(p)=\int_0^1 |f(x)|^p\,dx,
\qquad
F(p)=\log I(p)
\qquad (p>0).
\]
For $0<\theta<1$ and $p,q>0$, Hölder's inequality gives
\[
I(\theta p+(1-\theta)q)
=\int |f|^{\theta p}|f|^{(1-\theta)q}
\le I(p)^\theta I(q)^{1-\theta}.
\]
Therefore $F$ is convex on $(0,\infty)$.

Since $f\ne0$ a.e., $|f|^p\to1$ a.e. as $p\downarrow0$, and for $0<p\le1$ we have $|f|^p\le1+|f|$. Dominated convergence yields
\[
I(p)\longrightarrow1,
\qquad
F(p)\longrightarrow0.
\]
Define $F(0)=0$. Then $F$ is convex on $[0,1]$. For a convex function with $F(0)=0$, the secant slope
\[
\frac{F(p)}p
\]
is nondecreasing in $p>0$. Hence the limit
\[
L:=\lim_{p\downarrow0}\frac{F(p)}p
\]
exists in $[-\infty,\infty)$.
Since
\[
\log\|f\|_p=\frac1p\log I(p)=\frac{F(p)}p,
\]
we obtain
\[
\lim_{p\downarrow0}\|f\|_p=e^L,
\]
with the convention $e^{-\infty}=0$.
:::

<1>3. If $f$ vanishes on a set of positive measure, the limit is zero.
::: {.proof}
Let
\[
q=m\{x\in[0,1]:f(x)\ne0\}.
\]
If $m\{f=0\}>0$, then $q<1$. Again $|f|^p\to\mathbf 1_{\{f\ne0\}}$ a.e. and $|f|^p\le1+|f|$, so dominated convergence gives
\[
I(p)=\int_0^1|f|^p\longrightarrow q<1.
\]
Choose $c$ with $q<c<1$. For all sufficiently small $p>0$, $I(p)\le c$, and therefore
\[
0\le \|f\|_p=I(p)^{1/p}\le c^{1/p}\longrightarrow0.
\]
Thus
\[
\lim_{p\downarrow0}\|f\|_p=0.
\]
:::
:::
