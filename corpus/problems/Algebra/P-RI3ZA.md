---
schema: qual/card@1
id: P-RI3ZA
kind: problem
title: Normality of field extensions is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: The compilation card embedded the wrong counterexample. The intended non-transitivity claim is corroborated by source-backed UGA Fall 2018 and UCSD Fall 2011 cards in the corpus.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Give an example of a tower of field extensions
\[
K\subseteq L\subseteq M
\]
such that \(L/K\) and \(M/L\) are normal, but \(M/K\) is not normal.
:::

::: {.solution}
Take
\[
K=\mathbb Q,
\qquad
L=\mathbb Q(\sqrt2),
\qquad
M=\mathbb Q(\sqrt[4]{2}).
\]
Put \(\alpha=\sqrt[4]{2}\), so \(\alpha^2=\sqrt2\).

<1>1. The extension \(L/K\) is normal.
::: {.proof}
The field \(L=\mathbb Q(\sqrt2)\) is the splitting field over \(\mathbb Q\) of
\[
x^2-2=(x-\sqrt2)(x+\sqrt2).
\]
Hence \(L/K\) is normal.
:::

<1>2. The extension \(M/L\) is normal.
::: {.proof}
Over \(L\), the element \(\alpha\) is a root of
\[
x^2-\sqrt2.
\]
This polynomial splits in \(M\) as
\[
(x-\alpha)(x+\alpha).
\]
Moreover \(\alpha\notin L\), since \([\mathbb Q(\alpha):\mathbb Q]=4\) by Eisenstein's criterion applied to \(x^4-2\), whereas \([L:\mathbb Q]=2\). Thus \(M=L(\alpha)\) is the splitting field of \(x^2-\sqrt2\) over \(L\), so \(M/L\) is normal.
:::

<1>3. The extension \(M/K\) is not normal.
::: {.proof}
The polynomial
\[
x^4-2
\]
is irreducible over \(\mathbb Q\) by Eisenstein's criterion at \(2\), so it is the minimal polynomial of \(\alpha\) over \(K\). Its roots are
\[
\alpha,-\alpha,i\alpha,-i\alpha.
\]
But \(M=\mathbb Q(\alpha)\subseteq\mathbb R\), so \(i\alpha\notin M\). Hence the minimal polynomial of \(\alpha\) over \(K\) does not split in \(M\), and therefore \(M/K\) is not normal.
:::

<1>4. Thus normality of field extensions is not transitive.
::: {.proof}
Combine <1>1--<1>3.
:::
:::
