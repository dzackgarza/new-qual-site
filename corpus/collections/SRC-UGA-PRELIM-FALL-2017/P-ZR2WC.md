---
schema: qual/card@1
id: P-ZR2WC
kind: problem
title: Uniform convergence to zero implies convergence of the integrals
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Riemann Integrability
relations: []
review: draft
---

::: problem
Let $\{f_n:[0,1]\to\mathbb R\}_{n=1}^{\infty}$ be continuous functions that converge uniformly to $0$. Show that
\[
\int_0^1 f_n(x)\,dx\longrightarrow0.
\]
:::

::: solution
Uniform convergence to zero gives
\[
\|f_n\|_{\infty}=\sup_{x\in[0,1]}|f_n(x)|\longrightarrow0.
\]
Therefore
\[
\left|\int_0^1f_n(x)\,dx\right|
\leq\int_0^1|f_n(x)|\,dx
\leq\|f_n\|_{\infty}\longrightarrow0.
\]
:::
