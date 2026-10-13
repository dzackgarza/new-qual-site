---
schema: qual/card@1
id: P-TRIV-LA41
kind: problem
title: Consistency of a $3\times 3$ linear system
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 41, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Check if the system of linear equations has a solution and solve

$$
\left\{ { \begin{array} { l } { x + 2 y + 3 z = - 4 } \\ { 2 x + 3 y + 4 z = 1 } \\ { 3 x + 4 y + 5 z = 6 } \end{array} } \right.\tag{9}
$$
:::

::: {.solution}
<1>1. Subtract twice the first equation from the second. The result is
$$
y+2z=-9.
$$

::: {.proof}
The left-hand side is
$$
(2x+3y+4z)-2(x+2y+3z)
=
-y-2z,
$$
while the right-hand side is
$$
1-2(-4)=9.
$$
Thus
$$
-y-2z=9,
$$
equivalently
$$
y+2z=-9.
$$
:::

<1>2. Subtract three times the first equation from the third. The result is
again
$$
y+2z=-9.
$$

::: {.proof}
The left-hand side becomes
$$
(3x+4y+5z)-3(x+2y+3z)
=
-2y-4z,
$$
while the right-hand side is
$$
6-3(-4)=18.
$$
Hence
$$
-2y-4z=18,
$$
which reduces to the same equation as in step <1>1.
:::

<1>3. The system is consistent and has one free parameter.

::: {.proof}
Steps <1>1--<1>2 show that the second and third equations impose the same
condition after eliminating $x$. Thus no contradictory equation arises, and
the rank is $2<3$.
:::

<1>4. Let
$$
z=t.
$$
Then
$$
y=-9-2t.
$$

::: {.proof}
Solve the equation from step <1>1 for $y$.
:::

<1>5. Substituting into the first equation gives
$$
x=14+t.
$$

::: {.proof}
The first equation becomes
$$
x+2(-9-2t)+3t=-4.
$$
Thus
$$
x-18-t=-4,
$$
so
$$
x=14+t.
$$
:::

<1>6. Therefore the complete solution set is
$$
\boxed{
(x,y,z)
=
(14+t,-9-2t,t),
\qquad
t\in\mathbb R.
}
$$

::: {.proof}
Steps <1>4--<1>5 give every solution. Conversely, direct substitution shows
that every displayed triple satisfies all three original equations.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the full solution family.
:::
:::
