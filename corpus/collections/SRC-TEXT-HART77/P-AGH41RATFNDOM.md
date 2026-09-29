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

::: pf

::: {.pf-step #s1}

The piecewise rule
$$
h(x)=
\begin{cases}
f(x),&x\in U,\\
g(x),&x\in V
\end{cases}
$$
defines a regular function on $U\cup V$.

::: pf-proof

The rule is well-defined because $f=g$ on $U\cap V$.
Fix $x\in U\cup V$.
If $x\in U$, then on the open neighborhood $U$ of $x$ the function $h$ equals the regular function $f$.
If $x\in V$, then on the open neighborhood $V$ it equals the regular function $g$.
Thus every point has an open neighborhood on which $h$ is regular.
Regularity is local, so $h$ is regular on $U\cup V$.
This proves (a).

:::

:::

::: {.pf-step #s2}

Let $r\in K(X)$ be a rational function and let
$$
D(r)=\bigcup\{U\subseteq X: U\text{ is open and }r\text{ is represented on }U\text{ by a regular function}\}.
$$
Then $D(r)$ is open.

::: pf-proof

It is a union of open subsets of $X$.

:::

:::

::: {.pf-step #s3}

The local representatives of $r$ glue to a regular function on $D(r)$.

::: pf-proof

For every open $U$ occurring in the union of step [](#s2){.pf-ref}, let $r_U$ be the regular representative of $r$ on $U$.
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

:::

::: {.pf-step #s4}

The open subset $D(r)$ is the largest open subset on which $r$ is represented by a regular function.

::: pf-proof

By step [](#s3){.pf-ref}, $r$ is represented regularly on $D(r)$.
If $W\subseteq X$ is any open set on which $r$ has a regular representative, then $W$ occurs in the union defining $D(r)$, so
$$
W\subseteq D(r).
$$
Thus $D(r)$ is maximal by inclusion and is uniquely determined.
This proves (b).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), and steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (b).

:::

:::

:::
