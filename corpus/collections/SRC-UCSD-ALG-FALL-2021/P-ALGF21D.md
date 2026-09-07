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

::: problem
Let $F \subseteq K$ be an extension of fields with $[K : F] < \infty$.
Show that if $K$ is a perfect field, then so is $F$.
:::

::: {.solution}
<1>1. If $\operatorname{char}F=0$, then $F$ is perfect.
::: {.proof}
Every field of characteristic zero is perfect, so there is nothing to prove in this case.
:::

<1>2. Assume $\operatorname{char}F=p>0$.
Then
\[
F^p\subseteq F\subseteq K,
\]
where
\[
F^p=\{x^p:x\in F\}.
\]
::: {.proof}
The Frobenius map is a field homomorphism in characteristic $p$, so its image $F^p$ is a subfield of $F$.
:::

<1>3. The Frobenius isomorphisms induce
\[
[K^p:F^p]=[K:F].
\]
::: {.proof}
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

<1>4. Since $K$ is perfect,
\[
K^p=K.
\]
Consequently
\[
[K:F^p]=[K:F].
\]
::: {.proof}
For a field of characteristic $p>0$, perfectness is equivalent to surjectivity of Frobenius.
Hence $K=K^p$.
Using <1>3,
\[
[K:F^p]
=[K^p:F^p]
=[K:F].
\]
:::

<1>5. One has
\[
F=F^p.
\]
::: {.proof}
By the tower law applied to
\[
F^p\subseteq F\subseteq K,
\]
we have
\[
[K:F^p]=[K:F][F:F^p].
\]
By <1>4, the left side equals $[K:F]$.
Since $[K:F]$ is a positive finite integer, cancellation gives
\[
[F:F^p]=1.
\]
Therefore $F=F^p$.
:::

<1>6. The field $F$ is perfect.
::: {.proof}
If $\operatorname{char}F=0$, this is <1>1.
If $\operatorname{char}F=p>0$, <1>5 shows that Frobenius on $F$ is surjective, which is equivalent to perfectness.
:::
:::
