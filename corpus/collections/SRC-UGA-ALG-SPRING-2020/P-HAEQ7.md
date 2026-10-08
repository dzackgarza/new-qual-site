---
schema: qual/card@1
id: P-HAEQ7
kind: problem
title: Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Jordan Canonical Form
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $T:V\to V$ be a linear transformation where $V$ is a finite-dimensional vector space over $\CC$.
Prove the Cayley-Hamilton theorem: if $p(x)$ is the characteristic polynomial of $T$, then $p(T) = 0$.
You may use canonical forms.
:::

::: {.solution}
Choose a complex basis of $V$ and write $A$ for the matrix of $T$ in this basis.

<1>1. There exists $P\in\operatorname{GL}(V)$ such that $P^{-1}AP=J=\bigoplus_{i=1}^s J_i$, where $J_i=\lambda_i I_{m_i}+N_i$ is a Jordan block of size $m_i$.
::: {.proof}
Since $\mathbb C$ is algebraically closed, the Jordan canonical form theorem supplies a basis in which the matrix of $T$ is the displayed block diagonal matrix. Each $N_i$ has ones on its superdiagonal and zero elsewhere, so $N_i^{m_i}=0$.
:::

<1>2. The characteristic polynomial of $T$ is $p(x)=\prod_{i=1}^s(x-\lambda_i)^{m_i}$.
::: {.proof}
Similarity preserves characteristic polynomials, so $p(x)=\det(xI-J)$. The matrix $J$ is block diagonal, and $xI_{m_i}-J_i$ is upper triangular with diagonal entries $x-\lambda_i$. Multiplicativity of determinants across diagonal blocks therefore gives the formula.
:::

<1>3. For every $1\leq i\leq s$, the evaluation $p(J_i)$ vanishes.
::: {.proof}
By step <1>1, $(J_i-\lambda_i I_{m_i})^{m_i}=N_i^{m_i}=0$. By step <1>2, the polynomial $p(x)$ is divisible by $(x-\lambda_i)^{m_i}$. Therefore $p(J_i)$ has the zero factor $(J_i-\lambda_i I_{m_i})^{m_i}$, and hence $p(J_i)=0$.
:::

<1>4. The operator $T$ satisfies
\[
\boxed{p(T)=0}.
\]
::: {.proof}
Polynomial evaluation commutes with direct sums, so step <1>3 gives $p(J)=\bigoplus_i p(J_i)=0$. Polynomial evaluation also respects conjugation: $p(A)=Pp(J)P^{-1}=0$. Since $A$ represents $T$, this means $p(T)=0$.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 proves the Cayley–Hamilton theorem.
:::
:::
