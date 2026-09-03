---
schema: qual/card@1
id: E-AIQEU
kind: problem
title: $e^{ax}\operatorname{sech}(z)$
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

:::{.exercise}
\[
I \da \int_\RR {e^{ax} \over \cosh(x) }\dx = \pi \sec\qty{a\pi \over 2} && \abs{\Re(a)} < 1
.\]

:::

:::{.solution}
Heuristically, $\int e^{ax} \sech(x)$ should converge since $\sech(x) \sim e^{-x}$, so $\abs{f} \sim \abs{e^{(a-1)x}}\sim e^{\Re(a-1)x} \sim e^{-x}$ when $\Re(a-1)$ is negative, so $\Re(a) < 1$.

We'll need a contour along $\RR$, so immediate options are a semicircular contour or a rectangle.
A semicircular contour is not a good idea here, since there are infinitely many poles of this function:
\[
\cosh(z) = 0 \implies e^z + e^{-z} = 0 \implies e^{2z} = -1 \implies z = {i\pi \cdot k \over 2}
.\]
It turns out the residues at these poles are all 1, the residue theorem would yield a divergent series.
So take the rectangle contour with one side long $\RR$ and one along $\ts{t+ib \st t\in [-R, R]}$ respectively, where we'll choose $ib$ so that the two integrals differ by a scalar.
Computing the symmetry by looking at $f(z+ib)$:
\[
{e^{a(z+ib)} \over \cosh(z+ib)} 
= e^{aib} {e^{z} \over e^z e^{ib} + e^{-z} e^{-ib} }
,\]
and we now need $e^{ib} = e^{-ib}$ in order to scale it out.
Noting that if $z\da e^{ib}$ then $\bar{z} = e^{-ib}$, this forces $z\in \RR$, so $z=\pm 1$.
Taking $z=+1$ forces $b=0$, which is the original contour, so taking $z=-1$ yields $b=\pi i$.
So we take the following contour:

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-16-12.png)

Computing the integral on the upper contour:
\[
\int_{\gamma_1} f(z) \dz 
&= \int_R^{-R} f(t+ib) \dt \qquad z=t+ib, \dz = \dt \\
&= - \int_{-R}^R f(t+ib) \dt \\
&= - \int_{-R}^R {e^{a(t+i\pi)} \over \cosh(t+i\pi ) } \dt \\
&= - \int_{-R}^R e^{ai\pi} {e^{t} \over e^t e^{i\pi} + e^{-t} e^{-i\pi} } \dt \\
&= - \int_{-R}^R e^{ai\pi} {e^{t} \over -e^t - e^{-t} } \dt \\
&= \int_{-R}^R e^{ai\pi} {e^{t} \over e^t + e^{-t} } \dt \\
&= e^{ai\pi} \int_{-R}^R {e^{t} \over e^t + e^{-t} } \dt \\
&= e^{ai\pi} \int_{-R}^R {e^{t} \over \cosh(t) } \dt \\
&= e^{ai\pi} \int_{\gamma_0} f(z) \dz
,\]
so
\[
\qty{\int_{\gamma_0} + \int_{\gamma_1}} f = (1+e^{ai\pi}) I
.\]

:::{.claim}
The integrals along the sides vanish as $R\to\infty$.

The quick argument: $\cos(z) \sim e^z$ so $\sech(z) \sim e^{-z}$, so
\[
\abs{f(R+ it)} &= \abs{e^{a(R+it)}\sech(R+it)} \sim \abs{ e^{aR}e^{-R}}  = \abs{ e^{R(a-1)} } = e^{R\cdot \Re(a-1)} \\
\abs{f(-R+ it)} &= \abs{e^{a(-R+it)}\sech(-R+it)} \sim \abs{ e^{-aR}e^{R}}  = \abs{ e^{-R(a+1)}} = e^{-R \cdot \Re(a+1)}
,\]
where the first goes to zero when $\Re(a)<1$ and the second when $\Re(a) > -1$.
:::

:::{.proof title="That the side integral vanish"}
Parameterize the right contour as 
\[
\gamma^+ = \ts{R+it \st t\in [0, \pi]}
.\]
Then
\[
\abs{ \int_{\gamma^+} f(z) \dz }
&= \abs{ \int_0^\pi f(R+it) \dt} \qquad z=R+it, \dz=\dt \\
&= \abs{ \int_0^\pi { e^{a(R+it)} \over \cosh(R+it) }  \dt } \\
&= \abs{ \int_0^\pi { e^{aR}e^{ait} \over e^Re^{it} + e^{-R} e^{-it} }   \dt } \\
&\leq  \int_0^\pi \abs{{ e^{aR}e^{ait} \over e^Re^{it} + e^{-R} e^{-it} } }  \dt  \\
&=  \int_0^\pi {{ \abs{ e^{aR}e^{ait} } \over \abs{ e^Re^{it} + e^{-R} e^{-it} } } }  \dt  \\
&\leq  c\int_0^\pi {{ \abs{ e^{aR} } \over \abs{ e^{-R} (e^{2R}e^{it} + e^{-it}) } } }  \dt \qquad c\da e^{ait} \\
&=  c\int_0^\pi {{ \abs{ e^{(a-1)R} } \over \abs{(e^{2R}e^{it} + e^{-it}) } } }  \dt  \\
&\leq  c\int_0^\pi {{ \abs{ e^{(a-1)R} } \over \abs{e^{2R}e^{it} } - \abs{e^{-it} } } }  \dt  \\
&=  c\int_0^\pi {{ e^{\Re((a-1)R)} \over e^{2R} - 1 } }  \dt  \\
&=  {{ c\pi e^{\Re((a-1)R)} \over e^{2R} - 1 } }  \\
&\leq  {{ c\pi e^{R\cdot \Re((a-1))}} }
\]
which goes to zero provide $\Re(a-1) < 0$, so $\Re(a) < 1$ (as assumed).
Here we've thrown out positive denominators, which only makes the terms larger.

Similarly, parameterized the left contour as 
\[
\gamma^- = \ts{-R+it \st t\in [0, \pi]}
,\]
then
\[
\abs{ \int_{\gamma^-} f(z) \dz }
&= \abs{ \int_0^\pi f(-R+it) \dt \qquad z=-R+it, \dz=\dt} \\
&= \abs{ \int_0^\pi { e^{a(-R+it)} \over \cosh(-R+it) }  \dt } \\
&= \abs{ \int_0^\pi { e^{-aR}e^{ait} \over e^{-R}e^{it} + e^{R} e^{-it} }   \dt } \\
&\leq  \int_0^\pi \abs{{ e^{-aR}e^{ait} \over e^{-R}e^{it} + e^{R} e^{-it} } }  \dt  \\
&=  \int_0^\pi {{ \abs{ e^{-aR}e^{ait} } \over \abs{ e^{-R}e^{it} + e^{R} e^{-it} } } }  \dt  \\
&\leq  c\int_0^\pi {{ \abs{ e^{-aR} } \over \abs{ e^{-R} (e^{it} + e^{2R}e^{-it}) } } }  \dt  \\
&=  c\int_0^\pi {{ \abs{ e^{-R(a+1)} } \over \abs{(e^{it} + e^{2R}e^{-it}) } } }  \dt  \\
&\leq  c\int_0^\pi {{ \abs{ e^{-R(a+1)} } \over \abs{e^{2R}e^{-it} } - \abs{e^{it} } } }  \dt  \\
&=  c\int_0^\pi {{ e^{\Re(-R(a+1))} \over e^{2R} - 1 } }  \dt  \\
&=  {{ c\pi e^{\Re(-R(a+1))} \over e^{2R} - 1 } }  \\
&\leq  {{ c\pi e^{-R \cdot \Re((a+1))}} }
,\]
which now goes to zero provided $\Re(a+1)>0$, so $\Re(a) > -1$ (again as assumed).

:::

Given thus, noting that only the pole $z_0 = {i\pi \over 2}$ is enclosed, the residue theorem yields
\[
2\pi i \Res_{z=z_0}f(z) = \int_\Gamma f = (1+e^{ai\pi})I \implies I = {2\pi i \Res_{z=z_0} f(z) \over 1 + e^{ai\pi}}
.\]
Computing the residue:
\[
\Res_{z=z_0}f(z) 
&= \lim_{z\to z_0} {(z-z_0)e^{az} \over \cosh(z)}\\
&\eqLH \lim_{z\to z_0} {a(z-z_0) e^{az} \over \sinh(z)} + {e^{az}\over \sinh(z)} \\
&= {a \cdot 0 \cdot e^{ai\pi \over 2} \over i \sin\qty{\pi \over 2} } + {e^{a i \pi \over 2} \over i\sin\qty{\pi \over 2}} \\
&= {e^{ai\pi\over 2} \over i} \\
&= -i e^{ai\pi \over 2}
,\]
where we've used that $\sinh(iz) = i\sin(z)$.
Putting it all together:
\[
I 
&= {2\pi i \cdot -i e^{ai\pi \over 2} \over 1 + e^{a i \pi}} \\
&= {2\pi e^{ai\pi \over 2} \over 1 + e^{a i \pi}} \\
&= {2\pi \over e^{-ai\pi \over 2}\qty{ 1 + e^{a i \pi}} } \\
&= {2\pi \over e^{-ai\pi \over 2}+ e^{a i \pi\over 2} }  \\
&= {\pi \over \cos\qty{a\pi \over 2}}\\
&= \pi \csc\qty{a\pi \over 2}
.\]

  
:::

