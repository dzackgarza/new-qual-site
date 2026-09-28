---
schema: qual/card@1
id: P-1IM1B
kind: problem
title: The sum of (skew-)symmetric matrices is (skew-)symmetric
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $M_n(F)$ be the space of $n \times n$ matrices over a field $F$.

1. Prove that the sum and scalar multiples of symmetric matrices are symmetric (so symmetric matrices form a subspace of $M_n(F)$).

2. Prove that the sum and scalar multiples of skew-symmetric matrices are skew-symmetric (so skew-symmetric matrices form a subspace of $M_n(F)$).

3. If $\operatorname{char}(F) \neq 2$, prove that $M_n(F) = \operatorname{Sym}_n(F) \oplus \operatorname{Skew}_n(F)$ as an internal direct sum.
:::

::: {.solution}
Let $\operatorname{Sym}_n(F)=\{A:A^t=A\}$ and $\operatorname{Skew}_n(F)=\{A:A^t=-A\}$.

<1>1. $\operatorname{Sym}_n(F)$ and $\operatorname{Skew}_n(F)$ are subspaces of $M_n(F)$.

::: {.proof}
Both contain $0$.
For $A,B$ in one of them, $c\in F$, and $\varepsilon=\pm1$ with $A^t=\varepsilon A$, $B^t=\varepsilon B$, linearity of the transpose gives $(cA+B)^t=cA^t+B^t=\varepsilon(cA+B)$.
:::

<1>2. If $\operatorname{char}(F)\neq2$, then $M_n(F)=\operatorname{Sym}_n(F)+\operatorname{Skew}_n(F)$.

::: {.proof}
For $M\in M_n(F)$, $M=\frac{M+M^t}2+\frac{M-M^t}2$, and $(M^t)^t=M$ shows that the first summand is symmetric and the second skew-symmetric.
:::

<1>3. If $\operatorname{char}(F)\neq2$, then $\operatorname{Sym}_n(F)\cap\operatorname{Skew}_n(F)=0$.

::: {.proof}
If $X=X^t=-X$, then $2X=0$, and $2$ is invertible in $F$, so $X=0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 gives parts 1 and 2, and steps <1>2 and <1>3 give part 3.
:::
:::
