---
schema: qual/card@1
id: E-MKK6X
kind: problem
title: The minimal uncountable order is not separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Show that the minimal uncountable order with the order topology is not separable.
:::

::: {.solution}

::: pf

::: pf-step

Let $\omega_1$ denote the set of all countable ordinals with the order topology. Suppose $D\subseteq\omega_1$ is countable.

::: pf-proof

This is the minimal uncountable ordinal/order.

:::

:::

::: pf-step

The supremum $\alpha=\sup D$ is still a countable ordinal, hence $\alpha<\omega_1$.

::: pf-proof

A countable union of countable ordinals is countable, so the supremum of countably many countable ordinals is countable.

:::

:::

::: {.pf-step #s3}

The open ray
$$(\alpha,\omega_1)=\{\beta<\omega_1:\beta>\alpha\}$$
is nonempty and disjoint from $D$.

::: pf-proof

It is a basic open final interval in the order topology, and every element of $D$ is at most $\alpha$.

:::

:::

::: pf-step

Therefore no countable subset of $\omega_1$ is dense, so $\omega_1$ is not separable.

::: pf-proof

Every countable subset misses the nonempty open set from step [](#s3){.pf-ref}.

:::

:::

:::

:::
