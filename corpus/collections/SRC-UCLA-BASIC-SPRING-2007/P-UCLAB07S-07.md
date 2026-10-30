---
schema: qual/card@1
id: P-UCLAB07S-07
kind: problem
title: Quadratic convergence of Newton iteration near a simple root
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $f\colon\RR\to\RR$ be twice continuously differentiable with uniformly bounded second derivative and a simple root $x^*$, so $f(x^*)=0$ and $f'(x^*)\ne0$.
For Newton iteration
$$
x_n=F(x_{n-1}),\qquad F(x)=x-\frac{f(x)}{f'(x)},
$$
prove that if $x_0$ is sufficiently close to $x^*$, then there is a constant $C$ such that
$$
\abs{x_n-x^*}\le C\abs{x_{n-1}-x^*}^2
$$
for all $n$.
:::

::: {.solution}

Let
$$
M=\sup_{x\in\RR}\abs{f''(x)}<\infty.
$$

::: pf

::: {.pf-step #s1-1}

There exists $\delta>0$ such that
$$
\abs{f'(x)}\ge \frac{\abs{f'(x^*)}}{2}
$$
whenever
$$
\abs{x-x^*}\le\delta.
$$


::: pf-proof

Since $f'$ is continuous and
$$
f'(x^*)\ne0,
$$
there exists $\delta>0$ such that
$$
\abs{f'(x)-f'(x^*)}
<
\frac{\abs{f'(x^*)}}{2}
$$
whenever
$$
\abs{x-x^*}\le\delta.
$$
Then
$$
\abs{f'(x)}
\ge
\abs{f'(x^*)}
-
\abs{f'(x)-f'(x^*)}
>
\frac{\abs{f'(x^*)}}{2}.
$$

:::

:::

::: {.pf-step #s1-2}

For every $x$ with
$$
\abs{x-x^*}\le\delta,
$$
Taylor's theorem gives
$$
f(x^*)
=
f(x)+f'(x)(x^*-x)
+
\frac12 f''(\xi)(x^*-x)^2
$$
for some $\xi$ between $x$ and $x^*$.


::: pf-proof

Apply Taylor's theorem with Lagrange remainder to $f$ centered at $x$ and evaluated at $x^*$.
The hypotheses hold because $f\in C^2(\RR)$.

:::

:::

::: {.pf-step #s1-3}

Since
$$
f(x^*)=0,
$$
one has
$$
F(x)-x^*
=
\frac{f''(\xi)}{2f'(x)}
(x-x^*)^2
$$
for some $\xi$ between $x$ and $x^*$.


::: pf-proof

From step [](#s1-2){.pf-ref} and
$$
f(x^*)=0,
$$
one gets
$$
0
=
f(x)-f'(x)(x-x^*)
+
\frac12f''(\xi)(x-x^*)^2.
$$
Thus
$$
f(x)
=
f'(x)(x-x^*)
-
\frac12f''(\xi)(x-x^*)^2.
$$
Now
$$
\begin{aligned}
F(x)-x^*
&=
x-x^*
-
\frac{f(x)}{f'(x)}\\
&=
x-x^*
-
\left(
x-x^*
-
\frac{f''(\xi)}{2f'(x)}
(x-x^*)^2
\right)\\
&=
\frac{f''(\xi)}{2f'(x)}
(x-x^*)^2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For all $x$ with
$$
\abs{x-x^*}\le\delta,
$$
one has
$$
\boxed{
\abs{F(x)-x^*}
\le
C\abs{x-x^*}^2
}
$$
with
$$
C=\frac{M}{\abs{f'(x^*)}}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\abs{F(x)-x^*}
\le
\frac{\abs{f''(\xi)}}{2\abs{f'(x)}}
\abs{x-x^*}^2.
$$
The bound on $f''$ gives
$$
\abs{f''(\xi)}\le M,
$$
while step [](#s1-1){.pf-ref} gives
$$
2\abs{f'(x)}
\ge
\abs{f'(x^*)}.
$$
Hence
$$
\frac{\abs{f''(\xi)}}{2\abs{f'(x)}}
\le
\frac{M}{\abs{f'(x^*)}}
=C.
$$

:::

:::

::: {.pf-step #s1-5}

Shrink $\delta$ if necessary so that
$$
C\delta\le1.
$$
Then
$$
\abs{x-x^*}\le\delta
$$
implies
$$
\abs{F(x)-x^*}\le\delta.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\abs{F(x)-x^*}
\le
C\abs{x-x^*}^2
\le
C\delta\abs{x-x^*}
\le
\abs{x-x^*}
\le
\delta.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
\abs{x_0-x^*}\le\delta,
$$
then every Newton iterate $x_n$ is defined and satisfies
$$
\abs{x_n-x^*}\le\delta.
$$


::: pf-proof

Proceed by induction.
The assertion holds for $n=0$ by hypothesis.
Suppose
$$
\abs{x_{n-1}-x^*}\le\delta.
$$
Then step [](#s1-1){.pf-ref} gives
$$
f'(x_{n-1})\ne0,
$$
so the Newton step is defined.
Step [](#s1-5){.pf-ref} then gives
$$
\abs{x_n-x^*}
=
\abs{F(x_{n-1})-x^*}
\le
\delta.
$$

:::

:::

::: {.pf-step #s1-7}

For every $n\ge1$,
$$
\boxed{
\abs{x_n-x^*}
\le
C\abs{x_{n-1}-x^*}^2
}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, every iterate
$$
x_{n-1}
$$
lies within distance $\delta$ of $x^*$.
Therefore step [](#s1-4){.pf-ref} applies to
$$
x=x_{n-1},
$$
giving
$$
\abs{x_n-x^*}
=
\abs{F(x_{n-1})-x^*}
\le
C\abs{x_{n-1}-x^*}^2.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required quadratic error estimate for all Newton iterates starting sufficiently close to the simple root.

:::

:::

:::
