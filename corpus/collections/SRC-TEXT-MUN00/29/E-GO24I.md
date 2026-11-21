---
schema: qual/card@1
id: E-GO24I
kind: problem
title: The rationals are not locally compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 1, printed p. 186, with the
    definition of local compactness printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.1, PDF p. 21. No rational interval with
    irrational endpoints is compact, by the increasing-union cover; and a compact
    neighbourhood of a rational point would contain such an interval as a closed subset.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the rationals $\QQ$ are not locally compact.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.1, PDF p. 21** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the two-paragraph argument is theirs, with the construction of the open cover and of the irrational endpoints separated below.

Recall that $X$ is locally compact at $x$ when some compact subspace of $X$ contains a neighbourhood of $x$ (§29, printed p. 185).

::: pf

::: {.pf-step #no-compact-interval}
If $a<b$ are irrational, then $\QQ\cap[a,b]$ is not compact.

:::: {.pf-proof}

::: {.pf-step #cover}
$\QQ\cap[a,b]$ is countably infinite, say $\theset{q_{1},q_{2},\ldots}$, and the sets $U_{i}=\QQ\cap[a,q_{i})$ form an open cover of it.

::: pf-proof
$\QQ\cap[a,b]$ is countable as a subset of $\QQ$. Each $U_{i}$ is open in the subspace $\QQ\cap[a,b]$, being the trace of the open set $(-\infty,q_{i})$ of $\QQ$. For $q\in\QQ\cap[a,b]$ one has $q<b$ because $b$ is irrational, so by density of $\QQ$ there is a rational $q_{i}$ with $q<q_{i}<b$, and then $q\in U_{i}$; and $a\le q$ since $q\in[a,b]$. So the $U_{i}$ cover.
:::

:::

::: {.pf-step #no-finite-subcover}
No finite subcollection of $\theset{U_{i}}$ covers $\QQ\cap[a,b]$.

::: pf-proof
Let $U_{i_{1}},\ldots,U_{i_{n}}$ be finitely many of them and let $j=\max\theset{i_{1},\ldots,i_{n}}$. Membership $x\in U_{i}$ means $x<q_{i}$, so $U_{i}\subseteq U_{j}$ for every $i\le j$; hence the union of the chosen sets is $U_{j}$. But $q_{j}\in\QQ\cap[a,b]$ and $q_{j}\notin U_{j}$, since $q_{j}\not<q_{j}$. So the finite subcollection does not cover.
:::

:::

::: {.pf-step #not-compact}
$\QQ\cap[a,b]$ is not compact.

::: pf-proof
By steps [](#cover){.pf-ref} and [](#no-finite-subcover){.pf-ref} it has an open cover with no finite subcover.
:::

:::

::::

:::

::: {.pf-step #local}
If $\QQ$ were locally compact at $x\in\QQ$, some compact $C\subseteq\QQ$ would contain a set $\QQ\cap[a,b]$ with $a<b$ irrational, and that set would be compact.

:::: {.pf-proof}

::: {.pf-step #contained}
A compact $C$ containing a neighbourhood of $x$ contains $\QQ\cap[a,b]$ for some irrational $a<b$.

::: pf-proof
A neighbourhood of $x$ in $\QQ$ contains an open set of $\QQ$ containing $x$, hence contains $\QQ\cap(a',b')$ for some $a'<x<b'$; choosing irrationals $a,b$ with $a'<a<x<b<b'$, which is possible by density of the irrationals, gives $\QQ\cap[a,b]\subseteq\QQ\cap(a',b')$.
:::

:::

::: {.pf-step #closed-compact}
$\QQ\cap[a,b]$ is closed in $\QQ$ and contained in $C$, hence compact.

::: pf-proof
$[a,b]$ is closed in $\RR$, so $\QQ\cap[a,b]$ is closed in the subspace $\QQ$. A closed subset of the compact space $C$ is compact (Theorem 26.2, printed p. 165).
:::

:::

::::

:::

::: {.pf-qed}
Step [](#local){.pf-ref} would make $\QQ\cap[a,b]$ compact, contradicting step [](#no-compact-interval){.pf-ref}. So no point of $\QQ$ has a compact neighbourhood: $\QQ$ is not locally compact.
:::

:::

:::
