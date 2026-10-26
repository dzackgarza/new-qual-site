---
schema: qual/card@1
id: P-SQUAL2-02
kind: problem
title: A strictly coarser topology on a compact Hausdorff space is compact but not Hausdorff
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $(X,\tau)$ be compact Hausdorff, and let $\tau'$ be another topology on $X$ such that
$$\tau'\subsetneq\tau.$$
Show that $(X,\tau')$ is compact but not Hausdorff.
:::

## Compactness

::: pf

::: pf-step

Let
\[
\mathcal U
\]
be an open cover of \(X\) in the topology \(\tau'\).


::: pf-proof

To prove \((X,\tau')\) compact, it suffices to show that an arbitrary \(\tau'\)-open cover has a finite subcover.

:::

:::

::: pf-step

Every member of \(\mathcal U\) is also \(\tau\)-open.


::: pf-proof

The hypothesis
\[
\tau'\subseteq\tau
\]
means every \(\tau'\)-open set belongs to \(\tau\).

:::

:::

::: pf-step

Therefore \(\mathcal U\) is an open cover of \((X,\tau)\).


::: pf-proof

It covers the same underlying set \(X\), and all its members are \(\tau\)-open by step <1>2.

:::

:::

::: pf-step

Since \((X,\tau)\) is compact, \(\mathcal U\) has a finite subcover.


::: pf-proof

Apply compactness of \((X,\tau)\) to the cover from step <1>3.

:::

:::

::: pf-step

Hence
\[
\boxed{
(X,\tau')
\text{ is compact}.}
\]


::: pf-proof

The \(\tau'\)-open cover in step <1>1 was arbitrary.

:::

:::

::: pf-step

Consider the identity map
\[
\operatorname{id}_X:(X,\tau)\to(X,\tau').
\]


::: pf-proof

The domain and codomain have the same underlying set.

:::

:::

::: pf-step

The identity map in step <1>6 is continuous.


::: pf-proof

If
\[
U\in\tau',
\]
then
\[
\operatorname{id}_X^{-1}(U)=U.
\]
Since
\[
\tau'\subseteq\tau,
\]
the set \(U\) is \(\tau\)-open.

:::

:::

::: pf-step

The identity map is bijective.


::: pf-proof

It is the identity function on the same set \(X\).

:::

:::

::: pf-step

A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.


::: pf-proof

Let
\[
f:K\to Y
\]
be continuous and bijective, with \(K\) compact and \(Y\) Hausdorff. If \(C\subseteq K\) is closed, then \(C\) is compact, so \(f(C)\) is compact in \(Y\). Compact subsets of Hausdorff spaces are closed. Thus \(f\) is a closed bijection, so \(f^{-1}\) is continuous.

:::

:::

::: pf-step

Therefore
\[
\operatorname{id}_X:(X,\tau)\to(X,\tau')
\]
is a homeomorphism.


::: pf-proof

The domain is compact by hypothesis, the codomain is Hausdorff by the contradiction assumption, and steps <1>7--<1>8 give continuity and bijectivity. Apply step <1>9.

:::

:::

::: pf-step

Hence the inverse identity
\[
\operatorname{id}_X:(X,\tau')\to(X,\tau)
\]
is continuous.


::: pf-proof

A homeomorphism has continuous inverse.

:::

:::

::: pf-step

Therefore
\[
\boxed{\tau\subseteq\tau'}.
\]


::: pf-proof

Let
\[
U\in\tau.
\]
Continuity of the inverse identity means
\[
U=\operatorname{id}_X^{-1}(U)
\]
must be \(\tau'\)-open.

:::

:::

::: pf-step

Combining
\[
\tau'\subseteq\tau
\]
with step <1>12 gives
\[
\tau'=\tau.
\]


::: pf-proof

Two sets contained in one another are equal.

:::

:::

::: pf-step

This contradicts the strict inclusion
\[
\tau'\subsetneq\tau.
\]


::: pf-proof

The equality from step <1>13 is incompatible with the hypothesis.

:::

:::

::: pf-step

Therefore
\[
\boxed{
(X,\tau')
\text{ is not Hausdorff}.}
\]


::: pf-proof

The assumption that \((X,\tau')\) was Hausdorff led to the contradiction in step <1>14.

:::

:::

::: pf-qed

Step <1>5 proves compactness, and step <1>15 proves failure of the Hausdorff property.

:::

:::
