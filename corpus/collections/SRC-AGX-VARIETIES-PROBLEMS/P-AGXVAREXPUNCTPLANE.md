---
schema: qual/card@1
id: P-AGXVAREXPUNCTPLANE
kind: problem
title: The punctured affine plane is not affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Regular Functions
  - Hartogs Extension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the final clause of Zaidenberg Exercise 9.2 in the recorded source,
    which asks that A^2_C minus the origin is not affine. No source solution is
    incorporated.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the D(x) union D(y) localization computation of global regular
    functions, the UFD intersection R_x intersect R_y=R, and the
    identification of the canonical map to the maximal spectrum of global
    functions with the
    non-surjective inclusion into A^2. Cross-checked the extension step
    against P-AGXEXTENDPUNCT.
---

::: {.problem}
Show that $\AA^2\slice{\CC} \smz$ is not an affine variety.
:::

::: {.solution}
Put
$$
U=\AA^2_\CC\setminus\{(0,0)\},
\qquad
R=\CC[x,y].
$$
Then
$$
U=D(x)\cup D(y).
$$

::: pf

::: {.pf-step #global-functions-are-polynomials}
Every global regular function on $U$ is the restriction of a unique
polynomial in $\CC[x,y]$:
$$
\boxed{\OO(U)=\CC[x,y].}
$$

::: pf-proof
Since
$$
D(x)=\operatorname{Specm}R_x,
\qquad
D(y)=\operatorname{Specm}R_y,
$$
a regular function
$$
f\in\OO(U)
$$
is represented by
$$
f|_{D(x)}=\frac{a}{x^m},
\qquad
f|_{D(y)}=\frac{b}{y^n}
$$
for some
$$
a,b\in R,
\qquad
m,n\geq0.
$$
On the overlap $D(xy)$ these representatives agree, so in
$$
\Frac R=\CC(x,y)
$$
one has
$$
\frac{a}{x^m}
=
\frac{b}{y^n}.
$$
Hence
$$
ay^n=bx^m.
$$
The ring $R$ is a UFD and $x,y$ are relatively prime prime elements. Thus
$$
x^m\mid a
\qquad\text{and}\qquad
y^n\mid b.
$$
Write
$$
a=x^m c,
\qquad
b=y^n c'
$$
with $c,c'\in R$. The equality $ay^n=bx^m$ then gives $c=c'$. Therefore
$$
f|_{D(x)}=c=f|_{D(y)},
$$
so $f$ is the restriction of the polynomial $c$.

Uniqueness follows because a polynomial vanishing on the nonempty open subset
$U$ of the irreducible affine plane must be zero.
:::

:::

::: {.pf-step #canonical-map-is-inclusion}
Under the identification in step [](#global-functions-are-polynomials){.pf-ref}, the canonical map
$$
\alpha:U\longrightarrow
\operatorname{Specm}\OO(U)
\cong
\operatorname{Specm}\CC[x,y]
=
\AA^2_\CC
$$
is the ordinary inclusion
$$
U\hookrightarrow\AA^2_\CC.
$$

::: pf-proof
For a point
$$
p=(a,b)\in U,
$$
the canonical map to the maximal spectrum of global functions sends $p$ to the
maximal ideal of global regular functions vanishing at $p$.

By step [](#global-functions-are-polynomials){.pf-ref}, the global functions are exactly the restrictions of
polynomials in $\CC[x,y]$. The vanishing ideal at $(a,b)$ is therefore
$$
(x-a,y-b)\subseteq\CC[x,y].
$$
This is exactly the point $(a,b)$ of $\AA^2_\CC$. Hence $\alpha$ agrees
pointwise with the inclusion of the punctured plane into the affine plane.
:::

:::

::: {.pf-step #affine-forces-iso}
If $U$ were affine, the map $\alpha$ in step [](#canonical-map-is-inclusion){.pf-ref} would be an
isomorphism.

::: pf-proof
For any affine variety $Y$, the canonical morphism
$$
Y\longrightarrow\operatorname{Specm}\OO(Y)
$$
is an isomorphism: this is the affine variety--coordinate ring
correspondence. Thus affineness of $U$ would force $\alpha$ to be an
isomorphism.
:::

:::

::: {.pf-step #punctured-plane-not-affine}
The punctured affine plane is not affine:
$$
\boxed{
\AA^2_\CC\setminus\{(0,0)\}
\text{ is not an affine variety}.
}
$$

::: pf-proof
By step [](#canonical-map-is-inclusion){.pf-ref}, $\alpha$ is the inclusion
$$
U\hookrightarrow\AA^2_\CC.
$$
It is not surjective, because $(0,0)$ is not in its image. Therefore it is
not an isomorphism. Step [](#affine-forces-iso){.pf-ref} shows that this is impossible if $U$ is affine.
Hence $U$ is not affine.
:::

:::

::: pf-qed
Step [](#punctured-plane-not-affine){.pf-ref} is the required conclusion.
:::

:::

:::
