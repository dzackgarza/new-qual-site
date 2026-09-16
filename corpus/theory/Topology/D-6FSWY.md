---
schema: qual/card@1
id: D-6FSWY
kind: definition
title: Retract and retraction
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
A \dfn{retraction} of $X$ onto $A$ is a continuous map $r\colon X\to A$ with $r\circ\iota = \id_A$, that is, $r(a) = a$ for all $a\in A$:

\begin{tikzcd}
	A && X \\
	\\
	&& A
	\arrow["\iota", hook, from=1-1, to=1-3]
	\arrow["r", from=1-3, to=3-3]
	\arrow["{\id_A}"', from=1-1, to=3-3]
\end{tikzcd}

The subspace $A$ is a \dfn{retract} of $X$ if there exists a retraction of $X$ onto $A$.
:::

::: {.remark}
A retraction $r\colon X\to A$ is surjective.
If $r$ is a retraction and $a_0\in A$, then $r_*\circ\iota_* = \id$ on $\pi_1(A, a_0)$ and on $H_n(A)$, so $\iota_*\colon \pi_1(A, a_0)\to\pi_1(X, a_0)$ and $\iota_*\colon H_n(A)\to H_n(X)$ are injective.
For every point $x_0$ of a topological space $X$, the subspace $\ts{x_0}$ is a retract of $X$, via the constant map $X\to\ts{x_0}$.
:::
