---
schema: qual/card@1
id: P-BKS03-5A
kind: problem
title: A singular perturbation of a symmetric matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $L$ be a real symmetric $n\times n$ matrix with $0$ as a simple eigenvalue, and let $v\in\mathbb R^n$.

(a) Show that for all sufficiently small $\varepsilon>0$, the equation
\[
Lx+\varepsilon x=v
\]
has a unique solution $x(\varepsilon)$.

(b) Evaluate $\lim_{\varepsilon\to0^+}\varepsilon x(\varepsilon)$ in terms of $v$ and the eigenvectors of $L$.
:::

::: {.solution}
Since $L$ is real and symmetric, $\RR^n$ has an orthonormal basis of eigenvectors $e_1,\ldots,e_n$ of $L$. Let $\lambda_1,\ldots,\lambda_n$ be the associated eigenvalues.
Without loss of generality, $\lambda_1=0$ and $\lambda_i\neq0$ for $i>1$. Write $v=\sum_{i=1}^nv_ie_i$ and $x=\sum x_ie_i$ with $v_i,x_i\in\RR$. The equation $Lx+\varepsilon x=v$ is equivalent to $\lambda_ix_i+\varepsilon x_i=v_i$ for each $i$, which has the unique solution $x_i=v_i/(\lambda_i+\varepsilon)$, provided that $0<\varepsilon<\min_{i\neq1}\abs{\lambda_i}$. Now

$$
\varepsilon x=\sum\varepsilon x_ie_i=\sum\frac{\varepsilon}{\lambda_i+\varepsilon}v_ie_i.
$$

As $\varepsilon\to0$, all terms in the sum on the right tend to $0$ except the first, which tends to $v_1e_1=\inner{v}{e_1}e_1$.
:::
