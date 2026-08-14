---
schema: qual/card@1
id: T-EF5IX
kind: theorem
title: "Lifting criterion for covers, Hatcher 1.33"
classification:
  areas:
  - topology
  topics:
  - covering-spaces
  - fundamental-group
relations: []
review: draft
---

::: {.theorem title="Lifting criterion for covers, Hatcher 1.33"}
If $f: Y\to X$ with $Y$ path-connected and locally path-connected, then there exists a unique lift $\tilde f: Y\to \tilde X$ if and only if $f_*(\pi_1(Y)) \subset \pi_*(\pi_1 (\tilde X))$:

\begin{tikzcd}
	&& {\tilde X} \\
	\\
	{Y} && {X}
	\arrow["{p}", from=1-3, to=3-3]
	\arrow["{f}"', from=3-1, to=3-3]
	\arrow["{\tilde f}", from=3-1, to=1-3, dashed]
\end{tikzcd}
> [Link to diagram](https://q.uiver.app/?q=WzAsMyxbMCwyLCJZIl0sWzIsMiwiWCJdLFsyLDAsIlxcdGlsZGUgWCJdLFsyLDEsInAiXSxbMCwxLCJmIiwyXSxbMCwyLCJcXHRpbGRlIGYiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0=)

Moreover, lifts are *unique* if they agree at a single point.
:::
