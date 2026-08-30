---
title: Is this group abelian?
order: 0
problems:
  topics:
  - Abelian Groups
  - Classification
---

# Is this group abelian?

The question is asked directly, and it is also the hidden form of "classify the groups of order $n$", since the abelian ones are settled by the structure theorem and only the rest need work.

## From the order alone

| $\size G$ | Conclusion |
| --- | --- |
| $p$ | cyclic, hence abelian |
| $p^2$ | abelian, by the class equation |
| $pq$ with $p < q$ and $p \nmid q-1$ | cyclic, hence abelian |
| $pq$ with $p \divides q-1$ | a nonabelian one exists |
| $p^3$ | need not be abelian: $D_4$ and $Q_8$ |

The $p^2$ case is the argument worth remembering: the class equation forces $Z(G)\neq 1$, and $G/Z(G)$ cyclic forces $G$ abelian, so $\size{Z(G)}$ cannot be $p$.

## From a quotient

::: {.remark title="The $G/Z(G)$ trick"}
If $G/Z(G)$ is cyclic then $G$ is abelian.
So $\size{Z(G)}$ can never be exactly $\size G / p$ for $p$ prime, which rules out most of the possibilities the class equation leaves open.
:::

## From the structure theorem

Once $G$ is known to be abelian, it is a product of cyclic groups and the classification is complete: list the partitions of each prime's exponent in $\size G$.
For $\size G = p^2 q$ there are $2\cdot 1 = 2$ abelian groups, and so on.
This is the same computation as [[algebra/modules/classify-this-module|Classify this module]] over $\ZZ$.

## When it is not abelian

Then the question is which nonabelian group, and the tools are:

- A normal Sylow subgroup, giving a semidirect product, from [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]].

- The number of elements of each order, which distinguishes $D_4$ from $Q_8$: $D_4$ has five elements of order $2$ and $Q_8$ has one.

- The abelianization $G/[G,G]$, which is an invariant computable from a presentation.

- The centre, the conjugacy class sizes, and the automorphism group, in that order of cheapness.
