---
schema: qual/card@1
id: P-TRIV-RA28
kind: problem
title: Convergence of $\int\frac{dx}{x^\alpha\log^\beta x}$ on $(0,1)$ and $(1,\infty)$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
For what values of $\alpha$ and $\beta$ the following integrals are convergent?

(a) $\int_0^1 \frac{dx}{x^\alpha\log^\beta x}$, (b) $\int_1^{\infty} \frac{dx}{x^\alpha\log^\beta x}$.
:::

::: {.remark}
For arbitrary real $\beta$, the expression $(\log x)^\beta$ is generally not
real-valued on $0<x<1$. The intended real convergence problem is interpreted
as using $\abs{\log x}^\beta=(-\log x)^\beta$ in part (a). This interpretation
also makes the endpoint singularity at $x=1$ explicit.
:::

::: {.solution}

::: pf

::: pf-step

In part (a), set
$$
t=-\log x.
$$
Then
$$
x=e^{-t},
\qquad
dx=-e^{-t}\,dt,
$$
and
$$
\abs{\log x}=t.
$$


::: pf-proof

These identities follow directly from the substitution $t=-\log x$.

:::

:::

::: {.pf-step #s1-2}

The integral in part (a) becomes
$$
\int_0^\infty
e^{(\alpha-1)t}t^{-\beta}
\,dt.
$$


::: pf-proof

As $x$ runs from $0$ to $1$, $t$ runs from $\infty$ to $0$. Also
$$
x^{-\alpha}dx
=
e^{\alpha t}(-e^{-t}dt)
=
-e^{(\alpha-1)t}dt.
$$
Reversing the endpoints gives the displayed integral.

:::

:::

::: {.pf-step #s1-3}

Near $t=0$, the integral in step [](#s1-2){.pf-ref} converges exactly when
$$
\beta<1.
$$


::: pf-proof

The exponential factor tends to $1$ as $t\to0^+$. Thus the local behavior is
that of
$$
\int_0^1 t^{-\beta}\,dt,
$$
which converges exactly for $-\beta>-1$, equivalently $\beta<1$.

:::

:::

::: {.pf-step #s1-4}

As $t\to\infty$, the integral in step [](#s1-2){.pf-ref} converges if
$$
\alpha<1,
$$
diverges if
$$
\alpha>1,
$$
and for $\alpha=1$ converges exactly when $\beta>1$.


::: pf-proof

If $\alpha<1$, the exponential factor decays like
$$
e^{-(1-\alpha)t},
$$
which dominates any power of $t$. If $\alpha>1$, the exponential grows and
the integrand cannot be integrable at infinity. If $\alpha=1$, the integrand
is $t^{-\beta}$, whose integral over $[1,\infty)$ converges exactly for
$\beta>1$.

:::

:::

::: {.pf-step #s1-5}

Therefore part (a) converges exactly when
$$
\boxed{\alpha<1\quad\text{and}\quad\beta<1.}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} requires $\beta<1$. Under that condition, the exceptional case
$\alpha=1$ from step [](#s1-4){.pf-ref} would require the incompatible condition
$\beta>1$. Hence the only possible convergence regime is $\alpha<1$ together
with $\beta<1$, and steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show this regime is sufficient.

:::

:::

::: pf-step

In part (b), set
$$
t=\log x.
$$
Then
$$
x=e^t,
\qquad
dx=e^t\,dt.
$$


::: pf-proof

These are the standard relations for the logarithmic substitution.

:::

:::

::: {.pf-step #s1-7}

The integral in part (b) becomes
$$
\int_0^\infty
e^{(1-\alpha)t}t^{-\beta}
\,dt.
$$


::: pf-proof

Now
$$
x^{-\alpha}dx
=
e^{-\alpha t}e^t\,dt
=
e^{(1-\alpha)t}\,dt,
$$
and $\log x=t$.

:::

:::

::: {.pf-step #s1-8}

Near $t=0$, convergence again requires
$$
\beta<1.
$$


::: pf-proof

As in step [](#s1-3){.pf-ref}, the exponential tends to $1$, so the behavior is
$t^{-\beta}$.

:::

:::

::: {.pf-step #s1-9}

As $t\to\infty$, the integral in step [](#s1-7){.pf-ref} converges if
$$
\alpha>1,
$$
diverges if
$$
\alpha<1,
$$
and for $\alpha=1$ converges exactly when $\beta>1$.


::: pf-proof

This is the same argument as step [](#s1-4){.pf-ref} with the exponential sign reversed.

:::

:::

::: {.pf-step #s1-10}

Therefore part (b) converges exactly when
$$
\boxed{\alpha>1\quad\text{and}\quad\beta<1.}
$$


::: pf-proof

Step [](#s1-8){.pf-ref} requires $\beta<1$. The borderline case $\alpha=1$ from step
[](#s1-9){.pf-ref} requires $\beta>1$, so it cannot satisfy the endpoint condition at
$x=1$. Hence only $\alpha>1$, $\beta<1$ remains, and it is sufficient by
steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-10){.pf-ref} give the complete convergence regions for parts (a) and
(b), respectively.

:::

:::

:::
