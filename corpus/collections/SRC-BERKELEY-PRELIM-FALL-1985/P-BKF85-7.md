---
schema: qual/card@1
id: P-BKF85-7
kind: problem
title: Divergence to infinity for an autonomous ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md; Flash drops the leading $0$ in the domain and garbles “as $t\to+\infty$,” both restored from the deterministic sentence structure.
---

::: {.problem}
Let $y(t)$ be a real-valued solution, defined for
\[
0<t<\infty,
\]
of
\[
\frac{dy}{dt}=e^{-y}-e^{-3y}+e^{-5y}.
\]
Show that
\[
y(t)\longrightarrow+\infty
\qquad\text{as }t\to+\infty.
\]
:::

::: {.solution}
Define
$$
F(y)\coloneqq e^{-y}-e^{-3y}+e^{-5y}.
$$

<1>1. One has
$$
F(y)>0
$$
for every $y\in\RR$.

::: {.proof}
Set
$$
u=e^{-2y}>0.
$$
Then
$$
F(y)
=
e^{-y}(1-u+u^2).
$$
Moreover,
$$
1-u+u^2
=
\left(u-\frac12\right)^2+\frac34
>0.
$$
Since $e^{-y}>0$, it follows that $F(y)>0$.
:::

<1>2. The solution $y(t)$ is strictly increasing on $(0,\infty)$.

::: {.proof}
The differential equation and step <1>1 give
$$
y'(t)=F(y(t))>0
$$
for every $t>0$.
:::

<1>3. The function $y$ cannot be bounded above.

::: {.proof}
Suppose instead that $y$ were bounded above. By step <1>2, $y$ is increasing, so there would be a finite limit
$$
L\coloneqq\lim_{t\to\infty}y(t)\in\RR.
$$
By continuity of $F$ and step <1>1,
$$
F(L)>0.
$$
Hence there exist $c>0$ and $T>0$ such that
$$
F(y(t))\geq c
$$
for all $t\geq T$. Therefore
$$
y'(t)\geq c
$$
for $t\geq T$, and integration gives
$$
y(t)\geq y(T)+c(t-T).
$$
The right-hand side tends to $+\infty$, contradicting the assumed boundedness of $y$.
:::

<1>4. One has
$$
\lim_{t\to\infty}y(t)=+\infty.
$$

::: {.proof}
By step <1>2, $y$ is increasing. By step <1>3, it is not bounded above. An increasing real-valued function that is unbounded above tends to $+\infty$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
