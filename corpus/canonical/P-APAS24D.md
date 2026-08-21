---
schema: qual/card@1
id: P-APAS24D
kind: problem
title: Diagonal similarity making a matrix norm close to the spectral radius
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Given an upper triangular matrix $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ and $\varepsilon\in\mathbb{R}$, $\varepsilon>0$, prove there exists $\eta\in\mathbb{R}$, $\eta>0$, such that the diagonal matrix $D=(d_{ij})\in M_n(\mathbb{R})=\mathbb{R}^{n\times n}$ with entries
\[
d_{jj}=\eta^{j-1},
\]
for $1\le j\le n$, satisfies
\[
\|A\|\le\rho(A)+\varepsilon,
\]
where the matrix norm $\|\cdot\|$ is defined by
\[
\|B\|=\|D^{-1}BD\|_1
\]
for all $B\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$.
:::
