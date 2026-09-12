---
schema: qual/card@1
id: P-WESRA04-P5
kind: problem
title: Equality of all restricted integrals forces equality almost everywhere
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Real Analysis section 2.3, problem 5 of the Wesleyan Preliminary Examination, August 2, 2004, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $f,g$ be integrable functions on a measure space $(X,\mathcal B,\mu)$. Suppose that
\[
\int_A f\,d\mu=\int_A g\,d\mu
\]
for every $A\in\mathcal B$. Prove that $f=g$ almost everywhere.
:::

::: solution
Set
\[
h=f-g\in L^1(\mu).
\]
Then
\[
\int_A h\,d\mu=0
\qquad(A\in\mathcal B).
\]
For each $n\ge1$, let
\[
E_n=\{x:h(x)>1/n\}.
\]
If $\mu(E_n)>0$, then
\[
0=\int_{E_n}h\,d\mu
\ge \frac1n\mu(E_n)>0,
\]
a contradiction. Hence every $E_n$ is null, so
\[
\mu\{h>0\}=0.
\]
Applying the same argument to $-h$ gives
\[
\mu\{h<0\}=0.
\]
Therefore $h=0$ almost everywhere, i.e.
\[
\boxed{f=g\quad\mu\text{-a.e.}}
\]

If the functions are complex-valued, apply the same argument separately to the real and imaginary parts of $h$.
:::
