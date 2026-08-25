---
schema: qual/card@1
id: P-LOXDS
kind: problem
title: Uncountable $E\subset[0,1]$ is uncountable on both sides of some $t$
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
---

:::{.problem}
Show that if $E\subset [0, 1]$ is uncountable, then there is some $t\in \RR$ such that $E\intersect (-\infty ,t)$ and $E\intersect (t, \infty)$ are also uncountable.
:::


:::{.solution}
See 3.2.12 of Understanding analysis 2ed. of Abbott.
Show something stronger, that the following set is nonempty and open:
\[
S \da \ts{t\in \RR \st E \intersect (-\infty, t), E \intersect (t, \infty) \text{ are uncountable}}
\subseteq \RR
.\]
Write
\[
S_- &\da \ts{ t\in \RR \st E \intersect (- \infty, t) \text{ is countable}} \\
S_+ &\da \ts{ s\in \RR \st E \intersect (s, \infty) \text{ is countable}}
.\]

Note that $S_- \neq \RR$ since then we could write $E = \Union_{n\in \ZZ} E \intersect (- \infty, n)$ as a countable union of countable sets.

Claim: $S = (\sup S_-,, \inf S_+)$.

???

:::




