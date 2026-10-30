---
schema: qual/card@1
id: P-HAEQ7
kind: problem
title: Cayley-Hamilton theorem
classification:
  areas:
    - algebra
    - applied-algebra
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

::: pf

::: {.pf-step #s1}

There exists $P\in\operatorname{GL}(V)$ such that $P^{-1}AP=J=\bigoplus_{i=1}^s J_i$, where $J_i=\lambda_i I_{m_i}+N_i$ is a Jordan block of size $m_i$.

::: pf-proof

Since $\CC$ is algebraically closed, the Jordan canonical form theorem supplies a basis in which the matrix of $T$ is the displayed block diagonal matrix. Each $N_i$ has ones on its superdiagonal and zero elsewhere, so $N_i^{m_i}=0$.

:::

:::

::: {.pf-step #s2}

The characteristic polynomial of $T$ is $p(x)=\prod_{i=1}^s(x-\lambda_i)^{m_i}$.

::: pf-proof

Similarity preserves characteristic polynomials, so $p(x)=\det(xI-J)$. The matrix $J$ is block diagonal, and $xI_{m_i}-J_i$ is upper triangular with diagonal entries $x-\lambda_i$. Multiplicativity of determinants across diagonal blocks therefore gives the formula.

:::

:::

::: {.pf-step #s3}

For every $1\leq i\leq s$, the evaluation $p(J_i)$ vanishes.

::: pf-proof

By step [](#s1){.pf-ref}, $(J_i-\lambda_i I_{m_i})^{m_i}=N_i^{m_i}=0$. By step [](#s2){.pf-ref}, the polynomial $p(x)$ is divisible by $(x-\lambda_i)^{m_i}$. Therefore $p(J_i)$ has the zero factor $(J_i-\lambda_i I_{m_i})^{m_i}$, and hence $p(J_i)=0$.

:::

:::

::: {.pf-step #s4}

The operator $T$ satisfies
$$
\boxed{p(T)=0}.
$$

::: pf-proof

Polynomial evaluation commutes with direct sums, so step [](#s3){.pf-ref} gives $p(J)=\bigoplus_i p(J_i)=0$. Polynomial evaluation also respects conjugation: $p(A)=Pp(J)P^{-1}=0$. Since $A$ represents $T$, this means $p(T)=0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the Cayley–Hamilton theorem.

:::

:::

:::

::: {.remark title="Variations"}
The same theorem may be asked with the Schur decomposition in place of canonical forms.
Write $U^*AU=T$ with $U$ unitary and $T$ upper triangular with diagonal $\lambda_1,\ldots,\lambda_n$, so $p(x)=\prod_j(x-\lambda_j)$.
With $V_j=\operatorname{span}\{e_1,\ldots,e_j\}$, upper triangularity gives $(T-\lambda_jI)V_j\subseteq V_{j-1}$, so $\prod_{j}(T-\lambda_jI)$ maps $\CC^n=V_n$ to $V_0=0$.
Hence $p(T)=0$, and $p(A)=U\,p(T)\,U^*=0$.
:::
