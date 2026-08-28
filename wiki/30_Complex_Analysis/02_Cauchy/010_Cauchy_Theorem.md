---
order: 10
---

# Cauchy-Goursat

[[D-6DAXB]]

[[T-2OVCI]]

[[FT-5JQUR]]

:::{.slogan}
Closed path integrals of holomorphic functions vanish.

:::

## Applications of Cauchy's Theorem

### Integral Formulas and Estimates
> See [reference](http://home.iitk.ac.in/~psraj/mth102/lecture_notes/comp8.pdf)
[[T-6DEUH]]

:::{.proof}
![image_2021-05-27-16-54-06](../../../../assets/assets/figures/image_2021-05-27-16-54-06.png)

:::
:::{.proof}
![image_2021-05-27-16-56-39](../../../../assets/assets/figures/image_2021-05-27-16-56-39.png)
![image_2021-05-27-16-56-52](../../../../assets/assets/figures/image_2021-05-27-16-56-52.png)

:::
[[T-22RQZ]]

:::{.proof title="of Cauchy's inequality"}
\envlist
- Given $z_0\in \Omega$, pick the largest disc $D_R(z_0) \subset \Omega$ and let $C = \bd D_R$.
- Then apply the integral formula.

\[
\left|f^{(n)}(z_0)\right|
&= \abs{ \frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta) }{(\zeta-z_0)^{n+1}} \dzeta } \\
&=\left|\frac{n !}{2 \pi i} \int_{0}^{2 \pi} \frac{f\left(z_0 + r e^{i \theta}\right) r i e^{i \theta} }{\left(r e^{i \theta}\right)^{n+1}} \dtheta \right| \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi}\left|\frac{f\left( z_0 +r e^{i \theta}\right) r i e^{i \theta}}{\left(r e^{i \theta}\right)^{n+1}}\right| \dtheta \\
&=\frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{\left|f\left(z_0 +r e^{i \theta}\right)\right|}{r^{n}} \dtheta \\
&\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{M}{r^{n}} \dtheta \\
&=\frac{M n !}{r^{n}}
.\]

:::
:::{.slogan}
The $n$th Taylor coefficient of an analytic function is at most $\sup_{\abs z = R} \abs{f}/R^n$.

:::
[[T-5BLYU]]

### Liouville
[[T-QHIHJ]]

:::{.proof title="of Liouville"}
\envlist

- Since $f$ is bounded, $f(z) \leq M$ uniformly on $\CC$.
- Apply Cauchy's estimate for the 1st derivative:
\[
\abs{f'(z)} \leq { 1! \norm{f}_{C_R} \over R } \leq {M \over R}\converges{R\to\infty}\too 0
,\]
  so $f'(z) = 0$ for all $z$.

:::
[[E-FZLDN]]

### Continuation Principle
[[T-RGE7C]]

:::{.slogan}
Two functions agreeing on a set with a limit point are equal on a domain.

:::
:::{.proof}
Apply Improved Taylor Theorem?

:::
[[E-IYBZP]]

## Exercises
[[E-NKDKF]]
[[E-XXZVG]]
[[E-NSN6G]]

:::{.proof title="of Cauchy"}
Apply Stokes':
\[
\oint_{\partial D} f(z) d z=\int_{D} d(f(z) d z)=\int_{D}\left(\frac{\partial f}{\partial z} d z+\frac{\partial f}{\partial \bar{z}} d \bar{z}\right) \wedge d z=\int_{D} \frac{\partial f}{\partial z} d z \wedge d z+0 d \bar{z} \wedge d z=0
.\]

:::

# Cauchy's Theorem

## Complex Integrals
[[D-6DAXB]]
