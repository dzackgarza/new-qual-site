---
schema: qual/card@1
id: P-PRELIM82S-03
kind: problem
title: A strict distance contraction on a compact metric space has a unique fixed point
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
    The strict distance inequality implies the nonexpansive estimate
    d(phi(x),phi(y))<=d(x,y), hence continuity. The continuous displacement
    F(x)=d(x,phi(x)) attains a minimum on compact K. A positive minimum
    would strictly decrease at phi(x), so the minimum is zero and gives a
    fixed point. Two distinct fixed points would contradict the strict
    contraction inequality.
---

::: {.problem}
Let $K$ be a nonempty compact subset of a metric space with distance $d$.
Suppose $\varphi:K\to K$ satisfies
\[
d(\varphi(x),\varphi(y))<d(x,y)
\]
for all distinct $x,y\in K$.
Show that $\varphi$ has exactly one fixed point in $K$.
:::

::: {.solution}
<1>1. For all $x,y\in K$,
$$
d(\varphi(x),\varphi(y))
\leq
d(x,y).
$$

::: {.proof}
If $x\neq y$, this follows from the strict inequality in the hypothesis.
If $x=y$, both sides are zero.
:::

<1>2. The map $\varphi:K\to K$ is continuous.

::: {.proof}
Step <1>1 gives
$$
d(\varphi(x),\varphi(y))
\leq
d(x,y)
$$
for all $x,y\in K$. Thus $\varphi$ is $1$-Lipschitz and hence continuous.
:::

<1>3. The function
$$
F:K\longrightarrow\RR,
\qquad
F(x)=d(x,\varphi(x)),
$$
is continuous.

::: {.proof}
The metric
$$
d:K\times K\longrightarrow\RR
$$
is continuous, and step <1>2 gives continuity of $\varphi$. Therefore
$$
x\longmapsto d(x,\varphi(x))
$$
is continuous.
:::

<1>4. There is a point $x_0\in K$ at which $F$ attains its minimum.

::: {.proof}
The set $K$ is nonempty and compact, and $F$ is continuous by step <1>3.
The extreme value theorem therefore gives
$$
F(x_0)
=
\min_{x\in K}F(x)
$$
for some $x_0\in K$.
:::

<1>5. One has
$$
F(x_0)=0.
$$

::: {.proof}
Suppose instead that
$$
F(x_0)>0.
$$
Then
$$
x_0\neq\varphi(x_0).
$$
Applying the strict contraction inequality to these two distinct points
gives
$$
\begin{aligned}
F(\varphi(x_0))
&=
d(\varphi(x_0),\varphi^2(x_0))\\
&<
d(x_0,\varphi(x_0))\\
&=
F(x_0).
\end{aligned}
$$
This contradicts the minimality of $F(x_0)$ from step <1>4. Hence
$F(x_0)=0$.
:::

<1>6. The point $x_0$ is a fixed point of $\varphi$.

::: {.proof}
By step <1>5,
$$
d(x_0,\varphi(x_0))=0.
$$
A metric separates points, so
$$
\varphi(x_0)=x_0.
$$
:::

<1>7. The fixed point is unique.

::: {.proof}
Suppose $x,y\in K$ are fixed points and $x\neq y$. Then the hypothesis
gives
$$
d(x,y)
=
d(\varphi(x),\varphi(y))
<
d(x,y),
$$
which is impossible. Thus no two distinct fixed points exist.
:::

<1>8. Therefore $\varphi$ has exactly one fixed point:
$$
\boxed{
\exists!\,x\in K
\text{ such that }
\varphi(x)=x.
}
$$

::: {.proof}
Existence is step <1>6 and uniqueness is step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
