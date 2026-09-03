---
schema: qual/card@1
id: E-CFTRQ
kind: problem
title: Automorphisms of $\CP^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Fractional Linear Transformations
  - Riemann Surfaces
relations: []
review: draft
---

:::{.exercise}
Show that $\Aut(\CP^1) = \ts{{az+b\over cz+d} \st ad-bc\neq 0}$.

:::

:::{.solution}
Write $I(z) \da {1\over z}$ and note that
\[
{az+b\over cz+d} = {a \over c} + {bc-ad\over c}{1\over cz+d} = (z\mapsto cz+d)\circ\qty{ z \mapsto {1\over z} }\circ\qty{{ a\over c} + {bc-ad\over c} z}
,\]
which is $I$ composed with affine transformations.
Note that the last map satisfies
\[
\dd{}{z} {bc-ad \over c} z + {a\over c} = {bc-ad\over c}
,\]
which is nonzero (making the map conformal) precisely when $bd-ad\neq 0$.

$\supseteq$:
All LFTs are bijective, since if $f$ is an LFT then $f = A_1 \circ I \circ A_2$ with the $A_i$ affine and invertible, and $I(z)$ is invertible on $\CP^1$, so $f\inv = A_2\inv \circ I\inv \circ A_1\inv$.
Noting that the $A_i$ are conformal, if $I$ is conformal then by the chain rule $f'\neq 0$.
That $I$ is conformal on $\CP^1$: away from $z=0$ and $z=\infty$, $I(z) = 1/z$ is holomorphic with derivative $I'(z) = -1/z^2 \neq 0$, so it is conformal there.
Now use that $I\qty{1\over w} = w$ is conformal at zero, and ${1\over I(z)}$ is conformal at $\infty$.

$\subseteq$:
Suppose $f\in \Aut(\CP^1)$.
If $f(\infty) = \infty$, then the claim is that $f$ must be affine.
Define $F(z) \da {1\over f(1/z)}$ satisfies $F(0) = 0$, and $F$ is conformal at zero since it is a composition of $f$ and $I$.
So $F(0) = 0$ but $F'(0) \neq 0$, making zero a pole of $F$ of order one.
So $f$ has a pole of order 1 at $\infty$, and by injectivity, $f\inv(\infty) = \ts{\infty}$ has a single element.
Now $G(z) \da {f(z) - f(0) \over z}$ is bounded on $\CC$ and thus constant, so $f(z) - f(0) = cz \implies f(z) = cz + f(0)$.

If $f(\infty) = w < \infty$, consider $F(z) \da {1\over z-w}$.
The map $F$ is an LFT (it has the form $\frac{az+b}{cz+d}$ with $a=0, b=1, c=1, d=-w$), and $G(z) \da {1\over f(z) - w} = (F\circ f)(z)$ is an automorphism of $\CP^1$ satisfying $G(\infty) = \infty$ (since $f(\infty) = w$ makes $f(z) - w \to 0$ as $z \to \infty$, so $G(z) \to \infty$).
By the previous case, $G$ is affine, so 
\[
G(z) = az + b \implies {1\over f(z) - w} = az + b \implies f(z) = {1\over az + b } + w = {waz + wb\over az+b }
,\]
which is visibly an LFT.
:::
