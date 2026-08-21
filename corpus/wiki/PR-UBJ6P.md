---
schema: qual/card@1
id: PR-UBJ6P
kind: proposition
title: Fundamental theorem of covering spaces, Hatcher 1.39
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.proposition title="Fundamental theorem of covering spaces, Hatcher 1.39"}
If $X$ is

- Path-connected,

- Locally path-connected, and

- Semilocally simply connected,

then $X$ admits a universal cover $\hat{X} \to X$: if $C \mapsvia{q} X$ is any other covering map with $C$ connected, then there exists a covering map $\tilde p: \hat{X} \to C$ making the following diagram commute:

\begin{tikzcd}
	{C} && {\hat X} \\
	\\
	{X}
	\arrow["{q}", from=1-1, to=3-1, two heads]
	\arrow["{p}", from=1-3, to=3-1, two heads]
	\arrow["{\tilde p}"', from=1-3, to=1-1, dashed, two heads]
\end{tikzcd}
> [Link to diagram](https://q.uiver.app/?q=WzAsMyxbMCwyLCJYIl0sWzAsMCwiQyJdLFsyLDAsIlxcdGlsZGUgWCJdLFsxLDAsInEiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMiwwLCJwIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV0sWzIsMSwiXFx0aWxkZSBwIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn0sImhlYWQiOnsibmFtZSI6ImVwaSJ9fX1dXQ==)

That is, any other cover $C$ of $X$ is itself covered by $\hat X$.
Note that by the universal property, $\hat X$ is unique up to homeomorphism when it exists.

Moreover, letting $\tilde X \to X$ be an arbitrary path-connected cover and $H\da p_* \pi_1(\tilde X; \tilde x_0), G\da \pi_1(X; x_0)$,

- The $\tilde X\to X$ is Galois iff $H\normal G$,

- $\Deck(\tilde X\to X) \cong N_{G}(H)/H$ where $N$ is the normalizer in $G$ of $H$,

- $\Deck(\tilde X\to X) \cong G/H$ if $\tilde X\to X$ is Galois,

- $\Deck(\hat{X} \to X) \cong G$.
:::
