---
schema: qual/card@1
id: P-LW3KB
kind: problem
title: $Y\subset X$ implies $X^\perp\subseteq Y^\perp$, and $Y^\perp/X^\perp\hookrightarrow(X/Y)^*$,
  for a nondegenerate symmetric bilinear form
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Dual Spaces
  - Vector Spaces
relations: []
review: draft
---

::: {.problem}
Let $V$ be a vector space over a field $F$, and let $(\cdot, \cdot): V \times V \to F$ be a non-degenerate symmetric bilinear form on $V$. For any subspace $W \subseteq V$, define its orthogonal complement by
$$
W^{\perp} = \{v \in V \mid (v, w) = 0 \text{ for all } w \in W\}.
$$

(a) Show that if $X, Y$ are subspaces of $V$ with $Y \subseteq X$, then $X^{\perp} \subseteq Y^{\perp}$.

(b) Define an injective linear map
$$
\psi: Y^{\perp}/X^{\perp} \hookrightarrow (X/Y)^*,
$$
and prove that $\psi$ is an isomorphism if $\dim_F V < \infty$.
:::

::: {.solution}
**Goal:** Prove anti-monotonicity of orthogonal complements in (a), construct an injective evaluation map on quotient spaces in (b), and prove it is an isomorphism in finite dimensions by dimension counting.

::: pf

::: pf-step
Part (a): $Y \subseteq X \implies X^\perp \subseteq Y^\perp$.

::: pf-proof

::: pf-step
Let $v \in X^\perp$.
:::

::: pf-step
By definition of $X^\perp$, $(v, x) = 0$ for every $x \in X$.
:::

::: pf-step
Since $Y \subseteq X$, every element $y \in Y$ satisfies $y \in X$.
:::

::: pf-step
Thus $(v, y) = 0$ for all $y \in Y$.
:::

::: pf-step
By definition of $Y^\perp$, $v \in Y^\perp$.
:::

::: pf-step
Therefore $X^\perp \subseteq Y^\perp$.
:::

:::

:::

::: pf-step
Part (b): Construction and well-definedness of $\psi$.

::: pf-proof

::: pf-step
For each $u \in Y^\perp$, consider the linear functional $f_u: X \to F$ defined by $f_u(x) = (u, x)$.
:::

::: pf-step
Since $u \in Y^\perp$, $(u, y) = 0$ for all $y \in Y$, so $Y \subseteq \ker(f_u)$.
:::

::: pf-step
By the universal property of quotient vector spaces, $f_u$ induces a unique linear functional $\bar{f}_u \in (X/Y)^*$ given by
$$\bar{f}_u(x + Y) = (u, x) \quad \text{for all } x \in X.$$
:::

::: pf-step
Define the map $\psi: Y^\perp / X^\perp \to (X/Y)^*$ by
$$\psi(u + X^\perp) = \bar{f}_u.$$
:::

::: pf-step
Well-definedness:

- If $u + X^\perp = u' + X^\perp$, then $u - u' \in X^\perp$.
- For any $x \in X$, $\bar{f}_u(x + Y) - \bar{f}_{u'}(x + Y) = (u - u', x) = 0$.
- Thus $\bar{f}_u = \bar{f}_{u'}$, showing that $\psi$ is well-defined.
:::

::: pf-step
Linearity:

- By bilinearity of $(\cdot, \cdot)$, $\bar{f}_{a u_1 + b u_2}(x + Y) = (a u_1 + b u_2, x) = a (u_1, x) + b (u_2, x) = a \bar{f}_{u_1}(x + Y) + b \bar{f}_{u_2}(x + Y)$.
- Thus $\psi$ is an $F$-linear transformation.
:::

:::

:::

::: pf-step
Part (b): Injectivity of $\psi$.

::: pf-proof

::: pf-step
Suppose $u + X^\perp \in \ker(\psi)$.
:::

::: pf-step
Then $\psi(u + X^\perp) = 0$, so $\bar{f}_u(x + Y) = (u, x) = 0$ for all $x \in X$.
:::

::: pf-step
This means $(u, x) = 0$ for all $x \in X$, which implies $u \in X^\perp$.
:::

::: pf-step
Therefore $u + X^\perp = 0 + X^\perp$ in $Y^\perp / X^\perp$.
:::

::: pf-step
Thus $\ker(\psi) = \{0\}$, so $\psi$ is injective.
:::

:::

:::

::: pf-step
Part (b): Isomorphism when $\dim_F V < \infty$.

::: pf-proof

::: pf-step
Assume $\dim_F V = n < \infty$.
:::

::: pf-step
Since $(\cdot, \cdot)$ is non-degenerate, the map $v \mapsto (v, \cdot)$ is an isomorphism $V \cong V^*$.
:::

::: pf-step
For any subspace $W \subseteq V$, $\dim_F W^\perp = \dim_F V - \dim_F W$.
:::

::: pf-step
Compute the dimension of the domain:
$$\dim_F(Y^\perp / X^\perp) = \dim_F Y^\perp - \dim_F X^\perp = (n - \dim_F Y) - (n - \dim_F X) = \dim_F X - \dim_F Y.$$
:::

::: pf-step
Compute the dimension of the codomain:
$$\dim_F((X/Y)^*) = \dim_F(X/Y) = \dim_F X - \dim_F Y.$$
:::

::: pf-step
An injective linear map between finite-dimensional vector spaces of the same dimension is an isomorphism.
:::

::: pf-step
Thus $\psi: Y^\perp / X^\perp \to (X/Y)^*$ is an isomorphism.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$Y \subseteq X \implies X^\perp \subseteq Y^\perp$, and $\psi(u + X^\perp)(x + Y) = (u, x)$ defines an injective map which is an isomorphism in finite dimensions.
:::

:::

:::
:::
