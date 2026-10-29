---
schema: qual/card@1
id: P-ALGS21G
kind: problem
title: "Z[x]/(2x-1) is isomorphic to the localization of Z at powers of 2"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Let $R = \ZZ[x]/(2x-1)$.
Let $S = \{1, 2, 4, 8, \ldots\} \subseteq \ZZ$.

(a) Show that $R$ is isomorphic as a ring to the localization $S^{-1}\ZZ$.

(b) Is $R$ a free $\ZZ$-module?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

In \(R=\ZZ[x]/(2x-1)\), the class \(\bar x\) satisfies
\[
2\bar x=1.
\]
Hence every element of \(S=\{2^k:k\ge0\}\) maps to a unit in \(R\).

::: pf-proof

The defining relation is \(2x-1=0\), so \(2\bar x=1\). Thus \(2\) is invertible with inverse \(\bar x\), and every power \(2^k\) is invertible as well.

:::

:::

::: pf-step

By the universal property of localization, there is a unique ring homomorphism
\[
\phi:S^{-1}\ZZ\longrightarrow R
\]
extending the natural map \(\ZZ\to R\). Explicitly,
\[
\phi\!\left(\frac{a}{2^k}\right)=a\bar x^{\,k}.
\]

::: pf-proof

The universal property applies because every element of \(S\) maps to a unit by step [](#s1){.pf-ref}. Since \(2^{-1}\) must map to \(\bar x\), the displayed formula follows.

:::

:::

::: pf-step

Evaluation at \(x=1/2\) gives a ring homomorphism
\[
\psi:R\longrightarrow S^{-1}\ZZ,
\qquad \psi(\bar x)=\frac12.
\]

::: pf-proof

The evaluation map \(\ZZ[x]\to S^{-1}\ZZ\), \(x\mapsto1/2\), sends \(2x-1\) to zero. Hence it factors through the quotient \(R\).

:::

:::

::: {.pf-step #s4}

The maps \(\phi\) and \(\psi\) are inverse isomorphisms. Therefore
\[
R\cong S^{-1}\ZZ=\ZZ[1/2].
\]

::: pf-proof

Both composites fix every integer. Moreover,
\[
(\phi\circ\psi)(\bar x)=\phi(1/2)=\bar x,
\]
so \(\phi\circ\psi\) fixes the ring generators of \(R\). Likewise \(\psi\circ\phi\) fixes \(1/2\), hence every \(a/2^k\). Thus both composites are identities.

:::

:::

::: pf-step

The \(\ZZ\)-module \(R\) is not free.

::: pf-proof

Via step [](#s4){.pf-ref}, suppose \(\ZZ[1/2]\) were a free \(\ZZ\)-module with basis \(B\). Tensoring with \(\QQ\) gives
\[
\QQ\otimes_{\ZZ}\ZZ[1/2]\cong\QQ,
\]
while a free module on \(B\) would tensor to the \(\QQ\)-vector space with basis \(B\). Hence \(|B|=1\), so \(\ZZ[1/2]\) would be free of rank one, isomorphic to \(\ZZ\).

But multiplication by \(2\) is surjective on \(\ZZ[1/2]\), since \(a/2^k=2(a/2^{k+1})\), whereas multiplication by \(2\) is not surjective on any nonzero rank-one free \(\ZZ\)-module. This contradiction shows \(R\) is not free over \(\ZZ\).

:::

:::

:::

:::
