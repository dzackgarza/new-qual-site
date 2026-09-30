---
schema: qual/card@1
id: E-JUT2P
kind: problem
title: A singularity is removable for $f$ if and only if it is removable for $f'$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Cauchy Estimates
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is meromorphic. Show that if $z_0$ is a removable singularity of $f$, then it is also a removable singularity of $f'$.
Conversely, if $z_0$ is removable for $f'$, then it is also removable for $f$.

:::

::: {.solution}
Let $f$ be holomorphic on a punctured disk $\DD_\eps^*(z_0)$.

If $z_0$ is removable for $f$, let $F$ be the holomorphic extension of $f$ to $\DD_\eps(z_0)$. Then $F'$ is holomorphic on $\DD_\eps(z_0)$ and equals $f'$ on $\DD_\eps^*(z_0)$, so $z_0$ is removable for $f'$.

For the converse, if $z_0$ is removable for $f'$, let $g$ be the holomorphic extension of $f'$ to $\DD_\eps(z_0)$, which exists by Riemann's removable singularity theorem.
Since $g$ is holomorphic on the disk, it has a primitive $F(z) \definedas \int_{z_0}^z g(\xi) \dxi$ there.
Now $G\definedas F - f$ satisfies $G' = g - f' \equiv 0$ on the connected set $\DD_\eps^*(z_0)$, so $G\equiv c$ is constant and $f(z) = F(z) - c$.
In particular,
\[
\lim_{z\to z_0} f(z) = F(z_0) - c
\]
exists, so $z_0$ is removable for $f$.

:::
