---
schema: qual/card@1
id: P-AGXMISCGENUSZEROCONIC
kind: problem
title: Every genus zero smooth projective curve over $\CC$ is a plane conic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann--Roch
  - Rational Curves
  - Conics
relations: []
review: draft
---
::: {.problem}
Is every smooth projective curve of genus 0 defined over the field of complex numbers isomorphic to a conic in the projective plane?
Give an explanation for your answer.
:::

::: {.solution}
Let $C$ be a smooth projective curve over $\CC$ with $g(C)=0$.

::: pf

::: {.pf-step #s1}

$C\cong\PP^1$.

::: pf-proof

Fix a point $p\in C$. By Riemann--Roch,
$$
\ell(p)-\ell(K_C-p)=\deg(p)+1-g(C)=2.
$$
Since
$$
\deg(K_C-p)=2g(C)-2-1=-3<0,
$$
one has $\ell(K_C-p)=0$, so $\ell(p)=2$. Hence there exists a nonconstant meromorphic function $f\in L(p)$. Its only possible pole is at $p$, and that pole has order at most $1$.

Because $f$ is nonconstant, it has a pole, so its pole divisor is exactly $[p]$. Therefore the induced morphism
$$
f:C\longrightarrow\PP^1
$$
has degree $1$. A finite morphism of degree $1$ between smooth projective curves is an isomorphism. Thus $C\cong\PP^1$.

:::

:::

::: {.pf-step #s2}

$C$ is isomorphic to the plane conic
$$
\boxed{V(z_0z_2-z_1^2)\subset\PP^2}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, it suffices to embed $\PP^1$ as a conic. The quadratic Veronese map
$$
\nu_2:\PP^1\longrightarrow\PP^2,
\qquad
[t_0:t_1]\longmapsto[t_0^2:t_0t_1:t_1^2]
$$
is a closed immersion. Its image satisfies $z_0z_2=z_1^2$. Conversely, every point of the smooth conic $V(z_0z_2-z_1^2)$ lies in this image, so $\nu_2$ identifies $\PP^1$ with that conic. Composing the isomorphism from step [](#s1){.pf-ref} with $\nu_2$ gives the required isomorphism from $C$ to a plane conic.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves that every smooth projective genus-zero curve over $\CC$ is isomorphic to a conic in $\PP^2$.

:::

:::

:::
