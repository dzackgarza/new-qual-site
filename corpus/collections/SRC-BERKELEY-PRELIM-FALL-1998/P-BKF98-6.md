---
schema: qual/card@1
id: P-BKF98-6
kind: problem
title: Nullity bound for a product of linear transformations
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Restricted B to ker(AB); its kernel is ker B and its image lies in
    ker A, so rank-nullity yields the nullity bound.
---

::: {.problem}
Let $A$ and $B$ be linear transformations on a finite-dimensional vector space $V$. Prove that
\[
\dim\ker(AB)
\le
\dim\ker A+\dim\ker B.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #B-image-in-kerA}
The restriction
$$
B|_{\ker(AB)}:
\ker(AB)\longrightarrow V
$$
has image contained in
$$
\ker A.
$$

::: pf-proof
If
$$
x\in\ker(AB),
$$
then
$$
A(Bx)
=
(AB)x
=0.
$$
Hence $Bx\in\ker A$.
:::

:::

::: {.pf-step #restricted-kernel-is-kerB}
The kernel of the restricted map in step [](#B-image-in-kerA){.pf-ref} is exactly
$$
\ker B.
$$

::: pf-proof
Certainly
$$
\ker B\subseteq\ker(AB),
$$
because $Bx=0$ implies $ABx=0$. Therefore
$$
\ker\bigl(B|_{\ker(AB)}\bigr)
=
\{x\in\ker(AB):Bx=0\}
=
\ker B.
$$
:::

:::

::: {.pf-step #rank-nullity-restricted}
Rank--nullity for the restricted map gives
$$
\dim\ker(AB)
=
\dim\ker B
+
\dim B(\ker(AB)).
$$

::: pf-proof
Apply the rank--nullity theorem to
$$
B|_{\ker(AB)}.
$$
Step [](#restricted-kernel-is-kerB){.pf-ref} identifies its kernel, while its image is
$B(\ker(AB))$.
:::

:::

::: {.pf-step #image-dim-leq-kerA}
One has
$$
\dim B(\ker(AB))
\leq
\dim\ker A.
$$

::: pf-proof
Step [](#B-image-in-kerA){.pf-ref} gives the inclusion
$$
B(\ker(AB))
\subseteq
\ker A.
$$
The dimension of a subspace cannot exceed the dimension of the containing
space.
:::

:::

::: {.pf-step #nullity-bound}
Therefore
$$
\boxed{
\dim\ker(AB)
\leq
\dim\ker A+\dim\ker B
}.
$$

::: pf-proof
Substitute the estimate from step [](#image-dim-leq-kerA){.pf-ref} into the equality from step [](#rank-nullity-restricted){.pf-ref}.
:::

:::

::: pf-qed
Step [](#nullity-bound){.pf-ref} is the required inequality.
:::

:::

:::
