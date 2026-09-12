---
schema: qual/card@1
id: P-ALGS12C
kind: problem
title: Surjective endomorphisms of Noetherian rings are injective
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Noetherian Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 3 of the official UCSD Spring 2012 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Used stabilization of kernels for the Noetherian case and the left-shift endomorphism of a countably generated polynomial ring for the counterexample.
---

::: problem
Let $R$ be a commutative ring.

(a) Suppose that $R$ is noetherian.
Prove that if $\phi \colon R \to R$ is a surjective ring homomorphism, then $\phi$ is injective.

(b) If $R$ is not noetherian, must a surjective ring homomorphism $\phi \colon R \to R$ be injective?
Prove or give a counterexample.
:::

::: {.solution}
<1>1. Suppose \(R\) is Noetherian and \(\phi:R\to R\) is surjective.
Then the ascending chain
\[
\ker\phi\subseteq\ker\phi^2\subseteq\ker\phi^3\subseteq\cdots
\]
stabilizes.
::: {.proof}
Each \(\ker\phi^n\) is an ideal of \(R\). Since \(R\) is Noetherian, every ascending chain of ideals stabilizes.
Thus there exists \(N\ge1\) such that
\[
\ker\phi^N=\ker\phi^{N+1}.
\]
:::

<1>2. Under the hypotheses of <1>1, \(\ker\phi=0\).
::: {.proof}
Let \(a\in\ker\phi\). Since \(\phi\) is surjective, so is \(\phi^N\). Hence there exists \(b\in R\) with
\[
\phi^N(b)=a.
\]
Then
\[
\phi^{N+1}(b)=\phi(a)=0,
\]
so \(b\in\ker\phi^{N+1}\). By stabilization,
\[
b\in\ker\phi^N.
\]
Therefore
\[
a=\phi^N(b)=0.
\]
Thus \(\ker\phi=0\).
:::

<1>3. Therefore every surjective endomorphism of a Noetherian commutative ring is injective.
::: {.proof}
A ring homomorphism is injective exactly when its kernel is zero, and <1>2 gives \(\ker\phi=0\).
:::

<1>4. The conclusion fails without the Noetherian hypothesis.
::: {.proof}
Let \(k\) be any field and set
\[
R=k[x_1,x_2,x_3,\ldots].
\]
This ring is not Noetherian, because the ideals
\[
(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots
\]
form a strictly increasing chain.

Define a \(k\)-algebra endomorphism \(\phi:R\to R\) by
\[
\phi(x_1)=0,
\qquad
\phi(x_{i+1})=x_i\quad(i\ge1).
\]
The map is surjective because every generator \(x_i\) lies in its image:
\[
x_i=\phi(x_{i+1}).
\]
But \(x_1\neq0\) and
\[
\phi(x_1)=0,
\]
so \(\phi\) is not injective.
Hence a surjective endomorphism of a non-Noetherian ring need not be injective.
:::
:::
