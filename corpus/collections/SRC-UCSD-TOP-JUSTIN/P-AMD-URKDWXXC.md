---
schema: qual/card@1
id: P-AMD-URKDWXXC
kind: problem
title: $\operatorname{Tor}(\mathbb{Q},A)$ and $\operatorname{Tor}(\mathbb{Q}/\mathbb{Z},A)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.problem}
Compute $\Tor(\QQ, A)$

1. Compute $\Tor(\QQ/\ZZ, A)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every abelian group $A$,
$$
\boxed{\operatorname{Tor}_1^{\mathbb Z}(\mathbb Q,A)=0.}
$$

::: pf-proof

The $\mathbb Z$-module $\mathbb Q$ is a localization of $\mathbb Z$, hence is flat. Tor in positive degree with a flat module vanishes.

:::

:::

::: {.pf-step #s2}

Apply $-\otimes_{\mathbb Z}A$ to
$$
0\longrightarrow\mathbb Z\longrightarrow\mathbb Q\longrightarrow\mathbb Q/\mathbb Z\longrightarrow0.
$$
The resulting long exact Tor sequence contains
$$
0\longrightarrow
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Q/\mathbb Z,A)
\longrightarrow A
\longrightarrow \mathbb Q\otimes A.
$$

::: pf-proof

The term $\operatorname{Tor}_1(\mathbb Q,A)$ on the left is zero by step [](#s1){.pf-ref}, and $\mathbb Z\otimes A\cong A$.

:::

:::

::: {.pf-step #s3}

The kernel of the localization map $A\to\mathbb Q\otimes A$ is exactly the torsion subgroup $A_{\mathrm{tors}}$.

::: pf-proof

Under $\mathbb Q\otimes A\cong S^{-1}A$ with $S=\mathbb Z\setminus\{0\}$, an element $a\in A$ maps to zero iff some nonzero integer $s$ annihilates $a$, which is precisely the definition of torsion.

:::

:::

::: pf-step

Hence
$$
\boxed{\operatorname{Tor}_1^{\mathbb Z}(\mathbb Q/\mathbb Z,A)\cong A_{\mathrm{tors}}.}
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
