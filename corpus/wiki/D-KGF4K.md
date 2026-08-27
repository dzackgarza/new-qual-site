---
schema: qual/card@1
id: D-KGF4K
kind: definition
title: Embeddings and Lifts
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Homomorphisms
relations: []
review: draft
---

::: {.definition}
Let $k$ denote a field, and $L/k$ extension.
Every field morphism is an embedding (injection).
An **embedding** of $k\dash$algebras $L\embeds L'$ will refer to any ring morphism over $k$, i.e. a field morphism that restricts to the identity on $k$:

\begin{tikzcd}
	L && {L'} \\
	\\
	& k
	\arrow[hook', from=3-2, to=1-1]
	\arrow[hook, from=3-2, to=1-3]
	\arrow[hook, from=1-1, to=1-3]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMyxbMCwwLCJMIl0sWzIsMCwiTCciXSxbMSwyLCJrIl0sWzIsMCwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJib3R0b20ifX19XSxbMiwxLCIiLDIseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDEsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV1d)

More generally, we can ask for lifts of any map $\sigma: k\to k'$:

\begin{tikzcd}
	L && {L'} \\
	\\
	k && {k'}
	\arrow[""{name=0, anchor=center, inner sep=0}, hook, from=1-1, to=1-3]
	\arrow[""{name=1, anchor=center, inner sep=0}, "\sigma", hook, from=3-1, to=3-3]
	\arrow[hook, from=3-1, to=1-1]
	\arrow[hook, from=3-3, to=1-3]
	\arrow[shorten <=9pt, shorten >=9pt, Rightarrow, from=1, to=0]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMCwwLCJMIl0sWzIsMCwiTCciXSxbMCwyLCJrIl0sWzIsMiwia19cXHNpZ21hIl0sWzAsMSwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMiwzLCJcXHNpZ21hIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMiwwLCIiLDEseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFszLDEsIiIsMSx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzUsNCwiIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfX1dXQ==)

Most often, we'll take $\sigma: k\to k$ to be the identity.
:::
