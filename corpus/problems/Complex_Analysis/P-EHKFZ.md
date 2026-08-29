---
schema: qual/card@1
id: P-EHKFZ
kind: problem
title: Area of $f(\{r<|z|<R\})$ is $\pi\sum_{n=-\infty}^\infty n|c_n|^2(R^{2n}-r^{2n})$
  for a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f(z) = \sum_{n=-\infty}^\infty c_n z^n$ be analytic and one-to-one (univalent) in the open annulus $r_0 < |z| < R_0$.
For $r_0 < r < R < R_0$, let $D(r, R) = \{z \in \mathbb{C} \mid r < |z| < R\}$ be the concentric sub-annulus.
Prove that the area $S$ of the image domain $f(D(r, R))$ is finite and given by the series formula:
$$S = \pi \sum_{n=-\infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$
:::

::: solution
**Goal:** Compute $\operatorname{Area}(f(D(r, R))) = \iint_{D(r, R)} |f'(z)|^2 \, dx dy$ using polar coordinates and Fourier orthogonality.

<1>1. Area Formula for Injective Holomorphic Maps:
    *Proof:*
    <2>1. Since $f$ is analytic, viewing $f$ as a mapping from $\mathbb{R}^2 \to \mathbb{R}^2$, the real Jacobian determinant is:
        $$J_f(z) = u_x v_y - u_y v_x = u_x^2 + v_x^2 = |f'(z)|^2.$$
    <2>2. Because $f$ is **one-to-one** (univalent) on $D(r, R)$, the Change of Variables Formula gives the exact area of the image $f(D(r, R))$ without double counting:
        $$S = \operatorname{Area}(f(D(r, R))) = \iint_{D(r, R)} |f'(z)|^2 \, dx \, dy.$$

<1>2. Complex Derivative and Fourier Series on Circles:
    *Proof:*
    <2>1. Differentiating the Laurent series term-by-term (valid by uniform convergence on compact sub-annuli):
        $$f'(z) = \sum_{n=-\infty}^\infty n c_n z^{n-1}.$$
    <2>2. In polar coordinates $z = \rho e^{i\theta}$ where $\rho \in (r, R)$ and $\theta \in [0, 2\pi)$:
        $$f'(\rho e^{i\theta}) = \sum_{n=-\infty}^\infty n c_n \rho^{n-1} e^{i(n-1)\theta}.$$
    <2>3. The squared magnitude is:
        $$|f'(\rho e^{i\theta})|^2 = f'(\rho e^{i\theta}) \overline{f'(\rho e^{i\theta})} = \left( \sum_{n=-\infty}^\infty n c_n \rho^{n-1} e^{i(n-1)\theta} \right) \left( \sum_{m=-\infty}^\infty m \bar{c}_m \rho^{m-1} e^{-i(m-1)\theta} \right).$$

<1>3. Angular Integration and Orthogonality of Exponentials:
    *Proof:*
    <2>1. Integrating with respect to $\theta$ from $0$ to $2\pi$:
        $$\int_0^{2\pi} e^{i(n - m)\theta} \, d\theta = 2\pi \delta_{n, m} = \begin{cases} 2\pi & \text{if } n = m, \\ 0 & \text{if } n \ne m. \end{cases}$$
    <2>2. Applying this orthogonality relation (Parseval's identity):
        $$\int_0^{2\pi} |f'(\rho e^{i\theta})|^2 \, d\theta = 2\pi \sum_{n=-\infty}^\infty n^2 |c_n|^2 \rho^{2n-2}.$$

<1>4. Radial Integration:
    *Proof:*
    <2>1. Now integrate with respect to $\rho$ from $r$ to $R$ using the area element $dx \, dy = \rho \, d\rho \, d\theta$:
        $$S = \int_r^R \rho \left( \int_0^{2\pi} |f'(\rho e^{i\theta})|^2 \, d\theta \right) d\rho = 2\pi \sum_{n=-\infty}^\infty n^2 |c_n|^2 \int_r^R \rho^{2n-1} \, d\rho.$$
    <2>2. We evaluate the definite radial integral:
        - For $n \ne 0$:
          $$\int_r^R \rho^{2n-1} \, d\rho = \left[ \frac{\rho^{2n}}{2n} \right]_r^R = \frac{R^{2n} - r^{2n}}{2n}.$$
        - For $n = 0$: the factor $n^2 |c_n|^2 = 0 \cdot |c_0|^2 = 0$, so the $n=0$ term contributes $0$ (which also matches $\lim_{n \to 0} n \frac{R^{2n} - r^{2n}}{2n} = 0$).
    <2>3. Substituting this into the sum:
        $$S = 2\pi \sum_{n=-\infty}^\infty n^2 |c_n|^2 \left( \frac{R^{2n} - r^{2n}}{2n} \right) = \pi \sum_{n=-\infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$

<1>5. Finiteness of Area:
    *Proof:*
    <2>1. Because $f$ is analytic on the slightly larger open annulus $r_0 < |z| < R_0$, the Laurent series converges absolutely on $|z| = r$ and $|z| = R$, ensuring geometric decay of coefficients and absolute convergence of the series.

<1>6. Conclusion:
    The area is given by $S = \pi \sum_{n=-\infty}^\infty n |c_n|^2 (R^{2n} - r^{2n})$. Q.E.D.
:::
