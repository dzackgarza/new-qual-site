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

Show that $\beta(\ZZ_+)$ has cardinality at least as great as $I^I$, where $I = [0, 1]$.
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
Construction of continuous surjection $\beta(\ZZ_+) \twoheadrightarrow I^I$:

::: pf-proof

::: pf-step
Enumerate the countable dense subset as $D = \{y_n \mid n \in \ZZ_+\}$.
:::

::: pf-step
Define the map $f: \ZZ_+ \to I^I$ by $f(n) = y_n$.
:::

::: pf-step
Because $\ZZ_+$ has the discrete topology, $f$ is continuous.
:::

::: pf-step
By the universal extension property of the Stone-Čech compactification $\beta(\ZZ_+)$, since $I^I$ is compact Hausdorff, there exists a unique continuous extension:
$$\beta f: \beta(\ZZ_+) \to I^I$$
such that $\beta f|_{\ZZ_+} = f$.
:::

::: pf-step
The image $\beta f(\beta(\ZZ_+))$ is a compact subset of $I^I$ (hence closed, as $I^I$ is Hausdorff) containing the dense set $f(\ZZ_+) = D$.
:::

::: pf-step
Therefore:
$$\beta f(\beta(\ZZ_+)) \supseteq \overline{D} = I^I.$$
:::

::: pf-step
Thus $\beta f: \beta(\ZZ_+) \to I^I$ is surjective.
:::

:::

:::

::: {.pf-step #cardinality-comparison}
Cardinality comparison:

::: pf-proof

::: pf-step
Since $\beta f: \beta(\ZZ_+) \to I^I$ is surjective by step [](#beta-surjects-onto-ii){.pf-ref},
$$|\beta(\ZZ_+)| \ge |I^I| = 2^\mathfrak{c}.$$
:::

::: pf-step
Furthermore, since $\beta(\ZZ_+)$ embeds into $[0, 1]^{C(\ZZ_+, [0, 1])}$ and $|C(\ZZ_+, [0, 1])| = \mathfrak{c}^{\aleph_0} = \mathfrak{c}$, we have $|\beta(\ZZ_+)| \le \mathfrak{c}^\mathfrak{c} = 2^\mathfrak{c}$, so $|\beta(\ZZ_+)| = |I^I| = 2^\mathfrak{c}$.
:::

:::

:::

::: pf-qed
Step [](#cardinality-comparison){.pf-ref} gives $|\beta(\ZZ_+)| \ge |I^I|$.
:::

:::

:::
