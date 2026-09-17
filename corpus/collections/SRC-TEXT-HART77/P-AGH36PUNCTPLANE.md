---
schema: qual/card@1
id: P-AGH36PUNCTPLANE
kind: problem
title: The punctured plane $\AA^2 \sm \ts{(0,0)}$ is quasi-affine but not affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasi-Affine Varieties
  - Regular Functions
  - Affine Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and hint with Hartshorne I.3.6. The proof computes global regular functions from the principal-open cover D(x) union D(y) and then applies the affine coordinate-ring criterion to the inclusion into A^2.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the localization calculation and the final coordinate-ring contradiction against published solutions; the UFD divisibility argument shows every global regular function extends across the missing origin.'
---

::: {.problem}
There are quasi-affine varieties which are not affine.
Show that $X = \AA^2 \sm \ts{(0,0)}$ is not affine.
:::

::: {.hint}
Show that $\mco(X) \cong k[x,y]$ and compare with the affine criterion.
:::

::: {.solution}
Write $R=k[x,y]$ and let
$$
j:X\hookrightarrow\AA^2
$$
be the inclusion.
The principal opens $D(x)$ and $D(y)$ cover $X$.

<1>1. Every regular function on $X$ is the restriction of a unique polynomial in $R$; hence
$$
\mco(X)=k[x,y].
$$

::: {.proof}
Let $f\in\mco(X)$.
On the principal affine opens $D(x)$ and $D(y)$, write
$$
f|_{D(x)}=\frac{a}{x^m},
\qquad
f|_{D(y)}=\frac{b}{y^n}
$$
with $a,b\in R$ and $m,n\ge0$.
On the overlap $D(xy)$ these expressions agree, so in the fraction field $k(x,y)$,
$$
a y^n=b x^m.
$$
Since $R$ is a UFD and $x$ and $y$ are relatively prime prime elements, $x^m$ divides $a$ and $y^n$ divides $b$.
Thus $a=x^m c$ and $b=y^n c'$ for some $c,c'\in R$.
The displayed equality then gives $c=c'$.
Therefore $f$ equals the polynomial $c$ on both members of the cover, hence on all of $X$.

Conversely every polynomial restricts to a regular function on $X$.
The restriction map $R\to\mco(X)$ is injective because a polynomial vanishing on the nonempty open subset $X$ of the irreducible variety $\AA^2$ vanishes identically.
Hence it is an isomorphism.
:::

<1>2. The variety $X$ is not affine.

::: {.proof}
Suppose that $X$ were affine.
By step <1>1, the pullback on coordinate rings induced by the inclusion $j$ is the isomorphism
$$
j^*:k[x,y]=A(\AA^2)\longrightarrow A(X)=\mco(X)=k[x,y]
$$
given by restriction.
For affine varieties, a morphism is an isomorphism exactly when its induced homomorphism of coordinate rings is an isomorphism.
Thus $j$ would be an isomorphism $X\cong\AA^2$.
But $j$ is not surjective on points: its image omits $(0,0)$.
This contradiction proves that $X$ is not affine.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 proves the required nonaffineness; step <1>1 supplies the global-function computation from the hint.
:::
:::
