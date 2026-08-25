---
schema: qual/card@1
id: P-IV4XE
kind: problem
title: $\int_{\RR}\frac{e^{i\xi x}}{\cosh x}\,dx$ for $\xi\in\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
---

:::{.problem}
Let $\xi\in \RR$, evaluate
\[
\int_\RR {e^{i\xi x} \over \cosh(x)} \dx
.\]

:::

:::{.solution}
Note $\cosh(z) \da {1\over 2}(e^z + e^{-z})$, and
\[
\cosh(z) &= 0 \\
\iff e^z + e^{-z} &= 0 \\
\iff e^{-z}(e^{2z} + 1) &= 0 \\
\iff e^{2z} &= -1 \quad \text{since }\abs{e^{-z}} = e^{\Re(z)} > 0 \\
\iff 2z &= (2k+1)i\pi \\
\iff z &\in \ts{\cdots, {-3i\pi \over 2}, {-i\pi \over 2}, {i\pi \over 2}, {3i\pi \over 2}, \cdots}
.\]
So take the following rectangular contour enclosing the singularity $z= i\pi/2$:

![](../../assets/30_Complex_Analysis/999_Quals/figures/2021-11-11_22-15-56.png)

Then letting $\Gamma$ be the entire contour and $I$ be the desired integral, we can solve for $I$:
\[
\int_\Gamma f &= \int_{-R}^R f + \int_{\gamma_{R_1}} f + \int_{\gamma_2}f + \int_{\gamma_{R_2}} f \\
\int_\Gamma f &= I + \int_{\gamma_{R_1}} f + \int_{\gamma_2}f + \int_{\gamma_{R_2}} f \\ \\
I &= \int_{\gamma_{R_1}} f + \int_{\gamma_2}f + \int_{\gamma_{R_2}} f - \int_\Gamma f 
,\]
being very sloppy about the fact that we're going to take $R\to \infty$.

Computing the residue term $\int_\Gamma f = 2\pi i \Res_{z=i\pi/2} f(z)$:
\[
{1\over 2\ pi i } \int_\Gamma f 
&= \Res_{z = i\pi/2} f(z)\\
&= \Res_{z = i\pi/2} {e^{i\xi z} \over \cosh(z) } \\
&= {e^{i\xi z} \over \dd{}{t} \cosh(z) } \evalfrom_{i\pi/2}\\
&= {e^{i\xi \cdot i\pi/2} \over \sinh(i\pi/2)} \\
&= {e^{-\xi \pi/ 2} \over i} \\
\implies 2\pi i \Res_{z=i\pi/2} f(z) &= 2\pi e^{-\xi \pi/ 2}
.\]
using that $2\sinh(i\pi/2) = e^{i\pi/2} - e^{-i\pi/2} = i-(-i) = 2i$. 

The $\gamma_2$ term:
parameterize $\gamma_2 = \ts{t + i\pi \st t\in [-R, R]}$, then
\[
\int_{\gamma_2} f 
&= -\int_{-\gamma_2} f \\
&= -\int_{-R}^{R} { e^{iz} \over \cosh(t + i\pi) } \dz, \quad z = t+i\pi, \dz = \dt \\
&= -\int_{-R}^{R} { e^{i\xi(t+i\pi)} \over \cosh(t + i\pi) }\dt \\
&= -e^{-\xi \pi} \int_{-R}^R {e^{i\xi t} \over \cosh(t+i\pi)} \dt \\
&= e^{-\xi \pi} \int_{-R}^R {e^{i\xi t} \over \cosh(t)} \dt \\
&\da e^{-\xi \pi} I
,\]
using that $\cosh(z + i\pi) = -\cosh(z)$.

The two $\gamma_{R_i}$ terms:
the claim is that these vanish in the limit $R\to \infty$.
Parameterize $\gamma_{R_2} = \ts{R = i \pi t \st t\in [0, 1]}$, then
\[
\abs{\int_{\gamma_{R_2}} f} 
&= \abs{ \int_0^1 {e^{i\xi(R+i\pi t)} \over \cosh(R + i\pi t)} \dt } \\
&= \abs{ 2e^{i\xi R} \int_0^1 {e^{-\xi \pi t } \over {e^{R+ i\pi t} + e^{-R - i\pi t}} } \dt } \\
&\leq 2 \int_0^1 \abs{ {e^{-\xi \pi t } \over {e^{R+ i\pi t} + e^{-R - i\pi t}} }  } \dt \\
&\leq 2 \int_0^1 {e^{-\xi \pi t } \over { \abs{ e^{R+ i\pi t} }  -  \abs{ e^{-R - i\pi t} } }  }\dt \\
&= 2 \int_0^1 {e^{-\xi\pi t} \over e^R - e^{-R} } \\
&= { 2\over e^R - e^{-R}} \int_0^1 e^{-\xi \pi t} \dt \\
&= {2\over e^R - e^{-R}} \qty{-1\over \xi \pi} e^{\xi \pi t}\evalfrom_{t=0}^{t=1} \\
&= {2\over e^R - e^{-R}} \qty{1 - e^{-\pi \xi } \over \xi \pi} \\
&\convergesto{R\to\infty} 0
.\]

Putting it all together:
\[
(1 + e^{-\xi \pi}) I &= 2\pi e^{-\xi \pi / 2} \\
\implies I &= {2\pi e^{-\xi \pi / 2} \over 1 + e^{-\xi \pi }} \\
&= {2\pi \over e^{\xi\pi/2} (1 + e^{-\xi \pi })} \\
&= {2\pi \over e^{\xi\pi/2} + e^{-\xi\pi/2} } \\
&= {2\pi \over 2\cosh(\xi\pi/2)} \\
&= {\pi \over \cosh\qty{\xi\pi\over 2}} \\ \\
&= \pi \sech\qty{\xi\pi\over 2 } 
.\]

:::



