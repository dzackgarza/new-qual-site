---
schema: qual/card@1
id: P-JHUFA08ANC
kind: problem
title: $\ell^\infty$ is not separable
classification:
  areas:
    - real-analysis
  topics:
    - Banach Spaces
    - Separability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, Fall 2008, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the retained exam file assets/attachments/JHU Years of Analysis
    Exams.pdf, problem 3 of "PROBLEMS FOR ANALYSIS QUALIFYING EXAM, Fall 2008" (page 34 of
    the collection): "Is the Banach space l-infinity of bounded complex sequences a =
    (a_n) with the supremum norm ... separable? Prove your assertion." The card's
    statement is that problem, with the norm written out.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the card's own argument into numbered steps; no retained solution set for
    the JHU exams covers it. The steps keep the characteristic-sequence family and the
    1/3-balls, and state the two counting facts the prose uses without naming them: that
    points at distance 1 give pairwise disjoint balls of radius 1/3, and that a separable
    space meets only countably many pairwise disjoint nonempty open sets.
---

::: {.problem}
Is the Banach space $\ell^\infty$ of bounded complex sequences, with the supremum norm, separable? Prove your answer.
:::

::: {.solution}

The problem is problem 3 of the JHU Analysis Qualifying Exam, Fall 2008, retained at
`assets/attachments/JHU Years of Analysis Exams.pdf` (p. 34 of the collection). No retained
solution set covers it; the argument below is the card's own, restructured as numbered steps.

For $A\subseteq\NN$ let $x^{A}\in\ell^{\infty}$ be its characteristic sequence,
$x^{A}_{n}=1$ for $n\in A$ and $x^{A}_{n}=0$ otherwise, and write
$\norm{x}_{\infty}=\sup_{n}\abs{x_{n}}$.

::: pf

::: {.pf-step #family}

$\norm{x^{A}}_{\infty}=1$ for every $A\subseteq\NN$.

::: pf-proof

Each entry of $x^{A}$ is $0$ or $1$, and at least one entry is $1$ — for instance, the entry
at any $n\in A$, or at any $n\notin A$ if $A=\emptyset$. So the supremum of the moduli of the
entries is $1$, and $x^{A}$ is bounded, hence in $\ell^{\infty}$.

:::

:::

::: {.pf-step #separated}

If $A\ne B$ then $\norm{x^{A}-x^{B}}_{\infty}=1$.

::: pf-proof

As $A\ne B$ there is $n$ in exactly one of them; at that $n$ one sequence has entry $1$ and
the other $0$, so $\abs{x^{A}_{n}-x^{B}_{n}}=1$. Every entry of the difference is $0$ or
$\pm1$ in modulus, so the supremum is $1$.

:::

:::

::: {.pf-step #balls}

The balls $B(x^{A},1/3)$, $A\subseteq\NN$, are nonempty, pairwise disjoint, and there are
uncountably many of them.

::: pf-proof

Each contains $x^{A}$, so is nonempty. If $A\ne B$ and some $y$ lay in both, the triangle
inequality would give $\norm{x^{A}-x^{B}}_{\infty}\le\norm{x^{A}-y}_{\infty}
+\norm{y-x^{B}}_{\infty}<1/3+1/3<1$, contradicting step [](#separated){.pf-ref}. The index set
$\mathcal{P}(\NN)$ is uncountable, and the assignment $A\mapsto x^{A}$ is injective by step
[](#separated){.pf-ref}, so there are uncountably many balls.

:::

:::

::: {.pf-step #separable-count}

A separable metric space has only countably many pairwise disjoint nonempty open sets.

::: pf-proof

Let $D$ be a countable dense set and let $\theset{U_{i}}_{i\in I}$ be pairwise disjoint nonempty
open sets. Each $U_{i}$ meets $D$, so choose $d_{i}\in U_{i}\cap D$; the $d_{i}$ are distinct
because the $U_{i}$ are disjoint, so $i\mapsto d_{i}$ is an injection of $I$ into the
countable set $D$.

:::

:::

::: {.pf-step #not-separable}

$\ell^{\infty}$ is not separable.

::: pf-proof

If it were, step [](#separable-count){.pf-ref} would make the family of step
[](#balls){.pf-ref} countable, and that family is uncountable. So no countable dense subset
exists.

:::

:::

:::

:::
