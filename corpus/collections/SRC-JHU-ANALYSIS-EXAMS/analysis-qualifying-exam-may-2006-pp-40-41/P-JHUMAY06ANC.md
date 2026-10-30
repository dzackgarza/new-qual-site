---
schema: qual/card@1
id: P-JHUMAY06ANC
kind: problem
title: Entire functions bounded by $\abs{z}^{3/2}$ outside the unit disk
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
3. Find all entire functions $f$ such that $\abs{f(z)} \le \abs{z}^{3/2}$ whenever $\abs{z} \geq 1$. Give explicit formulas for the functions and give a proof for your answer. (An entire function is a holomorphic function on $\CC$.)
:::

::: {.solution}
The functions are precisely
$$
\boxed{f(z)=az+b,\qquad a,b\in\CC,\quad \abs{a}+\abs{b}\leq1.}
$$

::: pf

::: {.pf-step #every-solution-affine}
Every solution is affine.

::: pf-proof
Write the entire Taylor expansion as $f(z)=\sum_{k\geq0}c_kz^k$.
For each $R\geq1$, the hypothesis gives
$\max_{\abs{z}=R}\abs{f(z)}\leq R^{3/2}$. Cauchy's coefficient
estimate therefore yields
$$
\abs{c_k}\leq R^{3/2-k}
$$
[@SS03]. For every $k\geq2$, the right-hand side tends
to zero as $R\to\infty$, so $c_k=0$. Consequently
$f(z)=az+b$ for $a=c_1$ and $b=c_0$.
:::

:::

::: {.pf-step #unit-circle-bound}
The unit-circle bound is equivalent to $\abs{a}+\abs{b}\leq1$.

::: pf-proof
The triangle inequality gives $\abs{az+b}\leq\abs{a}+\abs{b}$ on
$\abs{z}=1$. Equality is attained: if $a$ and $b$ are nonzero,
take $z=(b/\abs{b})(\overline a/\abs{a})$, so $az$ and $b$
have the same argument. If either coefficient is zero,
every point of the circle attains the sum. Hence
$$
\max_{\abs{z}=1}\abs{az+b}=\abs{a}+\abs{b}.
$$
The given bound at $\abs{z}=1$ implies that this sum is at
most one.
:::

:::

::: pf-step
Every stated affine function obeys the original exterior bound.

::: pf-proof
If $r=\abs{z}\geq1$ and $\abs{a}+\abs{b}\leq1$, then
$$
\abs{az+b}\leq \abs{a}r+\abs{b}\leq r(\abs{a}+\abs{b})\leq r\leq r^{3/2}.
$$
Thus every displayed function satisfies the inequality
for every required $z$. Together with steps [](#every-solution-affine){.pf-ref} and
[](#unit-circle-bound){.pf-ref}, this proves the exhaustive classification.
:::

:::

:::
:::
