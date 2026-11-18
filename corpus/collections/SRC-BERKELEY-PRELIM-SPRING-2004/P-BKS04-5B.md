---
schema: qual/card@1
id: P-BKS04-5B
kind: problem
title: A finite group with pairwise noncommuting elements of prescribed orders
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2004
    prelim solutions, Problem 5B, PDF p. 7, the file named in the collection's provenance),
    which the card now cites; it previously carried no citation. Added: explicit disjoint sets
    of the prescribed sizes and the order of G; the verification that each g_i is a single
    cycle of length n_i and hence has exact order n_i; and the two computations
    (g_i g_j)(x) in T_j and (g_j g_i)(x) in T_i, which is what the noncommutation rests on.
    Statement unchanged.
---

::: {.problem}
Let $n_1,\ldots,n_r$ be integers $\geq2$. Prove that there is a finite group $G$ containing elements $g_1,\ldots,g_r$ such that $g_i$ has exact order $n_i$ for each $i$, and $g_ig_j\neq g_jg_i$ for $i\neq j$.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2004 prelim solutions, Problem 5B, PDF p. 7** (`assets/attachments/s04solution.pdf`, the file named in this collection's `provenance`): the construction of disjoint sets $T_i$ with $\#T_i=n_i-1$, the extra point $x$, and the $n_i$-cycles fixing everything else is that solution's. The card verifies the order and the noncommutation, which the sheet states.

Throughout $n_1,\dots,n_r\ge2$ are integers, $r\ge1$.

::: pf

::: {.pf-step #construction}
Take pairwise disjoint sets $T_1,\dots,T_r$ with $\#T_i=n_i-1$, a point $x\notin\bigcup_iT_i$, and $G=\operatorname{Sym}(S)$ for $S=\bigcup_iT_i\cup\theset{x}$. Then $G$ is a finite group of order $\bigl(1+\sum_i(n_i-1)\bigr)!$.

::: pf-proof
The $T_i$ can be chosen as disjoint finite sets of the prescribed sizes, for instance $T_i=\theset{(i,1),\dots,(i,n_i-1)}$ inside $\NN^2$; $S$ is finite of size $1+\sum_i(n_i-1)$, and the symmetric group on a finite set is a finite group of that order.

:::

:::

::: {.pf-step #orders}
The permutation $g_i$ that is the cycle $x\mapsto t_{i,1}\mapsto t_{i,2}\mapsto\cdots\mapsto t_{i,n_i-1}\mapsto x$ on $T_i\cup\theset{x}$ and fixes $S\setminus(T_i\cup\theset{x})$ has order exactly $n_i$.

::: pf-proof
$g_i$ is a single cycle of length $\#(T_i\cup\theset{x})=n_i$ on $T_i\cup\theset{x}$ and the identity elsewhere, so its order is the length $n_i$ of that cycle.

:::

:::

::: {.pf-step #noncommuting}
$g_ig_j\ne g_jg_i$ for $i\ne j$.

::: pf-proof
$g_j(x)\in T_j$, because $g_j$ cycles $x$ into $T_j$; and $g_i$ fixes every element outside $T_i\cup\theset{x}$, in particular fixes $T_j$ pointwise when $i\ne j$. So $(g_ig_j)(x)=g_i(g_j(x))=g_j(x)\in T_j$. Symmetrically $(g_jg_i)(x)\in T_i$. Since $T_i\cap T_j=\varnothing$ for $i\ne j$, the two permutations send $x$ to different points and are therefore different.

:::

:::

::: {.pf-step #conclusion}
There is a finite group containing elements of the prescribed exact orders, pairwise noncommuting.

::: pf-proof
The group $G$ of step [](#construction){.pf-ref} and its elements $g_1,\dots,g_r$ of steps [](#orders){.pf-ref} and [](#noncommuting){.pf-ref} satisfy all the requirements.

:::

:::

:::
:::
