---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W4
kind: problem
title: Normality need not pass to a coarser topology
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations:
- kind: related-to
  target: P-T09A4
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/day_3_sep_counterex_defn_extracted.md; the packet asks only part (a) of June 2009 A4.
---

::: {.problem}
Let $(X,\mathcal T)$ and $(X,\mathcal T')$ be topological spaces with $\mathcal T\subseteq\mathcal T'$.
If $(X,\mathcal T')$ is normal, must $(X,\mathcal T)$ also be normal?
:::

::: {.solution}
The answer is
\[
\boxed{\text{no}}.
\]

<1>1. Let
\[
X=\{a,b,c\}
\]
and define
\[
\boxed{
\mathcal T
=
\{\varnothing,\{c\},\{a,c\},\{b,c\},X\}}.
\]

::: {.proof}
The displayed family contains \(\varnothing\) and \(X\). Arbitrary unions and finite intersections of its members remain in the same list, so it is a topology.
:::

<1>2. Let
\[
\boxed{
\mathcal T'=\mathcal P(X)}
\]
be the discrete topology.

::: {.proof}
The power set of \(X\) is the discrete topology.
:::

<1>3. One has
\[
\boxed{
\mathcal T\subsetneq\mathcal T'}.
\]

::: {.proof}
Every member of \(\mathcal T\) is a subset of \(X\), hence belongs to \(\mathcal T'\). The inclusion is strict because, for example,
\[
\{a\}\in\mathcal T'
\]
but
\[
\{a\}\notin\mathcal T.
\]
:::

<1>4. The space
\[
(X,\mathcal T')
\]
is normal.

::: {.proof}
In a discrete space every subset is both open and closed. Thus two disjoint closed subsets are themselves disjoint open neighborhoods of one another.
:::

<1>5. In the coarser topology \(\mathcal T\), the sets
\[
\boxed{\{a\}}
\]
and
\[
\boxed{\{b\}}
\]
are closed.

::: {.proof}
Their complements are
\[
X-\{a\}=\{b,c\}\in\mathcal T
\]
and
\[
X-\{b\}=\{a,c\}\in\mathcal T.
\]
:::

<1>6. These two closed sets are disjoint.

::: {.proof}
The points \(a\) and \(b\) are distinct.
:::

<1>7. Every open neighborhood of \(a\) in \((X,\mathcal T)\) contains \(c\).

::: {.proof}
The only open sets containing \(a\) are
\[
\{a,c\}
\qquad\text{and}\qquad
X,
\]
and both contain \(c\).
:::

<1>8. Every open neighborhood of \(b\) in \((X,\mathcal T)\) also contains \(c\).

::: {.proof}
The only open sets containing \(b\) are
\[
\{b,c\}
\qquad\text{and}\qquad
X.
\]
:::

<1>9. Therefore the closed sets \(\{a\}\) and \(\{b\}\) cannot be separated by disjoint open neighborhoods.

::: {.proof}
Any open neighborhood of \(\{a\}\) contains \(c\) by step <1>7, and any open neighborhood of \(\{b\}\) contains \(c\) by step <1>8. Hence any such two neighborhoods intersect at \(c\).
:::

<1>10. Thus
\[
\boxed{
(X,\mathcal T)
\text{ is not normal}}.
\]

::: {.proof}
Steps <1>5--<1>9 give two disjoint closed subsets that cannot be separated by disjoint open neighborhoods.
:::

<1>11. Hence normality does not necessarily pass from a finer topology to a strictly coarser topology.

::: {.proof}
The finer space \((X,\mathcal T')\) is normal by step <1>4, whereas the coarser space \((X,\mathcal T)\) is not normal by step <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 answers the question.
:::
:::
