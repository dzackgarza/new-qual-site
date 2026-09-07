---
schema: qual/card@1
id: P-ALGF21C
kind: problem
title: $\sqrt[3]{2}$ not in a cyclotomic field $\mathbb{Q}(\zeta_n)$
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

::: problem
Let $\zeta \in \mathbb{C}$ be a primitive $n$th root of unity for some integer $n \geq 2$.
Prove that $\sqrt[3]{2} \notin \mathbb{Q}(\zeta)$.
*(Use the Fundamental Theorem of Galois Theory).*
:::

::: {.solution}
Set
\[
L=\mathbb Q(\zeta).
\]

<1>1. The extension $L/\mathbb Q$ is finite abelian Galois.
::: {.proof}
The field $L$ is the splitting field over $\mathbb Q$ of the $n$th cyclotomic polynomial, so $L/\mathbb Q$ is finite Galois.
Moreover,
\[
\operatorname{Gal}(L/\mathbb Q)
\hookrightarrow
(\mathbb Z/n\mathbb Z)^\times,
\]
indeed every automorphism is determined by
\[
\zeta\longmapsto\zeta^a
\]
for some $a$ prime to $n$.
Hence $\operatorname{Gal}(L/\mathbb Q)$ is abelian.
:::

<1>2. Every intermediate field
\[
\mathbb Q\subseteq E\subseteq L
\]
is Galois over $\mathbb Q$.
::: {.proof}
By the fundamental theorem of Galois theory,
\[
E=L^H
\]
for the subgroup
\[
H=\operatorname{Gal}(L/E)
\le\operatorname{Gal}(L/\mathbb Q).
\]
By <1>1, the ambient Galois group is abelian, so every subgroup is normal.
The Galois correspondence therefore implies that $E/\mathbb Q$ is Galois.
:::

<1>3. The extension
\[
\mathbb Q(\sqrt[3]{2})/\mathbb Q
\]
is not Galois.
::: {.proof}
The polynomial
\[
x^3-2
\]
is irreducible over $\mathbb Q$ by Eisenstein's criterion at $2$, so it is the minimal polynomial of $\sqrt[3]{2}$.
Its three roots are
\[
\sqrt[3]{2},
\qquad
\omega\sqrt[3]{2},
\qquad
\omega^2\sqrt[3]{2},
\]
where $\omega$ is a primitive cube root of unity.
The field $\mathbb Q(\sqrt[3]{2})$ is contained in $\mathbb R$, whereas the latter two roots are nonreal.
Thus the minimal polynomial does not split over $\mathbb Q(\sqrt[3]{2})$, so this extension is not normal and hence is not Galois.
:::

<1>4. One has
\[
\sqrt[3]{2}\notin\mathbb Q(\zeta).
\]
::: {.proof}
Suppose instead that
\[
\sqrt[3]{2}\in L.
\]
Then
\[
\mathbb Q
\subseteq
\mathbb Q(\sqrt[3]{2})
\subseteq
L.
\]
By <1>2, the intermediate extension $\mathbb Q(\sqrt[3]{2})/\mathbb Q$ would be Galois.
This contradicts <1>3.
Therefore
\[
\sqrt[3]{2}\notin\mathbb Q(\zeta).
\]
:::
:::
