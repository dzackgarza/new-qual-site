---
schema: qual/card@1
id: P-BKF14-3B
kind: problem
title: Continuity of a unique maximizer $y_x$ of $f(x,\cdot)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet and its
    compactness argument for limits of unique maximizers.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the subsequence extraction, passage to the limit in the
    maximizing inequality, and the use of uniqueness at the limiting x.
---

::: {.problem}
Let $f : [ 0 , 1 ] \times [ 0 , 1 ] \to \mathbb { R }$ be continuous and assume that for all $x \in [ 0 , 1 ]$ there is a unique $y _ { x }$ such that $f ( x , y _ { x } ) = \operatorname* { m a x } \{ f ( x , y ) ; y \in [ 0 , 1 ] \}$ . Let $g ( x ) = y _ { x }$ . Show that $g : [0,1] \to [0,1]$ is continuous.
:::

::: {.solution}
<1>1. Let $(x_n)$ be any sequence in $[0,1]$ such that
$$
x_n\longrightarrow x.
$$
It is enough to prove
$$
g(x_n)\longrightarrow g(x).
$$

::: {.proof}
Both the domain and codomain are metric spaces, so continuity is
equivalent to sequential continuity.
:::

<1>2. Every convergent subsequence
$$
g(x_{n_j})\longrightarrow b
$$
has limit
$$
b=g(x).
$$

::: {.proof}
For every $j$, the definition of $g(x_{n_j})$ as a maximizer gives
$$
f(x_{n_j},g(x_{n_j}))
\ge
f(x_{n_j},g(x)).
$$
Since
$$
x_{n_j}\to x
\qquad\text{and}\qquad
g(x_{n_j})\to b,
$$
continuity of $f$ allows passage to the limit:
$$
f(x,b)\ge f(x,g(x)).
$$
But $g(x)$ is the unique point of $[0,1]$ at which
$y\mapsto f(x,y)$ attains its maximum. Thus the displayed inequality
forces $b=g(x)$.
:::

<1>3. One has
$$
g(x_n)\longrightarrow g(x).
$$

::: {.proof}
Suppose not. Then there is an $\varepsilon>0$ and a subsequence
$(x_{n_j})$ such that
$$
|g(x_{n_j})-g(x)|\ge\varepsilon
$$
for every $j$. The sequence $(g(x_{n_j}))$ lies in the compact interval
$[0,1]$, so it has a convergent subsequence
$$
g(x_{n_{j_k}})\longrightarrow b.
$$
The inequality above passes to the limit and gives
$$
|b-g(x)|\ge\varepsilon,
$$
so $b\ne g(x)$. This contradicts step <1>2.
:::

<1>4. The map
$$
\boxed{g:[0,1]\to[0,1]}
$$
is continuous.

::: {.proof}
The sequence $(x_n)$ and its limit $x$ in step <1>1 were arbitrary,
and step <1>3 proves the required sequential continuity at every
$x\in[0,1]$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
