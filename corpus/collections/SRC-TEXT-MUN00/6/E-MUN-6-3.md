---
schema: qual/card@1
id: E-MUN-6-3
kind: problem
title: Binary sequences are in bijection with a proper subset
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 3, printed p. 44; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.3,
    printed p. 76 (tmp/sources/munkres-solutions-whitman.pdf). He uses the same proper
    subset, the sequences beginning with 0, and the map that shifts the input one place
    to the right behind a leading 0; the card writes that map and its inverse and checks
    both composites. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed answer into numbered steps: the proper subset, the two maps and their
    well-definedness, and the two composites computed on an arbitrary sequence. The mathematics is
    the earlier reading's and no defect was found in it. Not re-read this session: the Whitman page
    and Munkres printed p. 44.
---

::: {.exercise}

Let $X$ be the two-element set $\{0,1\}$ . Find a bijective correspondence between $X^{\omega}$ and a proper subset of itself.
:::

::: {.solution}

The proper subset and the one-place shift behind a leading $0$ are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.3** (`tmp/sources/munkres-solutions-whitman.pdf`); the maps are written out below together with both composites.

Let $X=\{0,1\}$ and let $X^{\omega}$ be the set of sequences $x=(x_{1},x_{2},\dots)$ with $x_{i}\in X$.

::: pf

::: {.pf-step #proper}
$P\coloneqq\{(y_{1},y_{2},\dots)\in X^{\omega}\mid y_{1}=0\}$ is a proper subset of $X^{\omega}$.

::: pf-proof
$P\subset X^{\omega}$ by definition, and the sequence $(1,0,0,\dots)$ lies in $X^{\omega}$ but has first term $1\neq0$, so it is not in $P$.
:::

:::

::: {.pf-step #F}
The formula $F(x_{1},x_{2},\dots)=(0,x_{1},x_{2},\dots)$ defines a map $F\colon X^{\omega}\to P$.

::: pf-proof
For $x\in X^{\omega}$ the sequence $F(x)$ has first term $0\in X$ and all its other terms equal to terms of $x$, hence in $X$; so $F(x)\in X^{\omega}$, and its first term is $0$, so $F(x)\in P$.
:::

:::

::: {.pf-step #G}
The formula $G(y_{1},y_{2},y_{3},\dots)=(y_{2},y_{3},\dots)$ defines a map $G\colon P\to X^{\omega}$.

::: pf-proof
For $y\in P$ the sequence $G(y)$ consists of terms of $y$ with indices shifted by one, all in $X$, so $G(y)\in X^{\omega}$. The definition uses only the terms $y_{2},y_{3},\dots$ of $y$, and the condition $y_{1}=0$ is used only to know that $y$ belongs to the domain $P$.
:::

:::

::: {.pf-step #composites}
$G\circ F=\mathrm{id}_{X^{\omega}}$ and $F\circ G=\mathrm{id}_{P}$.

::: pf-proof
For $x=(x_{1},x_{2},\dots)$, $F(x)=(0,x_{1},x_{2},\dots)$ and $G(F(x))=(x_{1},x_{2},\dots)=x$. For $y=(0,y_{2},y_{3},\dots)\in P$, $G(y)=(y_{2},y_{3},\dots)$ and $F(G(y))=(0,y_{2},y_{3},\dots)=y$.
:::

:::

::: {.pf-step}
$F$ is a bijection of $X^{\omega}$ onto the proper subset $P$ of itself.

::: pf-proof
$F$ is injective and surjective by step [](#composites){.pf-ref}: the first composite being the identity makes $F$ injective, the second makes it surjective onto $P$. So $X^{\omega}$ is in bijective correspondence with a proper subset of itself, as the exercise asks.
:::

:::

:::

:::
