---
schema: qual/card@1
id: P-BERK86S-11
kind: problem
title: An orthonormal rational family on the real line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
For $n\in\mathbb Z$, define
\[
f_n(x)=\frac{(x-i)^n}{\sqrt\pi\,(x+i)^{n+1}},
\qquad x\in\mathbb R.
\]
Prove that the functions $f_n$ are orthonormal:
\[
\int_{-\infty}^{\infty}f_m(x)\overline{f_n(x)}\,dx
=
\begin{cases}
1,&m=n,\\
0,&m\ne n.
\end{cases}
\]
:::
