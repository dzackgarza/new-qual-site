---
schema: qual/card@1
id: P-XMOZA
kind: problem
title: Connectedness of $\{(x,y)\in\RR^2:x>0,\,y\geq 0,\,y/x\in\QQ\}$
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Subspace Topology
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 3 of the official UGA Fall 2018 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the irrational-slope separation and converted the retained sound argument to Lamport proof divs.
---

::: problem
Let
\[
X=\left\{(x,y)\in\RR^2:x>0,\ y\ge0,\ \text{and }\frac yx\in\QQ\right\}
\]
and equip $X$ with the subspace topology induced by the usual topology on $\RR^2$.
Prove or disprove that $X$ is connected.
:::

::: {.solution}
The space $X$ is not connected.

<1>1. Let
\[
U=\{(x,y)\in\RR^2:y<\sqrt2\,x\},
\qquad
V=\{(x,y)\in\RR^2:y>\sqrt2\,x\}.
\]
Then $U$ and $V$ are disjoint open subsets of $\RR^2$.
::: {.proof}
The map
\[
g:\RR^2\longrightarrow\RR,
\qquad
g(x,y)=y-\sqrt2\,x
\]
is continuous, and
\[
U=g^{-1}((-\infty,0)),
\qquad
V=g^{-1}((0,\infty)).
\]
Thus both sets are open, and their defining inequalities make them disjoint.
:::

<1>2. The subsets
\[
A=X\cap U,
\qquad
B=X\cap V
\]
are disjoint open subsets of $X$ whose union is $X$.
::: {.proof}
They are open in $X$ by the definition of the subspace topology and are disjoint by <1>1.
Now let $(x,y)\in X$.
Because $x>0$ and $y/x\in\QQ$, while $\sqrt2\notin\QQ$, one has
\[
\frac yx\neq\sqrt2.
\]
Hence either
\[
y<\sqrt2\,x
\]
or
\[
y>\sqrt2\,x.
\]
Thus every point of $X$ lies in $A$ or $B$, so
\[
X=A\cup B.
\]
:::

<1>3. Both $A$ and $B$ are nonempty.
::: {.proof}
The point $(1,1)$ belongs to $X$ and satisfies
\[
1<\sqrt2,
\]
so $(1,1)\in A$.
Likewise, $(1,2)\in X$ and
\[
2>\sqrt2,
\]
so $(1,2)\in B$.
:::

<1>4. Therefore $X$ is disconnected.
::: {.proof}
By <1>2 and <1>3, $A$ and $B$ form a separation of $X$ into two disjoint nonempty open subsets.
Hence $X$ is not connected.
:::
:::
