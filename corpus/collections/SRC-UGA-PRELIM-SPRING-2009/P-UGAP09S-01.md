---
schema: qual/card@1
id: P-UGAP09S-01
kind: problem
title: Uniform continuity and its negation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Write the precise definition of what it means for a function $f:\mathbb R\to\mathbb R$ to be uniformly continuous. Then, without using the word “not,” state precisely what it means for $f$ to fail to be uniformly continuous.
:::

::: {.solution}
<1>1. The function $f:\mathbb R\to\mathbb R$ is uniformly continuous if
\[
\boxed{
\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in\mathbb R,\quad
|x-y|<\delta\Longrightarrow |f(x)-f(y)|<\varepsilon }.
\]

::: {.proof}
This is the definition of uniform continuity: the same $\delta$ must work
simultaneously for every pair $x,y$ in the domain.
:::

<1>2. The function $f$ fails to be uniformly continuous precisely when
\[
\boxed{
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x,y\in\mathbb R
\text{ such that }
|x-y|<\delta
\text{ and }
|f(x)-f(y)|\ge\varepsilon_0 }.
\]

::: {.proof}
This is the logical negation of the quantifier statement in step <1>1:
the existential and universal quantifiers reverse, the implication fails by
having its hypothesis true and conclusion false, and
\[
|f(x)-f(y)|<\varepsilon_0
\]
becomes
\[
|f(x)-f(y)|\ge\varepsilon_0.
\]
The displayed statement itself uses no occurrence of the word prohibited by
the problem.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the two requested precise statements.
:::
:::
