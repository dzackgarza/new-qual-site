---
schema: qual/card@1
id: E-QVMUV
kind: problem
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

:::{.exercise}
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

::: solution
The statement has three notation errors: the opening display is missing an
equality sign, the coefficient formula uses $n$ where it must use $k$, and the
radii are written with $a_{\pm n}$ instead of the coefficients $c_{\pm n}$.
With these corrections, if
\[
f(z)=\sum_{k\in\ZZ}c_k(z-z_0)^k,
\]
then for any positively oriented circle $\gamma$ centered at $z_0$ and lying
in the annulus of analyticity,
\[
\boxed{c_k={1\over2\pi i}\int_\gamma
{f(z)\over(z-z_0)^{k+1}}\,dz.}
\]
Indeed, termwise integration gives
\[
{1\over2\pi i}\int_\gamma
{f(z)\over(z-z_0)^{k+1}}\,dz
=\sum_jc_j{1\over2\pi i}\int_\gamma(z-z_0)^{j-k-1}\,dz=c_k.
\]

For the positive-power part, Cauchy--Hadamard gives outer radius
\[
R={1\over\limsup_{n\to\infty}|c_n|^{1/n}}.
\]
For the negative-power part, put $w=(z-z_0)^{-1}$; then
\[
\sum_{n\ge1}c_{-n}(z-z_0)^{-n}=\sum_{n\ge1}c_{-n}w^n
\]
has radius $1/\limsup|c_{-n}|^{1/n}$ in $w$, hence converges exactly when
\[
|z-z_0|>r,
\qquad
r=\limsup_{n\to\infty}|c_{-n}|^{1/n}.
\]
Therefore the Laurent series converges on
\[
\boxed{r<|z-z_0|<R.}
\]
The two-circle formula in the hint is the usual Cauchy formula on an annulus;
expanding each kernel geometrically yields the same Laurent expansion and
coefficient formula.
:::
