---
schema: qual/card@1
id: P-CAFA22E
kind: problem
title: "Harmonic function on punctured plane and its Laurent decomposition"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G = \mathbb{C} \setminus \{0\}$, and let $h : G \to \mathbb{R}$ be harmonic.

(i) Show that $g = h_x - ih_y$ is a holomorphic function in $G$, and that its residue at $0$ is a real number.

(ii) Show that there exist a constant $c$ and a holomorphic function $f : G \to \mathbb{C}$ such that
$$
h(z) = c\log|z| + \operatorname{Re} f(z) \quad \forall z \in G.
$$
:::

::: solution
Since $h$ is harmonic,
\[
g=h_x-ih_y=2\frac{\partial h}{\partial z}
\]
is holomorphic on $G$. For a positively oriented circle $|z|=r$,
parametrized by $z=re^{it}$,
\[
\int_{|z|=r}g(z)\,dz
=\int_0^{2\pi}(h_x-ih_y)(-r\sin t+ir\cos t)\,dt.
\]
Its real part is the integral of the tangential derivative of $h$ around the
circle, hence is $0$. Therefore the integral is purely imaginary, and
\[
\operatorname{Res}_0 g=\frac1{2\pi i}\int_{|z|=r}g(z)\,dz
\]
is real. Write this residue as $c\in\mathbb R$.

Then $g(z)-c/z$ has zero period around a generator of
$\mathbb C\setminus\{0\}$, hence all its periods vanish. It therefore has a
holomorphic primitive $F$ on $G$. Since
\[
2\frac{\partial}{\partial z}\bigl(h-c\log|z|-\operatorname{Re}F\bigr)=0,
\]
the real-valued function in parentheses is constant. Absorb that real
constant into $F$. We obtain
\[
\boxed{h(z)=c\log|z|+\operatorname{Re}F(z)}.
\]
:::
