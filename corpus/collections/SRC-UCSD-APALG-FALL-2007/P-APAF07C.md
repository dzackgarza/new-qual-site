---
schema: qual/card@1
id: P-APAF07C
kind: problem
title: Matrices near diagonalizable; orthonormal eigenbasis iff $A^HA=AA^H$
classification:
  areas:
  - applied-algebra
  topics:
  - Diagonalization
  - Normal Operators
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
(a) Use Schur's Theorem to prove that every square matrix is arbitrarily close to a diagonalizable matrix.

(b) Show that a square matrix matrix $A$ has an orthonormal basis of eigenvectors iff $A^HA=AA^H$ ($A^*A=AA^*$).
:::

::: {.solution}
<1>1. Every complex square matrix is arbitrarily close, in Frobenius norm, to a diagonalizable matrix.
::: {.proof}
Let $A\in M_n(\mathbb C)$ and let $\varepsilon>0$. By Schur's theorem there is a unitary matrix $U$ such that
\[
T=U^*AU
\]
is upper triangular. Write its diagonal entries as
\[
\lambda_1,\ldots,\lambda_n.
\]

Choose complex numbers $\delta_1,\ldots,\delta_n$ such that
\[
|\delta_j|<\frac{\varepsilon}{\sqrt n}
\]
for every $j$, and such that the numbers
\[
\lambda_1+\delta_1,\ldots,\lambda_n+\delta_n
\]
are pairwise distinct. This can be done inductively: after $\delta_1,\ldots,\delta_{j-1}$ are chosen, only finitely many values of $\delta_j$ are forbidden by the equalities
\[
\lambda_j+\delta_j=\lambda_i+\delta_i\qquad(i<j),
\]
while the disk $|\delta_j|<\varepsilon/\sqrt n$ contains infinitely many choices.

Set
\[
T_\varepsilon=T+\operatorname{diag}(\delta_1,\ldots,\delta_n)
\]
and
\[
A_\varepsilon=UT_\varepsilon U^*.
\]
Then $T_\varepsilon$ is upper triangular with $n$ distinct diagonal entries, hence has $n$ distinct eigenvalues and is diagonalizable. Therefore $A_\varepsilon$, being similar to $T_\varepsilon$, is diagonalizable.

Finally, the Frobenius norm is unitarily invariant, so
\[
\|A_\varepsilon-A\|_F
=\|T_\varepsilon-T\|_F
=\left(\sum_{j=1}^n|\delta_j|^2\right)^{1/2}
<\varepsilon.
\]
Thus diagonalizable matrices are dense in $M_n(\mathbb C)$. This proves part (a).
:::

<1>2. If $A$ has an orthonormal basis of eigenvectors, then
\[
A^*A=AA^*.
\]
::: {.proof}
Let $u_1,\ldots,u_n$ be an orthonormal eigenbasis, with
\[
Au_j=\lambda_j u_j.
\]
Let
\[
U=[u_1\ \cdots\ u_n],
\qquad
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
\]
Then $U$ is unitary and
\[
A=UDU^*.
\]
Hence
\[
A^*A
=UD^*DU^*,
\qquad
AA^*
=UDD^*U^*.
\]
Since diagonal matrices commute with their adjoints,
\[
D^*D=DD^*,
\]
so $A^*A=AA^*$.
:::

<1>3. Every upper-triangular normal matrix is diagonal.
::: {.proof}
We argue by induction on the size $n$. The statement is trivial for $n=1$.

Let $T=(t_{ij})\in M_n(\mathbb C)$ be upper triangular and normal. Comparing the $(1,1)$ entries of
\[
TT^*=T^*T
\]
gives
\[
\sum_{j=1}^n|t_{1j}|^2
=
\sum_{j=1}^n|t_{j1}|^2.
\]
Because $T$ is upper triangular,
\[
t_{j1}=0\qquad(j>1),
\]
so the right-hand side is $|t_{11}|^2$. Therefore
\[
\sum_{j=2}^n|t_{1j}|^2=0,
\]
and hence
\[
t_{1j}=0\qquad(j>1).
\]
Thus
\[
T=
\begin{pmatrix}
t_{11}&0\\
0&B
\end{pmatrix}
\]
with $B$ upper triangular. Normality of $T$ implies
\[
BB^*=B^*B,
\]
so $B$ is normal. By the induction hypothesis, $B$ is diagonal. Hence $T$ is diagonal.
:::

<1>4. If $A^*A=AA^*$, then $A$ has an orthonormal basis of eigenvectors.
::: {.proof}
Assume $A$ is normal. By Schur's theorem there is a unitary $U$ such that
\[
T=U^*AU
\]
is upper triangular. Unitary similarity preserves normality, since
\[
T^*T
=U^*A^*AU,
\qquad
TT^*
=U^*AA^*U.
\]
Thus $T$ is upper triangular and normal. By <1>3, $T$ is diagonal.
Therefore
\[
A=UTU^*
\]
is unitarily diagonalizable, and the columns of $U$ form an orthonormal basis of eigenvectors of $A$.
:::

<1>5. Hence a complex square matrix has an orthonormal basis of eigenvectors if and only if it is normal, equivalently
\[
A^*A=AA^*.
\]
::: {.proof}
The forward implication is <1>2 and the reverse implication is <1>4. This proves part (b).
:::
:::
