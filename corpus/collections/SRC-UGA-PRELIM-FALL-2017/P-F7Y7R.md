---
schema: qual/card@1
id: P-F7Y7R
kind: problem
title: Negation of two quantified statements
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
relations: []
review: draft
audit:
- event: solution-written
  by: dzackgarza
  date: 2026-08-27
  note: written with the restored problem statement, replacing an imported one
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's two answers into numbered steps, with the quantifier rule written out as
    the justification of each. Checked: the shape of the negations, and that the second uses the
    pointwise rather than the uniform definition of continuity. Not checked against a printed
    source: the UGA preliminary examinations are not retained in tmp/sources and the card records
    no page.
---

::: {.problem}
Negate the following statements without using the word “not.”

(a) For every real number $x$, there is a real number $y$ such that $\abs{x-y}\geq2017$.

(b) The function $f:\RR\to\RR$ is continuous.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $\RR$ is the real line with its usual absolute value and continuity of $f:\RR\to\RR$ is the pointwise $\varepsilon$-$\delta$ condition at every point; a negation of $\forall x\,\exists y\,P$ is $\exists x\,\forall y\,\neg P$.

::: pf

::: {.pf-step #a}

The negation of (a) is: there is $x\in\RR$ such that $\abs{x-y}<2017$ for every $y\in\RR$.

::: pf-proof

The statement is $\forall x\in\RR\,\exists y\in\RR\,\abs{x-y}\geq2017$; negating gives $\exists x\in\RR\,\forall y\in\RR\,\abs{x-y}<2017$, and $<$ is the negation of $\geq$ on $\RR$.

:::

:::

::: {.pf-step #cont}

Continuity of $f$ is: $\forall x\,\forall\varepsilon>0\,\exists\delta>0\,\forall y\,(\abs{x-y}<\delta\Rightarrow\abs{f(x)-f(y)}<\varepsilon)$.

::: pf-proof

This is the $\varepsilon$-$\delta$ definition of continuity at each point $x$, with the variable $y$ in place of the usual $x'$.

:::

:::

::: {.pf-step #b}

The negation of (b) is: there are $x\in\RR$ and $\varepsilon>0$ such that for every $\delta>0$ there is $y\in\RR$ with $\abs{x-y}<\delta$ and $\abs{f(x)-f(y)}\geq\varepsilon$.

::: pf-proof

Negate the quantifier string of step [](#cont){.pf-ref} left to right: $\forall x$ becomes $\exists x$, $\forall\varepsilon>0$ becomes $\exists\varepsilon>0$, $\exists\delta>0$ becomes $\forall\delta>0$, $\forall y$ becomes $\exists y$; and the implication $P\Rightarrow Q$ has negation $P$ and not $Q$, that is $\abs{x-y}<\delta$ and $\abs{f(x)-f(y)}\geq\varepsilon$.

:::

:::

:::

:::
