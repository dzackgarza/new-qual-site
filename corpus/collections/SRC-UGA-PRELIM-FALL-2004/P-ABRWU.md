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
Let $f:\RR\to\RR$ be a function and let $a$ be a real number.
Let $S$ be the statement "If $f$ has a local minimum at $a$, then $f'(a)=0$ or $f$ is not differentiable at $a$".

(a) Write the contrapositive of $S$.

(b) Write the converse of $S$.

(c) Which of the statements in (a) and (b) are true?
If either statement is false, give a counterexample.
:::

::: {.solution}

The three answers are the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Write $P$ for "$f$ has a local minimum at $a$" and $Q$ for "$f'(a)=0$ or $f$ is not differentiable at $a$", so that $S$ is $P\Rightarrow Q$.

::: pf

::: {.pf-step #contrapositive}
(a) The contrapositive of $S$ is: if $f$ is differentiable at $a$ and $f'(a)\ne0$, then $f$ does not have a local minimum at $a$.

::: pf-proof
The contrapositive of $P\Rightarrow Q$ is $\lnot Q\Rightarrow\lnot P$. The negation of $Q$ is "it is false that $f'(a)=0$ or $f$ is not differentiable at $a$", that is "$f'(a)\ne0$ and $f$ is differentiable at $a$", by De Morgan and the fact that $f'(a)$ is defined exactly when $f$ is differentiable at $a$. The negation of $P$ is " $f$ does not have a local minimum at $a$ ". So the contrapositive is the displayed statement.
:::

:::

::: {.pf-step #converse}
(b) The converse of $S$ is: if $f'(a)=0$ or $f$ is not differentiable at $a$, then $f$ has a local minimum at $a$.

::: pf-proof
The converse of $P\Rightarrow Q$ is $Q\Rightarrow P$, and substituting the two statements gives the display.
:::

:::

::: {.pf-step #truth}
(c) The contrapositive of (a) is true and the converse of (b) is false.

::: pf-proof
A statement and its contrapositive are logically equivalent, so (a) has the truth value of $S$, which is true: this is Fermat's theorem, that a function differentiable at a local minimum has derivative $0$ there. The converse is refuted twice over. First, $f(x)=x^{3}$ at $a=0$: $f'(0)=0$ so $Q$ holds, while $f$ is strictly increasing and has no local minimum at $0$, so $P$ fails. Second, $f(x)=x^{1/3}$ at $a=0$: $f$ is not differentiable at $0$, so $Q$ holds by its second alternative, while $f$ is strictly increasing and has no local minimum at $0$. Either counterexample shows the converse is false.
:::

:::

:::
:::
