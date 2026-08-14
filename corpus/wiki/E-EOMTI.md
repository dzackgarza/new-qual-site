---
schema: qual/card@1
id: E-EOMTI
kind: exercise
title: "$\\log(x) / (1+x^2)^2$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - complex-logarithm
relations: []
review: draft
---
:::{.exercise title="$\log(x) / (1+x^2)^2$"}
\[
I\da \int_0^\infty {\log(x) \over (1+x^2)^2}\dx = -{\pi \over 4}
.\]

:::

:::{.solution title="Semicircle, real reduction trick"}
Let $f$ be the integrand, then $f\sim \log(z)/(z^4+1)$, so an indented semicircular contour will work since $\abs{f}\to 0$ as $\abs{z\to\infty}$, and the inner integral will be dominated by a term of the form $\eps\log(\eps)/\eps^4\to 0$ as $\eps\to 0$.
So take such a contour, branch cutting along $\theta = -\pi/2$:

![](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-22_05-21-05.png)

Now consider the contribution from $\gamma_2$:
\[
\int_{\gamma_2} f(z) \dz 
&= \int_{-R}^{-\eps} f(t+0i) \dt \\
&= \int_{-R}^{-\eps} {\log(t) \over (t^2 + 1)^2 }\dt \\
&= -\int_{R}^{\eps} {\log(-x) \over ((-x)^2 + 1)^2 }\dx \\
&= \int_{\eps}^{R} {\ln\abs{x} + i\pi  \over (x^2 + 1)^2 }\dx \\
&\to I + i\pi \int_{0}^\infty {1\over (x^2 + 1)^2}\dx
.\]
This auxiliary integral can be handled easily with a usual semicircular contour, since the integrand is $\bigo(x^4)$:
\[
\int_{0}^\infty {1\over (z^2 + 1)}\dx 
&= 2\pi i \sum_{z_k\in \HH}\Res_{z=z_k} {1\over (z^2 + 1)} \\
&= 2\pi i \Res_{z=i} {1\over (z^2 + 1)} \\
&= 2\pi i \lim_{z\to i} \dd{}{z} {1\over (z+i)^2} \\
&= 2\pi i \cdot {-2\over (2i)^3 } \\
&= 2\pi i \cdot {-i\over 4} \\
&= {\pi \over 2}
.\]
Computing the residue of the main integral:
\[
2\pi i \Res_{z=i} f(z) 
&= 2\pi i \lim_{z\to i} \dd{}{z} { \log(z) \over (z+i)^2} \\
&= 2\pi i \lim_{z\to i} { (z+i)^2 z\inv - 2(z+i)\log(z) \over (z+i)^4 } \\
&= 2\pi i { -i(2i)^2 - 2(2i)\qty{i\pi \over 2} \over (2i)^4 } \\
&= \pi i { 2i + \pi \over 2^2 }\\
&= -{\pi \over 2} + {i\pi^2 \over 4}
.\]
Combining all of this:
\[
2\pi i \Res_{z=i} f(z) = \int_\Gamma f(z) \dz = \qty{\int_{\gamma_1} + \int_{ \gamma_2} } f 
= I + \qty{I + {i\pi^2\over 4}} \\
\implies -{\pi \over 2} + {i\pi^2 \over 4} = 2I + {i\pi^2\over 4} \\
\implies -{\pi\over 2} = 2I \\
implies I = -{\pi \over 4}
.\]

:::

:::{.solution title="Log squaring trick"}
Factor $(1+z^2)^2 = (z+i)^2(z-i)^2$.
Apropos of nothing, considering the auxiliary function
\[
g(z) \da \qty{\log(z) \over 1+x^2}^2 = {\log^2(z) \over (1+x^2)^2}
.\]
Use a keyhole contour for a branch cut along $\theta = -\pi$, so $\Arg(z) \in (-\pi, \pi)$:

- $\gamma_+: \ts{t + i\eps \st t \in [-\eps, -R]}$,
- $\gamma_{\eps}: \ts{\eps e^{it} \st t\in [-\pi + \eps, \pi - \eps] }$,
- $\gamma_+: \ts{t - i\eps \st t \in [-\eps, -R]}$,
- $\gamma_{R}: \ts{R e^{it} \st t\in [-\pi + \eps, \pi - \eps] }$,

and $\Gamma$ the combined contour oriented counterclockwise.
Note the symmetry:
\[
\int_{\gamma_+}g(z) 
&= \int_{-R}^{-\eps} { \log^2(t) \over (t^2 +1)^2 } \dt \\
&= - \int_{-eps}^{-R} { \log^2(t) \over (t^2 +1)^2 } \dt \\
&= \int_{\eps}^{R} { \log^2(e^{i\pi} s) \over ( ( e^{i\pi} s)^2 +1)^2 } \ds && t = e^{i\pi}s,\, \ds = -\dt \\
&= \int_{\eps}^{R} { \qty{ \log(s) + i\pi}^2 \over (s^2 +1)^2 } \ds \\
,\]
and similarly
\[
\int_{\gamma_-}g(z) 
&= \int_{-\eps}^{-R} { \log^2(t) \over (t^2 +1)^2 } \dt \\
&= -\int_{\eps}^{R} { \log^2(e^{-i\pi} s) \over ((e^{-i\pi} s)^2 +1)^2 } \ds && t=e^{-i\pi }s,\, \dt = -\ds \\
&= -\int_{\eps}^{R} { \qty{ \log(s) - i\pi}^2 \over (s^2 +1)^2 } \dt \\
.\]
Now note that
\[
(\log(s) + i\pi)^2 - (\log(s) - i\pi)^2 
&= \cdots \\
&= \qty{\log^2(s) + 2i\pi \log(s) - \pi^2 } - \qty{\log^2(s) -2i\pi\log(s) - \pi^2} \\
&= 4i\pi\log(s)
,\]
and so miraculously
\[
\int_{\gamma_+}f(z)\dz + \int_{\gamma_-}f(z)\dz 
&= \int_{\eps}^{R} { \qty{ \log(s) + i\pi}^2 \over (s^2 +1)^2 } \ds - \int_{\eps}^{R} { \qty{ \log(s) - i\pi}^2 \over (s^2 +1)^2 } \dt \\
&= \int_\eps^R { \qty{ \log(s) + i\pi}^2 - \qty{ \log(s) - i\pi}^2  \over (s^2+1)^2 }\ds \\
&= 4i\pi \int_{\eps}^R {\log(s) \over (s^2+1)^2}\ds \\
&\too 4i \pi I
.\]
The contributions from $\gamma_R$ vanish since ${\log(z) \over z^4}\to 0$ as $\abs{z}\to \infty$, and the contribution from $\gamma_\eps$ vanish since ${\eps \log(\eps) \over \eps^4+c}\to 0$ as $\eps \to 0$ (and applying the ML estimate).
Thus
\[
2\pi i \sum_{z_k\in \CC}\Res_{z=z_k}g(z) = \int_\Gamma g(z) \dz = 4i\pi I
.\]
Factoring the denominator as $(1+z^2)^2 = (z-i)^2(z+i)^2$, there are two order 2 poles at $\pm i$.
At $z=i$:
\[
\Res_{z=i}g(z) 
&= \lim_{z\to i} \dd{}{z} {\log^2(z) \over (z+i)^2} \\
&= \lim_{z\to i} {(z+i)^2 2\log(z)z\inv - \log^2(z) 2(z+i) \over (z+i)^4} \\
&= 2^{-4}\qty{(2i)^2 \cdot 2 \cdot {i\pi \over 2} {1\over i} - \qty{i\pi \over 2}^2 \cdot 2 \cdot 2i} \\
&= 2^{-4}\qty{2^3 i^2 {\pi \over 2} - 2^{-2}i^2 \pi^2 2^2 i} \\
&= 2^{-4}\qty{-2^2\pi + i\pi ^2} \\
&= r_1 \da - {\pi \over 4} + i {\pi^2\over 16} 
.\]
Similarly,
\[
\Res_{z=-i}g(z)
&= \lim_{z\to -i} \dd{}{z} {\log^2(z) \over (z+i)^2} \\
&= \lim_{z\to -i} {(z-i)^2 2\log(z) z\inv - \log^2(z) 2(z-i) \over (z-i)^4} \\
&= 2^{-4} \qty{ (-2i)^2 \cdot 2 \qty{-i\pi \over 2}{1\over -i} - \qty{-i\pi\over 2}^2 \cdot 2(-2i) } \\
&= 2^{-4} \qty{ 2^2 i^2 \pi - 2^{-2} \pi^2 (-4i) }\\
&= 2^{-4}\qty{-2^2\pi - \pi^2} \\
&= r_2 \da -{\pi \over 4} - i {\pi^2\over 16}
.\]
Solving for $I$ above, we have
\[
I &= {2\pi i \over 4\pi i}(r_1 + r_2) \\
&= {1\over 2} \qty{- {\pi \over 4} - {\pi \over 4}} \\
&= -{\pi \over 4}
.\]
:::

