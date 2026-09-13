---
schema: qual/card@1
id: P-TIE-F15-05
kind: problem
title: Questions from Tie — Fall 2015, question 5
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 5.
---

::: {.problem}
(Cauchy's formula for “exterior” region) Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$. Assume $f'(z)$ exists in an open set containing $\gamma$ and $\Omega_2$, and
\[
\lim_{z\to\infty}f(z)=A.
\]
Show that
\[
\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi-z}\,d\xi
=
\begin{cases}
A, & z\in\Omega_1,\\
-f(z)+A, & z\in\Omega_2.
\end{cases}
\]
:::
