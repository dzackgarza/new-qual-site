---
schema: qual/card@1
id: P-LD3TY
kind: problem
title: Geometric diagonalisation of a quadratic form
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Diagonalization
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Explain geometrically how you diagonalize a real quadratic form $q(x) = x^t A x$ on $\RR^n$ (Principal Axis Theorem and Gram-Schmidt orthogonalization).
:::

::: {.solution}
Take $A=A^t$, which loses nothing since $x^tAx=x^t\frac{A+A^t}{2}x$.

::: pf

::: {.pf-step #principal-axes}
There is an orthogonal matrix $Q=[v_1\ \cdots\ v_n]$ with $Q^tAQ=\diag(\lambda_1,\ldots,\lambda_n)$, and in the coordinates $x=Qy$,
$$
q(x)=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
$$

::: pf-proof
This is the principal axis theorem. Geometrically: the maximum of $q$ on the Euclidean unit sphere is attained at some $v_1$, and the Lagrange condition there is $Av_1=\lambda_1v_1$. The orthogonal complement $v_1^\perp$ is $A$-invariant, since $Av\cdot v_1=v\cdot Av_1=\lambda_1\,v\cdot v_1=0$ for $v\perp v_1$, so the argument repeats on $v_1^\perp$. The resulting orthonormal eigenvectors are the principal axes, and the change of coordinates $x=Qy$ is a rotation or reflection that removes the cross terms.
:::

:::

::: pf-step
The eigenvalues describe the level sets of $q$ along the principal axes.

::: pf-proof
By step [](#principal-axes){.pf-ref}, if every $\lambda_i>0$ then $q=1$ is an ellipsoid whose semiaxis along $v_i$ has length $1/\sqrt{\lambda_i}$. Positive and negative eigenvalues give the directions in which $q=1$ is elliptic and hyperbolic, and zero eigenvalues give directions along which the level set is a cylinder.
:::

:::

::: pf-step
Without orthogonality of the change of coordinates, Gram--Schmidt orthogonalization for the symmetric bilinear form $B(x,y)=x^tAy$ diagonalizes $q$, and by Sylvester's law of inertia an invertible change of coordinates brings $q$ to
$$
y_1^2+\cdots+y_s^2-y_{s+1}^2-\cdots-y_{s+r}^2,
$$
where $s$, $r$ and $n-s-r$ are invariants of $q$.

::: pf-proof
Gram--Schmidt with respect to $B$ in place of the dot product produces a $B$-orthogonal basis $w_1,\ldots,w_n$; this is completing squares, and it requires choosing at each stage a vector with $B(w,w)\ne0$ whenever $B$ is nonzero on the remaining complement. In that basis $q=\sum B(w_i,w_i)y_i^2$, and rescaling each $w_i$ with $B(w_i,w_i)\ne0$ by $\abs{B(w_i,w_i)}^{-1/2}$ gives the displayed normal form. Sylvester's law states that $s$ and $r$, the numbers of positive and negative coefficients, do not depend on the basis; in the coordinates of step [](#principal-axes){.pf-ref} they are the numbers of positive and negative eigenvalues of $A$.
:::

:::

:::

:::
