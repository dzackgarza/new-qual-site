---
schema: qual/card@1
id: P-RAF25E
kind: problem
title: "Translations of an L^2 function with nonvanishing Fourier transform span a dense subspace"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - L2 Spaces
  - Density
relations: []
review: draft
solved: false
---

::: problem
Let $f \in L^2(\mathbb{R}^n)$ such that $\hat{f}(\xi) \neq 0$ for a.e. $\xi \in \mathbb{R}^n$.
For $a \in \mathbb{R}^n$, let $f_a \in L^2(\mathbb{R})$ be given by $f_a(x) = f(x - a)$.

(1) Prove that if $a \in \mathbb{R}^n$, then $\hat{f_a}(\xi) = e^{-2\pi i \xi \cdot a} \hat{f}(\xi)$ for a.e. $\xi \in \mathbb{R}^n$.
(You can use without proof the fact that this identity holds if $f \in L^1(\mathbb{R})$.)

(2) Prove that the linear span of $\{f_a : a \in \mathbb{R}^n\}$ is dense in $L^2(\mathbb{R}^n)$.
:::
