---
schema: qual/card@1
id: P-AGXMISCTSENPONEBUNDLE
kind: problem
title: A family of genus-zero curves over a curve is a $\PP^1$-bundle
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tsen's Theorem
  - Projective Bundles
  - Cohomology and Base Change
relations:
- kind: uses
  target: T-COHBC
- kind: related-to
  target: D-VARSEVBRAUER
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Proved the relative degree-one criterion by cohomology and base change:
    f_*L is rank two, evaluation defines X -> P_Y(f_*L), and the map is an
    isomorphism on every fibre and hence globally. Also checked the Tsen
    argument on the generic fibre and extension of the resulting rational
    section over a smooth base curve by properness.
---

::: {.problem}
Use Tsen's theorem to show that given a flat family $X\to Y$ with $Y$ a curve where the fibers smooth curves of genus 0, this determines a Zariski $\PP^1$-bundle iff there exists a relative degree 1 line bundle on $X$ over $Y$.
:::

::: {.solution}
Let $X$ and $Y$ be
integral schemes, let $Y$ be a smooth curve over an algebraically closed
field $k$, and let
$$
f:X\longrightarrow Y
$$
be projective and flat with smooth genus-zero fibres. Here a Zariski
$\PP^1$-bundle means a projective bundle $\PP_Y(\mce)$ for a rank-two
locally free sheaf $\mce$. A relative degree-one line bundle is an
invertible sheaf $\mcl$ on $X$ such that
$$
\deg(\mcl|_{X_y})=1
$$
for every $y\in Y$.
Since a projective morphism is of finite presentation, flatness together
with smooth geometric fibres implies that $f$ is smooth.

<1>1. If
$$
X\cong\PP_Y(\mce)
$$
for a rank-two vector bundle $\mce$ on $Y$, then $X$ has a relative
degree-one line bundle.

::: {.proof}
The projective bundle carries its tautological quotient line bundle
$$
\OO_{\PP_Y(\mce)}(1).
$$
On every fibre
$$
\PP(\mce_y)\cong\PP^1_{\kappa(y)},
$$
its restriction is $\OO_{\PP^1}(1)$, which has degree $1$.
:::

<1>2. Conversely, suppose $\mcl$ is a relative degree-one line bundle.
For every fibre $C=X_y$,
$$
h^0(C,\mcl_y)=2,
\qquad
h^1(C,\mcl_y)=0.
$$

::: {.proof}
The curve $C$ is smooth proper of genus $0$, and
$$
\deg\mcl_y=1.
$$
Riemann--Roch gives
$$
h^0(C,\mcl_y)-h^1(C,\mcl_y)
=
\deg\mcl_y+1-g
=2.
$$
By Serre duality,
$$
h^1(C,\mcl_y)
=
h^0(C,\omega_C\tensor\mcl_y^{-1}).
$$
The line bundle on the right has degree
$$
-2-1=-3,
$$
so it has no nonzero section. Hence $h^1=0$ and $h^0=2$.
:::

<1>3. The sheaf
$$
\mce=f_*\mcl
$$
is locally free of rank $2$, and its formation commutes with base change:
$$
\mce\tensor\kappa(y)
\cong
H^0(X_y,\mcl_y).
$$

::: {.proof}
The line bundle $\mcl$ is flat over $Y$ because it is locally free over
$\OO_X$ and $X$ is flat over $Y$. By step <1>2, the fibre dimensions
$$
h^0(X_y,\mcl_y)=2
$$
are constant. Cohomology and base change [[T-COHBC]] therefore gives that
$f_*\mcl$ is locally free of rank $2$ and commutes with restriction to
every fibre.
:::

<1>4. For every fibre $C=X_y$, the line bundle $\mcl_y$ is isomorphic to
$\OO_{\PP^1}(1)$ after identifying $C\cong\PP^1_{\kappa(y)}$, and its
complete linear system defines an isomorphism
$$
C\xrightarrow{\sim}\PP\bigl(H^0(C,\mcl_y)\bigr).
$$

::: {.proof}
By step <1>2, $\mcl_y$ has a nonzero section. Its zero divisor is an
effective divisor of degree $1$, hence a single $\kappa(y)$-rational point
$p$. A smooth proper genus-zero curve with a rational point is
$\PP^1_{\kappa(y)}$ [[D-VARSEVBRAUER]], and under such an identification
$$
\mcl_y\cong\OO_{\PP^1}(p)\cong\OO_{\PP^1}(1).
$$
The complete linear system of $\OO_{\PP^1}(1)$ is the standard
isomorphism to projective one-space.
:::

<1>5. The evaluation homomorphism
$$
f^*\mce\longrightarrow\mcl
$$
is surjective and defines a $Y$-morphism
$$
g:X\longrightarrow\PP_Y(\mce)
$$
whose restriction to every fibre is an isomorphism.

::: {.proof}
By step <1>3, restriction of the evaluation map to $X_y$ is
$$
H^0(X_y,\mcl_y)\tensor\OO_{X_y}
\longrightarrow
\mcl_y.
$$
By step <1>4 this is the usual evaluation map for $\OO_{\PP^1}(1)$, so
it is surjective. The cokernel of the global evaluation map is coherent
and has zero restriction to every fibre; Nakayama's lemma therefore
implies that the cokernel is zero.

A quotient
$$
f^*\mce\twoheadrightarrow\mcl
$$
defines the displayed morphism to the projective bundle. Base change in
step <1>3 identifies its fibre map with the complete-linear-system map in
step <1>4, hence
$$
g_y:X_y\xrightarrow{\sim}\PP(\mce_y)
$$
for every $y$.
:::

<1>6. The morphism $g$ is an isomorphism. Thus a relative degree-one line
bundle makes $X$ a Zariski $\PP^1$-bundle.

::: {.proof}
The morphism $g$ is proper because $X$ is proper over $Y$ and
$\PP_Y(\mce)$ is separated over $Y$. Since every fibre map $g_y$ is an
isomorphism, $g$ is quasi-finite. Proper and quasi-finite implies finite.

The map on the generic fibre is an isomorphism by step <1>5, so $g$ is
birational. Since $Y$ is smooth and $\mce$ is locally free,
$$
\PP_Y(\mce)
$$
is smooth over the regular curve $Y$, hence regular and in particular
normal. A finite birational morphism onto a normal integral scheme is an
isomorphism. Therefore
$$
g:X\xrightarrow{\sim}\PP_Y(\mce).
$$
:::

<1>7. Hence
$$
\boxed{
X\cong\PP_Y(\mce)\text{ for a rank-two }\mce
\iff
X\text{ carries a relative degree-one line bundle}.
}
$$

::: {.proof}
Step <1>1 proves the forward implication and steps <1>2--<1>6 prove the
reverse implication.
:::

<1>8. Tsen's theorem supplies such a degree-one line bundle for the
generic genus-zero fibre.

::: {.proof}
Let
$$
K=k(Y)
$$
and let $X_\eta$ be the generic fibre. It is a smooth proper genus-zero
curve over $K$, hence a one-dimensional Severi--Brauer variety. Tsen's
theorem gives
$$
\operatorname{Br}(K)=0,
$$
so [[D-VARSEVBRAUER]] yields
$$
X_\eta\cong\PP^1_K.
$$
In particular $X_\eta$ has a $K$-rational point, which is a rational
section
$$
s_\eta:\eta\dashrightarrow X
$$
of $f$.

For a closed point $y\in Y$, the local ring $\OO_{Y,y}$ is a DVR with
fraction field $K$. Properness of $f$ and the valuative criterion extend
$s_\eta$ uniquely over $\Spec\OO_{Y,y}$. Since $X\to Y$ is of finite
presentation, this morphism from the local scheme descends to a section
over some open neighborhood of $y$. The resulting local sections all
agree on the generic point; separatedness of $f$ makes them agree on
their overlaps. They therefore glue to a global section
$$
s:Y\longrightarrow X.
$$
Since $f$ is a smooth relative curve, its section $s$ is a regular closed
immersion of codimension one. Thus $s(Y)$ is an effective Cartier divisor
meeting every fibre in one point. Therefore
$$
\OO_X(s(Y))
$$
has relative degree $1$.
:::

<1>9. In particular, over a smooth curve $Y$ over an algebraically closed
field, every such smooth genus-zero family is a Zariski $\PP^1$-bundle.

::: {.proof}
Step <1>8 constructs a relative degree-one line bundle, and step <1>7
applies the criterion.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>7 proves the requested equivalence, and steps <1>8--<1>9 use
Tsen's theorem to produce the relative degree-one line bundle.
:::
:::
