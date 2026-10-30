---
schema: qual/card@1
id: P-UCLARA12S-02
kind: problem
title: Borel measurability under continuous maps and products
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Borel Measures
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

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
\mathcal F
\coloneqq
\{E\subset Y:f^{-1}(E)\in\mathcal B(X)\}.
$$
Then $\mathcal F$ is a $\sigma$-algebra on $Y$.


::: pf-proof

Since
$$
f^{-1}(Y)=X,
$$
one has $Y\in\mathcal F$.

If $E\in\mathcal F$, then
$$
f^{-1}(Y\setminus E)
=
X\setminus f^{-1}(E)
\in
\mathcal B(X),
$$
so $Y\setminus E\in\mathcal F$.

If $E_n\in\mathcal F$, then
$$
f^{-1}\left(\bigcup_{n=1}^\infty E_n\right)
=
\bigcup_{n=1}^\infty f^{-1}(E_n)
\in
\mathcal B(X).
$$
Thus $\mathcal F$ is closed under countable unions.

:::

:::

::: {.pf-step #s1-2}

Every open subset of $Y$ belongs to $\mathcal F$.


::: pf-proof

If $U\subset Y$ is open, continuity of $f$ gives
$$
f^{-1}(U)
$$
open in $X$. Hence
$$
f^{-1}(U)\in\mathcal B(X),
$$
so $U\in\mathcal F$.

:::

:::

::: {.pf-step #s1-3}

If $E\in\mathcal B(Y)$, then
$$
\boxed{f^{-1}(E)\in\mathcal B(X)}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, $\mathcal F$ is a $\sigma$-algebra containing every open subset of $Y$. Therefore
$$
\mathcal B(Y)\subset\mathcal F.
$$
The definition of $\mathcal F$ gives the claim.

:::

:::

::: {.pf-step #s1-4}

The coordinate projections
$$
\pi_X:X\times Y\to X,
\qquad
\pi_Y:X\times Y\to Y
$$
are continuous.


::: pf-proof

This is part of the definition of the product topology: the product topology is the coarsest topology on $X\times Y$ for which both coordinate projections are continuous.

:::

:::

::: {.pf-step #s1-5}

If
$$
A\in\mathcal B(X),
\qquad
E\in\mathcal B(Y),
$$
then
$$
\pi_X^{-1}(A),
\pi_Y^{-1}(E)
\in
\mathcal B(X\times Y).
$$


::: pf-proof

Apply part (a), proved in step [](#s1-3){.pf-ref}, to the continuous maps $\pi_X$ and $\pi_Y$ from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
A\times E
\in
\mathcal B(X\times Y)
}.
$$


::: pf-proof

By elementary set theory,
$$
A\times E
=
\pi_X^{-1}(A)
\cap
\pi_Y^{-1}(E).
$$
Both inverse images are Borel by step [](#s1-5){.pf-ref}, and Borel sets are closed under finite intersections.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
