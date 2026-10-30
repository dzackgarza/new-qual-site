---
schema: qual/card@1
id: P-APAS23C
kind: problem
title: Subordinate norms; $\norm{xy^H}$; Frobenius bound; Frobenius norm of $xy^H$
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, and $\CC^n$ is the set of column vectors with $n$ complex components.

(a) Given a vector norm $\norm{\cdot}$, define the matrix norm subordinate to $\norm{\cdot}$.
Prove that every subordinate matrix norm is consistent.

(b) Given $A \in M_{m,n}$, let $\norm{A}$ denote the matrix norm subordinate to the vector norm $\norm{\cdot}$.
Prove that $\norm{xy^H} = \norm{x} \norm{y}_D$ for all $x, y \in \CC^n$, where $\norm{y}_D$ denotes the vector norm dual to $\norm{\cdot}$.

(c) Given $A \in M_{m,n}$, prove that $\norm{Ax}_2 \le \norm{A}_F \norm{x}_2$ for all $x \in \CC^n$.

(d) Find $\norm{xy^H}$ for the Frobenius norm.
:::

::: {.solution}
**Goal.** Prove the four facts about subordinate and Frobenius matrix norms.

::: pf

::: {.pf-step #s1}
(a) The subordinate norm is $\norm{A} \coloneqq \sup_{x \neq 0} \frac{\norm{Ax}}{\norm{x}}$, and it is consistent.

::: pf-proof

::: pf-step
Definition: $\norm{A} = \sup_{\norm{x} = 1} \norm{Ax}$.

::: pf-proof
this is the matrix norm subordinate to the vector norm $\norm{\cdot}$.
:::

:::

::: pf-step
Consistency: $\norm{AB} \le \norm{A}\,\norm{B}$.

::: pf-proof
$\norm{ABx} = \norm{A(Bx)} \le \norm{A}\,\norm{Bx} \le \norm{A}\,\norm{B}\,\norm{x}$, so $\norm{AB} \le \norm{A}\,\norm{B}$.
:::

:::

:::

:::

::: {.pf-step #s2}
(b) $\norm{xy^H} = \norm{x}\,\norm{y}_D$.

::: pf-proof

::: pf-step
$xy^H$ is the rank-one matrix $z \mapsto x\,(y^H z) = x\,\langle z, y\rangle$.

::: pf-proof
$y^H z$ is the inner product $\langle z, y\rangle$.
:::

:::

::: {.pf-step #s2-2}
$\norm{xy^H} = \sup_{\norm{z}=1} \norm{x\,(y^H z)} = \norm{x} \sup_{\norm{z}=1} \abs{y^H z}$.

::: pf-proof
$\norm{x\,(y^H z)} = \abs{y^H z}\,\norm{x}$.
:::

:::

::: {.pf-step #s2-3}
$\sup_{\norm{z}=1} \abs{y^H z} = \norm{y}_D$.

::: pf-proof
the dual norm is defined by $\norm{y}_D = \sup_{\norm{z}=1} \abs{y^H z}$.
:::

:::

::: pf-step
Hence $\norm{xy^H} = \norm{x}\,\norm{y}_D$.

::: pf-proof
combine step [](#s2-2){.pf-ref} and step [](#s2-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
(c) $\norm{Ax}_2 \le \norm{A}_F \norm{x}_2$.

::: pf-proof

::: pf-step
$\norm{Ax}_2^2 = \sum_i \abs{\sum_j a_{ij} x_j}^2$.

::: pf-proof
expand the squared Euclidean norm.
:::

:::

::: pf-step
$\sum_i \abs{\sum_j a_{ij} x_j}^2 \le \sum_i \qty(\sum_j \abs{a_{ij}}^2)\qty(\sum_j \abs{x_j}^2)$.

::: pf-proof
Cauchy–Schwarz applied to each row: $\abs{\sum_j a_{ij} x_j}^2 \le (\sum_j \abs{a_{ij}}^2)(\sum_j \abs{x_j}^2)$.
:::

:::

::: pf-step
$\sum_i \sum_j \abs{a_{ij}}^2 = \norm{A}_F^2$ and $\sum_j \abs{x_j}^2 = \norm{x}_2^2$.

::: pf-proof
definition of the Frobenius norm and the Euclidean norm.
:::

:::

::: pf-step
Hence $\norm{Ax}_2^2 \le \norm{A}_F^2 \norm{x}_2^2$, so $\norm{Ax}_2 \le \norm{A}_F \norm{x}_2$.

::: pf-proof
take square roots.
:::

:::

:::

:::

::: {.pf-step #s4}
(d) $\norm{xy^H}_F = \norm{x}_2 \norm{y}_2$.

::: pf-proof

::: pf-step
$(xy^H)_{ij} = x_i \bar y_j$.

::: pf-proof
the $(i,j)$ entry of the outer product.
:::

:::

::: pf-step
$\norm{xy^H}_F^2 = \sum_{i,j} \abs{x_i \bar y_j}^2 = \sum_i \abs{x_i}^2 \sum_j \abs{y_j}^2 = \norm{x}_2^2 \norm{y}_2^2$.

::: pf-proof
$\abs{x_i \bar y_j}^2 = \abs{x_i}^2 \abs{y_j}^2$, and the double sum factors.
:::

:::

::: pf-step
Hence $\norm{xy^H}_F = \norm{x}_2 \norm{y}_2$.

::: pf-proof
take square roots.
:::

:::

:::

:::

::: pf-qed
step [](#s1){.pf-ref}, step [](#s2){.pf-ref}, step [](#s3){.pf-ref}, and step [](#s4){.pf-ref} prove (a)–(d).
:::

:::
:::
