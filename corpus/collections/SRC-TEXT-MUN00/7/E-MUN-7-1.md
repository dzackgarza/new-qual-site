---
schema: qual/card@1
id: E-MUN-7-1
kind: problem
title: Countability of $\QQ$
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

Show that $\QQ$ is countably infinite.
:::

::: {.solution}
The positive rationals are countable. Indeed, the map
$$
q:\ZZ_+\times\ZZ_+\longrightarrow\QQ_+,
\qquad
q(m,n)=\frac mn,
$$
is surjective, and $\ZZ_+\times\ZZ_+$ is countable. Hence $\QQ_+$ is countable.

Now
$$
\QQ=\QQ_+\cup\{0\}\cup(-\QQ_+),
$$
a finite union of countable sets, so $\QQ$ is countable. It is infinite because it contains $\ZZ_+$. Therefore
$$
\boxed{\QQ\text{ is countably infinite}.}
$$
:::
