---
schema: qual/card@1
id: P-BKF97-1
kind: problem
title: Convergence of the recurrence $x_{n+1}=1/(2+x_n)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the map x↦1/(2+x), whose derivative has absolute value at most 1/4
    on the nonnegative axis, to obtain geometric decay of successive
    differences; the positive fixed point is sqrt(2)-1.
---

::: {.problem}
Define a sequence of real numbers by
\[
x_0=1,
\qquad
x_{n+1}=\frac1{2+x_n}\quad(n\ge0).
\]
Show that $(x_n)$ converges, and evaluate its limit.
:::

::: {.solution}
Define
$$
\phi(x)\coloneqq\frac1{2+x}.
$$

<1>1. Every term of the sequence is positive.

::: {.proof}
One has
$$
x_0=1>0.
$$
If $x_n>0$, then
$$
x_{n+1}
=
\frac1{2+x_n}
>0.
$$
Induction proves the claim.
:::

<1>2. For all $x,y\geq0$,
$$
\abs{\phi(x)-\phi(y)}
\leq
\frac14\abs{x-y}.
$$

::: {.proof}
The derivative is
$$
\phi'(t)
=
-\frac1{(2+t)^2}.
$$
For $t\geq0$,
$$
\abs{\phi'(t)}
\leq
\frac14.
$$
The mean value theorem gives the displayed Lipschitz estimate.
:::

<1>3. For every $n\geq1$,
$$
\abs{x_{n+1}-x_n}
\leq
\left(\frac14\right)^n
\abs{x_1-x_0}.
$$

::: {.proof}
Since
$$
x_{n+1}=\phi(x_n)
$$
and all terms are nonnegative by step <1>1, step <1>2 gives
$$
\abs{x_{n+1}-x_n}
\leq
\frac14\abs{x_n-x_{n-1}}.
$$
Iterating this inequality yields the claimed bound.
:::

<1>4. The sequence $(x_n)$ is Cauchy.

::: {.proof}
If $m>n$, then
$$
\begin{aligned}
\abs{x_m-x_n}
&\leq
\sum_{k=n}^{m-1}\abs{x_{k+1}-x_k}\\
&\leq
\abs{x_1-x_0}
\sum_{k=n}^{\infty}
\left(\frac14\right)^k.
\end{aligned}
$$
The geometric tail tends to zero as $n\to\infty$, uniformly in $m>n$.
Thus $(x_n)$ is Cauchy.
:::

<1>5. The sequence converges to a nonnegative real number $L$ satisfying
$$
L=\frac1{2+L}.
$$

::: {.proof}
The real numbers are complete, so step <1>4 gives
$$
x_n\longrightarrow L
$$
for some $L\in\RR$. Step <1>1 gives $L\geq0$. Passing to the limit in
$$
x_{n+1}=\frac1{2+x_n}
$$
is valid by continuity of $\phi$ and gives the displayed fixed-point
equation.
:::

<1>6. The limit is
$$
\boxed{\sqrt2-1}.
$$

::: {.proof}
The fixed-point equation from step <1>5 is equivalent to
$$
L^2+2L-1=0.
$$
Its two roots are
$$
-1\pm\sqrt2.
$$
Only
$$
\sqrt2-1
$$
is nonnegative, so step <1>5 forces this value.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>4--<1>6 prove convergence and evaluate the limit.
:::
:::
