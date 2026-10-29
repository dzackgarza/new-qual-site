---
schema: qual/card@1
id: P-LATEST2-38
kind: problem
title: A hundredth power of a cyclic permutation matrix
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Let
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Determine $M^{100}$ from the following choices:

(A) $M$

(B) $\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}$

(C) $I_3$

(D) the zero matrix

(E) none of the above
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The matrix $M$ cyclically permutes the standard basis vectors.


::: pf-proof

Let $e_1,e_2,e_3$ be the standard basis of $\RR^3$.
From the columns of $M$,
$$
Me_1=e_3,
\qquad
Me_2=e_1,
\qquad
Me_3=e_2.
$$
Thus $M$ acts by a $3$-cycle.

:::

:::

::: {.pf-step #s1-2}

One has
$$
M^3=I_3.
$$


::: pf-proof

Applying the $3$-cycle from step [](#s1-1){.pf-ref} three times returns each basis vector to itself.
Hence
$$
M^3e_j=e_j
$$
for $j=1,2,3$, so
$$
M^3=I_3.
$$

:::

:::

::: pf-step

Since
$$
100=3\cdot33+1,
$$
one has
$$
M^{100}=M.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
\begin{aligned}
M^{100}
&=M^{99}M\\
&=(M^3)^{33}M\\
&=I_3^{33}M\\
&=M.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{M^{100}=M}.
$$


::: pf-proof

This is answer choice $\boxed{\text{(A)}}$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required value.

:::

:::

:::
