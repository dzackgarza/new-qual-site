---
schema: qual/card@1
id: FE-SRFBLOW
kind: example
title: What a blowup does to $\Pic$, to $K$, and to the intersection form
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Intersection Theory
  - Canonical Divisor
relations:
- kind: uses
  target: D-VARBLOW
- kind: uses
  target: D-SRFINT
review: draft
prompts:
- What happens to the Picard group under a blowup?
- Compute the self-intersection of an exceptional curve.
- How does the canonical divisor change under a blowup?
- What is the strict transform?
---

::: {.example}
Let $\pi \colon \tilde{X} = \Bl_p X \to X$ be the blowup of a smooth surface at a point, with exceptional curve $E \cong \PP^1$.
Then
\[
\Pic \tilde{X} = \pi^* \Pic X \oplus \ZZ E ,
\]
and the intersection numbers are
\[
\pi^*C \cdot \pi^*D = C \cdot D , \qquad \pi^*C \cdot E = 0 , \qquad E^2 = -1 .
\]
For the canonical divisor,
\[
K_{\tilde{X}} = \pi^* K_X + E , \qquad K_{\tilde{X}}^2 = K_X^2 - 1 ,
\]
and $\chi(\OO)$, $p_g$ and $q$ are unchanged.
:::

::: {.theorem title="Hironaka resolution (characteristic zero)"}
Let $k = \CC$.

(a) For every projective variety $Y$ there exist a smooth projective variety $Y'$ and a birational morphism $\varphi \colon Y' \to Y$ such that $\varphi$ is an isomorphism over $\reg Y$.

(b) For every smooth projective variety $X$ and projective subvariety $Y \subset X$ there exist a smooth projective variety $W$ and a birational morphism $\varphi \colon W \to X$ such that $\varphi^{-1}(Y)$ is a divisor with simple normal crossings in $W$.

(c) If $Y \subset X$ as in (b) is a hypersurface, there is a unique irreducible component $Y'$ of $\varphi^{-1}(Y)$ dominating $Y$, and $\varphi\vert_{Y'} \colon Y' \to Y$ is a desingularization as in (a); it is called an embedded desingularization of $Y$.

(d) In (a) and (b) the morphism $\varphi$ can be chosen as a composition of blowups with smooth centres.

In particular every projective variety admits a desingularization by a sequence of blowups with smooth centres, and every subvariety can be made SNC after such a sequence.
:::

::: {.definition title="Strict transform"}
For $C \subseteq X$ passing through $p$ with multiplicity $m$, the **strict transform** $\tilde{C}$ is the closure of $\pi^{-1}(C \setminus p)$, and
\[
\pi^* C = \tilde{C} + mE , \qquad \tilde{C}^2 = C^2 - m^2 , \qquad p_a(\tilde{C}) = p_a(C) - \binom{m}{2} .
\]
:::

::: {.remark}
$E^2 = -1$ is the fact the rest hangs on, and it follows from $\pi^*C \cdot E = 0$ applied to a curve through $p$: writing $\pi^*C = \tilde{C} + E$ for a smooth $C$ gives $0 = \tilde{C}\cdot E + E^2 = 1 + E^2$.

The genus drop is the tool for resolving plane curve singularities: blowing up an ordinary $m$-fold point removes $\binom{m}{2}$ from the arithmetic genus, which matches the delta invariant, so repeated blowups compute the geometric genus.
A node has $m=2$ and drops the genus by one.

$K^2$ decreasing by one while $\chi(\OO)$ stays fixed is the numerical fingerprint of a blowup, and it is what Noether's formula balances: $c_2$ goes up by one.
:::
