---
schema: qual/card@1
id: P-R7HSU
kind: problem
title: The cokernel of $A\in M_n(\ZZ)$ is finite iff $\det A\neq 0$, with order $\abs{\det
  A}$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $A \in M_n(\ZZ)$ be an $n \times n$ matrix with integer entries, viewed as a $\ZZ$-module homomorphism $A: \ZZ^n \to \ZZ^n$.

(a) Prove that the cokernel $\operatorname{coker}(A) = \ZZ^n / \im(A)$ is finite if and only if $\det(A) \ne 0$.

(b) Prove that when $\det(A) \ne 0$, the order of the cokernel is given by:
$$\abs{\operatorname{coker}(A)} = \abs{\det(A)}.$$
:::

::: {.solution}
::: pf

::: {.pf-step #snf}
There are $U,V\in\GL_n(\ZZ)$ and integers $d_1\mid\cdots\mid d_n$, some possibly $0$, with $UAV=\operatorname{diag}(d_1,\ldots,d_n)$ and
$$
\operatorname{coker}(A)\cong\bigoplus_{i=1}^n\ZZ/d_i\ZZ ,
$$
where $\ZZ/0\ZZ=\ZZ$.

::: pf-proof
The matrix factorization is the Smith normal form over the PID $\ZZ$. Since $U$ and $V$ are automorphisms of $\ZZ^n$, $\operatorname{coker}(A)\cong\operatorname{coker}(UAV)$, and the cokernel of a diagonal matrix is the direct sum of the $\ZZ/d_i\ZZ$.
:::

:::

::: {.pf-step #det}
$\abs{\det A}=\prod_i\abs{d_i}$.

::: pf-proof
$\det U,\det V\in\{\pm1\}$ because they are units of $\ZZ$, and $\det(UAV)=d_1\cdots d_n$.
:::

:::

::: pf-step
(a) $\operatorname{coker}(A)$ is finite if and only if $\det A\ne0$.

::: pf-proof
By step [](#snf){.pf-ref}, the cokernel is finite exactly when every $d_i\ne0$, which by step [](#det){.pf-ref} holds exactly when $\det A\ne0$.
:::

:::

::: pf-step
(b) If $\det A\ne0$, then $\abs{\operatorname{coker}(A)}=\abs{\det A}$.

::: pf-proof
By step [](#snf){.pf-ref}, $\abs{\operatorname{coker}(A)}=\prod_i\abs{d_i}$, which equals $\abs{\det A}$ by step [](#det){.pf-ref}.
:::

:::

:::
:::
