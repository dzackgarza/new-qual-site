---
schema: qual/card@1
id: D-JMATC
kind: definition
title: Distinguished classes of field extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.definition}
A class $\mathcal{S}$ of field extensions is \dfn{distinguished} if it satisfies the following two conditions.

1. For every tower of fields $k\subseteq K\subseteq L$, $L/k \in \mathcal{S}$ if and only if $L/K \in \mathcal{S}$ and $K/k\in \mathcal{S}$:

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

2. If $K/k\in \mathcal{S}$ and $L/k$ is an extension such that $K$ and $L$ are subfields of a common field, then $LK/L \in \mathcal{S}$, where $LK$ is the compositum.
   The extension $LK/L$ is the \dfn{lift} of $K/k$ to $L$:

\begin{tikzcd}
	& LK \\
	L && K \\
	& k
	\arrow[draw={rgb,255:red,214;green,92;blue,92}, dashed, hook, from=3-2, to=2-3]
	\arrow[hook', from=3-2, to=2-1]
	\arrow["\therefore", draw={rgb,255:red,214;green,92;blue,92}, dashed, hook, from=2-1, to=1-2]
	\arrow[hook, from=2-3, to=1-2]
\end{tikzcd}
:::

::: {.proposition}
Let $\mathcal{S}$ be a distinguished class of field extensions.
If $L/k\in\mathcal{S}$ and $K/k\in \mathcal{S}$, with $K$ and $L$ subfields of a common field, then $LK/k \in \mathcal{S}$:

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
:::

::: {.proof}
By the lifting condition applied to $K/k\in\mathcal{S}$ and $L/k$, the extension $LK/L$ lies in $\mathcal{S}$.
Applying the tower condition to $k\subseteq L\subseteq LK$, with $LK/L\in\mathcal{S}$ and $L/k\in\mathcal{S}$, gives $LK/k\in\mathcal{S}$.
:::
