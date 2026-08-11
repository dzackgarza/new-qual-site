# Cauchy-Goursat

:::{.definition title="Complex Integral"}
\[
\int_{\gamma} f d z:=\int_{I} f(\gamma(t)) \gamma^{\prime}(t) \dt
= \int_\gamma (u+iv)\dx + (-v+iu)\dy
.\]
:::

:::{.theorem title="Cauchy-Goursat Theorem" ref="CauchyTheorem"}
If $f$ is holomorphic on a region $\Omega$ with $\pi_1 \Omega = 1$, then for any closed path $\gamma \subseteq \Omega$,
\[ 
\int_{\gamma} f(z) \dz = 0
.\]
:::

:::{.slogan}
Closed path integrals of holomorphic functions vanish.
:::

## Applications of Cauchy's Theorem
### Integral Formulas and Estimates
> See [reference](http://home.iitk.ac.in/~psraj/mth102/lecture_notes/comp8.pdf)
:::{.theorem title="Cauchy Integral Formula" ref="CauchyIntegral"}
Suppose $f$ is holomorphic on $\Omega$, then for any $z_0 \in \Omega$ and any open disc $\closure{D_R(z_0)}$ such that $\gamma \da \bd \closure{D_R(z_0)} \subseteq \Omega$,
\[
f(z_0) = {1 \over 2\pi i} \int_{\gamma} {f(\xi) \over \xi-z_0}\ \dxi
\]
and
\[
\dd{^nf }{z^n}(z_0) = {n! \over 2\pi i} \int_{\gamma} {f(\xi) \over (\xi - z_0)^{n+1}} \dxi
.\]
:::
:::{.proof title="?"}
![image_2021-05-27-16-54-06](figures/image_2021-05-27-16-54-06.png)

:::
:::{.proof title="?"}
![image_2021-05-27-16-56-39](figures/image_2021-05-27-16-56-39.png)
![image_2021-05-27-16-56-52](figures/image_2021-05-27-16-56-52.png)
:::
:::{.theorem title="Cauchy's Inequality / Cauchy's Estimate" ref="CauchyInequality"}
For $z_0 \in D_R(z_0) \subset \Omega$, setting $M \da \sup_{z\in \gamma}\abs{f(z)}$ so $\abs{f(z)}\leq M$ on $\gamma$
\[
\abs{ f^{(n)} (z_0) }
\leq \frac{n !}{2 \pi} \int_{0}^{2 \pi} \frac{ M } {R^{n+1}} R \dtheta
= \frac{M n ! }{R^n}
.\]
:::
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
:::{.theorem title="Mean Value Property for Holomorphic Functions"}
If $f$ is holomorphic on $D_r(z_0)$
\[
f(z_0)
= {1\over 2\pi} \int_0^{2\pi} f(z_0 + re^{i\theta}) \dtheta
= {1\over \pi r^2} \iint_{D_r(z_0)} f(z)\, dA
.\]
Taking the real part of both sides, one can replace $f=u+iv$ with $u$.
:::
### Liouville
:::{.theorem title="Liouville's Theorem" ref="Liouville"}
If $f$ is entire and bounded, $f$ is constant.
:::
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
:::{.theorem title="Continuation Principle / Identity Theorem"}
If $f$ is holomorphic on a bounded connected domain $\Omega$ and there exists a sequence $\theset{z_i}$ with a limit point in $\Omega$ such that $f(z_i) = 0$, then $f\equiv 0$ on $\Omega$.
:::
:::{.slogan}
Two functions agreeing on a set with a limit point are equal on a domain.
:::
:::{.proof title="?"}
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
:::{.definition title="Complex Integral"}
\[
\int_{\gamma} f d z:=\int_{I} f(\gamma(t)) \gamma^{\prime}(t) \dt
= \int_\gamma (u+iv)\dx \wedge (-v+iu)\dy
.\]
:::
