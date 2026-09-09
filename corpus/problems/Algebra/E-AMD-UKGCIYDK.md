---
schema: qual/card@1
id: E-AMD-UKGCIYDK
kind: problem
title: Non-units in a local ring form a proper ideal contained in the Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Jacobson Radical
  - Maximal Ideals
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
Show that if $R$ is a local ring then $R\setminus R\units$ is a proper ideal that is contained in the Jacobson radical $J(R)$.
:::


::: {.solution}
Let $\mathfrak m$ be the unique maximal ideal of the local ring $R$.

<1>1. Every element of $\mathfrak m$ is a nonunit.
::: {.proof}
If $x\in\mathfrak m$ were a unit, then $1=x^{-1}x\in\mathfrak m$, contradicting the properness of the maximal ideal $\mathfrak m$. Thus
\[
\mathfrak m\subseteq R\setminus R\units.
\]
:::

<1>2. Every nonunit of $R$ lies in $\mathfrak m$.
::: {.proof}
Let $x\in R$ be a nonunit. Then the principal ideal $(x)$ is proper, so it is contained in a maximal ideal of $R$. Since $R$ is local, its only maximal ideal is $\mathfrak m$. Hence $x\in\mathfrak m$, and therefore
\[
R\setminus R\units\subseteq\mathfrak m.
\]
:::

<1>3. The set of nonunits is a proper ideal.
::: {.proof}
By <1>1 and <1>2,
\[
R\setminus R\units=\mathfrak m.
\]
Since $\mathfrak m$ is a proper ideal, so is the set of nonunits.
:::

<1>4. In fact, the set of nonunits equals the Jacobson radical.
::: {.proof}
By definition, $J(R)$ is the intersection of all maximal ideals of $R$. A local ring has the single maximal ideal $\mathfrak m$, so
\[
J(R)=\mathfrak m=R\setminus R\units.
\]
In particular, $R\setminus R\units\subseteq J(R)$.
:::
:::
