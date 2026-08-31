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

::: problem
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

::: solution
**Goal:** Prove anti-monotonicity of orthogonal complements in (a), construct an injective evaluation map on quotient spaces in (b), and prove it is an isomorphism in finite dimensions by dimension counting.

<1>1. Part (a): $Y \subseteq X \implies X^\perp \subseteq Y^\perp$.
::: {.proof}
    <2>1. Let $v \in X^\perp$.
    <2>2. By definition of $X^\perp$, $(v, x) = 0$ for every $x \in X$.
    <2>3. Since $Y \subseteq X$, every element $y \in Y$ satisfies $y \in X$.
    <2>4. Thus $(v, y) = 0$ for all $y \in Y$.
    <2>5. By definition of $Y^\perp$, $v \in Y^\perp$.
    <2>6. Therefore $X^\perp \subseteq Y^\perp$.

:::

<1>2. Part (b): Construction and well-definedness of $\psi$.
::: {.proof}
    <2>1. For each $u \in Y^\perp$, consider the linear functional $f_u: X \to F$ defined by $f_u(x) = (u, x)$.
    <2>2. Since $u \in Y^\perp$, $(u, y) = 0$ for all $y \in Y$, so $Y \subseteq \ker(f_u)$.
    <2>3. By the universal property of quotient vector spaces, $f_u$ induces a unique linear functional $\bar{f}_u \in (X/Y)^*$ given by
    $$\bar{f}_u(x + Y) = (u, x) \quad \text{for all } x \in X.$$
    <2>4. Define the map $\psi: Y^\perp / X^\perp \to (X/Y)^*$ by
    $$\psi(u + X^\perp) = \bar{f}_u.$$
    <2>5. Well-definedness:
        - If $u + X^\perp = u' + X^\perp$, then $u - u' \in X^\perp$.
        - For any $x \in X$, $\bar{f}_u(x + Y) - \bar{f}_{u'}(x + Y) = (u - u', x) = 0$.
        - Thus $\bar{f}_u = \bar{f}_{u'}$, showing that $\psi$ is well-defined.
    <2>6. Linearity:
        - By bilinearity of $(\cdot, \cdot)$, $\bar{f}_{a u_1 + b u_2}(x + Y) = (a u_1 + b u_2, x) = a (u_1, x) + b (u_2, x) = a \bar{f}_{u_1}(x + Y) + b \bar{f}_{u_2}(x + Y)$.
        - Thus $\psi$ is an $F$-linear transformation.

:::

<1>3. Part (b): Injectivity of $\psi$.
::: {.proof}
    <2>1. Suppose $u + X^\perp \in \ker(\psi)$.
    <2>2. Then $\psi(u + X^\perp) = 0$, so $\bar{f}_u(x + Y) = (u, x) = 0$ for all $x \in X$.
    <2>3. This means $(u, x) = 0$ for all $x \in X$, which implies $u \in X^\perp$.
    <2>4. Therefore $u + X^\perp = 0 + X^\perp$ in $Y^\perp / X^\perp$.
    <2>5. Thus $\ker(\psi) = \{0\}$, so $\psi$ is injective.

:::

<1>4. Part (b): Isomorphism when $\dim_F V < \infty$.
::: {.proof}
    <2>1. Assume $\dim_F V = n < \infty$.
    <2>2. Since $(\cdot, \cdot)$ is non-degenerate, the map $v \mapsto (v, \cdot)$ is an isomorphism $V \cong V^*$.
    <2>3. For any subspace $W \subseteq V$, $\dim_F W^\perp = \dim_F V - \dim_F W$.
    <2>4. Compute the dimension of the domain:
    $$\dim_F(Y^\perp / X^\perp) = \dim_F Y^\perp - \dim_F X^\perp = (n - \dim_F Y) - (n - \dim_F X) = \dim_F X - \dim_F Y.$$
    <2>5. Compute the dimension of the codomain:
    $$\dim_F((X/Y)^*) = \dim_F(X/Y) = \dim_F X - \dim_F Y.$$
    <2>6. An injective linear map between finite-dimensional vector spaces of the same dimension is an isomorphism.
    <2>7. Thus $\psi: Y^\perp / X^\perp \to (X/Y)^*$ is an isomorphism.

:::

<1>5. Conclusion:
::: {.proof}
    $Y \subseteq X \implies X^\perp \subseteq Y^\perp$, and $\psi(u + X^\perp)(x + Y) = (u, x)$ defines an injective map which is an isomorphism in finite dimensions.
:::
:::
