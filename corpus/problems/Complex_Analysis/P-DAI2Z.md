---
schema: qual/card@1
id: P-DAI2Z
kind: problem
title: Number of solutions of $e^z=az^n$ in the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $n\in \ZZ^{\geq 0}$ and show that the equation
$$
e^z = az^n
$$
has $n$ solutions in the open unit disc if $\abs{a} > e$, and no solutions if $\abs{a} < {1\over e}$.
:::

::: {.solution}

Let $F(z)\coloneqq e^z-az^n$.

::: pf

::: {.pf-step #bounds}
On $\abs{z}=1$, $e^{-1}\le\abs{e^z}\le e$.

::: pf-proof
$\abs{e^z}=e^{\Re z}$ and $-1\le\Re z\le1$.
:::

:::

::: {.pf-step #large-count}
If $\abs{a}>e$, $F$ has exactly $n$ zeros in $\abs{z}<1$, counted with multiplicity.

::: pf-proof
On $\abs{z}=1$, step [](#bounds){.pf-ref} gives $\abs{e^z}\le e<\abs{a}=\abs{-az^n}$.
By Rouché's theorem $F$ has as many zeros in $\abs{z}<1$ as $-az^n$, which has the single zero $0$ of order $n$.
:::

:::

::: pf-step
If $\abs{a}>e$, the $n$ zeros of step [](#large-count){.pf-ref} are distinct, so the equation has exactly $n$ solutions in the disc.

::: pf-proof
At a common zero of $F$ and $F'$, $e^z=az^n$ and $e^z=naz^{n-1}$, so $az^{n-1}(z-n)=0$.
Here $a\ne0$, $z\ne0$ because $e^0\ne0$, and $z=n$ is not in the open disc when $n\ge1$; so every zero of $F$ in the disc is simple.
:::

:::

::: pf-step
If $\abs{a}<1/e$, the equation has no solutions in $\abs{z}<1$.

::: pf-proof
On $\abs{z}=1$, step [](#bounds){.pf-ref} gives $\abs{-az^n}=\abs{a}<e^{-1}\le\abs{e^z}$.
By Rouché's theorem $F$ has as many zeros in $\abs{z}<1$ as $e^z$, which has none.
:::

:::

:::

:::
