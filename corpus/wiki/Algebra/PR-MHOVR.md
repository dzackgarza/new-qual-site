---
schema: qual/card@1
id: PR-MHOVR
kind: proposition
title: Normal extensions are upper transitive, forward implication
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
relations: []
review: draft
---

::: {.proposition}
For $L/k$ finite,

\begin{tikzcd}
	L &&&& L \\
	\\
	K && \implies && K \\
	\\
	k &&&& k
	\arrow[from=3-1, to=1-1]
	\arrow[from=5-1, to=3-1]
	\arrow["{\text{Normal}}"', color={rgb,255:red,214;green,92;blue,92}, curve={height=24pt}, dashed, from=5-1, to=1-1]
	\arrow[from=5-5, to=3-5]
	\arrow[from=3-5, to=1-5]
	\arrow["{\text{Normal}}"', color={rgb,255:red,214;green,92;blue,92}, curve={height=18pt}, dashed, from=3-5, to=1-5]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNyxbMCwwLCJMIl0sWzAsMiwiSyJdLFswLDQsImsiXSxbMiwyLCJcXGltcGxpZXMiXSxbNCwwLCJMIl0sWzQsMiwiSyJdLFs0LDQsImsiXSxbMSwwXSxbMiwxXSxbMiwwLCJcXHRleHR7Tm9ybWFsfSIsMix7ImN1cnZlIjo0LCJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fSxbMCw2MCw2MCwxXV0sWzYsNV0sWzUsNF0sWzUsNCwiXFx0ZXh0e05vcm1hbH0iLDIseyJjdXJ2ZSI6MywiY29sb3VyIjpbMCw2MCw2MF0sInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX0sWzAsNjAsNjAsMV1dXQ==)
:::
