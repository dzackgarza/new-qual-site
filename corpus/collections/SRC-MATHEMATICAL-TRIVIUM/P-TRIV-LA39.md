---
schema: qual/card@1
id: P-TRIV-LA39
kind: problem
title: Solving a $3\times 3$ linear system
classification:
  areas: [prelim]
  topics:
  - Systems of Linear Equations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 39, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve the system of linear equations

$$
\begin{cases} y + 3z = -1 \\ 2x + 3y + 5z = 3 \\ 3x + 5y + 7z = 6 \end{cases} \tag{8}
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

From the first equation,
$$
y=-1-3z.
$$


::: pf-proof

Rearrange
$$
y+3z=-1.
$$

:::

:::

::: {.pf-step #s1-2}

Substituting step [](#s1-1){.pf-ref} into the second equation gives
$$
x=3+2z.
$$


::: pf-proof

The second equation becomes
$$
2x+3(-1-3z)+5z=3.
$$
Thus
$$
2x-3-4z=3,
$$
so
$$
2x=6+4z
$$
and hence
$$
x=3+2z.
$$

:::

:::

::: pf-step

Substituting steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} into the third equation gives
$$
z=-1.
$$


::: pf-proof

The third equation becomes
$$
3(3+2z)+5(-1-3z)+7z=6.
$$
Simplifying,
$$
9+6z-5-15z+7z=6,
$$
so
$$
4-2z=6.
$$
Therefore
$$
z=-1.
$$

:::

:::

::: pf-step

Consequently,
$$
y=2
$$
and
$$
x=1.
$$


::: pf-proof

Substitute $z=-1$ into steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}:
$$
y=-1-3(-1)=2,
$$
and
$$
x=3+2(-1)=1.
$$

:::

:::

::: {.pf-step #s1-5}

Thus the solution is
$$
\boxed{(x,y,z)=(1,2,-1)}.
$$


::: pf-proof

Direct substitution gives
$$
2+3(-1)=-1,
$$
$$
2(1)+3(2)+5(-1)=3,
$$
and
$$
3(1)+5(2)+7(-1)=6.
$$
Hence the triple satisfies all three equations.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required solution.

:::

:::

:::
