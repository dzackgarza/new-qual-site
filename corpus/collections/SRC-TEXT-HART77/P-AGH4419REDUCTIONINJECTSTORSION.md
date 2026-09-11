---
schema: qual/card@1
id: P-AGH4419REDUCTIONINJECTSTORSION
kind: problem
title: Reduction mod $p$ injects the prime-to-$p$ torsion of $X(\QQ)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
---

::: problem
Let $X, P_0$ be an elliptic curve defined over $\QQ$, represented as a curve in $\PP^2$ defined by an equation with integer coefficients. Then $X$ can be considered as the fibre over the generic point of a scheme $\bar{X}$ over $\Spec \ZZ$. Let $T \subseteq \Spec \ZZ$ be the open subset consisting of all primes $p \neq 2$ such that the fibre $X_{(p)}$ of $\bar{X}$ over $p$ is nonsingular.

- For any $n$, show that $n_X: X \to X$ is defined over $T$, and is a flat morphism.
- Show that the kernel of $n_X$ is also flat over $T$.
- Conclude that for any $p \in T$, the natural map $X(\QQ) \to X_{(p)}(\FF_p)$ induced on the groups of rational points, maps the $n$-torsion points of $X(\QQ)$ injectively into the torsion subgroup of $X_{(p)}(\FF_p)$, for any $(n, p)=1$.

By this method one can show easily that the groups $X(\QQ)$ in (Ex. 4.17) and (Ex. 4.18) are torsion-free.
:::
