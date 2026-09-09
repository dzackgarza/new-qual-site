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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
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
<1>1. Put
\[
G=\operatorname{Gal}(E/F),\qquad H=\operatorname{Gal}(E/K).
\]
Then for every \(\sigma\in G\),
\[
\sigma H\sigma^{-1}=\operatorname{Gal}(E/\sigma(K)).
\]
::: {.proof}
An element \(\tau\in G\) lies in \(\sigma H\sigma^{-1}\) exactly when
\(\sigma^{-1}\tau\sigma\) fixes \(K\) pointwise. This is equivalent to \(\tau\) fixing
\(\sigma(K)\) pointwise, which is precisely
\(\tau\in\operatorname{Gal}(E/\sigma(K))\).
:::

<1>2. Suppose first that \(K/F\) is normal. Then \(H\trianglelefteq G\).
::: {.proof}
Fix \(\sigma\in G\). The restriction \(\sigma|_K:K\to E\) is an \(F\)-embedding.
Because \(K/F\) is finite and normal, every \(F\)-embedding of \(K\) into an algebraic
closure has image \(K\). Hence \(\sigma(K)=K\). By <1>1,
\[
\sigma H\sigma^{-1}
=\operatorname{Gal}(E/\sigma(K))
=\operatorname{Gal}(E/K)
=H.
\]
Since this holds for every \(\sigma\in G\), the subgroup \(H\) is normal in \(G\).
:::

<1>3. Conversely, suppose \(H\trianglelefteq G\). Then \(\sigma(K)=K\) for every
\(\sigma\in G\).
::: {.proof}
By the fundamental theorem of Galois theory, \(K=E^H\). For \(\sigma\in G\), one has
\[
\sigma(K)=\sigma(E^H)=E^{\sigma H\sigma^{-1}}.
\]
Since \(H\trianglelefteq G\), \(\sigma H\sigma^{-1}=H\), and therefore
\[
\sigma(K)=E^H=K.
\]
:::

<1>4. Under the hypothesis of <1>3, the extension \(K/F\) is normal.
::: {.proof}
Let \(\iota:K\hookrightarrow\overline F\) be any \(F\)-embedding into an algebraic closure.
Because \(E/K\) is algebraic, the embedding-extension theorem extends \(\iota\) to an
\(F\)-embedding
\[
\widetilde\iota:E\hookrightarrow\overline F.
\]
The extension \(E/F\) is finite Galois, hence normal, so every \(F\)-embedding of \(E\)
into \(\overline F\) has image \(E\). Thus \(\widetilde\iota\) is an element of
\(G=\operatorname{Gal}(E/F)\). By <1>3,
\[
\iota(K)=\widetilde\iota(K)=K.
\]
Therefore every \(F\)-embedding of \(K\) into \(\overline F\) preserves \(K\), which is
the normality criterion for the finite extension \(K/F\).
:::

<1>5. Hence
\[
K/F\text{ is normal}
\quad\Longleftrightarrow\quad
\operatorname{Gal}(E/K)\trianglelefteq\operatorname{Gal}(E/F).
\]
::: {.proof}
Combine <1>2 and <1>4.
:::
:::
