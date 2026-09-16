---
schema: qual/card@1
id: P-C4RYM
kind: problem
title: Burnside's lemma
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Prove Burnside's theorem.
:::

::: {.solution}
Let a finite group $G$ act on a finite set $X$, and let
\[
S=\{(g,x)\in G\times X:gx=x\}.
\]
Counting first by \(g\) gives
\[
|S|=\sum_{g\in G}|X^g|.
\]
Counting first by \(x\) gives
\[
|S|=\sum_{x\in X}|G_x|.
\]
By orbit-stabilizer,
\[
|G_x|=\frac{|G|}{|Gx|}.
\]
For each orbit \(O\), summing this quantity over \(x\in O\) contributes
\[
|O|\frac{|G|}{|O|}=|G|.
\]
Therefore
\[
\sum_{g\in G}|X^g|
=|G|\cdot |X/G|,
\]
and hence
\[
|X/G|=\frac1{|G|}\sum_{g\in G}|X^g|.
\]
This is Burnside's lemma.
:::
