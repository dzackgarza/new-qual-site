---
schema: qual/card@1
id: P-UCLAB14S-09
kind: problem
title: Minimizing Dirichlet energy with fixed endpoints
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Find a function that minimizes
$$
\int_0^1 \abs{f'(x)}^2\,dx
$$
among all $f\in C^1(\RR)$ such that $f(0)=0$ and $f(1)=1$.
Is the minimizing $C^1$ function unique on $[0,1]$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every admissible $f$,
$$
1=f(1)-f(0)=\int_0^1f'(x)\,dx.
$$


::: pf-proof

Since $f\in C^1(\RR)$, the fundamental theorem of calculus gives
$$
f(1)-f(0)=\int_0^1f'(x)\,dx.
$$
The endpoint conditions make the left side equal to $1$.

:::

:::

::: {.pf-step #s1-2}

Cauchy--Schwarz gives
$$
1\leq\int_0^1\abs{f'(x)}^2\,dx.
$$


::: pf-proof

Apply Cauchy--Schwarz to $f'$ and the constant function $1$:
$$
\abs{\int_0^1f'(x)\,dx}^2
\leq
\left(\int_0^1\abs{f'(x)}^2\,dx\right)
\left(\int_0^1 1^2\,dx\right).
$$
The first factor on the left is $1$ by step [](#s1-1){.pf-ref}, and the final integral is $1$.

:::

:::

::: {.pf-step #s1-3}

The function
$$
f_0(x)=x
$$
is admissible and has energy
$$
\int_0^1\abs{f_0'(x)}^2\,dx=1.
$$


::: pf-proof

The function is $C^1(\RR)$, satisfies $f_0(0)=0$ and $f_0(1)=1$, and has derivative identically equal to $1$.

:::

:::

::: {.pf-step #s1-4}

Therefore the minimum energy is $1$, attained by $f_0(x)=x$.


::: pf-proof

Step [](#s1-2){.pf-ref} gives the lower bound $1$ for every admissible function, and step [](#s1-3){.pf-ref} exhibits an admissible function attaining it.

:::

:::

::: pf-step

If an admissible $f$ is a minimizer, then equality holds in the Cauchy--Schwarz inequality of step [](#s1-2){.pf-ref}.


::: pf-proof

By step [](#s1-4){.pf-ref}, a minimizer has energy exactly $1$. Thus the inequality in step [](#s1-2){.pf-ref} is an equality.

:::

:::

::: pf-step

Equality in Cauchy--Schwarz implies that $f'$ is a constant function on $[0,1]$.


::: pf-proof

Equality in Cauchy--Schwarz for the functions $f'$ and $1$ occurs exactly when they are linearly dependent in $L^2([0,1])$. Thus $f'=c$ almost everywhere for some constant $c$. Since $f'$ is continuous, it follows that $f'(x)=c$ for every $x\in[0,1]$.

:::

:::

::: {.pf-step #s1-7}

The endpoint conditions force this constant to be $1$ and hence
$$
f(x)=x
\qquad(0\leq x\leq1).
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives
$$
1=\int_0^1c\,dx=c.
$$
Thus $f'=1$ on $[0,1]$. Since $f(0)=0$, integration gives $f(x)=x$ there.

:::

:::

::: {.pf-step #s1-8}

Consequently the minimizing function is unique on $[0,1]$:
$$
\boxed{f(x)=x.}
$$


::: pf-proof

Every minimizer must equal $x$ on $[0,1]$ by step [](#s1-7){.pf-ref}, while step [](#s1-3){.pf-ref} shows this function is a minimizer.

:::

:::

::: pf-step

The extension outside $[0,1]$ is not unique.


::: pf-proof

The functional and endpoint constraints depend only on the restriction to $[0,1]$. Any $C^1$ extension of the function $x$ from $[0,1]$ to all of $\RR$ remains a minimizer. The question asks uniqueness on $[0,1]$, where step [](#s1-8){.pf-ref} proves uniqueness.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref} give the minimum and the requested uniqueness statement.

:::

:::

:::
