---
schema: qual/card@1
id: E-HAT-1.1-4
kind: problem
title: Locally star-shaped paths are piecewise linear up to homotopy
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used a Lebesgue-number subdivision and verified local star-shapedness separately for open sets and finite unions of closed convex sets.
---

A subspace $X \subset \mathbb{R}^n$ is said to be star-shaped if there is a point $x_0 \in X$ such that, for each $x \in X$, the line segment from $x_0$ to $x$ lies in $X$.
Show that if a subspace $X \subset \mathbb{R}^n$ is locally star-shaped, in the sense that every point of $X$ has a star-shaped neighborhood in $X$, then every path in $X$ is homotopic in $X$ to a piecewise linear path, that is, a path consisting of a finite number of straight line segments traversed at constant speed.
Show this applies in particular when $X$ is open or when $X$ is a union of finitely many closed convex sets.

::: {.solution}
Let
\[
\gamma:I\to X
\]
be a path.

<1>1. There is a subdivision
\[
0=t_0<t_1<\cdots<t_m=1
\]
such that for every $i$ the set $\gamma([t_{i-1},t_i])$ lies in a star-shaped neighborhood $V_i\subseteq X$.
::: {.proof}
For every $x\in\gamma(I)$, choose a star-shaped neighborhood $V_x$ of $x$ in $X$.
The sets
\[
\gamma^{-1}(V_x)
\]
form an open cover of the compact metric space $I$.
Choose a Lebesgue number $\delta>0$ for this cover, and choose a subdivision whose mesh is less than $\delta$.
Then each interval $[t_{i-1},t_i]$ is contained in some $\gamma^{-1}(V_x)$, giving the required $V_i$.
:::

<1>2. If $V\subseteq\mathbb R^n$ is star-shaped and $a,b\in V$, then every path in $V$ from $a$ to $b$ is homotopic relative to its endpoints to a piecewise linear path from $a$ to $b$.
::: {.proof}
Let $c\in V$ be a star center, so each segment $[c,z]$ with $z\in V$ lies in $V$.
The map
\[
C:V\times I\to V,
\qquad
C(z,t)=(1-t)z+tc,
\]
is a contraction of $V$ to $c$.
Hence every loop in $V$ is null-homotopic, so $V$ is simply connected.

Now let $\alpha$ be any path from $a$ to $b$, and let $p$ be the broken line obtained by traversing the segment from $a$ to $c$ and then the segment from $c$ to $b$.
Both segments lie in $V$, so $p$ is a piecewise linear path in $V$.
The loop $\alpha\cdot\bar p$ is null-homotopic in $V$.
For paths with common endpoints, null-homotopy of $\alpha\cdot\bar p$ is equivalent to a homotopy $\alpha\simeq p$ relative to the endpoints: concatenate the null-homotopy with $p$ and use the standard cancellation homotopies $\bar p\cdot p\simeq c_b$.
Thus $\alpha$ is homotopic rel endpoints to the piecewise linear path $p$.
:::

<1>3. The path $\gamma$ is homotopic relative to its endpoints to a piecewise linear path in $X$.
::: {.proof}
For each $i$, reparametrize the restricted path
\[
\gamma|_{[t_{i-1},t_i]}
\]
to $I$.
By <1>1 its image lies in the star-shaped set $V_i$, so <1>2 gives a homotopy rel endpoints to a broken line $p_i\subseteq V_i$.

Because each homotopy fixes the two endpoints $\gamma(t_{i-1})$ and $\gamma(t_i)$, the finitely many homotopies paste along the subdivision points to a homotopy of $\gamma$ relative to $\gamma(0),\gamma(1)$.
The terminal path is the concatenation
\[
p_1\cdot p_2\cdots p_m,
\]
which consists of finitely many straight line segments and is therefore piecewise linear.
:::

<1>4. Every open subspace $X\subseteq\mathbb R^n$ is locally star-shaped.
::: {.proof}
For $x\in X$, openness gives $r>0$ with
\[
B(x,r)\subseteq X.
\]
The ball $B(x,r)$ is convex, hence star-shaped, and is a neighborhood of $x$ in $X$.
:::

<1>5. A finite union of closed convex subsets of $\mathbb R^n$ is locally star-shaped.
::: {.proof}
Write
\[
X=C_1\cup\cdots\cup C_N
\]
with each $C_j$ closed and convex, and fix $x\in X$.
Let
\[
J=\{j:x\in C_j\}.
\]
For every $j\notin J$, closedness of $C_j$ and $x\notin C_j$ give an open ball about $x$ disjoint from $C_j$.
Since there are only finitely many such $j$, choose $r>0$ so that
\[
B(x,r)\cap C_j=\varnothing
\qquad(j\notin J).
\]
Then
\[
X\cap B(x,r)=\bigcup_{j\in J}(C_j\cap B(x,r)).
\]
Each $C_j\cap B(x,r)$ is convex and contains $x$.
Thus if $y\in X\cap B(x,r)$, then $y$ belongs to some $C_j\cap B(x,r)$ with $j\in J$, and the whole segment $[x,y]$ lies in that same convex set.
Therefore $X\cap B(x,r)$ is star-shaped with center $x$.
:::

<1>6. Hence the conclusion applies both to open subsets of $\mathbb R^n$ and to finite unions of closed convex subsets.
::: {.proof}
Apply <1>3 using the local star-shapedness established in <1>4 and <1>5.
:::
:::
