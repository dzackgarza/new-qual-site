---
schema: qual/card@1
id: P-RR26L
kind: problem
title: Self-adjoint operators have real eigenvalues and are unitarily diagonalizable,
  and Schur's theorem
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Diagonalization
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Suppose $A^* = A$.
It is then a fact that $A$ is self-adjoint, and so for every $\vector{v}\in V$ we have 
$$
\inner{A\vector{v}}{\vector{v}} =
\inner{\vector{v}}{A^*\vector{v}} =
\inner{\vector{v}}{A\vector{v}}.
$$

Let $(\lambda, \vector v)$ be an eigenvalue of $A$ with one of its corresponding eigenvectors, so $A\vector{v} = \lambda{\vector v}$.

On one hand,
\begin{align*}
\inner{A\vector{v}}{\vector{v}}
=
\inner{\lambda\vector{v}}{\vector{v}}
=
\lambda \inner{\vector{v}}{\vector{v}}
=
\lambda \norm{\vector{v}}^2
,\end{align*}

while on the other hand,

\begin{align*}
\inner{A\vector{v}}{\vector{v}}
=
\inner{\vector{v}}{A^*\vector{v}} 
=
\inner{\vector{v}}{A\vector{v}}
=
\inner{\vector{v}}{\lambda\vector{v}}
=
\overline{\lambda} \inner{\vector{v}}{\vector{v}}
=
\overline{\lambda} \norm{\vector{v}}^2
.\end{align*}

Equating these expressions, we find that
$$
\lambda = \overline{\lambda} \implies \lambda \in \RR. \qed
$$

We can make use of the following fact:

**Theorem (Schur):**
Every square matrix $A \in M_n(\CC)$ is unitarily similar to an upper triangular matrix, i.e. there exists a unitary matrix $U$ such that $A = UTU\inv$ where $T$ is upper-triangular.

Applying this theorem yields $A = UTU\inv$ and thus $T = U\inv A U$. In particular, $A \sim T$.

Noting that if $U$ is unitary then $U\inv = U^*$, we have

\begin{align*}
T^* 
&= (U\inv A U)^* \\
&= U^* A^* (U\inv)^* \\
&= U^* A^* U^{**} \\
&= U\inv A^* U \\
&= T
,\end{align*}

and so $T^* = T$. 

Since $T$ is upper triangular, this forces $T_{ij} = 0$ whenever $i\neq j$
But this makes $T$ diagonal, so $A$ is similar to a diagonal matrix. 
$\qed$

*Proof of Schur's Theorem:*
We'll proceed by induction on $n = \dim_\CC(V)$, and showing that there is an orthonormal basis of $V$ such that the matrix of $A$ is upper triangular.

**Lemma:** 
If $V$ is finite dimensional and $\lambda$ is an eigenvalue of $A$, then $\overline{\lambda}$ is an eigenvalue of $A^*$.

*Proof:*
Since $A^* - \bar\lambda I = (A - \lambda I)^*$ and $\det(M^*) = \overline{\det M}$,
$$
\operatorname{det}\left(A^{*} - \bar{\lambda} I\right) = \overline{\operatorname{det}(A-\lambda I)} = \bar 0 = 0. \qed
$$

Since $\CC$ is algebraically closed, every matrix $A \in M_n(\CC)$ will have an eigenvalue, since its characteristic polynomial will have a root by the Fundamental Theorem of Algebra.

So let $\lambda_1, \vector v_1$ be an eigenvalue/eigenvector pair of the adjoint $A^*$.

Consider the space $S = \spanof_\CC\theset{\vector v_1}$; then $V = S \oplus S^\perp$.
The claim is that the original $A$ will restrict to an operator on $S^\perp$, which has dimension $n-1$.
The inductive hypothesis will then apply to $\restrictionof{A}{S^\perp}$.

Note that if this holds, there will be an orthonormal basis $\mathcal{B}$ of $S^\perp$ such that the matrix
$$
\mathbf{A}' \definedas [\restrictionof{A}{S^\perp}]_{\mathcal{B}}
$$ 
will be upper triangular. 
We would then be able to obtain an orthonormal basis 
$\mathcal{C} \definedas \mathcal{B} \union \theset{\vector{v_1}}$ of $S \oplus S^\perp = V$, **ordered with $\vector v_1$ last**.

Only $S^\perp$ is $A\dash$invariant here; $S$ is an eigenspace of $A^*$, not of $A$, so $\restrictionof{A}{S}$ is not defined and the matrix is not block diagonal.
What the invariance of $S^\perp$ gives is that the first $n-1$ columns have no $\vector v_1$ component, i.e. a zero in the last row:

\begin{align*}
[A]_{\mathcal{C}} &=
\left[\begin{array}{cc}
[\restrictionof{A}{S^\perp}]_{\mathcal{B}} & \vector u \\
0 & c
\end{array}\right]
=
\left[\begin{array}{cc}
\mathbf{A}' & \vector u \\
0 & c
\end{array}\right]
,\end{align*}

where $\vector u$ and the scalar $c$ record $A\vector v_1$ in the basis $\mathcal C$, and are otherwise unconstrained.
This is upper-triangular since $\mathbf{A}'$ is upper-triangular.

> Ordering $\vector v_1$ first would instead put the unconstrained column on the left and give a **lower** triangular matrix.

To see that $A$ does indeed restrict to an operator on $S^\perp$, we need to show that $A(S^\perp) \subseteq S^\perp$.
So let $\vector s \in S^\perp$; then $\inner{\vector v_1}{\vector s} = 0$ by definition.
Then $A\vector s \in S^\perp$ since

\begin{align*}
\inner{\vector v_1}{A\vector s} 
&= \inner{A^* \vector v_1}{\vector s} \\
&= \inner{\lambda_1 \vector v_1}{\vector s} \\
&= \lambda_1 \inner{\vector v_1}{\vector s} \\
&= 0
.\end{align*}

$\qed$
:::

::: {.solution}
**Goal.** Show a self-adjoint operator has real eigenvalues and is unitarily diagonalizable.

<1>1. Every eigenvalue of $A$ is real.
<2>1. Let $A\vector v = \lambda \vector v$ with $\vector v \neq 0$.
::: {.proof}
take an eigenpair.
:::
<2>2. $\inner{A\vector v}{\vector v} = \lambda \norm{\vector v}^2$.
::: {.proof}
$\inner{A\vector v}{\vector v} = \inner{\lambda \vector v}{\vector v} = \lambda \inner{\vector v}{\vector v}$.
:::
<2>3. $\inner{A\vector v}{\vector v} = \overline{\lambda} \norm{\vector v}^2$.
::: {.proof}
$\inner{A\vector v}{\vector v} = \inner{\vector v}{A^*\vector v} = \inner{\vector v}{A\vector v} = \inner{\vector v}{\lambda \vector v} = \overline{\lambda}\inner{\vector v}{\vector v}$.
:::
<2>4. Hence $\lambda = \overline{\lambda}$, so $\lambda \in \RR$.
::: {.proof}
equate <2>2 and <2>3 and divide by $\norm{\vector v}^2 \neq 0$.
:::

<1>2. $A$ is unitarily diagonalizable.
<2>1. By Schur's theorem, $A = UTU\inv$ with $U$ unitary and $T$ upper triangular.
::: {.proof}
Schur's theorem.
:::
<2>2. $T^* = T$.
::: {.proof}
$T = U\inv A U = U^* A U$, so $T^* = (U^* A U)^* = U^* A^* U = U^* A U = T$.
:::
<2>3. $T$ is diagonal.
::: {.proof}
$T$ is upper triangular and $T^* = T$ forces $T_{ij} = 0$ for $i \neq j$.
:::
<2>4. Hence $A$ is unitarily similar to a diagonal matrix.
::: {.proof}
<2>1 and <2>3.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
