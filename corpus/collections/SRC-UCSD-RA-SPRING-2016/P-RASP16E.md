---
schema: qual/card@1
id: P-RASP16E
kind: problem
title: "An operator within norm 1 of a topological isomorphism is a topological isomorphism"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Neumann Series
  - Bounded Inverse Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $X$ be a Banach space and denote by $\mathcal{L}(X)$ the space of all linear and bounded operators from $X$ to $X$.
Let $T \in \mathcal{L}(X)$ be a topological isomorphism, i.e., $T : X \to X$ is linear, bijective, and both $T$ and $T^{-1}$ are continuous.
Let $S \in \mathcal{L}(X)$ be such that $\|(S - T)T^{-1}\| < 1$.
Prove that $S : X \to X$ is also a topological isomorphism.
:::


::: solution
<1>1. Reduce to a perturbation of the identity.
::: proof
Set
\[
A:=(S-T)T^{-1}\in\mathcal L(X).
\]
By hypothesis,
\[
\|A\|<1.
\]
Since
\[
S-T=AT,
\]
we have
\[
S=(I+A)T.
\]
Thus it is enough to show that \(I+A\) is a topological isomorphism.
:::

<1>2. Invert \(I+A\) by the Neumann series.
::: proof
Because \(\|A\|<1\), the series
\[
R:=\sum_{n=0}^\infty (-A)^n
\]
converges in the Banach algebra \(\mathcal L(X)\). For the partial sums,
\[
(I+A)\sum_{n=0}^N(-A)^n
=I+(-1)^N A^{N+1},
\]
and similarly on the other side. Since
\[
\|A^{N+1}\|\le\|A\|^{N+1}\to0,
\]
passing to the limit gives
\[
(I+A)R=R(I+A)=I.
\]
Hence \(I+A\) is bijective and its inverse \(R\) is bounded.
:::

<1>3. Conclude for \(S\).
::: proof
Both \(T\) and \(I+A\) are topological isomorphisms, so their product
\[
S=(I+A)T
\]
is also a topological isomorphism. Explicitly,
\[
S^{-1}=T^{-1}(I+A)^{-1}
=T^{-1}\sum_{n=0}^\infty(-A)^n,
\]
which is bounded. Therefore
\[
\boxed{S:X\to X\text{ is a topological isomorphism}.}
\]
:::
:::
