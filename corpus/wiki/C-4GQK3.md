---
schema: qual/card@1
id: C-4GQK3
kind: corollary
title: "Normality satisfies the lifting property"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.corollary title="Normality satisfies the lifting property"}
$E_1/k$ normal and $E_2/k$ normal $\implies E_1E_2/k$ normal and $E_1 \intersect E_2 / k$ normal.

\begin{tikzcd}
	&& {E_1 E_2} \\
	\\
	{E_1} &&&& {E_2} \\
	&& {E_1 \cap E_2} \\
	\\
	\\
	&& {k}
	\arrow["{\text{normal}}", from=3-5, to=7-3]
	\arrow[from=4-3, to=7-3, dashed, no head, "\text{normal}", near start]
	\arrow["{\text{normal}}"', from=3-1, to=7-3]
	\arrow[from=1-3, to=3-1, no head]
	\arrow[from=1-3, to=3-5, no head]
	\arrow[from=1-3, to=4-3, no head]
	\arrow[from=1-3, to=7-3, curve={height=25pt}, dashed, no head, "\text{normal}"', near start]
	\arrow[from=3-1, to=4-3, no head]
	\arrow[from=4-3, to=3-5, no head]
\end{tikzcd}

> [Link to diagram](https://q.uiver.app/?q=WzAsNSxbMiwwLCJFXzEgRV8yIl0sWzAsMiwiRV8xIl0sWzQsMiwiRV8yIl0sWzIsMywiRV8xIFxcY2FwIEVfMiJdLFsyLDYsImsiXSxbMiw0LCJcXHRleHR7bm9ybWFsfSJdLFszLDQsIiIsMix7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzEsNCwiXFx0ZXh0e25vcm1hbH0iLDJdLFswLDEsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMCwyLCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMywiIiwxLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFswLDQsIiIsMSx7ImN1cnZlIjozLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifSwiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsxLDMsIiIsMSx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbMywyLCIiLDEseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV1d)
:::
