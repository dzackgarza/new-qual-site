---
schema: qual/card@1
id: P-TRIV-LA39
kind: problem
title: Solving a $3\times 3$ linear system
classification:
  areas: [prelim]
  topics: []
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
\left\{ \begin{array} { l l } { y + 3 z = - 1 } \\ { 2 x + 3 y + 5 z = 3 } \\ { 3 x + 5 y + 7 z = 6 } \end{array} \right.\tag{8}
$$
:::

::: {.solution}
<1>1. From the first equation,
$$
y=-1-3z.
$$

::: {.proof}
Rearrange
$$
y+3z=-1.
$$
:::

<1>2. Substituting step <1>1 into the second equation gives
$$
x=3+2z.
$$

::: {.proof}
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

<1>3. Substituting steps <1>1--<1>2 into the third equation gives
$$
z=-1.
$$

::: {.proof}
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

<1>4. Consequently,
$$
y=2
$$
and
$$
x=1.
$$

::: {.proof}
Substitute $z=-1$ into steps <1>1--<1>2:
$$
y=-1-3(-1)=2,
$$
and
$$
x=3+2(-1)=1.
$$
:::

<1>5. Thus the solution is
$$
\boxed{(x,y,z)=(1,2,-1)}.
$$

::: {.proof}
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

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required solution.
:::
:::
