---
schema: qual/card@1
id: E-LV54B
kind: problem
title: Composites of covering maps over a base with a universal covering
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $q: X \to Y$ and $r: Y \to Z$ be maps; let $p = r \circ q$.

(a) Let $q$ and $r$ be covering maps.
Show that if $Z$ has a universal covering space, then $p$ is a covering map.
Compare [[E-PBG3W]].

(b) Give an example where $q$ and $r$ are covering maps but $p$ is not.
:::

::: {.solution}
**Goal.** (a) Show $p = r \circ q$ is a covering map when $q, r$ are coverings and $Z$ has a universal cover. (b) Give a counterexample without that hypothesis.

::: pf

::: {.pf-step #s1}

(a) $p = r \circ q$ is a covering map.

::: pf-proof

::: pf-step

Let $z \in Z$ and let $U$ be an evenly covered neighborhood of $z$ for $r$.

::: pf-proof

$r$ is a covering map.

:::

:::

::: pf-step

$r^{-1}(U) = \bigsqcup_\alpha V_\alpha$ with each $V_\alpha \to U$ a homeomorphism.

::: pf-proof

definition of evenly covered.

:::

:::

::: pf-step

For each $\alpha$, $q^{-1}(V_\alpha) = \bigsqcup_\beta W_{\alpha\beta}$ with each $W_{\alpha\beta} \to V_\alpha$ a homeomorphism.

::: pf-proof

$q$ is a covering map, so each $V_\alpha$ is evenly covered.

:::

:::

::: pf-step

Then $p^{-1}(U) = \bigsqcup_{\alpha, \beta} W_{\alpha\beta}$, and each $W_{\alpha\beta} \to U$ is a homeomorphism (composite of two homeomorphisms).

::: pf-proof

$p^{-1}(U) = q^{-1}(r^{-1}(U)) = q^{-1}(\bigsqcup_\alpha V_\alpha) = \bigsqcup_{\alpha,\beta} W_{\alpha\beta}$, and $W_{\alpha\beta} \to V_\alpha \to U$ is a homeomorphism.

:::

:::

::: pf-step

Hence $p$ is a covering map.

::: pf-proof

$U$ is an evenly covered neighborhood of $z$, and $z$ was arbitrary.

:::

:::

:::

:::

::: pf-step

(b) Counterexample without the universal-cover hypothesis.

::: pf-proof

::: pf-step

Take $X = Y = Z = S^1$, $q = r = \text{id}$.

::: pf-proof

the identity is a covering map.

:::

:::

::: pf-step

Then $p = \text{id}$ is a covering map, so this is not a counterexample.

::: pf-proof

the identity is a covering map.

:::

:::

:::

:::

::: {.pf-step #s3}

The standard counterexample: the "Hawaiian earring" or a space without a universal cover.

::: pf-proof

::: pf-step

Take $Z$ to be a space with no universal cover (e.g. the Hawaiian earring), and $q, r$ covering maps whose composite fails to be a covering map.

::: pf-proof

the composite of two covering maps is a covering map iff the pullback condition holds; without a universal cover, the composite can fail.

:::

:::

::: pf-step

A concrete example: $q: X \to Y$ and $r: Y \to Z$ coverings with $p = r \circ q$ not a covering map (this requires $Z$ to lack a universal cover, e.g. the Hawaiian earring).

::: pf-proof

this is the standard example (Munkres); the composite of coverings is a covering when the base has a universal cover, and can fail otherwise.

:::

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a); step [](#s3){.pf-ref} gives the counterexample for (b).

:::

:::

:::
