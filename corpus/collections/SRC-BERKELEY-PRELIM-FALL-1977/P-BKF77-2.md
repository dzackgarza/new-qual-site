---
schema: qual/card@1
id: P-BKF77-2
kind: problem
title: Homogeneous systems and dimension of finite-dimensional vector spaces
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the underdetermined homogeneous-system result by elementary elimination and induction, then used it to compare the sizes of maximal independent subsets without invoking rank-nullity."
---

::: problem
(a) Using only the axioms for a field $F$, prove that a system of $m$ homogeneous linear equations in $n$ unknowns with $m<n$ and coefficients in $F$ has a nonzero solution.

(b) Use part (a) to show that if $V$ is a vector space over $F$ spanned by finitely many elements, then every maximal linearly independent subset of $V$ has the same number of elements.
:::

::: solution
<1>1. Prove part (a) by induction on the number of equations.
::: proof
We prove the following statement for every $m\ge0$: if
$$
m<n,
$$
then every system of $m$ homogeneous linear equations in $n$ unknowns over
$F$ has a nonzero solution.

If $m=0$, there are no equations, so for example
$$
(1,0,\ldots,0)
$$
is a nonzero solution.

Now suppose $m>0$ and the assertion is known for $m-1$ equations. Consider
$$
\sum_{j=1}^n a_{ij}x_j=0,
\qquad 1\le i\le m.
$$
If the first equation is identically zero, discard it. The remaining
$m-1$ equations still have $m-1<n$ unknowns, so by induction they have a
nonzero solution.

Otherwise some coefficient in the first equation is nonzero. After merely
renumbering the unknowns, assume
$$
a_{11}\ne0.
$$
The first equation is then equivalent, using only field operations, to
$$
x_1=-a_{11}^{-1}\sum_{j=2}^n a_{1j}x_j.
$$
Substitute this expression into equations $2,\ldots,m$. We obtain
$m-1$ homogeneous linear equations in the $n-1$ unknowns
$$
x_2,\ldots,x_n.
$$
Since $m<n$,
$$
m-1<n-1.
$$
The induction hypothesis therefore gives a nonzero solution
$(x_2,\ldots,x_n)$ of the reduced system. Define $x_1$ by the displayed
formula. Then all $m$ original equations hold, and the resulting vector is
nonzero because its last $n-1$ coordinates are not all zero.

Thus every such homogeneous system has a nonzero solution.
:::

<1>2. Any linearly independent subset of a finitely spanned space is finite.
::: proof
Suppose
$$
V=\operatorname{span}\{v_1,\ldots,v_N\}.
$$
Take any $N+1$ vectors
$$
w_1,\ldots,w_{N+1}\in V.
$$
Write
$$
w_j=\sum_{i=1}^N a_{ij}v_i.
$$
The equation
$$
c_1w_1+\cdots+c_{N+1}w_{N+1}=0
$$
is implied by the $N$ homogeneous equations
$$
\sum_{j=1}^{N+1}a_{ij}c_j=0,
\qquad 1\le i\le N.
$$
There are $N$ equations in $N+1$ unknowns, so part (a) gives a nonzero
solution $(c_1,\ldots,c_{N+1})$. Hence every $N+1$ vectors in $V$ are
linearly dependent. Therefore a linearly independent subset of $V$ has at
most $N$ elements.
:::

<1>3. Every maximal linearly independent subset spans $V$.
::: proof
Let $B$ be maximal linearly independent. By step <1>2 it is finite. If
$$
\operatorname{span}B\ne V,
$$
choose
$$
v\in V\setminus\operatorname{span}B.
$$
Then $B\cup\{v\}$ is linearly independent, contradicting maximality. Thus
$B$ spans $V$ and is a basis.
:::

<1>4. Any two maximal linearly independent subsets have the same cardinality.
::: proof
Let
$$
B=\{b_1,\ldots,b_r\},
\qquad
C=\{c_1,\ldots,c_s\}
$$
be maximal linearly independent subsets. By step <1>3 both are bases.

Suppose, for contradiction, that $r>s$. Since $C$ spans $V$, write
$$
b_j=\sum_{i=1}^s a_{ij}c_i
$$
for $1\le j\le r$. By part (a), the $s$ homogeneous equations
$$
\sum_{j=1}^r a_{ij}x_j=0,
\qquad 1\le i\le s,
$$
in the $r$ unknowns $x_1,\ldots,x_r$ have a nonzero solution because
$s<r$. For that solution,
$$
\sum_{j=1}^r x_jb_j
=\sum_{i=1}^s\left(\sum_{j=1}^r a_{ij}x_j\right)c_i
=0,
$$
contradicting the linear independence of $B$. Hence
$$
r\le s.
$$
Interchanging $B$ and $C$ gives $s\le r$. Therefore
$$
\boxed{r=s.}
$$
So every maximal linearly independent subset of $V$ has the same number of
elements.
:::
:::
