---
schema: qual/card@1
id: E-SS5.PR-3
kind: problem
title: Order of an entire function with coefficients $(n!)^{-\alpha}$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
Show that

$$
\sum_{n=0}^{\infty}\frac{z^n}{(n!)^\alpha}
$$

is an entire function of order $1/\alpha$.
:::

::: solution
Let
\[
F(z)=\sum_{n=0}^\infty \frac{z^n}{(n!)^\alpha},\qquad \alpha>0.
\]
The ratio test shows that the radius of convergence is infinite, so $F$ is entire.

Use the elementary Stirling lower bound $n!\ge (n/e)^n$. Put $R=r^{1/\alpha}$. Then
\[
\frac{r^n}{(n!)^\alpha}
\le \left(\frac{eR}{n}\right)^{\alpha n}.
\tag{1}
\]
For real $x>0$, the function
\[
x\bigl(1+\log R-\log x\bigr)
\]
has derivative $\log(R/x)$ and therefore has maximum $R$ at $x=R$. Hence every term on the right of (1) is at most $e^{\alpha R}$.

Let $N=\lceil 2eR\rceil$. For $n>N$, $eR/n<1/2$, so (1) gives
\[
\frac{r^n}{(n!)^\alpha}\le 2^{-\alpha n}.
\]
Consequently
\[
M_F(r)\le F(r)
\le (N+1)e^{\alpha R}+\sum_{n>N}2^{-\alpha n}
\le C e^{C'R}
=C e^{C'r^{1/\alpha}}
\]
for suitable constants $C,C'>0$. Hence the order is at most $1/\alpha$.

For the reverse inequality, suppose $F$ had order $\rho<1/\alpha$. Choose $\sigma$ with $\rho<\sigma<1/\alpha$. Then for some $A,B>0$,
\[
M_F(r)\le Ae^{Br^\sigma}.
\]
Cauchy's estimate gives
\[
\frac1{(n!)^\alpha}\le \frac{Ae^{Br^\sigma}}{r^n}.
\]
Taking $r=(n/(B\sigma))^{1/\sigma}$ minimizes the right-hand side, so
\[
\log (n!)^\alpha
\ge \frac n\sigma\log n+O(n).
\]
But Stirling gives $\log (n!)^\alpha=\alpha n\log n+O(n)$, forcing $\alpha\ge1/\sigma$, contrary to $\sigma<1/\alpha$. Thus the order is exactly
\[
\boxed{1/\alpha}.
\]
:::
