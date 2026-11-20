---
schema: qual/card@1
id: E-V7QV9
kind: problem
title: Comparing the nine topologies on a three-point set
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 2, printed p. 83, with Figure 12.1
    and the text of §12 on printed p. 77; the stored statement is the printed question. The
    nine topologies and their arrangement were re-read from printed p. 77, where the book
    itself states that the upper right-hand topology is strictly finer than the three in the
    first column, strictly coarser than the other two in the third, and incomparable with
    those in the second.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.2, printed pp.
    141-142. The answer is his: his 9x9 matrix, indexed by row and column of Figure 12.1,
    names the finer topology of each pair or records 'Inc'. The card writes the nine
    topologies out, gives the twelve cover relations of his matrix, and lists one set
    witnessing each of its twelve incomparable pairs; the twelve cover relations generate 24
    comparable pairs, which with those twelve accounts for all 36 pairs, so the comparison
    is complete. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; the mathematics of the answer is unchanged and every
    claim in it was re-checked by enumerating the nine collections as lists of subsets, with
    these results: all nine are topologies and are pairwise distinct; exactly 24 of the 36
    pairs are comparable and exactly the twelve pairs tabulated are incomparable; every one of
    the 24 witnesses is a set in one of the two topologies and not in the other; each of the
    twelve listed relations is a covering relation, no member of the nine lying between; and
    the five maximal chains are chains and cannot be enlarged. Three defects of the prose were
    found and repaired in the rewriting: the distinctness of the nine was argued with two
    witnesses that are false as stated, "{a} in T_2 - T_5" and "{b} in T_3 - T_8", both of
    those sets lying in both topologies, and no witness at all was given for T_4 and T_7,
    which have the same three members; the count of memberships checked in the cover step was
    written as forty-eight where twelve pairs give twenty-four; and the comparable pairs were
    counted as the sum 10+6+10+3+1 over the five maximal chains, which is 30 rather than 24,
    the chains sharing pairs, and which also fails to reach T_7 < T_6, a comparable pair lying
    in none of the five. The count is now taken from 36 - 12, with comparability generating
    every comparable pair by covers. Pages verified: Example 1 of §12 on printed pp. 76-77 with
    Figure 12.1, the book's remark on the upper right-hand corner on printed p. 77, and the
    exercise on printed p. 83.
---

::: {.exercise}

Consider the nine topologies on the set $X = \theset{a, b, c}$ indicated in Example 1 of §12. Compare them; that is, for each pair of topologies, determine whether they are comparable, and if so, which is the finer.
:::

::: {.solution}
The answer is the retained published solution, **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.2** (`tmp/sources/munkres-solutions-whitman.pdf`), which prints a $9\times9$ matrix for the pairs in the numbering of Figure 12.1 and adds the maximal simply ordered subcollections; the same answer is reached below from the nine lists, and it agrees with the book's own remark after Figure 12.1 (printed p. 77): there the upper right-hand topology is strictly finer than the three in the first column, strictly coarser than the other two in the third, and incomparable with the three in the second, which is exactly what steps [](#covers){.pf-ref} and [](#incomparable){.pf-ref} record for $\mathcal{T}_3$.

Throughout $X=\theset{a,b,c}$, a topology is a collection containing $\varnothing$ and $X$ and closed under arbitrary unions and finite intersections, and $\mathcal{T}<\mathcal{T}'$ means $\mathcal{T}\subsetneq\mathcal{T}'$; on a finite set closure under binary unions and binary intersections suffices. Figure 12.1 (printed pp. 76--77) shows nine topologies in the positions
$$
\begin{array}{ccc}
\mathcal{T}_1 & \mathcal{T}_2 & \mathcal{T}_3\\
\mathcal{T}_4 & \mathcal{T}_5 & \mathcal{T}_6\\
\mathcal{T}_7 & \mathcal{T}_8 & \mathcal{T}_9,
\end{array}
$$
and the lists are
$$
\begin{aligned}
\mathcal T_1&=\{\varnothing,X\}, &
\mathcal T_2&=\{\varnothing,\{a\},\{a,b\},X\}, &
\mathcal T_3&=\{\varnothing,\{b\},\{a,b\},\{b,c\},X\},\\
\mathcal T_4&=\{\varnothing,\{b\},X\}, &
\mathcal T_5&=\{\varnothing,\{a\},\{b,c\},X\}, &
\mathcal T_6&=\{\varnothing,\{b\},\{c\},\{a,b\},\{b,c\},X\},\\
\mathcal T_7&=\{\varnothing,\{a,b\},X\}, &
\mathcal T_8&=\{\varnothing,\{a\},\{b\},\{a,b\},X\}, &
\mathcal T_9&=\mathcal P(X).
\end{aligned}
$$
The three corners are given in the text of Example 1 ; the others are the same figure. The exercise is §13 Exercise 2 .

::: pf

::: {.pf-step #topologies}
Each $\mathcal T_i$ is a topology on $X$, and the nine are pairwise distinct.

::: pf-proof
Each list contains $\varnothing$ and $X$. For each, the intersection and the union of any two members is again a member, which is checked directly from the lists: in $\mathcal T_3$, for instance, $\{b\}\cap\{b,c\}=\{b\}$, $\{b\}\cup\{a,b\}=\{a,b\}$, $\{a,b\}\cup\{b,c\}=X$ and $\{a,b\}\cap\{b,c\}=\{b\}$ are all in the list, and every other pair is comparable by inclusion or has intersection $\varnothing$ or union $X$. The same reading settles the other eight, each of which is contained in $\mathcal P(X)$ and visibly closed. Distinctness follows from the cardinalities $2,4,5,3,4,6,3,5,8$, which separate all but the pairs $\mathcal T_2,\mathcal T_5$ (four members each), $\mathcal T_3,\mathcal T_8$ (five each) and $\mathcal T_4,\mathcal T_7$ (three each), and those are separated by a member: $\{a,b\}\in\mathcal T_2-\mathcal T_5$, $\{b,c\}\in\mathcal T_3-\mathcal T_8$ and $\{b\}\in\mathcal T_4-\mathcal T_7$.
:::

:::

::: {.pf-step #covers}
Twelve relations hold, each with the displayed witness in the larger topology and no member of the nine strictly between.

::: pf-proof
$$
\begin{array}{llll}
\mathcal T_1<\mathcal T_4\ (\{b\}), & \mathcal T_4<\mathcal T_3\ (\{a,b\}), & \mathcal T_3<\mathcal T_6\ (\{c\}), & \mathcal T_6<\mathcal T_9\ (\{a\}),\\
\mathcal T_4<\mathcal T_8\ (\{a\}), & \mathcal T_8<\mathcal T_9\ (\{c\}), & \mathcal T_1<\mathcal T_7\ (\{a,b\}), & \mathcal T_7<\mathcal T_2\ (\{a\}),\\
\mathcal T_2<\mathcal T_8\ (\{b\}), & \mathcal T_1<\mathcal T_5\ (\{a\}), & \mathcal T_5<\mathcal T_9\ (\{b\}), & \mathcal T_7<\mathcal T_3\ (\{b\}).
\end{array}
$$
In each entry the set in parentheses lies in the second topology because it is in its list, and not in the first because it is not in that list; that is a check of twenty-four memberships against the nine lists. For the twelve pairs, comparing the lists shows no $\mathcal T_k$ with $\mathcal T_i<\mathcal T_k<\mathcal T_j$. Note that $\mathcal T_3$ is finer than each of $\mathcal T_1,\mathcal T_4,\mathcal T_7$ and coarser than each of $\mathcal T_6,\mathcal T_9$, which is the book's remark (printed p. 77) about the upper right-hand corner.
:::

:::

::: {.pf-step #closure}
The comparable pairs are exactly the twenty-four pairs generated from those twelve by transitivity.

::: pf-proof
Every pair generated from the twelve by transitivity is comparable, inclusion being transitive. Conversely, let $\mathcal T_i<\mathcal T_j$. The set of the nine is finite, so we may choose $\mathcal T_j$ of least cardinality among the topologies strictly above $\mathcal T_i$: then $\mathcal T_i<\mathcal T_j$ is one of the twelve covers, and iterating this choice walks from $\mathcal T_i$ up to $\mathcal T_j$ by covers. Hence the generated pairs are exactly the comparable ones. Their number is twenty-four: step [](#incomparable){.pf-ref} exhibits twelve pairs that are incomparable, and $\binom92=36$, so $36-12=24$ pairs are left and all of them are comparable.
:::

:::

::: {.pf-step #incomparable}
The twelve pairs below are incomparable, each witness set lying in exactly one of the two topologies.

::: pf-proof
$$
\begin{array}{llll}
\mathcal T_2,\mathcal T_3:\ \{a\}\ / \ \{b\}; & \mathcal T_2,\mathcal T_4:\ \{a\}\ / \ \{b\}; & \mathcal T_2,\mathcal T_5:\ \{a,b\}\ / \ \{b,c\}; & \mathcal T_2,\mathcal T_6:\ \{a\}\ / \ \{b\};\\
\mathcal T_3,\mathcal T_5:\ \{b\}\ / \ \{a\}; & \mathcal T_3,\mathcal T_8:\ \{b,c\}\ / \ \{a\}; & \mathcal T_4,\mathcal T_5:\ \{b\}\ / \ \{a\}; & \mathcal T_4,\mathcal T_7:\ \{b\}\ / \ \{a,b\};\\
\mathcal T_5,\mathcal T_6:\ \{a\}\ / \ \{b\}; & \mathcal T_5,\mathcal T_7:\ \{a\}\ / \ \{a,b\}; & \mathcal T_5,\mathcal T_8:\ \{b,c\}\ / \ \{b\}; & \mathcal T_6,\mathcal T_8:\ \{c\}\ / \ \{a\}.
\end{array}
$$
In each entry the first set lies in the first topology and not the second, the second set in the second and not the first, as the lists show; so neither contains the other. The three pairs involving $\mathcal T_3$ and a second-column topology, $\mathcal T_2,\mathcal T_5,\mathcal T_8$, are the book's remark about the upper right-hand corner.
:::

:::

::: {.pf-step}
$\mathcal T_1$ is the coarsest of the nine and $\mathcal T_9$ the finest, and the maximal simply ordered subcollections are the five chains of step [](#closure){.pf-ref}.

::: pf-proof
Every pair is either comparable, by step [](#closure){.pf-ref}, or one of the twelve of step [](#incomparable){.pf-ref}; so the comparison is complete and the partial order is exactly the one displayed. $\mathcal T_1$ and $\mathcal T_9$ are the least and greatest elements of every chain, hence coarsest and finest. The maximal simply ordered subcollections, in the numbering above and in Whitman's, are the five chains of step [](#covers){.pf-ref}:
$$
\mathcal T_1<\mathcal T_4<\mathcal T_3<\mathcal T_6<\mathcal T_9,\quad
\mathcal T_1<\mathcal T_4<\mathcal T_8<\mathcal T_9,\quad
\mathcal T_1<\mathcal T_7<\mathcal T_2<\mathcal T_8<\mathcal T_9,
$$
$$
\mathcal T_1<\mathcal T_5<\mathcal T_9,\quad
\mathcal T_7<\mathcal T_3.
$$
Each is simply ordered by step [](#covers){.pf-ref} and cannot be enlarged: a topology insertable at any position would have to lie strictly between its neighbours there, and the twelve covers are exactly the covering relations, so there is no such member of the nine. Not every comparable pair lies in one of these chains — $\mathcal T_7<\mathcal T_6$ holds and no chain above contains both — which is why the chains are listed for the order and not used to count the comparable pairs.
:::

:::

:::
:::
