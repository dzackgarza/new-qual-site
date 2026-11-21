---
schema: qual/card@1
id: P-MNR6F
kind: problem
title: $f^{-1}(f(S))=S$ for all $S$ iff $f$ is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps; both implications are unchanged, and the
    converse is written as the elementwise argument at the singleton. Checked: the easy inclusion,
    the injective case, and the singleton argument. Not checked against a printed source: the UGA
    preliminary examinations are not retained in tmp/sources and the card records no page.
---

::: {.problem}
Let $f:X\to Y$ be a map of sets.
Give, with proof, necessary and sufficient conditions for
$$
f^{-1}(f(S))=S
$$
for every subset $S\subseteq X$.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $f:X\to Y$ is a map of sets and $S$ ranges over the subsets of $X$; the claim is that $f^{-1}(f(S))=S$ for every $S$ exactly when $f$ is injective.

::: pf

::: {.pf-step #incl}

$S\subseteq f^{-1}(f(S))$ for every $S\subseteq X$.

::: pf-proof

If $s\in S$ then $f(s)\in f(S)$, which is exactly the condition $s\in f^{-1}(f(S))$.

:::

:::

::: {.pf-step #suff}

If $f$ is injective then $f^{-1}(f(S))=S$ for every $S$.

::: pf-proof

Let $x\in f^{-1}(f(S))$. Then $f(x)=f(s)$ for some $s\in S$, and injectivity gives $x=s\in S$; with step [](#incl){.pf-ref} the two sets are equal.

:::

:::

::: {.pf-step #nec}

If $f^{-1}(f(S))=S$ for every $S$ then $f$ is injective.

::: pf-proof

Suppose $f(a)=f(b)$ with $a,b\in X$. Then $b\in f^{-1}(f(\theset{a}))$, since $f(b)=f(a)\in\theset{f(a)}$, and $f^{-1}(f(\theset{a}))=\theset{a}$ by hypothesis, so $b=a$.

:::

:::

::: {.pf-step #done}

$f$ is injective if and only if $f^{-1}(f(S))=S$ for every $S\subseteq X$.

::: pf-proof

Steps [](#suff){.pf-ref} and [](#nec){.pf-ref}.

:::

:::

:::

:::
