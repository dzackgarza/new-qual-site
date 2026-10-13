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
\[
x'=x^2+t^2,\qquad x(0)=1.
\]

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
\|\varphi-1\|_\infty\leq\frac12
\right\}.
$$

<1>1. The metric space $\mathcal X$, with the sup norm, is complete.

::: {.proof}
The space $C([0,b])$ with the sup norm is Banach. The set $\mathcal X$ is the closed ball of radius $1/2$ centered at the constant function $1$, hence is a closed subset of a complete metric space and is therefore complete.
:::

<1>2. Define
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

::: {.proof}
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
\|T\varphi-1\|_\infty<\frac12,
$$
so $T\varphi\in\mathcal X$.
:::

<1>3. The map $T:\mathcal X\to\mathcal X$ is a contraction with contraction constant $3/5$.

::: {.proof}
If $\varphi,\psi\in\mathcal X$, then
$$
|\varphi(s)|,|\psi(s)|\leq\frac32.
$$
Thus
$$
\begin{aligned}
|(T\varphi)(t)-(T\psi)(t)|
&\leq
\int_0^t
|\varphi(s)^2-\psi(s)^2|\,ds\\
&\leq
\int_0^t
|\varphi(s)+\psi(s)|
|\varphi(s)-\psi(s)|\,ds\\
&\leq
3t\,\|\varphi-\psi\|_\infty\\
&\leq
\frac35\|\varphi-\psi\|_\infty.
\end{aligned}
$$
Taking the supremum over $t\in[0,b]$ gives the claim.
:::

<1>4. There is a unique $x\in\mathcal X$ satisfying
$$
x=Tx.
$$

::: {.proof}
By steps <1>1--<1>3, $T$ is a contraction of the complete metric space $\mathcal X$ into itself. The Banach fixed-point theorem therefore gives a unique fixed point.
:::

<1>5. The fixed point from step <1>4 is a solution of
$$
x'=x^2+t^2,
\qquad
x(0)=1
$$
on
$$
\boxed{[0,1/5]}.
$$

::: {.proof}
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

<1>6. Any solution on an interval $[0,c]$ is positive and nondecreasing there.

::: {.proof}
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

<1>7. No solution exists on $[0,1]$.

::: {.proof}
Suppose a solution existed on $[0,1]$. By step <1>6,
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

<1>8. Thus an explicit value for part 3 is
$$
\boxed{c=1}.
$$

::: {.proof}
Step <1>7 proves that there is no solution on $[0,1]$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>5 proves parts 1--2, and step <1>8 proves part 3.
:::
:::
