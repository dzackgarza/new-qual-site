---
schema: qual/card@1
id: P-AMD-ZM6JCKEX
kind: problem
title: The equatorial inclusion $\mathbb{RP}^2\to\mathbb{RP}^3$ is not nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $i: \mathbb{RP}^2 \to \mathbb{RP}^3$, induced by $S^2 \hookrightarrow S^3$ as the equator.
Show that $i \not\simeq \text{const}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The inclusion
$$
i:\mathbb{RP}^2\hookrightarrow\mathbb{RP}^3
$$
induces the identity isomorphism
$$
i_*:\pi_1(\mathbb{RP}^2)\cong\mathbb Z/2\longrightarrow\pi_1(\mathbb{RP}^3)\cong\mathbb Z/2.
$$

::: pf-proof

Use the standard CW structures
$$
\mathbb{RP}^2=e^0\cup e^1\cup e^2,
\qquad
\mathbb{RP}^3=\mathbb{RP}^2\cup e^3.
$$
Attaching cells of dimension at least $3$ does not change the fundamental group. Hence the inclusion of the $2$-skeleton induces an isomorphism on $\pi_1$.

:::

:::

::: {.pf-step #s2}

A null-homotopic map induces the trivial homomorphism on fundamental groups.

::: pf-proof

Homotopic maps induce the same map on $\pi_1$ up to the usual basepoint conjugacy. A constant map induces the zero homomorphism, and conjugating the trivial homomorphism leaves it trivial.

:::

:::

::: pf-step

Therefore $i$ is not null-homotopic.

::: pf-proof

If $i\simeq\mathrm{const}$, then step [](#s2){.pf-ref} would force $i_*$ to be trivial, contradicting the nontrivial isomorphism in step [](#s1){.pf-ref}. Hence
$$
\boxed{i\not\simeq\mathrm{const}}.
$$

:::

:::

:::

:::
