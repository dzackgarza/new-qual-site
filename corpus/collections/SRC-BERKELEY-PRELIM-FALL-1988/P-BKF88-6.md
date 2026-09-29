---
schema: qual/card@1
id: P-BKF88-6
kind: problem
title: Closed graph implies continuity for a self-map of the unit interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let $f:[0,1]\to[0,1]$ and suppose its graph
\[
G_f=\{(x,f(x)):x\in[0,1]\}
\]
is a closed subset of the unit square.
Prove that $f$ is continuous.
:::

::: {.solution}
Let
$$
\pi_1,\pi_2:[0,1]^2\longrightarrow[0,1]
$$
denote the two coordinate projections.

::: pf

::: {.pf-step #s1}

The graph $G_f$ is compact.

::: pf-proof

The square $[0,1]^2$ is compact. By hypothesis, $G_f$ is closed in $[0,1]^2$, and a closed subset of a compact space is compact.

:::

:::

::: {.pf-step #s2}

The restricted projection
$$
\pi_1|_{G_f}:G_f\longrightarrow[0,1]
$$
is a homeomorphism.

::: pf-proof

The restriction is continuous. It is surjective because for every $x\in[0,1]$ the point $(x,f(x))$ belongs to $G_f$, and it is injective because a graph contains exactly one point with any prescribed first coordinate.

By step [](#s1){.pf-ref}, the domain $G_f$ is compact, while $[0,1]$ is Hausdorff. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism. Hence $\pi_1|_{G_f}$ is a homeomorphism.

:::

:::

::: {.pf-step #s3}

The function $f$ is continuous.

::: pf-proof

For every $x\in[0,1]$,
$$
\left(\pi_1|_{G_f}\right)^{-1}(x)
=
(x,f(x)).
$$
Therefore
$$
f
=
\pi_2\circ\left(\pi_1|_{G_f}\right)^{-1}.
$$
By step [](#s2){.pf-ref}, the inverse of $\pi_1|_{G_f}$ is continuous, and $\pi_2$ is continuous. Hence their composition $f$ is continuous.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
