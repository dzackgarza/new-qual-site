---
schema: qual/card@1
id: E-5NREC
kind: problem
title: Images of locally compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 3, printed p. 186; the two questions
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.3, PDF p. 22. The identity from the discrete
    rationals to the usual rationals is continuous with image not locally compact; a
    continuous open map does carry local compactness, images of compact neighbourhoods being
    compact neighbourhoods. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the counterexample (the identity from the
    discrete rationals, locally compact, onto the usual rationals, not locally compact) and
    the positive result (a compact neighbourhood in X maps to a compact set containing an
    open neighbourhood in f(X) when f is open), with Theorem 29.2. positron0802, Chapter 3
    Exercise 29.3, PDF p. 22. The printed statement needed no repair.
---

::: {.exercise}

Let $X$ be a locally compact space.
If $f: X \to Y$ is continuous, does it follow that $f(X)$ is locally compact?
What if $f$ is both continuous and open?
Justify your answer.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.3, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves and the counterexample are theirs.

::: pf

::: {.pf-step #continuous-not-enough}
A continuous image of a locally compact space need not be locally compact.

::: pf-proof
Let $\QQ_{d}$ be the rationals with the discrete topology and $\QQ$ the rationals with the usual topology; the identity $i:\QQ_{d}\to\QQ$ is continuous, since every subset of $\QQ_{d}$ is open. The discrete space $\QQ_{d}$ is locally compact: for $x\in\QQ_{d}$ the singleton $\{x\}$ is open, and it is compact because its only open cover is $\{\{x\}\}$ together with sets containing $x$. But $i(\QQ_{d})=\QQ$ is not locally compact in the usual topology (Munkres §29 Exercise 1).
:::

:::

::: {.pf-step #open-suffices}
If $f:X\to Y$ is continuous and open and $X$ is locally compact, then $f(X)$ is locally compact.

::: pf-proof
Let $y\in f(X)$, say $y=f(x)$. Since $X$ is locally compact there is a compact subspace $C\subset X$ containing a neighbourhood $U$ of $x$ (Theorem 29.2). Then $f(C)$ is compact, being a continuous image of a compact space, and it is a subspace of $f(X)$; and $f(U)$ is a neighbourhood of $y$ in $f(X)$, because $U$ is open and contains $x$ and $f$ is an open map onto its image, with $f(U)\subset f(C)$. So every point of $f(X)$ has a compact subspace containing a neighbourhood of it, and $f(X)$ is locally compact.
:::

:::

::: {.pf-step}
The two answers hold.

::: pf-proof
Steps [](#continuous-not-enough){.pf-ref} and [](#open-suffices){.pf-ref} answer the two questions.
:::

:::

:::
:::
