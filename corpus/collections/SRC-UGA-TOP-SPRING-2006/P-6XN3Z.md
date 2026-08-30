---
schema: qual/card@1
id: P-6XN3Z
kind: problem
title: Whether the covering $S^2\to\RP^2$ is null-homotopic
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $S^2 \to \RP^2$ be the universal covering map.

Is this map null-homotopic?
Give a proof of your answer.
:::

::: {.solution}
<1>1. The universal covering map $p: S^2 \to \mathbb{RP}^2$ is **not null-homotopic**.
Proof: statement of claim.

<1>2. Proof via higher homotopy groups:
<2>1. Since $p: S^2 \to \mathbb{RP}^2$ is a covering map with discrete fiber $S^0 \cong \mathbb{Z}_2$, the induced homomorphism on homotopy groups:
\[
p_*: \pi_n(S^2) \xrightarrow{\sim} \pi_n(\mathbb{RP}^2)
\]
is an isomorphism for all $n \ge 2$.
Proof: long exact sequence of homotopy groups for covering spaces.
<2>2. In degree $n = 2$, $\pi_2(S^2) \cong \mathbb{Z}$.
Thus $\pi_2(\mathbb{RP}^2) \cong \mathbb{Z}$, and $p_*: \pi_2(S^2) \to \pi_2(\mathbb{RP}^2)$ is an isomorphism of non-trivial groups.
Proof: Hurewicz theorem and <2>1.
<2>3. If $p$ were null-homotopic ($p \simeq c$ for a constant map $c$), then the induced homomorphism $p_*: \pi_2(S^2) \to \pi_2(\mathbb{RP}^2)$ would be the zero homomorphism ($p_* = c_* = 0$).
Proof: homotopic maps induce identical homomorphisms on homotopy groups.
<2>4. Since $p_*$ is an isomorphism between non-trivial groups $\mathbb{Z} \to \mathbb{Z}$, $p_* \neq 0$.
This contradicts $p_* = 0$.
Proof: non-zero isomorphism cannot be the zero map.

<1>3. Conclusion:
$p: S^2 \to \mathbb{RP}^2$ is not null-homotopic. Q.E.D.
Proof: <1>1 and <1>2.
:::
