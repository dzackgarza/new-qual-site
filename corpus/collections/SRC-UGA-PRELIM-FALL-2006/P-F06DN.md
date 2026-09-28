---
schema: qual/card@1
id: P-F06DN
kind: problem
title: Inductive formula for the derivatives of $xe^{2x}$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f(x) = xe^{2x}$.
Writing $f^{(n)}(x)$ for the $n$th derivative of $f(x)$, prove by induction that $f^{(n)}(x) = 2^n xe^{2x} + n 2^{n-1}e^{2x}$ for all $n \geq 0$.
:::

::: {.solution}
For $n=0$, the formula reads
\[
f(x)=xe^{2x}=2^0xe^{2x}+0,
\]
so the base case holds.

Assume
\[
f^{(n)}(x)=2^nxe^{2x}+n2^{n-1}e^{2x}.
\]
Differentiating gives
\[
\begin{aligned}
f^{(n+1)}(x)
&=2^n e^{2x}+2^{n+1}xe^{2x}+n2^n e^{2x}\\
&=2^{n+1}xe^{2x}+(n+1)2^n e^{2x}.
\end{aligned}
\]
This is exactly the claimed formula with $n$ replaced by $n+1$. Hence it holds for all $n\ge0$.
:::
