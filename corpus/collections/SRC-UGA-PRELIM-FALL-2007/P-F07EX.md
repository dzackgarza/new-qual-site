---
schema: qual/card@1
id: P-F07EX
kind: problem
title: 'Examples: an integral with a corner, a series with divergent squares, and
  a basis of a subspace of $\mathcal{P}_3$'
classification:
  areas:
  - prelim
  topics:
  - Counterexamples
  - Series of Numbers
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give an example (without proof) of each of the following:

a. An integrable function $f: \mathbb{R} \to \mathbb{R}$ so that the function $F(x) = \int_0^x f(t)\,dt$ is differentiable everywhere but at $x = 1$.

b. A sequence $\{a_n\}$ of real numbers such that $\sum_{n=1}^{\infty} a_n$ converges and $\sum_{n=1}^{\infty} a_n^2$ diverges.

c. A basis for the subspace of $\mathcal{P}_3$ spanned by $x^2 + x + 1$, $x^3 - x + 2$, $x^3 + x^2 + 3$, and $-x^3 + x^2 + 2x + 1$.
:::

::: solution
(a) Take
\[
f(t)=\begin{cases}0,&t<1,\\1,&t\ge1.\end{cases}
\]
Then
\[
F(x)=\int_0^x f(t)\,dt
\]
is differentiable for every $x\ne1$ and not differentiable at $x=1$.

(b) Take
\[
a_n=\frac{(-1)^n}{\sqrt n}.
\]
The alternating-series test gives convergence of $\sum a_n$, while
\[
\sum a_n^2=\sum\frac1n
\]
diverges.

(c) Relative to the coefficient basis $(1,x,x^2,x^3)$, the four given polynomials have columns
\[
(1,1,1,0),\ (2,-1,0,1),\ (3,0,1,1),\ (1,2,1,-1).
\]
The first, second, and fourth are linearly independent, and the span of all four has rank $3$. Hence one valid basis is
\[
\boxed{\{x^2+x+1,\ x^3-x+2,\ -x^3+x^2+2x+1\}}.
\]
:::
