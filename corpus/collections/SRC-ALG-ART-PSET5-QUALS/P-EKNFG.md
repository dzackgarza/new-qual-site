---
schema: qual/card@1
id: P-EKNFG
kind: problem
title: Normal intermediate extensions and normal subgroups of a Galois group
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}

Let $E/F$ be a finite Galois extension, and let $K$ be an intermediate field.
Prove that $K/F$ is normal if and only if $\operatorname{Gal}(E/K)$ is a normal subgroup of $\operatorname{Gal}(E/F)$.
:::


::: {.solution}
Let
\[
G=\operatorname{Gal}(E/F),\qquad H=\operatorname{Gal}(E/K).
\]

<1>1. For every \(\sigma\in G\),
\[
\sigma H\sigma^{-1}=\operatorname{Gal}(E/\sigma(K)).
\]
::: {.proof}
An element \(\tau\in G\) lies in \(\sigma H\sigma^{-1}\) exactly when \(\sigma^{-1}\tau\sigma\) fixes every element of \(K\). Equivalently, for every \(a\in K\),
\[
\tau(\sigma(a))=\sigma(a).
\]
Thus \(\tau\) fixes \(\sigma(K)\) pointwise, which is precisely the condition \(\tau\in\operatorname{Gal}(E/\sigma(K))\).
:::

<1>2. The subgroup \(H\) is normal in \(G\) if and only if \(\sigma(K)=K\) for every \(\sigma\in G\).
::: {.proof}
By <1>1,
\[
\sigma H\sigma^{-1}=H
\]
if and only if
\[
\operatorname{Gal}(E/\sigma(K))=\operatorname{Gal}(E/K).
\]
The Galois correspondence for the finite Galois extension \(E/F\) is injective on intermediate fields, so this equality of subgroups is equivalent to \(\sigma(K)=K\).
:::

<1>3. If \(K/F\) is normal, then \(H\trianglelefteq G\).
::: {.proof}
For \(\sigma\in G\), the restriction \(\sigma|_K:K\to E\) is an \(F\)-embedding. Since \(K/F\) is normal, every \(F\)-embedding of \(K\) into an algebraic closure has image \(K\). Hence \(\sigma(K)=K\). By <1>2, \(H\) is normal in \(G\).
:::

<1>4. If \(H\trianglelefteq G\), then \(K/F\) is normal.
::: {.proof}
By <1>2, \(\sigma(K)=K\) for every \(\sigma\in G\). Since \(E/F\) is finite Galois, \(K/F\) is finite and separable.

Let \(\iota:K\hookrightarrow\overline F\) be any \(F\)-embedding. Because \(E/F\) is finite separable, \(\iota\) extends to an \(F\)-embedding
\[
\widetilde\iota:E\hookrightarrow\overline F.
\]
Since \(E/F\) is normal, \(\widetilde\iota(E)=E\), so \(\widetilde\iota\in G\). Therefore
\[
\iota(K)=\widetilde\iota(K)=K.
\]
Thus every \(F\)-embedding of \(K\) into an algebraic closure has image \(K\), and since \(K/F\) is separable, \(K/F\) is normal.
:::

<1>5. Therefore
\[
K/F\text{ is normal}\iff \operatorname{Gal}(E/K)\trianglelefteq\operatorname{Gal}(E/F).
\]
::: {.proof}
Combine <1>3 and <1>4.
:::
:::
