---
schema: qual/card@1
id: E-20CHL
kind: problem
title: Continuity implies separate continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 11, printed p. 112; the definition
    of continuity in each variable separately is stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.11, PDF p. 13. Each slice map is the composite
    of F with an imbedding x -> x x y_0 (Exercise 18.4), hence continuous.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof, both variables now symmetric steps and the
    continuity of the slice map a step of its own. Re-read the retained set's lines for Exercise
    18.11 in its text version (tmp/sources/positron-ch2.txt, the paragraph beginning "Exercise
    18.11. Assume F is continuous") against the two steps: the set composes F with the slice
    imbedding x -> x x y_0 of Exercise 18.4 and says nothing more, which is what the card's steps
    verify. Continuity of the slice map is now obtained from the criterion for a map into a
    product (Theorem 18.4) rather than quoted from Exercise 18.4, since that criterion is the
    book's own statement and the exercise is its special case. The concluding step adds the
    witness for the strictness of the implication: Exercise 18.12's function, separately
    continuous and discontinuous at the origin. Nothing on the statement changed; the converse
    is not claimed.
---

::: {.exercise}

Let $F: X \times Y \to Z$.
We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \to Z$ defined by $h(x) = F(x \times y_0)$ is continuous, and for each $x_0$ in $X$, the map $k: Y \to Z$ defined by $k(y) = F(x_0 \times y)$ is continuous.
Show that if $F$ is continuous, then $F$ is continuous in each variable separately.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.11, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the composition argument is theirs. Whitman, printed p. 188, proves the same by chasing a neighbourhood through a product basis element.

::: pf

::: {.pf-step #slice-imbedding}
For each $y_{0}\in Y$ the slice map $j_{y_{0}}:X\to X\times Y$, $j_{y_{0}}(x)=x\times y_{0}$, is continuous; and for each $x_{0}\in X$ the slice map $j'_{x_{0}}:Y\to X\times Y$, $j'_{x_{0}}(y)=x_{0}\times y$, is continuous.

::: pf-proof
The composite $\pi_{1}\circ j_{y_{0}}$ is the identity map of $X$ and the composite $\pi_{2}\circ j_{y_{0}}$ is the constant map at $y_{0}$; both are continuous, so $j_{y_{0}}$ is continuous by the criterion for continuity of a map into a product space (Theorem 18.4), which asks only that its composites with the two projections be continuous. Interchanging the roles of the coordinates, $\pi_{1}\circ j'_{x_{0}}$ is constant and $\pi_{2}\circ j'_{x_{0}}$ is the identity of $Y$, so $j'_{x_{0}}$ is continuous as well. These are the maps shown to be imbeddings in Exercise 18.4; only their continuity is used here.
:::

:::

::: {.pf-step #first-variable}
For each $y_{0}\in Y$ the map $h:X\to Z$ of the exercise, $h(x)=F(x\times y_{0})$, is continuous.

::: pf-proof
The map $h$ equals $F\circ j_{y_{0}}$, a composite of the continuous map of step [](#slice-imbedding){.pf-ref} with the continuous map $F:X\times Y\to Z$. A composite of continuous maps is continuous.
:::

:::

::: {.pf-step #second-variable}
For each $x_{0}\in X$ the map $k:Y\to Z$ of the exercise, $k(y)=F(x_{0}\times y)$, is continuous.

::: pf-proof
The map $k$ equals $F\circ j'_{x_{0}}$, again a composite of the continuous map of step [](#slice-imbedding){.pf-ref} with $F$.
:::

:::

::: {.pf-step #conclusion}
A continuous $F:X\times Y\to Z$ is continuous in each variable separately, and the implication does not reverse.

::: pf-proof
Steps [](#first-variable){.pf-ref} and [](#second-variable){.pf-ref} establish the continuity of every map $h$ and every map $k$ named in the definition of continuity in each variable separately, which is the first assertion. For the failure of the converse, Exercise 18.12 gives $F:\RR\times\RR\to\RR$ with $F(x\times y)=xy/(x^{2}+y^{2})$ off the origin and $F(0\times 0)=0$: for fixed $y_{0}\ne0$ the map $x\mapsto xy_{0}/(x^{2}+y_{0}^{2})$ is continuous and for $y_{0}=0$ it is constantly $0$, and symmetrically in $y$, while along the diagonal $x=y\ne0$ the value is $\tfrac12$ and at the origin $0$, so $F$ is not continuous at $0\times0$.
:::

:::

:::
:::
