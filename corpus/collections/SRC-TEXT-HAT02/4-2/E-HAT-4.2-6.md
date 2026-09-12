---
schema: qual/card@1
id: E-HAT-4.2-6
kind: problem
title: "Relative Hurewicz implies absolute"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that the relative form of the Hurewicz theorem in dimension $n$ implies the absolute form in dimension $n-1$ by considering the pair $(CX, X)$ where $CX$ is the cone on $X$.

::: {.solution}
Assume the relative Hurewicz theorem in dimension $n$. Let $X$ be $(n-2)$-connected, as in the absolute Hurewicz theorem in dimension $n-1$, and consider the cone pair $(CX,X)$. Since $CX$ is contractible, the long exact homotopy sequence gives
\[
\pi_i(CX,X)\cong \pi_{i-1}(X)\qquad(i\ge2).
\]
Hence $(CX,X)$ is $(n-1)$-connected. Relative Hurewicz therefore gives an isomorphism
\[
h:\pi_n(CX,X)\xrightarrow{\cong}H_n(CX,X).
\]
The homology long exact sequence of the pair, again using contractibility of $CX$, gives
\[
H_n(CX,X)\cong \widetilde H_{n-1}(X).
\]
Under these two boundary isomorphisms, naturality of the Hurewicz maps makes the square
\[
\begin{array}{ccc}
\pi_n(CX,X)&\xrightarrow{h}&H_n(CX,X)\\
\downarrow\partial&&\downarrow\partial\\
\pi_{n-1}(X)&\xrightarrow{h}&H_{n-1}(X)
\end{array}
\]
commute. The three other arrows are isomorphisms, so the bottom Hurewicz map is an isomorphism. This is exactly the absolute Hurewicz theorem in dimension $n-1$.
:::
