---
schema: qual/card@1
id: P-ALGF23D
kind: problem
title: "Tensor products of projective and flat modules over commutative rings"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; both tensor-product assertions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified projectivity by exhibiting the tensor product as a direct summand of a free tensor product and flatness by associativity of tensor and exactness of the two flat tensor functors.
---

::: problem
Suppose $A$ is a unital commutative ring.

(a) Suppose $P_1$ and $P_2$ are projective $A$-modules.
Prove that $P_1 \otimes_A P_2$ is a projective $A$-module.

(b) Suppose $M_1$ and $M_2$ are flat $A$-modules.
Prove that $M_1 \otimes_A M_2$ is a flat $A$-module.
:::

::: {.solution}
<1>1. Choose free $A$-modules $F_1,F_2$ and modules $Q_1,Q_2$ such that
\[
F_1\cong P_1\oplus Q_1,
\qquad
F_2\cong P_2\oplus Q_2.
\]
::: {.proof}
An $A$-module is projective if and only if it is a direct summand of a free module.
Apply this characterization separately to $P_1$ and $P_2$.
:::

<1>2. The tensor product $F_1\otimes_A F_2$ is free.
::: {.proof}
Let $(e_i)_{i\in I}$ and $(f_j)_{j\in J}$ be bases of $F_1$ and $F_2$.
Then
\[
F_1\cong\bigoplus_{i\in I}A,
\qquad
F_2\cong\bigoplus_{j\in J}A.
\]
Tensor product commutes with direct sums in each variable, so
\[
F_1\otimes_A F_2
\cong
\bigoplus_{(i,j)\in I\times J}A.
\]
Thus it is free, with basis given by the pure tensors $e_i\otimes f_j$.
:::

<1>3. The module $P_1\otimes_A P_2$ is a direct summand of $F_1\otimes_A F_2$.
::: {.proof}
Using <1>1 and distributivity of tensor product over direct sums,
\[
F_1\otimes_A F_2
\cong
(P_1\oplus Q_1)\otimes_A(P_2\oplus Q_2)
\]
and hence
\[
F_1\otimes_A F_2
\cong
(P_1\otimes_A P_2)
\oplus(P_1\otimes_A Q_2)
\oplus(Q_1\otimes_A P_2)
\oplus(Q_1\otimes_A Q_2).
\]
Therefore $P_1\otimes_A P_2$ is a direct summand.
:::

<1>4. The module $P_1\otimes_A P_2$ is projective.
::: {.proof}
By <1>2, $F_1\otimes_A F_2$ is free, and by <1>3 the desired tensor product is a direct summand of it.
Every direct summand of a free module is projective.
This proves part (a).
:::

<1>5. For every $A$-module $X$, there is a natural isomorphism
\[
X\otimes_A(M_1\otimes_A M_2)
\cong
(X\otimes_A M_1)\otimes_A M_2.
\]
::: {.proof}
This is the associativity isomorphism for tensor products over the commutative ring $A$.
:::

<1>6. The functor
\[
-\otimes_A(M_1\otimes_A M_2)
\]
is exact.
::: {.proof}
Since $M_1$ is flat, the functor
\[
-\otimes_A M_1
\]
is exact.
Since $M_2$ is flat, the functor
\[
-\otimes_A M_2
\]
is exact as well.
Their composite is therefore exact.
By <1>5, that composite is naturally isomorphic to
\[
-\otimes_A(M_1\otimes_A M_2).
\]
Hence the latter functor is exact.
:::

<1>7. The module $M_1\otimes_A M_2$ is flat.
::: {.proof}
Flatness is exactly the exactness of the tensor functor in <1>6.
Thus $M_1\otimes_A M_2$ is flat, proving part (b).
:::
:::
