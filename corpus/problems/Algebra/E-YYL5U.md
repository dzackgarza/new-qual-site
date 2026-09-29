---
schema: qual/card@1
id: E-YYL5U
kind: problem
title: A ring in which every element is a unit or nilpotent is local
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Nilpotence
  - Rings
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

::: {.exercise}
Show that if $R$ is a nonzero ring where every element is either a unit or nilpotent, then $R$ is local.
:::


::: {.solution}
Let $N(R)$ denote the nilradical, i.e. the set of nilpotent elements of $R$.

::: pf

::: {.pf-step #nilpotent-not-unit}
No nilpotent element of the nonzero ring $R$ is a unit.

::: pf-proof
If $a^m=0$ and $a$ were a unit, then multiplying by $a^{-m}$ would give $1=0$, contradicting that $R$ is nonzero.
:::

:::

::: {.pf-step #nonunits-eq-nilrad}
The set of nonunits of $R$ is exactly $N(R)$.

::: pf-proof
By hypothesis every element of $R$ is either a unit or nilpotent. By step [](#nilpotent-not-unit){.pf-ref} these possibilities are disjoint. Hence an element is a nonunit exactly when it is nilpotent.
:::

:::

::: pf-step
The set of nonunits is a proper ideal.

::: pf-proof
Because $R$ is commutative, its nilpotent elements form the nilradical $N(R)=\sqrt{(0)}$, which is an ideal. It is proper because $1$ is not nilpotent in a nonzero ring. By step [](#nonunits-eq-nilrad){.pf-ref}, this ideal is exactly the set of nonunits.
:::

:::

::: {.pf-step #unique-maximal-ideal}
The ring $R$ has a unique maximal ideal.

::: pf-proof
Since $N(R)$ is proper, it is contained in some maximal ideal $\mathfrak m$. Every element of a proper ideal is a nonunit, so $\mathfrak m\subseteq N(R)$ by step [](#nonunits-eq-nilrad){.pf-ref}. Thus $N(R)=\mathfrak m$.

If $\mathfrak m'$ is any maximal ideal, then every element of $\mathfrak m'$ is a nonunit, hence lies in $N(R)=\mathfrak m$. Maximality gives $\mathfrak m'=\mathfrak m$. Thus the maximal ideal is unique.
:::

:::

::: pf-step
Therefore $R$ is local.

::: pf-proof
A nonzero commutative ring is local precisely when it has a unique maximal ideal. By step [](#unique-maximal-ideal){.pf-ref}, that ideal is $N(R)$.
:::

:::

:::

:::
