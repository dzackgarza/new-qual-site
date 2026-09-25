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
<1>1. The restriction
$$
B|_{\ker(AB)}:
\ker(AB)\longrightarrow V
$$
has image contained in
$$
\ker A.
$$

::: {.proof}
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

<1>2. The kernel of the restricted map in step <1>1 is exactly
$$
\ker B.
$$

::: {.proof}
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

<1>3. Rank--nullity for the restricted map gives
$$
\dim\ker(AB)
=
\dim\ker B
+
\dim B(\ker(AB)).
$$

::: {.proof}
Apply the rank--nullity theorem to
$$
B|_{\ker(AB)}.
$$
Step <1>2 identifies its kernel, while its image is
$B(\ker(AB))$.
:::

<1>4. One has
$$
\dim B(\ker(AB))
\leq
\dim\ker A.
$$

::: {.proof}
Step <1>1 gives the inclusion
$$
B(\ker(AB))
\subseteq
\ker A.
$$
The dimension of a subspace cannot exceed the dimension of the containing
space.
:::

<1>5. Therefore
$$
\boxed{
\dim\ker(AB)
\leq
\dim\ker A+\dim\ker B
}.
$$

::: {.proof}
Substitute the estimate from step <1>4 into the equality from step <1>3.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required inequality.
:::
:::
