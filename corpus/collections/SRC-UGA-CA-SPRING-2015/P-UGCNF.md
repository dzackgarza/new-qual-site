---
schema: qual/card@1
id: P-UGCNF
kind: problem
title: $-\frac12\bigl(z+\frac1z\bigr)$ maps the upper half-disk conformally onto the
  upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: problem
Prove that $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a conformal map from half disc $\{z=x+iy:\ |z|<1,\ y>0\}$ to upper

half plane ${\mathbb H}=\{z=x+iy:\ y>0\}$.
:::

::: solution
Let
\[
G=\{z:|z|<1,\ \operatorname{Im}z>0\}.
\]
For $z=x+iy$,
\[
\operatorname{Im}\left(z+\frac1z\right)
=y-\frac{y}{|z|^2}
=y\left(1-\frac1{|z|^2}\right)<0
\]
on $G$. Hence
\[
\operatorname{Im}f(z)>0,
\]
so $f(G)\subset\mathbb H$.

Also
\[
f'(z)=-\frac12\left(1-\frac1{z^2}\right).
\]
Its zeros are $z=\pm1$, which lie on the boundary, so $f'$ never vanishes in
$G$.

To prove injectivity, suppose $f(z_1)=f(z_2)$. Then
\[
z_1+\frac1{z_1}=z_2+\frac1{z_2},
\]
so
\[
(z_1-z_2)\left(1-\frac1{z_1z_2}\right)=0.
\]
If $z_1\ne z_2$, then $z_1z_2=1$, impossible because
$|z_1z_2|<1$. Thus $z_1=z_2$.

Finally, the boundary of $G$ consists of $(-1,0)\cup(0,1)$ on the real axis
and the upper semicircle $|z|=1$. On the real intervals, $f$ is real; on the
upper semicircle, $1/z=\overline z$, so again $f(z)=-\operatorname{Re}z$ is
real. As $z\to0$ through $G$, $|f(z)|\to\infty$. Hence the boundary is mapped
to the extended real line. Since $f$ is injective and holomorphic with
nonvanishing derivative, $f(G)$ is a simply connected open subset of
$\mathbb H$ whose boundary in the sphere is the full extended real line. It
must therefore be all of $\mathbb H$.

Thus $f:G\to\mathbb H$ is a conformal bijection.
:::
