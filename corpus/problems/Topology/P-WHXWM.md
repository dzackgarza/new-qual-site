---
schema: qual/card@1
id: P-WHXWM
kind: problem
title: Strict implications $T_4\Rightarrow T_3\Rightarrow T_2\Rightarrow T_1\Rightarrow
  T_0$
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Prove the following implications of separation axioms, and show that they are strict: ![](../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520150233.png)
:::

::: {.solution}
**Goal.** Prove the implications $T_4 \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0$ and show each is strict.

<1>1. $T_4 \Rightarrow T_3$.
<2>1. $T_4$ means normal and $T_1$; $T_3$ means regular and $T_1$.
::: {.proof}
definitions.
:::
<2>2. A normal $T_1$ space is regular.
::: {.proof}
given a closed set $C$ and a point $x \notin C$, since the space is $T_1$ the singleton $\theset{x}$ is closed, and normality separates the disjoint closed sets $C$ and $\theset{x}$ by disjoint open sets.
:::

<1>2. $T_3 \Rightarrow T_2$.
<2>1. A regular $T_1$ space is Hausdorff.
::: {.proof}
given distinct $x, y$, $T_1$ makes $\theset{y}$ closed and $x \notin \theset{y}$; regularity separates $x$ and $\theset{y}$ by disjoint open sets.
:::

<1>3. $T_2 \Rightarrow T_1$.
<2>1. A Hausdorff space is $T_1$.
::: {.proof}
given distinct $x, y$, Hausdorff gives disjoint open $U \ni x$, $V \ni y$; then $x \notin V$ and $y \notin U$, so each singleton is closed.
:::

<1>4. $T_1 \Rightarrow T_0$.
<2>1. A $T_1$ space is $T_0$.
::: {.proof}
given distinct $x, y$, $T_1$ gives an open set containing $x$ but not $y$ (namely $X \sm \theset{y}$).
:::

<1>5. Each implication is strict.
<2>1. $T_0$ but not $T_1$: the Sierpiński space $\theset{0,1}$ with open sets $\theset{\emptyset, \theset{1}, \theset{0,1}}$.
::: {.proof}
$1$ has a neighborhood not containing $0$, but $\theset{0}$ is not closed.
:::
<2>2. $T_1$ but not $T_2$: the cofinite topology on an infinite set.
::: {.proof}
singletons are closed, but any two nonempty open sets intersect.
:::
<2>3. $T_2$ but not $T_3$: the "slotted plane" or the irrational-slope topology.
::: {.proof}
a standard example of a Hausdorff space that is not regular.
:::
<2>4. $T_3$ but not $T_4$: the Sorgenfrey plane $\RR_\ell \times \RR_\ell$.
::: {.proof}
the Sorgenfrey line is regular, and its square is regular but not normal.
:::

<1>6. Q.E.D.
::: {.proof}
<1>1–<1>4 prove the implications; <1>5 shows each is strict.
:::
:::
