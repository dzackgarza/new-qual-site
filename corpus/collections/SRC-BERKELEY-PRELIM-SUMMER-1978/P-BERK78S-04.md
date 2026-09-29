---
schema: qual/card@1
id: P-BERK78S-04
kind: problem
title: Homogeneous systems and the dimension of a finitely spanned vector space
classification:
  areas:
  - prelim
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
    Proved the homogeneous-system statement by induction on the number of
    equations, eliminating one variable from a nonzero first equation.
    Then used it to show that an independent set in a space spanned by s
    vectors has at most s elements. Maximal independent subsets span the
    whole space, so applying that bound in both directions gives equal
    cardinalities.
---

::: {.problem}
1. Using only the axioms for a field $F$, prove that a system of $m$ homogeneous linear equations in $n$ unknowns with $m<n$ and coefficients in $F$ has a nonzero solution.
2. Use part 1 to show that if a vector space $V$ over $F$ is spanned by finitely many elements, then every maximal linearly independent subset of $V$ has the same number of elements.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (1) holds when there are no equations.

::: pf-proof

If $m=0$, there are no constraints on the $n>0$ unknowns. For example,
$$
(1,0,\ldots,0)
$$
is a nonzero solution.

:::

:::

::: {.pf-step #s2}

Assume part (1) holds for every homogeneous system with
$m-1$ equations and more than $m-1$ unknowns. Then it holds for a system
of $m$ equations in $n$ unknowns with $m<n$.

::: pf-proof

Write the system as
$$
\sum_{j=1}^n a_{ij}x_j=0,
\qquad
1\leq i\leq m.
$$

If the first equation is the zero equation, discard it. The remaining
$m-1$ equations in the same $n$ unknowns have a nonzero solution by the
induction hypothesis, since
$$
m-1<n.
$$

Otherwise, some coefficient in the first equation is nonzero. After
renumbering the unknowns, assume
$$
a_{1n}\neq0.
$$
The first equation is equivalent to
$$
x_n
=
-a_{1n}^{-1}
\sum_{j=1}^{n-1}a_{1j}x_j.
$$
Substitute this expression for $x_n$ into equations
$2,\ldots,m$. The result is a homogeneous system of $m-1$ equations in
the $n-1$ unknowns
$$
x_1,\ldots,x_{n-1}.
$$
Because
$$
m-1<n-1,
$$
the induction hypothesis gives a nonzero solution
$$
(x_1,\ldots,x_{n-1}).
$$
Define $x_n$ by the displayed formula. Then all $m$ original equations
hold. The full vector is nonzero because its first $n-1$ coordinates are
not all zero.

:::

:::

::: {.pf-step #s3}

Every system of $m$ homogeneous linear equations in $n$ unknowns
over $F$ with $m<n$ has a nonzero solution.

::: pf-proof

Step [](#s1){.pf-ref} is the base case for induction on $m$, and step [](#s2){.pf-ref} is the
inductive step.

:::

:::

::: {.pf-step #s4}

If a vector space is spanned by $s$ vectors, then every linearly
independent subset has at most $s$ elements.

::: pf-proof

Suppose
$$
V=\operatorname{span}\{v_1,\ldots,v_s\}
$$
and suppose, toward a contradiction, that
$$
w_1,\ldots,w_r
$$
are linearly independent with $r>s$.
For each $j$, write
$$
w_j=\sum_{i=1}^s a_{ij}v_i.
$$
Consider scalars $c_1,\ldots,c_r$. The equation
$$
\sum_{j=1}^r c_jw_j=0
$$
is implied by the homogeneous system
$$
\sum_{j=1}^r a_{ij}c_j=0,
\qquad
1\leq i\leq s.
$$
This is a system of $s$ homogeneous equations in $r>s$ unknowns.
By step [](#s3){.pf-ref} it has a nonzero solution
$$
(c_1,\ldots,c_r).
$$
For that solution,
$$
\sum_{j=1}^r c_jw_j
=
\sum_{i=1}^s
\left(
\sum_{j=1}^r a_{ij}c_j
\right)v_i
=
0,
$$
which is a nontrivial linear relation among the $w_j$. This contradicts
their linear independence.

:::

:::

::: {.pf-step #s5}

Every maximal linearly independent subset of a finitely spanned
vector space is finite.

::: pf-proof

Suppose $V$ is spanned by $s$ vectors. By step [](#s4){.pf-ref}, no linearly
independent subset can contain more than $s$ elements. Hence every maximal
linearly independent subset is finite.

:::

:::

::: {.pf-step #s6}

Every maximal linearly independent subset of $V$ spans $V$.

::: pf-proof

Let $B$ be maximal linearly independent. If
$$
\operatorname{span}B\neq V,
$$
choose
$$
v\in V\sm\operatorname{span}B.
$$
Then
$$
B\cup\{v\}
$$
is linearly independent: any relation involving $v$ with nonzero
coefficient would express $v$ as an element of $\operatorname{span}B$.
This contradicts maximality of $B$. Therefore
$$
\operatorname{span}B=V.
$$

:::

:::

::: {.pf-step #s7}

Any two maximal linearly independent subsets of $V$ have the same
number of elements.

::: pf-proof

Let
$$
B=\{b_1,\ldots,b_r\},
\qquad
C=\{c_1,\ldots,c_s\}
$$
be maximal linearly independent subsets. They are finite by step [](#s5){.pf-ref} and
span $V$ by step [](#s6){.pf-ref}.

Since $C$ spans $V$ and $B$ is linearly independent, step [](#s4){.pf-ref} gives
$$
r\leq s.
$$
Since $B$ spans $V$ and $C$ is linearly independent, the same step gives
$$
s\leq r.
$$
Hence
$$
r=s.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (1), and step [](#s7){.pf-ref} proves part (2).

:::

:::

:::
