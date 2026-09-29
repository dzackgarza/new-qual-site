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

::: pf

::: pf-step
By the Jordan canonical form, $T$ is similar to a block-diagonal matrix $J = \bigoplus J_i$, where each $J_i$ is a Jordan block for an eigenvalue $\lambda_i$.

::: pf-proof
the Jordan canonical form over $\CC$.
:::

:::

::: pf-step
The characteristic polynomial is $p(x) = \prod_i (x - \lambda_i)^{m_i}$, where $m_i$ is the size of the Jordan block $J_i$.

::: pf-proof
the characteristic polynomial of a Jordan block $J_i$ (of size $m_i$ with eigenvalue $\lambda_i$) is $(x - \lambda_i)^{m_i}$.
:::

:::

::: {.pf-step #jordan-block-nilpotent-vanishes}
For each Jordan block $J_i = \lambda_i I + N_i$ (where $N_i$ is nilpotent with $N_i^{m_i} = 0$), we have $(J_i - \lambda_i I)^{m_i} = N_i^{m_i} = 0$.

::: pf-proof
$J_i - \lambda_i I = N_i$ is nilpotent of index $m_i$.
:::

:::

::: {.pf-step #p-vanishes-on-block}
Hence $p(J_i) = \prod_j (J_i - \lambda_j I)^{m_j} = 0$ for each block $J_i$.

::: pf-proof
the factor $(J_i - \lambda_i I)^{m_i} = 0$ (step [](#jordan-block-nilpotent-vanishes){.pf-ref}) is one of the factors of $p(J_i)$, so the whole product vanishes.
:::

:::

::: {.pf-step #p-vanishes-on-j}
Therefore $p(J) = \bigoplus_i p(J_i) = 0$, and since $T$ is similar to $J$, $p(T) = 0$.

::: pf-proof
Step [](#p-vanishes-on-block){.pf-ref} and similarity.
:::

:::

::: pf-qed
Step [](#p-vanishes-on-j){.pf-ref}.
:::

:::

:::
