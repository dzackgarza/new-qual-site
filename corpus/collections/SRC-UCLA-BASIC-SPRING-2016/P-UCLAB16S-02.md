---
schema: qual/card@1
id: P-UCLAB16S-02
kind: problem
title: Riemann integrability after changing a convergent sequence
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $a<b$ be real numbers.

1. Define what it means for a function $f:[a,b]\to\mathbb R$ to be Riemann integrable on $[a,b]$.
2. Let $\{x_n\}_{n=1}^{\infty}\subset[a,b]$ be a sequence such that $\lim_{n\to\infty}x_n$ exists, and define
\[
f(x)=\begin{cases}
1,&x\notin\{x_n:n\ge1\},\\
0,&x\in\{x_n:n\ge1\}.
\end{cases}
\]
Using your definition, prove that $f$ is Riemann integrable on $[a,b]$.
:::
