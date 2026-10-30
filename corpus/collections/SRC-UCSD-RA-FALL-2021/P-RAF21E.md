---
schema: qual/card@1
id: P-RAF21E
kind: problem
title: "Weak convergence plus norm convergence implies strong convergence in $L^2$"
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

::: {.problem}
Let $f_n, f \in L^2(\RR)$ satisfy $f_n \to f$ weakly and $\norm{f_n}_2 \to \norm{f}_2$ as $n \to \infty$.
Show that $f_n \to f$ in $L^2(\RR)$.
:::

::: {.solution}

::: pf

::: pf-step

$\norm{f_n-f}_2^2=\norm{f_n}_2^2+\norm{f}_2^2-2\operatorname{Re}\langle f_n,f\rangle\to0$.

::: pf-proof

Since $L^2(\RR)$ is a Hilbert space,
$$
\norm{f_n-f}_2^2
=\norm{f_n}_2^2+
\norm{f}_2^2
-2\operatorname{Re}\langle f_n,f\rangle.
$$
Weak convergence $f_n\rightharpoonup f$ implies, by testing against the fixed vector $f$,
$$
\langle f_n,f\rangle\longrightarrow\langle f,f\rangle=\norm{f}_2^2.
$$
The assumed convergence of norms gives
$$
\norm{f_n}_2^2\longrightarrow\norm{f}_2^2.
$$
Therefore
$$
\norm{f_n-f}_2^2\longrightarrow
\norm{f}_2^2+
\norm{f}_2^2-
2\norm{f}_2^2
=0.
$$
Hence
$$
\boxed{\norm{f_n-f}_2\to0.}
$$

:::

:::

:::

:::
