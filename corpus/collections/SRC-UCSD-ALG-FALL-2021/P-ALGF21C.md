---
schema: qual/card@1
id: P-ALGF21C
kind: problem
title: $\sqrt[3]{2}$ not in a cyclotomic field $\QQ(\zeta_n)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2021 source; the cyclotomic-field statement and Galois-theory hint agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: "Rewrote the proof around the precise Galois-correspondence obstruction: every intermediate field of a finite abelian Galois extension is Galois, whereas Q(cuberoot 2)/Q is not normal."
---

::: {.problem}
Let $\zeta \in \CC$ be a primitive $n$th root of unity for some integer $n \geq 2$.
Prove that $\sqrt[3]{2} \notin \QQ(\zeta)$.
*(Use the Fundamental Theorem of Galois Theory).*
:::

::: {.solution}
Set
$$
L=\QQ(\zeta).
$$

::: pf

::: {.pf-step #s1}

The extension $L/\QQ$ is finite abelian Galois.

::: pf-proof

The field $L$ is the splitting field over $\QQ$ of the $n$th cyclotomic polynomial, so $L/\QQ$ is finite Galois.
Moreover,
$$
\operatorname{Gal}(L/\QQ)
\hookrightarrow
(\ZZ/n\ZZ)^\times,
$$
indeed every automorphism is determined by
$$
\zeta\longmapsto\zeta^a
$$
for some $a$ prime to $n$.
Hence $\operatorname{Gal}(L/\QQ)$ is abelian.

:::

:::

::: {.pf-step #s2}

Every intermediate field
$$
\QQ\subseteq E\subseteq L
$$
is Galois over $\QQ$.

::: pf-proof

By the fundamental theorem of Galois theory,
$$
E=L^H
$$
for the subgroup
$$
H=\operatorname{Gal}(L/E)
\le\operatorname{Gal}(L/\QQ).
$$
By step [](#s1){.pf-ref}, the ambient Galois group is abelian, so every subgroup is normal.
The Galois correspondence therefore implies that $E/\QQ$ is Galois.

:::

:::

::: {.pf-step #s3}

The extension
$$
\QQ(\sqrt[3]{2})/\QQ
$$
is not Galois.

::: pf-proof

The polynomial
$$
x^3-2
$$
is irreducible over $\QQ$ by Eisenstein's criterion at $2$, so it is the minimal polynomial of $\sqrt[3]{2}$.
Its three roots are
$$
\sqrt[3]{2},
\qquad
\omega\sqrt[3]{2},
\qquad
\omega^2\sqrt[3]{2},
$$
where $\omega$ is a primitive cube root of unity.
The field $\QQ(\sqrt[3]{2})$ is contained in $\RR$, whereas the latter two roots are nonreal.
Thus the minimal polynomial does not split over $\QQ(\sqrt[3]{2})$, so this extension is not normal and hence is not Galois.

:::

:::

::: pf-step

One has
$$
\sqrt[3]{2}\notin\QQ(\zeta).
$$

::: pf-proof

Suppose instead that
$$
\sqrt[3]{2}\in L.
$$
Then
$$
\QQ
\subseteq
\QQ(\sqrt[3]{2})
\subseteq
L.
$$
By step [](#s2){.pf-ref}, the intermediate extension $\QQ(\sqrt[3]{2})/\QQ$ would be Galois.
This contradicts step [](#s3){.pf-ref}.
Therefore
$$
\sqrt[3]{2}\notin\QQ(\zeta).
$$

:::

:::

:::

:::
