---
order: 125
---

# Harmonic Functions

## Delbar and the Laplacian

:::{.definition title="Laplacian and Harmonic Functions"}
A real function of two variables $u(x, y)$ is **harmonic** iff it is in the kernel of the Laplacian operator:
\[  
\Delta u \definedas \qty{\dd{^2}{x^2} + \dd{^2}{y^2}}u = 0
.\]
:::

:::{.definition title="del and delbar operators"}
\[
\del \da \del_z \da {1\over 2}\qty{\del_x - i \del_y}
\quad
\text{ and }
\quad
\delbar
\da \del_{\bar z}
={1\over 2}\qty{ \del_x + i\del_y}
.\]
Moreover, the 1-form corresponding to $F$ can be written as 
\[
dF = \del F + \delbar F = \dd{F}{z} \dz + \dd{F}{\zbar}\dzbar
.\]

Written slightly more explicitly:
\[
\dd{F}{z} = {1\over 2}\qty{\dd{F}{x} + {1\over i}\dd{F}{y} } && 
\dd{F}{\zbar} = {1\over 2}\qty{\dd{F}{x} - {1\over i}\dd{F}{y} } 
.\]

:::


:::{.proposition title="Mean Value Property"}
If $u$ is harmonic on $\Omega$ then
\[
u(z_0) = u(x_0 + i y_0) = {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} u \ds = {1\over \pi r^2} \iint_{\DD_r(z_0)} u(x, y) \dx \dy
.\]
:::


:::{.proof title="?"}
Define
\[
F(r) \da {1\over 2\pi r} \oint_{\DD_r(z_0)} u\ds = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it} ) \dt
.\]

Then differentiate:
\[
F'(r) 
&= {1\over 2 \pi} \int_{[-\pi, \pi]} \cos(t) u_x(z_0 +re^{it} ) + \sin(t) u_y(z_0 + re^{it}) \dt \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)}\qty{x-x_0\over r} u_x(x, y) + \qty{y-y_0\over r}u_y(x, y) \ds \\
&= {1\over 2\pi r} \oint_{\bd \DD_r(z_0)} \dd{u}{w} \ds \qquad w = \tv{{x-x_0\over r}, {y-y_0\over r}} \\
&= {1\over 2\pi r} \iiint_{\DD_r(z_0)} \laplacian u \dx \dy \\
&= 0
,\]
where we've used Green's theorem and that $\laplacian u = 0$.
so $F$ is constant.
Take $r\to 1$ to obtain 
\[
F(r) = {1\over 2\pi} \int_{[-\pi, \pi]} u(z_0 + re^{it}) \ds \too \int_{[-\pi, \pi]} u(z_0) \ds = u(z_0) = u(x_0, y_0)
.\]
:::


:::{.remark}
An important use: if $u$ satisfies the mean value property on every disc and is continuous, then $u$ is automatically harmonic.
:::




## Exercises: Harmonic Functions

[[E-P2PEF]]

[[E-TZJKN]]

[[E-I6W47]]

[[E-2AVJU]]

[[E-BQ2JY]]
