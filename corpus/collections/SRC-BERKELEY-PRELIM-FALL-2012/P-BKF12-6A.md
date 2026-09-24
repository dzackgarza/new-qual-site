---
schema: qual/card@1
id: P-BKF12-6A
kind: problem
title: Dimension inequality for three pairwise independent subspaces
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 6A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the dimension reduction using pairwise direct sums and the strict
    example of three distinct lines in a two-dimensional space.
---

::: {.problem}
If $U,V,W$ are subspaces of a vector space such that any two have
intersection zero, prove that

$$
\dim(U+V+W)+\dim U+\dim V+\dim W
\le
\dim(U+V)+\dim(V+W)+\dim(W+U)
$$

and give an example where equality does not hold.
:::

::: {.solution}
<1>1. The pairwise-intersection hypothesis gives
$$
\begin{aligned}
\dim(U+V)&=\dim U+\dim V,\\
\dim(V+W)&=\dim V+\dim W,\\
\dim(W+U)&=\dim W+\dim U.
\end{aligned}
$$

::: {.proof}
For finite-dimensional subspaces $A,B$,
$$
\dim(A+B)=\dim A+\dim B-\dim(A\cap B).
$$
Each of the three intersections in the problem is the zero subspace, so applying
this formula to the three pairs gives the displayed equalities.
:::

<1>2. One has
$$
\dim(U+V+W)\le\dim U+\dim V+\dim W.
$$

::: {.proof}
Consider the linear map
$$
\Phi\colon U\oplus V\oplus W\longrightarrow U+V+W,
\qquad
\Phi(u,v,w)=u+v+w.
$$
It is surjective by definition of $U+V+W$. Therefore
$$
\dim(U+V+W)
\le\dim(U\oplus V\oplus W)
=\dim U+\dim V+\dim W.
$$
:::

<1>3. The required dimension inequality holds.

::: {.proof}
By step <1>1, its right-hand side equals
$$
2(\dim U+\dim V+\dim W).
$$
Its left-hand side equals
$$
\dim(U+V+W)+\dim U+\dim V+\dim W,
$$
which is at most the same quantity by step <1>2.
:::

<1>4. In $\RR^2$, the choice
$$
\boxed{
U=\operatorname{span}(e_1),\qquad
V=\operatorname{span}(e_2),\qquad
W=\operatorname{span}(e_1+e_2)
}
$$
satisfies the hypotheses and makes the inequality strict.

::: {.proof}
The three lines are distinct, so any two intersect trivially.
Each has dimension $1$, every pair spans $\RR^2$, and all three
together also span $\RR^2$. Thus the left-hand side of the required
inequality is
$$
2+1+1+1=5,
$$
while its right-hand side is
$$
2+2+2=6.
$$
Hence equality fails.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves the inequality, and step <1>4 gives the requested
strict example.
:::
:::
