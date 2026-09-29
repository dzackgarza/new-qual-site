---
schema: qual/card@1
id: P-BERK78S-07
kind: problem
title: A differential inequality forcing a zero solution
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Solved g'=2g by the integrating factor e^{-2x}. For the inequality,
    f'≥0 and f(0)=0 imply f≥0, while
    (e^{-2x}f(x))'=e^{-2x}(f'-2f)≤0 and the same initial value imply
    e^{-2x}f(x)≤0. Thus f is both nonnegative and nonpositive.
---

::: {.problem}
1. Solve
   \[
   g'=2g,\qquad g(0)=a,
   \]
   where $a$ is a real constant.
2. Suppose $f:[0,1]\to\mathbb R$ is continuous, $f(0)=0$, and $f$ is differentiable for $0<x<1$ with
   \[
   0\le f'(x)\le2f(x).
   \]
   Prove that $f$ is identically zero.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every solution of
$$
g'=2g
$$
satisfies
$$
\frac{d}{dx}\left(e^{-2x}g(x)\right)=0.
$$

::: pf-proof

By the product rule,
$$
\begin{aligned}
\frac{d}{dx}\left(e^{-2x}g(x)\right)
&=
-2e^{-2x}g(x)
+
e^{-2x}g'(x)\\
&=
e^{-2x}(g'(x)-2g(x))\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The unique solution of
$$
g'=2g,
\qquad
g(0)=a,
$$
is
$$
\boxed{
g(x)=ae^{2x}.
}
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
e^{-2x}g(x)
$$
is constant. Evaluating at $x=0$ shows that the constant is
$$
g(0)=a.
$$
Hence
$$
g(x)=ae^{2x}.
$$
Conversely, direct differentiation verifies that this function satisfies
both the differential equation and the initial condition.

:::

:::

::: {.pf-step #s3}

Under the hypotheses of part (2),
$$
f(x)\geq0
$$
for every $x\in[0,1]$.

::: pf-proof

For
$$
0<x<1,
$$
the hypothesis gives
$$
f'(x)\geq0.
$$
Hence $f$ is nondecreasing on $[0,1]$. Since
$$
f(0)=0,
$$
it follows that
$$
f(x)\geq0
$$
for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s4}

Define
$$
h(x)=e^{-2x}f(x).
$$
Then
$$
h'(x)\leq0
$$
for
$$
0<x<1.
$$

::: pf-proof

By the product rule,
$$
\begin{aligned}
h'(x)
&=
-2e^{-2x}f(x)
+
e^{-2x}f'(x)\\
&=
e^{-2x}(f'(x)-2f(x)).
\end{aligned}
$$
The hypothesis
$$
f'(x)\leq2f(x)
$$
and positivity of $e^{-2x}$ give
$$
h'(x)\leq0.
$$

:::

:::

::: {.pf-step #s5}

For every $x\in[0,1]$,
$$
h(x)\leq0.
$$

::: pf-proof

Step [](#s4){.pf-ref} shows that $h$ is nonincreasing. Also
$$
h(0)
=
e^0f(0)
=
0.
$$
Therefore
$$
h(x)\leq h(0)=0
$$
for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s6}

For every $x\in[0,1]$,
$$
f(x)\leq0.
$$

::: pf-proof

Since
$$
f(x)=e^{2x}h(x)
$$
and $e^{2x}>0$, step [](#s5){.pf-ref} gives
$$
f(x)\leq0.
$$

:::

:::

::: {.pf-step #s7}

The function $f$ is identically zero on $[0,1]$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s6){.pf-ref} give
$$
0\leq f(x)\leq0
$$
for every $x\in[0,1]$. Hence
$$
\boxed{
f(x)=0
}
$$
for every $x\in[0,1]$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} solves part (1), and step [](#s7){.pf-ref} proves part (2).

:::

:::

:::
