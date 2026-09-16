---
schema: qual/card@1
id: P-ABRWU
kind: problem
title: 'Contrapositive and converse of: a local minimum at $a$ implies $f''(a)=0$
  or nondifferentiability at $a$'
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f:\mathbb{R}\to\mathbb{R}$ be a function and let $a$ be a real number.
Let $S$ be the statement "If $f$ has a local minimum at $a$, then $f'(a)=0$ or $f$ is not differentiable at $a$".

a) Write the contrapositive of $S$.
b) Write the converse of $S$.
c) Which of the statements in (a) and (b) are true?
If either statement is false, give a counterexample.
:::

::: {.solution}
Write
\[
P:\ f\text{ has a local minimum at }a,
\qquad
Q:\ f'(a)=0\text{ or }f\text{ is not differentiable at }a.
\]
The contrapositive is $\neg Q\Rightarrow\neg P$, namely:

> If $f$ is differentiable at $a$ and $f'(a)\ne0$, then $f$ does not have a local minimum at $a$.

This is true because it is logically equivalent to the original statement $S$.

The converse is $Q\Rightarrow P$, namely:

> If $f'(a)=0$ or $f$ is not differentiable at $a$, then $f$ has a local minimum at $a$.

This is false. For example, $f(x)=x^3$ at $a=0$ has $f'(0)=0$ but no local minimum there. Also $f(x)=x^{1/3}$ is not differentiable at $0$ and has no local minimum there.
:::
