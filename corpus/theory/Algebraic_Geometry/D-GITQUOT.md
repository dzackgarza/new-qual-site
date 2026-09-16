---
schema: qual/card@1
id: D-GITQUOT
kind: definition
title: GIT quotients
classification:
  areas:
  - algebraic-geometry
  topics:
  - Geometric Invariant Theory
  - Group Actions
  - Quotients
relations: []
review: draft
prompts:
- What is a GIT quotient?
---

::: {.definition title="Affine GIT quotient"}
Let $G$ be a reductive group over an algebraically closed field $k$ acting on an affine variety $X = \Spec A$.
The ring of invariants $A^G$ is finitely generated, and the \dfn{GIT quotient} is $X /\!\!/ G = \Spec A^G$, with the morphism $\pi \colon X \to X/\!\!/G$ induced by $A^G \subseteq A$.
:::

::: {.proposition}
$\pi$ is surjective and constant on orbits, and $\pi(x) = \pi(y)$ exactly when the orbit closures $\overline{Gx}$ and $\overline{Gy}$ meet.
Each fibre contains a unique closed orbit, so the closed points of $X/\!\!/G$ correspond to closed $G$-orbits in $X$.
:::

::: {.definition title="Projective GIT quotient"}
If $G$ acts on a projective variety $X$ with a $G$-linearized ample line bundle $L$, a point $x$ is \dfn{semistable} if some invariant section $s \in H^0(X, L^m)^G$ has $s(x) \neq 0$.
The GIT quotient is $X /\!\!/_L G = \Proj \bigoplus_{m \geq 0} H^0(X, L^m)^G$, a projective variety receiving a morphism from the open set $X^{ss}$ of semistable points.
:::

::: {.example}
Let $\GG_m$ act on $\AA^2$.
With weights $(1,1)$, $k[x,y]^{\GG_m} = k$ and $\AA^2/\!\!/\GG_m$ is a point, because every orbit closure contains the origin.
With weights $(1,-1)$, $k[x,y]^{\GG_m} = k[xy]$ and $\AA^2/\!\!/\GG_m = \AA^1$; the fibre over $0$ is the union of the two axes and contains three orbits, of which only the origin is closed.
With weights $(1,1)$ and the linearization $\OO$ twisted by the identity character, the semistable locus is $\AA^2 \setminus \{0\}$ and the projective quotient is $\PP^1$.
:::
