---
schema: qual/card@1
id: P-BKF03-3A
kind: problem
title: Berkeley Fall 2003 prelim problem 3A
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
  note: Checked against Problem 3A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified necessity from A^n tending to zero on eigenvectors and sufficiency by the two Jordan-form cases.
---

::: {.problem}
Let A be a $2 \times 2$ matrix with complex entries.
Prove that the series $I + A + A ^ { 2 } + . . .$ converges if and only if every eigenvalue of A has absolute value less than 1.
:::
\n\n::: {.solution}\nConvergence of a matrix series is equivalent in any matrix norm on $M_2(\mathbb C)$, so we may freely conjugate the series by a fixed invertible matrix.\n\n<1>1. If $\sum_{n=0}^\infty A^n$ converges, then every eigenvalue of $A$ has modulus less than $1$.\n::: {.proof}\nConvergence of the series implies its terms tend to zero:\n\[\nA^n\longrightarrow0.\n\]\nLet $v\ne0$ be an eigenvector with eigenvalue $\lambda$. Then\n\[\nA^nv=\lambda^n v.\n\]\nSince $A^nv\to0$ and $v\ne0$, one must have $\lambda^n\to0$. This is equivalent to $|\lambda|<1$.\n:::\n\n<1>2. Suppose every eigenvalue of $A$ has modulus less than $1$. Reduce $A$ to Jordan normal form.\n::: {.proof}\nThere is an invertible matrix $S$ such that\n\[\nA=SJS^{-1},\n\qquad\nA^n=SJ^nS^{-1}.\n\]\nHence\n\[\n\sum_{n=0}^N A^n\n=S\left(\sum_{n=0}^N J^n\right)S^{-1}.\n\]\nThus the series for $A$ converges if the series for $J$ converges. For a $2\times2$ matrix, $J$ is either diagonal or a single Jordan block.\n:::\n\n<1>3. If $J=\operatorname{diag}(\lambda,\mu)$ with $|\lambda|,|\mu|<1$, then $\sum J^n$ converges.\n::: {.proof}\nOne has\n\[\nJ^n=\begin{pmatrix}\lambda^n&0\\0&\mu^n\end{pmatrix}.\n\]\nTherefore\n\[\n\sum_{n=0}^\infty J^n\n=\begin{pmatrix}\sum_{n=0}^\infty\lambda^n&0\\0&\sum_{n=0}^\infty\mu^n\end{pmatrix},\n\]\nand both scalar geometric series converge.\n:::\n\n<1>4. If\n\[\nJ=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},\n\qquad |\lambda|<1,\n\]\nthen $\sum J^n$ also converges.\n::: {.proof}\nWrite $J=\lambda I+N$ with\n\[\nN=\begin{pmatrix}0&1\\0&0\end{pmatrix},\n\qquad N^2=0.\n\]\nFor $n\ge1$, the binomial theorem gives\n\[\nJ^n=\lambda^n I+n\lambda^{n-1}N\n=\begin{pmatrix}\lambda^n&n\lambda^{n-1}\\0&\lambda^n\end{pmatrix}.\n\]\nThe geometric series $\sum\lambda^n$ converges, and\n\[\n\sum_{n=1}^\infty n\lambda^{n-1}=\frac1{(1-\lambda)^2}\n\]\nalso converges absolutely for $|\lambda|<1$. Hence every entry of $\sum J^n$ converges.\n:::\n\nBy <1>2--<1>4, if every eigenvalue of $A$ has modulus less than $1$, then $\sum A^n$ converges. Together with <1>1, this proves the equivalence.\n:::\n