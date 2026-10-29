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
$$
\Pic \tilde{X} = \pi^* \Pic X \oplus \ZZ E ,
$$
and the intersection numbers are
$$
\pi^*C \cdot \pi^*D = C \cdot D , \qquad \pi^*C \cdot E = 0 , \qquad E^2 = -1 .
$$
For the canonical divisor,
$$
K_{\tilde{X}} = \pi^* K_X + E , \qquad K_{\tilde{X}}^2 = K_X^2 - 1 ,
$$
and $\chi(\OO)$, $p_g$ and $q$ are unchanged.
:::

::: {.theorem title="Hironaka resolution (characteristic zero)"}
Let $k = \CC$.

(a) For every projective variety $Y$ there exist a smooth projective variety $Y'$ and a birational morphism $\varphi \colon Y' \to Y$ such that $\varphi$ is an isomorphism over $\reg Y$.

(b) For every smooth projective variety $X$ and proper closed subvariety $Y \subsetneq X$ there exist a smooth projective variety $W$ and a birational morphism $\varphi \colon W \to X$ such that $\varphi^{-1}(Y)$ is a divisor with simple normal crossings in $W$.

(c) If $Y \subset X$ as in (b) is an irreducible hypersurface, there is a unique irreducible component $Y'$ of $\varphi^{-1}(Y)$ dominating $Y$, and $\varphi\vert_{Y'} \colon Y' \to Y$ is a desingularization as in (a); it is called an embedded desingularization of $Y$.

(d) In (a) and (b) the morphism $\varphi$ can be chosen as a composition of blowups with smooth centres.

In particular every projective variety admits a desingularization by a sequence of blowups with smooth centres, and the preimage of every proper closed subvariety of a smooth projective variety becomes a simple normal crossings divisor after such a sequence.
:::

::: {.definition title="Strict transform"}
For a curve $C \subseteq X$ passing through $p$ with multiplicity $m$, the \dfn{strict transform} $\tilde{C}$ is the closure of $\pi^{-1}(C \setminus p)$, and
$$
\pi^* C = \tilde{C} + mE , \qquad \tilde{C}^2 = C^2 - m^2 , \qquad p_a(\tilde{C}) = p_a(C) - \binom{m}{2} .
$$
:::

::: {.remark}
$E^2=-1$ follows from $\pi^*C\cdot E=0$ applied to a smooth curve $C$ through $p$: writing $\pi^*C=\tilde C+E$ gives $0=\tilde C\cdot E+E^2=1+E^2$.

Blowing up an ordinary $m$-fold point lowers the arithmetic genus by $\binom{m}{2}$, matching its delta invariant; repeated blowups therefore recover the geometric genus from the plane model.
A node has $m=2$ and drops the genus by one.

By Noether's formula $12\chi(\OO) = K^2 + c_2$, the drop of $K^2$ by one with $\chi(\OO)$ fixed means that $c_2$ goes up by one.
:::
