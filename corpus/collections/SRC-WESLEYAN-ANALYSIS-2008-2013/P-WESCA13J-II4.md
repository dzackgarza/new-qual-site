---
schema: qual/card@1
id: P-WESCA13J-II4
kind: problem
title: 'Products of uniformly convergent uniformly bounded sequences'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $(f_n)$ and $(g_n)$ converge uniformly on a set $A$.
Suppose both sequences are uniformly bounded: there is $M$ such that $|f_n(z)|,|g_n(z)|\le M$ for every $z\in A$ and $n$.
Prove that $(f_ng_n)$ converges uniformly on $A$.
:::

::: {.solution}

Let
$$
f_n\to f
\qquad\text{and}\qquad
g_n\to g
$$
uniformly on
$$
A.
$$

::: pf

::: {.pf-step #s1-1}

The limits satisfy
$$
\boxed{
|f(z)|\le M,
\qquad
|g(z)|\le M
}
$$
for every
$$
z\in A.
$$


::: pf-proof

Fix
$$
z\in A.
$$
Since
$$
f_n(z)\to f(z)
$$
and
$$
|f_n(z)|\le M
$$
for every
$$
n,
$$
continuity of the absolute value gives
$$
|f(z)|
=
\lim_{n\to\infty}|f_n(z)|
\le M.
$$
The same argument gives
$$
|g(z)|\le M.
$$

:::

:::

::: {.pf-step #s1-2}

For every
$$
z\in A
$$
and every
$$
n,
$$
one has
$$
|f_n(z)g_n(z)-f(z)g(z)|
\le
M|g_n(z)-g(z)|
+
M|f_n(z)-f(z)|.
$$


::: pf-proof

Add and subtract
$$
f_n(z)g(z):
$$
$$
\begin{aligned}
f_n g_n-fg
&=
f_n(g_n-g)
+g(f_n-f).
\end{aligned}
$$
Taking absolute values and using
$$
|f_n(z)|\le M
$$
together with step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
|f_n g_n-fg|
&\le
|f_n||g_n-g|
+|g||f_n-f|\\
&\le
M|g_n-g|
+M|f_n-f|.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Taking suprema over
$$
A
$$
gives
$$
\|f_ng_n-fg\|_{\infty}
\le
M\|g_n-g\|_{\infty}
+
M\|f_n-f\|_{\infty}.
$$


::: pf-proof

The pointwise inequality of step [](#s1-2){.pf-ref} holds for every
$$
z\in A.
$$
Taking the supremum of the left-hand side and bounding the supremum of the sum by the sum of the suprema yields the estimate.

:::

:::

::: {.pf-step #s1-4}

The right-hand side in step [](#s1-3){.pf-ref} tends to
$$
0.
$$


::: pf-proof

Uniform convergence means precisely that
$$
\|f_n-f\|_{\infty}\to0
$$
and
$$
\|g_n-g\|_{\infty}\to0.
$$
Multiplication by the fixed constant
$$
M
$$
preserves convergence to zero, and so does addition.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f_ng_n\to fg
\text{ uniformly on }A.}
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\|f_ng_n-fg\|_{\infty}
\longrightarrow0,
$$
which is the definition of uniform convergence.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required conclusion.

:::

:::

:::
