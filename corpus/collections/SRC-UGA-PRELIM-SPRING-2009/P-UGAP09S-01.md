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
Write the precise definition of what it means for a function $f:\RR\to\RR$ to be uniformly continuous. Then, without using the word “not,” state precisely what it means for $f$ to fail to be uniformly continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f:\RR\to\RR$ is uniformly continuous if
$$
\boxed{
\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in\RR,\quad
\abs{x-y}<\delta\Longrightarrow \abs{f(x)-f(y)}<\varepsilon }.
$$


::: pf-proof

This is the definition of uniform continuity: the same $\delta$ must work
simultaneously for every pair $x,y$ in the domain.

:::

:::

::: {.pf-step #s1-2}

The function $f$ fails to be uniformly continuous precisely when
$$
\boxed{
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x,y\in\RR
\text{ such that }
\abs{x-y}<\delta
\text{ and }
\abs{f(x)-f(y)}\ge\varepsilon_0 }.
$$


::: pf-proof

This is the logical negation of the quantifier statement in step [](#s1-1){.pf-ref}:
the existential and universal quantifiers reverse, the implication fails by
having its hypothesis true and conclusion false, and
$$
\abs{f(x)-f(y)}<\varepsilon_0
$$
becomes
$$
\abs{f(x)-f(y)}\ge\varepsilon_0.
$$
The displayed statement itself uses no occurrence of the word prohibited by
the problem.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the two requested precise statements.

:::

:::

:::
