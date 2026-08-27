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
The **separable degree** of an extension $L/k$ is defined by fixing an embedding $\sigma: k\embeds \bar{k}$ (the algebraic or separable closure) and letting $[L:k]_s$ be the number of embeddings $\sigma':L\to \bar{k}$:

\begin{tikzcd}
	L && {\bar{k}} \\
	\\
	k && k
	\arrow["{\sigma'}", dashed, hook, from=1-1, to=1-3]
	\arrow[hook, from=3-1, to=1-1]
	\arrow["\sigma"', hook, from=3-3, to=1-3]
	\arrow[Rightarrow, no head, from=3-1, to=3-3]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMCwyLCJrIl0sWzIsMCwiXFxiYXJ7a30iXSxbMCwwLCJMIl0sWzIsMiwiayJdLFsyLDEsIlxcc2lnbWEnIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifSwiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzAsMiwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMywxLCJcXHNpZ21hIiwyLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMCwzLCIiLDIseyJsZXZlbCI6Miwic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dXQ==)
:::
