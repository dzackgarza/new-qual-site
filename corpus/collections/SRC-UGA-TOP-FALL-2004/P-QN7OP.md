---
schema: qual/card@1
id: P-QN7OP
kind: problem
title: Connectedness via maps to $\{0,1\}$, connected fibers over a connected Hausdorff
  space, and a noncompact counterexample
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Compactness
  - Continuity
relations: []
review: draft
---

:::{.problem}
Let $X$ be a topological space.

a.  
Prove that $X$ is connected if and only if there is no continuous
nonconstant map to the discrete two-point space $\theset{0, 1}$.

b.
Suppose in addition that $X$ is compact and $Y$ is a connected Hausdorff space.
Suppose further that there is a surjective continuous map $f : X \to Y$ such that
every preimage $f\inv (y)$ for $y \in Y$, is a connected subset of $X$. 

Show that $X$ is connected.

c.  
Give an example showing that the conclusion of (b) may be false if
$X$ is not compact.

:::

::: {.solution}
<1>1. If $X$ is disconnected, there is a continuous nonconstant map $X\to\{0,1\}$.
::: {.proof}
Choose a separation
\[
X=U\disjoint V
\]
with $U,V$ nonempty and open. Define
\[
g:X\to\{0,1\},
\qquad
g|_U=0,
\quad
g|_V=1.
\]
Since $\{0,1\}$ is discrete, the inverse images of its open subsets are unions of $U$ and $V$, so $g$ is continuous. It is nonconstant.
:::

<1>2. If there is a continuous nonconstant map $X\to\{0,1\}$, then $X$ is disconnected.
::: {.proof}
Let
\[
g:X\to\{0,1\}
\]
be continuous and nonconstant. Then $g^{-1}(0)$ and $g^{-1}(1)$ are disjoint nonempty open subsets of $X$ whose union is $X$. Thus they form a separation.
:::

<1>3. Part (a) follows.
::: {.proof}
The two implications are <1>1 and <1>2.
:::

<1>4. Under the hypotheses of part (b), if
\[
X=A\disjoint B
\]
is a separation, then $f(A)\cap f(B)\neq\emptyset$.
::: {.proof}
The sets $A$ and $B$ are closed subsets of the compact space $X$, hence compact. Therefore $f(A)$ and $f(B)$ are compact, and since $Y$ is Hausdorff they are closed in $Y$.

Surjectivity gives
\[
Y=f(A)\cup f(B).
\]
If $f(A)$ and $f(B)$ were disjoint, each would be the complement of the other and hence both would be nonempty open subsets separating the connected space $Y$. Thus they intersect.
:::

<1>5. Under the hypotheses of part (b), $X$ is connected.
::: {.proof}
Suppose toward a contradiction that $X=A\disjoint B$ is a separation. By <1>4 choose
\[
y\in f(A)\cap f(B).
\]
Then the fiber
\[
F=f^{-1}(y)
\]
meets both $A$ and $B$. Moreover
\[
F=(F\cap A)\disjoint(F\cap B),
\]
and both intersections are open in the subspace $F$, because $A$ and $B$ are open in $X$. This separates $F$, contradicting the hypothesis that every fiber is connected. Hence $X$ is connected.
:::

<1>6. Compactness of $X$ cannot be omitted in part (b).
::: {.proof}
Let
\[
X=(-\infty,0]\ \amalg\ (0,\infty)
\]
be the topological disjoint union, let $Y=\RR$, and define $f:X\to Y$ by the ordinary inclusion on each summand. The map is continuous and surjective. It is also bijective, so every fiber is a singleton and hence connected.

However, the two summands are disjoint nonempty open-and-closed subsets of $X$, so $X$ is disconnected. It is noncompact, since the second summand $(0,\infty)$ is a closed subspace of $X$ and is not compact. Thus compactness in (b) cannot be omitted.
:::
:::
