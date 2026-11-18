---
schema: qual/card@1
id: E-BRPKJ
kind: problem
title: Where a proof about closures of unions fails
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 7, printed p. 101; the stored
    statement is the printed paragraph and the stored criticism is the one the exercise asks
    for.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.7, printed pp.
    162-163. The diagnosis is his: what the argument needs is one index whose set meets
    every neighbourhood of x, and the hypothesis gives only an index for each neighbourhood.
    The failure is shown to be real by his reference to the example of Exercise 17.6(c),
    which is written out on the card so that it stands alone. (tmp/sources/munkres-
    solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as two steps: the exchange of quantifiers that the criticized argument makes, and the counterexample showing its conclusion is the wrong inclusion. Exercise 17.6(c) was re-checked. No statement change.
---

::: {.exercise}

Criticize the following "proof" that $\overline{\bigcup A_\alpha} \subset \bigcup \overline{A}_\alpha$: if $\theset{A_\alpha}$ is a collection of sets in $X$ and if $x \in \overline{\bigcup A_\alpha}$, then every neighborhood $U$ of $x$ intersects $\bigcup A_\alpha$.
Thus $U$ must intersect some $A_\alpha$, so that $x$ must belong to the closure of some $A_\alpha$.
Therefore, $x \in \bigcup \overline{A}_\alpha$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.7, printed pp. 162--163** (`tmp/sources/munkres-solutions-whitman.pdf`); the diagnosis and the counterexample it points to are his. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.7, PDF p. 7, states the same diagnosis.

The criticized argument runs: every neighbourhood $U$ of $x$ meets $\bigcup_{\alpha}A_{\alpha}$, therefore $U$ meets some $A_{\alpha}$, "so that $x$ must belong to the closure of some $A_{\alpha}$".

::: pf

::: {.pf-step #gap}

The passage from "every neighbourhood of $x$ meets $\bigcup_{\alpha}A_{\alpha}$" to "$x$ lies in the closure of some $A_{\alpha}$" is invalid.

::: pf-proof

For $x$ to lie in $\overline{A_{\beta}}$ one needs a single index $\beta$ such that every neighbourhood of $x$ meets $A_{\beta}$. What the hypothesis delivers is weaker: for each neighbourhood $U$ separately, an index $\alpha$ depending on $U$ with $U\cap A_{\alpha}\ne\varnothing$. Nothing makes those indices agree as $U$ varies, and in general they cannot, so the quantifiers have been exchanged.

:::

:::

::: pf-step

The conclusion of the argument, $\overline{\bigcup_{\alpha}A_{\alpha}}\subset\bigcup_{\alpha}\overline{A_{\alpha}}$, is false in general.

::: pf-proof

In $\RR$ with the standard topology let $A_{n}=(1/n,2]$ for $n\in\ZZ_{+}$ and let $x=0$. Every neighbourhood of $0$ meets $\bigcup_{n}A_{n}=(0,2]$, so $0\in\overline{\bigcup_{n}A_{n}}$. For a given $n$ the neighbourhood $(-1,1/n)$ of $0$ misses $A_{n}=(1/n,2]$, so $0\notin\overline{A_{n}}$; hence $0\notin\bigcup_{n}\overline{A_{n}}$. So the exhibited argument cannot be repaired by better bookkeeping: its conclusion is the wrong inclusion, the correct one being $\bigcup_{\alpha}\overline{A_{\alpha}}\subset\overline{\bigcup_{\alpha}A_{\alpha}}$ (Exercise 17.6(c)).

:::

:::

:::
:::
