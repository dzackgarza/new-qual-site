---
schema: qual/card@1
id: P-UCLAB06S-10
kind: problem
title: Commuting complex matrices have a common eigenvector
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the retained UCLA Basic Examination Spring 2006 PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Proved the statement for an arbitrary commuting family by induction on
    dimension. A nonscalar member has a nonzero proper eigenspace invariant
    under every matrix in the family; the scalar-only and empty-family cases
    are immediate.
---

::: {.problem}
Let Y be an arbitrary set of commuting matrices in $M _ { n } ( \mathbf { C } )$ $( \mathrm { i . e . , } A B = B A$ for all $A , B \in Y )$ Prove that there exists a non-zero vector $v \in \mathbf { C } ^ { n }$ which is a common eigenvector of all elements of Y.
:::

::: {.solution}
We prove the assertion by induction on $n$.

<1>1. The assertion holds when $n=1$.

::: {.proof}
Every linear operator on the one-dimensional space $\CC$ acts by a
scalar, so every nonzero vector is an eigenvector of every member of $Y$.
This also covers the case $Y=\varnothing$.
:::

<1>2. Assume $n>1$ and the assertion is known in every smaller positive
dimension. If $Y=\varnothing$, then every nonzero vector in $\CC^n$ is a
common eigenvector.

::: {.proof}
There are no eigenvector conditions to check when the family is empty.
Thus the assertion is vacuous in this case.
:::

<1>3. Suppose $Y\neq\varnothing$. If every member of $Y$ is a scalar
matrix, then every nonzero vector in $\CC^n$ is a common eigenvector.

::: {.proof}
For each $A\in Y$, write
$$
A=\lambda_A I.
$$
Then every nonzero $v\in\CC^n$ satisfies
$$
Av=\lambda_Av.
$$
:::

<1>4. Suppose some $A\in Y$ is not scalar. Then $A$ has an eigenspace
$$
E_\lambda=\ker(A-\lambda I)
$$
satisfying
$$
0<\dim E_\lambda<n.
$$

::: {.proof}
Because the ground field is $\CC$, the characteristic polynomial of $A$
has a root $\lambda$, so $E_\lambda\neq\{0\}$. If
$E_\lambda=\CC^n$, then $A=\lambda I$, contrary to the choice of $A$.
Thus the eigenspace is proper.
:::

<1>5. The subspace $E_\lambda$ from step <1>4 is invariant under every
$B\in Y$.

::: {.proof}
Let $v\in E_\lambda$. Since $A$ and $B$ commute,
$$
A(Bv)
=
B(Av)
=
B(\lambda v)
=
\lambda Bv.
$$
Hence $Bv\in E_\lambda$.
:::

<1>6. The restricted family
$$
\{B|_{E_\lambda}:B\in Y\}
$$
is a commuting family of endomorphisms of the smaller complex vector
space $E_\lambda$.

::: {.proof}
Step <1>5 makes every restriction well-defined. For $B,C\in Y$,
$$
(B|_{E_\lambda})(C|_{E_\lambda})
=
(BC)|_{E_\lambda}
=
(CB)|_{E_\lambda}
=
(C|_{E_\lambda})(B|_{E_\lambda}),
$$
because the members of $Y$ commute.
:::

<1>7. There exists a nonzero vector $v\in E_\lambda$ that is an
eigenvector of every $B\in Y$.

::: {.proof}
By step <1>4,
$$
1\leq\dim E_\lambda<n.
$$
Apply the induction hypothesis to the commuting restricted family from
step <1>6. It yields a nonzero $v\in E_\lambda$ such that, for every
$B\in Y$,
$$
Bv=\mu_Bv
$$
for some scalar $\mu_B\in\CC$.
:::

<1>8. Therefore every commuting family $Y\subseteq M_n(\CC)$ has a
common nonzero eigenvector.

::: {.proof}
Steps <1>2 and <1>3 settle the empty-family and scalar-only cases. In the
remaining case, step <1>7 gives a vector that is an eigenvector of every
member of $Y$. Since $v\in E_\lambda$, it is in particular an
eigenvector of the chosen matrix $A$ as well.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 completes the induction.
:::
:::
