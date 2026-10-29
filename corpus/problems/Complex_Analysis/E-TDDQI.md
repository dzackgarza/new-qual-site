---
schema: qual/card@1
id: E-TDDQI
kind: problem
title: Area of the image of an annulus under a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
---

::: {.problem}
Let $f(z) = \sum_{n= -\infty}^\infty c_n z^n$ be analytic and one-to-one in $r_0< \abs{z} < R_0$.
For $r_0<r<R<R_0$, let $D(r,R)$ be the annulus $r<\abs{z}<R$.
Show that the area of $f(D(r,R))$ is finite and is given by $$S = \pi \sum_{n=- \infty}^\infty n \abs{c_n}^2 (R^{2n} - r^{2n}).$$
:::

::: {.solution}

::: pf

::: {.pf-step #jacobian}
The area of $f(D(r,R))$ is $\iint_{D(r,R)}\abs{f'(z)}^2\,dA(z)$.

::: pf-proof
$f$ is an injective holomorphic map, so it is a diffeomorphism of $D(r,R)$ onto its image, and its real Jacobian determinant is $u_xv_y-u_yv_x = u_x^2+v_x^2 = \abs{f'}^2$ by the Cauchy--Riemann equations. Apply the change of variables formula.
:::

:::

::: {.pf-step #parseval}
For $r\leq\rho\leq R$, $\int_0^{2\pi}\abs{f'(\rho e^{i\theta})}^2\dtheta = 2\pi\sum_{n\in\ZZ} n^2\abs{c_n}^2\rho^{2n-2}$.

::: pf-proof
$f'(z) = \sum_n nc_nz^{n-1}$, and this Laurent series converges absolutely and uniformly on the compact annulus $r\leq\abs{z}\leq R$, which lies inside $r_0<\abs{z}<R_0$. So on $\abs{z}=\rho$ we may multiply out $f'\,\overline{f'}$ and integrate term by term; the orthogonality relation $\int_0^{2\pi}e^{i(n-m)\theta}\dtheta = 2\pi\delta_{nm}$ leaves only the diagonal terms.
:::

:::

::: pf-step
The area of $f(D(r,R))$ is $\pi \sum_{n} n \abs{c_n}^2 (R^{2n} - r^{2n})$, and it is finite.

::: pf-proof
In polar coordinates, step [](#jacobian){.pf-ref} and step [](#parseval){.pf-ref} give
$$
S = \int_r^R 2\pi\sum_n n^2\abs{c_n}^2\rho^{2n-1}\,d\rho = \sum_{n\neq 0} 2\pi n^2\abs{c_n}^2\,\frac{R^{2n}-r^{2n}}{2n} = \pi\sum_n n\abs{c_n}^2(R^{2n}-r^{2n}),
$$
where the interchange of sum and integral holds by Tonelli's theorem, since every term is nonnegative, and the $n=0$ term vanishes. The area is finite because $\abs{f'}^2$ is continuous on the compact closed annulus, hence bounded there.
:::

:::

:::

:::
