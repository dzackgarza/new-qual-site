---
schema: qual/card@1
id: P-JHUU51RA3
kind: problem
title: "A Hoelder-type norm makes a Banach space of functions on [0,1]"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 3 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $X$ be the set of functions $f:[0,1]\to\mathbb R$ for which
\[
\|f\|:=|f(0)|+\sup_{x\ne y}\frac{|f(x)-f(y)|}{|x-y|^{1/5}}<\infty.
\]
Prove that $(X,\|\cdot\|)$ is a Banach space.
:::

::: {.solution}
Write
\[
[f]_{1/5}:=\sup_{x\ne y}\frac{|f(x)-f(y)|}{|x-y|^{1/5}}.
\]
Then
\[
\|f\|=|f(0)|+[f]_{1/5}.
\]

<1>1. $X$ is a vector space and $\|\cdot\|$ is a norm.
::: {.proof}
If $f,g\in X$ and $a,b\in\mathbb R$, then
\[
[af+bg]_{1/5}\le |a|[f]_{1/5}+|b|[g]_{1/5}<\infty,
\]
so $af+bg\in X$. The seminorm $[\cdot]_{1/5}$ is homogeneous and subadditive, hence so is $\|\cdot\|$.

If $\|f\|=0$, then $f(0)=0$ and $[f]_{1/5}=0$, so $f(x)=f(y)$ for all $x,y$. Thus $f$ is constant, and since $f(0)=0$, one has $f\equiv0$. Therefore $\|\cdot\|$ is a norm.
:::

<1>2. The norm controls uniform convergence.
::: {.proof}
For every $f\in X$ and $x\in[0,1]$,
\[
|f(x)|\le |f(0)|+|f(x)-f(0)|
\le |f(0)|+[f]_{1/5}|x|^{1/5}
\le \|f\|.
\]
Hence
\[
\|f\|_\infty\le\|f\|.
\]
:::

<1>3. $X$ is complete.
::: {.proof}
Let $(f_n)$ be Cauchy in $\|\cdot\|$. By <1>2, it is uniformly Cauchy, so there is a function $f:[0,1]\to\mathbb R$ such that
\[
f_n\to f
\]
uniformly.

Fix $\varepsilon>0$. Since $(f_n)$ is Cauchy in $\|\cdot\|$, there exists $N$ such that for all $m,n\ge N$,
\[
|f_n(0)-f_m(0)|+[f_n-f_m]_{1/5}<\varepsilon.
\]
Fix $n\ge N$ and let $m\to\infty$. Uniform convergence gives
\[
|f_n(0)-f(0)|\le\varepsilon,
\]
and for every $x\ne y$,
\[
|(f_n-f)(x)-(f_n-f)(y)|
=\lim_{m\to\infty}|(f_n-f_m)(x)-(f_n-f_m)(y)|
\le\varepsilon |x-y|^{1/5}.
\]
Therefore
\[
[f_n-f]_{1/5}\le\varepsilon,
\]
so
\[
\|f_n-f\|\le2\varepsilon.
\]
In particular $f_n\to f$ in $\|\cdot\|$. Since $f=f_n-(f_n-f)$ and both terms have finite Hölder seminorm, $f\in X$. Thus every Cauchy sequence converges in $X$, and $X$ is Banach.
:::
:::
