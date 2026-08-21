---
schema: qual/card@1
id: PR-QDRB4
kind: proposition
title: Galois is upper transitive, characterization of when lower transitivity holds
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

:::{.proposition title="Galois is upper transitive, characterization of when lower transitivity holds"}
If $L/k$ is Galois, then $L/F$ is **always** Galois.
Moreover, $F/k$ is Galois if and only if \( \Gal(L/F) \normal \Gal(L/k) \)

\begin{tikzcd}
	{L} \\
	\\
	{F} \\
	\\
	{k}
	\arrow["{\text{Galois}}", from=1-1, to=5-1, curve={height=-18pt}, no head]
	\arrow["{\text{Galois}}", from=5-1, to=3-1, curve={height=-12pt}, squiggly, no head]
	\arrow["{\text{Galois}}"', from=1-1, to=3-1, curve={height=12pt}, dashed, no head]
\end{tikzcd}

> [Link to diagram](https://q.uiver.app/?q=WzAsMyxbMCwwLCJMIl0sWzAsMiwiRiJdLFswLDQsImsiXSxbMCwyLCJcXHRleHR7R2Fsb2lzfSIsMCx7ImN1cnZlIjotMywic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoibm9uZSJ9fX1dLFsyLDEsIlxcdGV4dHtHYWxvaXN9IiwwLHsiY3VydmUiOi0yLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJzcXVpZ2dseSJ9LCJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzAsMSwiXFx0ZXh0e0dhbG9pc30iLDIseyJjdXJ2ZSI6Miwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XV0=)

In this case, 
\[
\Gal(F/k) \cong \frac{\Gal(L/k)}{\Gal(L/F)}
.\]

:::
