---
schema: qual/card@1
id: P-TRIV-RA54
kind: problem
title: $\sum_{n\ge1}\frac{x^{n-1}}{n(n+1)}$
classification:
  areas: [real-analysis]
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 54, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the sum $\sum_{n=1}^{\infty} \frac{x^{n-1}}{n(n+1)}$ for all possible values of $x$.
:::

::: {.solution}

Define
$$
S(x)
=
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n(n+1)}.
$$

::: pf

::: {.pf-step #s1-1}

The series converges absolutely for
$$
\abs{x}\leq1.
$$


::: pf-proof

If $\abs{x}\leq1$, then
$$
\abs{
\frac{x^{n-1}}{n(n+1)}
}
\leq
\frac1{n(n+1)}.
$$
The comparison series converges, since
$$
\frac1{n(n+1)}
=
\frac1n-\frac1{n+1}
$$
telescopes.

:::

:::

::: {.pf-step #s1-2}

If
$$
\abs{x}>1,
$$
the series diverges.


::: pf-proof

The term magnitudes are
$$
\frac{\abs{x}^{n-1}}{n(n+1)}.
$$
Exponential growth dominates the quadratic denominator, so these terms do not tend to $0$.

:::

:::

::: {.pf-step #s1-3}

Therefore the complete convergence set is
$$
\boxed{\abs{x}\leq1}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For every $n\geq1$,
$$
\frac1{n(n+1)}
=
\frac1n-\frac1{n+1}.
$$


::: pf-proof

Combine the two fractions on the right over the common denominator $n(n+1)$.

:::

:::

::: {.pf-step #s1-5}

For $\abs{x}<1$ and $x\neq0$,
$$
S(x)
=
\sum_{n=1}^{\infty}
\frac{x^{n-1}}n
-
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}.
$$


::: pf-proof

Use step [](#s1-4){.pf-ref} term by term.
Absolute convergence permits splitting the series.

:::

:::

::: {.pf-step #s1-6}

The first sum in step [](#s1-5){.pf-ref} is
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}n
=
-\frac{\log(1-x)}x.
$$


::: pf-proof

For $\abs{x}<1$,
$$
-\log(1-x)
=
\sum_{n=1}^{\infty}\frac{x^n}{n}.
$$
Divide by $x$.

:::

:::

::: {.pf-step #s1-7}

The second sum in step [](#s1-5){.pf-ref} is
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}
=
\frac{-\log(1-x)-x}{x^2}.
$$


::: pf-proof

Set $m=n+1$:
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}
=
\frac1{x^2}
\sum_{m=2}^{\infty}
\frac{x^m}{m}.
$$
Now
$$
\sum_{m=2}^{\infty}\frac{x^m}{m}
=
-\log(1-x)-x.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore, for $\abs{x}<1$ and $x\neq0$,
$$
\boxed{
S(x)
=
\frac{x+(1-x)\log(1-x)}{x^2}.
}
$$


::: pf-proof

Substitute steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} into step [](#s1-5){.pf-ref} and combine over the denominator $x^2$.

:::

:::

::: {.pf-step #s1-9}

At $x=0$,
$$
\boxed{S(0)=\frac12}.
$$


::: pf-proof

In the original series, every term with $n\geq2$ contains a positive power of $x$ and vanishes at $x=0$.
The $n=1$ term is
$$
\frac1{1\cdot2}.
$$
The formula in step [](#s1-8){.pf-ref} has the same removable limit.

:::

:::

::: {.pf-step #s1-10}

At $x=1$,
$$
\boxed{S(1)=1}.
$$


::: pf-proof

The series becomes
$$
\sum_{n=1}^{\infty}
\frac1{n(n+1)}
=
\sum_{n=1}^{\infty}
\left(
\frac1n-\frac1{n+1}
\right),
$$
which telescopes to $1$.

:::

:::

::: {.pf-step #s1-11}

At $x=-1$,
$$
\boxed{S(-1)=2\log2-1}.
$$


::: pf-proof

Because the series converges absolutely at $x=-1$, its value equals the continuous boundary limit of the power-series expression in step [](#s1-8){.pf-ref}. Thus
$$
S(-1)
=
-1+2\log2.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the full convergence set, and steps [](#s1-8){.pf-ref} through [](#s1-11){.pf-ref} give the sum at every point of that set.

:::

:::

:::
