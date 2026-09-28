---
schema: qual/card@1
id: P-BERK81S-18
kind: problem
title: Real similarity of rational matrices implies rational similarity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The intertwining equation XA=BX is a homogeneous linear system with
    rational coefficients, so its real solution space has a basis of
    rational matrices. Writing the given real conjugator in this basis
    makes the determinant a nonzero polynomial with rational coefficients
    in the basis coordinates. A nonzero polynomial over Q cannot vanish on
    all of Q^d, so rational coordinates can be chosen with nonzero
    determinant, giving an invertible rational intertwiner.
---

::: {.problem}
Let $A$ and $B$ be square matrices with rational entries.
Suppose
\[
CAC^{-1}=B
\]
for some invertible real matrix $C$.
Prove that one can choose such a conjugating matrix $C$ with rational entries.
:::

::: {.solution}
Suppose $A,B\in M_n(\QQ)$.
Define
$$
W_{\QQ}
=
\{X\in M_n(\QQ):XA=BX\}
$$
and
$$
W_{\RR}
=
\{X\in M_n(\RR):XA=BX\}.
$$

<1>1. The space $W_{\RR}$ has a basis consisting of matrices in
$W_{\QQ}$.

::: {.proof}
The equation
$$
XA=BX
$$
is a homogeneous linear system in the $n^2$ entries of $X$. Since the
entries of $A$ and $B$ are rational, every coefficient of this system is
rational.

Row reduction over $\QQ$ produces a parametrization of its solutions whose
coefficient vectors are rational. The same row-reduced system describes
the solutions after allowing the free parameters to range over $\RR$.
Hence there are matrices
$$
X_1,\ldots,X_d\in W_{\QQ}
$$
which form a $\QQ$-basis of $W_{\QQ}$ and an $\RR$-basis of $W_{\RR}$.
:::

<1>2. Let
$$
C_0\in GL_n(\RR)
$$
be a matrix satisfying
$$
C_0A=BC_0.
$$
There are real numbers $t_1^{(0)},\ldots,t_d^{(0)}$ such that
$$
C_0
=
\sum_{j=1}^d
t_j^{(0)}X_j.
$$

::: {.proof}
The relation
$$
C_0AC_0^{-1}=B
$$
from the hypothesis is equivalent to
$$
C_0A=BC_0.
$$
Thus $C_0\in W_{\RR}$. Step <1>1 says that
$X_1,\ldots,X_d$ is a basis of $W_{\RR}$, so $C_0$ has the displayed
coordinates.
:::

<1>3. Define
$$
P(t_1,\ldots,t_d)
=
\det
\left(
\sum_{j=1}^d t_jX_j
\right).
$$
Then
$$
P\in\QQ[t_1,\ldots,t_d]
$$
and $P$ is not the zero polynomial.

::: {.proof}
Every entry of every $X_j$ is rational. The determinant is a polynomial
with integer coefficients in the matrix entries, so $P$ has rational
coefficients.

By step <1>2,
$$
P(t_1^{(0)},\ldots,t_d^{(0)})
=
\det C_0
\neq
0.
$$
Therefore $P$ is not identically zero.
:::

<1>4. If
$$
Q\in\QQ[x_1,\ldots,x_d]
$$
is a nonzero polynomial, then there is a point
$$
q\in\QQ^d
$$
such that
$$
Q(q)\neq0.
$$

::: {.proof}
Proceed by induction on $d$.

For $d=1$, a nonzero polynomial has only finitely many roots, while
$\QQ$ is infinite. Hence some rational number is not a root.

Suppose the statement holds for $d-1$. Write
$$
Q(x_1,\ldots,x_d)
=
\sum_{k=0}^m
Q_k(x_1,\ldots,x_{d-1})x_d^k,
$$
where at least one coefficient polynomial $Q_k$ is nonzero. By the
induction hypothesis, choose
$$
(q_1,\ldots,q_{d-1})\in\QQ^{d-1}
$$
so that this nonzero coefficient does not vanish. Then
$$
x_d
\longmapsto
Q(q_1,\ldots,q_{d-1},x_d)
$$
is a nonzero one-variable polynomial. It has only finitely many roots, so
some $q_d\in\QQ$ is not a root.
:::

<1>5. There are rational numbers $q_1,\ldots,q_d$ such that the matrix
$$
C
=
\sum_{j=1}^d q_jX_j
$$
is invertible.

::: {.proof}
Apply step <1>4 to the nonzero polynomial $P$ from step <1>3. Choose
$$
(q_1,\ldots,q_d)\in\QQ^d
$$
with
$$
P(q_1,\ldots,q_d)\neq0.
$$
By the definition of $P$,
$$
\det C
=
P(q_1,\ldots,q_d)
\neq
0.
$$
Thus $C$ is invertible. Since the $X_j$ and the coefficients $q_j$ are
rational, every entry of $C$ is rational.
:::

<1>6. The rational matrix $C$ from step <1>5 satisfies
$$
\boxed{
CAC^{-1}=B.
}
$$

::: {.proof}
Each $X_j$ lies in $W_{\QQ}$, so every rational linear combination of the
$X_j$ also lies in $W_{\QQ}$. Hence
$$
CA=BC.
$$
Step <1>5 says that $C$ is invertible. Multiplying the last equality on
the right by $C^{-1}$ gives
$$
CAC^{-1}=B.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives an invertible conjugating matrix with rational entries.
:::
:::
