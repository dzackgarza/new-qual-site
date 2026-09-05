---
schema: qual/card@1
id: P-A5CFD
kind: problem
title: Closed graphs and continuous maps between topological spaces
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Hausdorff Spaces
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 3 of the official UGA Fall 2006 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Hausdorff separation argument and proved the compact-factor projection lemma directly from the product-topology and compactness definitions.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Checked the shared statement against problem 3 of the official UGA Spring
    2005 topology exam; it is the same two-part closed-graph problem as the
    Fall 2006 appearance.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Rechecked both parts for the Spring 2005 appearance; the existing
    Hausdorff-separation and compact-projection proofs require no change.
---

::: {.problem}
If $f$ is a function from $X$ to $Y$, consider the graph
\[
G=\{(x,y)\in X\times Y\mid f(x)=y\}.
\]

a.
Prove that if $f$ is continuous and $Y$ is Hausdorff, then $G$ is a closed subset of $X \times Y$.

b.
Prove that if $G$ is closed and $Y$ is compact, then $f$ is continuous.
:::

::: {.solution}
<1>1. If $f:X\to Y$ is continuous and $Y$ is Hausdorff, then its graph $G$ is closed in $X\times Y$.
::: {.proof}
It is enough to prove that $(X\times Y)\setminus G$ is open.
Let
\[
(x_0,y_0)\in(X\times Y)\setminus G.
\]
Then
\[
y_0\ne f(x_0).
\]
Because $Y$ is Hausdorff, there are disjoint open sets $U,V\subseteq Y$ such that
\[
f(x_0)\in U,
\qquad
y_0\in V.
\]
Continuity of $f$ implies that $f^{-1}(U)$ is open in $X$, and it contains $x_0$.
Hence
\[
f^{-1}(U)\times V
\]
is an open neighborhood of $(x_0,y_0)$ in $X\times Y$.

This neighborhood is disjoint from $G$.
Indeed, if $(x,y)$ belonged both to $G$ and to $f^{-1}(U)\times V$, then
\[
y=f(x)\in U
\]
because $x\in f^{-1}(U)$, while also $y\in V$, contradicting $U\cap V=\varnothing$.

Thus every point of $(X\times Y)\setminus G$ has an open neighborhood contained in the complement, so the complement is open and $G$ is closed.
:::

<1>2. If $Y$ is compact, then the projection
\[
\pi_X:X\times Y\longrightarrow X
\]
sends closed subsets of $X\times Y$ to closed subsets of $X$.
::: {.proof}
Let $F\subseteq X\times Y$ be closed, and let
\[
x_0\in X\setminus\pi_X(F).
\]
Then
\[
\{x_0\}\times Y\subseteq (X\times Y)\setminus F.
\]
The complement of $F$ is open.
For each $y\in Y$, the definition of the product topology therefore gives open sets
\[
U_y\subseteq X,
\qquad
V_y\subseteq Y
\]
such that
\[
x_0\in U_y,
\qquad
y\in V_y,
\qquad
U_y\times V_y\subseteq (X\times Y)\setminus F.
\]
The family $\{V_y:y\in Y\}$ is an open cover of the compact space $Y$, so there are
\[
y_1,\ldots,y_m\in Y
\]
with
\[
Y=V_{y_1}\cup\cdots\cup V_{y_m}.
\]
Set
\[
U=U_{y_1}\cap\cdots\cap U_{y_m}.
\]
Then $U$ is an open neighborhood of $x_0$.
For every $u\in U$ and $y\in Y$, choose $i$ with $y\in V_{y_i}$.
Since $u\in U\subseteq U_{y_i}$,
\[
(u,y)\in U_{y_i}\times V_{y_i}\subseteq(X\times Y)\setminus F.
\]
Therefore
\[
U\times Y\subseteq(X\times Y)\setminus F,
\]
so
\[
U\cap\pi_X(F)=\varnothing.
\]
Thus every point outside $\pi_X(F)$ has an open neighborhood outside it.
Hence $X\setminus\pi_X(F)$ is open and $\pi_X(F)$ is closed.
:::

<1>3. If $G$ is closed and $Y$ is compact, then $f$ is continuous.
::: {.proof}
Let $C\subseteq Y$ be closed.
Then
\[
X\times C
\]
is closed in $X\times Y$, because its complement is the open set
\[
X\times(Y\setminus C).
\]
Hence
\[
F=G\cap(X\times C)
\]
is closed in $X\times Y$.
By <1>2, its projection $\pi_X(F)$ is closed in $X$.

We claim that
\[
\pi_X(F)=f^{-1}(C).
\]
Indeed,
\[
x\in\pi_X(F)
\]
if and only if there exists $y\in C$ with $(x,y)\in G$, and by the definition of the graph this is equivalent to $f(x)\in C$.

Thus $f^{-1}(C)$ is closed for every closed subset $C\subseteq Y$.
Equivalently, if $W\subseteq Y$ is open and $C=Y\setminus W$, then
\[
X\setminus f^{-1}(W)=f^{-1}(C)
\]
is closed, so $f^{-1}(W)$ is open.
This is exactly continuity of $f$.
:::
:::
