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
f(x) = \sum_{n=1}^\infty \frac{\sin nx}{n^{5/2}}
$$

converges for all $x \in \RR$ and that $f(x)$ is a continuous function on $\RR$ with a continuous derivative.
State clearly any facts you assume.
:::

::: {.solution}

For
$$
f_n(x)=\frac{\sin(nx)}{n^{5/2}},
$$
write
$$
f(x)=\sum_{n=1}^\infty f_n(x).
$$

::: pf

::: {.pf-step #s1-1}

The series
$$
\sum_{n=1}^\infty f_n(x)
$$
converges uniformly on $\RR$.


::: pf-proof

For every $x\in\RR$,
$$
\abs{f_n(x)}
\le
\frac1{n^{5/2}}.
$$
The scalar $p$-series
$$
\sum_{n=1}^\infty \frac1{n^{5/2}}
$$
converges.
By the Weierstrass $M$-test, the series of functions converges uniformly on $\RR$.
In particular, it converges for every real $x$.

:::

:::

::: {.pf-step #s1-2}

The limit function
$$
f
$$
is continuous on $\RR$.


::: pf-proof

Each function
$$
f_n(x)=\frac{\sin(nx)}{n^{5/2}}
$$
is continuous.
By step [](#s1-1){.pf-ref}, the series converges uniformly.
A uniform limit of continuous functions is continuous.

:::

:::

::: {.pf-step #s1-3}

Each $f_n$ is continuously differentiable and
$$
f_n'(x)
=
\frac{\cos(nx)}{n^{3/2}}.
$$


::: pf-proof

Differentiate:
$$
\frac d{dx}\sin(nx)=n\cos(nx).
$$
Therefore
$$
\frac d{dx}
\left(
\frac{\sin(nx)}{n^{5/2}}
\right)
=
\frac{n\cos(nx)}{n^{5/2}}
=
\frac{\cos(nx)}{n^{3/2}}.
$$

:::

:::

::: {.pf-step #s1-4}

The derivative series
$$
\sum_{n=1}^\infty f_n'(x)
=
\sum_{n=1}^\infty
\frac{\cos(nx)}{n^{3/2}}
$$
converges uniformly on $\RR$.


::: pf-proof

For every $x$,
$$
\abs{f_n'(x)}
\le
\frac1{n^{3/2}}.
$$
The scalar series
$$
\sum_{n=1}^\infty \frac1{n^{3/2}}
$$
converges.
Thus the Weierstrass $M$-test gives uniform convergence of the derivative series.

:::

:::

::: {.pf-step #s1-5}

The sum $f$ is differentiable and
$$
\boxed{
f'(x)
=
\sum_{n=1}^\infty
\frac{\cos(nx)}{n^{3/2}}
}.
$$


::: pf-proof

Use the standard termwise-differentiation theorem:
if each $f_n$ is $C^1$, if
$$
\sum f_n'(x)
$$
converges uniformly on an interval, and if
$$
\sum f_n(x_0)
$$
converges at one point $x_0$, then
$$
\sum f_n
$$
converges to a differentiable function whose derivative is the sum of the derivative series.

Here step [](#s1-4){.pf-ref} gives uniform convergence of the derivative series on every interval, indeed on all of $\RR$.
Also at
$$
x_0=0,
$$
one has
$$
f_n(0)=0
$$
for every $n$, so
$$
\sum f_n(0)
$$
converges.
Therefore the theorem applies.

:::

:::

::: {.pf-step #s1-6}

The derivative $f'$ is continuous on $\RR$.


::: pf-proof

Each partial derivative term
$$
x\longmapsto
\frac{\cos(nx)}{n^{3/2}}
$$
is continuous.
By step [](#s1-4){.pf-ref}, their series converges uniformly.
Therefore its sum
$$
f'
$$
is continuous.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{f\in C^1(\RR)}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives continuity of $f$.
Step [](#s1-5){.pf-ref} gives differentiability, and step [](#s1-6){.pf-ref} gives continuity of the derivative.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} prove every assertion in the problem.
The facts used are the Weierstrass $M$-test, uniform limits of continuous functions are continuous, and the standard theorem permitting termwise differentiation under uniform convergence of the derivative series.

:::

:::

:::
