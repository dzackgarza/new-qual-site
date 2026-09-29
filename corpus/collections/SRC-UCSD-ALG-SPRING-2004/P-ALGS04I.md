---
schema: qual/card@1
id: P-ALGS04I
kind: problem
title: "Dimension of tensor product of vector spaces via the universal mapping property"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $V$ and $W$ be finite-dimensional vector spaces over the field of complex numbers of dimensions $m$ and $n$.
Use the universal mapping property to prove that $V \otimes W$ is a vector space of dimension $mn$.
:::

::: {.solution}

::: pf

::: pf-step

Let $\{v_1, \ldots, v_m\}$ be a basis of $V$ and $\{w_1, \ldots, w_n\}$ a basis of $W$.

::: pf-proof

choose bases.

:::

:::

::: {.pf-step #s2}

The set $\{v_i \otimes w_j : 1 \le i \le m, 1 \le j \le n\}$ spans $V \otimes W$.

::: pf-proof

every element of $V \otimes W$ is a finite sum of pure tensors $v \otimes w$, and each $v = \sum_i a_i v_i$, $w = \sum_j b_j w_j$ expands to $\sum_{i,j} a_i b_j (v_i \otimes w_j)$ by bilinearity.

:::

:::

::: {.pf-step #s3}

The set $\{v_i \otimes w_j\}$ is linearly independent.

::: pf-proof

for each pair $(i, j)$, define the bilinear map $\varphi_{ij} : V \times W \to \mathbb{C}$ by $\varphi_{ij}(v, w) = v_i^*(v) w_j^*(w)$ (where $v_i^*, w_j^*$ are the dual basis functionals).
By the universal property, $\varphi_{ij}$ induces a linear map $\tilde\varphi_{ij} : V \otimes W \to \mathbb{C}$ with $\tilde\varphi_{ij}(v_p \otimes w_q) = \delta_{ip}\delta_{jq}$.
If $\sum_{i,j} c_{ij}(v_i \otimes w_j) = 0$, applying $\tilde\varphi_{ij}$ gives $c_{ij} = 0$ for each $(i,j)$.

:::

:::

::: {.pf-step #s4}

Hence $\{v_i \otimes w_j\}$ is a basis of $V \otimes W$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Therefore $\dim(V \otimes W) = mn$.

::: pf-proof

Step [](#s4){.pf-ref} (there are $mn$ basis elements).

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
