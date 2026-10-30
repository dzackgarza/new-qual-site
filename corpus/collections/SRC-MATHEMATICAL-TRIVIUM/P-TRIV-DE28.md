---
schema: qual/card@1
id: P-TRIV-DE28
kind: problem
title: Series solution of Laguerre's equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated Laguerre's ODE from problem 27, against Differential Equations Problems 27-28 on pages 24-25 of the source PDF.
---

::: {.problem}
Develop a series solution for Laguerre's ODE (given in problem 27).

Problem 27 of the source gives Laguerre's ODE as $x y'' + (1 - x) y' + a y = 0$.
:::

::: {.solution}

Seek a power series
$$
y(x)=\sum_{n=0}^{\infty}c_nx^n.
$$

::: pf

::: {.pf-step #s1-1}

Substitution into Laguerre's equation gives the recurrence
$$
\boxed{c_{n+1}=\frac{n-a}{(n+1)^2}c_n}
\qquad(n\geq0).
$$


::: pf-proof

The derivatives are
$$
y'=\sum_{n=0}^{\infty}(n+1)c_{n+1}x^n,
\qquad
y''=\sum_{n=0}^{\infty}(n+2)(n+1)c_{n+2}x^n.
$$
Thus
$$
xy''+y'-xy'+ay=0.
$$
For each $n\geq0$, the coefficient of $x^n$ is
$$
(n+1)^2c_{n+1}+(a-n)c_n,
$$
which yields the recurrence.

:::

:::

::: {.pf-step #s1-2}

The coefficients are
$$
c_n=c_0\frac{(-a)_n}{(n!)^2},
$$
where
$$
(-a)_n=(-a)(1-a)\cdots(n-1-a)
$$
is the rising factorial.


::: pf-proof

Iterating step [](#s1-1){.pf-ref} gives
$$
c_n=c_0\prod_{j=0}^{n-1}\frac{j-a}{(j+1)^2}
=c_0\frac{(-a)_n}{(n!)^2}.
$$

:::

:::

::: {.pf-step #s1-3}

Hence the analytic series solution at $x=0$ is
$$
\boxed{
y(x)=c_0\sum_{n=0}^{\infty}
\frac{(-a)_n}{(n!)^2}x^n}.
$$


::: pf-proof

Insert the coefficients from step [](#s1-2){.pf-ref} into the power series. The ratio of consecutive absolute terms is asymptotic to $\abs{x}/n$, so the series converges for every finite $x$.

:::

:::

::: {.pf-step #s1-4}

If $a=N\in\NN_0$, the series terminates at degree $N$ and is proportional to the Laguerre polynomial
$$
L_N(x)=\sum_{n=0}^{N}(-1)^n\binom{N}{n}\frac{x^n}{n!}.
$$


::: pf-proof

For $a=N$, step [](#s1-1){.pf-ref} gives $c_{N+1}=0$, and every later coefficient is then zero. Moreover,
$$
\frac{(-N)_n}{(n!)^2}
=(-1)^n\frac{N!}{(N-n)!(n!)^2}
=(-1)^n\binom Nn\frac1{n!},
$$
which is the displayed polynomial after choosing $c_0=1$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} develop the requested series solution, and step [](#s1-4){.pf-ref} records its polynomial specialization.

:::

:::

:::
