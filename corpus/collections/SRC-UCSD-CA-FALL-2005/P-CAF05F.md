---
schema: qual/card@1
id: P-CAF05F
kind: problem
title: "Statement and proof of Harnack's inequality for harmonic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
State and prove Harnack's inequality for non-negative functions that are continuous in $\overline{\mathbb{D}}$ and harmonic in $\mathbb{D}$.
(You may use without proof the Poisson integral formula.)
:::

::: solution
For a nonnegative harmonic function $u$ on $\mathbb D$ that is continuous on
$\overline{\mathbb D}$, Harnack's inequality states that for $z\in\mathbb D$,
\[
\boxed{\displaystyle
\frac{1-|z|}{1+|z|}\,u(0)
\le u(z)\le
\frac{1+|z|}{1-|z|}\,u(0).}
\]

Write $z=re^{i\phi}$, $0\le r<1$. By the Poisson integral formula,
\[
u(re^{i\phi})
=\frac1{2\pi}\int_0^{2\pi}
P_r(\phi-t)u(e^{it})\,dt,
\]
where
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]
Since
\[
(1-r)^2\le 1-2r\cos\theta+r^2\le(1+r)^2,
\]
we have
\[
\frac{1-r}{1+r}
\le P_r(\theta)\le
\frac{1+r}{1-r}.
\]
Because $u(e^{it})\ge0$, multiplying these inequalities by the boundary values
and integrating gives
\[
\frac{1-r}{1+r}\,
\frac1{2\pi}\int_0^{2\pi}u(e^{it})\,dt
\le u(re^{i\phi})\le
\frac{1+r}{1-r}\,
\frac1{2\pi}\int_0^{2\pi}u(e^{it})\,dt.
\]
Applying the mean-value property at the origin identifies the common integral
with $u(0)$, proving the inequality.
:::
