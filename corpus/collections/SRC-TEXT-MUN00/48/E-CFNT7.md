---
schema: qual/card@1
id: E-CFNT7
kind: problem
title: Countable unions in Baire spaces
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
---

::: {.exercise}

Let $X$ equal the countable union $\bigcup B_n$.
Show that if $X$ is a nonempty Baire space, at least one of the sets $\overline{B}_n$ has a nonempty interior.
:::

::: {.solution}
If every $\overline{B_n}$ had empty interior, then the closed sets $\overline{B_n}$ would all be nowhere dense. But
\[
X=\bigcup_nB_n\subset\bigcup_n\overline{B_n}=X,
\]
so $X$ would be a countable union of nowhere dense sets. This contradicts the Baire property for the nonempty open set $X$ itself. Hence some $\overline{B_n}$ has nonempty interior.
:::
