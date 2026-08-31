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

::: problem
Let $M_n(F)$ be the space of $n \times n$ matrices over a field $F$.

1. Prove that the sum and scalar multiples of symmetric matrices are symmetric (so symmetric matrices form a subspace of $M_n(F)$).

2. Prove that the sum and scalar multiples of skew-symmetric matrices are skew-symmetric (so skew-symmetric matrices form a subspace of $M_n(F)$).

3. If $\operatorname{char}(F) \neq 2$, prove that $M_n(F) = \operatorname{Sym}_n(F) \oplus \operatorname{Skew}_n(F)$ as an internal direct sum.
:::

::: {.solution}
<1>1. Symmetric matrices $\operatorname{Sym}_n(F) = \{A \in M_n(F) : A^t = A\}$ form a subspace: <2>1. The zero matrix satisfies $0^t = 0$, so $0 \in \operatorname{Sym}_n(F)$.
::: {.proof}
transpose of zero matrix is zero.
:::
<2>2. Let $A, B \in \operatorname{Sym}_n(F)$ and $c \in F$.
By the linearity of the transpose map:
\[
(cA + B)^t = c A^t + B^t = cA + B.
\]
::: {.proof}
$(A + B)^t = A^t + B^t$ and $(cA)^t = c A^t$.
:::
<2>3. Thus $cA + B \in \operatorname{Sym}_n(F)$, so $\operatorname{Sym}_n(F)$ is a subspace of $M_n(F)$.
::: {.proof}
subspace criterion.
:::

<1>2. Skew-symmetric matrices $\operatorname{Skew}_n(F) = \{A \in M_n(F) : A^t = -A\}$ form a subspace: <2>1. The zero matrix satisfies $0^t = 0 = -0$, so $0 \in \operatorname{Skew}_n(F)$.
::: {.proof}
transpose of zero matrix.
:::
<2>2. Let $A, B \in \operatorname{Skew}_n(F)$ and $c \in F$.
By the linearity of the transpose map:
\[
(cA + B)^t = c A^t + B^t = c(-A) + (-B) = -(cA + B).
\]
::: {.proof}
linearity of transpose.
:::
<2>3. Thus $cA + B \in \operatorname{Skew}_n(F)$, so $\operatorname{Skew}_n(F)$ is a subspace of $M_n(F)$.
::: {.proof}
subspace criterion.
:::

<1>3. Direct sum decomposition when $\operatorname{char}(F) \neq 2$: <2>1. For any matrix $M \in M_n(F)$, write:
\[
M = \frac{M + M^t}{2} + \frac{M - M^t}{2}.
\]
::: {.proof}
algebraic identity using $2 \neq 0$ in $F$.
:::
<2>2. Let $S = \frac{M + M^t}{2}$ and $K = \frac{M - M^t}{2}$.
Compute $S^t = \frac{M^t + (M^t)^t}{2} = \frac{M^t + M}{2} = S \in \operatorname{Sym}_n(F)$.
Compute $K^t = \frac{M^t - (M^t)^t}{2} = \frac{M^t - M}{2} = -K \in \operatorname{Skew}_n(F)$.
::: {.proof}
involution property $(M^t)^t = M$.
:::
<2>3. Thus $M_n(F) = \operatorname{Sym}_n(F) + \operatorname{Skew}_n(F)$.
::: {.proof}
<2>1 and <2>2. <2>4. Suppose $X \in \operatorname{Sym}_n(F) \cap \operatorname{Skew}_n(F)$.
:::
Then $X = X^t = -X$, which gives $2X = 0$.
Since $\operatorname{char}(F) \neq 2$, $2$ is invertible in $F$, so $X = 0$.
::: {.proof}
$2X = 0 \implies X = 0$.
:::
<2>5. Thus $\operatorname{Sym}_n(F) \cap \operatorname{Skew}_n(F) = \{0\}$, so the sum is direct:
\[
M_n(F) = \operatorname{Sym}_n(F) \oplus \operatorname{Skew}_n(F).
\]
::: {.proof}
<2>3 and <2>4.
:::

<1>4. Conclusion: Both symmetric and skew-symmetric matrices are closed under sums and scalar multiplication, and decompose $M_n(F)$ as a direct sum when $\operatorname{char}(F) \neq 2$.
::: {.proof}
<1>1, <1>2, and <1>3.
:::
Q.E.D.
:::
