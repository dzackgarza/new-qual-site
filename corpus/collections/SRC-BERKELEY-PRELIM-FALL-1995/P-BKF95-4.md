---
schema: qual/card@1
id: P-BKF95-4
kind: problem
title: Complex similarity of real matrices implies real similarity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Wrote the complex intertwiner as X+iY. Every real combination X+tY
    still intertwines A and B, and det(X+tY) is a nonzero real polynomial
    because its value at t=i is det C.
---

::: {.problem}
Suppose $A,B$ are real $n\times n$ matrices and $C$ is an invertible complex $n\times n$ matrix such that
\[
CAC^{-1}=B.
\]
Find an invertible real $n\times n$ matrix $D$ such that
\[
DAD^{-1}=B.
\]
:::

::: {.solution}
Write
$$
C=X+iY
$$
with
$$
X,Y\in M_n(\RR).
$$

<1>1. The real matrices $X$ and $Y$ satisfy
$$
XA=BX
\qquad\text{and}\qquad
YA=BY.
$$

::: {.proof}
The hypothesis
$$
CAC^{-1}=B
$$
is equivalent to
$$
CA=BC.
$$
Substitute $C=X+iY$:
$$
(X+iY)A
=
B(X+iY).
$$
Since $A$ and $B$ are real, equality of real and imaginary parts gives the
two displayed relations.
:::

<1>2. For every real number $t$, the real matrix
$$
D_t\coloneqq X+tY
$$
satisfies
$$
D_tA=BD_t.
$$

::: {.proof}
By step <1>1,
$$
\begin{aligned}
D_tA
&=
XA+tYA\\
&=
BX+tBY\\
&=
B(X+tY)\\
&=
BD_t.
\end{aligned}
$$
:::

<1>3. The polynomial
$$
p(t)\coloneqq\det(X+tY)\in\RR[t]
$$
is not identically zero.

::: {.proof}
Evaluate the polynomial at the complex number $i$:
$$
p(i)
=
\det(X+iY)
=
\det C.
$$
The matrix $C$ is invertible, so $\det C\neq0$. Hence $p$ cannot be the
zero polynomial.
:::

<1>4. There is a real number $t_0$ such that
$$
\det(X+t_0Y)\neq0.
$$

::: {.proof}
By step <1>3, $p$ is a nonzero polynomial. It has only finitely many real
roots, so choose any real $t_0$ outside that finite set.
:::

<1>5. The real matrix
$$
\boxed{D=X+t_0Y}
$$
is invertible and satisfies
$$
DAD^{-1}=B.
$$

::: {.proof}
Step <1>4 gives $\det D\neq0$, so $D$ is invertible. Step <1>2 gives
$$
DA=BD.
$$
Multiplying on the right by $D^{-1}$ yields
$$
DAD^{-1}=B.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 constructs the required invertible real matrix.
:::
:::
