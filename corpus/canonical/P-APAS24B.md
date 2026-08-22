---
schema: qual/card@1
id: P-APAS24B
kind: problem
title: Gershgorin disks contain every eigenvalue
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
solved: false
---

::: problem
Let $A=(a_{ij})\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ and define the sets
\[
D_i=\Biggl\{\beta\in\mathbb{C}\ \Biggm|\ |\beta-a_{ii}|\le\sum_{\substack{j=1\\ j\neq i}}^{n}|a_{ij}|\Biggr\}\subseteq\mathbb{C},
\]
for $1\le i\le n$. Given any eigenvalue $\lambda$ of $A$, prove
\[
\lambda\in\bigcup_{i=1}^{n}D_i.
\]
:::
