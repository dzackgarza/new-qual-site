---
schema: qual/card@1
id: E-HAT-1.1-1
kind: problem
title: Cancellation property for composition of paths
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that composition of paths satisfies the following cancellation property: If $f_0 \cdot g_0 \simeq f_1 \cdot g_1$ and $g_0 \simeq g_1$ then $f_0 \simeq f_1$.
:::

::: {.solution}

::: pf

::: pf-step

Properties of the path homotopy groupoid:

::: pf-proof

::: pf-step

Let $[f]$ denote the path homotopy class of a path $f: [0, 1] \to X$ relative to its endpoints $\{0, 1\}$.
The path concatenation $[f] \cdot [g] = [f \cdot g]$ is well-defined when $f(1) = g(0)$.

::: pf-proof

standard definition of path concatenation and homotopy classes.

:::

:::

::: pf-step

Path concatenation satisfies:
- **Associativity:** $([f] \cdot [g]) \cdot [h] = [f] \cdot ([g] \cdot [h])$ whenever the compositions are defined.
- **Right Identity:** $[f] \cdot [c_{f(1)}] = [f]$, where $c_x$ denotes the constant path at $x$.
- **Right Inverse:** For the reverse path $\bar{g}(s) = g(1 - s)$, $[g] \cdot [\bar{g}] = [c_{g(0)}]$.

::: pf-proof

fundamental groupoid axioms.

:::

:::

:::

:::

::: {.pf-step #s2}

Algebraic derivation of the cancellation:

::: pf-proof

::: {.pf-step #s2-1}

By hypothesis:
\[
[f_0 \cdot g_0] = [f_1 \cdot g_1] \implies [f_0] \cdot [g_0] = [f_1] \cdot [g_1].
\]

::: pf-proof

hypothesis $f_0 \cdot g_0 \simeq f_1 \cdot g_1$.

:::

:::

::: {.pf-step #s2-2}

Since $g_0 \simeq g_1$, we have $[g_0] = [g_1]$, which also gives $[\bar{g}_0] = [\bar{g}_1]$.

::: pf-proof

reversing homotopies between paths preserves path homotopy classes.

:::

:::

::: pf-step

Multiply both sides of step [](#s2-1){.pf-ref} on the right by $[\bar{g}_0]$:
\[
([f_0] \cdot [g_0]) \cdot [\bar{g}_0] = ([f_1] \cdot [g_1]) \cdot [\bar{g}_0].
\]

::: pf-proof

well-definedness of multiplication in the path groupoid.

:::

:::

::: pf-step

Applying associativity and substituting $[\bar{g}_0] = [\bar{g}_1]$ on the right-hand side:
\[
[f_0] \cdot ([g_0] \cdot [\bar{g}_0]) = [f_1] \cdot ([g_1] \cdot [\bar{g}_1]).
\]

::: pf-proof

associativity and step [](#s2-2){.pf-ref}.

:::

:::

::: pf-step

Simplifying the inverse pairs:
Since $[g_0] \cdot [\bar{g}_0] = [c_{g_0(0)}] = [c_{f_0(1)}]$ and $[g_1] \cdot [\bar{g}_1] = [c_{g_1(0)}] = [c_{f_1(1)}]$:
\[
[f_0] \cdot [c_{f_0(1)}] = [f_1] \cdot [c_{f_1(1)}] \implies [f_0] = [f_1].
\]
Thus $f_0 \simeq f_1$.

::: pf-proof

right identity property of constant paths.

:::

:::

:::

:::

::: pf-step

Conclusion:
$f_0 \simeq f_1$. Q.E.D.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

:::

:::
