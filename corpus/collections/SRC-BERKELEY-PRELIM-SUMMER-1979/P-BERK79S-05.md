---
schema: qual/card@1
id: P-BERK79S-05
kind: problem
title: A discontinuous derivative and Darboux's intermediate-value property
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The extraction drops the arrow in the source's map f:R->R and renders f' as f 0; the surrounding statement fixes both readings.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For part 1 used f(x)=x^2 sin(1/x), f(0)=0; its derivative exists at
    zero but oscillates between values tending to ±1 along sequences
    approaching zero. For part 2 applied Fermat's theorem to
    h(x)=f(x)-2x: h'(0)<0 forces smaller values just right of zero and
    h'(1)>0 forces smaller values just left of one, so the minimum on
    [0,1] occurs at an interior point where h'=0.
---

::: {.problem}
1. Give an example of a differentiable function $f:\mathbb R\to\mathbb R$ whose derivative $f'$ is not continuous.

2. Let $f$ be differentiable and suppose
   \[
   f'(0)<2<f'(1).
   \]
   Prove that $f'(x)=2$ for some $x\in[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (1), define
$$
f(x)
=
\begin{cases}
x^2\sin(1/x),&x\neq0,\\
0,&x=0.
\end{cases}
$$
Then $f$ is differentiable on $\RR$.

::: pf-proof

For $x\neq0$, the displayed formula is a product of differentiable
functions. At $0$,
$$
\frac{f(h)-f(0)}h
=
h\sin(1/h).
$$
Since
$$
\abs{h\sin(1/h)}
\leq
\abs h
\longrightarrow
0,
$$
the derivative exists and
$$
f'(0)=0.
$$

:::

:::

::: {.pf-step #s2}

For $x\neq0$,
$$
f'(x)
=
2x\sin(1/x)-\cos(1/x).
$$

::: pf-proof

Differentiate
$$
x^2\sin(1/x)
$$
using the product and chain rules:
$$
\begin{aligned}
f'(x)
&=
2x\sin(1/x)
+
x^2\cos(1/x)\left(-\frac1{x^2}\right)\\
&=
2x\sin(1/x)-\cos(1/x).
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The derivative $f'$ from part (1) is not continuous at $0$.

::: pf-proof

Set
$$
x_n=\frac1{2\pi n}.
$$
Then $x_n\to0$ and step [](#s2){.pf-ref} gives
$$
f'(x_n)=-1.
$$
On the other hand, set
$$
y_n=\frac1{(2n+1)\pi}.
$$
Then $y_n\to0$ and
$$
f'(y_n)=1.
$$
Thus $f'(x)$ has no limit as $x\to0$, while step [](#s1){.pf-ref} gives $f'(0)=0$.
Hence $f'$ is discontinuous at $0$.

:::

:::

::: {.pf-step #s4}

For part (2), define
$$
h(x)=f(x)-2x.
$$
Then
$$
h'(0)<0
\qquad\text{and}\qquad
h'(1)>0.
$$

::: pf-proof

Differentiation gives
$$
h'(x)=f'(x)-2.
$$
Therefore the assumptions
$$
f'(0)<2<f'(1)
$$
are exactly the displayed inequalities.

:::

:::

::: {.pf-step #s5}

There is a point $x_0\in(0,1)$ such that
$$
h(x_0)<h(0).
$$

::: pf-proof

Since
$$
h'(0)<0,
$$
the definition of the derivative gives a $\delta>0$ such that for
$$
0<x<\delta,
$$
one has
$$
\frac{h(x)-h(0)}x<0.
$$
Choose such an $x_0$ with $x_0<1$. Since $x_0>0$, the last inequality
implies
$$
h(x_0)<h(0).
$$

:::

:::

::: {.pf-step #s6}

There is a point $x_1\in(0,1)$ such that
$$
h(x_1)<h(1).
$$

::: pf-proof

Since
$$
h'(1)>0,
$$
there is a $\delta>0$ such that whenever
$$
1-\delta<x<1,
$$
one has
$$
\frac{h(x)-h(1)}{x-1}>0.
$$
Choose such an $x_1$ with $x_1>0$. Since $x_1-1<0$, multiplying the last
inequality by $x_1-1$ reverses the sign and gives
$$
h(x_1)-h(1)<0.
$$

:::

:::

::: {.pf-step #s7}

The function $h$ attains its minimum on $[0,1]$ at some point
$$
c\in(0,1).
$$

::: pf-proof

The differentiable function $f$ is continuous, so $h$ is continuous.
Therefore $h$ attains a minimum on the compact interval $[0,1]$.
Step [](#s5){.pf-ref} shows that $0$ is not a minimizer, and step [](#s6){.pf-ref} shows that
$1$ is not a minimizer. Hence some minimizer lies in the open interval.

:::

:::

::: {.pf-step #s8}

There is a point $c\in(0,1)$ such that
$$
\boxed{
f'(c)=2.
}
$$

::: pf-proof

Let $c$ be an interior minimizer from step [](#s7){.pf-ref}. Fermat's theorem gives
$$
h'(c)=0.
$$
By the definition of $h$ in step [](#s4){.pf-ref},
$$
0
=
h'(c)
=
f'(c)-2.
$$
Thus $f'(c)=2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} give the requested example for part (1), and step [](#s8){.pf-ref}
proves part (2).

:::

:::

:::
