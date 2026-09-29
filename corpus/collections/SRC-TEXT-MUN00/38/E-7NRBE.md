---
schema: qual/card@1
id: E-7NRBE
kind: problem
title: Cardinality of the Stone--Čech compactification of $\ZZ_+$
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that $\beta(\mathbb{Z}_+)$ has cardinality at least as great as $I^I$, where $I = [0, 1]$.
[Hint: The space $I^I$ has a countable dense subset.]
:::

::: {.solution}

::: pf

::: pf-step
Properties of the product space $I^I$:

::: pf-proof

::: pf-step
By Tychonoff's Theorem, $I^I = [0, 1]^{[0, 1]}$ is a compact Hausdorff space.
:::

::: pf-step
The cardinality of the index set and factor space is $|I| = \mathfrak{c} = 2^{\aleph_0}$, so:
$$|I^I| = \mathfrak{c}^\mathfrak{c} = (2^{\aleph_0})^\mathfrak{c} = 2^{\aleph_0 \cdot \mathfrak{c}} = 2^\mathfrak{c}.$$
:::

::: pf-step
By the Hewitt-Marczewski-Pondiczery Theorem on product separability, a product of at most $2^{\aleph_0}$ separable spaces is separable.
:::

::: pf-step
Since $I$ is separable, $I^I$ is separable, meaning it possesses a countable dense subset $D \subseteq I^I$.
:::

:::

:::

::: {.pf-step #beta-surjects-onto-ii}
Construction of continuous surjection $\beta(\mathbb{Z}_+) \twoheadrightarrow I^I$:

::: pf-proof

::: pf-step
Enumerate the countable dense subset as $D = \{y_n \mid n \in \mathbb{Z}_+\}$.
:::

::: pf-step
Define the map $f: \mathbb{Z}_+ \to I^I$ by $f(n) = y_n$.
:::

::: pf-step
Because $\mathbb{Z}_+$ has the discrete topology, $f$ is continuous.
:::

::: pf-step
By the universal extension property of the Stone-Čech compactification $\beta(\mathbb{Z}_+)$, since $I^I$ is compact Hausdorff, there exists a unique continuous extension:
$$\beta f: \beta(\mathbb{Z}_+) \to I^I$$
such that $\beta f|_{\mathbb{Z}_+} = f$.
:::

::: pf-step
The image $\beta f(\beta(\mathbb{Z}_+))$ is a compact subset of $I^I$ (hence closed, as $I^I$ is Hausdorff) containing the dense set $f(\mathbb{Z}_+) = D$.
:::

::: pf-step
Therefore:
$$\beta f(\beta(\mathbb{Z}_+)) \supseteq \overline{D} = I^I.$$
:::

::: pf-step
Thus $\beta f: \beta(\mathbb{Z}_+) \to I^I$ is surjective.
:::

:::

:::

::: {.pf-step #cardinality-comparison}
Cardinality comparison:

::: pf-proof

::: pf-step
Since $\beta f: \beta(\mathbb{Z}_+) \to I^I$ is surjective by step [](#beta-surjects-onto-ii){.pf-ref},
$$|\beta(\mathbb{Z}_+)| \ge |I^I| = 2^\mathfrak{c}.$$
:::

::: pf-step
Furthermore, since $\beta(\mathbb{Z}_+)$ embeds into $[0, 1]^{C(\mathbb{Z}_+, [0, 1])}$ and $|C(\mathbb{Z}_+, [0, 1])| = \mathfrak{c}^{\aleph_0} = \mathfrak{c}$, we have $|\beta(\mathbb{Z}_+)| \le \mathfrak{c}^\mathfrak{c} = 2^\mathfrak{c}$, so $|\beta(\mathbb{Z}_+)| = |I^I| = 2^\mathfrak{c}$.
:::

:::

:::

::: pf-qed
Step [](#cardinality-comparison){.pf-ref} gives $|\beta(\mathbb{Z}_+)| \ge |I^I|$.
:::

:::

:::
