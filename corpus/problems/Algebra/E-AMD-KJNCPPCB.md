---
schema: qual/card@1
id: E-AMD-KJNCPPCB
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
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the duplicate proof by the standard Zorn multiplicative-set argument.
---

::: {.exercise}
Show that $\sqrt I$ is the intersection of all prime ideals containing $I$.
:::

::: {.solution}
We prove
\[
\sqrt I=\bigcap_{\substack{\mathfrak p\supseteq I\\ \mathfrak p\text{ prime}}}\mathfrak p.
\]

If $x\in\sqrt I$, then $x^m\in I$ for some $m\ge1$. For every prime $\mathfrak p\supseteq I$, we have $x^m\in\mathfrak p$, hence $x\in\mathfrak p$. Thus $x$ lies in the displayed intersection.

Conversely, suppose $f\notin\sqrt I$ and let
\[
S=\{1,f,f^2,\dots\}.
\]
Then $S\cap I=\varnothing$. Consider the ideals $J\supseteq I$ with $J\cap S=\varnothing$, ordered by inclusion. A union of a chain is again such an ideal, so Zorn's lemma gives a maximal one, say $\mathfrak p$.

To see that $\mathfrak p$ is prime, suppose $a,b\notin\mathfrak p$. Maximality implies
\[
(\mathfrak p+(a))\cap S\ne\varnothing,
\qquad
(\mathfrak p+(b))\cap S\ne\varnothing.
\]
Hence for some $r,s$,
\[
f^r\in\mathfrak p+(a),\qquad f^s\in\mathfrak p+(b).
\]
If $ab\in\mathfrak p$, multiplying gives
\[
f^{r+s}\in(\mathfrak p+(a))(\mathfrak p+(b))\subseteq\mathfrak p+(ab)=\mathfrak p,
\]
contrary to $\mathfrak p\cap S=\varnothing$. Thus $ab\notin\mathfrak p$, so $\mathfrak p$ is prime. It contains $I$ but not $f$, proving that $f$ is not in the intersection of the primes over $I$.
:::
