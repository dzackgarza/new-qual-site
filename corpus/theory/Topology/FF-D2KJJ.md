---
schema: qual/card@1
id: FF-D2KJJ
kind: fact
title: Tor groups among $\ZZ/n$, $\ZZ$ and $\QQ$
prompts:
- What are the groups $\operatorname{Tor}^{\mathbf{Z}}_*$ among $\ZZ/n$, $\ZZ$ and $\QQ$?
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.fact}
Let $m, n\geq 1$ and $d\coloneqq\gcd(m,n)$.
For an abelian group $A$ let $A[n]\coloneqq\ts{a\in A \st na = 0}$.
Then $\Tor^{\ZZ}_0(\ZZ/n, A)\cong A/nA$, $\Tor^{\ZZ}_1(\ZZ/n, A)\cong A[n]$, $\Tor^{\ZZ}_k(\ZZ, A) = 0$ for $k\geq 1$, $\Tor^{\ZZ}_1(A, B)\cong\Tor^{\ZZ}_1(B, A)$, and $\Tor^{\ZZ}_1(A, B) = 0$ whenever $A$ or $B$ is torsion-free [@Hat02].
The groups $\Tor^{\ZZ}_0(V, W) = V\otimes_{\ZZ}W$ are

| $V \otimes_{\ZZ} W$ | $W=\ZZ/m$ | $W=\ZZ$ | $W=\QQ$ |
| :-- | :-- | :-- | :-- |
| $V=\ZZ/n$ | $\ZZ/d$ | $\ZZ/n$ | $0$ |
| $V=\ZZ$ | $\ZZ/m$ | $\ZZ$ | $\QQ$ |
| $V=\QQ$ | $0$ | $\QQ$ | $\QQ$ |

and the groups $\Tor^{\ZZ}_1(V, W)$ are

| $\Tor^{\ZZ}_1(V, W)$ | $W=\ZZ/m$ | $W=\ZZ$ | $W=\QQ$ |
| :-- | :-- | :-- | :-- |
| $V=\ZZ/n$ | $\ZZ/d$ | $0$ | $0$ |
| $V=\ZZ$ | $0$ | $0$ | $0$ |
| $V=\QQ$ | $0$ | $0$ | $0$ |

All higher groups $\Tor^{\ZZ}_k$, $k\geq 2$, vanish.
:::
