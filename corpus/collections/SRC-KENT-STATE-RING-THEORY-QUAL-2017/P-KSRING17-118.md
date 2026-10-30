---
schema: qual/card@1
id: P-KSRING17-118
kind: problem
title: Matrix rings $M_n(F)$ over a field are simple
classification:
  areas: [algebra]
  topics:
  - Simple Rings
  - Matrix Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 118 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled endomorphism ring End_F(V) against problem 118 on Ring_Theory_Qual_Problems.pdf PDF page 14.
---

::: {.problem}
If $n$ is a positive integer and $F$ is any field, let $M_n(F)$ denote the ring of $n \times n$ matrices with entries in $F$.
Prove that $M_n(F)$ is a simple ring.
Equivalently, $\operatorname{End}_F(V)$ is a simple ring if $V$ is a finite dimensional vector space over $F$.
:::

::: {.solution}

Let
$$
J
\trianglelefteq
M_n(F)
$$
be a nonzero two-sided ideal.

::: pf

::: pf-step

Choose a nonzero matrix
$$
A=(a_{ij})\in J.
$$
Then some entry
$$
a_{ij}
$$
is nonzero.


::: pf-proof

Because
$$
A\ne0,
$$
not all of its entries vanish.
Choose indices
$$
i,j
$$
with
$$
a_{ij}\ne0.
$$

:::

:::

::: {.pf-step #s1-2}

For any indices
$$
k,\ell,
$$
one has
$$
E_{ki}AE_{j\ell}
=
a_{ij}E_{k\ell}.
$$


::: pf-proof

Left multiplication by
$$
E_{ki}
$$
keeps only the $i$th row of $A$ and moves it to the $k$th row.
Right multiplication by
$$
E_{j\ell}
$$
then keeps only the $j$th column and moves it to the $\ell$th column.
The unique surviving entry is
$$
a_{ij}
$$
in position
$$
(k,\ell).
$$
Thus the product is
$$
a_{ij}E_{k\ell}.
$$

:::

:::

::: {.pf-step #s1-3}

For every
$$
k,\ell,
$$
the matrix
$$
a_{ij}E_{k\ell}
$$
belongs to $J$.


::: pf-proof

Since
$$
A\in J
$$
and $J$ is a two-sided ideal,
$$
E_{ki}AE_{j\ell}
\in
J.
$$
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Every matrix unit
$$
E_{k\ell}
$$
belongs to $J$.


::: pf-proof

The scalar
$$
a_{ij}
$$
is nonzero in the field $F$, hence invertible.
The scalar matrix
$$
a_{ij}^{-1}I_n
$$
lies in
$$
M_n(F).
$$
Multiplying the element from step [](#s1-3){.pf-ref} by this scalar matrix gives
$$
(a_{ij}^{-1}I_n)
(a_{ij}E_{k\ell})
=
E_{k\ell}
\in
J.
$$

:::

:::

::: {.pf-step #s1-5}

Every matrix in
$$
M_n(F)
$$
belongs to $J$.


::: pf-proof

Every matrix
$$
B=(b_{k\ell})
$$
has the expansion
$$
B
=
\sum_{k,\ell=1}^{n}
b_{k\ell}E_{k\ell}.
$$
By step [](#s1-4){.pf-ref},
$$
E_{k\ell}\in J.
$$
Since $J$ is an ideal, each scalar multiple
$$
b_{k\ell}E_{k\ell}
$$
lies in $J$, and since $J$ is closed under finite sums,
$$
B\in J.
$$
Thus
$$
J=M_n(F).
$$

:::

:::

::: {.pf-step #s1-6}

Therefore the only two-sided ideals of
$$
M_n(F)
$$
are
$$
(0)
\qquad\text{and}\qquad
M_n(F).
$$


::: pf-proof

The zero ideal always exists.
Step [](#s1-5){.pf-ref} shows that every nonzero two-sided ideal is the whole ring.

:::

:::

::: {.pf-step #s1-7}

The ring
$$
M_n(F)
$$
is nonzero and satisfies
$$
M_n(F)^2\ne0.
$$


::: pf-proof

The identity matrix
$$
I_n
$$
is nonzero and satisfies
$$
I_n^2=I_n\ne0.
$$

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
M_n(F)
\text{ is a simple ring}.
}
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives the required ideal structure, and step [](#s1-7){.pf-ref} gives the nonzero product condition.

:::

:::

::: {.pf-step #s1-9}

If $V$ is a finite-dimensional $F$-vector space of dimension $n$, then
$$
\operatorname{End}_F(V)
\cong
M_n(F).
$$


::: pf-proof

Choose a basis of
$$
V.
$$
Every $F$-linear endomorphism is represented by a unique
$$
n\times n
$$
matrix over $F$, and composition corresponds to matrix multiplication.
Thus the matrix-representation map is a ring isomorphism.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\operatorname{End}_F(V)
\text{ is simple}.
}
$$


::: pf-proof

Simplicity is preserved by ring isomorphism.
Apply step [](#s1-8){.pf-ref} through the isomorphism in step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves the matrix-ring statement, and step [](#s1-10){.pf-ref} proves the equivalent endomorphism-ring formulation.

:::

:::

:::
