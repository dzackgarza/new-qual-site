---
schema: qual/card@1
id: E-JUT2P
kind: exercise
title: Removable singularities for derivatives
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Cauchy Estimates
  - Singularities
relations: []
review: draft
solved: true
---

:::{.exercise title="Removable singularities for derivatives"}
Suppose $f$ is meromorphic. Show that if $z_0$ is a removable singularity of $f$, then it is also a removable singularity of $f'$.
Conversely, if $z_0$ is removable for $f'$, then it is also removable for $f$.

:::

:::{.solution}
It suffices to show that $f'$ is bounded in a neighborhood of $z_0$.
Since $z_0$ is a removable singularity of $f$, there is a neighborhood $\DD_R(a)$ on which $\abs{f(z)} \leq M$ is bounded.
Using the Cauchy estimates,
\[
\abs{f'(z_0)} 
&\leq {1\over 2\pi } \oint_{\abs{z-a} = R } {\abs{f(z)} \over \abs{z-z_0}^2 } \dz \\
&\leq {1\over 2\pi } \oint_{\abs{z-a} = R } MR^{-2} \dz \\
&= {1\over 2\pi } MR^{-2} \cdot 2\pi R \\
&= MR\inv < \infty
.\]

For the converse, if $z_0$ is removable for $f'$, write $F'$ for the holomorphic extension of $f'$ over $\DD_\eps(a)$ which exists by Riemann's removable singularity theorem.
Since $F'$ is holomorphic, it has a primitive $F(z) \da \int_{w}^z F'(\xi) \dxi$ for any point $w$ in this region.
Now $G\da F' - f' \equiv 0$ on $\DD_\eps^*(a)$ making $G\equiv c$ constant, so $f(z) = F(z) + c$.
In particular,
\[
\lim_{z\to a} f(z) = \lim_{z\to a} F(z) + c = \lim_{z\to a} \int_w^z F' \dz + c = F'(a) + c < \infty
,\]
so $a$ is removable for $f$.

:::
