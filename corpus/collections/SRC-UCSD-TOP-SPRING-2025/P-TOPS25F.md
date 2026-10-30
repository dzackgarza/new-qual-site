---
schema: qual/card@1
id: P-TOPS25F
kind: problem
title: 'Every self-homotopy equivalence of $\CP^{2n}$ has degree $+1$'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Projective Spaces
  - Homotopy Equivalence
relations: []
review: draft
---

::: {.problem}
Show that any homotopy equivalence from $\CP^{2n}$ to itself is orientation-preserving, that is, has degree $+1$.
:::

::: {.solution}

::: pf

::: {.pf-step #ring}

$H^*(\CP^{2n};\ZZ)\cong\ZZ[x]/(x^{2n+1})$ with $x\in H^2$, and $x^{2n}$ generates $H^{4n}(\CP^{2n};\ZZ)\cong\ZZ$.

:::

::: {.pf-step #gen}

If $f:\CP^{2n}\to\CP^{2n}$ is a homotopy equivalence, then $f^*x=\varepsilon x$ for some $\varepsilon\in\{\pm1\}$.

::: pf-proof

$f^*$ is a ring automorphism of $H^*(\CP^{2n};\ZZ)$, so it restricts to an automorphism of $H^2\cong\ZZ$, which is multiplication by $\pm1$.

:::

:::

::: pf-qed

By Steps [](#ring){.pf-ref} and [](#gen){.pf-ref}, $f^*(x^{2n})=(f^*x)^{2n}=\varepsilon^{2n}x^{2n}=x^{2n}$. The degree of $f$ is the integer by which $f^*$ acts on the generator $x^{2n}$ of top cohomology, so $\deg f=+1$.

:::

:::

:::
