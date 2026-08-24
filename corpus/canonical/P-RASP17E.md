---
schema: qual/card@1
id: P-RASP17E
kind: problem
title: "Dilations of R^2 act isometrically on L^2 and continuously as t approaches 1"
classification:
  areas:
  - real-analysis
  topics:
  - L2 Spaces
  - Change of Variables
  - Density Arguments
relations: []
review: draft
---

::: problem
For $t > 0$, let $A_t = \begin{pmatrix} t & 0 \\ 0 & t^{-1} \end{pmatrix}$ and for $f : \mathbb{R}^2 \to \mathbb{C}$ let $T_t f(x) = f(A_t x)$ for $x \in \mathbb{R}^2$.

1. Show $\|T_t f\|_2 = \|f\|_2$ for all $f \in L^2(\mathbb{R}^2, m)$.

2. Explain why $\lim_{t \to 1} \|T_t f - f\|_2 = 0$ for all $f \in C_c(\mathbb{R}^2)$.

3. Show $\lim_{t \to 1} \|T_t f - f\|_2 = 0$ for all $f \in L^2(\mathbb{R}^2, m)$.
:::
