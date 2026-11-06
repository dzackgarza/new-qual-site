---
schema: qual/card@1
id: E-AMD-JGCVGZJE
kind: problem
title: $\units{R}$ need not be closed under addition
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the verbose counterexample by the universal nonzero-ring obstruction.
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (asks
    for a demonstration that closure fails, no repair needed), and the existing prose
    against a fresh re-derivation: 1 and -1 are units since each is its own inverse
    ((-1)(-1) = 1); 0 is not a unit in a nonzero ring, since 0*v = 0 != 1; so
    1 + (-1) = 0 is a sum of units that is not a unit; and in Z the units are exactly
    +-1, whose sums -2, 0, 2 are not units. Correct. The prose asserted that 0 is not
    a unit and that the units of Z are +-1; the proof gives both with their reasons,
    including that 1 = 0 forces the ring to be zero. No source solution is retained
    for this card, so no source comparison was made. What was not checked: any
    printed source.
---

::: {.exercise}
Show that $R^\times$ need not be closed under addition.
:::

::: {.solution}
Let $R$ be a ring with $1$ and $R^\times$ its group of units, the elements having a two-sided inverse.

::: pf

::: {.pf-step #units}
$1\in R^\times$ and $-1\in R^\times$.

::: pf-proof
$1\cdot1=1$, so $1$ is its own inverse. And $(-1)(-1)=1$ in any ring, because $(-1)(-1)=-(1\cdot(-1))=-(-1)=1$; so $-1$ is its own inverse. Both are therefore units.
:::

:::

::: {.pf-step #zero}
$0\notin R^\times$ whenever $R\neq0$.

::: pf-proof
If $0$ had an inverse $v$, then $1=0\cdot v=0$; so $1=0$ in $R$, which forces $R=0$ because every element $r$ satisfies $r=r\cdot1=r\cdot0=0$. Since $R\neq0$, $0$ is not a unit.
:::

:::

::: {.pf-step #not-closed}
$R^\times$ is not closed under addition.

::: pf-proof
By steps [](#units){.pf-ref} and [](#zero){.pf-ref}, $1$ and $-1$ are units whose sum $1+(-1)=0$ is not, in a nonzero ring $R$. So there are elements of $R^\times$ whose sum is outside $R^\times$, which is exactly the failure of closure under addition.
:::

:::

::: {.pf-step #example}
In $R=\ZZ$ the units are $\pm1$, and no sum of two units is a unit.

::: pf-proof
An integer $m$ is a unit exactly when $mn=1$ for some $n\in\ZZ$, which forces $m=\pm1$. The sums of two elements of $\{\pm1\}$ are $-2$, $0$ and $2$, and none of these is $\pm1$; by the same criterion none is a unit. So $\ZZ$ is a concrete instance of a ring whose units are not closed under addition.
:::

:::

:::
:::
