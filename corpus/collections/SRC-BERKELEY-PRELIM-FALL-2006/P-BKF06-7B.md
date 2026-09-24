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

<1>1. Fix $x\in X$ and $\epsilon>0$. There exists an index $N$ such
that
$$
d_Y(f_N(t),f(t))<\frac{\epsilon}{3}
$$
for every $t\in X$.

::: {.proof}
This is exactly uniform convergence of $f_n$ to $f$, applied with
$\epsilon/3$.
:::

<1>2. There exists $\delta>0$ such that
$$
d_X(x,x')<\delta
$$
implies
$$
d_Y(f_N(x),f_N(x'))<\frac{\epsilon}{3}.
$$

::: {.proof}
The function $f_N$ is continuous at the fixed point $x$. Apply its
continuity with tolerance $\epsilon/3$.
:::

<1>3. If $d_X(x,x')<\delta$, then
$$
d_Y(f(x),f(x'))<\epsilon.
$$

::: {.proof}
By the triangle inequality and steps <1>1--<1>2,
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
The two outer bounds come from step <1>1, which holds uniformly for
all points of $X$.
:::

<1>4. The function $f$ is continuous at $x$.

::: {.proof}
Step <1>3 gives the $\epsilon$--$\delta$ condition for continuity at
$x$.
:::

<1>5. Therefore
$$
\boxed{f\text{ is continuous on }X}.
$$

::: {.proof}
The point $x\in X$ in step <1>1 was arbitrary.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
