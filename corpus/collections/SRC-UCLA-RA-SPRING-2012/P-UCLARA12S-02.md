---
schema: qual/card@1
id: P-UCLARA12S-02
kind: problem
title: Borel measurability under continuous maps and products
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $X$ and $Y$ be topological spaces, and give $X\times Y$ the product topology.
Write $\mathcal B(X)$, $\mathcal B(Y)$, and $\mathcal B(X\times Y)$ for the corresponding Borel $\sigma$-algebras.

(a) If $f:X\to Y$ is continuous, prove that $E\in\mathcal B(Y)$ implies $f^{-1}(E)\in\mathcal B(X)$.

(b) If $A\in\mathcal B(X)$ and $E\in\mathcal B(Y)$, prove that $A\times E\in\mathcal B(X\times Y)$.
:::

::: pf

::: pf-step

Let
\[
\mathcal F
\coloneqq
\{E\subset Y:f^{-1}(E)\in\mathcal B(X)\}.
\]
Then $\mathcal F$ is a $\sigma$-algebra on $Y$.


::: pf-proof

Since
\[
f^{-1}(Y)=X,
\]
one has $Y\in\mathcal F$.

If $E\in\mathcal F$, then
\[
f^{-1}(Y\setminus E)
=
X\setminus f^{-1}(E)
\in
\mathcal B(X),
\]
so $Y\setminus E\in\mathcal F$.

If $E_n\in\mathcal F$, then
\[
f^{-1}\left(\bigcup_{n=1}^\infty E_n\right)
=
\bigcup_{n=1}^\infty f^{-1}(E_n)
\in
\mathcal B(X).
\]
Thus $\mathcal F$ is closed under countable unions.

:::

:::

::: pf-step

Every open subset of $Y$ belongs to $\mathcal F$.


::: pf-proof

If $U\subset Y$ is open, continuity of $f$ gives
\[
f^{-1}(U)
\]
open in $X$. Hence
\[
f^{-1}(U)\in\mathcal B(X),
\]
so $U\in\mathcal F$.

:::

:::

::: pf-step

If $E\in\mathcal B(Y)$, then
\[
\boxed{f^{-1}(E)\in\mathcal B(X)}.
\]


::: pf-proof

By steps <1>1 and <1>2, $\mathcal F$ is a $\sigma$-algebra containing every open subset of $Y$. Therefore
\[
\mathcal B(Y)\subset\mathcal F.
\]
The definition of $\mathcal F$ gives the claim.

:::

:::

::: pf-step

The coordinate projections
\[
\pi_X:X\times Y\to X,
\qquad
\pi_Y:X\times Y\to Y
\]
are continuous.


::: pf-proof

This is part of the definition of the product topology: the product topology is the coarsest topology on $X\times Y$ for which both coordinate projections are continuous.

:::

:::

::: pf-step

If
\[
A\in\mathcal B(X),
\qquad
E\in\mathcal B(Y),
\]
then
\[
\pi_X^{-1}(A),
\pi_Y^{-1}(E)
\in
\mathcal B(X\times Y).
\]


::: pf-proof

Apply part (a), proved in step <1>3, to the continuous maps $\pi_X$ and $\pi_Y$ from step <1>4.

:::

:::

::: pf-step

One has
\[
\boxed{
A\times E
\in
\mathcal B(X\times Y)
}.
\]


::: pf-proof

By elementary set theory,
\[
A\times E
=
\pi_X^{-1}(A)
\cap
\pi_Y^{-1}(E).
\]
Both inverse images are Borel by step <1>5, and Borel sets are closed under finite intersections.

:::

:::

::: pf-qed

Step <1>3 proves part (a), and step <1>6 proves part (b).

:::

:::
