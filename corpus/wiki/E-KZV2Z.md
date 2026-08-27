---
schema: qual/card@1
id: E-KZV2Z
kind: exercise
title: $1/x^2+3x+2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

:::{.exercise}
\[
I\da \int_\RR {1\over x^2 + 3x+ 2 }\dx
.\]

 

:::

:::{.solution title="Phantom log trick"}
Note that $f(x) = (x+2)(x+1)$, so the singularities on on $\RR_{< 0}$.
The function isn't even, so a semicircular contour won't work.
Attempting to find a ray-like symmetry only yields one option:
\[
f(z) = f(e^{i\theta } z) \implies \theta = 2k\pi
,\]
which suggests a keyhole.
But since there's no $\log$ in $f$, there's no monodromy, and the contributions cancel out.
So introduce a log with a branch cut along $\theta = 0$, and consider
\[
\int f(z) \log(z)
.\]

![](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-24_04-03-05.png)

Let $\gamma_+ = \ts{t + i\eps \st t\geq 0}$ (right-to left) and $\gamma_0 = \ts{t-i\eps \st t\geq 0}$ (left-to-right).
Now use the general fact
\[
\int_{\gamma_+}f(z)\log(z) \dz &= \int_\eps^R f(t+i\eps)\log(t+i\eps) \dt \too \int_\RR f(t)\log(t)\dt \\
\int_{\gamma_-}f(z)\log(z) \dz &= \int_R^\eps f(t-i\eps)\log(t-i\eps) \dt \too -\int_\RR f(t)\qty{ \log(t) + 2\pi i} \dt \\
,\]
thus 
\[
\int_{\gamma_+}f(z)\log(z)\dz + \int_{\gamma_-}f(z)\log(z) 
&\too \int_0^\infty f(t)\log(t)\dt - \int_0^\infty f(t)(\log(t) + 2\pi i) \dt \\
&= -2\pi i \int_0^\infty f(t) \dt
.\]

By the ML estimate, the semicircular piece vanishes.
Miraculously, since $\lim_{x\to 0}{ x\log(x) \over x^n+c} = 0$ for any $c>0$ and $n\geq 1$, the inner indented pieces goes to zero.
Parameterize by $z= \eps e^{it}$
\[
\int_{C_\eps} f(z)\log(z)\dz
&\approx \int_{\eps}^{2\pi - \eps} {\log(\eps e^{it}) \over \eps^2 + 3\eps + 2} \eps e^{it}\dt \\
&= \int_{\eps}^{2\pi - \eps} {\log(\eps) + it \over \eps^2 + 3\eps + 2} \eps e^{it}\dt \\
&\approx \int_\eps^{2\pi - \eps} {\eps \log(\eps) + c_1 \over \eps^2 + c_2}\dt \\
&\convergesto{\eps\to 0} 0
,\]
where I've been *extremely* sloppy and left out many negligible $e^{it}$ terms.
By the residue theorem,
\[
2\pi i \sum_{z_k\in \CC} \Res_{z=z_k} f(z)\log(z) = \int_\Gamma f(z)\log(z)\dz = -2\pi i\int_\RR f(z)\dz
.\]
There are just two simple poles at $z_1 = -1, z_2 = -2$, so
For $z_1$:
\[
\Res_{z=-1}{\log(z) \over (z+1)(z+2)} 
= \lim_{z\to -1} {\log(z) \over z+2} 
= \log(-1)
,\]
and for $z_2$,
\[
\Res_{z=-2}{\log(z) \over (z+1)(z+2)} 
= \lim_{z\to -2} {\log(z) \over z+1}
= -\log(-2)
.\]

Thus
\[
I 
&= -(\log(-1) - \log(-2)) \\
&= - (\ln(1) + i\pi) + (\ln(2) + i\pi) \\
&= \ln(2)
,\]
noting that we've chosen a branch of $\log(z) \da \ln\qty{\abs{z}} + i\Arg(z)$ where $\Arg(z) \in (0, 2\pi)$.
:::

