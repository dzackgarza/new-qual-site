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
|x_n-x^*|\le C|x_{n-1}-x^*|^2
$$
for all $n$.
:::

::: {.solution}

Let
$$
M=\sup_{x\in\RR}|f''(x)|<\infty.
$$

::: pf

::: {.pf-step #s1-1}

There exists $\delta>0$ such that
$$
|f'(x)|\ge \frac{|f'(x^*)|}{2}
$$
whenever
$$
|x-x^*|\le\delta.
$$


::: pf-proof

Since $f'$ is continuous and
$$
f'(x^*)\ne0,
$$
there exists $\delta>0$ such that
$$
|f'(x)-f'(x^*)|
<
\frac{|f'(x^*)|}{2}
$$
whenever
$$
|x-x^*|\le\delta.
$$
Then
$$
|f'(x)|
\ge
|f'(x^*)|
-
|f'(x)-f'(x^*)|
>
\frac{|f'(x^*)|}{2}.
$$

:::

:::

::: {.pf-step #s1-2}

For every $x$ with
$$
|x-x^*|\le\delta,
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
|x-x^*|\le\delta,
$$
one has
$$
\boxed{
|F(x)-x^*|
\le
C|x-x^*|^2
}
$$
with
$$
C=\frac{M}{|f'(x^*)|}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
|F(x)-x^*|
\le
\frac{|f''(\xi)|}{2|f'(x)|}
|x-x^*|^2.
$$
The bound on $f''$ gives
$$
|f''(\xi)|\le M,
$$
while step [](#s1-1){.pf-ref} gives
$$
2|f'(x)|
\ge
|f'(x^*)|.
$$
Hence
$$
\frac{|f''(\xi)|}{2|f'(x)|}
\le
\frac{M}{|f'(x^*)|}
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
|x-x^*|\le\delta
$$
implies
$$
|F(x)-x^*|\le\delta.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
|F(x)-x^*|
\le
C|x-x^*|^2
\le
C\delta|x-x^*|
\le
|x-x^*|
\le
\delta.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
|x_0-x^*|\le\delta,
$$
then every Newton iterate $x_n$ is defined and satisfies
$$
|x_n-x^*|\le\delta.
$$


::: pf-proof

Proceed by induction.
The assertion holds for $n=0$ by hypothesis.
Suppose
$$
|x_{n-1}-x^*|\le\delta.
$$
Then step [](#s1-1){.pf-ref} gives
$$
f'(x_{n-1})\ne0,
$$
so the Newton step is defined.
Step [](#s1-5){.pf-ref} then gives
$$
|x_n-x^*|
=
|F(x_{n-1})-x^*|
\le
\delta.
$$

:::

:::

::: {.pf-step #s1-7}

For every $n\ge1$,
$$
\boxed{
|x_n-x^*|
\le
C|x_{n-1}-x^*|^2
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
|x_n-x^*|
=
|F(x_{n-1})-x^*|
\le
C|x_{n-1}-x^*|^2.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required quadratic error estimate for all Newton iterates starting sufficiently close to the simple root.

:::

:::

:::
