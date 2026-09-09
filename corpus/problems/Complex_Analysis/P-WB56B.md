---
schema: qual/card@1
id: P-WB56B
kind: problem
title: An uncountable $E\subset[0,1]$ meets both $(-\infty,t)$ and $(t,\infty)$ in
  uncountable sets
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
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

::: problem
Show that if $E \subset [0, 1]$ is uncountable, then there exists some $t \in (0, 1)$ such that both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable.
:::

::: solution
For $t\in[0,1]$, set
\[
L_t=E\cap[0,t),\qquad R_t=E\cap(t,1].
\]
Suppose no $t\in(0,1)$ makes both sets uncountable.

Define
\[
a=\sup\{t\in[0,1]:L_t\text{ is countable}\}.
\]
Because $L_0=\varnothing$, the set is nonempty. Since $E$ is uncountable, $a<1$ cannot fail merely because all initial segments are countable; in any case the following argument handles the endpoint possibilities.

For every rational $q<a$, $L_q$ is countable. Hence
\[
E\cap[0,a)=\bigcup_{q\in\mathbb Q,\,q<a}L_q
\]
is countable.
For every rational $q>a$, maximality of $a$ implies $L_q$ is uncountable; by the assumed failure of the conclusion, $R_q$ must therefore be countable. Hence
\[
E\cap(a,1]=\bigcup_{q\in\mathbb Q,\,q>a}R_q
\]
is countable.
Thus
\[
E=(E\cap[0,a))\cup(E\cap\{a\})\cup(E\cap(a,1]
\]
is countable, a contradiction.

Therefore some $t\in(0,1)$ has both
\[
E\cap(-\infty,t)
\quad\text{and}\quad
E\cap(t,\infty)
\]
uncountable.
:::
