---
schema: qual/card@1
id: E-FQBAM
kind: problem
title: $\det(A^{a})=\det(A)^{n-1}$ and $(A^{a})^{a}=\det(A)^{n-2}A$
classification:
  areas:
  - algebra
  topics:
  - Determinants
  - Matrices
  - Rings
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

::: problem
3. For $n\geq 2$, consider the ring of $n \times n$ matrices over a commutative unital ring $R$, denoted $\operatorname{Mat}_{n}(R)$. Recall the determinant map $\det:\operatorname{Mat}_{n}(R)\to R$.
   For $A \in \operatorname{Mat}_{n}(R)$ also recall the definition of the classical adjoint $A^{a}$ of $A$.
   Prove that:

- $\operatorname{det}\left(A^{a}\right)=\operatorname{det}(A)^{n-1}$

- $\left(A^{a}\right)^{a}=\operatorname{det}(A)^{n-2} A$
:::

::: {.solution}
Write $\operatorname{adj}(A)=A^a$.

<1>1. It is enough to prove both identities for the generic matrix over $S=\ZZ[x_{ij}]$.
::: {.proof}
Each entry of $\operatorname{adj}(A)$ is a polynomial with integer coefficients in the entries of $A$, and determinants are polynomial expressions as well. Thus both desired identities are polynomial identities with integer coefficients in the entries of $A$. If they hold for the generic matrix
\[
X=(x_{ij})\in M_n(S),
\]
then for any commutative unital ring $R$ and any $A=(a_{ij})\in M_n(R)$, the specialization homomorphism $S\to R$, $x_{ij}\mapsto a_{ij}$, carries those identities to the corresponding identities for $A$.
:::

<1>2. Over the fraction field $K=\operatorname{Frac}(S)$, the generic matrix $X$ is invertible and
\[
\operatorname{adj}(X)=\det(X)X^{-1}.
\]
::: {.proof}
The polynomial $\det(X)$ is nonzero in the domain $S$, so it is a nonzero element of $K$. Hence $X$ is invertible over $K$. The standard adjugate identity
\[
X\operatorname{adj}(X)=\operatorname{adj}(X)X=\det(X)I_n
\]
then gives the displayed formula after multiplying by $X^{-1}$.
:::

<1>3. One has
\[
\det(\operatorname{adj}(X))=\det(X)^{n-1}.
\]
::: {.proof}
Using <1>2 and multiplicativity of the determinant over $K$,
\[
\det(\operatorname{adj}(X))
=\det(\det(X)X^{-1})
=\det(X)^n\det(X^{-1})
=\det(X)^{n-1}.
\]
Both sides lie in $S$, so the equality holds already in $S$.
:::

<1>4. One has
\[
\operatorname{adj}(\operatorname{adj}(X))=\det(X)^{n-2}X.
\]
::: {.proof}
By <1>2, $\operatorname{adj}(X)$ is invertible over $K$. Therefore, applying the same adjugate formula to $\operatorname{adj}(X)$ and then using <1>3,
\[
\begin{aligned}
\operatorname{adj}(\operatorname{adj}(X))
&=\det(\operatorname{adj}(X))\operatorname{adj}(X)^{-1}\\
&=\det(X)^{n-1}\bigl(\det(X)X^{-1}\bigr)^{-1}\\
&=\det(X)^{n-2}X.
\end{aligned}
\]
Since $n\ge2$, both sides are matrices whose entries lie in $S$. Hence the identity holds in $S$.
:::

<1>5. Specializing the generic identities gives, for every $A\in M_n(R)$,
\[
\det(A^a)=\det(A)^{n-1},
\qquad
(A^a)^a=\det(A)^{n-2}A.
\]
::: {.proof}
Apply <1>1 to the identities established in <1>3 and <1>4.
:::
:::
