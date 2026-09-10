---
schema: qual/card@1
id: P-NHWAK
kind: problem
title: Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Ideals
  - Maximal Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
(1) What is the Jacobson radical $J(R)$ of a ring $R$? State its equivalent characterizations.
(2) If $R$ is a finitely generated commutative algebra over a field $k$, what can you say about $J(R)$ (Jacobson rings and Hilbert's Nullstellensatz)?
:::

::: solution
For a commutative ring $R$ with $1$, the Jacobson radical is
\[
J(R)=\bigcap_{\mathfrak m\in\operatorname{MaxSpec}R}\mathfrak m.
\]
Equivalently,
\[
x\in J(R)\quad\Longleftrightarrow\quad 1-rx\in R^\times\text{ for every }r\in R.
\]
Also $\sqrt{(0)}\subseteq J(R)$ because every maximal ideal is prime.

If $R$ is a finitely generated commutative algebra over a field $k$, then $R$ is a Jacobson ring. Equivalently, for every prime ideal $\mathfrak p$,
\[
\mathfrak p=\bigcap_{\substack{\mathfrak m\supseteq\mathfrak p\\ \mathfrak m\text{ maximal}}}\mathfrak m.
\]
This is a standard consequence of Hilbert's Nullstellensatz (the weak Nullstellensatz itself says that maximal ideals of a finite-type $k$-algebra have residue fields algebraic, hence finite, over $k$).

Taking $\mathfrak p=(0)$ after passing to $R/\sqrt{0}$, or intersecting over all primes, gives
\[
J(R)=\bigcap_{\mathfrak m}\mathfrak m
=\bigcap_{\mathfrak p}\mathfrak p
=\sqrt{(0)}.
\]
Hence a reduced finite-type $k$-algebra has $J(R)=0$.

If moreover $R$ is finite-dimensional over $k$, then $R$ is Artinian, $J(R)$ is nilpotent, and $R/J(R)$ is a finite product of finite field extensions of $k$.
:::
