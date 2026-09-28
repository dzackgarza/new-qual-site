---
schema: qual/card@1
id: P-PRELIM82S-18
kind: problem
title: A quadratic integral functional attains its maximum on a unit Lipschitz ball
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Every u in E satisfies |u(x)|<=1, and E is uniformly
    equicontinuous because all its elements are 1-Lipschitz. Uniform
    limits remain in E, so Arzela-Ascoli makes E compact in the sup
    norm. On E the functional phi is 3-Lipschitz in that norm, hence
    continuous, and therefore attains a maximum.
---

::: {.problem}
Let $E$ be the set of continuous functions $u:[0,1]\to\mathbb R$ such that
\[
|u(x)-u(y)|\le |x-y|
\qquad(0\le x,y\le1),
\]
and $u(0)=0$.
Define
\[
\varphi(u)=\int_0^1\bigl(u(x)^2-u(x)\bigr)\,dx.
\]
Show that $\varphi$ attains its maximum value at some $u\in E$.
:::

::: {.solution}
Equip $C([0,1],\RR)$ with the supremum norm
$$
\norm{u}_\infty
=
\max_{0\leq x\leq1}\abs{u(x)}.
$$

<1>1. The family $E$ is uniformly bounded:
$$
\norm{u}_\infty\leq1
$$
for every $u\in E$.

::: {.proof}
For $u\in E$ and $x\in[0,1]$,
$$
\abs{u(x)}
=
\abs{u(x)-u(0)}
\leq
\abs{x-0}
\leq1.
$$
Taking the maximum over $x$ gives the claim.
:::

<1>2. The family $E$ is equicontinuous.

::: {.proof}
Every $u\in E$ satisfies
$$
\abs{u(x)-u(y)}\leq\abs{x-y}
$$
for all $x,y\in[0,1]$. Thus for every $\varepsilon>0$, taking
$\delta=\varepsilon$ gives
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{u(x)-u(y)}<\varepsilon
$$
simultaneously for all $u\in E$.
:::

<1>3. The set $E$ is closed in the supremum norm.

::: {.proof}
Suppose $u_j\in E$ and
$$
\norm{u_j-u}_\infty\longrightarrow0
$$
for some $u\in C([0,1],\RR)$. Then
$$
u(0)
=
\lim_{j\to\infty}u_j(0)
=0.
$$
For every $x,y\in[0,1]$,
$$
\begin{aligned}
\abs{u(x)-u(y)}
&=
\lim_{j\to\infty}
\abs{u_j(x)-u_j(y)}\\
&\leq
\abs{x-y}.
\end{aligned}
$$
Hence $u\in E$.
:::

<1>4. The set $E$ is compact in the supremum norm.

::: {.proof}
By steps <1>1 and <1>2, $E$ is uniformly bounded and equicontinuous.
The Arzelà--Ascoli theorem therefore says that the closure of $E$ in
$C([0,1],\RR)$ is compact. Step <1>3 says that $E$ is already closed,
so $E$ itself is compact.
:::

<1>5. For all $u,v\in E$,
$$
\abs{\varphi(u)-\varphi(v)}
\leq
3\norm{u-v}_\infty.
$$

::: {.proof}
By step <1>1,
$$
\abs{u(x)}\leq1,
\qquad
\abs{v(x)}\leq1
$$
for every $x\in[0,1]$. Therefore
$$
\begin{aligned}
\abs{\varphi(u)-\varphi(v)}
&\leq
\int_0^1
\abs{
u(x)^2-v(x)^2-u(x)+v(x)
}
\,dx\\
&\leq
\int_0^1
\abs{u(x)-v(x)}
\bigl(\abs{u(x)+v(x)}+1\bigr)
\,dx\\
&\leq
3\norm{u-v}_\infty.
\end{aligned}
$$
:::

<1>6. The functional
$$
\varphi:E\longrightarrow\RR
$$
is continuous.

::: {.proof}
Step <1>5 shows that $\varphi$ is Lipschitz with constant $3$.
:::

<1>7. There is $u_*\in E$ such that
$$
\boxed{
\varphi(u_*)
=
\max_{u\in E}\varphi(u)
}.
$$

::: {.proof}
The set $E$ is nonempty because the zero function belongs to it.
By step <1>4, $E$ is compact, and by step <1>6, $\varphi$ is
continuous. The extreme value theorem therefore gives a point
$u_*\in E$ at which $\varphi$ attains its maximum.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
