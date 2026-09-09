---
schema: qual/card@1
id: P-ALGS23C
kind: problem
title: "Injectivity detected by localization at maximal ideals"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
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

::: problem
Suppose $A$ is a unital commutative ring, $M$ and $N$ are $A$-modules, and $f: M \to N$ is an $A$-module homomorphism.
For every maximal ideal $\mathfrak{m}$ of $A$, let $M_\mathfrak{m}$ and $N_\mathfrak{m}$ be the localizations of $M$ and $N$ at $\mathfrak{m}$, respectively.
Recall that $$f_\mathfrak{m}: M_\mathfrak{m} \to N_\mathfrak{m}, \quad f_\mathfrak{m}\!\left(\frac{x}{s}\right) := \frac{f(x)}{s}$$ is an $A_\mathfrak{m}$-module homomorphism.
Prove that if $f_\mathfrak{m}$ is injective for all maximal ideals $\mathfrak{m}$, then $f$ is injective.

:::

::: {.solution}
<1>1. Let \(K=\ker f\). It suffices to show \(K=0\).
::: {.proof}
By definition, \(f\) is injective exactly when its kernel is zero.
:::

<1>2. Suppose for contradiction that \(0\ne x\in K\), and let
\[
I=\operatorname{Ann}_A(x)=\{a\in A:ax=0\}.
\]
Then \(I\) is a proper ideal of \(A\).
::: {.proof}
If \(I=A\), then \(1\in I\), so \(x=1x=0\), contrary to the choice of \(x\).
:::

<1>3. Choose a maximal ideal \(\mathfrak m\supseteq I\). Then \(x/1\ne0\) in \(M_{\mathfrak m}\).
::: {.proof}
If \(x/1=0\) in \(M_{\mathfrak m}\), then by the localization relation there exists \(s\in A\setminus\mathfrak m\) such that \(sx=0\). Hence \(s\in I\subseteq\mathfrak m\), contradicting \(s\notin\mathfrak m\).
:::

<1>4. On the other hand, \(f_{\mathfrak m}(x/1)=0\).
::: {.proof}
Since \(x\in\ker f\), one has \(f(x)=0\). Therefore
\[
f_{\mathfrak m}(x/1)=f(x)/1=0.
\]
:::

<1>5. This contradicts the injectivity of \(f_{\mathfrak m}\). Hence \(K=0\), so \(f\) is injective.
::: {.proof}
By <1>3 the element \(x/1\) is nonzero, while <1>4 shows that it lies in the kernel of the injective map \(f_{\mathfrak m}\).
:::
:::
