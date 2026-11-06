---
schema: qual/card@1
id: E-AMD-IDVVQWVQ
kind: problem
title: Every prime ideal is radical
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard exercise, no repair needed), and the existing prose solution against
    a fresh re-derivation — the inclusion p <= sqrt(p) is the case n = 1, and the
    reverse inclusion is induction on the exponent using that a product in a
    prime ideal has a factor in it; both directions are correct and the
    structured proof now isolates the induction and its two steps. Also checked:
    that the argument does not use the properness of p, so the closing sentence
    claims nothing it did not prove. No source solution is retained for this card
    (SRC-UNSORTED-ALGEBRA, a compilation with no provenance href), so no source
    comparison was made. What was not checked: any printed source.

---

::: {.exercise}
Show that every prime ideal is radical.
:::

::: {.solution}
Let $R$ be a commutative ring with $1$ and $\mathfrak p\trianglelefteq R$ a prime ideal: a proper ideal with the property that $xy\in\mathfrak p$ implies $x\in\mathfrak p$ or $y\in\mathfrak p$. The radical is $\sqrt{\mathfrak p}=\theset{x\in R:x^n\in\mathfrak p\text{ for some }n\geq1}$, and an ideal $I$ is radical when $\sqrt I=I$.

::: pf

::: {.pf-step #subset}
$\mathfrak p\subseteq\sqrt{\mathfrak p}$.

::: pf-proof
If $x\in\mathfrak p$ then $x^1=x\in\mathfrak p$, so $x\in\sqrt{\mathfrak p}$ by the definition of the radical.
:::

:::

::: {.pf-step #power}
For every $x\in R$ and every integer $n\geq1$, if $x^n\in\mathfrak p$ then $x\in\mathfrak p$.

::: pf-proof
We prove the statement for all $n\geq1$ by induction on $n$.

::: {.pf-step #base}
The statement holds for $n=1$.

::: pf-proof
For $n=1$ the hypothesis $x^1\in\mathfrak p$ is the conclusion $x\in\mathfrak p$.
:::

:::

::: {.pf-step #step}
If the statement holds for $n\geq1$, it holds for $n+1$.

::: pf-proof
Suppose $x^{n+1}\in\mathfrak p$. Since $x^{n+1}=x\cdot x^n$ and $\mathfrak p$ is prime, either $x\in\mathfrak p$, which is the conclusion, or $x^n\in\mathfrak p$, in which case $x\in\mathfrak p$ by the induction hypothesis.
:::

:::

Steps [](#base){.pf-ref} and [](#step){.pf-ref} give the statement for every $n\geq1$ by induction, and the induction is on a natural number, so it terminates after finitely many steps for each fixed $n$.
:::

:::

::: {.pf-step #superset}
$\sqrt{\mathfrak p}\subseteq\mathfrak p$.

::: pf-proof
Let $x\in\sqrt{\mathfrak p}$. By definition $x^n\in\mathfrak p$ for some integer $n\geq1$, and step [](#power){.pf-ref} then gives $x\in\mathfrak p$.
:::

:::

::: {.pf-step}
$\sqrt{\mathfrak p}=\mathfrak p$, that is, $\mathfrak p$ is radical.

::: pf-proof
Steps [](#subset){.pf-ref} and [](#superset){.pf-ref} give the two inclusions, hence equality. By definition an ideal equals its radical exactly when it is radical, so every prime ideal is radical. Neither inclusion used the properness of $\mathfrak p$: only the multiplicative property of primality entered, which is why the conclusion also holds for the unit ideal, whose radical is itself.
:::

:::

:::
:::
