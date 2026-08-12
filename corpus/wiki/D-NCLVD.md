---
schema: qual/card@1
id: D-NCLVD
kind: definition
title: "Retract"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.definition title="Retract"}
A map $r$ in $A\mathrel{\textstyle\substack{\injects^{\iota}\\\textstyle\dashleftarrow_{r}}} B$ satisfying $$r\circ\iota = \id_{A}.$$
A **retract** of $B$ onto a subspace $A$ is a map $r:B\to A$ that is a left-inverse for the inclusion $f:A\injects B$, so $r \circ f = \id_A$:


\begin{tikzcd}
	A && B
	\arrow["f", from=1-1, to=1-3]
	\arrow["r"', curve={height=18pt}, dashed, from=1-3, to=1-1]
	\arrow[loop left, from=1-1]{l}{\mathrm{id}_A}
\end{tikzcd}

> [Link to (partial) Diagram](https://q.uiver.app/?q=WzAsMixbMCwwLCJBIl0sWzIsMCwiQiJdLFswLDEsImYiXSxbMSwwLCJyIiwyLHsiY3VydmUiOjMsInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==)

Equivalently, a continuous map $r:B\to A$ with $\ro{r}{A} = \id_A$ restricting to the identity on $A$, i.e. fixing $A$ pointwise.
Note that $r$ is necessarily a surjection.

Alt:
Let $X$ be a topological space and $A \subset X$ be a subspace, then a **retraction** of $X$ onto $A$ is a map $r: X\into X$ such that the image of $X$ is $A$ and $r$ restricted to $A$ is the identity.
:::
