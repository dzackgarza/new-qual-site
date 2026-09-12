---
schema: qual/card@1
id: E-AMD-HWVXZVE4
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
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that for an ideal $I\trianglelefteq R$ in a commutative ring $R$, its radical $\sqrt{I}$ is the intersection of all prime ideals containing $I$.
:::

::: {.solution}
We prove
\[
\sqrt I=\bigcap_{\substack{\mathfrak p\in\Spec R\\ I\subseteq\mathfrak p}}\mathfrak p.
\]

If $x\in\sqrt I$, then $x^n\in I$ for some $n\ge1$. Every prime ideal $\mathfrak p\supseteq I$ contains $x^n$, hence contains $x$. Therefore
\[
\sqrt I\subseteq\bigcap_{\mathfrak p\supseteq I}\mathfrak p.
\]

Conversely, suppose $x\notin\sqrt I$. Then
\[
S=\{1,x,x^2,\dots\}
\]
is disjoint from $I$. Consider the ideals $J\supseteq I$ with $J\cap S=\varnothing$. By Zorn's lemma there is a maximal such ideal $\mathfrak p$.

We claim $\mathfrak p$ is prime. If $a,b\notin\mathfrak p$, maximality gives
\[
x^m\in\mathfrak p+(a),\qquad x^n\in\mathfrak p+(b)
\]
for some $m,n$. Hence
\[
x^{m+n}\in\mathfrak p+(ab).
\]
If $ab\in\mathfrak p$, then $x^{m+n}\in\mathfrak p$, contradicting $\mathfrak p\cap S=\varnothing$. Thus $ab\notin\mathfrak p$, so $\mathfrak p$ is prime.

By construction $I\subseteq\mathfrak p$ and $x\notin\mathfrak p$. Hence $x$ is not in the intersection of all primes containing $I$. This proves the reverse inclusion.
:::
