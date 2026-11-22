---
order: 100
title: Complex arithmetic
topics:
- Complex Numbers
- Roots of Unity
- Geometry
---

# Complex arithmetic

$\CC$ is the field $\RR[x]/(x^2+1)$, and the identification $x+iy\leftrightarrow(x,y)$ makes it the Euclidean plane with an algebra structure: addition is vector addition, and multiplication is a rotation followed by a dilation.

## Identities

::: {.fact title="Conjugate, modulus, and argument"}
For $z,w\in\CC$:
$\bar z = x-iy$, $\abs z^2 = z\bar z$, $z\bar w+\bar zw = 2\Re(z\bar w)$, $\abs{zw} = \abs z\abs w$, and $\abs{z+w}\leq\abs z+\abs w$ with equality exactly when one of $z,w$ is a nonnegative real multiple of the other.
If $z\neq0$ then $z = re^{i\theta}$ with $r = \abs z$ and $\theta = \arg z$ defined modulo $2\pi$, and multiplication reads $r_1e^{i\theta_1}\cdot r_2e^{i\theta_2} = r_1r_2e^{i(\theta_1+\theta_2)}$.
The triangle $\abs{z-w}\geq\abs{\abs z-\abs w}$ is the reverse triangle inequality, and $\abs{z+w}^2+\abs{z-w}^2 = 2\abs z^2+2\abs w^2$ is the parallelogram law.

The conjugation and modulus identities, including $\abs{z+w}\le\abs z+\abs w$ with its equality case, are [@Ahl73, ch. 1, §1.5, Inequalities], whose (11) is the triangle inequality and which records that equality holds only when one of the two numbers is a nonnegative real multiple of the other; the form $z=re^{i\theta}$ with $\arg z$ modulo $2\pi$, and the addition of arguments under multiplication, are [@Ahl73, ch. 1, §2.1, Geometric Addition and Multiplication], (16)--(17), with the exponential notation itself in [@Ahl73, ch. 2, §3.4, The Logarithm].
:::

## Multiplication as a map of the plane

::: {.fact title="Rotation and dilation"}
Multiplication by $w = \rho e^{i\varphi}\neq0$ is the map $z\mapsto \rho e^{i\varphi}z$, the dilation of ratio $\rho$ composed with the rotation through $\varphi$ about $0$.
It is $\RR$-linear with matrix $\begin{pmatrix}\rho\cos\varphi & -\rho\sin\varphi\\ \rho\sin\varphi & \rho\cos\varphi\end{pmatrix}$ and multiplies every length by $\rho$ and every oriented angle by adding $\varphi$.
Conjugation $z\mapsto\bar z$ is the reflection in the real axis; it preserves lengths and reverses oriented angles, so it is not [[D-TM4TE|conformal]].

That multiplication by $w$ is the composition of a dilation and a rotation is [@Ahl73, ch. 1, §2.1, Geometric Addition and Multiplication], which reads the product $r_1r_2\qty{\cos(\varphi_1+\varphi_2)+i\sin(\varphi_1+\varphi_2)}$ as the dilation of ratio $r_2$ followed by the rotation through $\varphi_2$; the matrix is that map in real coordinates.
:::

::: {.example title="The circle group and $n$-th roots"}
The unit circle $S^1 = \theset{z : \abs z = 1}$ is a group under multiplication, isomorphic to $\RR/2\pi\ZZ$ by $\theta\mapsto e^{i\theta}$.
Its elements of order dividing $n$ are the $n$-th roots of unity $\zeta_n^k = e^{2\pi i k/n}$, which form a cyclic group of order $n$; they are the vertices of a regular $n$-gon inscribed in $S^1$, and their sum is $0$ for $n\geq2$, since $\sum_{k=0}^{n-1}\zeta_n^k = (\zeta_n^n-1)/(\zeta_n-1)$.

The roots of unity as the vertices of a regular $n$-gon are [@Ahl73, ch. 1, §2.2, The Binomial Equation], which solves $z^n=1$ and reads the $n$ solutions as the vertices of a regular polygon; the vanishing of their sum is the geometric-series identity displayed, $\zeta_n\neq1$ for $n\geq2$ and $\zeta_n^n=1$.
:::

## Polynomials over $\CC$

[[T-6XDRA]]

[[T-QDRTC]]

## Problems on complex arithmetic

[[P-UGA8150S21-HW1-01]]

[[P-UGA8150S21-HW1-02]]

[[P-UGA8150S21-HW1-03]]

[[P-CZ3R7]]

[[P-UGA8150S21-HW1-05]]

[[P-37Z7J]]

[[P-AG7QC]]

## Problems on holomorphy and power series

[[P-UGA8150S21-HW1-07]]

[[P-UGA8150S21-HW1-08]]

[[P-IOUZO]]

[[E-SS2.EX-10]]

[[P-JHUU67CA1]]

[[E-SS2.EX-14]]

[[P-7UIYI]]

[[P-V7ULH]]
