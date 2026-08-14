---
schema: qual/card@1
id: P-RR26L
kind: problem
title: "Suppose $A^* = A$."
classification:
  areas:
  - algebra
  topics:
  - eigenvalues-and-eigenvectors
  - diagonalization
  - inner-product-spaces
relations: []
review: draft
---
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
$$
\operatorname{det}(A-\lambda I) = 
0 = \overline{\operatorname{det}\left(A^{*} - \bar{\lambda} I\right)}. \qed
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
$\mathcal{C} \definedas \mathcal{B} \union \theset{\vector{v_1}}$ of $S \oplus S^\perp = V$.

Since we have a direct sum decomposition, the matrix of $A$ with respect to $\mathcal{C}$ can be written in block form as 

\begin{align*}
[A]_{\mathcal{C}} &=
\left[\begin{array}{cc}
[\restrictionof{A}{S}]_{\mathcal{C}} & 0 \\
0 & [\restrictionof{A}{S^\perp}]_{\mathcal{C}}
\end{array}\right]
=
\left[\begin{array}{cc}
[\restrictionof{A}{S}]_{\theset{\vector v_1}} & 0 \\
0 & [\restrictionof{A}{S^\perp}]_{\mathcal{B}}
\end{array}\right]
=
\left[\begin{array}{cc}
\lambda_1 & 0 \\
0 & \mathbf{A}' 
\end{array}\right]
,\end{align*}

which is upper-triangular since $\mathbf{A}'$ is upper-triangular.

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
