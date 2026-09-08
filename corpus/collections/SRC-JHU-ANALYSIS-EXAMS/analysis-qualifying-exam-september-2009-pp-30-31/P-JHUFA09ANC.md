---
schema: qual/card@1
id: P-JHUFA09ANC
kind: problem
title: "Dyadic averages of an $L^1$ function converge almost everywhere"
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Analysis Qualifying Exam, September 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
For $n\ge1$ and $0\le j\le2^n-1$, let
\[
I_{n,j}=[j2^{-n},(j+1)2^{-n}].
\]
For $f\in L^1([0,1])$, define
\[
E_nf(x)=\sum_{j=0}^{2^n-1}\left(2^n\int_{I_{n,j}}f(t)\,dt\right)\chi_{I_{n,j}}(x).
\]
Prove that $E_nf(x)\to f(x)$ for almost every $x\in[0,1]$.
:::

::: {.solution}
The dyadic endpoints form a countable set, hence a null set. Fix $x\in(0,1)$ that is not a dyadic endpoint. For each $n$ there is then a unique dyadic interval $I_n(x)$ of length $2^{-n}$ containing $x$, and
\[
E_nf(x)=\frac1{|I_n(x)|}\int_{I_n(x)}f(t)\,dt.
\]
Moreover,
\[
x\in I_n(x),
\qquad
|I_n(x)|=2^{-n}\longrightarrow0.
\]

By the Lebesgue differentiation theorem, for almost every $x\in[0,1]$,
\[
\frac1{|I|}\int_I f(t)\,dt\longrightarrow f(x)
\]
whenever intervals $I$ contain $x$ and their lengths tend to $0$. Applying this to the dyadic intervals $I_n(x)$ gives
\[
E_nf(x)\longrightarrow f(x)
\]
for almost every non-dyadic $x$. Since the dyadic endpoints themselves form a null set, the conclusion holds almost everywhere on $[0,1]$.
:::
