---
schema: qual/card@1
id: E-MUN-7-1
kind: problem
title: Countability of $\mathbb{Q}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that $\mathbb{Q}$ is countably infinite.
:::

::: {.solution}
The positive rationals are countable. Indeed, the map
\[
q:\mathbb Z_+\times\mathbb Z_+\longrightarrow\mathbb Q_+,
\qquad
q(m,n)=\frac mn,
\]
is surjective, and \(\mathbb Z_+\times\mathbb Z_+\) is countable. Hence \(\mathbb Q_+\) is countable.

Now
\[
\mathbb Q=\mathbb Q_+\cup\{0\}\cup(-\mathbb Q_+),
\]
a finite union of countable sets, so \(\mathbb Q\) is countable. It is infinite because it contains \(\mathbb Z_+\). Therefore
\[
\boxed{\mathbb Q\text{ is countably infinite}.}
\]
:::
