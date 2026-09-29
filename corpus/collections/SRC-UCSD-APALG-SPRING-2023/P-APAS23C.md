---
schema: qual/card@1
id: P-APAS23C
kind: problem
title: Subordinate norms; $\|xy^H\|$; Frobenius bound; Frobenius norm of $xy^H$
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
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, and $\mathbb{C}^n$ is the set of column vectors with $n$ complex components.

(a) Given a vector norm $\|\cdot\|$, define the matrix norm subordinate to $\|\cdot\|$.
Prove that every subordinate matrix norm is consistent.

(b) Given $A \in M_{m,n}$, let $\|A\|$ denote the matrix norm subordinate to the vector norm $\|\cdot\|$.
Prove that $\|xy^H\| = \|x\| \|y\|_D$ for all $x, y \in \mathbb{C}^n$, where $\|y\|_D$ denotes the vector norm dual to $\|\cdot\|$.

(c) Given $A \in M_{m,n}$, prove that $\|Ax\|_2 \le \|A\|_F \|x\|_2$ for all $x \in \mathbb{C}^n$.

(d) Find $\|xy^H\|$ for the Frobenius norm.
:::

::: {.solution}
**Goal.** Prove the four facts about subordinate and Frobenius matrix norms.

::: pf

::: {.pf-step #s1}
(a) The subordinate norm is $\|A\| \definedas \sup_{x \neq 0} \frac{\|Ax\|}{\|x\|}$, and it is consistent.

::: pf-proof

::: pf-step
Definition: $\|A\| = \sup_{\|x\| = 1} \|Ax\|$.

::: pf-proof
this is the matrix norm subordinate to the vector norm $\|\cdot\|$.
:::

:::

::: pf-step
Consistency: $\|AB\| \le \|A\|\,\|B\|$.

::: pf-proof
$\|ABx\| = \|A(Bx)\| \le \|A\|\,\|Bx\| \le \|A\|\,\|B\|\,\|x\|$, so $\|AB\| \le \|A\|\,\|B\|$.
:::

:::

:::

:::

::: {.pf-step #s2}
(b) $\|xy^H\| = \|x\|\,\|y\|_D$.

::: pf-proof

::: pf-step
$xy^H$ is the rank-one matrix $z \mapsto x\,(y^H z) = x\,\langle z, y\rangle$.

::: pf-proof
$y^H z$ is the inner product $\langle z, y\rangle$.
:::

:::

::: {.pf-step #s2-2}
$\|xy^H\| = \sup_{\|z\|=1} \|x\,(y^H z)\| = \|x\| \sup_{\|z\|=1} |y^H z|$.

::: pf-proof
$\|x\,(y^H z)\| = |y^H z|\,\|x\|$.
:::

:::

::: {.pf-step #s2-3}
$\sup_{\|z\|=1} |y^H z| = \|y\|_D$.

::: pf-proof
the dual norm is defined by $\|y\|_D = \sup_{\|z\|=1} |y^H z|$.
:::

:::

::: pf-step
Hence $\|xy^H\| = \|x\|\,\|y\|_D$.

::: pf-proof
combine step [](#s2-2){.pf-ref} and step [](#s2-3){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
(c) $\|Ax\|_2 \le \|A\|_F \|x\|_2$.

::: pf-proof

::: pf-step
$\|Ax\|_2^2 = \sum_i |\sum_j a_{ij} x_j|^2$.

::: pf-proof
expand the squared Euclidean norm.
:::

:::

::: pf-step
$\sum_i |\sum_j a_{ij} x_j|^2 \le \sum_i \qty(\sum_j |a_{ij}|^2)\qty(\sum_j |x_j|^2)$.

::: pf-proof
Cauchy–Schwarz applied to each row: $|\sum_j a_{ij} x_j|^2 \le (\sum_j |a_{ij}|^2)(\sum_j |x_j|^2)$.
:::

:::

::: pf-step
$\sum_i \sum_j |a_{ij}|^2 = \|A\|_F^2$ and $\sum_j |x_j|^2 = \|x\|_2^2$.

::: pf-proof
definition of the Frobenius norm and the Euclidean norm.
:::

:::

::: pf-step
Hence $\|Ax\|_2^2 \le \|A\|_F^2 \|x\|_2^2$, so $\|Ax\|_2 \le \|A\|_F \|x\|_2$.

::: pf-proof
take square roots.
:::

:::

:::

:::

::: {.pf-step #s4}
(d) $\|xy^H\|_F = \|x\|_2 \|y\|_2$.

::: pf-proof

::: pf-step
$(xy^H)_{ij} = x_i \bar y_j$.

::: pf-proof
the $(i,j)$ entry of the outer product.
:::

:::

::: pf-step
$\|xy^H\|_F^2 = \sum_{i,j} |x_i \bar y_j|^2 = \sum_i |x_i|^2 \sum_j |y_j|^2 = \|x\|_2^2 \|y\|_2^2$.

::: pf-proof
$|x_i \bar y_j|^2 = |x_i|^2 |y_j|^2$, and the double sum factors.
:::

:::

::: pf-step
Hence $\|xy^H\|_F = \|x\|_2 \|y\|_2$.

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
