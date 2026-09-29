---
schema: qual/card@1
id: P-HCAO36
kind: problem
title: Equality of extended ideals and faithful flatness
classification:
  areas:
  - algebra
  topics:
  - Faithful Flatness
  - Ideals
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $A \subseteq B$ be a ring extension, and let $I \subseteq J$ be ideals of $A$.

a. If $IB=JB$, must $I=J$?
Give a counterexample if not.

b. Give a hypothesis on the extension $A \subseteq B$ which ensures that $IB=JB$ implies $I=J$.
:::

::: {.solution}

::: pf

::: pf-step
In general, equality after extension does not imply equality before
extension.

::: pf-proof
Take
\[
A=\mathbb Z,
\qquad
B=\mathbb Q,
\qquad
I=(2),
\qquad
J=(1).
\]
Then $I\subsetneq J$, but $2$ is a unit in $\mathbb Q$, so
\[
IB=2\mathbb Q=\mathbb Q=JB.
\]
:::

:::

::: {.pf-step #faithfully-flat-injective-on-ideals}
If $B$ is faithfully flat over $A$, then $IB=JB$ implies $I=J$.

::: pf-proof
Because $I\subseteq J$, there is an exact sequence
\[
0\longrightarrow I\longrightarrow J\longrightarrow J/I\longrightarrow0.
\]
Flatness of $B$ gives
\[
(J/I)\otimes_A B\cong JB/IB.
\]
If $IB=JB$, the right-hand side is zero. Faithful flatness detects zero
modules, so $J/I=0$. Hence $I=J$.
:::

:::

::: pf-step
If $B$ is faithfully flat over $A$, then every ideal is contracted from
its extension:
\[
IB\cap A=I
\]
for every ideal $I\subseteq A$.

::: pf-proof
Apply step [](#faithfully-flat-injective-on-ideals){.pf-ref} to $I\subseteq IB\cap A$. Extending both ideals to $B$ gives $IB$
in each case, hence they are equal.
:::

:::

:::
:::
