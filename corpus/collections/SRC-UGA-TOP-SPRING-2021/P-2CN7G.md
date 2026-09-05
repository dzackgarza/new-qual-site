---
schema: qual/card@1
id: P-2CN7G
kind: problem
title: The product $\prod_{n=1}^{\infty}\{0,1\}$ is totally disconnected
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Connectedness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 2 of the official UGA Spring 2021 topology exam and corrected the malformed product index in the imported statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the clopen coordinate-cylinder separation and the induced separation of every non-singleton subspace.
---

::: problem
Let
\[
X=\prod_{n=1}^{\infty}\{0,1\}
\]
be endowed with the product topology.

(a) Show that for all points $x,y\in X$ with $x\neq y$, there are open subsets $U_x,U_y\subseteq X$ such that
\[
x\in U_x,
\qquad
y\in U_y,
\qquad
U_x\cup U_y=X,
\qquad
U_x\cap U_y=\emptyset.
\]

(b) Show that $X$ is totally disconnected: the only nonempty connected subsets of $X$ are singletons.
:::

::: {.solution}
<1>1. If $x,y\in X$ are distinct, then they differ in some coordinate.
::: {.proof}
Write
\[
x=(x_1,x_2,\ldots),
\qquad
y=(y_1,y_2,\ldots).
\]
If $x_n=y_n$ for every $n$, then $x=y$ as elements of the Cartesian product.
Since $x\ne y$, there is therefore an index $m$ such that
\[
x_m\ne y_m.
\]
Because both entries lie in $\{0,1\}$, this means
\[
\{x_m,y_m\}=\{0,1\}.
\]
:::

<1>2. The $m$th coordinate gives the required disjoint open cover in part (a).
::: {.proof}
Let
\[
\pi_m:X\longrightarrow\{0,1\}
\]
be the $m$th coordinate projection and define
\[
U_x=\pi_m^{-1}(\{x_m\}),
\qquad
U_y=\pi_m^{-1}(\{y_m\}).
\]
The factor $\{0,1\}$ has the discrete topology, so the singletons $\{x_m\}$ and $\{y_m\}$ are open.
By the definition of the product topology, $\pi_m$ is continuous; hence $U_x$ and $U_y$ are open in $X$.
Clearly
\[
x\in U_x,
\qquad
y\in U_y.
\]
Since $x_m\ne y_m$, the two singletons are disjoint, so
\[
U_x\cap U_y=\emptyset.
\]
Finally, every $z\in X$ has
\[
z_m\in\{0,1\}=\{x_m,y_m\},
\]
so $z\in U_x\cup U_y$.
Thus
\[
U_x\cup U_y=X.
\]
This proves part (a).
:::

<1>3. Every nonempty connected subset of $X$ is a singleton.
::: {.proof}
Let $C\subseteq X$ be nonempty and connected, and choose $x\in C$.
Suppose for contradiction that there is a point $y\in C$ with $y\ne x$.
By <1>2 there are disjoint open sets $U_x,U_y\subseteq X$ such that
\[
x\in U_x,
\qquad
y\in U_y,
\qquad
U_x\cup U_y=X.
\]
Then
\[
C=(C\cap U_x)\cup(C\cap U_y).
\]
The two sets on the right are disjoint, nonempty, and open in the subspace topology on $C$.
They therefore form a separation of $C$, contradicting connectedness.
Hence no such $y$ exists, and
\[
C=\{x\}.
\]
Thus $X$ is totally disconnected.
:::
:::
