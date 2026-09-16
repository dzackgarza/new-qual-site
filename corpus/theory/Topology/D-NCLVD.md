---
schema: qual/card@1
id: D-NCLVD
kind: definition
title: Retract
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, and $\iota\colon A\injects X$ the inclusion.
A \dfn{retraction} of $X$ onto $A$ is a [[D-AEAAD|continuous map]] $r\colon X\to A$ with $r\circ\iota=\id_A$, that is, $r(a)=a$ for every $a\in A$:

\begin{tikzcd}
	A && X
	\arrow["\iota", hook, from=1-1, to=1-3]
	\arrow["r", curve={height=-18pt}, dashed, from=1-3, to=1-1]
\end{tikzcd}

The subspace $A$ is a \dfn{retract} of $X$ if a retraction of $X$ onto $A$ exists.
:::

::: {.proposition}
Let $A\subseteq X$ be a subspace with inclusion $\iota\colon A\injects X$.

(a) Every retraction $r\colon X\to A$ is surjective.

(b) Continuous maps $r\colon X\to A$ with $r\circ\iota=\id_A$ correspond bijectively to continuous maps $\rho\colon X\to X$ with $\rho(X)=A$ and $\rho(a)=a$ for all $a\in A$, via $\rho=\iota\circ r$.
:::

