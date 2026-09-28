---
schema: qual/card@1
id: P-BKF13-8A
kind: problem
title: Ring elements with several right inverses are exactly the right-invertible nonunits
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 8A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the one-sided zero-divisor issue forced by a right inverse and the
    construction of a distinct second right inverse for every nonunit.
---

::: {.problem}
Let R be a (possibly non-commutative) ring with identity, and let u be an element of R with a right inverse.
Prove that the following conditions on u are equivalent:

1. u has more than one right inverse;

2. u is a zero divisor;

3. u is not a unit.
:::

::: {.solution}
Fix a right inverse $v$ of $u$, so
$$
uv=1.
$$

<1>1. If $wu=0$, then $w=0$.

::: {.proof}
Using $uv=1$,
$$
w=w(uv)=(wu)v=0.
$$
Thus $u$ has no nonzero left annihilator. In particular, under either
standard convention for zero divisors in a noncommutative ring,
condition 2 here is equivalent to the existence of some nonzero $w$
with $uw=0$.
:::

<1>2. Condition 1 implies condition 2.

::: {.proof}
Suppose $v'$ is a second right inverse, with $v'\ne v$. Then
$$
u(v-v')
=uv-uv'
=1-1
=0,
$$
while $v-v'\ne0$. Hence $u$ is a zero divisor.
:::

<1>3. Condition 2 implies condition 3.

::: {.proof}
If $u$ were a unit and $uw=0$, then multiplying on the left by
$u^{-1}$ would give $w=0$. Together with step <1>1, this shows that a
unit cannot be a zero divisor. Therefore condition 2 forces $u$ not to
be a unit.
:::

<1>4. Condition 3 implies condition 1.

::: {.proof}
Assume $u$ is not a unit. Since $uv=1$, one must have
$$
vu\ne1;
$$
otherwise $v$ would be a two-sided inverse of $u$. Set
$$
w\coloneqq vu-1.
$$
Then $w\ne0$, and
$$
uw
=uvu-u
=(uv)u-u
=0.
$$
Consequently
$$
v'\coloneqq v+w
$$
is distinct from $v$ and satisfies
$$
uv'
=uv+uw
=1.
$$
Thus $u$ has more than one right inverse.
:::

<1>5. The three conditions are equivalent.

::: {.proof}
Steps <1>2, <1>3, and <1>4 give the cycle
$$
(1)\Longrightarrow(2)\Longrightarrow(3)\Longrightarrow(1).
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required equivalence.
:::
:::
