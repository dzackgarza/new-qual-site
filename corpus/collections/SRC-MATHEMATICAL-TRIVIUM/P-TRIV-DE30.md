---
schema: qual/card@1
id: P-TRIV-DE30
kind: problem
title: Eigenvalue problem for the Euler equation $x^2y''+3xy'+\lambda y=0$ on $[1,e]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 30, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the solutions of
$$
x^2y'' + 3xy' + \lambda y = 0 \tag{38}
$$
with $x \in [1, e]$ such that $y(1) = y(e) = 0$.
:::

::: {.solution}

Set
$$
t=\log x,
\qquad
Y(t)=y(e^t),
$$
so that $x\in[1,e]$ corresponds to $t\in[0,1]$.

::: pf

::: {.pf-step #s1-1}

The differential equation becomes
$$
Y''+2Y'+\lambda Y=0,
\qquad
Y(0)=Y(1)=0.
$$


::: pf-proof

Since
$$
y'(x)=\frac1xY'(t),
\qquad
y''(x)=\frac1{x^2}\bigl(Y''(t)-Y'(t)\bigr),
$$
one has
$$
x^2y''+3xy'=Y''-Y'+3Y'=Y''+2Y'.
$$
The boundary values follow from $t=\log x$.

:::

:::

::: {.pf-step #s1-2}

Writing
$$
Y(t)=e^{-t}Z(t)
$$
reduces the problem to
$$
Z''+(\lambda-1)Z=0,
\qquad
Z(0)=Z(1)=0.
$$


::: pf-proof

Differentiation gives
$$
Y'=e^{-t}(Z'-Z),
\qquad
Y''=e^{-t}(Z''-2Z'+Z).
$$
Substitution into step [](#s1-1){.pf-ref} yields
$$
e^{-t}\bigl(Z''+(\lambda-1)Z\bigr)=0.
$$
Because $e^{-t}$ is nonzero, the boundary conditions for $Y$ are equivalent to those for $Z$.

:::

:::

::: {.pf-step #s1-3}

A nonzero solution exists exactly for
$$
\boxed{\lambda_n=1+n^2\pi^2},
\qquad n=1,2,3,\ldots,
$$
and then
$$
Z_n(t)=C\sin(n\pi t).
$$


::: pf-proof

If $\lambda-1\leq0$, the elementary linear or hyperbolic solutions satisfying $Z(0)=0$ cannot also vanish at $t=1$ unless they are zero. If $\lambda-1=\mu^2>0$, then
$$
Z=A\cos(\mu t)+B\sin(\mu t).
$$
The condition $Z(0)=0$ gives $A=0$, while $Z(1)=0$ permits $B\ne0$ exactly when $\sin\mu=0$, i.e. $\mu=n\pi$ for $n\geq1$.

:::

:::

::: {.pf-step #s1-4}

Returning to $x$, all nonzero solutions are
$$
\boxed{
y_n(x)=\frac{C}{x}\sin(n\pi\log x),
\qquad
\lambda_n=1+n^2\pi^2,
\qquad n=1,2,3,\ldots,\ C\ne0.}
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
Y_n(t)=Ce^{-t}\sin(n\pi t).
$$
Substitute $t=\log x$ and $e^{-t}=1/x$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} lists every eigenvalue and corresponding nonzero solution satisfying the two boundary conditions.

:::

:::

:::
