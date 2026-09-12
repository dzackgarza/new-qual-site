---
schema: qual/card@1
id: E-LJ7PF
kind: problem
title: Complex normal matrices are unitarily diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Matrices
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Let $A\in M_n(\CC)$ be normal, so $AA^*=A^*A$. Show that $A$ is unitarily diagonalizable.
:::

::: {.solution}
<1>1. By Schur triangularization, there is a unitary matrix $U$ such that
\[
T:=U^*AU
\]
is upper triangular.
::: {.proof}
Schur's theorem applies to every complex square matrix. Thus $A=UTU^*$ for some unitary $U$ and upper-triangular $T$.
:::

<1>2. The triangular matrix $T$ is normal.
::: {.proof}
Since $A$ is normal,
\[
AA^*=A^*A.
\]
Conjugating by $U$ gives
\[
TT^*=T^*T.
\]
Thus $T$ is normal.
:::

<1>3. Every upper-triangular normal complex matrix is diagonal.
::: {.proof}
We argue by induction on $n$. The result is immediate for $n=1$.

Write $T=(t_{ij})$. Comparing the $(1,1)$ entries of $TT^*$ and $T^*T$ gives
\[
|t_{11}|^2+|t_{12}|^2+\cdots+|t_{1n}|^2=|t_{11}|^2.
\]
Hence
\[
t_{12}=\cdots=t_{1n}=0.
\]
Since $T$ is upper triangular, its first column also has no entries below $t_{11}$, so
\[
T=[t_{11}]\oplus T_1
\]
for an upper-triangular $(n-1)\times(n-1)$ matrix $T_1$. The equality $TT^*=T^*T$ then implies
\[
T_1T_1^*=T_1^*T_1,
\]
so $T_1$ is normal. By induction $T_1$ is diagonal. Therefore $T$ is diagonal.
:::

<1>4. Therefore $A$ is unitarily diagonalizable.
::: {.proof}
By <1>1 and <1>3, $T=D$ is diagonal. Hence
\[
A=UDU^*,
\]
which is a unitary diagonalization of $A$.
:::
:::
