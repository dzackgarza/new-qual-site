---
schema: qual/card@1
id: P-LKYOC
kind: problem
title: "11. First note that $\\pi_1(S^1\\cross S^1) \\cong \\ZZ^2$, the free abelian group o…"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - surfaces
relations: []
review: draft
solved: false
---

11. First note that $\pi_1(S^1\cross S^1) \cong \ZZ^2$, the free **abelian** group on two generators, say $[\alpha], [\beta]$ corresponding to the two nontrivial loops on the torus - say $\alpha$ is the longitudinal loop, and $\beta$ is the meridian.
    Then if $\gamma$ is a loop on a torus, then you can just count how many times it winds longitudinally and around the meridian, say $m$ and $n$ times respectively.
    Then $\gamma$ can be homotoped into $m$ copies of $\alpha$ and $n$ copies of $\beta$ based at $x_0$.
    So the induced map is $f_\sharp: \ZZ^2 \into \ZZ^2$ given by $\alpha \mapsto \alpha^m, \beta \mapsto \beta^n$.
    Writing $[\alpha] = (1,0)$ and $[\beta] = (0,1)$, the map $f_\sharp : \ZZ^2 \into \ZZ^2$ is given by $(1,0) \mapsto (m,0)$ and $(0,1) \mapsto (0,n)$.

::: {.remark}
This solution named $\pi_1(S^1\cross S^1)$ the free group $F_2$ and then asserted $F_2 \cong \ZZ\cross\ZZ$.
Both are wrong, and the second is what the first forces: $F_2$ is nonabelian, $\ZZ\cross\ZZ$ is abelian, so they are not isomorphic.
The torus has $\pi_1 = \gens{a,b \suchthat aba\inv b\inv} \cong \ZZ\cross\ZZ$, the free *abelian* group on two generators — Hatcher records the torus as a $K(\ZZ\cross\ZZ, 1)$ in §2.2. The winding-number argument the rest of the card gives is the abelian one and is unaffected.
:::
