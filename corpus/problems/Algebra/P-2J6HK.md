---
schema: qual/card@1
id: P-2J6HK
kind: problem
title: Groups of order $p^2$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the center quotient lemma and the elementary abelian/cyclic dichotomy.
---

::: {.exercise}
Show that every group of order $p^2$ is abelian and classify all such groups.
:::

::: {.solution}
Let $|G|=p^2$. The class equation for a finite $p$-group gives
\[
p\mid |Z(G)|,
\]
so $|Z(G)|=p$ or $p^2$.

If $|Z(G)|=p$, then $G/Z(G)$ has order $p$ and is cyclic. A standard lemma says that if $G/Z(G)$ is cyclic, then $G$ is abelian: if $G/Z(G)=\langle gZ(G)\rangle$, every element has the form $g^az$ with $z\in Z(G)$, and any two such elements commute. This would imply $Z(G)=G$, contradicting $|Z(G)|=p$. Hence
\[
Z(G)=G,
\]
so $G$ is abelian.

If $G$ has an element of order $p^2$, then it is cyclic:
\[
G\cong C_{p^2}.
\]
Otherwise every nonidentity element has order $p$. Choose $x\ne1$ and $y\notin\langle x\rangle$. Then
\[
\langle x\rangle\cap\langle y\rangle=1,
\]
and, since $G$ is abelian,
\[
G=\langle x\rangle\times\langle y\rangle\cong C_p\times C_p.
\]
Thus the two isomorphism types are
\[
C_{p^2}\quad\text{and}\quad C_p^2.
\]
:::
