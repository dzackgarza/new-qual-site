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
---

::: {.problem}
Show that if $N$ is a simple normal subgroup of a group $G$ and $G/N$ has a composition series, then $G$ has a composition series.
:::

::: solution
Let
\[
G/N=\overline G_0\trianglerighteq\overline G_1
\trianglerighteq\cdots\trianglerighteq\overline G_r=\{N\}
\]
be a composition series for $G/N$, and let
\[
\pi:G\longrightarrow G/N
\]
be the quotient map. Put $G_i=\pi^{-1}(\overline G_i)$.

<1>1. The preimages form a normal series
\[
G=G_0\trianglerighteq G_1\trianglerighteq\cdots
\trianglerighteq G_r=N.
\]
::: proof
Since $\overline G_{i+1}\trianglelefteq\overline G_i$, the preimage
$G_{i+1}$ is normal in $G_i$. Also
\[
G_0=\pi^{-1}(G/N)=G,
\qquad
G_r=\pi^{-1}(\{N\})=N.
\]
:::

<1>2. Every factor $G_i/G_{i+1}$ is simple.
::: proof
The restriction of $\pi$ induces an isomorphism
\[
G_i/G_{i+1}\cong
\overline G_i/\overline G_{i+1}
\]
by the correspondence/isomorphism theorem. The quotient on the right is simple
because the given series of $G/N$ is a composition series.
:::

<1>3. Appending the term $\{e\}$ gives a composition series
\[
G=G_0\trianglerighteq\cdots\trianglerighteq G_r=N
\trianglerighteq\{e\}.
\]
::: proof
By <1>2 all factors above $N$ are simple. The final factor
\[
N/\{e\}\cong N
\]
is simple by hypothesis. Hence every factor in the displayed normal series is
simple, which is precisely a composition series for $G$.
:::
:::
