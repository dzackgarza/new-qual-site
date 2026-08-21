---
schema: qual/card@1
id: PR-YCTNC
kind: proposition
title: Separability is transitive.
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
---

::: {.proposition title="Separability is transitive."}
If $L/K/k$, then $L/K$ is separable and $K/k$ is separable $\iff$ $L/k$ is separable:

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

> [Link to Diagram](https://q.uiver.app/?q=WzAsNixbMCwwLCJMIl0sWzAsMiwiSyJdLFswLDQsImsiXSxbMywwLCJMIl0sWzMsMiwiSyJdLFszLDQsImsiXSxbMiwxLCIiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzEsMCwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifSwiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFs1LDQsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNCwzLCIiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMSwiIiwyLHsiY3VydmUiOjIsImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMSwyLCIiLDIseyJjdXJ2ZSI6MiwiY29sb3VyIjpbMCw2MCw2MF0sInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFs1LDMsIiIsMix7ImN1cnZlIjozLCJjb2xvdXIiOlsxMjAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJhcnJvd2hlYWQifSwiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNyw5LCIiLDAseyJzaG9ydGVuIjp7InNvdXJjZSI6MjAsInRhcmdldCI6MjB9fV1d)
:::
