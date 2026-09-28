---
schema: qual/card@1
id: P-MIOKF
kind: problem
title: Proper subfields of $\CC$ isomorphic to $\CC$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Transcendence
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Can it happen that a proper subfield of $\mathbb{C}$ is isomorphic to $\mathbb{C}$?
How?
:::

::: {.solution}
Yes.

Choose a transcendence basis $B$ of $\mathbb C/\mathbb Q$. Then
\[
|B|=\operatorname{trdeg}_{\mathbb Q}\mathbb C=2^{\aleph_0}.
\]
Pick $t\in B$ and put
\[
B_0=B\setminus\{t\}.
\]
Since $B$ is infinite,
\[
|B_0|=|B|.
\]
Let $K$ be the algebraic closure of $\mathbb Q(B_0)$ inside $\mathbb C$, i.e. the set of elements of $\mathbb C$ algebraic over $\mathbb Q(B_0)$.

The field $K$ is proper because $t$ is transcendental over $\mathbb Q(B_0)$, so $t\notin K$. On the other hand, $K$ is algebraically closed of characteristic $0$ and
\[
\operatorname{trdeg}_{\mathbb Q}K=|B_0|=|B|=\operatorname{trdeg}_{\mathbb Q}\mathbb C.
\]
By the classification of algebraically closed fields by characteristic and transcendence degree,
\[
K\cong\mathbb C.
\]
Thus $\mathbb C$ has a proper subfield isomorphic to itself.

Equivalently, a bijection $B\to B_0$ extends to an isomorphism
\[
\mathbb C\xrightarrow{\sim}K\subsetneq\mathbb C,
\]
giving an injective but non-surjective field endomorphism of $\mathbb C$.
:::
