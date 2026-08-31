---
schema: qual/card@1
id: E-HAT-1.1-1
kind: exercise
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

Show that composition of paths satisfies the following cancellation property: If $f_0 \cdot g_0 \simeq f_1 \cdot g_1$ and $g_0 \simeq g_1$ then $f_0 \simeq f_1$.

::: {.solution}
<1>1. Properties of the path homotopy groupoid:
<2>1. Let $[f]$ denote the path homotopy class of a path $f: [0, 1] \to X$ relative to its endpoints $\{0, 1\}$.
The path concatenation $[f] \cdot [g] = [f \cdot g]$ is well-defined when $f(1) = g(0)$.
::: {.proof}
standard definition of path concatenation and homotopy classes.
:::
<2>2. Path concatenation satisfies:
- **Associativity:** $([f] \cdot [g]) \cdot [h] = [f] \cdot ([g] \cdot [h])$ whenever the compositions are defined.
- **Right Identity:** $[f] \cdot [c_{f(1)}] = [f]$, where $c_x$ denotes the constant path at $x$.
- **Right Inverse:** For the reverse path $\bar{g}(s) = g(1 - s)$, $[g] \cdot [\bar{g}] = [c_{g(0)}]$.
::: {.proof}
fundamental groupoid axioms.
:::

<1>2. Algebraic derivation of the cancellation:
<2>1. By hypothesis:
\[
[f_0 \cdot g_0] = [f_1 \cdot g_1] \implies [f_0] \cdot [g_0] = [f_1] \cdot [g_1].
\]
::: {.proof}
hypothesis $f_0 \cdot g_0 \simeq f_1 \cdot g_1$.
:::
<2>2. Since $g_0 \simeq g_1$, we have $[g_0] = [g_1]$, which also gives $[\bar{g}_0] = [\bar{g}_1]$.
::: {.proof}
reversing homotopies between paths preserves path homotopy classes.
:::
<2>3. Multiply both sides of <2>1 on the right by $[\bar{g}_0]$:
\[
([f_0] \cdot [g_0]) \cdot [\bar{g}_0] = ([f_1] \cdot [g_1]) \cdot [\bar{g}_0].
\]
::: {.proof}
well-definedness of multiplication in the path groupoid.
:::
<2>4. Applying associativity and substituting $[\bar{g}_0] = [\bar{g}_1]$ on the right-hand side:
\[
[f_0] \cdot ([g_0] \cdot [\bar{g}_0]) = [f_1] \cdot ([g_1] \cdot [\bar{g}_1]).
\]
::: {.proof}
associativity and <2>2.
:::
<2>5. Simplifying the inverse pairs:
Since $[g_0] \cdot [\bar{g}_0] = [c_{g_0(0)}] = [c_{f_0(1)}]$ and $[g_1] \cdot [\bar{g}_1] = [c_{g_1(0)}] = [c_{f_1(1)}]$:
\[
[f_0] \cdot [c_{f_0(1)}] = [f_1] \cdot [c_{f_1(1)}] \implies [f_0] = [f_1].
\]
Thus $f_0 \simeq f_1$.
::: {.proof}
right identity property of constant paths.
:::

<1>3. Conclusion:
$f_0 \simeq f_1$. Q.E.D.
::: {.proof}
<1>2.
:::
:::
