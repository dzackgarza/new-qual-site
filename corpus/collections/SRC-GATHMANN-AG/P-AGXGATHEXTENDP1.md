---
schema: qual/card@1
id: P-AGXGATHEXTENDP1
kind: problem
title: Extending morphisms into $\PP^1$ across a puncture
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Projective Space
  - Indeterminacy Loci
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Gathmann 5.7 card and collection context together with
    the retained Problem Set 5 native source and migration record. The source
    supplies the three statements but no worked argument. Cross-checked the
    projective-coordinate construction against T-DIVMAPPN and the dense-open
    uniqueness arguments against separatedness of P^1.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read all three parts. Checked that a reduced rational function gives a
    base-point-free pair on A^1, that [x:y] on the punctured affine plane
    forces incompatible values at the origin along the two coordinate axes,
    and that the standard two-chart computation gives
    Gamma(P^1,O)=k, hence every morphism P^1 to A^1 is constant.
---

::: {.problem}
Show that

a. Every morphism $f:\AA^1\smz \to \PP^1$ can be extended to a morphism $\hat f: \AA^1 \to \PP^1$.

b. Not every morphism $f:\AA^2\smz \to \PP^1$ can be extended to a morphism $\hat f: \AA^2 \to \PP^1$.

c. Every morphism $\PP^1\to \AA^1$ is constant.
:::

::: {.solution}
Write
$$
U_n=\AA^n\smz.
$$

::: pf

::: {.pf-step #rational-function-from-morphism}
Part (a): every nonconstant morphism
$$
f:U_1\longrightarrow\PP^1
$$
determines a rational function
$$
r(t)\in k(t).
$$

::: pf-proof
Let $t$ be the coordinate on $\AA^1$ and let $\eta$ be the generic point
of
$$
U_1=\operatorname{Spec}k[t,t^{-1}].
$$
If $f(\eta)$ were a closed point of $\PP^1$, continuity would give
$$
f(U_1)
\subseteq
\overline{\{f(\eta)\}}
=
\{f(\eta)\},
$$
so $f$ would be constant. Thus for nonconstant $f$, the generic point maps
to the generic point of $\PP^1$.

On the standard affine chart
$$
\AA^1\subset\PP^1
$$
with coordinate $z$, the pullback of $z$ at the generic point is therefore
an element
$$
r(t)\in k(t).
$$
This is the rational function induced by $f$.
:::

:::

::: {.pf-step #morphism-from-coprime-pair}
Part (a): write
$$
r(t)=\frac{p(t)}{q(t)}
$$
with coprime $p,q\in k[t]$. Then
$$
\hat f(t)=[p(t):q(t)]
$$
defines a morphism
$$
\boxed{\hat f:\AA^1\longrightarrow\PP^1}.
$$

::: pf-proof
Because $p$ and $q$ are coprime in the PID $k[t]$, there exist
$a,b\in k[t]$ such that
$$
ap+bq=1.
$$
Hence $p$ and $q$ have no common zero on $\AA^1$, or equivalently they
generate the trivial line bundle at every point.
The projective-coordinate construction [[T-DIVMAPPN]] therefore gives the
morphism
$$
t\longmapsto[p(t):q(t)].
$$
:::

:::

::: {.pf-step #extension-restricts-correctly}
Part (a): the morphism $\hat f$ of step [](#morphism-from-coprime-pair){.pf-ref} restricts to $f$ on
$U_1$.

::: pf-proof
On the dense open subset of $U_1$ where $q\ne0$ and where $f$ lands in the
affine chart $\AA^1\subset\PP^1$, both maps have affine coordinate
$$
\frac{p}{q}=r.
$$
Thus they agree on a dense open subset of the irreducible scheme $U_1$.
For two morphisms to $\PP^1$, the equalizer is the inverse image of the
diagonal
$$
\Delta_{\PP^1}\subset\PP^1\times\PP^1.
$$
In homogeneous coordinates
$$
([X_0:X_1],[Y_0:Y_1]),
$$
this diagonal is cut out by
$$
X_0Y_1-X_1Y_0=0,
$$
so it is closed. Hence the equalizer of the two morphisms
$$
U_1\rightrightarrows\PP^1
$$
is closed. It contains a dense open subset, hence it is all of $U_1$.
Therefore
$$
\hat f|_{U_1}=f.
$$

If $f$ is constant, the corresponding constant map on $\AA^1$ is already
an extension. This proves part (a).
:::

:::

::: {.pf-step #diagonal-map-on-punctured-plane}
Part (b): the formula
$$
f(x,y)=[x:y]
$$
defines a morphism
$$
f:U_2\longrightarrow\PP^1.
$$

::: pf-proof
On
$$
U_2=\AA^2\setminus\{(0,0)\},
$$
the functions $x$ and $y$ never vanish simultaneously. Thus they generate
the trivial line bundle on $U_2$, so [[T-DIVMAPPN]] gives the morphism
$$
(x,y)\longmapsto[x:y].
$$
:::

:::

::: {.pf-step #no-extension-to-plane}
Part (b): the morphism in step [](#diagonal-map-on-punctured-plane){.pf-ref} does not extend to
$\AA^2$.

::: pf-proof
Suppose that
$$
F:\AA^2\longrightarrow\PP^1
$$
extends $f$.
Let
$$
L_x=V(y),
\qquad
L_y=V(x)
$$
be the two coordinate axes.

On the dense open subset
$$
L_x\setminus\{(0,0)\},
$$
the map $F$ equals
$$
[x:0]=[1:0].
$$
As in step [](#extension-restricts-correctly){.pf-ref}, separatedness of $\PP^1$ implies that
$$
F|_{L_x}
$$
is the constant map with value $[1:0]$. In particular,
$$
F(0,0)=[1:0].
$$

Similarly, on
$$
L_y\setminus\{(0,0)\}
$$
one has
$$
F=[0:y]=[0:1],
$$
so
$$
F(0,0)=[0:1].
$$
These two points of $\PP^1$ are distinct, a contradiction.
Therefore the morphism in step [](#diagonal-map-on-punctured-plane){.pf-ref} has no extension to $\AA^2$.
:::

:::

::: {.pf-step #global-sections-are-constants}
Part (c):
$$
\boxed{\Gamma(\PP^1,\OO_{\PP^1})=k.}
$$

::: pf-proof
Use the standard affine cover
$$
U_0=D(Y)\cong\operatorname{Spec}k[t],
\qquad
U_\infty=D(X)\cong\operatorname{Spec}k[u],
$$
where
$$
u=t^{-1}
$$
on
$$
U_0\cap U_\infty\cong\operatorname{Spec}k[t,t^{-1}].
$$
A global regular function is given by polynomials
$$
p(t)\in k[t],
\qquad
q(u)\in k[u]
$$
whose restrictions agree:
$$
p(t)=q(t^{-1})
$$
in $k[t,t^{-1}]$.
Hence
$$
p(t)\in k[t]\cap k[t^{-1}]
$$
inside $k[t,t^{-1}]$.
The only Laurent polynomials involving only nonnegative powers of $t$ and
only nonpositive powers of $t$ are the constants. Therefore
$$
k[t]\cap k[t^{-1}]=k,
$$
and every global regular function on $\PP^1$ is constant.
:::

:::

::: {.pf-step #morphisms-to-affine-line-are-constant}
Part (c): every morphism
$$
f:\PP^1\longrightarrow\AA^1
$$
is constant.

::: pf-proof
Let $z$ be the coordinate on
$$
\AA^1=\operatorname{Spec}k[z].
$$
The pullback
$$
f^*z
$$
is a global regular function on $\PP^1$. By step [](#global-sections-are-constants){.pf-ref},
$$
f^*z=\lambda
$$
for some $\lambda\in k$.
Thus the induced map to $\AA^1$ has the same coordinate value
$\lambda$ at every point, so
$$
f
$$
is the constant morphism with value $\lambda$.
:::

:::

::: pf-qed
Steps [](#rational-function-from-morphism){.pf-ref}, [](#morphism-from-coprime-pair){.pf-ref} and [](#extension-restricts-correctly){.pf-ref} prove the extension statement in part (a).
Steps [](#diagonal-map-on-punctured-plane){.pf-ref} and [](#no-extension-to-plane){.pf-ref} give a morphism on the punctured affine plane that cannot
extend, proving part (b).
Steps [](#global-sections-are-constants){.pf-ref} and [](#morphisms-to-affine-line-are-constant){.pf-ref} prove part (c).
:::

:::
:::
