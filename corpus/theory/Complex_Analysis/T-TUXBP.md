---
schema: qual/card@1
id: T-TUXBP
kind: theorem
title: Implicit function theorem for $C^r$ maps
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
relations:
- kind: related-to
  target: T-QMGPN
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
Then there are a neighbourhood $B\subseteq\RR^k$ of $\vector a$ and a unique continuous $g\colon B\to\RR^n$ with $g(\vector a)=\vector b$ and
$$
f(\vector x,g(\vector x))=0\quad\text{for all }\vector x\in B,
$$
and this $g$ is of class $C^r$.
:::

::: {.remark}
The invertibility hypothesis is on the $n\times n$ block $\partial f/\partial\vector y$ belonging to the variables $\vector y$ being solved for; $Df$ itself is an $n\times(k+n)$ matrix.
Differentiating $f(\vector x,g(\vector x))=0$ gives
$$
\frac{\partial f}{\partial\vector x}+\frac{\partial f}{\partial\vector y}\,Dg=0,
\qquad\text{so}\qquad
Dg(\vector x)=-\Bigl[\frac{\partial f}{\partial\vector y}(\vector x,g(\vector x))\Bigr]^{-1}\frac{\partial f}{\partial\vector x}(\vector x,g(\vector x)).
$$
The proof applies the inverse function theorem to $F(\vector x,\vector y)\coloneqq(\vector x,f(\vector x,\vector y))$, whose derivative at a point is invertible if and only if $\partial f/\partial\vector y$ is invertible there.
:::

::: {.concept}
See Munkres, *Analysis on Manifolds*, §9, Theorem 9.2, p. 71; the derivative formula is Theorem 9.1.
:::
