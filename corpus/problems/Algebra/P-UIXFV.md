---
schema: qual/card@1
id: P-UIXFV
kind: problem
title: Dimensions of the irreducible representations of $D_n$, and $\sum_i(\dim V_i)^2=|G|$
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
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
How would you work out the orders of the irreducible representations of the dihedral group $D_n$?

Why is the sum of squares of dimensions equal to the order of the group?
:::

::: {.solution}
Write
\[
D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\qquad |D_n|=2n.
\]
Its abelianization has order $2$ when $n$ is odd and $4$ when $n$ is even. Hence there are respectively $2$ or $4$ one-dimensional irreducible complex representations.

The remaining irreducibles are two-dimensional. For
\[
\chi_k(r)=e^{2\pi i k/n}
\]
on $\langle r\rangle\cong C_n$, the induced representation
\[
\operatorname{Ind}_{\langle r\rangle}^{D_n}\chi_k
\]
is irreducible unless $k=0$ or, when $n$ is even, $k=n/2$. Moreover $k$ and $n-k$ give isomorphic induced representations. Thus the number of two-dimensional irreducibles is
\[
\frac{n-1}{2}\quad(n\text{ odd}),
\qquad
\frac{n-2}{2}\quad(n\text{ even}).
\]
Hence
\[
2\cdot1^2+\frac{n-1}{2}\cdot2^2=2n
\]
when $n$ is odd, while
\[
4\cdot1^2+\frac{n-2}{2}\cdot2^2=2n
\]
when $n$ is even.

The general identity
\[
\sum_i(\dim V_i)^2=|G|
\]
comes from the regular representation:
\[
\mathbb C[G]\cong\bigoplus_i V_i^{\oplus\dim V_i}.
\]
Taking dimensions gives the formula.
:::
