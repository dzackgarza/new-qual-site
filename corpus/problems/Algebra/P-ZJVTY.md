---
schema: qual/card@1
id: P-ZJVTY
kind: problem
title: $R^n/\im A$ is torsion iff $\operatorname{rank} A=n$ iff the Smith form of
  $A$ has $n$ nonzero invariant factors
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a Principal Ideal Domain (PID) and let $A \in M_n(R)$ be an $n \times n$ matrix representing an $R$-module homomorphism $A: R^n \to R^n$.
Let $M = R^n / \im(A)$ be the cokernel module.
Prove that the following three conditions are equivalent:

(1) $M = R^n / \im(A)$ is a torsion module (every element of $M$ is annihilated by some non-zero $r \in R$).

(2) The matrix rank of $A$ is $\operatorname{rank}_R(A) = n$ (equivalently, $\det(A) \ne 0$).

(3) The Smith Normal Form of $A$ has exactly $n$ non-zero invariant factors $d_1, d_2, \ldots, d_n \ne 0$.
:::

::: {.solution}
Take the Smith normal form $PAQ=\operatorname{diag}(d_1,\ldots,d_n)$ with $P,Q\in\GL_n(R)$ and $d_1\mid\cdots\mid d_n$, allowing some $d_i=0$. Condition (3) says that $d_i\ne0$ for every $i$.

::: pf

::: {.pf-step #decomp}

$M\cong\bigoplus_{i=1}^n R/(d_i)$, where $R/(0)=R$.

::: pf-proof

$P$ and $Q$ are automorphisms of $R^n$, so $R^n/\im A\cong R^n/\im(PAQ)$, and $\im(PAQ)=\bigoplus_i d_iR$.

:::

:::

::: pf-step

(1) holds if and only if (3) holds.

::: pf-proof

By step [](#decomp){.pf-ref}, $M$ is torsion exactly when each summand $R/(d_i)$ is. If $d_i\ne0$, then $d_i$ annihilates $R/(d_i)$. If $d_i=0$, the summand is $R$, and $1\in R$ is annihilated by no nonzero element because $R$ is a domain.

:::

:::

::: pf-step

(2) holds if and only if (3) holds.

::: pf-proof

Let $K=\operatorname{Frac}(R)$. Since $P,Q$ remain invertible over $K$, $\operatorname{rank}A=\operatorname{rank}_K\operatorname{diag}(d_1,\ldots,d_n)$, the number of nonzero $d_i$. Likewise $\det A$ is a unit multiple of $\prod_i d_i$, which is nonzero exactly when every $d_i\ne0$ because $R$ is a domain.

:::

:::

:::

:::
