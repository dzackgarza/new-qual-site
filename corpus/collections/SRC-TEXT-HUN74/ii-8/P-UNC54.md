---
schema: qual/card@1
id: P-UNC54
kind: problem
title: Extending a quotient composition series by a simple normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Normal Subgroups
  - Simple Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the retained Hungerford II.8 exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section II.8,
    exercise 3, book page 111: "If N is a simple normal subgroup of a group G and
    G/N has a composition series, then G has a composition series." The card
    states exactly this. The proof was checked: the preimages G_i of the terms of
    a composition series of G/N form a normal series from G to N, with
    G_i/G_{i+1} ≅ Ḡ_i/Ḡ_{i+1} simple by the third isomorphism theorem; the terms
    are distinct because the Ḡ_i are; and appending {e} adds the simple factor
    N. The last step is legitimate only because Hungerford's Definition 8.6
    excludes the trivial group from being simple, so N ≠ {e} and the final
    inclusion is strict; the card's use of the hypothesis therefore matches the
    book's convention. Complete; no defect.
---

::: {.problem}
Show that if $N$ is a simple normal subgroup of a group $G$ and $G/N$ has a composition series, then $G$ has a composition series.
:::

::: {.solution}
Let
$$
G/N=\overline G_0\trianglerighteq\overline G_1
\trianglerighteq\cdots\trianglerighteq\overline G_r=\{N\}
$$
be a composition series for $G/N$, and let
$$
\pi:G\longrightarrow G/N
$$
be the quotient map. Put $G_i=\pi^{-1}(\overline G_i)$.

::: pf

::: pf-step

The preimages form a normal series
$$
G=G_0\trianglerighteq G_1\trianglerighteq\cdots
\trianglerighteq G_r=N.
$$

::: pf-proof

Since $\overline G_{i+1}\trianglelefteq\overline G_i$, the preimage
$G_{i+1}$ is normal in $G_i$. Also
$$
G_0=\pi^{-1}(G/N)=G,
\qquad
G_r=\pi^{-1}(\{N\})=N.
$$

:::

:::

::: {.pf-step #s2}

Every factor $G_i/G_{i+1}$ is simple.

::: pf-proof

The restriction of $\pi$ induces an isomorphism
$$
G_i/G_{i+1}\cong
\overline G_i/\overline G_{i+1}
$$
by the third isomorphism theorem, since $\overline G_i=G_i/N$ and
$\overline G_{i+1}=G_{i+1}/N$. The quotient on the right is simple
because the given series of $G/N$ is a composition series.

:::

:::

::: pf-step

Appending the term $\{e\}$ gives a composition series
$$
G=G_0\trianglerighteq\cdots\trianglerighteq G_r=N
\trianglerighteq\{e\}.
$$

::: pf-proof

By step [](#s2){.pf-ref} all factors above $N$ are simple. The final factor
$$
N/\{e\}\cong N
$$
is simple by hypothesis. Hence every factor in the displayed normal series is
simple, which is precisely a composition series for $G$.

:::

:::

:::

:::
