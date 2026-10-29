---
schema: qual/card@1
id: P-TRIV-DE29
kind: problem
title: Neumann eigenvalue problem for $y''+\lambda y=0$ on $[0,\pi]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 29, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the solutions of:

$$
y ^ { \prime \prime } + \lambda y = 0\tag{37}
$$

with $y ^ { \prime } ( 0 ) = y ^ { \prime } ( \pi ) = 0 ;$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There is no nonzero solution when $\lambda<0$.


::: pf-proof

Write $\lambda=-\mu^2$ with $\mu>0$. Then
$$
y=A\cosh(\mu x)+B\sinh(\mu x),
$$
so
$$
y'=\mu A\sinh(\mu x)+\mu B\cosh(\mu x).
$$
The condition $y'(0)=0$ gives $B=0$, and then $y'(\pi)=\mu A\sinh(\mu\pi)=0$ gives $A=0$.

:::

:::

::: {.pf-step #s1-2}

When $\lambda=0$, the nonzero solutions are the constant functions
$$
\boxed{y(x)=A},\qquad A\ne0.
$$


::: pf-proof

The equation is $y''=0$, so $y=A+Bx$. Both boundary conditions reduce to $B=0$.

:::

:::

::: {.pf-step #s1-3}

If $\lambda>0$, write $\lambda=\mu^2$. A nonzero solution exists exactly when
$$
\mu=n\in\NN,
$$
and then
$$
\boxed{y(x)=A\cos(nx)}.
$$


::: pf-proof

For $\mu>0$,
$$
y=A\cos(\mu x)+B\sin(\mu x),
\qquad
y'=-\mu A\sin(\mu x)+\mu B\cos(\mu x).
$$
The condition $y'(0)=0$ gives $B=0$. The second condition becomes
$$
-\mu A\sin(\mu\pi)=0.
$$
For a nonzero solution $A\ne0$, so $\sin(\mu\pi)=0$, equivalently $\mu=n\in\NN$.

:::

:::

::: {.pf-step #s1-4}

Thus all eigenvalues and corresponding nonzero solutions are
$$
\boxed{\lambda_n=n^2,\qquad y_n(x)=A\cos(nx),\qquad n=0,1,2,\ldots,\ A\ne0}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} excludes negative eigenvalues, step [](#s1-2){.pf-ref} supplies $n=0$, and step [](#s1-3){.pf-ref} supplies every positive integer $n$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} lists every nonzero solution satisfying both Neumann boundary conditions.

:::

:::

:::
