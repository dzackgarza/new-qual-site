---
schema: qual/card@1
id: T-TORCY
kind: definition
title: '$\Tor_1^{\ZZ}(\ZZ/2,\ZZ/2)$ from a free presentation'
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $M$ be a $\ZZ$-module, let $0\to N\mapsvia{\iota}F\mapsvia{\pi}M\to0$ be a presentation with $F$ free, and let $A$ be a $\ZZ$-module.
The group $\Tor_1^{\ZZ}(M,A)$ is the kernel of the map
$$
N\tensor_\ZZ A\longrightarrow F\tensor_\ZZ A
$$
induced by $\iota$; it does not depend on the presentation chosen.
:::

::: {.proposition}
$\Tor_1^{\ZZ}(\ZZ/2\ZZ,\ZZ/2\ZZ)\cong\ZZ/2\ZZ$.
:::

::: {.proof}
Take the presentation $0\to\ZZ\mapsvia{2}\ZZ\mapsvia{\pi}\ZZ/2\ZZ\to0$, with $\pi$ the reduction modulo $2$.
Tensoring the sequence with $\ZZ/2\ZZ$ gives
$$
\ZZ/2\ZZ\mapsvia{0}\ZZ/2\ZZ\longrightarrow\ZZ/2\ZZ\tensor_\ZZ\ZZ/2\ZZ\longrightarrow0,
$$
because the map induced by multiplication by $2$ is multiplication by $2$ on $\ZZ/2\ZZ$, which is zero.
Hence $\Tor_1^{\ZZ}(\ZZ/2\ZZ,\ZZ/2\ZZ)$ is the kernel of the zero map on $\ZZ/2\ZZ$, which is $\ZZ/2\ZZ$; the tensor product that follows is $(\ZZ/2\ZZ)/2(\ZZ/2\ZZ)\cong\ZZ/2\ZZ$ by [[T-TENSR]].
:::
