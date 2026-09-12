---
schema: qual/card@1
id: P-RAF21E
kind: problem
title: "Weak convergence plus norm convergence implies strong convergence in L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - L2 Spaces
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f_n, f \in L^2(\mathbb{R})$ satisfy $f_n \to f$ weakly and $\|f_n\|_2 \to \|f\|_2$ as $n \to \infty$.
Show that $f_n \to f$ in $L^2(\mathbb{R})$.
:::

::: solution
<1>1. Expand the Hilbert-space norm of the difference.
::: proof
Since $L^2(\mathbb R)$ is a Hilbert space,
\[
\|f_n-f\|_2^2
=\|f_n\|_2^2+
\|f\|_2^2
-2\operatorname{Re}\langle f_n,f\rangle.
\]
Weak convergence $f_n\rightharpoonup f$ implies, by testing against the fixed vector $f$,
\[
\langle f_n,f\rangle\longrightarrow\langle f,f\rangle=\|f\|_2^2.
\]
The assumed convergence of norms gives
\[
\|f_n\|_2^2\longrightarrow\|f\|_2^2.
\]
Therefore
\[
\|f_n-f\|_2^2\longrightarrow
\|f\|_2^2+
\|f\|_2^2-
2\|f\|_2^2
=0.
\]
Hence
\[
\boxed{\|f_n-f\|_2\to0.}
\]
:::
:::
