---
schema: qual/card@1
id: P-AY6TZ
kind: problem
title: Neither the torus nor $\RP^2$ covers the other
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the migrated solution fragment, which falsely said there are no homomorphisms Z^2 -> Z/2, by the required injectivity obstruction.
---

::: {.problem}
Show that neither the torus $T^2=S^1\times S^1$ nor $\RP^2$ can cover the other.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A covering map $p:T^2\to\RP^2$ would induce an injective homomorphism
$$
p_*:\pi_1(T^2)\hookrightarrow\pi_1(\RP^2).
$$

::: pf-proof

A covering-space projection induces an injection on fundamental groups of path-connected based spaces.

:::

:::

::: {.pf-step #s2}

The groups in step [](#s1){.pf-ref} are
$$
\pi_1(T^2)\cong\ZZ^2,
\qquad
\pi_1(\RP^2)\cong\ZZ/2\ZZ.
$$

::: pf-proof

The first follows from
$$
T^2=S^1\times S^1
$$
and the product formula for fundamental groups.
The second is the standard computation from the universal double cover
$$
S^2\to\RP^2.
$$

:::

:::

::: {.pf-step #s3}

No injective homomorphism $\ZZ^2\to\ZZ/2\ZZ$ exists.

::: pf-proof

The image of any such homomorphism is a subgroup of the two-element group $\ZZ/2\ZZ$, hence has at most two elements.
The group $\ZZ^2$ is infinite, so an injective map is impossible.

:::

:::

::: pf-step

No covering map $T^2\to\RP^2$ exists.

::: pf-proof

Otherwise steps [](#s1){.pf-ref} and [](#s2){.pf-ref} would produce the injection ruled out by step [](#s3){.pf-ref}.

:::

:::

::: pf-step

No covering map $q:\RP^2\to T^2$ exists.

::: pf-proof

As in step [](#s1){.pf-ref}, such a covering would induce an injective homomorphism $q_*:\ZZ/2\ZZ\hookrightarrow\ZZ^2$, using step [](#s2){.pf-ref}.
The image of the nontrivial element would be a nonzero element of order $2$ in $\ZZ^2$.
The group $\ZZ^2$ is torsion-free, so no such element exists.

:::

:::

:::

:::
