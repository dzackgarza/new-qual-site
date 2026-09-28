---
schema: qual/card@1
id: D-WB4M5
kind: definition
title: Separable degree
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
Let $L/k$ be an algebraic field extension, let $\bar{k}$ be an algebraic closure of $k$, and fix an embedding $\sigma\colon k\embeds \bar{k}$.
The \dfn{separable degree} $[L:k]_s$ is the cardinality of the set of field embeddings $\sigma'\colon L\to \bar{k}$ that extend $\sigma$, that is, with $\sigma'|_k=\sigma$:

\begin{tikzcd}
	L && {\bar{k}} \\
	\\
	k && k
	\arrow["{\sigma'}", dashed, hook, from=1-1, to=1-3]
	\arrow["\iota", hook, from=3-1, to=1-1]
	\arrow["\sigma"', hook, from=3-3, to=1-3]
	\arrow["\id", Rightarrow, no head, from=3-1, to=3-3]
\end{tikzcd}

Here $\iota\colon k\embeds L$ is the inclusion.
:::
