---
schema: qual/card@1
id: P-AJML4
kind: problem
title: Whether inducing an irreducible representation of a subgroup remains irreducible
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
If you have an irreducible representation of a subgroup, is the induced representation of the whole group still irreducible?
:::


::: {.solution}
No.

<1>1. Let $G=C_2$ and let $H=\{e\}$.
::: {.proof}
The trivial subgroup has a unique irreducible representation over $\CC$, namely the one-dimensional trivial representation $\mathbf 1_H$.
:::

<1>2. Its induced representation is the regular representation of $C_2$.
::: {.proof}
By definition,
\[
\operatorname{Ind}_H^G(\mathbf 1_H)\cong \CC[G]
\]
as a $G$-representation because $H$ is trivial.
:::

<1>3. This induced representation is reducible.
::: {.proof}
The regular representation of $C_2=\{1,s\}$ has basis $e_1,e_s$. The lines
\[
\CC(e_1+e_s),\qquad \CC(e_1-e_s)
\]
are both $G$-stable, giving the decomposition into the trivial and sign representations. Thus the induced representation is not irreducible.
:::

Hence induction does not in general preserve irreducibility.
:::
