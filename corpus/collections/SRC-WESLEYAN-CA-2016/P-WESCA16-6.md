---
schema: qual/card@1
id: P-WESCA16-6
kind: problem
title: 'Automorphisms of the punctured disk'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Determine the conformal automorphism group of
\[
\DD^*=\{z:0<|z|<1\},
\]
and prove your claim.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $f:\DD^*\to\DD^*$ be a conformal automorphism. Then
$f$ extends holomorphically across $0$ to a map
\[
F:\DD\to\DD.
\]


::: pf-proof

The function $f$ is bounded by $1$ on a punctured neighborhood of $0$, so
the removable singularity theorem gives a holomorphic extension $F$ to
$\DD$. The extension satisfies $|F(0)|\le1$. If $|F(0)|=1$, then the
maximum modulus principle would force $F$ to be constant, contradicting that
$f$ is bijective. Hence $|F(0)|<1$, so $F(\DD)\subseteq\DD$.

:::

:::

::: {.pf-step #s1-2}

The inverse $f^{-1}$ extends to a holomorphic map
\[
G:\DD\to\DD,
\]
and $F$ and $G$ are inverse automorphisms of $\DD$.


::: pf-proof

Apply step [](#s1-1){.pf-ref} to $f^{-1}$ to obtain $G$. On $\DD^*$,
\[
G(F(z))=z.
\]
Both sides are holomorphic on $\DD$, so the identity theorem gives
\[
G\circ F=\operatorname{id}_{\DD}.
\]
Similarly,
\[
F\circ G=\operatorname{id}_{\DD}.
\]
Thus $F$ is a conformal automorphism of the full unit disk, with inverse $G$.

:::

:::

::: {.pf-step #s1-3}

The disk automorphism $F$ fixes $0$.


::: pf-proof

By hypothesis,
\[
F(\DD^*)=f(\DD^*)=\DD^*.
\]
By step [](#s1-2){.pf-ref}, $F$ is a bijection
\[
F:\DD\to\DD.
\]
Therefore the unique point in the image contributed by the omitted domain
point $0$ is the unique point omitted from $F(\DD^*)$. Since
\[
\DD\setminus\DD^*=\{0\},
\]
one must have
\[
F(0)=0.
\]

:::

:::

::: {.pf-step #s1-4}

There is $\lambda\in\CC$ with $|\lambda|=1$ such that
\[
F(z)=\lambda z
\qquad(z\in\DD).
\]


::: pf-proof

By step [](#s1-3){.pf-ref}, $F:\DD\to\DD$ is holomorphic and fixes $0$.
Schwarz's lemma gives
\[
|F(z)|\le|z|.
\]
Its inverse $G$ also fixes $0$, so Schwarz's lemma applied to $G$ gives
\[
|G(w)|\le|w|.
\]
Taking $w=F(z)$ yields
\[
|z|=|G(F(z))|\le|F(z)|.
\]
Hence
\[
|F(z)|=|z|
\]
for every $z$. Equality in Schwarz's lemma at any nonzero point implies that
$F$ is a rotation:
\[
F(z)=\lambda z,
\qquad
|\lambda|=1.
\]

:::

:::

::: {.pf-step #s1-5}

Consequently
\[
\boxed{
\operatorname{Aut}(\DD^*)
=\{z\mapsto\lambda z:|\lambda|=1\}
\cong S^1 }.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} shows that every conformal automorphism has this form. Conversely,
for every $|\lambda|=1$, the map
\[
z\longmapsto\lambda z
\]
is a conformal bijection of $\DD^*$ with inverse
$z\mapsto\overline\lambda z$. Composition corresponds to multiplication in
$S^1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} determines the automorphism group.

:::

:::

:::
