---
schema: qual/card@1
id: P-XPGT3
kind: problem
title: "Let $R$ be a ring with $1$ and let $M$ be a left \\(R\\dash\\)module."
classification:
  areas:
  - algebra
  topics:
  - modules
  - ideals
  - nakayamas-lemma
relations: []
review: draft
---
Let $R$ be a ring with $1$ and let $M$ be a left \(R\dash\)module.
If $I$ is a left ideal of $R$, define 
\[
IM \da \ts{ \sum_{i=1}^{N < \infty} a_i m_i \st a_i \in I, m_i \in M, n\in \NN}
,\]
i.e. the set of finite sums of of elements of the form $am$ where \( a\in I, m\in M \).

a. Prove that $IM \leq M$ is a submodule.

b. Let $M, N$ be left \(R\dash\)modules, $I$ a nilpotent left ideal of $R$, and $f: M\to N$ an \(R\dash\)module morphism.
Prove that if the induced morphism \( \bar{f}: M/IM \to N/IN \) is surjective, then $f$ is surjective.
