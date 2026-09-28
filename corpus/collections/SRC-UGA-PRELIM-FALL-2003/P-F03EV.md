---
schema: qual/card@1
id: P-F03EV
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
classification:
  areas:
  - prelim
  topics:
  - Eigenvalues
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $A$ be an $n \times n$ matrix.

a) Define what is meant by the eigenvalues and eigenvectors of $A$.

b) Show that if $v$ and $w$ are eigenvectors of $A$ corresponding to distinct eigenvalues $\lambda$ and $\mu$, then $v$ and $w$ are linearly independent.
:::

::: {.solution}
A scalar $\lambda$ is an eigenvalue of $A$ if there exists a nonzero vector $v$ such that
\[
Av=\lambda v.
\]
Such a nonzero vector is an eigenvector corresponding to $\lambda$.

Suppose $Av=\lambda v$ and $Aw=\mu w$, where $v,w\ne0$ and $\lambda\ne\mu$. If
\[
av+bw=0,
\]
then applying $A$ gives
\[
a\lambda v+b\mu w=0.
\]
Subtracting $\lambda$ times the original relation yields
\[
b(\mu-\lambda)w=0.
\]
Since $w\ne0$ and $\mu-\lambda\ne0$, we get $b=0$. Then $av=0$, so $a=0$. Thus $v$ and $w$ are linearly independent.
:::
