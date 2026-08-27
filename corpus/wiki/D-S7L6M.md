---
schema: qual/card@1
id: D-S7L6M
kind: definition
title: Exact Functor
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Category Theory
relations: []
review: draft
---

:::{.definition}
A functor $T$ is *right exact* if a short exact sequence 

\[0 \to A \to B \to C \to 0
\]
yields an exact sequence 

\[\ldots TA \to TB \to TC \to 0
\]
and is *left exact* if it yields 

\[0 \to TA \to TB \to TC \to \ldots
\]
Thus a functor is exact iff it is both left and right exact, yielding

\[0 \to TA \to TB \to TC \to 0
.\]


:::{.example}
$\wait \tensor_{R} \wait$ is a right exact bifunctor.
:::

:::
