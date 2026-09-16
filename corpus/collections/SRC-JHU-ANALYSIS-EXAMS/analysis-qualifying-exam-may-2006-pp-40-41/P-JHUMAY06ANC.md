---
schema: qual/card@1
id: P-JHUMAY06ANC
kind: problem
title: Entire functions bounded by $|z|^{3/2}$ outside the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked May 2006 problem 3 on PDF page 40, including the coefficient-one bound for every modulus at least one."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved the affine reduction, the necessary coefficient sum bound on the unit circle and its sufficiency on the full exterior region, including zero coefficients."
---

::: {.problem}
3. Find all entire functions f such that $| f ( z ) | \le | z | ^ { 3 / 2 }$ whenever $| z | \geq 1$ . Give explicit formulas for the functions and give a proof for your answer.
   (An entire function is a holomorphic function on C.)
:::

::: solution
The functions are precisely
$$
\boxed{f(z)=az+b,\qquad a,b\in\mathbb C,\quad |a|+|b|\leq1.}
$$

<1>1. Every solution is affine.
::: proof
Write the entire Taylor expansion as $f(z)=\sum_{k\geq0}c_kz^k$.
For each $R\geq1$, the hypothesis gives
$\max_{|z|=R}|f(z)|\leq R^{3/2}$. Cauchy's coefficient
estimate therefore yields
$$
|c_k|\leq R^{3/2-k}
$$
[@SS03]. For every $k\geq2$, the right-hand side tends
to zero as $R\to\infty$, so $c_k=0$. Consequently
$f(z)=az+b$ for $a=c_1$ and $b=c_0$.
:::

<1>2. The unit-circle bound is equivalent to $|a|+|b|\leq1$.
::: proof
The triangle inequality gives $|az+b|\leq|a|+|b|$ on
$|z|=1$. Equality is attained: if $a$ and $b$ are nonzero,
take $z=(b/|b|)(\overline a/|a|)$, so $az$ and $b$
have the same argument. If either coefficient is zero,
every point of the circle attains the sum. Hence
$$
\max_{|z|=1}|az+b|=|a|+|b|.
$$
The given bound at $|z|=1$ implies that this sum is at
most one.
:::

<1>3. Every stated affine function obeys the original exterior bound.
::: proof
If $r=|z|\geq1$ and $|a|+|b|\leq1$, then
$$
|az+b|\leq |a|r+|b|\leq r(|a|+|b|)\leq r\leq r^{3/2}.
$$
Thus every displayed function satisfies the inequality
for every required $z$. Together with steps <1>1 and
<1>2, this proves the exhaustive classification.
:::
:::
