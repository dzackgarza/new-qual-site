---
schema: qual/card@1
id: P-TRIV-LA42
kind: problem
title: Coplanarity of four points in $\RR^3$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 42, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash prints this source number as `4.` between Problems 41 and 43; source order determines that it is Problem 42.
---

::: {.problem}
Check if the following points belong to the same plane: (6, 1, 2), (2, 3, 1), (3, 4, 1), (6, 2, 2).
:::

::: {.solution}

Let
$$
p_1=(6,1,2),
\quad
p_2=(2,3,1),
\quad
p_3=(3,4,1),
\quad
p_4=(6,2,2).
$$

::: pf

::: pf-step

Form the displacement vectors from $p_1$:
$$
v_2=p_2-p_1=(-4,2,-1),
$$
$$
v_3=p_3-p_1=(-3,3,-1),
$$
and
$$
v_4=p_4-p_1=(0,1,0).
$$


::: pf-proof

These are obtained by coordinate-wise subtraction.

:::

:::

::: {.pf-step #s1-2}

One has
$$
v_3\times v_4=(1,0,-3).
$$


::: pf-proof

Compute
$$
(-3,3,-1)\times(0,1,0)
=
\bigl(3\cdot0-(-1)\cdot1,
-((-3)\cdot0-(-1)\cdot0),
(-3)\cdot1-3\cdot0\bigr),
$$
which equals $(1,0,-3)$.

:::

:::

::: {.pf-step #s1-3}

The scalar triple product is
$$
v_2\cdot(v_3\times v_4)=-1.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
(-4,2,-1)\cdot(1,0,-3)
=
-4+0+3
=
-1.
$$

:::

:::

::: {.pf-step #s1-4}

The three displacement vectors are linearly independent.


::: pf-proof

Their scalar triple product is nonzero by step [](#s1-3){.pf-ref}. Equivalently, the
$3\times3$ matrix with these vectors as columns has nonzero determinant.

:::

:::

::: {.pf-step #s1-5}

Therefore the four points do not lie in one plane.


::: pf-proof

Four points in $\RR^3$ are coplanar exactly when the three displacement
vectors from one of the points are linearly dependent. Step [](#s1-4){.pf-ref} shows that
they are linearly independent.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{\text{the four points are not coplanar}.}
$$


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
