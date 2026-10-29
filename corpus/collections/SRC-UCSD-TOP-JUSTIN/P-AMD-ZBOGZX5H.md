---
schema: qual/card@1
id: P-AMD-ZBOGZX5H
kind: problem
title: $H^1(X)$ is torsion-free, and free abelian when $H_1(X)$ is finitely generated
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked to show H^1(X) is free abelian for any space X, false for a wedge of countably many circles, where H^1 is Z^N; the statement now asks for torsion-free in general and free abelian when H_1(X) is finitely generated.'
---

::: {.problem}
For any space $X$, show that $H^1(X)$ is torsion-free, and that it is free abelian if $H_1(X)$ is finitely generated.
:::

::: {.solution}
Homology and cohomology have integer coefficients.

::: pf

::: {.pf-step #uct}

$H^1(X) \cong \operatorname{Hom}(H_1(X), \ZZ)$.

::: pf-proof

The universal coefficient theorem gives a split exact sequence $0 \to \operatorname{Ext}(H_0(X), \ZZ) \to H^1(X) \to \operatorname{Hom}(H_1(X), \ZZ) \to 0$. $H_0(X)$ is free abelian on the path components of $X$, so the Ext term vanishes.

:::

:::

::: pf-step

$H^1(X)$ is torsion-free.

::: pf-proof

By step [](#uct){.pf-ref} it suffices that $\operatorname{Hom}(A, \ZZ)$ is torsion-free for every abelian group $A$. If $k\varphi = 0$ with $k \ne 0$, then $k\varphi(a) = 0$ in $\ZZ$, so $\varphi(a) = 0$ for every $a \in A$.

:::

:::

::: pf-step

If $H_1(X)$ is finitely generated, $H^1(X)$ is free abelian.

::: pf-proof

Write $H_1(X) \cong \ZZ^r \oplus T$ with $T$ finite. Every homomorphism from the torsion group $T$ to $\ZZ$ is zero, so by step [](#uct){.pf-ref} $H^1(X) \cong \operatorname{Hom}(\ZZ^r, \ZZ) \cong \ZZ^r$.

:::

:::

:::

:::
