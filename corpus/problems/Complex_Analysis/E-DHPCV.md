---
schema: qual/card@1
id: E-DHPCV
kind: problem
title: $\|f\|_{(\infty,s)}\le c\|f\|_{(1,r)}$ for holomorphic $f$
classification:
  areas:
  - complex-analysis
  topics:
  - Mean Value Property
  - Cauchy Estimates
  - Holomorphic Functions
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
Let $f$ be holomorphic in a neighborhood of $\overline{D_r(z_0)}$. Show that for any $s < r$, there exists a constant $c > 0$ such that
$$
\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)}
,$$ 
where
$\displaystyle \|f\|_{(\infty, s)} = \sup_{z \in D_s(z_0)}|f(z)|$
and $\displaystyle \|f\|_{(1, r)} = \iint_{D_r(z_0)} |f(z)|\,dx\,dy$.
:::

::: solution
Let
\[
\delta=r-s>0.
\]
Fix $z\in D_s(z_0)$. Since $|z-z_0|<s$, the closed disk $\overline{D_\delta(z)}$ is contained in $D_r(z_0)$.

<1>1. For every $0<\rho<\delta$, the mean-value formula gives
\[
f(z)=\frac1{2\pi}\int_0^{2\pi}f(z+\rho e^{i\theta})\,d\theta.
\]
Multiply by $2\rho$ and integrate from $0$ to $\delta$. Using polar coordinates,
\[
\delta^2 f(z)
=\frac1\pi\iint_{D_\delta(z)}f(w)\,dA(w).
\]
Thus
\[
f(z)=\frac1{\pi\delta^2}\iint_{D_\delta(z)}f(w)\,dA(w).
\]

<1>2. Taking absolute values,
\[
|f(z)|
\le\frac1{\pi\delta^2}\iint_{D_\delta(z)}|f(w)|\,dA(w)
\le\frac1{\pi(r-s)^2}\|f\|_{(1,r)}.
\]

<1>3. Taking the supremum over $z\in D_s(z_0)$ yields
\[
\|f\|_{(\infty,s)}
\le\frac1{\pi(r-s)^2}\|f\|_{(1,r)}.
\]
Hence one may take
\[
c=\frac1{\pi(r-s)^2}.
\]
:::
