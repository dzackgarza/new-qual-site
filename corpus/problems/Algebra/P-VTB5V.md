---
schema: qual/card@1
id: P-VTB5V
kind: problem
title: The radical of an ideal is the intersection of the primes containing it
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Prime Ideals
  - Nilpotence
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring and $I\trianglelefteq R$. Show that
\[
\sqrt I=\bigcap_{\substack{\mathfrak p\supseteq I\\ \mathfrak p\text{ prime}}}\mathfrak p.
\]
:::

::: {.solution}
First suppose $x\in\sqrt I$. Then $x^n\in I$ for some $n\ge1$. If $\mathfrak p$ is any prime ideal containing $I$, then $x^n\in\mathfrak p$, and primality implies $x\in\mathfrak p$. Thus
\[
\sqrt I\subseteq\bigcap_{\mathfrak p\supseteq I}\mathfrak p.
\]

For the reverse inclusion, suppose $x\notin\sqrt I$. Then no positive power of $x$ lies in $I$. Let
\[
S=\{1,x,x^2,\ldots\}.
\]
Thus $I\cap S=\varnothing$.

Consider the set of ideals $J$ such that
\[
I\subseteq J,
\qquad
J\cap S=\varnothing,
\]
ordered by inclusion. Every chain has an upper bound given by its union, which is again an ideal disjoint from $S$. By Zorn's lemma there is a maximal such ideal $\mathfrak p$.

We claim $\mathfrak p$ is prime. Suppose $ab\in\mathfrak p$ while $a,b\notin\mathfrak p$. By maximality, both ideals $\mathfrak p+(a)$ and $\mathfrak p+(b)$ meet $S$. Hence there exist
\[
p_1+ra=x^m,
\qquad
p_2+sb=x^n,
\]
with $p_1,p_2\in\mathfrak p$. Multiplying gives
\[
x^{m+n}=(p_1+ra)(p_2+sb)\in\mathfrak p,
\]
because $ab\in\mathfrak p$. This contradicts $\mathfrak p\cap S=\varnothing$. Hence $\mathfrak p$ is prime.

We have $I\subseteq\mathfrak p$, but $x\notin\mathfrak p$ since $x\in S$. Therefore $x$ is not in the intersection of all prime ideals containing $I$.

Thus
\[
\sqrt I=\bigcap_{\mathfrak p\supseteq I}\mathfrak p.
\]
:::
