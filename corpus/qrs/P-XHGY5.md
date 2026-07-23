---
schema: qual/card@1
id: P-XHGY5
kind: problem
title: "Using the LES in Homotopy"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
Let $S^3 \to E \to S^5$ be a fiber bundle and compute $H_3(E)$.

:::{.solution title="Using the LES in Homotopy"}

\envlist
:::{.concept}
\envlist

- Homotopy LES: $F\to E\to B \leadsto \pi_*F() \to \pi_*(E) \to \pi_*(B)$.
- Hurewicz: $\pi_{\leq n}(X) = 0, \pi_n(X) \neq 0 \implies \pi_n(X) \cong H_n(X)$.
- $0\to A\to B \to 0$ exact iff $A\cong B$
:::

From the LES in homotopy we have

\begin{tikzcd}
	{\pi_4(S^3)} && {\pi_4(E)} && {\pi_4(S^5)} \\
	\\
	{\pi_3(S^3)} && {\pi_3(E)} && {\pi_3(S^5)} \\
	\\
	{\pi_2(S^3)} && {\pi_2(E)} & {} & {\pi_2(S^5)} \\
	\\
	{\pi_1(S^3)} && {\pi_1(E)} && {\pi_1(S^5)} \\
	\\
	{\pi_0(S^3)} && {\pi_0(E)} && {\pi_0(S^5)}
	\arrow[from=1-1, to=1-3]
	\arrow[from=1-3, to=1-5]
	\arrow[from=1-5, to=3-1, in=180, out=360]
	\arrow[from=3-1, to=3-3]
	\arrow[from=3-3, to=3-5]
	\arrow[from=3-5, to=5-1, in=180, out=360]
	\arrow[from=5-1, to=5-3]
	\arrow[from=5-3, to=5-5]
	\arrow[from=5-5, to=7-1, in=180, out=360]
	\arrow[from=7-1, to=7-3]
	\arrow[from=7-3, to=7-5]
	\arrow[from=7-5, to=9-1, in=180, out=360]
	\arrow[from=9-1, to=9-3]
	\arrow[from=9-3, to=9-5]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMTYsWzAsMCwiXFxwaV80KFNeMykiXSxbMiwwLCJcXHBpXzQoRSkiXSxbNCwwLCJcXHBpXzQoU141KSJdLFswLDIsIlxccGlfMyhTXjMpIl0sWzIsMiwiXFxwaV8zKEUpIl0sWzQsMiwiXFxwaV8zKFNeNSkiXSxbMyw0XSxbMCw0LCJcXHBpXzIoU14zKSJdLFswLDYsIlxccGlfMShTXjMpIl0sWzAsOCwiXFxwaV8wKFNeMykiXSxbMiw0LCJcXHBpXzIoRSkiXSxbNCw0LCJcXHBpXzIoU141KSJdLFsyLDYsIlxccGlfMShFKSJdLFs0LDYsIlxccGlfMShTXjUpIl0sWzIsOCwiXFxwaV8wKEUpIl0sWzQsOCwiXFxwaV8wKFNeNSkiXSxbMCwxXSxbMSwyXSxbMiwzXSxbMyw0XSxbNCw1XSxbNSw3XSxbNywxMF0sWzEwLDExXSxbMTEsOF0sWzgsMTJdLFsxMiwxM10sWzEzLDldLFs5LDE0XSxbMTQsMTVdXQ==)

and plugging in known information yields

\begin{tikzcd}
	{\pi_4(S^3)} && {\pi_4(E)} && 0 \\
	\\
	\textcolor{rgb,255:red,92;green,92;blue,214}{\ZZ} && \textcolor{rgb,255:red,92;green,92;blue,214}{\pi_3(E)} && 0 \\
	\\
	0 && \textcolor{rgb,255:red,214;green,92;blue,92}{\pi_2(E) = 0} & {} & 0 \\
	\\
	0 && \textcolor{rgb,255:red,214;green,92;blue,92}{\pi_1(E)=0} && 0 \\
	\\
	\ZZ && {\pi_0(E)} && \ZZ
	\arrow[from=1-1, to=1-3]
	\arrow[from=1-3, to=1-5]
	\arrow[from=1-5, to=3-1, in=180, out=360]
	\arrow["\sim", color={rgb,255:red,92;green,92;blue,214}, hook, two heads, from=3-1, to=3-3]
	\arrow[no head, from=3-3, to=3-5]
	\arrow[from=3-5, to=5-1, in=180, out=360]
	\arrow[from=5-1, to=5-3]
	\arrow[from=5-3, to=5-5]
	\arrow[from=5-5, to=7-1, in=180, out=360]
	\arrow[from=7-1, to=7-3]
	\arrow[from=7-3, to=7-5]
	\arrow[from=7-5, to=9-1, in=180, out=360]
	\arrow[hook, from=9-1, to=9-3]
	\arrow[two heads, from=9-3, to=9-5]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMTYsWzAsMCwiXFxwaV80KFNeMykiXSxbMiwwLCJcXHBpXzQoRSkiXSxbNCwwLCIwIl0sWzAsMiwiXFxaWiIsWzI0MCw2MCw2MCwxXV0sWzIsMiwiXFxwaV8zKEUpIixbMjQwLDYwLDYwLDFdXSxbNCwyLCIwIl0sWzMsNF0sWzAsNCwiMCJdLFswLDYsIjAiXSxbMCw4LCJcXFpaIl0sWzIsNCwiXFxwaV8yKEUpID0gMCIsWzAsNjAsNjAsMV1dLFs0LDQsIjAiXSxbMiw2LCJcXHBpXzEoRSk9MCIsWzAsNjAsNjAsMV1dLFs0LDYsIjAiXSxbMiw4LCJcXHBpXzAoRSkiXSxbNCw4LCJcXFpaIl0sWzAsMV0sWzEsMl0sWzIsM10sWzMsNCwiXFxjb25nIiwxLHsiY29sb3VyIjpbMjQwLDYwLDYwXSwic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifSwiaGVhZCI6eyJuYW1lIjoiZXBpIn19fSxbMjQwLDYwLDYwLDFdXSxbNCw1LCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJub25lIn19fV0sWzUsN10sWzcsMTBdLFsxMCwxMV0sWzExLDhdLFs4LDEyXSxbMTIsMTNdLFsxMyw5XSxbOSwxNCwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMTQsMTUsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6ImVwaSJ9fX1dXQ==)

where

- Rows 3 and 4 force $\pi_3(E) \cong \ZZ$, 
- Rows 0 and 1 force $\pi_0(E) = \ZZ$ (todo: not clear if this is true... is it even needed here?)
- The remaining rows force $\pi_1(E) = \pi_2(E) = 0$.

By Hurewicz, we thus have $H_3(E) = \pi_3(E) = \ZZ$. 
:::

:::{.solution title="Using the Serre spectral sequence"}

:::{.remark}
Four-corner spectral sequences, only homology in degrees 1,3,5,8. No differentials hit anything!
:::

:::

