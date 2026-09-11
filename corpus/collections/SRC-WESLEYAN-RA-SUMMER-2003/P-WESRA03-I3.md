---
schema: qual/card@1
id: P-WESRA03-I3
kind: problem
title: A positive-measure compact set containing no rational numbers
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Short Answer Question 3 of the Wesleyan Preliminary Exam in Analysis, August 4, 2003, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Is there a compact subset of $[0,1]\setminus\mathbb Q$ with positive Lebesgue measure?
:::

::: solution
Yes. Enumerate the rationals in $[0,1]$ as $(q_n)_{n\ge1}$. For each $n$, choose an open interval $I_n$ containing $q_n$ with
\[
m(I_n)<2^{-n-2}.
\]
Set
\[
U=\bigcup_{n=1}^\infty I_n,
\qquad
K=[0,1]\setminus U.
\]
Then $K$ is closed in the compact interval $[0,1]$, hence compact, and it contains no rational number. Moreover
\[
m(U)\le\sum_{n=1}^\infty2^{-n-2}=\frac14,
\]
so
\[
m(K)\ge\frac34>0.
\]
Thus such a compact set exists.
:::
