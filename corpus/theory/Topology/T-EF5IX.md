---
schema: qual/card@1
id: T-EF5IX
kind: theorem
title: Lifting criterion for covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.theorem}
Let $p\colon(\tilde X, \tilde x_0)\to(X, x_0)$ be a [[D-2PNEG|covering space]] and $f\colon(Y, y_0)\to(X, x_0)$ a map with $Y$ path-connected and locally path-connected.
Then a lift $\tilde f\colon(Y, y_0)\to(\tilde X, \tilde x_0)$ with $p\circ\tilde f = f$ exists if and only if $f_*(\pi_1(Y, y_0)) \subseteq p_*(\pi_1 (\tilde X, \tilde x_0))$ [@Hat02, Proposition 1.33, p. 61]:

\begin{tikzcd}
	&& {\tilde X} \\
	\\
	{Y} && {X}
	\arrow["{p}", from=1-3, to=3-3]
	\arrow["{f}"', from=3-1, to=3-3]
	\arrow["{\tilde f}", from=3-1, to=1-3, dashed]
\end{tikzcd}

If $Y$ is connected, two lifts of $f$ that agree at one point are equal [@Hat02, Proposition 1.34, p. 62].
:::
