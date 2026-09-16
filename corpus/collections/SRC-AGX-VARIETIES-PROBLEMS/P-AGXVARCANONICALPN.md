---
schema: qual/card@1
id: P-AGXVARCANONICALPN
kind: problem
title: The canonical bundle of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Bundle
  - Line Bundles
  - Projective Space
relations: []
review: draft
---

::: {.problem}
Prove that the canonical bundle of $\PP^n$ is $\OO(n-1)$.
:::

::: {.remark}
The statement is false as written: the canonical bundle of $\PP^n$ is $\OO(-n-1)$.
For $n = 1$, the canonical divisor of $\PP^1$ has degree $2g - 2 = -2$, while $\OO(0)$ has degree $0$.
The Euler sequence $0 \to \OO \to \OO(1)^{\oplus (n+1)} \to T_{\PP^n} \to 0$ gives $\det T_{\PP^n} \cong \OO(n+1)$, so $\omega_{\PP^n} = \det T_{\PP^n}^\dual \cong \OO(-n-1)$.
:::
