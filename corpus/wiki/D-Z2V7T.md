---
schema: qual/card@1
id: D-Z2V7T
kind: definition
title: "Exact Functor"
classification:
  areas:
  - topology
  topics:
  - homological-algebra
  - category-theory
relations: []
review: draft
---
:::{.definition title="Exact Functor"}
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

:::
