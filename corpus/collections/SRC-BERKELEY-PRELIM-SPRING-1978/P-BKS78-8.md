---
schema: qual/card@1
id: P-BKS78-8
kind: problem
title: Local existence and finite-time obstruction for $x'=x^2+t^2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Consider
$$
x'=x^2+t^2,\qquad x(0)=1.
$$

1. Prove that there is a solution on $[0,b]$ for some $b>0$.
2. Give an explicit such $b$.
3. Find $c>0$ such that no solution exists on $[0,c]$.
:::

::: {.solution}
Let
$$
b\coloneqq\frac15
$$
and define
$$
\mathcal X
\coloneqq
\left\{
\varphi\in C([0,b]):
\norm{\varphi-1}_\infty\leq\frac12
\right\}.
$$

::: pf

::: {.pf-step #complete-space}
The metric space $\mathcal X$, with the sup norm, is complete.

::: pf-proof
The space $C([0,b])$ with the sup norm is Banach. The set $\mathcal X$ is the closed ball of radius $1/2$ centered at the constant function $1$, hence is a closed subset of a complete metric space and is therefore complete.
:::

:::

::: {.pf-step #self-map}
Define
$$
(T\varphi)(t)
\coloneqq
1+\int_0^t
\bigl(\varphi(s)^2+s^2\bigr)\,ds.
$$
Then
$$
T(\mathcal X)\subseteq\mathcal X.
$$

::: pf-proof
If $\varphi\in\mathcal X$, then
$$
\frac12\leq\varphi(s)\leq\frac32
$$
for $0\leq s\leq b$. Therefore, for such $t$,
$$
\begin{aligned}
0
\leq
(T\varphi)(t)-1
&=
\int_0^t(\varphi(s)^2+s^2)\,ds\\
&\leq
\frac15
\left(
\frac94+\frac1{25}
\right)\\
&=
\frac{229}{500}
<
\frac12.
\end{aligned}
$$
Hence
$$
\norm{T\varphi-1}_\infty<\frac12,
$$
so $T\varphi\in\mathcal X$.
:::

:::

::: {.pf-step #contraction}
The map $T:\mathcal X\to\mathcal X$ is a contraction with contraction constant $3/5$.

::: pf-proof
If $\varphi,\psi\in\mathcal X$, then
$$
\abs{\varphi(s)},\abs{\psi(s)}\leq\frac32.
$$
Thus
$$
\begin{aligned}
\abs{(T\varphi)(t)-(T\psi)(t)}
&\leq
\int_0^t
\abs{\varphi(s)^2-\psi(s)^2}\,ds\\
&\leq
\int_0^t
\abs{\varphi(s)+\psi(s)}
\abs{\varphi(s)-\psi(s)}\,ds\\
&\leq
3t\,\norm{\varphi-\psi}_\infty\\
&\leq
\frac35\norm{\varphi-\psi}_\infty.
\end{aligned}
$$
Taking the supremum over $t\in[0,b]$ gives the claim.
:::

:::

::: {.pf-step #fixed-point}
There is a unique $x\in\mathcal X$ satisfying
$$
x=Tx.
$$

::: pf-proof
By [](#complete-space){.pf-ref}, [](#self-map){.pf-ref}, and [](#contraction){.pf-ref}, $T$ is a contraction of the complete metric space $\mathcal X$ into itself. The Banach fixed-point theorem therefore gives a unique fixed point.
:::

:::

::: pf-step
The fixed point from [](#fixed-point){.pf-ref} is a solution of
$$
x'=x^2+t^2,
\qquad
x(0)=1
$$
on
$$
\boxed{[0,1/5]}.
$$

::: pf-proof
The fixed-point identity is
$$
x(t)
=
1+\int_0^t
\bigl(x(s)^2+s^2\bigr)\,ds.
$$
The integrand is continuous, so the fundamental theorem of calculus gives
$$
x'(t)=x(t)^2+t^2.
$$
At $t=0$ the integral vanishes, giving $x(0)=1$. Thus part 1 holds, and the explicit value
$$
\boxed{b=\frac15}
$$
answers part 2.
:::

:::

::: {.pf-step #positive-solution}
Any solution on an interval $[0,c]$ is positive and nondecreasing there.

::: pf-proof
The differential equation gives
$$
x'(t)=x(t)^2+t^2\geq0.
$$
Hence
$$
x(t)\geq x(0)=1
$$
throughout its interval of existence.
:::

:::

::: {.pf-step #no-solution}
No solution exists on $[0,1]$.

::: pf-proof
Suppose a solution existed on $[0,1]$. By [](#positive-solution){.pf-ref},
$$
x(t)\geq1,
$$
so
$$
u(t)\coloneqq\frac1{x(t)}
$$
is differentiable and positive. The differential equation gives
$$
\begin{aligned}
u'(t)
&=
-\frac{x'(t)}{x(t)^2}\\
&=
-1-\frac{t^2}{x(t)^2}\\
&\leq-1.
\end{aligned}
$$
Integrating from $0$ to $1$ yields
$$
u(1)-u(0)\leq-1.
$$
Since $u(0)=1$,
$$
u(1)\leq0,
$$
contradicting the positivity of $u(1)$.
:::

:::

::: pf-step
Thus an explicit value for part 3 is
$$
\boxed{c=1}.
$$

::: pf-proof
[](#no-solution){.pf-ref} proves that there is no solution on $[0,1]$.
:::

:::

:::

:::
