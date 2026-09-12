---
schema: qual/card@1
id: E-LEJYZ
kind: problem
title: Every linear continuum is normal
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
  - Order Topology
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
Every linear continuum $X$ is normal.

(a) Let $C$ be a nonempty closed subset of $X$.
If $U$ is a component of $X - C$, show that $U$ is a set of the form $(c, c')$ or $(c, \infty)$ or $(-\infty, c)$, where $c, c' \in C$.

(b) Let $A$ and $B$ be closed disjoint subsets of $X$.
For each component $W$ of $X - A \cup B$ that is an open interval with one end point in $A$ and the other in $B$, choose a point $c_W$ of $W$.
Show that the set $C$ of the points $c_W$ is closed.

(c) Show that if $V$ is a component of $X - C$, then $V$ does not intersect both $A$ and $B$.
:::

::: {.solution}
(a) Let \(U\) be a component of \(X\setminus C\). Since \(X\) is a linear continuum, connected subsets are intervals, so \(U\) is convex. Because \(X\setminus C\) is open, \(U\) is an open interval or ray. Any finite endpoint of \(U\) must lie in \(C\): if an endpoint \(c\) were not in \(C\), openness of \(X\setminus C\) would allow \(U\) to extend past \(c\), contradicting maximality. Hence \(U\) has one of the forms
\[
(c,c'),\qquad(c,\infty),\qquad(-\infty,c)
\]
with the finite endpoints in \(C\).

(b) Let \(C_0=\{c_W\}\) be the chosen points. We show \(C_0\) is closed. If \(x\notin A\cup B\), then \(x\) lies in a component \(W\) of \(X\setminus(A\cup B)\). If \(W\) is not one of the bridge components, it contains no point of \(C_0\); if it is a bridge component, then \(C_0\cap W=\{c_W\}\), and since \(x\ne c_W\), a small interval around \(x\) inside \(W\) avoids \(c_W\).

Now suppose \(x\in A\) (the case \(x\in B\) is symmetric). Since \(B\) is closed and \(x\notin B\), choose a convex open neighborhood \(O\) of \(x\) disjoint from \(B\). Any bridge component having its chosen point in \(O\) must leave \(O\) through one of its two ends in order to reach an endpoint in \(B\). Since distinct components are disjoint convex intervals, there can be at most one such bridge component extending to the left and at most one extending to the right. Shrink \(O\) around \(x\) to avoid the finitely many corresponding chosen points. Thus \(x\) has a neighborhood disjoint from \(C_0\). Hence \(C_0\) is closed.

(c) Let \(V\) be a component of \(X\setminus C_0\). Suppose \(V\) met both \(A\) and \(B\). Since \(V\) is convex, choose \(a\in A\cap V\) and \(b\in B\cap V\), say \(a<b\). Moving in the interval \([a,b]\), the closed sets \(A\) and \(B\) must be separated by at least one component \(W\) of \(X\setminus(A\cup B)\) whose two endpoints lie one in \(A\) and one in \(B\). By construction \(c_W\in C_0\cap(a,b)\subset V\), contradicting \(V\subset X\setminus C_0\). Thus no component \(V\) meets both \(A\) and \(B\).

To conclude normality, let \(A,B\) be disjoint closed subsets of \(X\), construct \(C_0\) as above, and let \(\mathcal U\) be the union of all components of \(X\setminus C_0\) meeting \(A\), while \(\mathcal V\) is the union of those meeting \(B\). Components of the open set \(X\setminus C_0\) are open intervals or rays, hence open. By (c), \(\mathcal U\) and \(\mathcal V\) are disjoint open neighborhoods of \(A\) and \(B\). Therefore every linear continuum is normal.
:::
