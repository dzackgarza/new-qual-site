---
schema: qual/card@1
id: P-OX3MY
kind: problem
title: A non-invertible endomorphism $T$ admitting $S$ with $TS=0$ but $ST\neq 0$
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $V$ be a finite-dimensional $k\dash$vector space and $T:V\to V$ a nonzero, non-invertible $k\dash$linear map.
Show that there exists a $k\dash$linear map $S:V\to V$ with $T\circ S = 0$ but $S\circ T\neq 0$.
:::

::: {.solution}
<1>1. There exist nonzero vectors $v\in\ker T$ and $w\in\im T$.
::: {.proof}
Since $T$ is not invertible on the finite-dimensional space $V$, rank-nullity gives
$$
\dim\ker T>0.
$$
Choose $0\ne v\in\ker T$. Since $T\ne0$, choose $x_0\in V$ with
$$
w\coloneqq T(x_0)\ne0.
$$
Then $w\in\im T$.
:::

<1>2. There is a linear functional $\lambda\in V^\dual$ such that $\lambda(w)=1$.
::: {.proof}
Extend $w$ to a basis of $V$ and define $\lambda$ on that basis by sending $w$ to $1$ and all other basis vectors to $0$.
:::

<1>3. Define
$$
S:V\longrightarrow V,
\qquad
S(y)=\lambda(y)v.
$$
Then $T\circ S=0$.
::: {.proof}
For every $y\in V$,
$$
(T\circ S)(y)=T(\lambda(y)v)=\lambda(y)T(v)=0
$$
because $v\in\ker T$.
:::

<1>4. The composite $S\circ T$ is nonzero.
::: {.proof}
Using the vector $x_0$ from step <1>1,
$$
(S\circ T)(x_0)=S(w)=\lambda(w)v=v\ne0
$$
by step <1>2. Hence $S\circ T\ne0$.
:::

<1>5. Therefore
$$
\boxed{T\circ S=0\quad\text{and}\quad S\circ T\ne0}.
$$
::: {.proof}
This is exactly step <1>3 together with step <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
