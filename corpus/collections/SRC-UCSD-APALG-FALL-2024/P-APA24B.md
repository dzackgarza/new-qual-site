---
schema: qual/card@1
id: P-APA24B
kind: problem
title: A matrix is unitarily diagonalizable if and only if it is normal
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Diagonalization
  - Normal Operators
relations: []
review: draft
---

::: {.problem}
Consider $A \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$.
Prove the result: $A$ is unitarily diagonalizable if and only if $A$ is normal.

Note, mathematically, this can be written as: there exists $U \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$, satisfying $U^H U = U U^H = I$, such that $U^H A U$ is diagonal if and only if $A^H A = A A^H$, where $U^H = \overline{U}^T$ and $A^H = \overline{A}^T$.
:::

::: {.solution}
<1>1. If $A$ is unitarily diagonalizable, then $A$ is normal.
::: {.proof}
Suppose
\[
A=UDU^H
\]
with $U$ unitary and $D$ diagonal. Then
\[
A^H=UD^HU^H.
\]
Hence
\[
A^HA=UD^HDU^H,
\qquad
AA^H=UDD^HU^H.
\]
Since $D$ is diagonal, $D^HD=DD^H$, so $A^HA=AA^H$.
:::

<1>2. Every upper-triangular normal matrix is diagonal.
::: {.proof}
We argue by induction on the size $n$. The case $n=1$ is immediate.

Let $T=(t_{ij})\in M_n(\mathbb C)$ be upper triangular and normal. Comparing the $(1,1)$ entries of
\[
TT^*=T^*T
\]
gives
\[
\sum_{j=1}^n|t_{1j}|^2
=\sum_{j=1}^n|t_{j1}|^2.
\]
Because $T$ is upper triangular, $t_{j1}=0$ for $j>1$, so the right side is $|t_{11}|^2$. Therefore
\[
\sum_{j=2}^n|t_{1j}|^2=0,
\]
and hence $t_{1j}=0$ for every $j>1$.
Thus
\[
T=\begin{pmatrix}t_{11}&0\\0&B\end{pmatrix}
\]
with $B$ upper triangular. Normality of $T$ implies $B$ is normal, so by induction $B$ is diagonal. Hence $T$ is diagonal.
:::

<1>3. If $A$ is normal, then $A$ is unitarily diagonalizable.
::: {.proof}
By Schur decomposition there exists a unitary matrix $U$ such that
\[
T=U^HAU
\]
is upper triangular.
Unitary similarity preserves normality:
\[
T^HT=U^HA^HAU,
\qquad
TT^H=U^HAA^HU.
\]
Since $A^HA=AA^H$, we have $T^HT=TT^H$, so $T$ is normal.
By <1>2, $T$ is diagonal. Therefore
\[
U^HAU=T
\]
is diagonal, so $A$ is unitarily diagonalizable.
:::

<1>4. Therefore
\[
\boxed{A\text{ is unitarily diagonalizable}\iff A\text{ is normal}.}
\]
::: {.proof}
The forward implication is <1>1 and the reverse implication is <1>3.
:::
:::
