---
schema: qual/card@1
id: E-QSTAU
kind: problem
title: Nontrivial solutions of $Ax=0$ versus $\det A=0$ over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Determinants
  - Matrices
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
4. If $R$ is an integral domain and $A$ is an $n \times n$ matrix over $R$, prove that if a system of linear equations $A x=0$ has a nonzero solution then $\operatorname{det} A=0$.
   Is the converse true?
   What if we drop the assumption that $R$ is an integral domain?
:::

::: {.solution}
<1>1. Proof that non-trivial kernel implies $\det A = 0$ over an integral domain:
<2>1. Let $R$ be an integral domain, $A \in M_n(R)$, and $x = (x_1, \dots, x_n)^T \in R^n \setminus \{0\}$ such that $Ax = 0$.
Proof: hypothesis.
<2>2. Multiply the equation $Ax = 0$ on the left by the adjugate matrix $\operatorname{adj}(A) \in M_n(R)$:
\[
\operatorname{adj}(A) A x = (\det A) I_n x = (\det A) x = 0.
\]
Proof: adjugate identity $\operatorname{adj}(A) A = (\det A) I_n$.
<2>3. Since $x \neq 0$, there exists some index $j \in \{1, \dots, n\}$ such that $x_j \neq 0$.
Componentwise, $(\det A) x_j = 0$ in $R$.
Since $R$ is an integral domain and $x_j \neq 0$, we must have $\det A = 0$.
Proof: definition of an integral domain (no zero divisors).

<1>2. The Converse over an Integral Domain:
<2>1. **The converse is TRUE.**
Suppose $\det A = 0$. Let $F = \operatorname{Frac}(R)$ be the field of fractions of $R$.
Proof: construction of field of fractions.
<2>2. View $A$ as a matrix in $M_n(F)$. Since $\det A = 0$, standard linear algebra over the field $F$ implies that the nullspace of $A$ in $F^n$ is non-trivial: there exists a non-zero vector $y = (y_1, \dots, y_n)^T \in F^n \setminus \{0\}$ such that $Ay = 0$.
Proof: invertible matrix theorem over fields.
<2>3. Writing each $y_i = a_i / b_i$ with $a_i, b_i \in R$ and $b_i \neq 0$, let $d = b_1 b_2 \cdots b_n \in R \setminus \{0\}$.
Define $x = d y \in R^n$.
Then $x \neq 0$ (since $d \neq 0$ and $y \neq 0$), and $Ax = A(dy) = d(Ay) = d \cdot 0 = 0$.
Thus $Ax = 0$ has a non-zero solution in $R^n$.
Proof: clearing denominators in the field of fractions.

<1>3. Behavior when $R$ is not an integral domain:
<2>1. **The implication $Ax = 0 \implies \det A = 0$ FAILS in general:**
Let $R = \mathbb{Z}/4\mathbb{Z}$ and $n = 1$.
Consider the $1 \times 1$ matrix $A = (2)$.
The vector $x = (2) \in R^1$ is non-zero, and $Ax = 2 \cdot 2 = 4 \equiv 0 \pmod 4$.
However, $\det A = 2 \not\equiv 0 \pmod 4$.
Proof: explicit counterexample with zero divisors.
<2>2. **General ring characterization (McCoy's Theorem):**
Over an arbitrary commutative ring $R$, $Ax = 0$ has a non-zero solution $x \in R^n$ if and only if $\det A$ (and more generally the ideals of maximal rank minors) has a non-zero annihilator in $R$.
Proof: McCoy's Rank Theorem for matrices over commutative rings.

<1>4. Conclusion:
Over an integral domain, $Ax = 0$ has a non-zero solution $\iff \det A = 0$. When $R$ is not an integral domain, $Ax = 0$ can have non-zero solutions even when $\det A \neq 0$. Q.E.D.
Proof: <1>1 through <1>3.
:::
