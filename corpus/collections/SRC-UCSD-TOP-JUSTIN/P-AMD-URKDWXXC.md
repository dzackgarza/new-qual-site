---
schema: qual/card@1
id: P-AMD-URKDWXXC
kind: problem
title: $\operatorname{Tor}(\QQ,A)$ and $\operatorname{Tor}(\QQ/\ZZ,A)$
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
\boxed{\operatorname{Tor}_1^{\ZZ}(\QQ,A)=0.}
$$

::: pf-proof

The $\ZZ$-module $\QQ$ is a localization of $\ZZ$, hence is flat. Tor in positive degree with a flat module vanishes.

:::

:::

::: {.pf-step #s2}

Apply $-\otimes_{\ZZ}A$ to
$$
0\longrightarrow\ZZ\longrightarrow\QQ\longrightarrow\QQ/\ZZ\longrightarrow0.
$$
The resulting long exact Tor sequence contains
$$
0\longrightarrow
\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,A)
\longrightarrow A
\longrightarrow \QQ\otimes A.
$$

::: pf-proof

The term $\operatorname{Tor}_1(\QQ,A)$ on the left is zero by step [](#s1){.pf-ref}, and $\ZZ\otimes A\cong A$.

:::

:::

::: {.pf-step #s3}

The kernel of the localization map $A\to\QQ\otimes A$ is exactly the torsion subgroup $A_{\mathrm{tors}}$.

::: pf-proof

Under $\QQ\otimes A\cong S^{-1}A$ with $S=\ZZ\setminus\{0\}$, an element $a\in A$ maps to zero iff some nonzero integer $s$ annihilates $a$, which is precisely the definition of torsion.

:::

:::

::: pf-step

Hence
$$
\boxed{\operatorname{Tor}_1^{\ZZ}(\QQ/\ZZ,A)\cong A_{\mathrm{tors}}.}
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
