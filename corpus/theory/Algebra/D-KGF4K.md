---
schema: qual/card@1
id: D-KGF4K
kind: definition
title: Embeddings and lifts of field homomorphisms
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
Let $k$ be a field and let $L/k$ and $L'/k$ be field extensions.
A \dfn{$k$-embedding} $L\embeds L'$ is a ring homomorphism $\tau\colon L\to L'$ that restricts to the identity on $k$:

\begin{tikzcd}
	L && {L'} \\
	\\
	& k
	\arrow["\iota"', hook', from=3-2, to=1-1]
	\arrow["{\iota'}", hook, from=3-2, to=1-3]
	\arrow["\tau", hook, from=1-1, to=1-3]
\end{tikzcd}

Here $\iota$ and $\iota'$ are the inclusions, and the triangle commutes: $\tau\circ\iota=\iota'$.

More generally, let $\sigma\colon k\to k'$ be a homomorphism of fields and let $L/k$ and $L'/k'$ be field extensions with inclusions $\iota\colon k\to L$ and $\iota'\colon k'\to L'$.
A \dfn{lift} of $\sigma$ to $L\to L'$ is a ring homomorphism $\tau\colon L\to L'$ such that $\tau\circ\iota=\iota'\circ\sigma$:

\begin{tikzcd}
	L && {L'} \\
	\\
	k && {k'}
	\arrow["\tau", hook, from=1-1, to=1-3]
	\arrow["\sigma", hook, from=3-1, to=3-3]
	\arrow["\iota", hook, from=3-1, to=1-1]
	\arrow["{\iota'}"', hook, from=3-3, to=1-3]
\end{tikzcd}

A lift of $\sigma=\id_k$ is a $k$-embedding.
:::

::: {.remark}
Every ring homomorphism $\tau\colon L\to L'$ between [[D-UI6CU|fields]] is injective: $\ker\tau$ is an ideal of $L$ not containing $1$, and the only such ideal of a field is $0$.
:::
