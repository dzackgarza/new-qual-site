---
schema: qual/card@1
id: P-P6D6X
kind: problem
title: $f_n\to f$ almost everywhere in $L^1$ with $\int\abs{f_n}\to\int\abs{f}$ implies $\int f_n\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Fatou
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked it: g_n = |f_n| + |f| - |f_n - f| is nonnegative
    by the triangle inequality and tends to 2|f| almost everywhere; Fatou gives 2 int|f| <=
    liminf int g_n; the expansion of int g_n and the convergence of int|f_n| let the liminf be
    computed as 2 int|f| - limsup int|f_n - f|, so that limsup is at most 0 and the L1 distance
    tends to 0; the conclusion follows from |int f_n - int f| <= int|f_n - f|. Added the step
    that pulls a convergent term out of the liminf, which the prose performed silently. The
    statement is true as printed and no dominated-convergence hypothesis is needed.
---


::: {.problem}
Suppose that

- $f_n,f\in L^1$,
- $f_n\to f$ almost everywhere, and
- $\int \abs{f_n}\to\int \abs{f}$.

Show that $\int f_n\to\int f$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Put $g_n\coloneqq\abs{f_n}+\abs{f}-\abs{f_n-f}$.

::: pf

::: {.pf-step #nonnegative}
$g_n\ge0$ and $g_n\to2\abs{f}$ almost everywhere.

::: pf-proof
The triangle inequality gives $\abs{f_n-f}\le\abs{f_n}+\abs{f}$, so $g_n\ge0$. Since $f_n\to f$ almost everywhere and $w\mapsto\abs{w}$ is continuous, $\abs{f_n-f}\to0$ and $\abs{f_n}\to\abs{f}$ almost everywhere, whence $g_n\to2\abs{f}$ almost everywhere.
:::

:::

::: {.pf-step #fatou}
$2\int\abs{f}\le\liminf_{n}\int g_n$.

::: pf-proof
Each $g_n$ is measurable and nonnegative, and $g_n\to2\abs{f}$ almost everywhere, so Fatou's lemma gives $\int 2\abs{f}\le\liminf_n\int g_n$.
:::

:::

::: {.pf-step #expansion}
$\int g_n=\int\abs{f_n}+\int\abs{f}-\int\abs{f_n-f}$.

::: pf-proof
$\abs{f_n}$ and $\abs{f}$ are integrable by hypothesis and $\abs{f_n-f}$ is integrable, so all three integrals are finite and additivity and linearity of the integral apply.
:::

:::

::: {.pf-step #l1}
$\displaystyle\int\abs{f_n-f}\longrightarrow0$.

::: pf-proof
By steps [](#fatou){.pf-ref} and [](#expansion){.pf-ref},
$$
2\int\abs{f}\le\liminf_n\left(\int\abs{f_n}+\int\abs{f}-\int\abs{f_n-f}\right).
$$
The sequence $\int\abs{f_n}$ converges to $\int\abs{f}$ by hypothesis, so its limit may be pulled out of the $\liminf$: $\liminf_n(\int\abs{f_n}+\int\abs{f}-\int\abs{f_n-f})=2\int\abs{f}-\limsup_n\int\abs{f_n-f}$. Combining, $\limsup_n\int\abs{f_n-f}\le0$, and as the integrals are nonnegative the limit exists and equals $0$.
:::

:::

::: {.pf-step}
$\displaystyle\int f_n\longrightarrow\int f$.

::: pf-proof
$\abs{\int f_n-\int f}=\abs{\int(f_n-f)}\le\int\abs{f_n-f}$, which tends to $0$ by step [](#l1){.pf-ref}; hence the integrals converge, that is $\boxed{\int f_n\to\int f}$.
:::

:::

:::
:::
