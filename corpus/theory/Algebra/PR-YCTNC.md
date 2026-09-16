---
schema: qual/card@1
id: PR-YCTNC
kind: proposition
title: Separability is transitive in towers
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
---

::: {.proposition}
Let $k\subseteq K\subseteq L$ be algebraic field extensions.
Then $L/k$ is [[D-JGYLA|separable]] if and only if $L/K$ and $K/k$ are both separable:

\begin{tikzcd}
	L &&& L \\
	\\
	K &&& K \\
	\\
	k &&& k
	\arrow[hook, no head, from=5-1, to=3-1]
	\arrow[""{name=0, anchor=center, inner sep=0}, hook, no head, from=3-1, to=1-1]
	\arrow[hook, no head, from=5-4, to=3-4]
	\arrow[""{name=1, anchor=center, inner sep=0}, hook, no head, from=3-4, to=1-4]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, curve={height=12pt}, dashed, from=1-1, to=3-1]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, curve={height=12pt}, dashed, from=3-1, to=5-1]
	\arrow[color={rgb,255:red,92;green,214;blue,92}, curve={height=18pt}, dashed, tail reversed, no head, from=5-4, to=1-4]
	\arrow[shorten <=19pt, shorten >=19pt, Rightarrow, from=0, to=1]
\end{tikzcd}
:::
