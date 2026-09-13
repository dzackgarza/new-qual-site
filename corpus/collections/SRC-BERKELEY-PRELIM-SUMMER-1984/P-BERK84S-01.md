---
schema: qual/card@1
id: P-BERK84S-01
kind: problem
title: Index-two subgroups are normal
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified that the unique nontrivial left coset equals the unique nontrivial right coset for every element outside H.
---

::: {.problem}
Show that if a subgroup H of a group G has just one left coset different from itself, then it is a normal subgroup of G.
:::


::: {.solution}
Let $H\le G$. Since $H$ has exactly one left coset other than $H$ itself, there are exactly two left cosets of $H$ in $G$.

<1>1. If $g\in H$, then $gH=Hg=H$.
::: {.proof}
Because $H$ is a subgroup, left or right multiplication by an element of $H$ preserves $H$. Hence $gH=H=Hg$.
:::

<1>2. If $g\notin H$, then $gH=G\setminus H$ and $Hg=G\setminus H$.
::: {.proof}
The left cosets of $H$ partition $G$. Since there are only two of them, namely $H$ and one other coset, every $g\notin H$ lies in that unique other left coset. Thus
\[
gH=G\setminus H.
\]

The right cosets of $H$ also partition $G$, and right cosets are in bijection with left cosets by inversion:
\[
(Hx)^{-1}=x^{-1}H.
\]
Hence there are also exactly two right cosets. Since $g\notin H$, the right coset $Hg$ is the unique right coset different from $H$, so
\[
Hg=G\setminus H.
\]
Therefore $gH=Hg$.
:::

<1>3. Therefore $H$ is normal in $G$.
::: {.proof}
By <1>1 and <1>2, for every $g\in G$ we have $gH=Hg$. This is equivalent to
\[
gHg^{-1}=H
\]
for every $g\in G$. Hence
\[
\boxed{H\trianglelefteq G}.
\]
:::
:::
