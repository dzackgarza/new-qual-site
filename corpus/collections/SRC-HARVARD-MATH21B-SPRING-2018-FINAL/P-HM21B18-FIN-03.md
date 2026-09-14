---
schema: qual/card@1
id: P-HM21B18-FIN-03
kind: problem
title: Diagonalizability, linearity, and Fourier-coefficient diagnostics
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
(a) Decide which of
\[
A=\begin{pmatrix}0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\\1&0&0&0&0\end{pmatrix},
\quad
B=\begin{pmatrix}0&1&0&0&1\\1&0&1&0&0\\0&1&0&1&0\\0&0&1&0&1\\1&0&0&1&0\end{pmatrix},
\]
\[
C=\begin{pmatrix}0&1&1&0&0\\0&0&1&1&0\\0&0&0&1&1\\0&0&0&0&1\\0&0&0&0&0\end{pmatrix}
\]
are diagonalizable over $\mathbb R$.

(b) Decide which of the two displayed Game-of-Life matrices “Loaf” and “Boat” has a nonreal eigenvalue:
\[
L=\begin{pmatrix}
0&0&0&0&0&0\\0&0&1&1&0&0\\0&1&0&0&1&0\\0&0&1&0&1&0\\0&0&0&1&0&0\\0&0&0&0&0&0
\end{pmatrix},
\]
\[
B_0=\begin{pmatrix}
0&0&0&0&0\\0&1&1&0&0\\0&1&0&1&0\\0&0&1&0&0\\0&0&0&0&0
\end{pmatrix}.
\]

(c) On $X=C^\infty_{\mathrm{per}}([ -\pi,\pi])$, decide which of the sets
\[
\{f\in X:f(1)=b_1(f)\},\qquad \{f\in X:f'(1)=0\}
\]
are linear subspaces, and which of the maps
\[
T(f)=a_1(f)f,
\qquad
T(f)=\|f\|\sin x
\]
are linear.

(d) For a continuous Fourier series
\[
f(x)=\frac{a_0}{\sqrt2}+\sum_{n\ge1}a_n\cos(nx)+b_n\sin(nx),
\]
decide which of the assertions $a_0=0$, all $a_n=0$ for $n>0$, and all $b_n=0$ hold for every even $f$, every odd $f$, and every $f$ with no real zeros.
:::
