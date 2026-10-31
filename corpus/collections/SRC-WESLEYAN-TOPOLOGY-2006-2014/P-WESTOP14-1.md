---
schema: qual/card@1
id: P-WESTOP14-1
kind: problem
title: Continuous images preserve connectedness and compactness
classification: {areas: [topology], topics: [Connectedness, Compactness, Continuity]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Prove that the image of a connected space under a continuous map is connected.
2. Prove that the image of a compact space under a continuous map is compact.
:::

::: {.solution}

Let $f:X\to Y$ be continuous.

::: pf

::: pf-step

If $X$ is connected, then $f(X)$ is connected.

::: pf-proof

Suppose for contradiction that $f(X)$ is disconnected. Then there are disjoint nonempty sets $U,V\subseteq f(X)$ that are open in the subspace topology and satisfy
$$
f(X)=U\cup V.
$$
Because $U$ and $V$ are open in $f(X)$ and $f:X\to f(X)$ is continuous, the inverse images
$$
f^{-1}(U),
\qquad
f^{-1}(V)
$$
are open in $X$. They are disjoint and their union is $X$. They are both nonempty because $U$ and $V$ are nonempty subsets of the image. Thus they form a separation of $X$, contradicting connectedness.

:::

:::

::: pf-step

If $X$ is compact, then $f(X)$ is compact.

::: pf-proof

Let $\{U_\alpha\}_{\alpha\in A}$ be an open cover of $f(X)$ in the subspace topology. For each $\alpha$, the set
$$
f^{-1}(U_\alpha)
$$
is open in $X$ by continuity. Since the $U_\alpha$ cover $f(X)$, the sets $f^{-1}(U_\alpha)$ cover $X$.

Compactness of $X$ gives indices $\alpha_1,\ldots,\alpha_m$ such that
$$
X
=
f^{-1}(U_{\alpha_1})\cup\cdots\cup f^{-1}(U_{\alpha_m}).
$$
Applying $f$ shows
$$
f(X)
\subseteq
U_{\alpha_1}\cup\cdots\cup U_{\alpha_m}.
$$
Hence the original cover has a finite subcover of $f(X)$, so $f(X)$ is compact.

:::

:::

:::

:::
