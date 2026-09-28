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
  - Lebesgue Integration
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
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "The same dyadic-average statement appears in September 2009 problem 3 and in problem 1 of both undated packets (pp. 4-5 and 6-7); merged the duplicate card P-JHUU45RA1, whose Lebesgue-point estimate replaces the less explicit solution."
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
Except at dyadic endpoints, for each $n$ there is a unique interval $I_n(x)$ of length $2^{-n}$ containing $x$, and
\[
E_nf(x)=\frac1{|I_n(x)|}\int_{I_n(x)}f(t)\,dt.
\]
The intervals $I_n(x)$ shrink to $x$ and satisfy
\[
I_n(x)\subset[x-2^{-n},x+2^{-n}].
\]
If $x$ is a Lebesgue point of $f$, then
\[
\begin{aligned}
|E_nf(x)-f(x)|
&\le \frac1{|I_n(x)|}\int_{I_n(x)}|f(t)-f(x)|\,dt\\
&\le 2\cdot\frac1{2^{1-n}}\int_{x-2^{-n}}^{x+2^{-n}}|f(t)-f(x)|\,dt.
\end{aligned}
\]
The last expression tends to $0$ by the Lebesgue differentiation theorem. Since almost every point of $[0,1]$ is a Lebesgue point of $f$, and the dyadic endpoints form a countable set, we obtain
\[
E_nf(x)\longrightarrow f(x)
\]
for almost every $x\in[0,1]$.
:::
