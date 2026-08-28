---
schema: qual/card@1
id: E-7NRBE
kind: exercise
title: The size of the Stone-Cech compactification of the positive integers
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

::: solution
**Goal:** Prove that the Stone-Čech compactification $\beta(\mathbb{Z}_+)$ has cardinality $|\beta(\mathbb{Z}_+)| \ge |I^I| = 2^\mathfrak{c}$, where $I = [0, 1]$.

<1>1. Properties of the product space $I^I$:
    *Proof:*
    <2>1. By Tychonoff's Theorem, $I^I = [0, 1]^{[0, 1]}$ is a compact Hausdorff space.
    <2>2. The cardinality of the index set and factor space is $|I| = \mathfrak{c} = 2^{\aleph_0}$, so:
        $$|I^I| = \mathfrak{c}^\mathfrak{c} = (2^{\aleph_0})^\mathfrak{c} = 2^{\aleph_0 \cdot \mathfrak{c}} = 2^\mathfrak{c}.$$
    <2>3. By the Hewitt-Marczewski-Pondiczery Theorem on product separability, a product of at most $2^{\aleph_0}$ separable spaces is separable.
    <2>4. Since $I$ is separable, $I^I$ is separable, meaning it possesses a countable dense subset $D \subseteq I^I$.

<1>2. Construction of continuous surjection $\beta(\mathbb{Z}_+) \twoheadrightarrow I^I$:
    *Proof:*
    <2>1. Enumerate the countable dense subset as $D = \{y_n \mid n \in \mathbb{Z}_+\}$.
    <2>2. Define the map $f: \mathbb{Z}_+ \to I^I$ by $f(n) = y_n$.
    <2>3. Because $\mathbb{Z}_+$ has the discrete topology, $f$ is continuous.
    <2>4. By the universal extension property of the Stone-Čech compactification $\beta(\mathbb{Z}_+)$, since $I^I$ is compact Hausdorff, there exists a unique continuous extension:
        $$\beta f: \beta(\mathbb{Z}_+) \to I^I$$
        such that $\beta f|_{\mathbb{Z}_+} = f$.
    <2>5. The image $\beta f(\beta(\mathbb{Z}_+))$ is a compact subset of $I^I$ (hence closed, as $I^I$ is Hausdorff) containing the dense set $f(\mathbb{Z}_+) = D$.
    <2>6. Therefore:
        $$\beta f(\beta(\mathbb{Z}_+)) \supseteq \overline{D} = I^I.$$
    <2>7. Thus $\beta f: \beta(\mathbb{Z}_+) \to I^I$ is surjective.

<1>3. Cardinality comparison:
    *Proof:*
    <2>1. The existence of a surjective function $\beta f: \beta(\mathbb{Z}_+) \twoheadrightarrow I^I$ immediately implies:
        $$|\beta(\mathbb{Z}_+)| \ge |I^I| = 2^\mathfrak{c}.$$
    <2>2. Furthermore, since $\beta(\mathbb{Z}_+)$ embeds into $[0, 1]^{C(\mathbb{Z}_+, [0, 1])}$ and $|C(\mathbb{Z}_+, [0, 1])| = \mathfrak{c}^{\aleph_0} = \mathfrak{c}$, we have $|\beta(\mathbb{Z}_+)| \le \mathfrak{c}^\mathfrak{c} = 2^\mathfrak{c}$, so $|\beta(\mathbb{Z}_+)| = |I^I| = 2^\mathfrak{c}$.

<1>4. Conclusion:
    $|\beta(\mathbb{Z}_+)| \ge |I^I|$. Q.E.D.
:::
