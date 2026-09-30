---
schema: qual/card@1
id: E-2ZO7O
kind: problem
title: The nilradical is the intersection of all prime ideals
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Ideals
relations: []
review: draft
---

::: {.exercise}
Show that the nilradical is the intersection of all prime ideals.
:::

::: {.solution}
This is [@AM18, Proposition 1.8].
Let $R$ be a commutative ring and let $P$ be the intersection of all prime ideals of $R$.
\

$\nilrad{R} \subseteq P$: Suppose $r\in \nilrad{R}$ so $r^n = 0$ and let $\mfp \in \Spec R$.
Then $r^n = 0 \in \mfp$, and induction on $n$ using that $\mfp$ is prime gives $r\in \mfp$.
\

$\nilrad{R}^c \subseteq P^c$: Fix $f$ non-nilpotent; we want to produce one prime ideal that does not contain $f$.
Set $S$ to be the collection of ideals $I$ such that $f^n \not\in I$ for every $n\geq 1$.
Apply Zorn's lemma: $S\neq \emptyset$ since $\generators{0}\in S$, because $f$ is not nilpotent.
Ordering $S$ by inclusion, a union of a chain in $S$ is again in $S$, so $S$ contains a maximal element $\mfp$, which we claim is prime.
If $a,b \in \mfp^c$ then $\mfp + \generators{ a }$ and $\mfp + \generators{b} \supset \mfp$ strictly, and by maximality they aren't in $S$.
So there exist $m,n$ such that $f^m\in \mfp + \generators{ a }$ and $f^n \in \mfp + \generators{b}$.
Then $f^{m+n} \in \mfp + \generators{ab}$, so $\mfp + \generators{ab}$ is not in $S$, which forces $\mfp + \generators{ab} \supsetneq \mfp$.
Thus $ab\not \in \mfp$, and $\mfp$ is prime.
Since $\mfp\in S$ we have $f\not\in \mfp$, so $\mfp$ is a prime ideal missing $f$ and therefore $f\not \in P$.
:::
