---
schema: qual/card@1
id: P-AMD-MKIM3ULY
kind: problem
title: A group with cyclic quotient by its center is abelian
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Abelian Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against the source-audited UCSD Math 200A Homework 1 occurrence and independently against standard presentations of the Dummit--Foote center-quotient lemma.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    If xZ(G) generates G/Z(G), wrote arbitrary elements as x^a z and x^b w with z,w central, then commuted the powers of x and the central factors explicitly.
---

::: {.problem}
Given: $G/Z(G)$ is cyclic

Show: $G$ is abelian
:::

::: {.solution}
Assume
\[
G/Z(G)=\langle xZ(G)\rangle
\]
for some $x\in G$.

<1>1. Every element $g\in G$ can be written
\[
g=x^a z
\]
for some $a\in\mathbb Z$ and $z\in Z(G)$.
::: {.proof}
Since $gZ(G)$ belongs to the cyclic quotient, there is $a\in\mathbb Z$ such that
\[
gZ(G)=(xZ(G))^a=x^aZ(G).
\]
Equality of the cosets implies
\[
x^{-a}g\in Z(G).
\]
Put
\[
z=x^{-a}g.
\]
Then $z\in Z(G)$ and
\[
g=x^az.
\]
:::

<1>2. Any two elements of $G$ commute.
::: {.proof}
Let $g,h\in G$.
By <1>1, write
\[
g=x^az,
\qquad
h=x^bw,
\]
with $a,b\in\mathbb Z$ and $z,w\in Z(G)$.
Since $z$ and $w$ commute with every element of $G$,
\[
\begin{aligned}
gh
&=(x^az)(x^bw)\\
&=x^{a+b}zw\\
&=x^{b+a}wz\\
&=(x^bw)(x^az)\\
&=hg.
\end{aligned}
\]
Thus every pair of elements commutes.
:::

<1>3. Therefore $G$ is abelian.
::: {.proof}
This is exactly the conclusion of <1>2.
:::
:::
