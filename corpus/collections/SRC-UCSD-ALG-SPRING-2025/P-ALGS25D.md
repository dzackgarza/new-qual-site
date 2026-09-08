---
schema: qual/card@1
id: P-ALGS25D
kind: problem
title: Hom of finitely generated projective modules is projective
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Projective Modules
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
Let $A$ be a unital commutative ring.
Suppose $M$ and $N$ are two finitely generated projective $A$-modules.
Prove that $\operatorname{Hom}_A(M, N)$ is a projective $A$-module.
:::


::: {.solution}
<1>1. Since \(M\) is finitely generated projective, there exist an integer \(r\ge0\) and an \(A\)-module \(M'\) such that
\[
M\oplus M'\cong A^r.
\]
::: {.proof}
A finitely generated projective module is a direct summand of a finite free module.
:::

<1>2. The dual module
\[
M^\vee=\operatorname{Hom}_A(M,A)
\]
is finitely generated projective.
::: {.proof}
Apply \(\operatorname{Hom}_A(-,A)\) to the direct-sum isomorphism in <1>1. Since Hom sends a finite direct sum in the first variable to a direct sum,
\[
M^\vee\oplus (M')^\vee
\cong
\operatorname{Hom}_A(A^r,A)
\cong A^r.
\]
Thus \(M^\vee\) is a direct summand of a finite free module.
:::

<1>3. Since \(N\) is finitely generated projective, there exist an integer \(s\ge0\) and an \(A\)-module \(N'\) such that
\[
N\oplus N'\cong A^s.
\]
::: {.proof}
Again use that finitely generated projective modules are direct summands of finite free modules.
:::

<1>4. Applying \(\operatorname{Hom}_A(M,-)\) to <1>3 gives
\[
\operatorname{Hom}_A(M,N)
\oplus
\operatorname{Hom}_A(M,N')
\cong
\operatorname{Hom}_A(M,A^s)
\cong
(M^\vee)^s.
\]
::: {.proof}
Hom in the second variable preserves finite direct sums, and
\[
\operatorname{Hom}_A(M,A^s)
\cong
\operatorname{Hom}_A(M,A)^s.
\]
:::

<1>5. The module \((M^\vee)^s\) is projective.
::: {.proof}
By <1>2, \(M^\vee\) is projective. A finite direct sum of projective modules is projective.
:::

<1>6. Therefore \(\operatorname{Hom}_A(M,N)\) is projective.
::: {.proof}
By <1>4 it is a direct summand of the projective module \((M^\vee)^s\). Direct summands of projective modules are projective.
:::
:::
