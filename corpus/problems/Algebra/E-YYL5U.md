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

<1>1. No nilpotent element of the nonzero ring $R$ is a unit.
::: {.proof}
If $a^m=0$ and $a$ were a unit, then multiplying by $a^{-m}$ would give $1=0$, contradicting that $R$ is nonzero.
:::

<1>2. The set of nonunits of $R$ is exactly $N(R)$.
::: {.proof}
By hypothesis every element of $R$ is either a unit or nilpotent. By <1>1 these possibilities are disjoint. Hence an element is a nonunit exactly when it is nilpotent.
:::

<1>3. The set of nonunits is a proper ideal.
::: {.proof}
Because $R$ is commutative, its nilpotent elements form the nilradical $N(R)=\sqrt{(0)}$, which is an ideal. It is proper because $1$ is not nilpotent in a nonzero ring. By <1>2, this ideal is exactly the set of nonunits.
:::

<1>4. The ring $R$ has a unique maximal ideal.
::: {.proof}
Since $N(R)$ is proper, it is contained in some maximal ideal $\mathfrak m$. Every element of a proper ideal is a nonunit, so $\mathfrak m\subseteq N(R)$ by <1>2. Thus $N(R)=\mathfrak m$.

If $\mathfrak m'$ is any maximal ideal, then every element of $\mathfrak m'$ is a nonunit, hence lies in $N(R)=\mathfrak m$. Maximality gives $\mathfrak m'=\mathfrak m$. Thus the maximal ideal is unique.
:::

<1>5. Therefore $R$ is local.
::: {.proof}
A nonzero commutative ring is local precisely when it has a unique maximal ideal. By <1>4, that ideal is $N(R)$.
:::
:::
