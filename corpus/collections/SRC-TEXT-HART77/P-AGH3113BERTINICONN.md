---
schema: qual/card@1
id: P-AGH3113BERTINICONN
kind: problem
title: Connectedness of divisors in a base point free linear system
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Bertini's Theorem
  - Linear Systems
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.3 with its indicated references III.11.5,
    III.5.7(d), and III.7.9. Independently reconstructed the Stein-factor
    argument, including normality of the Stein target and the topological
    lemma that a closed surjection with connected fibres pulls connected
    subsets back to connected subsets, then compared it with the standard
    proof of the exercise.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a normal, projective variety over an algebraically closed field $k$.
Let $D$ be a linear system of effective Cartier divisors without base points, and assume that $D$ is **not composite with a pencil**, which means that if $f: X \to \PP_k^n$ is the morphism determined by $D$, then $\dim f(X) \geq 2$.

Show that every divisor in $D$ is connected.

Hints: see (10.9.1); use (11.5), (Ex.
5.7) and (7.9).
:::

::: {.solution}
Write $\mathcal D$ for the given base-point-free linear system, and let
$$
f:X\longrightarrow\PP_k^n
$$
be the associated morphism. Put
$$
Z=f(X)
$$
with its reduced induced structure.

::: pf

::: {.pf-step #s1}

Every member of $\mathcal D$ is the inverse image of a hyperplane
section of $Z$.

::: pf-proof

The morphism $f$ is defined by the vector space of sections underlying
$\mathcal D$. Hence
$$
\mco_X(D_0)\cong f^*\mco_{\PP^n}(1)
$$
for the divisor class $D_0$ represented by the system.

A member $D\in\mathcal D$ is the zero scheme of a nonzero linear
combination of these defining sections. The same linear combination defines a
hyperplane
$$
H\subset\PP_k^n,
$$
and scheme-theoretically
$$
D=f^{-1}(H)=f^*(H|_Z).
$$
Since the corresponding section is nonzero, $Z$ is not contained in $H$.
Thus $H|_Z$ is an effective Cartier divisor on the integral variety $Z$.

:::

:::

::: {.pf-step #s2}

The morphism $f:X\to Z$ has a factorization
$$
X\xrightarrow{h}Y\xrightarrow{g}Z
$$
such that $h$ is projective with connected fibres and $g$ is finite
surjective.

::: pf-proof

This is the Stein factorization [@Har10a, Corollary III.11.5], applied after
replacing the original target by the image $Z$. By construction,
$$
h_*\mco_X=\mco_Y.
$$
The map $g$ is surjective because $f$ is surjective onto $Z$.

:::

:::

::: {.pf-step #s3}

The variety $Y$ is normal, projective, and has dimension at least $2$.

::: pf-proof

First, $Y$ is irreducible because it is the image of the irreducible variety
$X$ under the surjective map $h$. It is reduced because for every open
$V\subseteq Y$,
$$
\Gamma(V,\mco_Y)
=
\Gamma(h^{-1}(V),\mco_X),
$$
and $X$ is reduced.

To prove normality, let $V\subseteq Y$ be affine and let
$$
a\in K(Y)
$$
be integral over $\Gamma(V,\mco_Y)$. Pulling back along the dominant map
$h$, the element $h^*a\in K(X)$ is integral over
$$
\Gamma(h^{-1}(V),\mco_X)
=
\Gamma(V,\mco_Y).
$$
A normal integral scheme has integrally closed rings of regular functions on
all open subsets, since such a ring is the intersection of its normal local
rings inside the function field. Hence
$$
h^*a\in\Gamma(h^{-1}(V),\mco_X)
=
\Gamma(V,\mco_Y).
$$
Since $h$ is dominant, $K(Y)\to K(X)$ is injective. The last equality
therefore implies
$$
a\in\Gamma(V,\mco_Y).
$$
Thus $Y$ is normal.

Since $g$ is finite and $Z$ is projective, $Y$ is projective. Moreover a
finite surjective morphism preserves dimension, so
$$
\dim Y=\dim Z=\dim f(X)\ge2.
$$

:::

:::

::: {.pf-step #s4}

For the hyperplane $H$ associated to a member $D\in\mathcal D$, the
divisor
$$
E=g^*(H|_Z)
$$
is an effective ample Cartier divisor on $Y$.

::: pf-proof

By step [](#s1){.pf-ref}, $H|_Z$ is an effective Cartier divisor and
$$
\mco_Z(H|_Z)=\mco_{\PP^n}(1)|_Z
$$
is ample.
Because $g:Y\to Z$ is finite surjective, pullback preserves ampleness by
[@Har10a, Exercise III.5.7(d)]. Therefore
$$
\mco_Y(E)=g^*\mco_Z(H|_Z)
$$
is ample. Pullback of the defining nonzerodivisor of $H|_Z$ remains nonzero
on the integral scheme $Y$, so $E$ is an effective Cartier divisor.

:::

:::

::: {.pf-step #s5}

The support $|E|$ is connected.

::: pf-proof

By step [](#s3){.pf-ref}, $Y$ is a normal projective variety of dimension at least $2$.
By step [](#s4){.pf-ref}, $|E|$ is the support of an effective ample divisor.
The Enriques--Severi--Zariski connectedness theorem
[@Har10a, Corollary III.7.9] therefore gives
$$
\boxed{|E|\text{ is connected}.}
$$

:::

:::

::: {.pf-step #s6}

If $C\subseteq Y$ is connected, then $h^{-1}(C)$ is connected.

::: pf-proof

The projective morphism $h$ is closed, surjective, and has connected fibres.
Suppose, to the contrary, that
$$
h^{-1}(C)=A\amalg B
$$
is a separation into two nonempty subsets closed in $h^{-1}(C)$. The
restriction
$$
h^{-1}(C)\longrightarrow C
$$
is again a closed map: if $F=F'\cap h^{-1}(C)$ with $F'\subseteq X$ closed,
then
$$
h(F)=h(F')\cap C.
$$
Hence $h(A)$ and $h(B)$ are closed in $C$, and they cover $C$.

They are disjoint. Indeed, if
$$
y\in h(A)\cap h(B),
$$
then the connected fibre $h^{-1}(y)$ meets both $A$ and $B$. But
$$
h^{-1}(y)
=
(h^{-1}(y)\cap A)\amalg(h^{-1}(y)\cap B)
$$
would then be a separation of that fibre, a contradiction.

Thus $C=h(A)\amalg h(B)$ is disconnected, contrary to the hypothesis.
Hence $h^{-1}(C)$ is connected.

:::

:::

::: pf-step

Every divisor $D\in\mathcal D$ is connected.

::: pf-proof

For the hyperplane $H$ corresponding to $D$, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
D=f^*(H|_Z)
=
h^*g^*(H|_Z)
=
h^*E.
$$
Consequently
$$
|D|=h^{-1}(|E|).
$$
Step [](#s5){.pf-ref} says that $|E|$ is connected, and step [](#s6){.pf-ref} says its inverse image
under $h$ is connected. Therefore $|D|$ is connected, which is exactly to say
that the divisor scheme $D$ is connected.

:::

:::

::: pf-qed

The argument applies to every hyperplane, hence to every member of the
base-point-free linear system $\mathcal D$. Thus every divisor in
$\mathcal D$ is connected.

:::

:::

:::
