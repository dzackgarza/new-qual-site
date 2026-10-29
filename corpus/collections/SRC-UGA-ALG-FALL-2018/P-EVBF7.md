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

::: pf

::: {.pf-step #s1}

Assertion (a) is false: an intermediate extension of a finite Galois extension need not be Galois over the base.

::: pf-proof

::: pf-step

Counterexample: Let $F = \QQ$, $K = \QQ(\sqrt[3]{2})$, and $L = \QQ(\sqrt[3]{2}, \omega)$, where $\omega = e^{2\pi i / 3}$.

:::

::: pf-step

$L/F$ is Galois: The polynomial $f(x) = x^3 - 2 \in \QQ[x]$ is irreducible by Eisenstein's criterion at $p = 2$. Its roots in $\CC$ are $\sqrt[3]{2}, \sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2$. The field $L = \QQ(\sqrt[3]{2}, \omega)$ is the splitting field of $f(x)$ over $\QQ$. Since $\operatorname{char}(\QQ) = 0$, $f(x)$ is separable, so $L/\QQ$ is a Galois extension.

:::

::: pf-step

$K/F$ is not Galois: The intermediate field $K = \QQ(\sqrt[3]{2}) \subset \RR$ contains one root of the irreducible polynomial $x^3 - 2$, but contains neither of the non-real roots $\sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2 \notin \RR$.

:::

::: pf-step

Thus $K/\QQ$ is not a normal extension, hence is not Galois.

:::

::: pf-step

Therefore, $L/F$ Galois does not imply $K/F$ Galois.

:::

:::

:::

::: {.pf-step #s2}

Assertion (b) is true: if $L/F$ is Galois, then $L/K$ is Galois.

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

::: {.pf-step #s3}

Assertion (c) is false: two successive Galois extensions need not have Galois composite extension.

::: pf-proof

::: pf-step

Counterexample: Let $F = \QQ$, $K = \QQ(\sqrt{2})$, and $L = \QQ(\sqrt[4]{2})$.

:::

::: pf-step

$K/F$ is Galois: $K = \QQ(\sqrt{2})$ is an extension of degree 2 over $\QQ$, which is the splitting field of $x^2 - 2$ over $\QQ$, hence Galois.

:::

::: pf-step

$L/K$ is Galois: $L = K(\sqrt[4]{2})$ is obtained by adjoining a root of $x^2 - \sqrt{2} \in K[x]$. Since $\sqrt[4]{2} \notin K$ (as $[\QQ(\sqrt[4]{2}) : \QQ] = 4$ and $[K : \QQ] = 2$), $[L : K] = 2$. Every degree 2 extension in characteristic zero is Galois, so $L/K$ is Galois.

:::

::: pf-step

$L/F$ is not Galois: The polynomial $x^4 - 2 \in \QQ[x]$ is irreducible over $\QQ$ by Eisenstein at $p = 2$. The field $L = \QQ(\sqrt[4]{2}) \subset \RR$ contains the real root $\sqrt[4]{2}$, but does not contain the complex roots $\pm i \sqrt[4]{2} \notin \RR$.

:::

::: pf-step

Thus $L/\QQ$ is not normal, and therefore is not Galois.

:::

::: pf-step

Hence, transitivity of Galois extensions fails in general.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} settle parts (a), (b), and (c), respectively.

:::

:::

:::
