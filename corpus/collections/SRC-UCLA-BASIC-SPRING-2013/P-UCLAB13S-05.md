---
schema: qual/card@1
id: P-UCLAB13S-05
kind: problem
title: Chebyshev polynomials of the second kind
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained source prints U_1=1 and U_2=2x while also indexing n from 0 and asking for U_n(cos theta)=sin((n+1)theta)/sin(theta). This card corrects the evident indexing typo to the standard U_0=1, U_1=2x.
---

::: {.problem}
Define polynomials $U_n(x)$, $n=0,1,2,\ldots$, by
\[
U_0(x)=1,\qquad U_1(x)=2x,\qquad U_{n+1}(x)=2xU_n(x)-U_{n-1}(x).
\]

(a) Prove that
\[
U_n(\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta}.
\]

(b) Prove that
\[
\int_{-1}^1 U_m(x)U_n(x)\sqrt{1-x^2}\,dx
=
\begin{cases}
0,&m\neq n,\\
\pi/2,&m=n.
\end{cases}
\]
:::
