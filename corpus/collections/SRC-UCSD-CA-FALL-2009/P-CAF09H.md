---
schema: qual/card@1
id: P-CAF09H
kind: problem
title: "Interpolation by entire functions with prescribed values and multiplicities"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
We are given two sequences of complex numbers, $\{\alpha_j\}_{j \geq 1}$ and $\{\beta_j\}_{j \geq 1}$, where the $\alpha_j$ are all distinct and $|\alpha_j| \to \infty$ as $j \to \infty$.
Use a combination of the Mittag-Leffler Theorem and the Weierstrass Product Theorem, or any other method, to show that there exists an entire function $f(z)$ such that for each $j$, $f(z)$ takes the value $\beta_j$ at $\alpha_j$ with multiplicity at least 2.

(Bonus: show that $f(z)$ can be chosen so that for all $j$, $f(z)$ takes the value $\beta_j$ at $z = \alpha_j$ with multiplicity exactly 2.)
:::

::: solution
By the Weierstrass product theorem, there is an entire function $P$ whose zeros
are exactly the points $\alpha_j$, all simple. Near $\alpha_j$, writing
$t=z-\alpha_j$, we have
\[
P(z)=p_{1,j}t+p_{2,j}t^2+O(t^3),
\qquad p_{1,j}=P'(\alpha_j)\ne0.
\]

We seek $f=P^2h$, where $h$ is meromorphic with poles only at the $\alpha_j$.
Prescribe at $\alpha_j$ the principal part
\[
h(z)=\frac{A_j}{t^2}+\frac{B_j}{t}+O(1),
\]
with
\[
A_j=\frac{\beta_j}{p_{1,j}^2},
\qquad
B_j=-\frac{2p_{2,j}\beta_j}{p_{1,j}^3}.
\]
The Mittag--Leffler theorem produces a meromorphic $h$ with exactly these
principal parts. Since
\[
P(z)^2
=p_{1,j}^2t^2+2p_{1,j}p_{2,j}t^3+O(t^4),
\]
we obtain
\[
P(z)^2h(z)=\beta_j+O(t^2).
\]
Thus $f=P^2h$ extends holomorphically across every $\alpha_j$ and satisfies
\[
f(\alpha_j)=\beta_j,
\qquad
f'(\alpha_j)=0.
\]
Hence $f-\beta_j$ has a zero of multiplicity at least $2$ at $\alpha_j$.

For the bonus, start with such an $f_0$. Any function of the form
\[
f=f_0+P^2g,
\]
with $g$ entire, preserves all values and first derivatives at the $\alpha_j$.
At each $\alpha_j$, the coefficient of $(z-\alpha_j)^2$ in
$f(z)-\beta_j$ depends affinely and nontrivially on $g(\alpha_j)$, because
$P'(\alpha_j)\ne0$. Therefore there is exactly one forbidden value of
$g(\alpha_j)$ that would make this quadratic coefficient vanish. Choose any
other value $c_j$ for each $j$.

Using the same Weierstrass--Mittag--Leffler interpolation construction in the
simple-value case, choose an entire $g$ with
\[
g(\alpha_j)=c_j
\]
for every $j$. Then the quadratic coefficient of $f-\beta_j$ is nonzero at
each $\alpha_j$, so every prescribed value is taken with multiplicity exactly
$2$.
:::
