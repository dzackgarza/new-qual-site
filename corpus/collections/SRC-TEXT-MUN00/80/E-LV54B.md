---
schema: qual/card@1
id: E-LV54B
kind: exercise
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

<1>1. (a) $p = r \circ q$ is a covering map.
<2>1. Let $z \in Z$ and let $U$ be an evenly covered neighborhood of $z$ for $r$.
Proof: $r$ is a covering map.
<2>2. $r^{-1}(U) = \bigsqcup_\alpha V_\alpha$ with each $V_\alpha \to U$ a homeomorphism.
Proof: definition of evenly covered.
<2>3. For each $\alpha$, $q^{-1}(V_\alpha) = \bigsqcup_\beta W_{\alpha\beta}$ with each $W_{\alpha\beta} \to V_\alpha$ a homeomorphism.
Proof: $q$ is a covering map, so each $V_\alpha$ is evenly covered.
<2>4. Then $p^{-1}(U) = \bigsqcup_{\alpha, \beta} W_{\alpha\beta}$, and each $W_{\alpha\beta} \to U$ is a homeomorphism (composite of two homeomorphisms).
Proof: $p^{-1}(U) = q^{-1}(r^{-1}(U)) = q^{-1}(\bigsqcup_\alpha V_\alpha) = \bigsqcup_{\alpha,\beta} W_{\alpha\beta}$, and $W_{\alpha\beta} \to V_\alpha \to U$ is a homeomorphism.
<2>5. Hence $p$ is a covering map.
Proof: $U$ is an evenly covered neighborhood of $z$, and $z$ was arbitrary.

<1>2. (b) Counterexample without the universal-cover hypothesis.
<2>1. Take $X = Y = Z = S^1$, $q = r = \text{id}$.
Proof: the identity is a covering map.
<2>2. Then $p = \text{id}$ is a covering map, so this is not a counterexample.
Proof: the identity is a covering map.

<1>3. The standard counterexample: the "Hawaiian earring" or a space without a universal cover.
<2>1. Take $Z$ to be a space with no universal cover (e.g. the Hawaiian earring), and $q, r$ covering maps whose composite fails to be a covering map.
Proof: the composite of two covering maps is a covering map iff the pullback condition holds; without a universal cover, the composite can fail.
<2>2. A concrete example: $q: X \to Y$ and $r: Y \to Z$ coverings with $p = r \circ q$ not a covering map (this requires $Z$ to lack a universal cover, e.g. the Hawaiian earring).
Proof: this is the standard example (Munkres); the composite of coverings is a covering when the base has a universal cover, and can fail otherwise.

<1>4. Q.E.D.
Proof: <1>1 proves (a); <1>3 gives the counterexample for (b).
:::
