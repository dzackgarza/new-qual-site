---
schema: qual/card@1
id: P-MMAQ-WEZIH3QOMQ
kind: problem
title: $F[[x]]$ is a Euclidean domain, and Euclidean domains are PIDs
classification:
  areas:
  - algebra
  topics:
  - rings
relations: []
review: draft
solved: false
---

::: problem
An integral domain $R$ is said to be an *Euclidean domain* if there
is a function $N: R \to \{n\in\mathbb{Z} \mid n\geq 0\}$ such that
$N(0)=0$ and for each $a,b\in R$ with $b\neq 0$, there exist
elements $q,r\in R$ with
`\begin{align*}
  a = qb + r, \quad \text{and} \quad r = 0 \, \text{ or } \, N(r) < N(b).
\end{align*}`{=tex}

Prove:

1.  The ring $F[[x]]$ of power series over a field $F$ is an
    Euclidean domain.

2.  Every Euclidean domain is a PID.
:::
