---
schema: qual/card@1
id: P-WESCA04-T1
kind: problem
title: "State the Casorati–Weierstrass theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.1, item 1 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the Casorati–Weierstrass theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Casorati--Weierstrass Theorem.**

Let $f$ be holomorphic on a punctured neighborhood
$$
0<\abs{z-z_0}<r
$$
and suppose $z_0$ is an essential singularity of $f$.
Then for every
$$
0<\rho<r,
$$
the image
$$
f\bigl(
\{z:0<\abs{z-z_0}<\rho\}
\bigr)
$$
is dense in
$$
\CC.
$$


::: pf-proof

Equivalently, for every
$$
w\in\CC
$$
and every
$$
\varepsilon>0,
$$
there exists
$$
z
$$
with
$$
0<\abs{z-z_0}<\rho
$$
such that
$$
\abs{f(z)-w}<\varepsilon.
$$

Equivalently again, every complex number is a limit of values
$$
f(z_n)
$$
along some sequence
$$
z_n\to z_0,
\qquad
z_n\ne z_0.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement.

:::

:::

:::
