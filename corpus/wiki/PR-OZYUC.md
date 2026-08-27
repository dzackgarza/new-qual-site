---
schema: qual/card@1
id: PR-OZYUC
kind: proposition
title: Characterization of normal algebraic extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
---

::: {.proposition}
For $L/k$ algebraic: let $\bar{k}$ be an algebraic closure containing $L$, then $L/k$ is normal iff every $k\dash$embedding $\sigma: L\to \bar{k}$ satisfies $\im \sigma = L$, so $\sigma$ is a $k\dash$automorphism of $L$:

\begin{tikzcd}
	&& {\bar{k}} \\
	\\
	L && \textcolor{rgb,255:red,92;green,214;blue,92}{\sigma(L) = L} \\
	\\
	k && k
	\arrow[hook, from=5-1, to=3-1]
	\arrow[Rightarrow, no head, from=5-1, to=5-3]
	\arrow[hook, from=5-3, to=3-3]
	\arrow[hook, from=3-3, to=1-3]
	\arrow["\sigma", hook, from=3-1, to=1-3]
	\arrow[hook, two heads, from=3-1, to=3-3]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNSxbMCw0LCJrIl0sWzAsMiwiTCJdLFsyLDQsImsiXSxbMiwwLCJcXGJhcntrfSJdLFsyLDIsIlxcc2lnbWEoTCkgPSBMIixbMTIwLDYwLDYwLDFdXSxbMCwxLCIiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDIsIiIsMSx7ImxldmVsIjoyLCJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzIsNCwiIiwxLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbNCwzLCIiLDEseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFsxLDMsIlxcc2lnbWEiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFsxLDQsIiIsMSx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn0sImhlYWQiOnsibmFtZSI6ImVwaSJ9fX1dXQ==)
:::
