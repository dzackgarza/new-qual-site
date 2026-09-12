---
schema: qual/card@1
id: E-SS10.EX-2
kind: problem
title: "SS 10.2: The generating function of the Fibonacci numbers"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
2. Consider the Fibonacci numbers $\{ F _ { n } \} _ { n = 0 } ^ { \infty }$ , defined by the two initial values $F _ { 0 } = 0 , F _ { 1 } = 1$ and the recursion relation

$$
F _ {n} = F _ {n - 1} + F _ {n - 2} \quad \mathrm{for} n \geq 2.
$$

(a) Consider the generating function $\textstyle F ( x ) = \sum _ { n = 0 } ^ { \infty } F _ { n } x ^ { n }$ associated to $\{ F _ { n } \}$ , and prove that

$$
F (x) = x ^ {2} F (x) + x F (x) + x
$$

for all x in a neighborhood of 0.

(b) Show that the polynomial $q ( x ) = 1 - x - x ^ { 2 }$ can be factored as

$$
q (x) = (1 - \alpha x) (1 - \beta x),
$$

where α and $\beta$ are the roots of the polynomial $p ( x ) = x ^ { 2 } - x - 1$

(c) Expand the expression for F in partial fractions and obtain

$$
F (x) = \frac {x}{1 - x - x ^ {2}} = \frac {x}{(1 - \alpha x) (1 - \beta x)} = \frac {A}{1 - \alpha x} + \frac {B}{1 - \beta x},
$$

where $A = 1 / ( \alpha - \beta )$ and $B = 1 / ( \beta - \alpha )$

(d) Conclude that $F _ { n } = A \alpha ^ { n } + B \beta ^ { n }$ for $n \geq 0$ . The two roots of $p$ are actually

$$
\alpha = \frac {1 + \sqrt {5}}{2} \quad \mathrm{and} \quad \beta = \frac {1 - \sqrt {5}}{2},
$$

so that $A = 1 / \sqrt { 5 }$ and $B = - 1 / \sqrt { 5 } .$

The number $1 / \alpha = ( \sqrt { 5 } - 1 ) / 2$ , which is known as the golden mean, satisfies the following property: given a line segment $\left[ A C \right]$ of unit length (Figure 2), there exists a unique point B on this segment so that the following proportion holds
:::

::: solution
Let
\[
F(x)=\sum_{n=0}^\infty F_nx^n.
\]
For \(|x|\) sufficiently small, the series converges absolutely. Using \(F_0=0\), \(F_1=1\), and \(F_n=F_{n-1}+F_{n-2}\) for \(n\ge2\),
\[
\begin{aligned}
F(x)
&=x+\sum_{n=2}^\infty(F_{n-1}+F_{n-2})x^n\\
&=x+xF(x)+x^2F(x).
\end{aligned}
\]
Therefore
\[
F(x)=\frac{x}{1-x-x^2}.
\]

Let \(\alpha,\beta\) be the roots of \(t^2-t-1\). Then
\[
\alpha+\beta=1,\qquad \alpha\beta=-1,
\]
so
\[
(1-\alpha x)(1-\beta x)
=1-(\alpha+\beta)x+\alpha\beta x^2
=1-x-x^2.
\]

Write
\[
\frac{x}{(1-\alpha x)(1-\beta x)}
=\frac{A}{1-\alpha x}+\frac{B}{1-\beta x}.
\]
Comparing numerators gives
\[
A+B=0,
\qquad
-A\beta-B\alpha=1,
\]
so
\[
A=\frac1{\alpha-\beta},
\qquad
B=\frac1{\beta-\alpha}.
\]
Expanding both geometric series near \(0\),
\[
F(x)=\sum_{n=0}^\infty(A\alpha^n+B\beta^n)x^n,
\]
and coefficient comparison yields
\[
F_n=A\alpha^n+B\beta^n.
\]
Since
\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\beta=\frac{1-\sqrt5}{2},
\]
we obtain Binet's formula
\[
\boxed{F_n=\frac{\alpha^n-\beta^n}{\sqrt5}}.
\]
:::
