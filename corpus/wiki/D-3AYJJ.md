---
schema: qual/card@1
id: D-3AYJJ
kind: definition
title: "Localization"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.definition title="Localization"}
For $R\in \CRing$ and $S \subseteq R$ a *multiplicatively closed* subset, so $RS \subseteq S$ and $1_R\in S$, the **localization of $R$ at $S$** can be constructed as
\[
R\localize{S} \da \qty{R\cross S} / \sim && (a, s)\sim (b, t) \iff \exists u\in S\quad (at-bs)u = 0_R
.\]

> Why the $u$: use in proof of transitivity.

:::
