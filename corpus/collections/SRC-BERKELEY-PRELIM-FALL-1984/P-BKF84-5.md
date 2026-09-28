---
schema: qual/card@1
id: P-BKF84-5
kind: problem
title: Small initial data for a nonlinear scalar ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the global Lipschitz bound on the strip $0\le x\le1$ and the Gronwall estimate against the zero solution.
---

::: {.problem}
Consider
\[
\frac{dy}{dx}=3xy+\frac{y}{1+y^2}.
\]
Prove:

1. for each $n=1,2,\ldots$ there is a unique solution $y=f_n(x)$ on $0\le x\le1$ satisfying $f_n(0)=1/n$;

2.
\[
\lim_{n\to\infty}f_n(1)=0.
\]
:::

::: {.solution}
Set
$$
F(x,y)
\coloneqq
3xy+\frac{y}{1+y^2}.
$$

<1>1. On the strip
$$
0\leq x\leq1,
\qquad
y\in\RR,
$$
the function $F$ is globally Lipschitz in $y$, with Lipschitz constant
$4$.

::: {.proof}
Differentiate with respect to $y$:
$$
\frac{\partial F}{\partial y}(x,y)
=
3x+\frac{1-y^2}{(1+y^2)^2}.
$$
For every real $y$,
$$
\left|
\frac{1-y^2}{(1+y^2)^2}
\right|
\leq
\frac{1+y^2}{(1+y^2)^2}
\leq1.
$$
Hence, for $0\leq x\leq1$,
$$
\left|
\frac{\partial F}{\partial y}(x,y)
\right|
\leq4.
$$
The mean value theorem in the $y$ variable gives
$$
\abs{F(x,y_1)-F(x,y_2)}
\leq
4\abs{y_1-y_2}.
$$
:::

<1>2. For every positive integer $n$, there is a unique solution
$$
f_n:[0,1]\longrightarrow\RR
$$
of
$$
f_n'(x)=F(x,f_n(x)),
\qquad
f_n(0)=\frac1n.
$$

::: {.proof}
The function $F$ is continuous on $[0,1]\times\RR$ and globally
Lipschitz in $y$ by step <1>1. The global Picard--Lindelöf theorem
therefore gives a unique solution throughout the whole interval
$[0,1]$ for every initial value.
:::

<1>3. For every $n$ and every $x\in[0,1]$,
$$
\abs{f_n(x)}
\leq
\frac{e^{4x}}n.
$$

::: {.proof}
The identically zero function is also a solution because
$$
F(x,0)=0.
$$
Using the integral equation for $f_n$ and step <1>1,
$$
\begin{aligned}
\abs{f_n(x)}
&=
\left|
\frac1n
+
\int_0^x
\bigl(F(t,f_n(t))-F(t,0)\bigr)
\,dt
\right|\\
&\leq
\frac1n
+
4\int_0^x\abs{f_n(t)}\,dt.
\end{aligned}
$$
Gronwall's inequality gives
$$
\abs{f_n(x)}
\leq
\frac1n e^{4x}.
$$
:::

<1>4. One has
$$
\boxed{
\lim_{n\to\infty}f_n(1)=0
}.
$$

::: {.proof}
Step <1>3 gives
$$
\abs{f_n(1)}
\leq
\frac{e^4}{n},
$$
and the right-hand side tends to $0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 proves Part (1), and step <1>4 proves Part (2).
:::
:::
