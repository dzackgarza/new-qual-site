---
schema: qual/card@1
id: P-EVBF7
kind: problem
title: Galois-ness of $K/F$ and of $L/K$ when $L/F$ is Galois, and of $L/F$ when $K/F$
  and $L/K$ are Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $F \subseteq K \subseteq L$ be finite-degree field extensions. For each of the following assertions, prove the statement or provide a counterexample with full justification:

(a) If $L/F$ is Galois, then $K/F$ is Galois.

(b) If $L/F$ is Galois, then $L/K$ is Galois.

(c) If $K/F$ and $L/K$ are both Galois, then $L/F$ is Galois.
:::

::: {.solution}
**Goal:** Adjudicate the three transitivity/sub-extension assertions for Galois extensions.

::: pf

::: pf-step
Part (a): False.

::: pf-proof

::: pf-step
Counterexample: Let $F = \mathbb{Q}$, $K = \mathbb{Q}(\sqrt[3]{2})$, and $L = \mathbb{Q}(\sqrt[3]{2}, \omega)$, where $\omega = e^{2\pi i / 3}$.
:::

::: pf-step
$L/F$ is Galois: The polynomial $f(x) = x^3 - 2 \in \mathbb{Q}[x]$ is irreducible by Eisenstein's criterion at $p = 2$. Its roots in $\mathbb{C}$ are $\sqrt[3]{2}, \sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2$. The field $L = \mathbb{Q}(\sqrt[3]{2}, \omega)$ is the splitting field of $f(x)$ over $\mathbb{Q}$. Since $\operatorname{char}(\mathbb{Q}) = 0$, $f(x)$ is separable, so $L/\mathbb{Q}$ is a Galois extension.
:::

::: pf-step
$K/F$ is not Galois: The intermediate field $K = \mathbb{Q}(\sqrt[3]{2}) \subset \mathbb{R}$ contains one root of the irreducible polynomial $x^3 - 2$, but contains neither of the non-real roots $\sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2 \notin \mathbb{R}$.
:::

::: pf-step
Thus $K/\mathbb{Q}$ is not a normal extension, hence is not Galois.
:::

::: pf-step
Therefore, $L/F$ Galois does not imply $K/F$ Galois.
:::

:::

:::

::: pf-step
Part (b): True.

::: pf-proof

::: pf-step
Since $L/F$ is a finite Galois extension, it is both normal and separable.
:::

::: pf-step
$L/K$ is separable: Let $\alpha \in L$. Since $L/F$ is separable, the minimal polynomial $m_{\alpha, F}(x) \in F[x]$ has distinct roots in an algebraic closure $\overline{F}$. Since $F \subseteq K$, the minimal polynomial $m_{\alpha, K}(x) \in K[x]$ divides $m_{\alpha, F}(x)$ in $K[x]$. Any divisor of a separable polynomial is separable, so $m_{\alpha, K}(x)$ has distinct roots. Thus every element of $L$ is separable over $K$.
:::

::: pf-step
$L/K$ is normal: Since $L/F$ is a finite normal extension, $L$ is the splitting field of some polynomial $g(x) \in F[x]$ over $F$. Since $F \subseteq K$, $g(x) \in K[x]$, so $L$ is also generated over $K$ by the roots of $g(x)$. Thus $L$ is the splitting field of $g(x)$ over $K$, which implies $L/K$ is normal.
:::

::: pf-step
Since $L/K$ is finite, normal, and separable, $L/K$ is a Galois extension.
:::

:::

:::

::: pf-step
Part (c): False.

::: pf-proof

::: pf-step
Counterexample: Let $F = \mathbb{Q}$, $K = \mathbb{Q}(\sqrt{2})$, and $L = \mathbb{Q}(\sqrt[4]{2})$.
:::

::: pf-step
$K/F$ is Galois: $K = \mathbb{Q}(\sqrt{2})$ is an extension of degree 2 over $\mathbb{Q}$, which is the splitting field of $x^2 - 2$ over $\mathbb{Q}$, hence Galois.
:::

::: pf-step
$L/K$ is Galois: $L = K(\sqrt[4]{2})$ is obtained by adjoining a root of $x^2 - \sqrt{2} \in K[x]$. Since $\sqrt[4]{2} \notin K$ (as $[\mathbb{Q}(\sqrt[4]{2}) : \mathbb{Q}] = 4$ and $[K : \mathbb{Q}] = 2$), $[L : K] = 2$. Every degree 2 extension in characteristic zero is Galois, so $L/K$ is Galois.
:::

::: pf-step
$L/F$ is not Galois: The polynomial $x^4 - 2 \in \mathbb{Q}[x]$ is irreducible over $\mathbb{Q}$ by Eisenstein at $p = 2$. The field $L = \mathbb{Q}(\sqrt[4]{2}) \subset \mathbb{R}$ contains the real root $\sqrt[4]{2}$, but does not contain the complex roots $\pm i \sqrt[4]{2} \notin \mathbb{R}$.
:::

::: pf-step
Thus $L/\mathbb{Q}$ is not normal, and therefore is not Galois.
:::

::: pf-step
Hence, transitivity of Galois extensions fails in general.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
(a) is false, (b) is true, and (c) is false.
:::

:::

:::
:::
