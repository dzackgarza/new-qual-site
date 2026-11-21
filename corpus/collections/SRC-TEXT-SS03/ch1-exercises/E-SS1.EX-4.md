---
schema: qual/card@1
id: E-SS1.EX-4
kind: problem
title: The complex numbers admit no ordered-field structure
classification:
  areas:
    - complex-analysis
  topics: [Complex Numbers, Ordered Fields]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the prose that was already there. Each step is the
      ordered-field axiom it uses: squares of nonzero elements are positive (both
      signs of the element handled, the negative case by transporting the
      inequality by (ii)), then 1 = 1^2 and -1 = i^2 are positive, and adding 1 to
      the second contradicts the first by trichotomy (i). The hint in the printed
      exercise asks for exactly the i case. Not checked: the book's own text of the
      exercise, which is not retained in this checkout; the statement is as
      transcribed on the card. No retained solution set covers this exercise (the
      collection's provenance is a Google Books record), so the argument is the
      card's own. No statement repair.
---

::: {.exercise}
Show that it is impossible to define a total ordering on $\CC$. In other words, one cannot find a relation $\succ$ between complex numbers so that:

(i) For any two complex numbers $z, w$, one and only one of the following is true: $z \succ w$, $w \succ z$ or $z = w$.

(ii) For all $z_1, z_2, z_3 \in \CC$ the relation $z_1 \succ z_2$ implies $z_1 + z_3 \succ z_2 + z_3$.

(iii) Moreover, for all $z_1, z_2, z_3 \in \CC$ with $z_3 \succ 0$, then $z_1 \succ z_2$ implies $z_1 z_3 \succ z_2 z_3$.

[Hint: First check if $i \succ 0$ is possible.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $\succ$ be a relation on $\CC$ satisfying (i)--(iii); the proof derives a contradiction.

::: pf

::: {.pf-step #twice}
$z\succ0$ implies $0\succ z$, and $0\succ z$ implies $z\succ0$.

::: pf-proof
Apply (ii) with $z_1=z$, $z_2=0$, $z_3=-z$: $z\succ0$ gives $z-z\succ0-z$, that is $0\succ-z$. Symmetrically, $0\succ z$ with the same choice of $z_3$ gives $-z\succ0$, and applying the first implication to the element $-z$ returns $0\succ z$, which is the second claim.
:::

:::

::: {.pf-step #squares}
$z^2\succ0$ for every $z\in\CC$ with $z\ne0$.

::: pf-proof
By trichotomy (i), $z\ne0$ leaves $z\succ0$ or $0\succ z$.

If $z\succ0$, apply (iii) with $z_1=z$, $z_2=0$, $z_3=z$: its hypothesis $z_3\succ0$ holds, so $z\cdot z\succ0\cdot z=0$.

If $0\succ z$, then $-z\succ0$ by step [](#twice){.pf-ref}, and (iii) with $z_1=0$, $z_2=z$, $z_3=-z$ gives $0\cdot(-z)\succ z\cdot(-z)$, that is $0\succ-z^2$. Adding $z^2$ to both sides by (ii) gives $z^2\succ0$.
:::

:::

::: {.pf-step #one}
$1\succ0$.

::: pf-proof
$1=1^2$ and $1\ne0$, so step [](#squares){.pf-ref} applies to $z=1$.
:::

:::

::: {.pf-step #minusone}
$0\succ1$.

::: pf-proof
$i\ne0$ and $i^2=-1$, so step [](#squares){.pf-ref} gives $-1\succ0$. Adding $1$ to both sides of $-1\succ0$ by (ii) gives $-1+1\succ0+1$, that is $0\succ1$.
:::

:::

::: {.pf-step}
No relation $\succ$ on $\CC$ satisfies (i)--(iii).

::: pf-proof
Steps [](#one){.pf-ref} and [](#minusone){.pf-ref} give both $1\succ0$ and $0\succ1$, while (i) says that for the pair $z=1$, $w=0$ one and only one of $1\succ0$, $0\succ1$, $1=0$ is true. So the assumption fails: $\CC$ carries no total ordering compatible with its addition and multiplication.
:::

:::

:::

:::
