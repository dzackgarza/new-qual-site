---
schema: qual/card@1
id: P-TRIV-DE31
kind: problem
title: Eigenvalues of $(xu')'=-\lambda u/x$ with mixed boundary conditions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the non-zero solutions of
$$
\left( xu'(x) \right)' = -\lambda\frac{u(x)}{x} \tag{39}
$$
such that $u(1) = 0$ and $u'(e) = 0$. What values of $\lambda$ are allowed?
:::

::: {.solution}

Set
$$
t=\log x,
\qquad
U(t)=u(e^t),
$$
so that $x\in[1,e]$ corresponds to $t\in[0,1]$.

::: pf

::: pf-step

The eigenvalue problem becomes
$$
U''+\lambda U=0,
\qquad
U(0)=0,
\qquad
U'(1)=0.
$$


::: pf-proof

Since $u'(x)=U'(t)/x$, one has $xu'(x)=U'(t)$ and therefore
$$
(xu')'=\frac1xU''(t).
$$
Multiplying the given equation by $x$ gives $U''=-\lambda U$.
Also, $u(1)=U(0)$, while $u'(e)=U'(1)/e$, so the second boundary condition is $U'(1)=0$.

:::

:::

::: {.pf-step #s1-2}

There is no nonzero solution for $\lambda\leq0$.


::: pf-proof

If $\lambda=0$, then $U=A+Bt$.
The condition $U(0)=0$ gives $A=0$, and $U'(1)=0$ gives $B=0$.
If $\lambda=-\mu^2<0$, then
$$
U=A\cosh(\mu t)+B\sinh(\mu t).
$$
The first condition gives $A=0$, and the second gives $B\mu\cosh\mu=0$, hence $B=0$.

:::

:::

::: {.pf-step #s1-3}

For $\lambda>0$, write $\lambda=\mu^2$.
A nonzero solution exists exactly when
$$
\cos\mu=0,
$$
that is,
$$
\mu=\left(n+\frac12\right)\pi,
\qquad n=0,1,2,\ldots.
$$


::: pf-proof

The general solution is
$$
U=A\cos(\mu t)+B\sin(\mu t).
$$
The condition $U(0)=0$ gives $A=0$.
Then
$$
U'(1)=B\mu\cos\mu,
$$
which vanishes for a nonzero solution exactly when $\cos\mu=0$.

:::

:::

::: {.pf-step #s1-4}

Hence the allowed values and corresponding nonzero solutions are
$$
\boxed{
\lambda_n=\left(n+\frac12\right)^2\pi^2,
\qquad
u_n(x)=C\sin\left(\left(n+\frac12\right)\pi\log x\right),
\quad n=0,1,2,\ldots,\ C\ne0.}
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $U_n(t)=C\sin((n+1/2)\pi t)$.
Substitute $t=\log x$.
Step [](#s1-2){.pf-ref} shows there are no additional eigenvalues.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives all nonzero solutions and all allowed values of $\lambda$.

:::

:::

:::
