---
schema: qual/card@1
id: E-PER08-6.3
kind: problem
title: Index 2 subgroups of the free group $F_2$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
(From May’s book.)
Identify all index 2 subgroups of the free group F2. Show that they are all free groups and identify generators for them.
:::

::: {.solution}
Write $F_2=\langle a,b\rangle$.
Index-$2$ subgroups are normal and are exactly the kernels of the three nonzero homomorphisms
\[
F_2\longrightarrow\mathbb Z/2.
\]
Thus there are exactly three.

<1>1. The kernel of $a\mapsto1$, $b\mapsto0$ is free on
\[
a^2,\quad b,\quad aba^{-1}.
\]
::: {.proof}
Use the Schreier transversal $\{1,a\}$.
The nontrivial Schreier generators $t x\overline{tx}^{-1}$ for $t\in\{1,a\}$ and $x\in\{a,b\}$ are precisely $b,a^2,aba^{-1}$.
:::

<1>2. The kernel of $a\mapsto0$, $b\mapsto1$ is free on
\[
b^2,\quad a,\quad bab^{-1}.
\]
::: {.proof}
This is the same Schreier computation with $a$ and $b$ interchanged.
:::

<1>3. The kernel of $a\mapsto1$, $b\mapsto1$ is free on
\[
a^2,\quad ba^{-1},\quad ab.
\]
::: {.proof}
With transversal $\{1,a\}$, Schreier's method yields the three displayed nontrivial generators.
Nielsen--Schreier also predicts rank $1+2(2-1)=3$, so each listed generating set is a free basis.
:::
:::
