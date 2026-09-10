---
schema: qual/card@1
id: E-FV0KE
kind: problem
title: A homotopy equivalence to a point that is not a deformation retract
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Find a space $X$ and a point $x_0$ of $X$ such that the inclusion $\ts{x_0} \to X$ is a homotopy equivalence, but $\ts{x_0}$ is not a deformation retract of $X$.
[Hint: Let $X$ be the subspace of $\mathbb{R}^2$ that is the union of the line segments $(1/n) \times I$, for $n \in \mathbb{Z}_+$, the line segment $0 \times I$, and the line segment $I \times 0$; let $x_0$ be the point $(0, 1)$. If $\ts{x_0}$ is a deformation retract of $X$, show that for any neighborhood $U$ of $x_0$, the path component of $U$ containing $x_0$ contains a neighborhood of $x_0$.]
:::

::: {.solution}
Let \(X\subset\mathbb R^2\) be the comb space from the hint:
\[
X=(I\times\{0\})\cup(\{0\}\times I)\cup\bigcup_{n\ge1}(\{1/n\}\times I),
\]
and let \(x_0=(0,1)\).

The space \(X\) is contractible. One explicit contraction first moves every point vertically down to the base and then moves along the base to \((0,0)\); concatenating this with the path in \(\{0\}\times I\) from \((0,0)\) to \(x_0\) gives a homotopy of the identity to the constant map at \(x_0\). Hence the inclusion \(\{x_0\}\hookrightarrow X\) is a homotopy equivalence.

We show that \(\{x_0\}\) is not a deformation retract. Suppose \(H:X\times I\to X\) were a deformation retraction onto \(x_0\), so \(H(x,0)=x\), \(H(x,1)=x_0\), and \(H(x_0,t)=x_0\).

A standard consequence of continuity at the compact set \(\{x_0\}\times I\) is the following: for every neighborhood \(U\) of \(x_0\), there is a neighborhood \(V\) of \(x_0\) such that
\[
H(V\times I)\subset U.
\]
Indeed, cover \(\{x_0\}\times I\) by finitely many product neighborhoods on which \(H\) lands in \(U\), then intersect their \(X\)-factors. For each \(v\in V\), the path \(t\mapsto H(v,t)\) lies in \(U\) and joins \(v\) to \(x_0\). Thus the path component of \(U\) containing \(x_0\) contains the neighborhood \(V\) of \(x_0\).

Now take
\[
U=X\cap\{(x,y):y>1/2\}.
\]
The path component of \(U\) containing \(x_0\) is exactly \(\{0\}\times(1/2,1]\): every other vertical tooth \(\{1/n\}\times(1/2,1]\) is a distinct path component because the horizontal base \(y=0\) has been removed. This component contains no neighborhood of \(x_0\) in \(X\), since every neighborhood of \((0,1)\) meets infinitely many teeth \(x=1/n\). Contradiction. Hence \(\{x_0\}\) is not a deformation retract.
:::
