---
schema: qual/card@1
id: P-BKS04-3B
kind: problem
title: UC Berkeley Spring 2004 prelim 3B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $A$ be a $d\times d$ matrix with complex entries.
Assume that every eigenvalue of $A$ has absolute value $1$. Prove that there exists a constant $c\in\RR$ independent of $n$ such that

$$
\norm{A^nx}\leq cn^{d-1}\norm{x}
$$

for all $n\geq1$ and $x\in\CC^d$. Here $\norm{x}\coloneqq(\abs{x_1}^2+\cdots+\abs{x_d}^2)^{1/2}$ for all $(x_1,\ldots,x_d)\in\CC^d$.
:::

::: {.solution}
We may use $\abs{x}_\infty\coloneqq\max\{\abs{x_1},\ldots,\abs{x_d}\}$ instead of $\norm{x}$, since different norms on a finite-dimensional vector space are bounded by positive constants times each other.
Then it suffices to show that the entries of $A^n$ are $O(n^{d-1})$ as $n\to\infty$. This property is unchanged if we conjugate all the $A^n$ by a fixed invertible matrix.
Thus we may assume that $A$ is in Jordan canonical form.
Thus $A=D+N$ where $D$ is diagonal, $N$ is nilpotent, and $D$ and $N$ commute.
By the Cayley--Hamilton theorem, $N^d=0$. Thus the binomial theorem gives

$$
A^n=D^n+\binom n1D^{n-1}N+\binom n2D^{n-2}N^2+\cdots+\binom{n}{d-1}D^{n-d+1}N^{d-1}.
$$

The diagonal entries of $D$ are the eigenvalues of $A$, which have absolute value $1$, so the entries of $D^m$ are $O(1)$ for any $m$. The entries of $N,N^2,\ldots,N^{d-1}$ do not depend on $n$. The binomial coefficients are $O(n^{d-1})$. Thus the entries of $A^n$ are $O(n^{d-1})$, as desired.
:::
