---
schema: qual/card@1
id: P-LKYOC
kind: problem
title: Winding-number isomorphism $\pi_1(T^2)\cong\ZZ^2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

11. First note that $\pi_1(S^1\cross S^1) \cong \ZZ^2$, the free **abelian** group on two generators, say $[\alpha], [\beta]$ corresponding to the two nontrivial loops on the torus - say $\alpha$ is the longitudinal loop, and $\beta$ is the meridian.
    Then if $\gamma$ is a loop on a torus, then you can just count how many times it winds longitudinally and around the meridian, say $m$ and $n$ times respectively.
    Then $\gamma$ can be homotoped into $m$ copies of $\alpha$ and $n$ copies of $\beta$ based at $x_0$.
    So the induced map is $f_\sharp: \ZZ^2 \into \ZZ^2$ given by $\alpha \mapsto \alpha^m, \beta \mapsto \beta^n$.
    Writing $[\alpha] = (1,0)$ and $[\beta] = (0,1)$, the map $f_\sharp : \ZZ^2 \into \ZZ^2$ is given by $(1,0) \mapsto (m,0)$ and $(0,1) \mapsto (0,n)$.

::: {.solution}
<1>1. $\pi_1(S^1 \times S^1) \cong \pi_1(S^1) \times \pi_1(S^1) \cong \ZZ \times \ZZ$.
Proof: the fundamental group of a product is the product of the fundamental groups, and $\pi_1(S^1) \cong \ZZ$.

<1>2. Let $\alpha$ be the longitudinal loop and $\beta$ the meridian; then $[\alpha] = (1,0)$ and $[\beta] = (0,1)$ generate $\ZZ^2$.
Proof: <1>1, with the two circle factors corresponding to the two coordinate loops.

<1>3. A loop $\gamma$ on the torus winds $m$ times longitudinally and $n$ times meridionally.
Proof: the winding numbers are the images of $[\gamma]$ under the two projections $\pi_1(T^2) \to \pi_1(S^1) \cong \ZZ$.

<1>4. Hence $[\gamma] = m[\alpha] + n[\beta] = (m, n) \in \ZZ^2$.
Proof: <1>2 and <1>3, since $\ZZ^2$ is free abelian on $[\alpha], [\beta]$.

<1>5. The induced map $f_\sharp : \ZZ^2 \to \ZZ^2$ sends $\alpha \mapsto \alpha^m$ and $\beta \mapsto \beta^n$, i.e. $(1,0) \mapsto (m,0)$ and $(0,1) \mapsto (0,n)$.
Proof: <1>4, reading off the winding numbers of the image loop.

<1>6. Q.E.D.
Proof: <1>1 and <1>5.
:::

::: {.remark}
This solution named $\pi_1(S^1\cross S^1)$ the free group $F_2$ and then asserted $F_2 \cong \ZZ\cross\ZZ$.
Both are wrong, and the second is what the first forces: $F_2$ is nonabelian, $\ZZ\cross\ZZ$ is abelian, so they are not isomorphic.
The torus has $\pi_1 = \gens{a,b \suchthat aba\inv b\inv} \cong \ZZ\cross\ZZ$, the free *abelian* group on two generators — Hatcher records the torus as a $K(\ZZ\cross\ZZ, 1)$ in §2.2. The winding-number argument the rest of the card gives is the abelian one and is unaffected.
:::
