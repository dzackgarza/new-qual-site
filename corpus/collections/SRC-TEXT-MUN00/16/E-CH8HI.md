---
schema: qual/card@1
id: E-CH8HI
kind: problem
title: Product topologies under refinement of the factors
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 5, printed p. 92; both parts and the
    hypothesis that the sets are nonempty are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.5, PDF p. 5. Part (a) is his: every basis
    element of the coarser product topology is a basis element of the finer one. Part (b) is
    his too: the converse does hold, because from U x Y open in the finer product and a
    point (x,y) one gets U' open in X' with x in U' contained in U, so every open U lies in
    the finer topology. The card records that Whitman answers (b) in the negative, and why
    his counterexample fails: it passes to subspace topologies on a two-point set which
    coincide, so the hypothesis that T' is not finer than T is not satisfied.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $X$ and $X'$ denote a single set in the topologies $\mathcal{T}$ and $\mathcal{T}'$, respectively; let $Y$ and $Y'$ denote a single set in the topologies $\mathcal{U}$ and $\mathcal{U}'$, respectively.
Assume these sets are nonempty.

(a) Show that if $\mathcal{T}' \supset \mathcal{T}$ and $\mathcal{U}' \supset \mathcal{U}$, then the product topology on $X' \times Y'$ is finer than the product topology on $X \times Y$.

(b) Does the converse of (a) hold?
Justify your answer.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.5, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); part (a) and the answer to (b) are his. Part (b) is answered **no** by Whitman on his printed p. 152, and that answer is not usable: his counterexample passes to the subspace topologies on the two-point set in each factor, which coincide, so the hypothesis of the converse ($\mathcal{T}'\not\supset\mathcal{T}$) is not met; the defect is recorded on this card rather than followed.

(a) Let $W$ be a basis element of the product topology on $X\times Y$, so $W=U\times V$ with $U\in\mathcal{T}$ and $V\in\mathcal{U}$. Then $U\in\mathcal{T}'$ and $V\in\mathcal{U}'$, so $W$ is also a basis element of the product topology on $X'\times Y'$; every open set of $X\times Y$ is a union of such $W$, hence open in $X'\times Y'$. So the product topology on $X'\times Y'$ is finer than the product topology on $X\times Y$.

(b) **The converse holds**: if the product topology on $X'\times Y'$ is finer than the product topology on $X\times Y$, and $X\times Y\ne\varnothing$, then $\mathcal{T}'\supset\mathcal{T}$ and $\mathcal{U}'\supset\mathcal{U}$.

Let $U\in\mathcal{T}$ be nonempty and let $x\in U$; since $Y\ne\varnothing$ choose $y\in Y$. The set $U\times Y$ is a basis element of the product topology on $X\times Y$, hence open in $X'\times Y'$, so by the definition of the product topology there are $U'\in\mathcal{T}'$ and $V'\in\mathcal{U}'$ with
$$
(x,y)\in U'\times V'\subset U\times Y .
$$
Then $x\in U'\subset U$, so $x$ is an interior point of $U$ for the topology $\mathcal{T}'$. As $x\in U$ was arbitrary, $U\in\mathcal{T}'$; and $\varnothing\in\mathcal{T}'$ as well. So $\mathcal{T}\subset\mathcal{T}'$, and the same argument with the roles of the factors exchanged, using $X\ne\varnothing$, gives $\mathcal{U}\subset\mathcal{U}'$.

The hypothesis that the two sets are nonempty is what the argument uses; if a factor is empty then $X\times Y=\varnothing$ and both product topologies are trivial, so the converse fails.
:::
