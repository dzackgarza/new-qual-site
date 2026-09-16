---
schema: qual/card@1
id: P-CRR65
kind: problem
title: Representations and character table of $D_4$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(1) Describe the irreducible complex representations and character table of the dihedral group $D_4$ (order 8).
(2) Explicitly construct the 2-dimensional irreducible representation.
(3) Provide its geometric interpretation as symmetries of the square.
:::

::: {.solution}
Write
\[
D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle.
\]
Its conjugacy classes are
\[
\{1\},\quad \{r^2\},\quad \{r,r^3\},\quad
\{s,sr^2\},\quad \{sr,sr^3\}.
\]
Hence there are five irreducible complex characters. Since
\[
[D_4,D_4]=\langle r^2\rangle,
\qquad D_4^{\mathrm{ab}}\cong C_2\times C_2,
\]
there are four one-dimensional characters, obtained by choosing independently \(r\mapsto\pm1\) and \(s\mapsto\pm1\).

The remaining irreducible representation is the geometric representation
\[
\rho(r)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\rho(s)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
These matrices satisfy \(r^4=s^2=1\) and \(srs=r^{-1}\), so they define a representation. Its character is
\[
\chi_5=(2,-2,0,0,0)
\]
on the five classes above, and
\[
\langle\chi_5,\chi_5\rangle
=\frac18(4+4)=1,
\]
so it is irreducible.

Thus the character table is
\[
\begin{array}{c|ccccc}
&1&r^2&\{r,r^3\}&\{s,sr^2\}&\{sr,sr^3\}\\\hline
\chi_1&1&1&1&1&1\\
\chi_2&1&1&-1&1&-1\\
\chi_3&1&1&1&-1&-1\\
\chi_4&1&1&-1&-1&1\\
\chi_5&2&-2&0&0&0
\end{array}
\]
with class sizes \(1,1,2,2,2\).

Geometrically, \(\rho(r)\) is rotation of the square by \(\pi/2\), and \(\rho(s)\) is reflection across the \(x\)-axis.
:::
