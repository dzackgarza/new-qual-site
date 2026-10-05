---
schema: qual/card@1
id: P-UCLAB06S-03
kind: problem
title: Continuous differentiability of $\sum\frac{\sin nx}{n^{5/2}}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 3 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
Prove that the series

$$
f ( x ) = \sum _ { n = 1 } ^ { \infty } { \frac { \sin n x } { n ^ { 5 / 2 } } }
$$

converges for all $x \in \mathbf { R }$ and that $f ( x )$ is a continuous function on $\mathbf { R }$ with a continuous derivative.
State clearly any facts you assume.
:::

::: {.solution}
For
\[
f_n(x)=\frac{\sin(nx)}{n^{5/2}},
\]
write
\[
f(x)=\sum_{n=1}^\infty f_n(x).
\]

<1>1. The series
\[
\sum_{n=1}^\infty f_n(x)
\]
converges uniformly on $\mathbb R$.

::: {.proof}
For every $x\in\mathbb R$,
\[
|f_n(x)|
\le
\frac1{n^{5/2}}.
\]
The scalar $p$-series
\[
\sum_{n=1}^\infty \frac1{n^{5/2}}
\]
converges.
By the Weierstrass $M$-test, the series of functions converges uniformly on $\mathbb R$.
In particular, it converges for every real $x$.
:::

<1>2. The limit function
\[
f
\]
is continuous on $\mathbb R$.

::: {.proof}
Each function
\[
f_n(x)=\frac{\sin(nx)}{n^{5/2}}
\]
is continuous.
By step <1>1, the series converges uniformly.
A uniform limit of continuous functions is continuous.
:::

<1>3. Each $f_n$ is continuously differentiable and
\[
f_n'(x)
=
\frac{\cos(nx)}{n^{3/2}}.
\]

::: {.proof}
Differentiate:
\[
\frac d{dx}\sin(nx)=n\cos(nx).
\]
Therefore
\[
\frac d{dx}
\left(
\frac{\sin(nx)}{n^{5/2}}
\right)
=
\frac{n\cos(nx)}{n^{5/2}}
=
\frac{\cos(nx)}{n^{3/2}}.
\]
:::

<1>4. The derivative series
\[
\sum_{n=1}^\infty f_n'(x)
=
\sum_{n=1}^\infty
\frac{\cos(nx)}{n^{3/2}}
\]
converges uniformly on $\mathbb R$.

::: {.proof}
For every $x$,
\[
|f_n'(x)|
\le
\frac1{n^{3/2}}.
\]
The scalar series
\[
\sum_{n=1}^\infty \frac1{n^{3/2}}
\]
converges.
Thus the Weierstrass $M$-test gives uniform convergence of the derivative series.
:::

<1>5. The sum $f$ is differentiable and
\[
\boxed{
f'(x)
=
\sum_{n=1}^\infty
\frac{\cos(nx)}{n^{3/2}}
}.
\]

::: {.proof}
Use the standard termwise-differentiation theorem:
if each $f_n$ is $C^1$, if
\[
\sum f_n'(x)
\]
converges uniformly on an interval, and if
\[
\sum f_n(x_0)
\]
converges at one point $x_0$, then
\[
\sum f_n
\]
converges to a differentiable function whose derivative is the sum of the derivative series.

Here step <1>4 gives uniform convergence of the derivative series on every interval, indeed on all of $\mathbb R$.
Also at
\[
x_0=0,
\]
one has
\[
f_n(0)=0
\]
for every $n$, so
\[
\sum f_n(0)
\]
converges.
Therefore the theorem applies.
:::

<1>6. The derivative $f'$ is continuous on $\mathbb R$.

::: {.proof}
Each partial derivative term
\[
x\longmapsto
\frac{\cos(nx)}{n^{3/2}}
\]
is continuous.
By step <1>4, their series converges uniformly.
Therefore its sum
\[
f'
\]
is continuous.
:::

<1>7. Hence
\[
\boxed{f\in C^1(\mathbb R)}.
\]

::: {.proof}
Step <1>2 gives continuity of $f$.
Step <1>5 gives differentiability, and step <1>6 gives continuity of the derivative.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 prove every assertion in the problem.
The facts used are the Weierstrass $M$-test, uniform limits of continuous functions are continuous, and the standard theorem permitting termwise differentiation under uniform convergence of the derivative series.
:::
:::
