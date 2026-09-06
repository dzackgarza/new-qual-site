---
schema: qual/card@1
id: P-AMD-2EM4AN2Y
kind: problem
title: $H \normal K \normal G$ need not imply $H \normal G$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Counterexamples
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 1(d).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Used H=< (12)(34) > inside the Klein four subgroup V_4 of A_4. The group
    V_4 is normal in A_4 and H is normal in the abelian group V_4, but
    conjugation by (123) sends (12)(34) to (14)(23), so H is not normal in A_4.
---

::: {.problem}
Give an example showing that
\[
H\normal K\normal G
\]
does not necessarily imply $H\normal G$.
:::

::: {.solution}
Take
\[
G=A_4,
\]
and let
\[
K=V_4
=\{e,(12)(34),(13)(24),(14)(23)\}.
\]
Finally set
\[
H=\langle(12)(34)\rangle
=\{e,(12)(34)\}.
\]

<1>1. We have $K\normal G$.
::: {.proof}
The subgroup $K$ consists of the identity together with all three double transpositions in $A_4$.
Conjugation in $S_4$ preserves cycle type, so every conjugate of a double transposition is again a double transposition.
Hence conjugation by every element of $A_4$ preserves $K$, and therefore
\[
K\normal A_4.
\]
:::

<1>2. We have $H\normal K$.
::: {.proof}
The Klein four group $K$ is abelian.
Every subgroup of an abelian group is normal, so
\[
H\normal K.
\]
:::

<1>3. The subgroup $H$ is not normal in $G$.
::: {.proof}
Let
\[
g=(123)\in A_4.
\]
Conjugating the nonidentity element of $H$ gives
\[
g(12)(34)g^{-1}
=(23)(14)
=(14)(23).
\]
This element is not in
\[
H=\{e,(12)(34)\}.
\]
Hence
\[
gHg^{-1}\ne H,
\]
so $H\not\normal A_4$.
:::

<1>4. Thus normality is not transitive.
::: {.proof}
Steps <1>1 and <1>2 give
\[
H\normal K\normal G,
\]
while <1>3 gives $H\not\normal G$.
:::
:::
