---
schema: qual/card@1
id: P-TRIV-RA35
kind: problem
title: Jacobians of spherical and cylindrical coordinates
classification:
  areas: [real-analysis]
  topics:
  - Jacobians
  - Change of Variables
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 35, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find Jacobi matrix and Jacobian for the change of coordinates in $\RR^3$ from Cartesian coordinates to

(a) spherical coordinates,

(b) cylindrical coordinates.

In what regions of $\RR^3$ are these coordinate changes regular?
:::

::: {.solution}

Use spherical coordinates
$$
x=r\sin\theta\cos\varphi,
\qquad
y=r\sin\theta\sin\varphi,
\qquad
z=r\cos\theta,
$$
with
$$
r>0,
\qquad
0<\theta<\pi,
$$
and a local branch of $\varphi$.

::: pf

::: {.pf-step #s1-1}

The Jacobian matrix of the spherical-to-Cartesian map is
$$
\boxed{
\frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)}
=
\begin{pmatrix}
\sin\theta\cos\varphi&r\cos\theta\cos\varphi&-r\sin\theta\sin\varphi\\
\sin\theta\sin\varphi&r\cos\theta\sin\varphi&r\sin\theta\cos\varphi\\
\cos\theta&-r\sin\theta&0
\end{pmatrix}.
}
$$


::: pf-proof

Differentiate the three coordinate formulas with respect to
$r,\theta,\varphi$.

:::

:::

::: {.pf-step #s1-2}

Its determinant is
$$
\boxed{r^2\sin\theta}.
$$


::: pf-proof

The three column vectors are
$$
e_r,
\qquad
r e_\theta,
\qquad
r\sin\theta\,e_\varphi,
$$
where $e_r,e_\theta,e_\varphi$ form a positively oriented orthonormal frame.
Their determinant is therefore
$$
1\cdot r\cdot r\sin\theta
=
r^2\sin\theta.
$$

:::

:::

::: {.pf-step #s1-3}

Hence the spherical coordinate change is locally regular exactly where
$$
r>0
\qquad\text{and}\qquad
\sin\theta\neq0.
$$


::: pf-proof

By the inverse function theorem, local regularity is equivalent to nonzero
Jacobian determinant. Step [](#s1-2){.pf-ref} vanishes precisely at $r=0$ or
$\theta=0,\pi$.

:::

:::

::: {.pf-step #s1-4}

In Cartesian language, the singular set for spherical coordinates is
the $z$-axis.


::: pf-proof

The conditions $\theta=0$ and $\theta=\pi$ describe the positive and negative
$z$-axes, while $r=0$ is their common origin. Away from the $z$-axis, a local
branch of the azimuthal angle $\varphi$ may be chosen smoothly.

:::

:::

::: {.pf-step #s1-5}

The inverse Jacobian matrix, from Cartesian to spherical coordinates, is
$$
\boxed{
\frac{\partial(r,\theta,\varphi)}{\partial(x,y,z)}
=
\begin{pmatrix}
\sin\theta\cos\varphi&\sin\theta\sin\varphi&\cos\theta\\
\dfrac{\cos\theta\cos\varphi}{r}&\dfrac{\cos\theta\sin\varphi}{r}&-\dfrac{\sin\theta}{r}\\
-\dfrac{\sin\varphi}{r\sin\theta}&\dfrac{\cos\varphi}{r\sin\theta}&0
\end{pmatrix}.
}
$$


::: pf-proof

This matrix is the inverse of the matrix in step [](#s1-1){.pf-ref}. Equivalently, its rows
are the gradients of $r$, $\theta$, and $\varphi$ in Cartesian coordinates.

:::

:::

::: {.pf-step #s1-6}

Its determinant is
$$
\boxed{\frac1{r^2\sin\theta}}.
$$


::: pf-proof

The determinant of an inverse matrix is the reciprocal of the original
determinant from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For cylindrical coordinates, use
$$
x=\rho\cos\varphi,
\qquad
y=\rho\sin\varphi,
\qquad
z=z,
$$
with $\rho>0$ and a local branch of $\varphi$.


::: pf-proof

These are the standard cylindrical coordinate formulas.

:::

:::

::: {.pf-step #s1-8}

The cylindrical-to-Cartesian Jacobian matrix is
$$
\boxed{
\frac{\partial(x,y,z)}{\partial(\rho,\varphi,z)}
=
\begin{pmatrix}
\cos\varphi&-\rho\sin\varphi&0\\
\sin\varphi&\rho\cos\varphi&0\\
0&0&1
\end{pmatrix}.
}
$$


::: pf-proof

Differentiate the coordinate formulas from step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Its determinant is
$$
\boxed{\rho}.
$$


::: pf-proof

The determinant of the upper-left $2\times2$ block is
$$
\rho(\cos^2\varphi+\sin^2\varphi)
=
\rho,
$$
and the last diagonal entry is $1$.

:::

:::

::: {.pf-step #s1-10}

Hence cylindrical coordinates are locally regular exactly where
$$
\rho>0,
$$
that is, away from the $z$-axis.


::: pf-proof

Apply the inverse function theorem to the determinant in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The inverse Cartesian-to-cylindrical Jacobian matrix is
$$
\boxed{
\frac{\partial(\rho,\varphi,z)}{\partial(x,y,z)}
=
\begin{pmatrix}
\cos\varphi&\sin\varphi&0\\
-\dfrac{\sin\varphi}{\rho}&\dfrac{\cos\varphi}{\rho}&0\\
0&0&1
\end{pmatrix},
}
$$
with determinant
$$
\boxed{\frac1\rho}.
$$


::: pf-proof

Invert the matrix from step [](#s1-8){.pf-ref}, or differentiate
$$
\rho=\sqrt{x^2+y^2},
\qquad
\varphi=\operatorname{atan2}(y,x).
$$
The determinant is the reciprocal of step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} solve the spherical case, and steps [](#s1-7){.pf-ref} through [](#s1-11){.pf-ref} solve the
cylindrical case and identify the regular regions.

:::

:::

:::
