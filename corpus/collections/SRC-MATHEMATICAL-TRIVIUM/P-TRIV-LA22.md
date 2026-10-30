---
schema: qual/card@1
id: P-TRIV-LA22
kind: problem
title: Common eigenvectors and commuting transformations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the transformations $A$, $B$ of the vector space $\RR^n$ sharing the same eigenvectors. Is this sufficient for their commutator to be zero? Is this necessary for their commutator to be zero?
:::

::: {.solution}

Interpret “sharing the same eigenvectors” as having a basis of common
eigenvectors.

::: pf

::: {.pf-step #s1-1}

If $A$ and $B$ have a basis
$$
v_1,\ldots,v_n
$$
of common eigenvectors, then
$$
[A,B]=0.
$$


::: pf-proof

For each $j$, write
$$
Av_j=\lambda_jv_j,
\qquad
Bv_j=\mu_jv_j.
$$
Then
$$
ABv_j
=
A(\mu_jv_j)
=
\mu_j\lambda_jv_j,
$$
while
$$
BAv_j
=
B(\lambda_jv_j)
=
\lambda_j\mu_jv_j.
$$
Hence
$$
(AB-BA)v_j=0
$$
for every basis vector $v_j$. Therefore
$$
AB-BA=0.
$$

:::

:::

::: {.pf-step #s1-2}

Thus a common eigenbasis is sufficient for the commutator to vanish.


::: pf-proof

This is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

A common eigenbasis is not necessary for two transformations to
commute.


::: pf-proof

In $\RR^2$, take
$$
A=I,
\qquad
B=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
$$
Since $A=I$,
$$
AB=BA=B,
$$
so the commutator is zero.

However, $B$ is a nontrivial Jordan block. Its eigenspace is
$$
\ker(B-I)
=
\operatorname{span}
\left\{
\begin{pmatrix}1\\0\end{pmatrix}
\right\},
$$
which is one-dimensional. Thus $B$ has no eigenbasis, and consequently there
cannot be a basis of common eigenvectors of $A$ and $B$.

:::

:::

::: {.pf-step #s1-4}

Therefore the answers are
$$
\boxed{\text{sufficient: yes; necessary: no}.}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves sufficiency, and step [](#s1-3){.pf-ref} gives a counterexample to
necessity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers both questions.

:::

:::

:::
