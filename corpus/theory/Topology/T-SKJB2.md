---
schema: qual/card@1
id: T-SKJB2
kind: theorem
title: Homotopy lifting property for covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
relations: []
review: draft
---

::: {.theorem}
Let $p\colon\tilde X \to X$ be a [[D-2PNEG|covering space]], $F\colon Y \cross I \to X$ a homotopy, and $\tilde F_0\colon Y\to \tilde X$ a lift of $F_0 = F(\wait, 0)$.
Then there is a unique homotopy $\tilde F\colon Y\cross I\to \tilde X$ with $\tilde F(y, 0) = \tilde F_0(y)$ for all $y\in Y$ and $p\circ\tilde F = F$ [@Hat02, Proposition 1.30, p. 60]:

\begin{tikzcd}
	{Y} && {\tilde X} \\
	\\
	{Y\cross I} && {X}
	\arrow["{p}", from=1-3, to=3-3]
	\arrow["{F}"', from=3-1, to=3-3]
	\arrow["{\tilde F_0}", from=1-1, to=1-3]
	\arrow["{\exists \tilde F}", from=3-1, to=1-3, dashed]
	\arrow["{y \mapsto (y, 0)}"', from=1-1, to=3-1, hook]
\end{tikzcd}
:::
