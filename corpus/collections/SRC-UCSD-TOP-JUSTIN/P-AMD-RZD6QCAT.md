---
schema: qual/card@1
id: P-AMD-RZD6QCAT
kind: problem
title: $A\hookrightarrow B$ implies $A\otimes\QQ\hookrightarrow B\otimes\QQ$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.problem}
Show that $A\injects B \implies A\tensor \QQ \injects B\tensor \QQ$
:::

::: {.solution}

::: pf

::: pf-step

The $\ZZ$-module $\QQ$ is flat.

::: pf-proof

It is the localization $S^{-1}\ZZ$ for $S=\ZZ\setminus\{0\}$. Localization is a flat module over the original ring.

:::

:::

::: pf-step

Therefore tensoring an injection $A\hookrightarrow B$ with $\QQ$ preserves injectivity:
$$
\boxed{A\otimes_{\ZZ}\QQ\hookrightarrow B\otimes_{\ZZ}\QQ.}
$$

::: pf-proof

Start with the exact sequence
$$
0\longrightarrow A\longrightarrow B.
$$
Since $\QQ$ is flat, applying $-\otimes_{\ZZ}\QQ$ preserves exactness at the left, yielding
$$
0\longrightarrow A\otimes\QQ\longrightarrow B\otimes\QQ.
$$

:::

:::

:::

:::
