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

::: pf

::: pf-step

The assertion holds when $n=1$.

::: pf-proof

Every linear operator on the one-dimensional space $\CC$ acts by a
scalar, so every nonzero vector is an eigenvector of every member of $Y$.
This also covers the case $Y=\varnothing$.

:::

:::

::: {.pf-step #s2}

Assume $n>1$ and the assertion is known in every smaller positive
dimension. If $Y=\varnothing$, then every nonzero vector in $\CC^n$ is a
common eigenvector.

::: pf-proof

There are no eigenvector conditions to check when the family is empty.
Thus the assertion is vacuous in this case.

:::

:::

::: {.pf-step #s3}

Suppose $Y\neq\varnothing$. If every member of $Y$ is a scalar
matrix, then every nonzero vector in $\CC^n$ is a common eigenvector.

::: pf-proof

For each $A\in Y$, write
$$
A=\lambda_A I.
$$
Then every nonzero $v\in\CC^n$ satisfies
$$
Av=\lambda_Av.
$$

:::

:::

::: {.pf-step #s4}

Suppose some $A\in Y$ is not scalar. Then $A$ has an eigenspace
$$
E_\lambda=\ker(A-\lambda I)
$$
satisfying
$$
0<\dim E_\lambda<n.
$$

::: pf-proof

Because the ground field is $\CC$, the characteristic polynomial of $A$
has a root $\lambda$, so $E_\lambda\neq\{0\}$. If
$E_\lambda=\CC^n$, then $A=\lambda I$, contrary to the choice of $A$.
Thus the eigenspace is proper.

:::

:::

::: {.pf-step #s5}

The subspace $E_\lambda$ from step [](#s4){.pf-ref} is invariant under every
$B\in Y$.

::: pf-proof

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

:::

::: {.pf-step #s6}

The restricted family
$$
\{B|_{E_\lambda}:B\in Y\}
$$
is a commuting family of endomorphisms of the smaller complex vector
space $E_\lambda$.

::: pf-proof

Step [](#s5){.pf-ref} makes every restriction well-defined. For $B,C\in Y$,
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

:::

::: {.pf-step #s7}

There exists a nonzero vector $v\in E_\lambda$ that is an
eigenvector of every $B\in Y$.

::: pf-proof

By step [](#s4){.pf-ref},
$$
1\leq\dim E_\lambda<n.
$$
Apply the induction hypothesis to the commuting restricted family from
step [](#s6){.pf-ref}. It yields a nonzero $v\in E_\lambda$ such that, for every
$B\in Y$,
$$
Bv=\mu_Bv
$$
for some scalar $\mu_B\in\CC$.

:::

:::

::: {.pf-step #s8}

Therefore every commuting family $Y\subseteq M_n(\CC)$ has a
common nonzero eigenvector.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} settle the empty-family and scalar-only cases. In the
remaining case, step [](#s7){.pf-ref} gives a vector that is an eigenvector of every
member of $Y$. Since $v\in E_\lambda$, it is in particular an
eigenvector of the chosen matrix $A$ as well.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} completes the induction.

:::

:::

:::
