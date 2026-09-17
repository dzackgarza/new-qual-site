---
schema: qual/card@1
id: P-AGH318PROJNORMAL
kind: problem
title: Projective normality depends on the embedding, via the twisted quartic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Varieties
  - Coordinate Rings
  - Rational Normal Curves
relations:
- kind: uses
  target: P-AGH317NORMAL
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with Hartshorne I.3.18 and restored the source reference to III.5.6. The proof uses the projective affine-chart coordinate rings for part (a), and the missing monomial t^2u^2 gives a direct integral-closure obstruction for the twisted quartic.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the chart normality argument, explicit inverse to the twisted-quartic parametrization, and the fraction-field witness against the source and published discussions. Some solution notes incorrectly call this P^3 map the full 4-uple embedding, which lands in P^4 and also has the t^2u^2 coordinate; the proof does not use that shortcut.'
---

::: {.problem}
A projective variety $Y \subseteq \PP^n$ is **projectively normal**, with respect to the given embedding, if its homogeneous coordinate ring $S(Y)$ is integrally closed.

(a) If $Y$ is projectively normal, show that $Y$ is normal.

(b) There are normal varieties in projective space which are not projectively normal.
Let $Y$ be the twisted quartic curve in $\PP^3$ given parametrically by $(x,y,z,w) = (t^4, t^3 u, t u^3, u^4)$.
Show that $Y$ is normal but not projectively normal. See (III, Ex. 5.6) for more examples.

(c) Show that the twisted quartic curve $Y$ above is isomorphic to $\PP^1$, which is projectively normal.
Thus projective normality depends on the embedding.
:::

::: {.solution}
<1>1. If a positively graded domain $S$ is integrally closed, then for every homogeneous element $f\in S$ of positive degree, the degree-zero subring
$$
(S_f)_0
$$
of the graded localization is integrally closed.

::: {.proof}
The localization $S_f$ is integrally closed by the localization result in [[P-AGH317NORMAL]].
Let
$$
\alpha\in\operatorname{Frac}((S_f)_0)
$$
be integral over $(S_f)_0$.
The same monic equation shows that $\alpha$ is integral over $S_f$, so integrally closedness gives
$$
\alpha\in S_f.
$$

Every element of $(S_f)_0$ is homogeneous of degree zero in the $\ZZ$-grading on $S_f$, so every quotient of two nonzero such elements also has degree zero in the fraction field of $S_f$.
Hence $\alpha$ is homogeneous of degree zero.
Since it already lies in $S_f$, it belongs to $(S_f)_0$.
Thus $(S_f)_0$ is integrally closed.
:::

<1>2. A projectively normal variety $Y\subseteq\PP^n$ is normal, proving (a).

::: {.proof}
Let $S=S(Y)$ be the homogeneous coordinate ring and assume that it is integrally closed.
For each standard projective chart $D_+(x_i)$, the affine open subset
$$
Y_i=Y\cap D_+(x_i)
$$
has coordinate ring
$$
A(Y_i)=(S_{x_i})_0
$$
[@Har10a, Theorem I.3.4(b)].
By step <1>1 this ring is integrally closed.
The affine normality criterion from [[P-AGH317NORMAL]] therefore makes every $Y_i$ normal.
These standard opens cover $Y$, so every local ring of $Y$ is integrally closed and $Y$ is normal.
:::

<1>3. The parametrization
$$
\nu:\PP^1\longrightarrow\PP^3,
\qquad
[t:u]\longmapsto[t^4:t^3u:tu^3:u^4]
$$
is an isomorphism onto the twisted quartic $Y$.

::: {.proof}
The four homogeneous coordinate polynomials have the same degree and no common zero on $\PP^1$, so they define a morphism.
By definition their image is $Y$.

The opens
$$
Y\cap D_+(x),
\qquad
Y\cap D_+(w)
$$
cover $Y$: for a parameter point, $x=t^4$ and $w=u^4$, which cannot vanish simultaneously.
On these opens define
$$
\psi_x([x:y:z:w])=[x:y],
\qquad
\psi_w([x:y:z:w])=[z:w].
$$
They are morphisms because the displayed coordinate pairs do not vanish on their respective domains.
For a parameter point with $t\ne0$,
$$
[x:y]=[t^4:t^3u]=[t:u],
$$
and for one with $u\ne0$,
$$
[z:w]=[tu^3:u^4]=[t:u].
$$
Thus both local maps are the set-theoretic inverse of $\nu$ on their domains.
They agree on the overlap and glue to a morphism
$$
\psi:Y\to\PP^1
$$
inverse to $\nu$.
Hence $Y\cong\PP^1$.
:::

<1>4. The twisted quartic $Y$ is normal.

::: {.proof}
The projective line is normal: its two standard affine charts have coordinate ring $k[s]$, a UFD and hence an integrally closed domain, so [[P-AGH317NORMAL]] applies.
By step <1>3, $Y\cong\PP^1$.
Normality is invariant under isomorphism, so $Y$ is normal.
:::

<1>5. The homogeneous coordinate ring of $Y$ is
$$
S(Y)\cong k[t^4,t^3u,tu^3,u^4]\subseteq k[t,u].
$$

::: {.proof}
The parametrization induces a homomorphism
$$
k[x,y,z,w]\longrightarrow k[t,u],
$$
$$
x\longmapsto t^4,
\qquad
y\longmapsto t^3u,
\qquad
z\longmapsto tu^3,
\qquad
w\longmapsto u^4.
$$
A homogeneous source polynomial of degree $d$ maps to a homogeneous polynomial of degree $4d$, so the kernel is homogeneous. For a homogeneous polynomial $F$, membership in the kernel is equivalent to vanishing on every parameter point $[t:u]$: the substituted homogeneous polynomial vanishes on all nonzero pairs in $k^2$, hence is zero. Thus the kernel is exactly $I(Y)$, and the first isomorphism theorem identifies the homogeneous coordinate ring with the displayed image subring.
:::

<1>6. The ring $S(Y)$ is not integrally closed, so $Y$ is not projectively normal.

::: {.proof}
Put
$$
q=t^2u^2.
$$
The element $q$ lies in the fraction field of $S(Y)$ because
$$
q=\frac{yw}{z}
=\frac{(t^3u)(u^4)}{tu^3}.
$$
It is integral over $S(Y)$, since
$$
q^2=t^4u^4=xw
$$
and hence it satisfies the monic equation
$$
T^2-xw=0.
$$

However, $q\notin S(Y)$.
Give the image subring its grading by total degree in $t,u$.
Every generator has degree four, so the degree-four part of $S(Y)$ is exactly
$$
\operatorname{span}_k\{t^4,t^3u,tu^3,u^4\}.
$$
The distinct monomial $t^2u^2$ is not in this span.
Terms of higher polynomial degree in the four generators have total degree at least eight, so they cannot contribute to a homogeneous element of total degree four.
Thus $q\notin S(Y)$.

This integral element of the fraction field proves that $S(Y)$ is not integrally closed.
Together with step <1>4, this proves (b).
:::

<1>7. The standard projective line is projectively normal.

::: {.proof}
Its homogeneous coordinate ring is
$$
S(\PP^1)=k[t,u],
$$
a UFD and hence an integrally closed domain.
Therefore $\PP^1$ is projectively normal.
Combined with the isomorphism of step <1>3 and the failure in step <1>6, this proves (c): projective normality depends on the chosen embedding.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>2 proves (a), steps <1>3--<1>6 prove (b), and steps <1>3 and <1>7 prove (c).
:::
:::
