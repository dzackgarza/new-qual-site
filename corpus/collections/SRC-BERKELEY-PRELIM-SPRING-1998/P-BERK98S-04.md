---
schema: qual/card@1
id: P-BERK98S-04
kind: problem
title: A nonnegative continuous function with zero integral vanishes identically
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
  date: 2026-09-23
---

::: {.problem}
Using properties of the Riemann integral, prove that if $f:[0,1]\to\mathbb R$ is continuous and nonnegative and
\[
\int_0^1f(x)\,dx=0,
\]
then $f(x)=0$ for every $x\in[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose, for contradiction, that there is a point $x_0\in[0,1]$
with
$$
f(x_0)>0.
$$

::: pf-proof

This is the negation of the desired conclusion because $f$ is nonnegative.

:::

:::

::: {.pf-step #s2}

There are numbers $a,b$ with
$$
0\leq a<b\leq1
$$
such that
$$
f(x)\geq\frac{f(x_0)}2
\qquad(a\leq x\leq b).
$$

::: pf-proof

By continuity of $f$ at $x_0$, there is $\delta>0$ such that
$$
\abs{x-x_0}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(x_0)}<\frac{f(x_0)}2.
$$
Set
$$
a\coloneqq\max\left\{0,x_0-\frac\delta2\right\},
\qquad
b\coloneqq\min\left\{1,x_0+\frac\delta2\right\}.
$$
Then $a<b$, and every $x\in[a,b]$ satisfies
$\abs{x-x_0}<\delta$. Hence
$$
f(x)
>f(x_0)-\frac{f(x_0)}2
=\frac{f(x_0)}2,
$$
which gives the claimed weak inequality.

:::

:::

::: {.pf-step #s3}

The integral of $f$ over $[0,1]$ is strictly positive.

::: pf-proof

Since $f\geq0$ on $[0,1]$, step [](#s2){.pf-ref} and monotonicity of the Riemann
integral give
$$
\begin{aligned}
\int_0^1 f(x)\,dx
&\geq\int_a^b f(x)\,dx\\
&\geq\int_a^b \frac{f(x_0)}2\,dx\\
&=\frac{f(x_0)}2(b-a)\\
&>0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

The assumption in step [](#s1){.pf-ref} is impossible.

::: pf-proof

Step [](#s3){.pf-ref} contradicts the hypothesis
$$
\int_0^1 f(x)\,dx=0.
$$

:::

:::

::: {.pf-step #s5}

Therefore $f(x)=0$ for every $x\in[0,1]$.

::: pf-proof

The function is nonnegative by hypothesis, and step [](#s4){.pf-ref} shows that it is
never positive. Hence it vanishes identically.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
