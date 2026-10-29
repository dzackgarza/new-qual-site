---
schema: qual/card@1
id: P-UCLAB14F-03
kind: problem
title: Pointwise monotone convergence to a continuous limit is uniform
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 3. Let $f_n:[0,1]\to\RR$ be monotonically increasing continuous functions. Assume that $f_n$ converge pointwise to a continuous function $f:[0,1]\to\RR$. Prove that $f_n$ converge uniformly to $f$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The pointwise limit $f$ is nondecreasing.


::: pf-proof

If
$$
x\le y,
$$
then for every $n$,
$$
f_n(x)\le f_n(y).
$$
Taking $n\to\infty$ and using pointwise convergence gives
$$
f(x)\le f(y).
$$

:::

:::

::: pf-step

Fix $\varepsilon>0$.
There is a partition
$$
0=x_0<x_1<\cdots<x_m=1
$$
such that
$$
f(x_j)-f(x_{j-1})
<
\frac{\varepsilon}{3}
$$
for every $j$.


::: pf-proof

The function $f$ is continuous on the compact interval $[0,1]$, hence uniformly continuous.
Choose $\delta>0$ such that
$$
|x-y|<\delta
$$
implies
$$
|f(x)-f(y)|<\frac{\varepsilon}{3}.
$$
Choose a partition whose mesh is smaller than $\delta$.
Since $f$ is nondecreasing by step [](#s1-1){.pf-ref},
$$
0\le f(x_j)-f(x_{j-1})<\frac{\varepsilon}{3}.
$$

:::

:::

::: pf-step

There exists $N$ such that for every $n\ge N$ and every partition point $x_j$,
$$
|f_n(x_j)-f(x_j)|
<
\frac{\varepsilon}{3}.
$$


::: pf-proof

For each fixed $j$, pointwise convergence gives an index $N_j$ such that the displayed inequality holds for all $n\ge N_j$.
There are only finitely many partition points.
Take
$$
N=\max_j N_j.
$$

:::

:::

::: {.pf-step #s1-4}

Let $n\ge N$ and
$$
x_{j-1}\le x\le x_j.
$$
Then
$$
f_n(x)-f(x)<\frac{2\varepsilon}{3}.
$$


::: pf-proof

Monotonicity of $f_n$ gives
$$
f_n(x)\le f_n(x_j),
$$
while monotonicity of $f$ gives
$$
f(x)\ge f(x_{j-1}).
$$
Therefore
$$
\begin{aligned}
f_n(x)-f(x)
&\le
f_n(x_j)-f(x_{j-1})\\
&=
\bigl(f_n(x_j)-f(x_j)\bigr)
+
\bigl(f(x_j)-f(x_{j-1})\bigr)\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

Under the same hypotheses,
$$
f(x)-f_n(x)<\frac{2\varepsilon}{3}.
$$


::: pf-proof

Monotonicity gives
$$
f(x)\le f(x_j)
$$
and
$$
f_n(x)\ge f_n(x_{j-1}).
$$
Hence
$$
\begin{aligned}
f(x)-f_n(x)
&\le
f(x_j)-f_n(x_{j-1})\\
&=
\bigl(f(x_j)-f(x_{j-1})\bigr)
+
\bigl(f(x_{j-1})-f_n(x_{j-1})\bigr)\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

For every $n\ge N$ and every $x\in[0,1]$,
$$
|f_n(x)-f(x)|<\varepsilon.
$$


::: pf-proof

Choose the partition interval containing $x$.
Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} give
$$
-\frac{2\varepsilon}{3}
<
f_n(x)-f(x)
<
\frac{2\varepsilon}{3}.
$$
Thus
$$
|f_n(x)-f(x)|
<
\frac{2\varepsilon}{3}
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{f_n\to f\text{ uniformly on }[0,1]}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} is exactly the definition of uniform convergence.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
