---
schema: qual/card@1
id: E-QVMUV
kind: exercise
title: Cauchy integral formula for coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Cauchy Integral Formula
  - Convergence Tests
relations: []
review: draft
---

:::{.exercise title="Cauchy integral formula for coefficients"}
Show that if $f(z) \sum_{k\in \ZZ} c_k (z-z_0)^k$, then 
\[
c_k = {1\over 2\pi i}\int_\gamma {f(z) \over (z-z_0)^{n+1}}\dz
,\]
and that this converges in an annulus $D_R(z_0)\sm \bar{D_r(z_0)}$ where
\[
r=\limsup _{n \rightarrow \infty} \sqrt[n]{\left|a_{-n}\right|} \text { and } R=\frac{1}{\limsup _{n \rightarrow \infty} \sqrt[n]{\left|a_{n}\right|}} \text {. }
.\]

Hint: start with
\[
f(z)=\frac{1}{2 \pi i} \oint_{\left|w-z_{0}\right|=s_{2}} \frac{f(w)}{w-z} d w-\frac{1}{2 \pi i} \oint_{\left|w-z_{0}\right|=s_{1}} \frac{f(w)}{w-z} d w
,\]
and try to obtain a geometric series to obtain
\[
f(z)=\sum_{j=-\infty}^{\infty}\left(\frac{1}{2 \pi i} \oint_{\left|w-z_{0}\right|=r} \frac{f(w)}{\left(w-z_{0}\right)^{j+1}} d w\right)\left(z-z_{0}\right)^{j}
.\]

:::

