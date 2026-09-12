---
schema: qual/card@1
id: E-SS2.EX-8
kind: problem
title: "SS 2.8: Derivatives inherit polynomial growth on a strip"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
8. If f is a holomorphic function on the strip $- 1 < y < 1 , x \in \mathbb { R }$ with

$$
| f (z) | \leq A (1 + | z |) ^ {\eta}, \quad \eta \text {   a   fixed   real   number }
$$

for all z in that strip, show that for each integer $n \geq 0$ there exists $A _ { n } \geq 0$ so that

$$
| f ^ {(n)} (x) | \leq A _ {n} (1 + | x |) ^ {\eta}, \quad \text {   for   all   } x \in \mathbb {R}.
$$

[Hint: Use the Cauchy inequalities.]
:::

::: solution
Fix $x\in\mathbb R$ and use the circle
\[
|z-x|=\frac12.
\]
It lies entirely in the strip $-1<\operatorname{Im}z<1$. Cauchy's inequalities give
\[
|f^{(n)}(x)|
\le n!\,2^n\sup_{|z-x|=1/2}|f(z)|.
\tag{1}
\]

On this circle,
\[
|x|-\frac12\le |z|\le |x|+\frac12,
\]
so
\[
\frac12(1+|x|)\le 1+|z|\le \frac32(1+|x|).
\]
Hence, for the fixed real exponent $\eta$, there is a constant
\[
C_\eta=\max\left\{\left(\frac32\right)^\eta,2^{-\eta}\right\}
\]
such that
\[
(1+|z|)^\eta\le C_\eta(1+|x|)^\eta
\]
for all $|z-x|=1/2$; this covers both signs of $\eta$.

Using the assumed growth bound in (1),
\[
|f^{(n)}(x)|
\le n!2^n A C_\eta(1+|x|)^\eta.
\]
Thus the required estimate holds with
\[
A_n=n!2^nAC_\eta.
\]
:::
