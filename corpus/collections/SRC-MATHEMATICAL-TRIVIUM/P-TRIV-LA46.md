---
schema: qual/card@1
id: P-TRIV-LA46
kind: problem
title: Canonical forms, rank and signature of three quadratic forms
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 46, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the missing parts (a) and (c) from Linear Algebra Problem 46 on page 6 of the source PDF.
---

::: {.problem}
Reduce the following quadratic forms to the canonical form and determine the rank and the signature:

(a) $x_1^2 + 2\sum_{i=2}^{n} x_i^2 - 2\sum_{i=1}^{n-1} x_i x_{i+1}$,

(b) $\sum_{i=1}^{n} x_i^2 + \sum_{1 \leqslant i < j \leqslant n} x_i x_j$,

(c) $\sum_{1 \leqslant i < j \leqslant n} x_i x_j$.
:::

::: {.solution}
Assume $n\geq2$.

<1>1. For part (a), one has
$$
x_1^2
+
2\sum_{i=2}^{n}x_i^2
-
2\sum_{i=1}^{n-1}x_ix_{i+1}
=
\sum_{i=1}^{n-1}(x_i-x_{i+1})^2+x_n^2.
$$

::: {.proof}
Expanding the right-hand side gives
$$
\sum_{i=1}^{n-1}
(x_i^2-2x_ix_{i+1}+x_{i+1}^2)
+x_n^2.
$$
The coefficient of $x_1^2$ is $1$, the coefficient of each $x_i^2$ for
$2\leq i\leq n$ is $2$, and the cross terms are exactly
$$
-2\sum_{i=1}^{n-1}x_ix_{i+1}.
$$
:::

<1>2. Define
$$
y_i=x_i-x_{i+1},
\qquad
i=1,\ldots,n-1,
$$
and
$$
y_n=x_n.
$$
Then the change of variables is invertible and part (a) becomes
$$
\boxed{y_1^2+\cdots+y_n^2}.
$$

::: {.proof}
The transformation from $x$ to $y$ is triangular with diagonal entries all
equal to $1$, hence invertible. Step <1>1 gives the displayed canonical form.
:::

<1>3. Therefore part (a) has
$$
\boxed{\operatorname{rank}=n,\qquad \text{inertia}=(n,0),\qquad \text{signature}=n}.
$$

::: {.proof}
The canonical form in step <1>2 contains $n$ positive squares and no negative
or zero squares.
:::

<1>4. For part (b), write
$$
q_b(x)
=
\sum_{i=1}^{n}x_i^2
+
\sum_{i<j}x_ix_j.
$$
Then
$$
q_b(x)
=
\frac12
\left(
\sum_{i=1}^{n}x_i^2
+
\left(\sum_{i=1}^{n}x_i\right)^2
\right).
$$

::: {.proof}
Use
$$
\left(\sum_i x_i\right)^2
=
\sum_i x_i^2
+
2\sum_{i<j}x_ix_j.
$$
:::

<1>5. Let
$$
e_1
=
\frac1{\sqrt n}(1,\ldots,1)
$$
and complete $e_1$ to an orthonormal basis
$$
e_1,e_2,\ldots,e_n
$$
of $\mathbb R^n$. If
$$
x
=
\sum_{j=1}^{n}y_je_j,
$$
then
$$
\sum_{i=1}^{n}x_i^2
=
\sum_{j=1}^{n}y_j^2
$$
and
$$
\sum_{i=1}^{n}x_i
=
\sqrt n,y_1.
$$

::: {.proof}
The first identity follows from orthonormality. The second follows because
the vector $(1,\ldots,1)$ equals $\sqrt n,e_1$ and is orthogonal to
$e_2,\ldots,e_n$.
:::

<1>6. Hence part (b) becomes
$$
q_b
=
\frac{n+1}{2}y_1^2
+
\frac12
\sum_{j=2}^{n}y_j^2.
$$

::: {.proof}
Substitute the identities from step <1>5 into step <1>4.
:::

<1>7. After rescaling
$$
u_1=\sqrt{\frac{n+1}{2}},y_1,
\qquad
u_j=\frac{y_j}{\sqrt2}
\quad(j\geq2),
$$
the canonical form is
$$
\boxed{u_1^2+u_2^2+\cdots+u_n^2}.
$$

::: {.proof}
Substitute the displayed rescaling into step <1>6.
:::

<1>8. Therefore part (b) has
$$
\boxed{\operatorname{rank}=n,\qquad \text{inertia}=(n,0),\qquad \text{signature}=n}.
$$

::: {.proof}
Step <1>7 has $n$ positive squares and no negative or zero squares.
:::

<1>9. For part (c), write
$$
q_c(x)
=
\sum_{i<j}x_ix_j.
$$
Then
$$
q_c(x)
=
\frac12
\left(
\left(\sum_{i=1}^{n}x_i\right)^2
-
\sum_{i=1}^{n}x_i^2
\right).
$$

::: {.proof}
Rearrange the identity
$$
\left(\sum_i x_i\right)^2
=
\sum_i x_i^2
+
2\sum_{i<j}x_ix_j.
$$
:::

<1>10. In the orthonormal coordinates from step <1>5,
$$
q_c
=
\frac{n-1}{2}y_1^2
-
\frac12
\sum_{j=2}^{n}y_j^2.
$$

::: {.proof}
Substitute
$$
\sum_i x_i=\sqrt n,y_1
$$
and
$$
\sum_i x_i^2=\sum_j y_j^2
$$
into step <1>9.
:::

<1>11. After rescaling
$$
u_1=\sqrt{\frac{n-1}{2}},y_1,
\qquad
u_j=\frac{y_j}{\sqrt2}
\quad(j\geq2),
$$
the canonical form is
$$
\boxed{u_1^2-u_2^2-\cdots-u_n^2}.
$$

::: {.proof}
Substitute the rescaling into step <1>10.
:::

<1>12. Therefore part (c) has
$$
\boxed{
\operatorname{rank}=n,
\qquad
\text{inertia}=(1,n-1),
\qquad
\text{signature}=2-n.
}
$$

::: {.proof}
Step <1>11 has one positive square and $n-1$ negative squares.
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>3, <1>8, and <1>12 give the canonical forms, ranks, and signatures
for parts (a), (b), and (c), respectively.
:::
:::
