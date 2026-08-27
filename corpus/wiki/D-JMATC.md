---
schema: qual/card@1
id: D-JMATC
kind: definition
title: Distinguished Classes
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
A collection of field extensions $\mathcal{S}$ is **distinguished** iff

1. (Transitive property) For any tower $L/K/k$, the extension $L/k \in \mathcal{S} \iff L/K \in \mcs$ (upper transitivity) and $K/k\in \mathcal{S}$ (lower transitivity):

\begin{tikzcd}
	L &&&& L \\
	\\
	K && \iff && K \\
	\\
	k &&&& k
	\arrow[hook, from=5-1, to=3-1]
	\arrow[hook, from=3-1, to=1-1]
	\arrow[hook, from=5-5, to=3-5]
	\arrow[hook, from=3-5, to=1-5]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, curve={height=18pt}, dashed, hook, from=5-1, to=1-1]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, curve={height=18pt}, dashed, hook, from=5-5, to=3-5]
	\arrow[color={rgb,255:red,214;green,92;blue,92}, curve={height=18pt}, dashed, hook, from=3-5, to=1-5]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNyxbMCw0LCJrIl0sWzAsMiwiSyJdLFswLDAsIkwiXSxbNCw0LCJrIl0sWzQsMiwiSyJdLFs0LDAsIkwiXSxbMiwyLCJcXGlmZiJdLFswLDEsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzEsMiwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMyw0LCIiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFs0LDUsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzAsMiwiIiwyLHsiY3VydmUiOjMsImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9LCJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMyw0LCIiLDIseyJjdXJ2ZSI6MywiY29sb3VyIjpbMCw2MCw2MF0sInN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn0sImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFs0LDUsIiIsMix7ImN1cnZlIjozLCJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifSwiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV1d)

2. (Lifting property) Lifts of distinguished extensions are distinguished: $K/k\in \mathcal{S}$ and $L/k$ any extension $\implies LK/L \in \mathcal{S}$:

\begin{tikzcd}
	& LK \\
	L && K \\
	& k
	\arrow[draw={rgb,255:red,214;green,92;blue,92}, dashed, hook, from=3-2, to=2-3]
	\arrow[hook', from=3-2, to=2-1]
	\arrow["\therefore", draw={rgb,255:red,214;green,92;blue,92}, dashed, hook, from=2-1, to=1-2]
	\arrow[hook, from=2-3, to=1-2]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMSwyLCJrIl0sWzIsMSwiSyJdLFswLDEsIkwiXSxbMSwwLCJMSyJdLFswLDEsIiIsMCx7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9LCJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMCwyLCIiLDIseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6ImJvdHRvbSJ9fX1dLFsyLDMsIlxcdGhlcmVmb3JlIiwwLHsiY29sb3VyIjpbMCw2MCw2MF0sInN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn0sImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFsxLDMsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV1d)

3. (Compositing property) Whenever $L/k, K/k\in \mcs$, the amalgam $LK/k \in \mcs$ as well:

\begin{tikzcd}
	& LK \\
	L && K \\
	& k
	\arrow[draw={rgb,255:red,214;green,92;blue,92}, hook, from=3-2, to=2-3]
	\arrow[draw={rgb,255:red,214;green,92;blue,92}, hook', from=3-2, to=2-1]
	\arrow[draw={rgb,255:red,214;green,92;blue,92}, hook, from=2-1, to=1-2]
	\arrow[hook, from=2-3, to=1-2]
	\arrow["\therefore", color={rgb,255:red,214;green,92;blue,92}, dashed, from=3-2, to=1-2]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMSwyLCJrIl0sWzIsMSwiSyJdLFswLDEsIkwiXSxbMSwwLCJMSyJdLFswLDEsIiIsMCx7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDIsIiIsMix7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6ImJvdHRvbSJ9fX1dLFsyLDMsIiIsMCx7ImNvbG91ciI6WzAsNjAsNjBdLCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFsxLDMsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzAsMywiXFx0aGVyZWZvcmUiLDAseyJjb2xvdXIiOlswLDYwLDYwXSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fSxbMCw2MCw2MCwxXV1d)

> One is supposed to think of $LK/L$ as a "lift" of $K/k$.
:::
