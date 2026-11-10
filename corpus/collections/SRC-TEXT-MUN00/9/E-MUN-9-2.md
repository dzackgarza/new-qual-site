---
schema: qual/card@1
id: E-MUN-9-2
kind: problem
title: Choice functions for countable collections
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 2, printed p. 61; the four collections (a)-(d) are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.2, printed pp. 101-102 (tmp/sources/munkres-solutions-whitman.pdf). His lemma gives a choice function for the nonempty subsets of any countable set by pulling back the least element of the image, which yields (a), (b) and (c); for (d) he argues that a choice function on the nonempty subsets of X^omega would well-order [0,1], which nobody has produced, and concludes that no explicit one is at hand. The card's (b) writes the listing 0,1,-1,2,-2,... rather than quoting countability of Z.
---

::: {.exercise}

Find if possible a choice function for each of the following collections, without using the choice axiom:

(a) The collection $\mathcal{A}$ of nonempty subsets of $\ZZ_{+}$ .

(b) The collection $\mathcal B$ of nonempty subsets of $\ZZ$.

(c) The collection $\mathcal C$ of nonempty subsets of $\QQ$.

(d) The collection $\mathcal{D}$ of nonempty subsets of $X^{\omega}$, where $X = \{0,1\}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.2, printed pp. 101--102** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice function of his lemma, which pulls back the least element of the image in $\ZZ_+$, is the one used in (a)--(c), and his reading of (d) is the one stated.


(a) Every nonempty $A\subseteq\ZZ_+$ has a least element. Thus
$c(A)=\min A$ is a choice function for $\mathcal A$.

(b) List the integers in the order $0,1,-1,2,-2,\ldots$. Every
nonempty $B\subseteq\ZZ$ has a first element in this list. Choosing it
defines a choice function for $\mathcal B$.

(c) Enumerate $\QQ$ as in [[E-MUN-7-1]], and write the list as
$q_1,q_2,\ldots$. For each
nonempty $C\subseteq\QQ$, choose $q_n$ for the least $n$ with $q_n\in C$.
This defines a choice function for $\mathcal C$.

(d) A choice function for *every* nonempty subset of $X^\omega$ exists
if $X^\omega$ is well-orderable: choose the least element of each subset.
Conversely, a choice function on all nonempty subsets of a set yields a
well-order of that set by transfinite recursion. Thus part (d) asks for a
well-order of $X^\omega$, which is not supplied by the coordinatewise
order or by the explicit enumerations in (a)-(c). The axiom of choice
guarantees one; without a further choice principle, its existence cannot
be concluded in ZF.
:::
