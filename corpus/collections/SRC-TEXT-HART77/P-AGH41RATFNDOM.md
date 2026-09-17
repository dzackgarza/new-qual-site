---
schema: qual/card@1
id: P-AGH41RATFNDOM
kind: problem
title: Gluing regular functions and the domain of definition of a rational function
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Regular Functions
  - Function Fields
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.4.1. The proof glues compatible regular functions locally and then takes the union of every open representative of a fixed rational function.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked well-definedness, local regularity, and maximality against the source and independent chapter notes.'
---

::: {.problem}
Let $X$ be a variety.

(a) Let $f$ and $g$ be regular functions on open subsets $U$ and $V$ of $X$, and suppose $f = g$ on $U \intersect V$.
Show that the function which equals $f$ on $U$ and $g$ on $V$ is a regular function on $U \union V$.

(b) Conclude that if $f$ is a rational function on $X$, then there is a largest open subset $U \subseteq X$ on which $f$ is represented by a regular function.
One says that $f$ is defined at the points of $U$.
:::

::: {.solution}
<1>1. The piecewise rule
$$
h(x)=
\begin{cases}
f(x),&x\in U,\\
g(x),&x\in V
\end{cases}
$$
defines a regular function on $U\cup V$.

::: {.proof}
The rule is well-defined because $f=g$ on $U\cap V$.
Fix $x\in U\cup V$.
If $x\in U$, then on the open neighborhood $U$ of $x$ the function $h$ equals the regular function $f$.
If $x\in V$, then on the open neighborhood $V$ it equals the regular function $g$.
Thus every point has an open neighborhood on which $h$ is regular.
Regularity is local, so $h$ is regular on $U\cup V$.
This proves (a).
:::

<1>2. Let $r\in K(X)$ be a rational function and let
$$
D(r)=\bigcup\{U\subseteq X: U\text{ is open and }r\text{ is represented on }U\text{ by a regular function}\}.
$$
Then $D(r)$ is open.

::: {.proof}
It is a union of open subsets of $X$.
:::

<1>3. The local representatives of $r$ glue to a regular function on $D(r)$.

::: {.proof}
For every open $U$ occurring in the union of step <1>2, let $r_U$ be the regular representative of $r$ on $U$.
If $U$ and $V$ are two such opens, then the two representatives define the same rational function.
Hence they agree on $U\cap V$.
Therefore the rule
$$
\widetilde r(x)=r_U(x)\qquad(x\in U)
$$
is independent of the choice of $U$.
At each $x\in D(r)$, choose one such $U$ containing $x$; on that neighborhood $\widetilde r=r_U$ is regular.
Thus $\widetilde r$ is regular on all of $D(r)$ and represents $r$ there.
:::

<1>4. The open subset $D(r)$ is the largest open subset on which $r$ is represented by a regular function.

::: {.proof}
By step <1>3, $r$ is represented regularly on $D(r)$.
If $W\subseteq X$ is any open set on which $r$ has a regular representative, then $W$ occurs in the union defining $D(r)$, so
$$
W\subseteq D(r).
$$
Thus $D(r)$ is maximal by inclusion and is uniquely determined.
This proves (b).
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves (a), and steps <1>2--<1>4 prove (b).
:::
:::
