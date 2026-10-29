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

::: pf

::: {.pf-step #s1}

If $Y\subseteq X$, then $X^\perp\subseteq Y^\perp$.

::: pf-proof

For $v\in X^\perp$, the functional $(v,-)$ vanishes on $X$ and therefore vanishes on its subspace $Y$. Hence $v\in Y^\perp$.

:::

:::

::: {.pf-step #s2}

The rule
$$
\boxed{\psi:Y^\perp/X^\perp\longrightarrow (X/Y)^*,\qquad
\psi(v+X^\perp)(x+Y)=(v,x)}
$$
defines an injective $F$-linear map.

::: pf-proof

For $v\in Y^\perp$, the functional $(v,-)|_X$ annihilates $Y$ and thus factors uniquely through $X/Y$. If $v$ is replaced by $v+w$ with $w\in X^\perp$, its restriction to $X$ is unchanged. The displayed assignment is therefore well defined on both quotients and linear by bilinearity. If $\psi(v+X^\perp)=0$, then $(v,x)=0$ for every $x\in X$, so $v\in X^\perp$ and its quotient class is zero. Thus $\psi$ is injective.

:::

:::

::: {.pf-step #s3}

If $\dim_FV<\infty$, then $\psi$ is an isomorphism.

::: pf-proof

In finite dimension, nondegeneracy makes the linear map $V\to V^*$, $v\mapsto(v,-)$, an isomorphism. For any subspace $W$, the annihilator of $W$ in $V^*$ has dimension $\dim V-\dim W$, hence $\dim W^\perp=\dim V-\dim W$. It follows that
$$
\dim(Y^\perp/X^\perp)=\dim X-\dim Y
=\dim(X/Y)^*.
$$
The injective linear map from step [](#s2){.pf-ref} between these finite-dimensional spaces of equal dimension is surjective as well.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (b).

:::

:::

:::
