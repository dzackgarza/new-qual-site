---
schema: qual/card@1
id: P-CWRU6
kind: problem
title: $f(x)\ge\limsup_{y\to x}f(y)$ implies $f$ is Borel measurable
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UGA Spring 2014 real-analysis exam source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f: \RR \to \RR$ and suppose
$$
\forall x\in \RR,\quad f(x) \geq \limsup _{y \rightarrow x} f(y)
$$
Prove that $f$ is Borel measurable.
:::
::: solution
<1>1. Show that every strict sublevel set is open.
::: proof
Fix $a\in\mathbb R$ and suppose $f(x)<a$. By hypothesis,
\[
\limsup_{y\to x}f(y)\le f(x)<a.
\]
Hence there exists $\delta>0$ such that
\[
|y-x|<\delta\quad\Longrightarrow\quad f(y)<a.
\]
Otherwise one could find a sequence $y_n\to x$ with $f(y_n)\ge a$, forcing
\[
\limsup_{y\to x}f(y)\ge a.
\]
Thus
\[
\{f<a\}
\]
is open for every $a$.
:::

<1>2. Deduce Borel measurability.
::: proof
Since each set $\{f<a\}$ is open, each set
\[
\{f\ge a\}=\mathbb R\setminus\{f<a\}
\]
is closed. Therefore
\[
\{f>a\}
=\bigcup_{n=1}^\infty\{f\ge a+1/n\}
\]
is an $F_\sigma$ set, hence Borel, for every $a\in\mathbb R$.

The rays $(a,\infty)$ generate the Borel sigma-algebra of $\mathbb R$, so the measurability of every preimage
\[
f^{-1}((a,\infty))=\{f>a\}
\]
proves that $f$ is Borel measurable.
:::
:::
