---
schema: qual/card@1
id: P-ZWJ7K
kind: problem
title: Lower semicontinuity equivalent to $\{f>a\}$ open, and the supremum of an arbitrary
  family of lower semicontinuous functions is Borel measurable
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 2 of the official UGA Fall 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reviewed the pre-existing lower-semicontinuity proof; normalized the solution block and made explicit that the arbitrary supremum may be extended-real valued.
---

::: {.problem}
a. Let $f: \RR \to \RR$.
Prove that
$$
f(x) \leq \liminf_{y\to x} f(y)~ \text{for each}~ x\in {\RR} \iff \{ x\in {\RR} \mid f(x) > a \}~\text{is open for all}~ a\in {\RR}
$$

b. Recall that a function $f: {\RR} \to {\RR}$ is called *lower semi-continuous* iff it satisfies either condition in part (a) above.

Prove that if $\mathcal{F}$ is any family of lower semi-continuous functions, then
$$
g(x) = \sup\{ f(x) \mid f\in \mathcal{F}\}
$$
(viewed as an extended-real-valued function if the supremum is $+\infty$) is Borel measurable.

> Note that $\mathcal{F}$ need not be a countable family.
:::
::: {.solution}
<1>1. Open strict superlevel sets imply lower semicontinuity.
::: {.proof}
Assume $\{f>a\}$ is open for every $a\in\mathbb R$. Fix $x$ and $a<f(x)$. Since $x\in\{f>a\}$, every sequence $y_n\to x$ is eventually in $\{f>a\}$, so
\[
\liminf_{n\to\infty}f(y_n)\ge a.
\]
Letting $a\uparrow f(x)$ gives
\[
f(x)\le\liminf_{y\to x}f(y).
\]
:::

<1>2. Lower semicontinuity implies open strict superlevel sets.
::: {.proof}
Assume $f(x)\le\liminf_{y\to x}f(y)$ at every $x$. If $\{f>a\}$ were not open, there would be $x\in\{f>a\}$ and a sequence $y_n\to x$ with $f(y_n)\le a$. Then
\[
\liminf_{n\to\infty}f(y_n)\le a<f(x),
\]
a contradiction. Thus $\{f>a\}$ is open.
:::

<1>3. Take an arbitrary supremum.
::: {.proof}
Let
\[
g(x)=\sup_{f\in\mathcal F}f(x),
\]
possibly with value $+\infty$. For every real $a$,
\[
\{g>a\}=\bigcup_{f\in\mathcal F}\{f>a\}.
\]
Every set on the right is open because each $f$ is lower semicontinuous, and arbitrary unions of open sets are open. Hence $g$ is lower semicontinuous as an extended-real-valued function. In particular all strict superlevel sets $\{g>a\}$ are Borel, so $g$ is Borel measurable.
:::
:::
