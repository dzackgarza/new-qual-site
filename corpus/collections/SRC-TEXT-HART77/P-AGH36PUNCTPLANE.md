---
schema: qual/card@1
id: P-AGH36PUNCTPLANE
kind: problem
title: The punctured plane $\AA^2 \sm \theset{(0,0)}$ is quasi-affine but not affine
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
Show that $X = \AA^2 \sm \theset{(0,0)}$ is not affine.
:::

::: {.hint}
Show that $\mco(X) \cong k[x,y]$ and use Proposition I.3.5. See Ex. III.4.3 for another proof.
:::

::: {.solution}
Write $R=k[x,y]$ and let
$$
j:X\hookrightarrow\AA^2
$$
be the inclusion.
The principal opens $D(x)$ and $D(y)$ cover $X$.

::: pf

::: {.pf-step #s1}

Every regular function on $X$ is the restriction of a unique polynomial in $R$; hence
$$
\mco(X)=k[x,y].
$$

::: pf-proof

Let $f\in\mco(X)$.
On the principal affine opens $D(x)$ and $D(y)$, write
$$
f\restrict_{D(x)}=\frac{a}{x^m},
\qquad
f\restrict_{D(y)}=\frac{b}{y^n}
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

:::

::: {.pf-step #s2}

The variety $X$ is not affine.

::: pf-proof

Suppose that $X$ were affine.
By step [](#s1){.pf-ref}, the pullback on coordinate rings induced by the inclusion $j$ is the isomorphism
$$
j^*:k[x,y]=A(\AA^2)\longrightarrow A(X)=\mco(X)=k[x,y]
$$
given by restriction.
For affine varieties, a morphism is an isomorphism exactly when its induced homomorphism of coordinate rings is an isomorphism.
Thus $j$ would be an isomorphism $X\cong\AA^2$.
But $j$ is not surjective on points: its image omits $(0,0)$.
This contradiction proves that $X$ is not affine.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the required nonaffineness; step [](#s1){.pf-ref} supplies the global-function computation from the hint.

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 3.6, PDF p. 4: a regular function on $X$ is $f/g$ with $f$ and $g$ coprime, the curves $f=0$ and $g=0$ meet in finitely many points, and $g$ can vanish only at $(0,0)$ or where $f$ vanishes, so $g$ is constant and $\mco(X)=k[x,y]$; the map $X\to\AA^2$ is then an isomorphism of coordinate rings but not surjective on points.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.6, PDF p. 11: the same computation of $\mco(X)=k[x,y]$, by Bézout's theorem, and then the equivalence $\Hom(\AA^2,X)\cong\Hom(k[x,y],k[x,y])$ of Proposition I.3.5, whose identity map corresponds to the non-isomorphism $X\hookrightarrow\AA^2$.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.6, PDF p. 32: an affine variety has $\mco(X)$ equal to its coordinate ring, and $f/g$ with $(f)+(g)=1$ has $g$ vanishing in only finitely many points, so $g$ is constant.
All three use the printed hint; the proof above reads $\mco(X)$ off the two charts $D(x)$ and $D(y)$ by a divisibility count in the UFD $k[x,y]$, which avoids the Bézout and coprimality arguments, and it is Proposition I.3.5, not Exercise 3.5, that the hint's "(3.5)" must mean, as all three sets read it.
Agree.
:::
