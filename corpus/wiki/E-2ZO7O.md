---
schema: qual/card@1
id: E-2ZO7O
kind: exercise
title: "Show that the nilradical is the intersection of all prime ideals."
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - prime-ideals
  - ideals
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that the nilradical is the intersection of all prime ideals.
:::

::: {.solution}

> See A&M 1.8

Write $P$ as the intersection of all prime ideals of $R$.
\

$\nilrad{R} \subseteq P$: Suppose $r\in \nilrad{R}$ so $r^n = 0$ and let $\mfp \in \spec R$.
Then use that $0\in I$ for any ideal: $r^n = 0 \in \mfp \implies r\in \mfp$, by induction on $n$ using that $\mfp$ is prime.
\

$\nilrad{R}^c \subseteq P^c$: Fix $f$ non-nilpotent; we want to produce one prime ideal that does not contain $f$.
Set $S$ to be the collection of ideals $I$ such that $f^n \not\in I$ for every $n\geq 1$.
Apply Zorn's lemma: $S\neq \emptyset$ since $\gens{0}\in S$, because $f$ is not nilpotent.
Ordering $S$ by inclusion, a union of a chain in $S$ is again in $S$, so $S$ contains a maximal element $\mfp$, which we claim is prime.
If $a,b \in \mfp^c$ then $\mfp + \gens{ a }$ and $\mfp + \gens{b} \supset \mfp$ strictly, and by maximality they aren't in $S$.
So there exist $m,n$ such that $f^m\in \mfp + \gens{ a }$ and $f^n \in \mfp + \gens{b}$.
Then $f^{m+n} \in \mfp + \gens{ab}$, so $\mfp + \gens{ab}$ is not in $S$, which forces $\mfp + \gens{ab} \supsetneq \mfp$.
Thus $ab\not \in \mfp$, and $\mfp$ is prime.
Since $\mfp\in S$ we have $f\not\in \mfp$, so $\mfp$ is a prime ideal missing $f$ and therefore $f\not \in P$.
:::
