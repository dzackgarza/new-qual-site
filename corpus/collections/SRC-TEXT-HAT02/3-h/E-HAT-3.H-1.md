---
schema: qual/card@1
id: E-HAT-3.H-1
kind: problem
title: "Homology of $S^1$ with twisted $\\ZZ$ coefficients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Compute $H_*(S^1; E)$ and $H^*(S^1; E)$ for $E \to S^1$ the nontrivial bundle with fiber $\ZZ$.
:::

::: {.solution}
Give $S^1$ its CW structure with one $0$-cell and one $1$-cell. For the nontrivial local system $E$ with fiber $\ZZ$, monodromy around the circle acts by $-1$.

The cellular chain complex with local coefficients is therefore
\[
0\longrightarrow \ZZ
\xrightarrow{(-1)-1=-2}\ZZ\longrightarrow0.
\]
Hence
\[
H_1(S^1;E)=\ker(-2)=0,
\qquad
H_0(S^1;E)=\operatorname{coker}(-2)\cong\ZZ_2.
\]

The cellular cochain complex is the dual two-term complex
\[
0\longrightarrow\ZZ
\xrightarrow{-2}\ZZ\longrightarrow0,
\]
so
\[
H^0(S^1;E)=0,
\qquad
H^1(S^1;E)\cong\ZZ_2.
\]
All other homology and cohomology groups vanish. Thus
\[
\boxed{H_n(S^1;E)=
\begin{cases}\ZZ_2,&n=0,\\0,&n\ne0,
\end{cases}}
\]
and
\[
\boxed{H^n(S^1;E)=
\begin{cases}\ZZ_2,&n=1,\\0,&n\ne1.
\end{cases}}
\]
:::
