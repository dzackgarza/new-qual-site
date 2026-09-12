---
schema: qual/card@1
id: P-EMHMR
kind: problem
title: Uniqueness of Laurent series coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Prove that if a function $f$ has two Laurent series expansions in an annulus $A = \{z \in \mathbb{C} \mid r < |z-a| < R\}$:
$$f(z) = \sum_{n=-\infty}^\infty c_n(z-a)^n \quad\text{and}\quad f(z) = \sum_{n=-\infty}^\infty c_n'(z-a)^n$$
then $c_n = c_n'$ for all $n \in \mathbb{Z}$.
:::

::: solution
Fix $\rho$ with
\[
r<\rho<R,
\]
and let
\[
\gamma(t)=a+\rho e^{it},\qquad0\le t\le2\pi.
\]
For every integer $k$, define
\[
I_k=\frac1{2\pi i}\int_\gamma\frac{f(z)}{(z-a)^{k+1}}\,dz.
\]

<1>1. A Laurent series converges uniformly on every circle compactly contained in its annulus of convergence. Hence the first expansion may be integrated term by term on $\gamma$:
\[
I_k
=\sum_{n\in\mathbb Z}c_n\frac1{2\pi i}\int_\gamma(z-a)^{n-k-1}\,dz.
\]

<1>2. For every integer $m$,
\[
\frac1{2\pi i}\int_\gamma(z-a)^m\,dz
=\begin{cases}
1,&m=-1,\\
0,&m\ne-1.
\end{cases}
\]
Therefore only the term $n=k$ survives, and
\[
I_k=c_k.
\]

<1>3. Applying the same computation to the second Laurent expansion gives
\[
I_k=c_k'.
\]
Thus
\[
c_k=c_k'
\]
for every $k\in\mathbb Z$.

Hence Laurent coefficients on a fixed annulus are unique, with
\[
c_k=\frac1{2\pi i}\int_{|z-a|=\rho}\frac{f(z)}{(z-a)^{k+1}}\,dz.
\]
:::
