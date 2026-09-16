---
schema: qual/card@1
id: P-MMAQ-KKD3SEOV36
kind: problem
title: Number of Sylow $p$-subgroups of $S_p$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the Sylow-count request with Groups 8 on PDF page 1."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked that the Sylow subgroups have prime order, the count of p-cycles, the disjoint partition by their generated subgroups, and p=2."
---

::: {.problem}
Count the number of $p$-Sylow subgroups of $S_p$.
:::

::: {.solution}
For every prime $p$, the number is $\boxed{(p-2)!}$.

<1>1. Each Sylow $p$-subgroup is cyclic of order $p$,
and its nonidentity elements are $p$-cycles.

::: {.proof}
The order of $S_p$ is $p!=p(p-1)!$, and $p$ does
not divide $(p-1)!$. Sylow subgroups therefore have
order $p$ [@DF04]. A nonidentity element generates
any group of prime order by Lagrange's theorem.

The order of a permutation is the least common
multiple of its disjoint-cycle lengths [@DF04].
For order $p$, every cycle length is $1$ or $p$,
and at least one is $p$. On exactly $p$ letters,
the permutation must thus be one $p$-cycle.
Conversely, a $p$-cycle generates a subgroup of
order $p$, which is Sylow.
:::

<1>2. Dividing the number of $p$-cycles by $p-1$
counts the Sylow subgroups exactly once.

::: {.proof}
There are $(p-1)!$ distinct $p$-cycles: write each
uniquely as $(1,a_2,\ldots,a_p)$, with the other
$p-1$ letters in arbitrary order. Each cyclic
subgroup of order $p$ has $p-1$ nonidentity elements,
all generators. Distinct such subgroups cannot
share one, since that element would generate both.
By step <1>1 these disjoint generator sets partition
the $p$-cycles. Thus the number is
$$
\frac{(p-1)!}{p-1}=(p-2)!.
$$
For $p=2$ this is $0!=1$, the subgroup $S_2$ itself.
:::
:::
