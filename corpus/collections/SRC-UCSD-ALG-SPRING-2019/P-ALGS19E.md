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
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $A$ is a unital commutative ring, and $P_1$ and $P_2$ are finitely generated projective $A$-modules.
Prove that $\operatorname{Hom}_A(P_1, P_2)$ is a projective $A$-module.
:::


::: {.solution}
<1>1. Since \(P_1\) and \(P_2\) are finitely generated projective, there are finitely generated modules \(Q_1,Q_2\) and integers \(m,n\ge 0\) such that
\[
P_1\oplus Q_1\cong A^m,
\qquad
P_2\oplus Q_2\cong A^n.
\]
::: {.proof}
A finitely generated projective module is a direct summand of a finite free module.
:::

<1>2. There is a canonical decomposition
\[
\operatorname{Hom}_A(P_1\oplus Q_1,P_2\oplus Q_2)
\cong
\operatorname{Hom}_A(P_1,P_2)
\oplus\operatorname{Hom}_A(P_1,Q_2)
\oplus\operatorname{Hom}_A(Q_1,P_2)
\oplus\operatorname{Hom}_A(Q_1,Q_2).
\]
::: {.proof}
A homomorphism from a direct sum to a direct sum is uniquely determined by its four component maps obtained by composing with the two inclusions in the source and the two projections in the target. Conversely, any four such component maps assemble uniquely into a homomorphism.
:::

<1>3. The module on the left of <1>2 is finite free:
\[
\operatorname{Hom}_A(A^m,A^n)\cong A^{mn}.
\]
::: {.proof}
After the identifications in <1>1, an \(A\)-linear map \(A^m\to A^n\) is uniquely represented by an \(n\times m\) matrix with entries in \(A\), giving the stated free module of rank \(mn\).
:::

<1>4. Therefore \(\operatorname{Hom}_A(P_1,P_2)\) is projective.
::: {.proof}
By <1>2 and <1>3, \(\operatorname{Hom}_A(P_1,P_2)\) is a direct summand of the free module \(A^{mn}\). Every direct summand of a free module is projective.
:::
:::
