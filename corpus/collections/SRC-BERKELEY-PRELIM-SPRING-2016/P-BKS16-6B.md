---
schema: qual/card@1
id: P-BKS16-6B
kind: problem
title: Optimality condition for nonnegative least squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked Problem 6B against the vendored Berkeley Spring 2016 exam. The exam states $A^T(y-Ax)\geq0$, while its supplied solution proves the opposite sign by working with $A^T(Ax-y)$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified a one-dimensional counterexample to the printed sign and proved the corrected first-order inequality in every coordinate.
---

::: {.problem}
Let $A$ be an $m\times n$ real matrix and $y\in\mathbb R^m$.
Let $x\in\mathbb R^n$ be a vector with nonnegative entries that minimizes the Euclidean distance $\lVert y-Ax\rVert$ among all nonnegative vectors $x$.
Show that the vector
\[
v=A^T(y-Ax)
\]
has nonnegative entries.
:::

::: {.solution}
<1>1. The assertion as stated is $\boxed{\text{false}}$.

::: {.proof}
Take $m=n=1$, $A=[1]$, and $y=-1$. For a feasible scalar $u\geq0$,
$$
\lVert y-Au\rVert=|-1-u|=1+u,
$$
so the minimizing feasible point is $x=0$. At this minimizer,
$$
v=A^T(y-Ax)=-1,
$$
which is not nonnegative.
:::

<1>2. The correct optimality condition is
$$
A^T(y-Ax)\leq0
$$
coordinatewise, equivalently
$$
A^T(Ax-y)\geq0.
$$

::: {.proof}
Let $a_j=Ae_j$ be the $j$-th column of $A$, and put
$$
r\coloneqq y-Ax.
$$
For every $\varepsilon>0$, the vector $x+\varepsilon e_j$ is still feasible because $x$ has nonnegative entries. Minimality of $x$ gives
$$
\lVert r\rVert^2
\leq
\lVert r-\varepsilon a_j\rVert^2.
$$
Hence
$$
0
\leq
-2\varepsilon a_j^Tr
+\varepsilon^2\lVert a_j\rVert^2.
$$
After division by $\varepsilon>0$ and passage to the limit $\varepsilon\downarrow0$,
$$
a_j^Tr\leq0.
$$
Since $a_j^Tr$ is the $j$-th entry of $A^T(y-Ax)$ and $j$ was arbitrary, every entry is nonpositive.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 disproves the printed assertion, and step <1>2 proves the sign condition established by the supplied source solution.
:::
:::

::: {.remark}
The vendored exam states that $A^T(y-Ax)$ has nonnegative entries. The vendored solution instead assumes a negative entry of $A^T(Ax-y)$ and derives a contradiction, which proves $A^T(Ax-y)\geq0$, equivalently the nonpositive inequality in step <1>2.
:::
