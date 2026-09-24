---
schema: qual/card@1
id: P-BKF16-7A
kind: problem
title: Rational matrices similar over $\mathbb C$ are similar over $\mathbb Q$
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
    Independently checked the retained Fall 2016 solution packet: the
    intertwining equation is a rational linear system, and the determinant
    restricted to its rational solution space is a nonzero rational
    polynomial.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked scalar extension of the rational solution space, nonvanishing
    of the determinant polynomial, and the induction showing that a
    nonzero rational polynomial is nonzero at some rational point.
---

::: {.problem}
Let A and B be two $n \times n$ matrices with coefficients in Q. For any field extension K of Q, we say that A and B are similar over K if $A = P B P ^ { - 1 }$ for some $n \times n$ invertible matrix P with coefficients in K. Prove that A and B are similar over Q if and only if they are similar over C.
:::

::: {.solution}
<1>1. If $A$ and $B$ are similar over $\QQ$, then they are similar
over $\CC$.

::: {.proof}
An invertible matrix with entries in $\QQ$ is also an invertible
matrix with entries in $\CC$, since $\QQ\subset\CC$. Thus the same
conjugating matrix works over $\CC$.
:::

<1>2. Define
$$
V_{\QQ}
\coloneqq
\{X\in M_n(\QQ):AX=XB\}
$$
and
$$
V_{\CC}
\coloneqq
\{X\in M_n(\CC):AX=XB\}.
$$
Then $V_{\CC}$ has a basis consisting of matrices in $V_{\QQ}$.

::: {.proof}
The matrix equation
$$
AX=XB
$$
is a homogeneous system of $n^2$ linear equations in the $n^2$
entries of $X$. Because $A$ and $B$ have rational entries, all
coefficients of this linear system lie in $\QQ$.

Row reduction of its coefficient matrix can therefore be carried out
over $\QQ$. The resulting rational parametrization of the solution
space gives matrices
$$
Q_1,\ldots,Q_m\in M_n(\QQ)
$$
that form a $\QQ$-basis of $V_{\QQ}$. The same row-reduced system over
$\CC$ has the same pivot and free variables, so these same matrices
form a $\CC$-basis of $V_{\CC}$.
:::

<1>3. Assume $A$ and $B$ are similar over $\CC$. Then there is an
invertible matrix
$$
P\in V_{\CC}.
$$

::: {.proof}
Complex similarity gives
$$
A=PBP^{-1}
$$
for some $P\in\operatorname{GL}_n(\CC)$. Multiplying on the right by
$P$ gives
$$
AP=PB,
$$
so $P\in V_{\CC}$.
:::

<1>4. Let
$$
Q_1,\ldots,Q_m
$$
be the rational basis from step <1>2 and define
$$
D(y_1,\ldots,y_m)
\coloneqq
\det\left(
\sum_{r=1}^m y_rQ_r
\right).
$$
Then
$$
D\in\QQ[y_1,\ldots,y_m]
$$
and $D$ is not the zero polynomial.

::: {.proof}
The entries of each $Q_r$ are rational and each entry of
$$
\sum_r y_rQ_r
$$
is a rational linear polynomial in the variables $y_r$. The
determinant formula therefore shows that $D$ has rational
coefficients.

By steps <1>2--<1>3, write
$$
P=\sum_{r=1}^m c_rQ_r
$$
with $c_r\in\CC$. Since $P$ is invertible,
$$
D(c_1,\ldots,c_m)
=
\det P
\ne
0.
$$
Hence $D$ is not identically zero.
:::

<1>5. If
$$
F\in\QQ[y_1,\ldots,y_m]
$$
is a nonzero polynomial, then there exists
$$
(q_1,\ldots,q_m)\in\QQ^m
$$
such that
$$
F(q_1,\ldots,q_m)\ne0.
$$

::: {.proof}
Proceed by induction on $m$. For $m=1$, a nonzero one-variable
polynomial has only finitely many roots, while $\QQ$ is infinite, so a
rational nonroot exists.

Suppose $m>1$. Write
$$
F
=
\sum_{k=0}^d
F_k(y_1,\ldots,y_{m-1})y_m^k
$$
with at least one coefficient polynomial $F_k$ nonzero. By the
induction hypothesis, choose
$$
q_1,\ldots,q_{m-1}\in\QQ
$$
so that this nonzero coefficient satisfies
$$
F_k(q_1,\ldots,q_{m-1})\ne0.
$$
Then
$$
y_m\longmapsto
F(q_1,\ldots,q_{m-1},y_m)
$$
is a nonzero one-variable polynomial over $\QQ$. Choose a rational
$q_m$ that is not one of its finitely many roots.
:::

<1>6. There is an invertible matrix
$$
Q\in V_{\QQ}.
$$

::: {.proof}
Apply step <1>5 to the nonzero polynomial $D$ from step <1>4. Choose
$$
q_1,\ldots,q_m\in\QQ
$$
with
$$
D(q_1,\ldots,q_m)\ne0,
$$
and set
$$
Q
\coloneqq
\sum_{r=1}^m q_rQ_r.
$$
Since $V_{\QQ}$ is a vector space, $Q\in V_{\QQ}$. Its entries are
rational, and
$$
\det Q
=
D(q_1,\ldots,q_m)
\ne
0,
$$
so $Q$ is invertible.
:::

<1>7. If $A$ and $B$ are similar over $\CC$, then they are similar
over $\QQ$.

::: {.proof}
By step <1>6, there is an invertible rational matrix $Q$ satisfying
$$
AQ=QB.
$$
Multiplying on the right by $Q^{-1}$ gives
$$
A=QBQ^{-1}.
$$
Thus $A$ and $B$ are similar over $\QQ$.
:::

<1>8. Therefore
$$
\boxed{
A\text{ and }B\text{ are similar over }\QQ
\iff
A\text{ and }B\text{ are similar over }\CC.
}
$$

::: {.proof}
The forward implication is step <1>1 and the reverse implication is
step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required equivalence.
:::
:::
