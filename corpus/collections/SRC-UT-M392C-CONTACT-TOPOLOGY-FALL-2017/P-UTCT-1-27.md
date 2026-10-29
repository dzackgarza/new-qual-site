---
schema: qual/card@1
id: P-UTCT-1-27
kind: problem
title: Poincaré--Hopf theorem for surfaces with boundary via the relative Euler class
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 1.27 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated Definition 1.24 and Example 1.26, on which the exercise depends, from pp. 6-7 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $F$ be a compact, oriented, connected surface with $\partial F \neq \emptyset$, and let $\xi \to F$ be an oriented plane bundle.
Given a nowhere zero section $v$ of $\xi$ over $\partial F$, the relative Euler class $e(\xi, v)$ is $[w^{-1}(0)]$ for an extension $w$ of $v$ to all of $F$ transverse to the zero section, that is, the signed count
$$
e(\xi, v) = \sum_{v(x) = 0} \operatorname{sign}_v(x).
$$
Changing $e(\xi, v)$ by $\pm 1$ is the same as adding $\pm 1$ twists to $v|_{\partial F}$, so for suitable $v$ (the "fix" on $v$) the zeros can be pushed to the boundary and $e(\xi, v) = 0$.

Show that not doing the fix on $v$ above retrieves the Poincaré--Hopf theorem as in the boundaryless case.
That is, for $F$ compact and connected, show that
$$
\chi(F) = e(TF, v),
$$
where on each component of $\partial F$, either $v$ is parallel to $\partial F$ or $v$ is perpendicular to $\partial F$.
:::

::: {.solution}

Choose a Riemannian metric on \(F\). Let
\[
T
\]
denote the positively oriented unit tangent vector field along
\(\partial F\).

::: pf

::: {.pf-step #s1-1}

On each connected component \(C\subset\partial F\), a nowhere-zero
vector field \(v\) that is everywhere parallel to \(C\) is homotopic through
nowhere-zero sections of \(TF|_C\) to \(T|_C\).


::: pf-proof

Since \(v\) is everywhere parallel to \(C\), there is a continuous
nowhere-zero function
\[
\lambda:C\to\RR-\{0\}
\]
such that
\[
v=\lambda T.
\]
Because \(C\) is connected, \(\lambda\) has constant sign. After positive
rescaling, \(v\) is homotopic either to \(T\) or to \(-T\). The fields
\(T\) and \(-T\) are homotopic through nonzero vectors by rotating through
angle \(\pi\) in the oriented plane \(TF|_C\).

:::

:::

::: {.pf-step #s1-2}

On each connected component \(C\subset\partial F\), a nowhere-zero
vector field \(v\) that is everywhere perpendicular to \(C\) is likewise
homotopic through nowhere-zero sections to \(T|_C\).


::: pf-proof

Let \(N\) be the unit normal to \(C\) inside the oriented plane \(TF|_C\),
chosen so that \((T,N)\) is an oriented orthonormal frame. A nonzero field
perpendicular to \(C\) is a nonzero scalar multiple of \(N\), hence is
homotopic to \(N\) or \(-N\). Rotating by the constant angle
\[
\pm\frac{\pi}{2}
\]
gives a homotopy through nowhere-zero vectors from either \(\pm N\) to \(T\).

:::

:::

::: pf-step

Therefore the given boundary section \(v\) is homotopic through
nowhere-zero boundary sections to \(T\).


::: pf-proof

Apply steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} independently on each connected component of
\(\partial F\). The boundary components are disjoint, so the homotopies
combine.

:::

:::

::: {.pf-step #s1-4}

The relative Euler class is unchanged under a homotopy of the
nowhere-zero boundary section. Hence
\[
\boxed{
e(TF,v)=e(TF,T)}.
\]


::: pf-proof

A homotopy of nowhere-zero boundary sections can be viewed as a nowhere-zero
section over
\[
\partial F\times I.
\]
Using a collar of the boundary, this homotopy extends to a bundle
isomorphism between the corresponding relative obstruction problems.
Equivalently, the relative Euler class depends only on the homotopy class of
the boundary trivialization. Therefore homotopic boundary sections determine
the same relative Euler number.

:::

:::

::: pf-step

Choose an extension
\[
w:F\to TF
\]
of \(T\) that is transverse to the zero section.


::: pf-proof

By the definition of the relative Euler class, one may choose any extension
of the prescribed nonzero boundary section and perturb it in the interior to
be transverse to the zero section while fixing the boundary.

:::

:::

::: {.pf-step #s1-6}

We may further arrange that on a collar
\[
\partial F\times[0,\varepsilon)
\]
the field \(w\) is independent of the collar coordinate and equals the
boundary tangent field \(T\).


::: pf-proof

The boundary field \(T\) is nowhere zero. Extend it constantly in the collar
direction. Since the relative Euler number is independent of the chosen
extension and zeros can be kept away from the collar, replace the original
extension by this collar-standard one and perturb only in the remaining
interior.

:::

:::

::: {.pf-step #s1-7}

The relative Euler number is the signed sum of the isolated zeros of
\(w\):
\[
\boxed{
e(TF,T)
=
\sum_{x\in w^{-1}(0)}
\operatorname{ind}_x(w)}.
\]


::: pf-proof

The extension \(w\) is transverse to the zero section, so its zeros are
isolated and carry the usual local signs. This signed count is the defining
evaluation of the relative Euler class on the relative fundamental class
\[
[F,\partial F].
\]

:::

:::

::: pf-step

Let
\[
DF
=
F_+\cup_{\partial F}F_-
\]
be the oriented double of \(F\).


::: pf-proof

Take two copies of \(F\), reverse the orientation on the second copy, and
identify corresponding boundary points. The result is a closed oriented
surface.

:::

:::

::: pf-step

Reflection across the seam defines a diffeomorphism
\[
\rho:F_-\to F_+
\]
that fixes \(\partial F\), preserves tangent directions to the boundary, and
reverses the collar-normal direction.


::: pf-proof

In collar coordinates
\[
(s,t)\in\partial F\times(-\varepsilon,\varepsilon),
\]
the reflection is
\[
\rho(s,t)=(s,-t).
\]
It fixes the \(s\)-direction and reverses the \(t\)-direction.

:::

:::

::: pf-step

Define a vector field \(W\) on the double by
\[
W|_{F_+}=w
\]
and
\[
W|_{F_-}=\rho^*w,
\]
using the reflected copy of \(w\).


::: pf-proof

On the collar, step [](#s1-6){.pf-ref} says \(w=T\) and is independent of the normal
coordinate. Since \(\rho\) fixes the tangential vector \(T\), the two
definitions agree smoothly along the seam. Thus they glue to a smooth vector
field \(W\) on \(DF\).

:::

:::

::: {.pf-step #s1-11}

The field \(W\) has no zeros on the seam.


::: pf-proof

Along the seam,
\[
W=T,
\]
and \(T\) is a unit tangent vector field, hence nowhere zero.

:::

:::

::: {.pf-step #s1-12}

Every zero \(x\) of \(w\) in \(F_+\) has a reflected zero
\[
x^-=\rho^{-1}(x)
\]
in \(F_-\), and there are no other zeros of \(W\).


::: pf-proof

On each copy away from the seam, \(W\) is exactly \(w\) or its reflected
copy. Step [](#s1-11){.pf-ref} rules out seam zeros.

:::

:::

::: {.pf-step #s1-13}

The two corresponding zeros have the same index:
\[
\boxed{
\operatorname{ind}_{x^-}(W)
=
\operatorname{ind}_{x}(w)}.
\]


::: pf-proof

The local index of a vector field is invariant under diffeomorphic change of
coordinates when the vector field is transported by the derivative. The
reflection reverses orientation both in the local domain and in the tangent
plane identification, so the two orientation signs cancel. Thus the degree
of the normalized vector field around the reflected zero is the same.

:::

:::

::: {.pf-step #s1-14}

Consequently,
\[
\boxed{
\sum_{z\in W^{-1}(0)}
\operatorname{ind}_z(W)
=
2e(TF,T)}.
\]


::: pf-proof

By steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref}, the zeros of \(W\) occur in reflected pairs with equal
indices. Summing the two copies of the index sum from step [](#s1-7){.pf-ref} gives the
formula.

:::

:::

::: {.pf-step #s1-15}

By the Poincaré--Hopf theorem for the closed surface \(DF\),
\[
\boxed{
\sum_{z\in W^{-1}(0)}
\operatorname{ind}_z(W)
=
\chi(DF)}.
\]


::: pf-proof

The double \(DF\) is closed and oriented, and \(W\) has isolated zeros.
Apply the usual boundaryless Poincaré--Hopf theorem.

:::

:::

::: {.pf-step #s1-16}

The Euler characteristic of the double is
\[
\boxed{
\chi(DF)=2\chi(F)}.
\]


::: pf-proof

Give \(F\) a finite CW structure with \(\partial F\) as a subcomplex.
The double is the union of two copies of \(F\) intersecting in
\(\partial F\). Euler characteristic is additive:
\[
\chi(DF)
=
2\chi(F)-\chi(\partial F).
\]
Every component of \(\partial F\) is a circle, and
\[
\chi(S^1)=0.
\]
Hence
\[
\chi(\partial F)=0.
\]

:::

:::

::: {.pf-step #s1-17}

Combining steps [](#s1-14){.pf-ref} through [](#s1-16){.pf-ref},
\[
2e(TF,T)
=
2\chi(F).
\]


::: pf-proof

Step [](#s1-14){.pf-ref} identifies the index sum with \(2e(TF,T)\), step [](#s1-15){.pf-ref} identifies
the same sum with \(\chi(DF)\), and step [](#s1-16){.pf-ref} identifies
\(\chi(DF)\) with \(2\chi(F)\).

:::

:::

::: {.pf-step #s1-18}

Therefore
\[
\boxed{
e(TF,T)=\chi(F)}.
\]


::: pf-proof

Divide the equality in step [](#s1-17){.pf-ref} by \(2\).

:::

:::

::: {.pf-step #s1-19}

Finally,
\[
\boxed{
e(TF,v)=\chi(F)}.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} gives
\[
e(TF,v)=e(TF,T),
\]
and step [](#s1-18){.pf-ref} computes the latter as \(\chi(F)\).

:::

:::

::: pf-qed

Step [](#s1-19){.pf-ref} is the Poincaré--Hopf formula requested in the exercise.

:::

:::

:::
