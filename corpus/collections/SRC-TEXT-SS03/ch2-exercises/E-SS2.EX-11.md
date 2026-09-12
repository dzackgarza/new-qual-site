---
schema: qual/card@1
id: E-SS2.EX-11
kind: problem
title: "Cauchy estimates on a smaller disk"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
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

::: exercise
Let $f$ be a holomorphic function on the disk $D_{R_0}(0) \subset \mathbb{C}$ of radius $R_0 > 0$.

(a) Prove that whenever $0 < R < R_0$ and $|z| < R$,
$$
f(z) = \frac{1}{2\pi} \int_0^{2\pi} f(R e^{i\varphi}) \operatorname{Re}\left( \frac{R e^{i\varphi} + z}{R e^{i\varphi} - z} \right) d\varphi.
$$

(b) Show that for $z = r \in [0, R)$ (and in general with $\gamma = \varphi - \theta$ where $z = r e^{i\theta}$):
$$
\operatorname{Re}\left( \frac{R e^{i\gamma} + r}{R e^{i\gamma} - r} \right) = \frac{R^2 - r^2}{R^2 - 2Rr\cos\gamma + r^2}.
$$
:::

::: solution
For part (b), let $z=re^{i\theta}$ and put $\gamma=\varphi-\theta$. Rotating by $e^{-i\theta}$ reduces the computation to real $r$. Then
\[
\frac{Re^{i\gamma}+r}{Re^{i\gamma}-r}
=
\frac{(Re^{i\gamma}+r)(Re^{-i\gamma}-r)}{|Re^{i\gamma}-r|^2}.
\]
The numerator has real part $R^2-r^2$, while
\[
|Re^{i\gamma}-r|^2=R^2-2Rr\cos\gamma+r^2.
\]
Hence
\[
\operatorname{Re}\frac{Re^{i\gamma}+r}{Re^{i\gamma}-r}
=
\frac{R^2-r^2}{R^2-2Rr\cos\gamma+r^2}.
\]

For part (a), first suppose $0<|z|<R$ and set
\[
w=\frac{R^2}{\overline z}.
\]
Then $|w|>R$. By Cauchy's formula and Cauchy's theorem,
\[
f(z)=\frac1{2\pi i}\int_{|\zeta|=R}f(\zeta)
\left(\frac1{\zeta-z}-\frac1{\zeta-w}\right)d\zeta.
\]
On $|\zeta|=R$,
\[
\zeta\left(\frac1{\zeta-z}-\frac1{\zeta-w}\right)
=
\frac{\zeta}{\zeta-z}+\frac{\overline z}{\overline\zeta-\overline z}
=
\operatorname{Re}\frac{\zeta+z}{\zeta-z}.
\]
With $\zeta=Re^{i\varphi}$ and $d\zeta=i\zeta\,d\varphi$, this gives
\[
f(z)=\frac1{2\pi}\int_0^{2\pi}
 f(Re^{i\varphi})
 \operatorname{Re}\left(\frac{Re^{i\varphi}+z}{Re^{i\varphi}-z}\right)d\varphi.
\]
If $z=0$, the formula is exactly the usual mean-value formula, so it holds for every $|z|<R$.
:::
