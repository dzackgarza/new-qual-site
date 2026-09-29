---
schema: qual/card@1
id: P-ALGF11A
kind: problem
title: Simple group of order $60$ with a subgroup of order $12$ is $A_5$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2011; the statement and warning agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the faithful coset action and sign argument identifying the image with A_5.
---

::: {.problem}
Consider a simple group $G$ with $60$ elements.
Show that if $G$ has a subgroup $H$ of order $12$ then $G \cong A_5$.

(Any simple group of order $60$ is isomorphic to $A_5$, but obviously you cannot use this fact, unless you prove it.)
:::


::: {.solution}
Let \(G\) act by left multiplication on the set of left cosets \(G/H\).
Since
\[
[G:H]=\frac{60}{12}=5,
\]
this action gives a homomorphism
\[
\rho:G\longrightarrow S_5.
\]

::: pf

::: {.pf-step #rho-nontrivial}
The homomorphism \(\rho\) is nontrivial.

::: pf-proof
If \(\rho\) were trivial, every \(g\in G\) would fix the coset \(H\).
Thus
\[
gH=H
\]
for every \(g\in G\), which implies \(g\in H\) for every \(g\).
Hence \(G=H\), contradicting \(|G|=60\) and \(|H|=12\).
Therefore \(\rho\) is nontrivial.
:::

:::

::: {.pf-step #rho-injective}
The homomorphism \(\rho\) is injective.

::: pf-proof
The kernel
\[
\ker\rho
\]
is a normal subgroup of the simple group \(G\).
Hence
\[
\ker\rho\in\{1,G\}.
\]
By step [](#rho-nontrivial){.pf-ref}, \(\rho\) is nontrivial, so \(\ker\rho\neq G\).
Therefore
\[
\ker\rho=1,
\]
and \(\rho\) is injective.
:::

:::

::: {.pf-step #image-in-a5}
The image \(\rho(G)\) is contained in \(A_5\).

::: pf-proof
Consider the sign homomorphism restricted to the image:
\[
\operatorname{sgn}|_{\rho(G)}:\rho(G)\longrightarrow\{\pm1\}.
\]
Because \(\rho:G\to\rho(G)\) is an isomorphism by step [](#rho-injective){.pf-ref}, the group \(\rho(G)\) is simple.
If the restricted sign map were nontrivial, its kernel would be a normal subgroup of index \(2\) in \(\rho(G)\), hence a nontrivial proper normal subgroup.
This contradicts simplicity.
Thus the restricted sign map is trivial, so every element of \(\rho(G)\) is even and
\[
\rho(G)\subseteq A_5.
\]
:::

:::

::: pf-step
Hence \(G\cong A_5\).

::: pf-proof
By injectivity,
\[
|\rho(G)|=|G|=60.
\]
Also
\[
|A_5|=\frac{5!}{2}=60.
\]
By step [](#image-in-a5){.pf-ref}, \(\rho(G)\subseteq A_5\), and the two finite groups have the same order.
Therefore
\[
\rho(G)=A_5.
\]
Since \(\rho\) is injective,
\[
G\cong A_5.
\]
:::

:::

:::
:::
