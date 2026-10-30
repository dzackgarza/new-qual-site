---
schema: qual/card@1
id: T-TUXBP
kind: theorem
title: Implicit function theorem
slogan: 'An invertible derivative block in the solved-for variables makes the zero set locally a unique $C^r$ graph.'
classification:
  areas:
  - complex-analysis
  - real-analysis
  topics:
  - Calculus
relations: []
review: draft
---

::: {.theorem}
Let $k,n\geq1$ and $r\geq1$, let $A\subseteq\RR^{k+n}$ be open, and let $f\colon A\to\RR^n$ be of class $C^r$.
Write $f(\vector x,\vector y)$ with $\vector x\in\RR^k$ and $\vector y\in\RR^n$, so that
$$
Df=\begin{bmatrix}\dfrac{\partial f}{\partial\vector x} & \dfrac{\partial f}{\partial\vector y}\end{bmatrix}
$$
splits into an $n\times k$ block and an $n\times n$ block.
Suppose $(\vector a,\vector b)\in A$ satisfies $f(\vector a,\vector b)=0$ and
$$
\det\frac{\partial f}{\partial\vector y}(\vector a,\vector b)\neq0.
$$
Then there are a connected open neighbourhood $B\subseteq\RR^k$ of $\vector a$ and a unique continuous $g\colon B\to\RR^n$ with $g(\vector a)=\vector b$ and
$$
f(\vector x,g(\vector x))=0\quad\text{for all }\vector x\in B,
$$
and this $g$ is of class $C^r$ [@Mun91, Section 9, Theorem 9.2].
:::

::: {.remark}
Differentiating $f(\vector x,g(\vector x))=0$ gives [@Mun91, Theorem 9.1]
$$
\frac{\partial f}{\partial\vector x}+\frac{\partial f}{\partial\vector y}\,Dg=0,
\qquad\text{so}\qquad
Dg(\vector x)=-\Bigl[\frac{\partial f}{\partial\vector y}(\vector x,g(\vector x))\Bigr]^{-1}\frac{\partial f}{\partial\vector x}(\vector x,g(\vector x)).
$$
:::
