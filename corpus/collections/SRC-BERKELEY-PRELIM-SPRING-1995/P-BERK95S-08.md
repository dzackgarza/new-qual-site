---
schema: qual/card@1
id: P-BERK95S-08
kind: problem
title: Determinant of $I-tL$ when the image of $L$ lies in an invariant subspace
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
  date: 2026-09-23
---

::: {.problem}
Let $W\subset V$ be finite-dimensional vector spaces over a field, and let $L:V\to V$ satisfy
\[
L(V)\subset W.
\]
Let $L_W:W\to W$ be the restriction of $L$. Prove that
\[
\det(I_V-tL)=\det(I_W-tL_W).
\]
:::

::: {.solution}
Choose a basis $w_1,\ldots,w_r$ of $W$ and extend it to a basis
$$
w_1,\ldots,w_r,v_1,\ldots,v_s
$$
of $V$.

::: pf

::: {.pf-step #s1}

In this basis, the matrix of $L$ has block form
$$
[L]=
\begin{pmatrix}
[L_W]&B\\
0&0
\end{pmatrix}
$$
for some matrix $B$.

::: pf-proof

Because $L(W)\subseteq L(V)\subseteq W$, the restriction $L_W$ is
well-defined and gives the upper-left block. Since every vector
$L(v_j)$ lies in $W$, all coordinates of $L(v_j)$ in the complementary
basis vectors $v_1,\ldots,v_s$ vanish. Hence the entire lower row of
blocks is zero.

:::

:::

::: {.pf-step #s2}

In the same basis,
$$
[I_V-tL]
=
\begin{pmatrix}
I_W-t[L_W]&-tB\\
0&I_s
\end{pmatrix}.
$$

::: pf-proof

Subtract $t[L]$ from the identity matrix, using the block form from
step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

$$
\det(I_V-tL)=\det(I_W-tL_W).
$$

::: pf-proof

The matrix in step [](#s2){.pf-ref} is block upper triangular. Therefore
$$
\det(I_V-tL)
=
\det(I_W-tL_W)\det(I_s)
=
\det(I_W-tL_W).
$$
This calculation holds in the polynomial ring over the ground field,
so it proves the asserted identity in $t$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required determinant identity.

:::

:::

:::
