---
schema: qual/card@1
id: P-LKYOC
kind: problem
title: "11. First note that $\\pi_1(S^1\\cross S^1) \\cong F^2$, the free group o\u2026"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - surfaces
relations: []
review: draft
---
11. First note that $\pi_1(S^1\cross S^1) \cong F^2$, the free group on two generators, say $[\alpha], [\beta]$ corresponding to the two nontrivial loops on the torus - say $\alpha$ is the longitudinal loop, and $\beta$ is the meridian. Then if $\gamma$ is a loop on a torus, then you can just count how many times it winds longitudinally and around the meridian, say $m$ and $n$ times respectively. Then $\gamma$ can be homotoped into $m$ copies of $\alpha$ and $n$ copies of $\beta$ based at $x_0$. So the induced map is $f_\sharp: F^2 \into F^2$ given by $\alpha \mapsto \alpha^m, \beta \mapsto \beta^n$. Since $F^2 \cong Z\cross Z$, we equivalently have $[\alpha] = (1,0), [\beta] = (0,1)$, and then $f_\sharp : Z^2 \into Z^2$ is given by $(1,0) \mapsto (m,0)$ and $(0,1) \mapsto (0,n)$.

