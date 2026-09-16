---
schema: qual/card@1
id: P-CAFA20G
kind: problem
title: "Dirichlet problem on a domain between two circles"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $\mathbb{D}$ denote the open unit disc, and let $\mathbb{D}' = \{z \in \mathbb{C} : |z + 2/5| < 2/5\}$ denote the open disc of center $-2/5$ and radius $2/5$.
Let $\Omega = \mathbb{D} \setminus \overline{\mathbb{D}'}$.

Find, with justification, an explicit continuous function $h: \overline{\Omega} \to \mathbb{R}$, harmonic in $\Omega$, and with boundary values $h = 0$ on $\partial\mathbb{D}$ and $h = 1$ on $\partial\mathbb{D}'$.

Hint: You may wish to use a conformal map to change the domain $\Omega$.
:::

::: {.solution}
The two boundary circles belong to the same coaxial family. Their limiting
points are $-1/2$ and $-2$, so consider the Möbius map
\[
\Phi(z)=\frac{z+1/2}{z+2}.
\]
On the outer boundary $|z|=1$, one checks that
\[
|\Phi(z)|=\frac12,
\]
while on the inner boundary $|z+2/5|=2/5$,
\[
|\Phi(z)|=\frac14.
\]
Hence $\Phi$ maps $\Omega$ conformally onto the annulus
\[
\frac14<|w|<\frac12.
\]

On that annulus the radial harmonic function taking boundary values $1$ on
$|w|=1/4$ and $0$ on $|w|=1/2$ is
\[
H(w)=\frac{\log(2|w|)}{\log(1/2)}
=\frac{\log\!\bigl(1/(2|w|)\bigr)}{\log 2}.
\]
Therefore
\[
\boxed{\displaystyle
h(z)=\frac{\log\!\left(\frac{|z+2|}{2|z+1/2|}\right)}{\log 2}}
\]
is harmonic on $\Omega$ and continuous on $\overline\Omega$. On
$\partial\mathbb D$, $|\Phi|=1/2$, so $h=0$; on
$\partial\mathbb D'$, $|\Phi|=1/4$, so $h=1$.
:::
