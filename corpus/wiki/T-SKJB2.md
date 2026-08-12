---
schema: qual/card@1
id: T-SKJB2
kind: theorem
title: "Homotopy lifting property for covers, Hatcher 1.30"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

::: {.theorem title="Homotopy lifting property for covers, Hatcher 1.30"}
Let $p:\tilde X \to X$ be any covering space, $F: Y \cross I \to X$ be any homotopy, and $\tilde F_0: Y\to \tilde X$ be any lift of $F_0$.
Then there exists a unique homotopy $\tilde F:Y\to \tilde X$ of $\tilde F_0$ that lifts $F$:

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
> [Link to diagram](https://q.uiver.app/?q=WzAsNCxbMiwwLCJcXHRpbGRlIFgiXSxbMiwyLCJYIl0sWzAsMiwiWVxcY3Jvc3MgSSJdLFswLDAsIlkiXSxbMCwxLCJwIl0sWzIsMSwiRiIsMl0sWzMsMCwiXFx0aWxkZSBGXzAiXSxbMiwwLCJcXGV4aXN0cyBcXHRpbGRlIEYiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMywyLCJ5IFxcbWFwc3RvICh5LCAwKSIsMix7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV1d)
:::
