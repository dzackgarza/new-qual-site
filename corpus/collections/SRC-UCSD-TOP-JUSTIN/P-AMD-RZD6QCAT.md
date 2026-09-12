---
schema: qual/card@1
id: P-AMD-RZD6QCAT
kind: problem
title: $A\hookrightarrow B$ implies $A\otimes\mathbb{Q}\hookrightarrow B\otimes\mathbb{Q}$
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
<1>1. The $\mathbb Z$-module $\mathbb Q$ is flat.
::: {.proof}
It is the localization $S^{-1}\mathbb Z$ for $S=\mathbb Z\setminus\{0\}$. Localization is a flat module over the original ring.
:::

<1>2. Therefore tensoring an injection $A\hookrightarrow B$ with $\mathbb Q$ preserves injectivity:
$$
\boxed{A\otimes_{\mathbb Z}\mathbb Q\hookrightarrow B\otimes_{\mathbb Z}\mathbb Q.}
$$
::: {.proof}
Start with the exact sequence
$$
0\longrightarrow A\longrightarrow B.
$$
Since $\mathbb Q$ is flat, applying $-\otimes_{\mathbb Z}\mathbb Q$ preserves exactness at the left, yielding
$$
0\longrightarrow A\otimes\mathbb Q\longrightarrow B\otimes\mathbb Q.
$$
:::
:::
