---
schema: qual/card@1
id: PR-L7LNZ
kind: proposition
title: Uniform Limits Commute with Integrals
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Integrals
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mathcal M,\mu)$ be a finite measure space. If $f_n,f\in L^1(X,\mu)$ and $f_n\to f$ uniformly (equivalently, $\|f_n-f\|_\infty\to0$), then
\[
\int_X f_n\,d\mu\longrightarrow\int_X f\,d\mu.
\]
More precisely,
\[
\left|\int_X(f_n-f)\,d\mu\right|
\le \mu(X)\|f_n-f\|_\infty.
\]
:::

::: {.proof}
Since $\mu(X)<\infty$,
\[
\begin{aligned}
\left|\int_X(f_n-f)\,d\mu\right|
&\le \int_X|f_n-f|\,d\mu\\
&\le \mu(X)\|f_n-f\|_\infty.
\end{aligned}
\]
The right-hand side tends to $0$, proving the claimed convergence of the integrals.
:::
