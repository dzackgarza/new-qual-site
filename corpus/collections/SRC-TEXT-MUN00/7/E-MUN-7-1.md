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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 1, printed p. 51; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.1,
    printed pp. 80-81 (tmp/sources/munkres-solutions-whitman.pdf): Q_+ is the image of
    the countable Z_+ x Z_+ under (m,n) -> m/n, hence countable, and Q is Q_+ with 0 and
    -Q_+ adjoined. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §7 Exercise 1, printed p. 51, and the argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.1, printed pp. 80--81, whose surjection $\ZZ_+\times\ZZ_+\to\QQ_+$ and passage to $\QQ$ these are. The countability of $\ZZ_+\times\ZZ_+$ and the closure of countability under finite unions are used as the book states them.
---

::: {.exercise}

Show that $\QQ$ is countably infinite.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.1** (`tmp/sources/munkres-solutions-whitman.pdf`); the surjection $\ZZ_+\times\ZZ_+\to\QQ_+$ and the passage to $\QQ$ are his. The statement is Munkres, *Topology* (2000), §7 Exercise 1.

::: pf

::: {.pf-step #surjection}
The map $q(m,n)=m/n$ is a surjection of $\ZZ_+\times\ZZ_+$ onto $\QQ_+$.

::: pf-proof
Every positive rational is $m/n$ for some positive integers $m,n$, by the construction of $\QQ$; so each element of $\QQ_+$ has a preimage.
:::
:::

::: {.pf-step #product}
$\ZZ_+\times\ZZ_+$ is countable.

::: pf-proof
This is the theorem of Munkres, §7, that a finite product of countable sets is countable.
:::
:::

::: {.pf-step #positive}
$\QQ_+$ is countable.

::: pf-proof
A surjective image of a countable set is countable, applied to step [](#surjection){.pf-ref} with step [](#product){.pf-ref}.
:::
:::

::: {.pf-step #all-rationals}
$\QQ=\QQ_+\cup\{0\}\cup(-\QQ_+)$ is countable.

::: pf-proof
Negation is a bijection of $\QQ_+$ with $-\QQ_+$, so the latter is countable and the singleton $\{0\}$ is finite; a finite union of countable sets is countable.
:::
:::

::: {.pf-step #infinite}
$\QQ$ is infinite.

::: pf-proof
It contains $\ZZ_+$, and the map $n\mapsto n$ exhibits an injection of the infinite set $\ZZ_+$ into $\QQ$.
:::
:::

::: {.pf-step}
$\QQ$ is countably infinite.

::: pf-proof
Steps [](#all-rationals){.pf-ref} and [](#infinite){.pf-ref} give countability and infinitude, which is countable infinity.
:::
:::

:::
:::
