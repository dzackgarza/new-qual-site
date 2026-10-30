---
schema: qual/card@1
id: P-UCLAB02S-08
kind: problem
title: Dimension of the annihilator of a subspace
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Exam Spring 2002 PDF. The source specifies that $V$ is real but defines functionals $f:V\to F$ without defining $F$; the intended real dual is used here.
---

::: {.problem}
Let $V$ be a finite-dimensional real vector space and let $W\subset V$ be a subspace.
Define
$$
W^0=\{f:V\to\RR\text{ linear}:f\restrict_W=0\}.
$$
Prove that
$$
\dim V=\dim W+\dim W^0.
$$
:::

::: {.solution}

Let
$$
\dim V=n
\qquad\text{and}\qquad
\dim W=r.
$$

::: pf

::: pf-step

Choose a basis
$$
w_1,\ldots,w_r
$$
of $W$ and extend it to a basis
$$
w_1,\ldots,w_r,v_{r+1},\ldots,v_n
$$
of $V$.


::: pf-proof

Every basis of a subspace of a finite-dimensional vector space extends to a basis of the ambient vector space.

:::

:::

::: pf-step

Let
$$
w_1^*,\ldots,w_r^*,v_{r+1}^*,\ldots,v_n^*
$$
be the dual basis of $V^*$.
Then
$$
v_{r+1}^*,\ldots,v_n^*
$$
all belong to $W^0$.


::: pf-proof

For
$$
j\ge r+1
$$
and
$$
i\le r,
$$
duality gives
$$
v_j^*(w_i)=0.
$$
Since
$$
w_1,\ldots,w_r
$$
span $W$, each $v_j^*$ vanishes on all of $W$.
Thus
$$
v_j^*\in W^0.
$$

:::

:::

::: {.pf-step #s1-3}

The functionals
$$
v_{r+1}^*,\ldots,v_n^*
$$
span $W^0$.


::: pf-proof

Let
$$
f\in W^0.
$$
Expand $f$ in the dual basis:
$$
f
=
\sum_{i=1}^r a_iw_i^*
+
\sum_{j=r+1}^n b_jv_j^*.
$$
For each
$$
i=1,\ldots,r,
$$
one has
$$
0
=
f(w_i)
=
a_i,
$$
because $f$ vanishes on $W$.
Hence
$$
f
=
\sum_{j=r+1}^n b_jv_j^*.
$$
Thus the displayed functionals span $W^0$.

:::

:::

::: {.pf-step #s1-4}

The functionals
$$
v_{r+1}^*,\ldots,v_n^*
$$
are linearly independent.


::: pf-proof

They are part of the dual basis, so they are linearly independent.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\dim W^0=n-r.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
v_{r+1}^*,\ldots,v_n^*
$$
form a basis of $W^0$.
There are exactly
$$
n-r
$$
such functionals.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{\dim V=\dim W+\dim W^0}.
$$


::: pf-proof

By definition,
$$
\dim V=n
\qquad\text{and}\qquad
\dim W=r.
$$
Step [](#s1-5){.pf-ref} gives
$$
\dim W^0=n-r.
$$
Therefore
$$
\dim W+\dim W^0
=
r+(n-r)
=n
=
\dim V.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required dimension formula.

:::

:::

:::
