---
schema: qual/card@1
id: P-ALGS19E
kind: problem
title: "Hom of finitely generated projective modules is projective"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Suppose $A$ is a unital commutative ring, and $P_1$ and $P_2$ are finitely generated projective $A$-modules.
Prove that $\operatorname{Hom}_A(P_1, P_2)$ is a projective $A$-module.
:::


::: {.solution}
<1>1. Since \(P_1\) and \(P_2\) are finitely generated projective, there exist finitely generated modules \(Q_1,Q_2\) and integers \(m,n\ge 0\) such that
\[
P_1\oplus Q_1\cong A^m,
\qquad
P_2\oplus Q_2\cong A^n.
\]
::: {.proof}
A finitely generated projective module is a direct summand of a finite free module. Indeed, choose a surjection \(A^m\twoheadrightarrow P_1\); projectivity splits it, so \(A^m\cong P_1\oplus Q_1\). The same argument applies to \(P_2\).
:::

<1>2. There is a natural direct-sum decomposition
\[
\operatorname{Hom}_A(P_1\oplus Q_1,P_2\oplus Q_2)
\cong
\operatorname{Hom}_A(P_1,P_2)
\oplus\operatorname{Hom}_A(P_1,Q_2)
\oplus\operatorname{Hom}_A(Q_1,P_2)
\oplus\operatorname{Hom}_A(Q_1,Q_2).
\]
::: {.proof}
A homomorphism from \(P_1\oplus Q_1\) to \(P_2\oplus Q_2\) is uniquely determined by its four component maps obtained by composing the two source inclusions with the two target projections. Conversely, any four such component maps assemble uniquely to a homomorphism of the direct sums.
:::

<1>3. The module in the left-hand side of <1>2 is finite free:
\[
\operatorname{Hom}_A(P_1\oplus Q_1,P_2\oplus Q_2)
\cong \operatorname{Hom}_A(A^m,A^n)
\cong A^{mn}.
\]
::: {.proof}
Use the isomorphisms from <1>1. An \(A\)-linear map \(A^m\to A^n\) is uniquely specified by an \(n\times m\) matrix with entries in \(A\), and the set of such matrices is the free \(A\)-module \(A^{mn}\).
:::

<1>4. Therefore \(\operatorname{Hom}_A(P_1,P_2)\) is projective.
::: {.proof}
By <1>2 and <1>3, \(\operatorname{Hom}_A(P_1,P_2)\) is a direct summand of the free module \(A^{mn}\). Every direct summand of a free module is projective.
:::
:::
