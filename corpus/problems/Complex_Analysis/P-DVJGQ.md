---
schema: qual/card@1
id: P-DVJGQ
kind: problem
title: Implicit function theorem from the inverse function theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Multivariable Calculus
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
State the most general version of the implicit function theorem for real functions and outline how it can be proved using the inverse function theorem.
:::

::: {.solution}
::: pf

::: pf-step
**Implicit Function Theorem.** Let $F : \mathbb{R}^{n+m} \to \mathbb{R}^m$ be $C^k$ ($k \ge 1$), and let $(a, b) \in \mathbb{R}^n \times \mathbb{R}^m$ with $F(a, b) = 0$. If the $m \times m$ matrix $\frac{\partial F}{\partial y}(a, b)$ (the partial derivatives with respect to the last $m$ variables) is invertible, then there are open neighborhoods $U \ni a$ and $V \ni b$ and a unique $C^k$ function $g : U \to V$ such that $g(a) = b$ and $F(x, g(x)) = 0$ for all $x \in U$.

::: pf-proof
statement of the theorem.
:::

:::

::: pf-step
Define $\Phi : \mathbb{R}^{n+m} \to \mathbb{R}^{n+m}$ by $\Phi(x, y) = (x, F(x, y))$.

::: pf-proof
augment $F$ with the identity on the first $n$ coordinates.
:::

:::

::: {.pf-step #jacobian-invertible}
The Jacobian of $\Phi$ at $(a, b)$ is
$$D\Phi(a,b) = \begin{pmatrix} I_n & 0 \\ \frac{\partial F}{\partial x}(a,b) & \frac{\partial F}{\partial y}(a,b) \end{pmatrix},$$
which is invertible because $\frac{\partial F}{\partial y}(a,b)$ is invertible.

::: pf-proof
block matrix; its determinant is $\det \frac{\partial F}{\partial y}(a,b) \neq 0$.
:::

:::

::: {.pf-step #local-inverse-exists}
By the inverse function theorem, $\Phi$ has a $C^k$ local inverse $\Psi$ near $(a, b)$.

::: pf-proof
Step [](#jacobian-invertible){.pf-ref} and the inverse function theorem.
:::

:::

::: {.pf-step #psi-relation}
Write $\Psi(x, z) = (x, \psi(x, z))$; then $\Phi(x, \psi(x,z)) = (x, z)$, so $F(x, \psi(x,z)) = z$.

::: pf-proof
Step [](#local-inverse-exists){.pf-ref}, matching the first $n$ coordinates.
:::

:::

::: {.pf-step #define-g}
Define $g(x) = \psi(x, 0)$.

::: pf-proof
set $z = 0$.
:::

:::

::: {.pf-step #g-satisfies-equation}
Then $F(x, g(x)) = F(x, \psi(x,0)) = 0$, and $g(a) = \psi(a, 0) = b$ (since $\Phi(a,b) = (a, 0)$).

::: pf-proof
Steps [](#psi-relation){.pf-ref} and [](#define-g){.pf-ref}.
:::

:::

::: {.pf-step #g-is-implicit-function}
Hence $g$ is the desired implicit function, proving the implicit function theorem from the inverse function theorem.

::: pf-proof
Step [](#g-satisfies-equation){.pf-ref}.
:::

:::

::: pf-qed
Step [](#g-is-implicit-function){.pf-ref}.
:::

:::
