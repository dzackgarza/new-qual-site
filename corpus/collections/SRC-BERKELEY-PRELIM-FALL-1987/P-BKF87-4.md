---
schema: qual/card@1
id: P-BKF87-4
kind: problem
title: Local functional dependence from parallel gradients
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-corrected
  by: chatgpt
  date: 2026-09-25
  note: >-
    The retained Fall 1987 PDF prints that the gradients are linearly
    independent, which makes the requested conclusion false. Replaced
    "linearly independent" by "linearly dependent"; for example,
    u(x,y)=x and v(x,y)=y disprove the printed statement.
---

::: {.problem}
Let $u,v:\mathbb R^2\to\mathbb R$ be $C^1$. Assume $\nabla u$ is nowhere zero and that $\nabla v$ and $\nabla u$ are linearly dependent at every point. Given $p_0\in\mathbb R^2$, show that there is a $C^1$ function $F$ of one variable such that
\[
v(x,y)=F(u(x,y))
\]
in some neighborhood of $p_0$.
:::

::: {.remark}
The source prints “linearly independent” in place of “linearly dependent.”
That printed statement is false: for
$$
u(x,y)=x,
\qquad
v(x,y)=y,
$$
the gradients are everywhere linearly independent, but $v$ cannot be a function of $u$ on any neighborhood.
Moreover, any identity $v=F(u)$ implies
$$
\nabla v=F'(u)\nabla u,
$$
so linear dependence is necessary.
:::

::: {.solution}
<1>1. There is a $C^1$ local coordinate system near $p_0$ whose first coordinate is $u$.

::: {.proof}
Write
$$
p_0=(x_0,y_0).
$$
Since $\nabla u(p_0)\neq0$, either
$$
u_x(p_0)\neq0
$$
or
$$
u_y(p_0)\neq0.
$$

If $u_x(p_0)\neq0$, define
$$
\Phi(x,y)=(u(x,y),y).
$$
Its Jacobian determinant at $p_0$ is $u_x(p_0)\neq0$.
If instead $u_y(p_0)\neq0$, define
$$
\Phi(x,y)=(u(x,y),x),
$$
whose Jacobian determinant at $p_0$ is $-u_y(p_0)\neq0$.

In either case, the inverse function theorem gives neighborhoods
$$
U\ni p_0,
\qquad
W\ni\Phi(p_0)
$$
such that
$$
\Phi:U\longrightarrow W
$$
is a $C^1$ diffeomorphism. After shrinking $W$, take it to be an open rectangle
$$
W=I\times J.
$$
Its first coordinate is $u$.
:::

<1>2. In the coordinates $(s,t)=\Phi(x,y)$, the function
$$
\widetilde v(s,t)=v\bigl(\Phi^{-1}(s,t)\bigr)
$$
satisfies
$$
\frac{\partial\widetilde v}{\partial t}(s,t)=0
$$
throughout $I\times J$.

::: {.proof}
Fix $(s,t)\in I\times J$ and put
$$
q=\Phi^{-1}(s,t).
$$
Let
$$
X=\frac{\partial\Phi^{-1}}{\partial t}(s,t)\in T_q\mathbb R^2.
$$
Because the first coordinate of $\Phi$ is $u$, the identity
$$
u\bigl(\Phi^{-1}(s,t)\bigr)=s
$$
gives, after differentiating with respect to $t$,
$$
du_q(X)=0.
$$

The hypothesis says that $du_q$ and $dv_q$ are linearly dependent.
Since $du_q\neq0$, there is a scalar $\lambda_q$ such that
$$
dv_q=\lambda_q\,du_q.
$$
Hence
$$
dv_q(X)=0.
$$
By the chain rule,
$$
\frac{\partial\widetilde v}{\partial t}(s,t)
=
dv_q(X)
=
0.
$$
:::

<1>3. There is a $C^1$ function $F:I\to\mathbb R$ such that
$$
\widetilde v(s,t)=F(s)
$$
for every $(s,t)\in I\times J$.

::: {.proof}
Choose any $t_0\in J$ and define
$$
F(s)=\widetilde v(s,t_0).
$$
Since $\widetilde v$ is $C^1$, so is $F$.

For fixed $s\in I$, step <1>2 says that the one-variable function
$$
t\longmapsto\widetilde v(s,t)
$$
has derivative zero throughout the interval $J$. By the mean value theorem it is constant on $J$. Therefore
$$
\widetilde v(s,t)=\widetilde v(s,t_0)=F(s)
$$
for all $t\in J$.
:::

<1>4. On the neighborhood $U$ of $p_0$,
$$
\boxed{v(x,y)=F(u(x,y))}.
$$

::: {.proof}
For $(x,y)\in U$, write
$$
\Phi(x,y)=(s,t).
$$
By construction,
$$
s=u(x,y).
$$
Step <1>3 gives
$$
v(x,y)
=
\widetilde v(s,t)
=
F(s)
=
F(u(x,y)).
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies the required $C^1$ function and neighborhood.
:::
:::
