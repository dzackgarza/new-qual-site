---
schema: qual/card@1
id: P-CAF06C
kind: problem
title: "Conformal map from a simply connected region to a disk without using the full Riemann mapping theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $Y$ be a simply-connected region contained inside the disk $D = \{z : |z| < 1\}$.
Assume $0 \in Y \neq D$.
Without appealing to the Riemann mapping theorem itself, prove that there exists an $r$ with $1 > r > 0$ and a univalent conformal map $f: Y \to D(r) = \{z : |z| < r\}$ with $f(0) = 0$ and $f'(0) = 1$.

Hint: You may use part of the proof of the Riemann mapping theorem.
:::

::: solution
Choose $a\in\mathbb D\setminus Y$. Since $0\in Y$, we have $a\ne0$. Let
\[
\phi_a(z)=\frac{z-a}{1-\overline a z},
\]
an automorphism of $\mathbb D$ sending $a$ to $0$. The function
$\phi_a$ has no zeros on $Y$. Since $Y$ is simply connected, it has a
holomorphic square root there: choose $q$ with
\[
q(z)^2=\phi_a(z).
\]
Because $\phi_a$ is injective, so is $q$. Also $|q(z)|<1$ on $Y$.

Put $b=q(0)$ and let
\[
\psi_b(w)=\frac{w-b}{1-\overline b w}.
\]
Then
\[
F=\psi_b\circ q:Y\to\mathbb D
\]
is univalent and satisfies $F(0)=0$. Since $b^2=\phi_a(0)=-a$,
$|b|^2=|a|$. Furthermore
\[
|q'(0)|=\frac{|\phi_a'(0)|}{2|b|}
=\frac{1-|a|^2}{2\sqrt{|a|}},
\]
and
\[
|\psi_b'(b)|=\frac1{1-|b|^2}=\frac1{1-|a|}.
\]
Thus
\[
|F'(0)|
=\frac{1+|a|}{2\sqrt{|a|}}>1,
\]
the strict inequality following from $(1-|a|)^2>0$.

Multiply $F$ by a unimodular constant so that $F'(0)=\lambda>1$ is positive
real, and define
\[
f(z)=\frac{F(z)}\lambda,
\qquad r=\frac1\lambda.
\]
Then $0<r<1$, $f$ is univalent and conformal,
\[
f:Y\to D(r),\qquad f(0)=0,\qquad f'(0)=1,
\]
as required.
:::
