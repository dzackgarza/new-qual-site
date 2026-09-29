---
schema: qual/card@1
id: P-BKS05-4B
kind: problem
title: Functions with compact graph are continuous
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained closed-set proof: slice the compact
    graph by the inverse image of a closed set under the second projection,
    then project that compact slice to the domain coordinate.
---

::: {.problem}
Let $D$ be a subset of $\RR$, and let $f\colon D\to\RR$ be a function.
The graph of $f$ is the subset

$$
G\coloneqq\{(x,y):x\in D,\ y=f(x)\}
$$

of $\RR^2$. Prove that if $G$ is compact, then $f$ is continuous.
:::

::: {.solution}
Let
$$
\pi_1,\pi_2:\RR^2\longrightarrow\RR
$$
be the coordinate projections.

::: pf

::: {.pf-step #s1}

For every closed set $C\subseteq\RR$, the set
$$
G_C\coloneqq G\cap\pi_2^{-1}(C)
$$
is compact.

::: pf-proof

The projection $\pi_2$ is continuous, so $\pi_2^{-1}(C)$ is closed
in $\RR^2$. Hence $G_C$ is closed in the compact set $G$, and is
therefore compact.

:::

:::

::: {.pf-step #s2}

For every closed set $C\subseteq\RR$,
$$
f^{-1}(C)=\pi_1(G_C).
$$

::: pf-proof

For $x\in D$,
$$
x\in f^{-1}(C)
$$
exactly when $f(x)\in C$, which is equivalent to
$$
(x,f(x))\in G\cap\pi_2^{-1}(C)=G_C.
$$
This is exactly the condition $x\in\pi_1(G_C)$.

:::

:::

::: {.pf-step #s3}

For every closed set $C\subseteq\RR$, the inverse image
$f^{-1}(C)$ is closed in $D$.

::: pf-proof

By step [](#s1){.pf-ref}, $G_C$ is compact. Since $\pi_1$ is continuous,
step [](#s2){.pf-ref} shows that $f^{-1}(C)=\pi_1(G_C)$ is compact in $\RR$.
Every compact subset of $\RR$ is closed in $\RR$, hence in the
subspace $D$.

:::

:::

::: {.pf-step #s4}

The function $f:D\to\RR$ is continuous.

::: pf-proof

Step [](#s3){.pf-ref} shows that the inverse image under $f$ of every closed subset
of $\RR$ is closed in $D$. This is the closed-set characterization of
continuity.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
