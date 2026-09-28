---
schema: qual/card@1
id: D-IV2ETCOV
kind: definition
title: Étale covers, trivial covers, and simple connectedness of $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Étale Morphisms
  - Fundamental Group
  - Riemann-Hurwitz
relations:
- kind: uses
  target: D-MORETALE
- kind: uses
  target: T-LKT0U
review: draft
prompts:
- What is an étale cover, and what is a trivial one?
- What does it mean for a curve to be simply connected?
- Prove that $\PP^1$ has no nontrivial étale covers.
- Is $\AA^1$ simply connected?
---

::: {.definition title="Étale cover"}
A morphism $f : X \to Y$ is an \dfn{étale cover} if it is finite and étale.
It is a \dfn{trivial} cover if $X \cong \coprod_{i \in I} Y$ for a finite index set $I$, with $f$ the identity on each copy.
$Y$ is \dfn{simply connected} if every étale cover of $Y$ is trivial, equivalently $\pi_1^{\Et}(Y) = 0$.
:::

::: {.theorem}
$\PP^1_k$ over $k = \kbar$ is simply connected, in every characteristic.
:::

::: {.proof}
Let $f : X \to \PP^1$ be an étale cover; it is enough to treat $X$ connected, and then to show $f$ is an isomorphism.
$X$ is regular because $f$ is étale and $\PP^1$ is smooth over $k$, and a connected regular scheme is irreducible, so $X$ is a curve; $f$ is finite, so $X$ is projective; $f$ is unramified, so $k(X)/k(\PP^1)$ is separable.
Riemann--Hurwitz therefore applies, and $R = 0$ since $f$ is unramified, so with $n = \deg f$,
$$
2 g_X - 2 = n(2 \cdot 0 - 2) = -2n .
$$
Then $g_X \geq 0$ gives $-2n \geq -2$, so $n = 1$ and $g_X = 0$, and a finite morphism of degree $1$ between curves is an isomorphism.
:::

::: {.remark title="Topological analogue"}
For a connected covering space $S\to S^2$ of degree $n$, $\chi(S)=n\chi(S^2)=2n$, and $\chi(S)\le2$ for a compact connected surface, so $n=1$; the proof above replaces $\chi$ by $2-2g$ and the covering space by a finite étale morphism.
:::

::: {.example title="The affine line in characteristic $p$"}
Let $\operatorname{char}k=p>0$.
The Artin--Schreier cover $\Spec k[x,y]/(y^p - y - x)\to\AA^1$, $(x,y)\mapsto x$, is finite étale of degree $p$ and connected, because $d(y^p - y) = -dy$ never vanishes; so $\AA^1_k$ is not simply connected.
The cover extends to a morphism $\PP^1\to\PP^1$ that is totally and wildly ramified at $\infty$ ([[D-IV2RAM]]).
Over $\CC$, $\AA^1$ has no nontrivial finite étale covers.
:::

::: {.remark title="Finite étale covers"}
Étale morphisms are defined in [[D-MORETALE]].
For a proper nonempty open subset $U\subseteq Y$, the morphism $U\sqcup Y\to Y$ is étale and surjective but not finite, and it is not of the form $\coprod_{i\in I}Y\to Y$.
:::
