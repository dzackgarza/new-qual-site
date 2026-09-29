---
schema: qual/card@1
id: P-ALGF21D
kind: problem
title: Finite extension of a perfect field is perfect below
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2021 source; the finite-extension and perfectness hypotheses agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the characteristic-p argument by comparing [K:F^p] through F and through K^p, using K=K^p and [K^p:F^p]=[K:F].
---

::: {.problem}
Let $F \subseteq K$ be an extension of fields with $[K : F] < \infty$.
Show that if $K$ is a perfect field, then so is $F$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\operatorname{char}F=0$, then $F$ is perfect.

::: pf-proof

Every field of characteristic zero is perfect, so there is nothing to prove in this case.

:::

:::

::: pf-step

Assume $\operatorname{char}F=p>0$.
Then
\[
F^p\subseteq F\subseteq K,
\]
where
\[
F^p=\{x^p:x\in F\}.
\]

::: pf-proof

The Frobenius map is a field homomorphism in characteristic $p$, so its image $F^p$ is a subfield of $F$.

:::

:::

::: {.pf-step #s3}

The Frobenius isomorphisms induce
\[
[K^p:F^p]=[K:F].
\]

::: pf-proof

The Frobenius maps
\[
F\longrightarrow F^p,
\qquad
x\longmapsto x^p,
\]
and
\[
K\longrightarrow K^p,
\qquad
x\longmapsto x^p,
\]
are field isomorphisms onto their images, and the second carries the subfield $F$ onto $F^p$.
Thus the extensions $K/F$ and $K^p/F^p$ are isomorphic as field extensions, so their degrees are equal.

:::

:::

::: {.pf-step #s4}

Since $K$ is perfect,
\[
K^p=K.
\]
Consequently
\[
[K:F^p]=[K:F].
\]

::: pf-proof

For a field of characteristic $p>0$, perfectness is equivalent to surjectivity of Frobenius.
Hence $K=K^p$.
Using step [](#s3){.pf-ref},
\[
[K:F^p]
=[K^p:F^p]
=[K:F].
\]

:::

:::

::: {.pf-step #s5}

One has
\[
F=F^p.
\]

::: pf-proof

By the tower law applied to
\[
F^p\subseteq F\subseteq K,
\]
we have
\[
[K:F^p]=[K:F][F:F^p].
\]
By step [](#s4){.pf-ref}, the left side equals $[K:F]$.
Since $[K:F]$ is a positive finite integer, cancellation gives
\[
[F:F^p]=1.
\]
Therefore $F=F^p$.

:::

:::

::: pf-step

The field $F$ is perfect.

::: pf-proof

If $\operatorname{char}F=0$, this is step [](#s1){.pf-ref}.
If $\operatorname{char}F=p>0$, step [](#s5){.pf-ref} shows that Frobenius on $F$ is surjective, which is equivalent to perfectness.

:::

:::

:::

:::
