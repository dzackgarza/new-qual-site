---
schema: qual/card@1
id: P-TRIV-DE43
kind: problem
title: Helmholtz equation in a cube with Dirichlet boundary conditions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 43, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve
$$
(\nabla^2 + k^2)u(x, y, z) = 0 \tag{40}
$$
so that $u = 0$ whenever any of the coordinates is equal to $0$ or $L$. What are the allowed values of $k^2$?
:::

::: {.solution}

Seek a separated nonzero solution
$$
u(x,y,z)=X(x)Y(y)Z(z).
$$

::: pf

::: {.pf-step #s1-1}

Separation of variables gives
$$
\frac{X''}{X}+\frac{Y''}{Y}+\frac{Z''}{Z}+k^2=0.
$$


::: pf-proof

Substitute $XYZ$ into $(\nabla^2+k^2)u=0$ and divide by $XYZ$ wherever it is nonzero. Each of the first three terms depends on only one coordinate.

:::

:::

::: {.pf-step #s1-2}

Write
$$
X''+\alpha^2X=0,
\qquad
Y''+\beta^2Y=0,
\qquad
Z''+\gamma^2Z=0,
$$
with
$$
k^2=\alpha^2+\beta^2+\gamma^2.
$$


::: pf-proof

Since the sum in step [](#s1-1){.pf-ref} is constant, each coordinate-dependent quotient must be constant. Denote the three constants by $-\alpha^2,-\beta^2,-\gamma^2$; their sum must be $-k^2$.

:::

:::

::: {.pf-step #s1-3}

The Dirichlet conditions in the $x$ coordinate require
$$
\alpha=\frac{n_x\pi}{L},
\qquad
X(x)=A\sin\frac{n_x\pi x}{L},
\qquad n_x=1,2,3,\ldots.
$$


::: pf-proof

The conditions $u=0$ on $x=0$ and $x=L$ imply $X(0)=X(L)=0$ for a nonzero separated mode. The standard Dirichlet problem $X''+\alpha^2X=0$ has a nonzero solution exactly when $\sin(\alpha L)=0$ with $\alpha>0$, giving the displayed values and eigenfunctions.

:::

:::

::: {.pf-step #s1-4}

Similarly,
$$
\beta=\frac{n_y\pi}{L},
\qquad
\gamma=\frac{n_z\pi}{L},
\qquad n_y,n_z=1,2,3,\ldots.
$$


::: pf-proof

Apply the argument of step [](#s1-3){.pf-ref} to the pairs of faces $y=0,L$ and $z=0,L$.

:::

:::

::: {.pf-step #s1-5}

Hence the separated eigenmodes are
$$
\boxed{
u_{n_x,n_y,n_z}(x,y,z)=C
\sin\frac{n_x\pi x}{L}
\sin\frac{n_y\pi y}{L}
\sin\frac{n_z\pi z}{L}}
$$
and the allowed values are
$$
\boxed{
k^2=\frac{\pi^2}{L^2}
\left(n_x^2+n_y^2+n_z^2\right),
\qquad n_x,n_y,n_z\in\NN.}
$$


::: pf-proof

Substitute the values from steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} into the relation in step [](#s1-2){.pf-ref}. Each product mode vanishes on all six faces and satisfies the Helmholtz equation. Linear combinations of modes sharing the same value of $k^2$ give the full eigenspace for that eigenvalue.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the Dirichlet modes and every allowed value of $k^2$.

:::

:::

:::
