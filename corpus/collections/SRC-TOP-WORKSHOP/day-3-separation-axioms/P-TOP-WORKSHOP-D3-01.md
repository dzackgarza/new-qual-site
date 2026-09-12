---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-01
kind: problem
title: A Hausdorff quotient without a countable basis
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Jan ’08 # B9) Let $X=\mathbb R^2$ and define an equivalence relation on $X$ by $(x_1,x_2)\sim(y_1,y_2)$ if and only if they are equal or $x_1=y_1=0$.
Set $Y=X/\sim$.
Show that $Y$ is Hausdorff but does not have a countable basis for its topology.
:::

::: {.solution}
Let \(q:\mathbb R^2\to Y\) be the quotient map and let \(p=q(\{0\}\times\mathbb R)\).

First \(Y\) is Hausdorff. If two quotient points are represented by points \(x,y\notin\{0\}\times\mathbb R\), choose disjoint Euclidean balls about \(x\) and \(y\) small enough to avoid the \(y\)-axis; these balls are saturated, so their images under \(q\) are disjoint open neighborhoods. If one point is \(p\) and the other is represented by \(x=(x_1,x_2)\) with \(x_1\ne0\), choose \(0<\delta<|x_1|/3\). The saturated strip
\[
S=\{(u,v):|u|<\delta\}
\]
contains the collapsed axis, while a sufficiently small ball about \(x\) is disjoint from \(S\) and from the axis. Their quotient images separate the two points. Thus \(Y\) is Hausdorff.

Now suppose \(p\) had a countable neighborhood basis \(U_1,U_2,\dots\). Put \(V_n=q^{-1}(U_n)\). Each \(V_n\) is an open set containing the entire \(y\)-axis. Hence for the point \((0,n)\) there exists \(r_n>0\) with
\[
B((0,n),r_n)\subset V_n.
\]
Choose \(0<t_n<\min(r_n,1/2)\) and set \(z_n=(t_n,n)\). Then \(z_n\in V_n\). The set \(F=\{z_n:n\ge1\}\) is closed in \(\mathbb R^2\): its second coordinates are distinct integers and it has no finite accumulation point. Therefore
\[
W=\mathbb R^2\setminus F
\]
is open, saturated, and contains the whole \(y\)-axis. Thus \(q(W)\) is an open neighborhood of \(p\). But \(U_n\nsubseteq q(W)\), since \(q(z_n)\in U_n\setminus q(W)\). This contradicts that \((U_n)\) is a neighborhood basis at \(p\).

Hence \(Y\) is not first countable at \(p\), and therefore cannot have a countable basis.
:::
