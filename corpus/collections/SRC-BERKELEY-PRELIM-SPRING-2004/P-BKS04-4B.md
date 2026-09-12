---
schema: qual/card@1
id: P-BKS04-4B
kind: problem
title: UC Berkeley Spring 2004 prelim 4B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $a _ { 1 } , \ldots , a _ { n }$ be positive real numbers.
Let $\Delta$ be the set of points $\mathbf { x } \in \mathbb { R } ^ { n }$ satisfying the conditions

$$
\sum _ { i = 1 } ^ { n } a _ { i } x _ { i } = 1 , \quad x _ { i } > 0 { \mathrm { ~ f o r ~ a l l ~ } } i .
$$

Prove that the function $\scriptstyle \log ( \prod _ { i = 1 } ^ { n } x _ { i } )$ has a unique maximum on $\Delta$ and find the point where it occurs.
:::

::: {.solution}
The given function is continuous and approaches −∞ at every point on the boundary of $\Delta$ (since each $x _ { i }$ is bounded above, and at least one of them approaches zero at every point on the boundary).
Hence a maximum exists.
By Lagrange multipliers, at a maximum we must have d log $\begin{array} { r } { ( \prod _ { i = 1 } ^ { n } x _ { i } ) \ : = \ : \lambda d \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } } \end{array}$ for some $\lambda ,$ or $\textstyle \sum _ { i } d x _ { i } / x _ { i } =$ $\lambda \sum _ { i } a _ { i } d x _ { i }$ . Hence $( x _ { 1 } , \ldots , x _ { n } ) = ( 1 / \lambda ) ( 1 / a _ { 1 } , \ldots , 1 / a _ { n } )$ . Combining this with the equation $\textstyle \sum _ { i } a _ { i } x _ { i } = 1$ shows that $\lambda = n$ and $( x _ { 1 } , \ldots , x _ { n } ) = ( 1 / n ) ( 1 / a _ { 1 } , \ldots , 1 / a _ { n } )$ . This locates the maximum and proves that it is unique.

Alternative solution: The arithmetic-mean–geometric-mean inequality gives

$$
{ \frac { \sum _ { i = 1 } ^ { n } a _ { i } x _ { i } } { n } } \geq \left( \prod _ { i = 1 } ^ { n } ( a _ { i } x _ { i } ) \right) ^ { 1 / n } ,
$$

with equality if and only if $a _ { 1 } x _ { 1 } = \cdots = a _ { n } x _ { n }$ . On $\Delta$ , the left hand side is constant, so we get an upper bound on $\textstyle \prod _ { i = 1 } ^ { n } x _ { i } ,$ attained exactly when $a _ { 1 } x _ { 1 } = \cdots = a _ { n } x _ { n }$ . It follows that there is a unique maximum where $a _ { i } x _ { i } = 1 / n$ for all $i ;$ that is, $x _ { i } = 1 / ( n a _ { i } )$ for all i.
:::
