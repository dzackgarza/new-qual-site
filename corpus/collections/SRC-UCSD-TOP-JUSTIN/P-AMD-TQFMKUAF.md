---
schema: qual/card@1
id: P-AMD-TQFMKUAF
kind: problem
title: Winding number of $8z^4+4z^3+2z^2+z^{-1}$ on $S^1$
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Determine the winding number of the following map: $f: S^1 \to \mathbb{C}-\{0\}, z\mapsto 8z^4 + 4z^3 + 2z^2 + z^{-1}$
:::

::: {.solution}

::: pf

::: pf-step

On $S^1$, write
$$
f(z)=z^{-1}g(z),\qquad g(z)=8z^5+4z^4+2z^3+1.
$$

::: pf-proof

This is immediate by multiplying the given Laurent polynomial by $z$.

:::

:::

::: {.pf-step #s2}

The polynomial $g$ has all five zeros in the open unit disk.

::: pf-proof

On $|z|=1$,
$$
|8z^5|=8>4+2+1\ge |4z^4+2z^3+1|.
$$
By Rouché's theorem, $g(z)$ and $8z^5$ have the same number of zeros in $|z|<1$, counted with multiplicity, namely five. The strict inequality also shows that $g$ has no zero on $S^1$.

:::

:::

::: {.pf-step #s3}

The winding number of $g|_{S^1}$ about $0$ is $5$.

::: pf-proof

By the argument principle, the winding number of a polynomial with no zeros on the contour equals the number of its zeros inside the contour, counted with multiplicity. Apply step [](#s2){.pf-ref}.

:::

:::

::: pf-step

The winding number of $z\mapsto z^{-1}$ is $-1$, so
$$
\boxed{\operatorname{wind}(f,0)=5-1=4}.
$$

::: pf-proof

Winding number is additive under pointwise multiplication of maps $S^1\to\mathbb C^*$. The map $z^{-1}$ has degree $-1$, while step [](#s3){.pf-ref} gives degree $5$ for $g$.

:::

:::

:::

:::
