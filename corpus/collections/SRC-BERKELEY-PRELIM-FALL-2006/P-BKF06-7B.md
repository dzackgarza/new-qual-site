---
schema: qual/card@1
id: P-BKF06-7B
kind: problem
title: Uniform limits of continuous maps between metric spaces are continuous
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained epsilon-over-three proof with the
    uniform quantifier separated from continuity at the chosen point.
---

::: {.problem}
Let $X,Y$ be metric spaces and let $f_1,f_2,\ldots:X\to Y$ be continuous.
Suppose $f_n$ converges uniformly to $f$.
Show that $f$ is continuous.
:::

::: {.solution}

Let $d_X$ and $d_Y$ denote the metrics on $X$ and $Y$.

::: pf

::: {.pf-step #uniform-convergence-N}
Fix $x\in X$ and $\epsilon>0$. There exists an index $N$ such
that
$$
d_Y(f_N(t),f(t))<\frac{\epsilon}{3}
$$
for every $t\in X$.

::: pf-proof
This is exactly uniform convergence of $f_n$ to $f$, applied with
$\epsilon/3$.
:::

:::

::: {.pf-step #fN-continuity-delta}
There exists $\delta>0$ such that
$$
d_X(x,x')<\delta
$$
implies
$$
d_Y(f_N(x),f_N(x'))<\frac{\epsilon}{3}.
$$

::: pf-proof
The function $f_N$ is continuous at the fixed point $x$. Apply its
continuity with tolerance $\epsilon/3$.
:::

:::

::: {.pf-step #f-close-bound}
If $d_X(x,x')<\delta$, then
$$
d_Y(f(x),f(x'))<\epsilon.
$$

::: pf-proof
By the triangle inequality and steps [](#uniform-convergence-N){.pf-ref} and [](#fN-continuity-delta){.pf-ref},
$$
\begin{aligned}
d_Y(f(x),f(x'))
&\le
d_Y(f(x),f_N(x))
+d_Y(f_N(x),f_N(x'))
+d_Y(f_N(x'),f(x'))
\\
&<
\frac{\epsilon}{3}
+\frac{\epsilon}{3}
+\frac{\epsilon}{3}
=
\epsilon.
\end{aligned}
$$
The two outer bounds come from step [](#uniform-convergence-N){.pf-ref}, which holds uniformly for
all points of $X$.
:::

:::

::: {.pf-step #f-continuous-at-x}
The function $f$ is continuous at $x$.

::: pf-proof
Step [](#f-close-bound){.pf-ref} gives the $\epsilon$--$\delta$ condition for continuity at
$x$.
:::

:::

::: {.pf-step #f-continuous-on-X}
Therefore
$$
\boxed{f\text{ is continuous on }X}.
$$

::: pf-proof
The point $x\in X$ in step [](#uniform-convergence-N){.pf-ref} was arbitrary.
:::

:::

::: pf-qed
Step [](#f-continuous-on-X){.pf-ref} is the required conclusion.
:::

:::

:::
