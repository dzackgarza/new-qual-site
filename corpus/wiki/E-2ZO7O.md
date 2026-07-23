---
schema: qual/card@1
id: E-2ZO7O
kind: exercise
title: "Show that the nilradical is the intersection of all prime ideals."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that the nilradical is the intersection of all prime ideals.

:::

:::{.solution}

> See A&M 1.8

Write $P$ as the intersection of all prime ideals of $R$.
\

$\nilrad{R} \subseteq P$:
Suppose $r\in \nilrad{R}$ so $r^n = 0$ and let $\mfp \in \spec R$.
Then use that $0\in I$ for any ideal: $r^n = 0 \in \mfp \implies r\in \mfp$ since $\mfp$ is prime.
\

$\nilrad{R}^c \subseteq P^c$:
Fix $f$ non-nilpotent, we want to show $f$ is not in any prime ideal.
set $S \subseteq R$ to be all ideals $I$ such that $f^{>0} \not \in I$.
Apply Zorn's lemma: $S\neq \emptyset$ since $0\in S$, so after ordering $I$ by inclusions $S$ contains a maximal $\mfp$ which we claim is prime.
If $a,b \in \mfp^c$ then $\mfp + \gens{ a }$ and $\mfp + \gens{b} supset \mfp$ strictly, and by maximality they aren't in $S$.
So there exist $m,n$ such that $f^m\in \mfp + \gens{ a }$ and $f^n \in \mfp + \gens{b}$. 
Then $f^{m+n} \in \mfp + \gens{ab}$, so $\mfp + \gens{ab}$ is not in $S$.
Thus $ab\not \in \mfp$ so $f\not\in \mfp$.
Letting $\mfp$ be arbitrary yields $f\not \in P$.
:::
