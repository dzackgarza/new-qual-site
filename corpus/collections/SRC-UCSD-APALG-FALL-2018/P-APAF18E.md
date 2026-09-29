---
schema: qual/card@1
id: P-APAF18E
kind: problem
title: Character values are real when $g$ is conjugate to $g^{-1}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the inverse-character and conjugacy argument.
---

::: {.problem}
Let $G$ be a finite group, let $V$ be a finite-dimensional complex representation of $G$, and let $\chi\colon G\to\mathbb{C}$ be the character of $V$.
Let $g\in G$ be a group element such that $g$ is conjugate to $g^{-1}$.
Prove that $\chi(g)$ is a real number.
:::

::: {.solution}
**Goal:** Prove that $\chi(g) \in \mathbb{R}$ for the character $\chi$ of a finite-dimensional complex representation $\rho: G \to \operatorname{GL}(V)$ of a finite group $G$, given that $g$ is conjugate to $g^{-1}$ in $G$.

::: pf

::: {.pf-step #s1}
Characters satisfy $\chi(g^{-1}) = \overline{\chi(g)}$ for all $g \in G$:

::: pf-proof

::: pf-step
Let $n = \dim_\mathbb{C}(V)$. The representation $\rho: G \to \operatorname{GL}(V)$ assigns to $g$ an operator $\rho(g)$ of finite order dividing $|G|$.
:::

::: pf-step
Hence $\rho(g)$ is diagonalizable with eigenvalues $\lambda_1, \dots, \lambda_n \in \mathbb{C}$, each satisfying $\lambda_j^{|G|} = 1$, so $|\lambda_j| = 1$ and $\lambda_j^{-1} = \overline{\lambda_j}$ for all $j \in \{1, \dots, n\}$.
:::

::: pf-step
The eigenvalues of $\rho(g^{-1}) = \rho(g)^{-1}$ are $\lambda_1^{-1}, \dots, \lambda_n^{-1}$.
:::

::: pf-step
The character value is the trace:
$$\chi(g) = \operatorname{tr}(\rho(g)) = \sum_{j=1}^n \lambda_j.$$
:::

::: pf-step
The character value at the inverse is:
$$\chi(g^{-1}) = \operatorname{tr}(\rho(g^{-1})) = \sum_{j=1}^n \lambda_j^{-1} = \sum_{j=1}^n \overline{\lambda_j} = \overline{\sum_{j=1}^n \lambda_j} = \overline{\chi(g)}.$$
:::

:::

:::

::: {.pf-step #s2}
Characters are class functions:
If two elements $a, b \in G$ are conjugate, then $\chi(a) = \chi(b)$.

::: pf-proof
If $b = x a x^{-1}$ for some $x \in G$, then $\rho(b) = \rho(x)\rho(a)\rho(x)^{-1}$. By the cyclic property of the trace, $\operatorname{tr}(\rho(b)) = \operatorname{tr}(\rho(x)\rho(a)\rho(x)^{-1}) = \operatorname{tr}(\rho(a))$, hence $\chi(b) = \chi(a)$.
:::

:::

::: {.pf-step #s3}
Evaluation at $g$ and $g^{-1}$:
Since $g$ is conjugate to $g^{-1}$ in $G$, $\chi(g) = \chi(g^{-1})$.

::: pf-proof
Direct consequence of step [](#s2){.pf-ref} with $a = g^{-1}$ and $b = g$.
:::

:::

::: pf-step
Conclusion: $\chi(g) \in \mathbb{R}$.

::: pf-proof
Combining step [](#s1){.pf-ref} and step [](#s3){.pf-ref} gives $\chi(g) = \overline{\chi(g)}$. Any complex number equal to its complex conjugate is real, so $\chi(g) \in \mathbb{R}$.
:::

:::

:::
:::
