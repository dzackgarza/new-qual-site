---
schema: qual/card@1
id: P-UCLAB07F-05
kind: problem
title: Polynomial approximation with a prescribed zero and a moment criterion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
(a) Let $f:[0,1]\to\RR$ be continuous with $f(1)=0$.
Show that there is a sequence of polynomials, each vanishing at $1$, that converges uniformly to $f$ on $[0,1]$.

(b) If $f$ is continuous on $[0,1]$ and $$\int_0^1 f(x)(x-1)^k\,dx=0\qquad(k=1,2,\ldots),$$ show that $f\equiv0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

By the Weierstrass approximation theorem, there is a sequence of polynomials $(q_n)$ such that
$$
\|q_n-f\|_\infty\longrightarrow0.
$$


::: pf-proof

The function $f$ is continuous on the compact interval $[0,1]$, so the Weierstrass approximation theorem applies.

:::

:::

::: {.pf-step #s1-2}

Define
$$
p_n(x)=q_n(x)-q_n(1).
$$
Then each $p_n$ is a polynomial satisfying
$$
p_n(1)=0.
$$


::: pf-proof

Subtracting the constant $q_n(1)$ preserves polynomiality, and
$$
p_n(1)=q_n(1)-q_n(1)=0.
$$

:::

:::

::: {.pf-step #s1-3}

If $f(1)=0$, then
$$
\|p_n-f\|_\infty\longrightarrow0.
$$


::: pf-proof

For every $x\in[0,1]$,
$$
\begin{aligned}
|p_n(x)-f(x)|
&=
|q_n(x)-q_n(1)-f(x)|\\
&\le
|q_n(x)-f(x)|+|q_n(1)-f(1)|.
\end{aligned}
$$
Since $f(1)=0$,
$$
|q_n(1)-f(1)|
\le
\|q_n-f\|_\infty.
$$
Therefore
$$
\|p_n-f\|_\infty
\le
2\|q_n-f\|_\infty
\longrightarrow0.
$$
This proves part (a).

:::

:::

::: {.pf-step #s1-4}

Every polynomial $p$ satisfying $p(1)=0$ can be written as
$$
p(x)=\sum_{k=1}^{m}c_k(x-1)^k
$$
for suitable coefficients $c_k$.


::: pf-proof

Expand $p$ in powers of $x-1$:
$$
p(x)=\sum_{k=0}^{m}c_k(x-1)^k.
$$
Evaluating at $x=1$ gives
$$
p(1)=c_0.
$$
Thus $p(1)=0$ implies $c_0=0$.

:::

:::

::: {.pf-step #s1-5}

Under the hypotheses of part (b),
$$
\int_0^1 f(x)p(x)\,dx=0
$$
for every polynomial $p$ with $p(1)=0$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
p(x)=\sum_{k=1}^{m}c_k(x-1)^k.
$$
Using linearity of the integral and the moment hypotheses,
$$
\int_0^1f(x)p(x)\,dx
=
\sum_{k=1}^{m}c_k
\int_0^1f(x)(x-1)^k\,dx
=0.
$$

:::

:::

::: {.pf-step #s1-6}

For every continuous function $g:[0,1]\to\RR$ satisfying $g(1)=0$,
$$
\int_0^1 f(x)g(x)\,dx=0.
$$


::: pf-proof

By part (a), proved in steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, there are polynomials $p_n$ satisfying
$$
p_n(1)=0
$$
and
$$
\|p_n-g\|_\infty\to0.
$$
By step [](#s1-5){.pf-ref},
$$
\int_0^1 f(x)p_n(x)\,dx=0
$$
for every $n$. Since $f$ is continuous on $[0,1]$, it is bounded, and therefore
$$
\left|
\int_0^1 f(x)g(x)\,dx
-
\int_0^1 f(x)p_n(x)\,dx
\right|
\le
\|f\|_\infty\|g-p_n\|_\infty
\longrightarrow0.
$$
Thus
$$
\int_0^1 f(x)g(x)\,dx=0.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
\int_0^1 (1-x)f(x)^2\,dx=0.
$$


::: pf-proof

Apply step [](#s1-6){.pf-ref} to the continuous function
$$
g(x)=(x-1)f(x),
$$
which satisfies $g(1)=0$. Then
$$
0
=
\int_0^1 f(x)(x-1)f(x)\,dx
=
-\int_0^1(1-x)f(x)^2\,dx.
$$

:::

:::

::: {.pf-step #s1-8}

The function $f$ vanishes on $[0,1)$.


::: pf-proof

The function
$$
h(x)=(1-x)f(x)^2
$$
is continuous and nonnegative on $[0,1]$. By step [](#s1-7){.pf-ref}, its integral is zero. Hence $h$ is identically zero.

For every $x<1$, one has $1-x>0$, so
$$
(1-x)f(x)^2=0
$$
implies
$$
f(x)=0.
$$

:::

:::

::: {.pf-step #s1-9}

The function $f$ is identically zero on $[0,1]$.


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
f(x)=0
$$
for all $x<1$. Continuity of $f$ at $1$ gives
$$
f(1)=\lim_{x\to1^-}f(x)=0.
$$
Therefore
$$
\boxed{f\equiv0}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
