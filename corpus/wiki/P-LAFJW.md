---
schema: qual/card@1
id: P-LAFJW
kind: problem
title: Homology of the complement of a knotted solid torus in $S^3$
classification:
  areas:
  - topology
  topics:
  - mayer-vietoris
  - homology
  - manifolds
relations: []
review: draft
solved: true
---

Compute $H_*$ of the complement of a knotted solid torus in $S^3$.

::: {.solution}

\envlist
::: {.concept}
\envlist

- $H_*(T^2) = [\ZZ, \ZZ^2, \ZZ, 0\rightarrow]$

- $N^{(1)} \homotopic S^1$, so $H_{\geq 2}(N) = 0$.

- A SES $0\to A\to B \to F \to 0$ with $F$ free splits.

- $0\to A \to B \mapsvia{\cong} C \to D \to 0$ implies $A = D = 0$.
:::

Let $N$ be the knotted solid torus, so that $\del N = T^2$, and let $X = S^3 - N$.
Then

- $S^3 = N \union_{T^2} X$

- $N \cap X = T^2$

and we apply Mayer-Vietoris to the reduced homology of $S^3$:

% https://q.uiver.app/?q=WzAsMTIsWzAsMCwiSF80KFReMikiXSxbMiwwLCJIXzQoTikgXFxvcGx1cyBIXzQoWCkiXSxbNCwwLCJIXzQoU14zKSJdLFswLDIsIkhfNChUXjIpIl0sWzAsNCwiSF80KFReMikiXSxbMiw0LCJIXzQoTikgXFxvcGx1cyBIXzQoWCkiXSxbMiwyLCJIXzQoTikgXFxvcGx1cyBIXzQoWCkiXSxbNCwyLCJIXzQoU14zKSJdLFs0LDQsIkhfNChTXjMpIl0sWzAsNiwiSF80KFNeMykiXSxbMiw2LCJIXzQoTikgXFxvcGx1cyBIXzQoWCkiXSxbNCw2LCJIXzQoU14zKSJdLFs0LDVdLFs4LDldLFs5LDEwXSxbMTAsMTFdLFs1LDhdLFszLDZdLFs2LDddLFs3LDRdLFsyLDNdLFswLDFdLFsxLDJdXQ==
\begin{tikzcd}
	{H_4(T^2)} && {H_4(N) \oplus H_4(X)} && {H_4(S^3)} \\
	\\
	{H_3(T^2)} && {H_3(N) \oplus H_3(X)} && {H_3(S^3)} \\
	\\
	{H_2(T^2)} && {H_2(N) \oplus H_2(X)} && {H_2(S^3)} \\
	\\
	{H_1(S^3)} && {H_1(N) \oplus H_1(X)} && {H_1(S^3)}
	\arrow[from=5-1, to=5-3]
	\arrow[from=5-3, to=5-5]
	\arrow[from=5-5, to=7-1, out=360, in=180]
	\arrow[from=7-1, to=7-3]
	\arrow[from=7-3, to=7-5]
	\arrow[from=3-1, to=3-3]
	\arrow[from=3-3, to=3-5]
	\arrow[from=3-5, to=5-1, out=360, in=180]
	\arrow[from=5-3, to=5-5]
	\arrow[from=1-5, to=3-1, out=360, in=180]
	\arrow[from=1-1, to=1-3]
	\arrow[from=1-3, to=1-5]
\end{tikzcd}

We can plug in known information and deduce some maps:

% https://q.uiver.app/?q=WzAsMTIsWzAsMCwiMCJdLFs0LDAsIjAiXSxbMCwyLCIwIixbMjQwLDYwLDYwLDFdXSxbMCw0LCJcXFpaIixbMjQwLDYwLDYwLDFdXSxbMiw0LCJIXzIoWCkiLFsyNDAsNjAsNjAsMV1dLFsyLDIsIkhfMyhYKSIsWzI0MCw2MCw2MCwxXV0sWzQsMiwiXFxaWiIsWzI0MCw2MCw2MCwxXV0sWzQsNCwiMCIsWzI0MCw2MCw2MCwxXV0sWzAsNiwiXFxaWl57XFxvcGx1cyAyfSJdLFsyLDYsIlxcWlogXFxvcGx1cyBIXzEoWCkgIl0sWzQsNiwiMCJdLFsyLDAsIjAiXSxbMyw0LCIiLDAseyJjb2xvdXIiOlsyNDAsNjAsNjBdfV0sWzcsOF0sWzgsOSwiXFxzaW0iLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9LCJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbOSwxMF0sWzQsNywiIiwwLHsiY29sb3VyIjpbMjQwLDYwLDYwXX1dLFsyLDUsIiIsMCx7ImNvbG91ciI6WzI0MCw2MCw2MF19XSxbNSw2LCIiLDAseyJjb2xvdXIiOlsyNDAsNjAsNjBdfV0sWzYsMywiIiwwLHsiY29sb3VyIjpbMjQwLDYwLDYwXX1dLFsxLDJdLFswLDExXSxbMTEsMV1d
\begin{tikzcd}
	0 && 0 && 0 \\
	\\
	\textcolor{rgb,255:red,92;green,92;blue,214}{0} && \textcolor{rgb,255:red,92;green,92;blue,214}{H_3(X)} && \textcolor{rgb,255:red,92;green,92;blue,214}{\ZZ} \\
	\\
	\textcolor{rgb,255:red,92;green,92;blue,214}{\ZZ} && \textcolor{rgb,255:red,92;green,92;blue,214}{H_2(X)} && \textcolor{rgb,255:red,92;green,92;blue,214}{0} \\
	\\
	{\ZZ^{\oplus 2}} && {\ZZ \oplus H_1(X) } && 0
	\arrow[color={rgb,255:red,92;green,92;blue,214}, from=5-1, to=5-3]
	\arrow[from=5-5, to=7-1, out=360, in=180]
	\arrow["\sim", hook, two heads, from=7-1, to=7-3]
	\arrow[from=7-3, to=7-5]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, from=5-3, to=5-5]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, from=3-1, to=3-3]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, from=3-3, to=3-5]
	\arrow[color={rgb,255:red,92;green,92;blue,214}, from=3-5, to=5-1, out=360, in=180]
	\arrow[from=1-5, to=3-1, out=360, in=180]
	\arrow[from=1-1, to=1-3]
	\arrow[from=1-3, to=1-5]
\end{tikzcd}

We then deduce:

- $H_0(X) = \ZZ$: ? (Appeal to some path-connectedness argument?)

- $H_1(X) = \ZZ$ using the SES appearing on the first row:
  \[
  0 \to \ZZ^{ \oplus 2} \to \ZZ \oplus H_1(X) \to 0
  \]
  which is thus an isomorphism.

- $H_2(X) = H_3(X) = 0$ by examining the SES spanning lines 3 and 2:
  \[
  0 \injects H_3(X) \injects \ZZ \mapsvia{\cong_{\del_3}} \ZZ \surjects H_2(X) \surjects 0
  \]
  Claim: \( \bd_3 \) must be an isomorphism.
  If this is true, $H_3(X) \cong \ker \bd_3 = 0$ and $H_2(X) \cong \coker(\bd_3) \da \ZZ/\im(\bd_3) \cong \ZZ/\ZZ = 0$.

::: {.remark}
Why is this true?
:::
:::
