---
schema: qual/card@1
id: P-WCV7R
kind: problem
title: $\CC[x,y]$ is not a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Polynomials
  - Ideals
relations: []
review: draft
---

::: {.problem}
Give a careful proof that the polynomial ring $\mathbb{C}[x, y]$ is not a principal ideal domain (PID).
:::

::: {.solution}
**Goal:** Prove that $\mathbb{C}[x, y]$ is not a PID by showing that the maximal ideal $I = \langle x, y \rangle$ is not principal.

::: pf

::: pf-step
Definition of the ideal $I = \langle x, y \rangle$:

::: pf-proof

::: pf-step
Define $I = \langle x, y \rangle = \{x p(x, y) + y q(x, y) : p, q \in \mathbb{C}[x, y]\}$.
:::

::: pf-step
$I$ is the ideal of all polynomials in $\mathbb{C}[x, y]$ having constant term zero.
:::

:::

:::

::: {.pf-step #s2}
$I$ is a proper ideal of $\mathbb{C}[x, y]$:

::: pf-proof

::: pf-step
Define the evaluation map $\phi: \mathbb{C}[x, y] \to \mathbb{C}$ at the origin by $\phi(f) = f(0, 0)$.
:::

::: pf-step
The map $\phi$ is a surjective ring homomorphism.
:::

::: pf-step
A polynomial $f(x, y)$ satisfies $\phi(f) = 0$ if and only if its constant term is 0, which holds if and only if $f \in I$. Thus $\ker \phi = I$.
:::

::: pf-step
By the First Isomorphism Theorem for rings, $\mathbb{C}[x, y]/I \cong \mathbb{C}$.
:::

::: pf-step
Since $\mathbb{C}$ is a field and $\mathbb{C} \neq 0$, $I$ is a proper maximal ideal of $\mathbb{C}[x, y]$. In particular, $1 \notin I$ and $I \neq \mathbb{C}[x, y]$.
:::

:::

:::

::: pf-step
$I$ is not a principal ideal:

::: pf-proof

::: pf-step
Suppose for contradiction that $I$ is principal, so $I = \langle f \rangle$ for some $f(x, y) \in \mathbb{C}[x, y]$.
:::

::: pf-step
Since $x \in I = \langle f \rangle$, there exists $g(x, y) \in \mathbb{C}[x, y]$ such that $x = f(x, y) g(x, y)$.
:::

::: pf-step
Looking at total degrees: $\deg(x) = 1 = \deg(f) + \deg(g)$, so $\deg(f) \in \{0, 1\}$.
:::

::: pf-step
If $\deg(f) = 0$, then $f = c \in \mathbb{C}$ is a constant. Since $I \neq \langle 0 \rangle$, $c \neq 0$, so $f$ is a unit in $\mathbb{C}[x, y]$.
:::

::: pf-step
If $f$ is a unit, then $I = \langle f \rangle = \mathbb{C}[x, y]$, which contradicts $I$ being a proper ideal ($1 \notin I$) from step [](#s2){.pf-ref}.
:::

::: pf-step
If $\deg(f) = 1$, then since $f \mid x$ and $x$ has degree 0 in $y$, $f(x, y) = c x$ for some $c \in \mathbb{C}^\times$.
:::

::: pf-step
Then $I = \langle x \rangle$. Since $y \in I = \langle x \rangle$, there must exist $h(x, y) \in \mathbb{C}[x, y]$ such that $y = x h(x, y)$.
:::

::: pf-step
Evaluating at $x = 0$ gives $y = 0 \cdot h(0, y) = 0$, which is a contradiction in the polynomial ring $\mathbb{C}[x, y]$.
:::

::: pf-step
Thus no such generator $f$ can exist, so $I$ is not principal.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Since $\mathbb{C}[x, y]$ is an integral domain containing the non-principal ideal $\langle x, y \rangle$, $\mathbb{C}[x, y]$ is not a principal ideal domain.
:::

:::

:::
:::
