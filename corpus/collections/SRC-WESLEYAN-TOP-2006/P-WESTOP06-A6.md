---
schema: qual/card@1
id: P-WESTOP06-A6
kind: problem
title: Maximal ideals and zero sets in rings of continuous functions
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The retained extraction prints I(S)={f in C(X) | Z(f) contains X}, although the following sentences use S and its closure. It also literally asks, for compact X, that every ideal I equal I(S) for some closed S. Both points are source-sensitive and are not silently repaired.
---

::: {.problem}
Recall the definition of a commutative ring with identity and of an ideal.

1. Use Zorn's Lemma to prove that every proper ideal is contained in a maximal ideal.
2. For a space $X$, let $C(X)$ be the ring of continuous real-valued functions and put
   \[
   Z(f)=\{x\in X:f(x)=0\}.
   \]
   The retained extraction defines
   \[
   I(S)=\{f\in C(X):Z(f)\supseteq X\},
   \]
   while immediately asserting $I(\overline S)=I(S)$ and $S_1\subseteq S_2\Rightarrow I(S_1)\supseteq I(S_2)$. Prove the requested ideal assertions, retaining this notation gap as source-sensitive.
3. The retained source next asks: for compact $X$, prove the converse that if $I$ is an ideal in $C(X)$, then $I=I(S)$ for some closed $S$. Record and address the statement as printed.
4. Determine the maximal ideals in $C(X)$ when $X$ is compact.
:::
