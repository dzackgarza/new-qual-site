---
schema: qual/card@1
id: P-RAF22E
kind: problem
title: "Invertibility on Hilbert space is equivalent to T and T* both bounded below"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Bounded Operators
  - Adjoints
  - Closed Range
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $H$ be a Hilbert space, let $T : H \to H$ be a bounded linear operator, and let $T^* : H \to H$ denote the adjoint of $T$.
Recall that a linear map $S : H \to H$ is bounded below if there is a constant $c > 0$ such that $\|Sx\| \geq c\|x\|$ for all $x \in H$.

Prove that $T$ is invertible (with bounded inverse) if and only if both $T$ and $T^*$ are bounded below.
:::

::: solution
<1>1. Invertibility implies both operators are bounded below.
::: proof
Suppose $T$ is invertible with bounded inverse. Then for every $x\in H$,
\[
\|x\|=\|T^{-1}Tx\|\le \|T^{-1}\|\,\|Tx\|,
\]
so
\[
\|Tx\|\ge \|T^{-1}\|^{-1}\|x\|.
\]
Thus $T$ is bounded below.

Moreover $T^*$ is invertible and
\[
(T^*)^{-1}=(T^{-1})^*.
\]
Applying the same argument to $T^*$ shows that $T^*$ is bounded below.
:::

<1>2. A bounded-below operator is injective and has closed range.
::: proof
Assume now that
\[
\|Tx\|\ge c\|x\|
\]
for some $c>0$. Then $Tx=0$ implies $x=0$, so $T$ is injective.

Let $(Tx_n)$ converge in $H$. Then
\[
\|x_n-x_m\|\le c^{-1}\|Tx_n-Tx_m\|,
\]
so $(x_n)$ is Cauchy. Since $H$ is complete, $x_n\to x$ for some $x\in H$. Continuity of $T$ gives
\[
Tx_n\to Tx.
\]
Hence the limit belongs to $\operatorname{ran}T$, so $\operatorname{ran}T$ is closed.
:::

<1>3. The lower bound for $T^*$ forces the range of $T$ to be dense.
::: proof
If $T^*$ is bounded below, then $T^*$ is injective, hence
\[
\ker T^*=\{0\}.
\]
For every bounded operator on a Hilbert space,
\[
(\operatorname{ran}T)^\perp=\ker T^*.
\]
Therefore
\[
(\operatorname{ran}T)^\perp=\{0\},
\]
which implies
\[
\overline{\operatorname{ran}T}=H.
\]
By Step 2 the range is already closed, so
\[
\operatorname{ran}T=H.
\]
Thus $T$ is surjective as well as injective.
:::

<1>4. The inverse is bounded.
::: proof
Since $T$ is bijective, define $T^{-1}:H\to H$. If $y=Tx$, then
\[
\|T^{-1}y\|=\|x\|\le c^{-1}\|Tx\|=c^{-1}\|y\|.
\]
Hence
\[
\|T^{-1}\|\le c^{-1}.
\]
Therefore $T$ is invertible with bounded inverse.
:::
:::
