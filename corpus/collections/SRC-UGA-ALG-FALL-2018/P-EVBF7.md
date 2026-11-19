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
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 15
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    trailing pf-qed, whose only content was a reference back to steps s1, s2 and s3, was removed; the
    last step of s3 is now the QED step, as STYLE-08 asks. The mathematics is unchanged and was re-read:
    x^3-2 and its splitting field QQ(cuberoot 2, omega) for (a), the divisor and splitting-field
    arguments for (b), and x^4-2 over QQ(sqrt 2) inside QQ(fourth root 2) for (c). Checked against the
    statement on the card, from the UGA Fall 2018 algebra qualifying exam; no published solution is
    cited, so the argument and both counterexamples are the card's own. Nothing in the statement was
    changed.
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
The subclaims exhibit the example, check that the top extension is Galois, and check that the intermediate one is not.

::: pf-step

Counterexample: Let $F = \QQ$, $K = \QQ(\sqrt[3]{2})$, and $L = \QQ(\sqrt[3]{2}, \omega)$, where $\omega = e^{2\pi i / 3}$.

::: pf-proof
This names the fields: $L$ is generated over $F$ by the real cube root of $2$ together with a primitive cube root of unity, and $F\subseteq K\subseteq L$ because $\sqrt[3]{2}\in L$.
:::

:::

::: pf-step

$L/F$ is Galois: The polynomial $f(x) = x^3 - 2 \in \QQ[x]$ is irreducible by Eisenstein's criterion at $p = 2$. Its roots in $\CC$ are $\sqrt[3]{2}, \sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2$. The field $L = \QQ(\sqrt[3]{2}, \omega)$ is the splitting field of $f(x)$ over $\QQ$. Since $\operatorname{char}(\QQ) = 0$, $f(x)$ is separable, so $L/\QQ$ is a Galois extension.

::: pf-proof
The three displayed numbers are exactly the roots of $x^3-2$, and $L$ is generated over $\QQ$ by them, so $L$ is their splitting field; a splitting field of a separable polynomial is normal, and the polynomial is separable because the characteristic is $0$. Normal together with separable is Galois.
:::

:::

::: pf-step

$K/F$ is not Galois: The intermediate field $K = \QQ(\sqrt[3]{2}) \subset \RR$ contains one root of the irreducible polynomial $x^3 - 2$, but contains neither of the non-real roots $\sqrt[3]{2}\omega, \sqrt[3]{2}\omega^2 \notin \RR$.

::: pf-proof
In a normal extension of $\QQ$ an irreducible polynomial with one root in the field has all of its roots there, since the conjugates are the images of that root under the $\QQ$-embeddings. Here $K\subseteq\RR$ while the other two roots are non-real, so $K/\QQ$ is not normal.
:::

:::

::: pf-step

Thus $K/\QQ$ is not a normal extension, hence is not Galois.

::: pf-proof
A Galois extension is by definition normal and separable, so the failure of normality just established excludes it.
:::

:::

::: pf-step

Therefore, $L/F$ Galois does not imply $K/F$ Galois.

::: pf-proof
The four preceding subclaims exhibit $F\subseteq K\subseteq L$ with $L/F$ Galois and $K/F$ not, which is precisely a counterexample to the assertion.
:::

:::

:::

:::

::: {.pf-step #s2}

Assertion (b) is true: if $L/F$ is Galois, then $L/K$ is Galois.

::: pf-proof
The two middle subclaims verify separability and normality of $L/K$, which together with finiteness are the definition of Galois.

::: pf-step

Since $L/F$ is a finite Galois extension, it is both normal and separable.

::: pf-proof
A finite Galois extension is by definition a finite, normal and separable extension.
:::

:::

::: pf-step

$L/K$ is separable: Let $\alpha \in L$. Since $L/F$ is separable, the minimal polynomial $m_{\alpha, F}(x) \in F[x]$ has distinct roots in an algebraic closure $\overline{F}$. Since $F \subseteq K$, the minimal polynomial $m_{\alpha, K}(x) \in K[x]$ divides $m_{\alpha, F}(x)$ in $K[x]$. Any divisor of a separable polynomial is separable, so $m_{\alpha, K}(x)$ has distinct roots. Thus every element of $L$ is separable over $K$.

::: pf-proof
The minimal polynomial over $K$ divides that over $F$ because $F\subseteq K$ and $m_{\alpha,F}(\alpha)=0$ makes $m_{\alpha,F}$ a polynomial over $K$ vanishing at $\alpha$. A divisor of a polynomial with distinct roots again has distinct roots, since each of its roots is a root of the larger polynomial.
:::

:::

::: pf-step

$L/K$ is normal: Since $L/F$ is a finite normal extension, $L$ is the splitting field of some polynomial $g(x) \in F[x]$ over $F$. Since $F \subseteq K$, $g(x) \in K[x]$, so $L$ is also generated over $K$ by the roots of $g(x)$. Thus $L$ is the splitting field of $g(x)$ over $K$, which implies $L/K$ is normal.

::: pf-proof
$L$ is generated over $K$ by the roots of $g$, which lie in $L$, because it is already generated over the smaller field $F$ by those roots; being a splitting field over $K$ is the definition of normality for the extension $L/K$.
:::

:::

::: pf-step

Since $L/K$ is finite, normal, and separable, $L/K$ is a Galois extension.

::: pf-proof
Finiteness is inherited from $L/F$, and the other two properties are the two preceding subclaims; normal together with separable is Galois.
:::

:::

:::

:::

::: {.pf-step #s3}

Assertion (c) is false: two successive Galois extensions need not have Galois composite extension.

::: pf-proof
The subclaims exhibit the example, check that each of the two steps is Galois and that the composite is not.

::: pf-step

Counterexample: Let $F = \QQ$, $K = \QQ(\sqrt{2})$, and $L = \QQ(\sqrt[4]{2})$.

::: pf-proof
These fields satisfy $\QQ\subseteq\QQ(\sqrt2)\subseteq\QQ(\sqrt[4]2)$, because $\sqrt2=(\sqrt[4]2)^2$ lies in $L$.
:::

:::

::: pf-step

$K/F$ is Galois: $K = \QQ(\sqrt{2})$ is an extension of degree 2 over $\QQ$, which is the splitting field of $x^2 - 2$ over $\QQ$, hence Galois.

::: pf-proof
$x^2-2$ is separable in characteristic $0$, and its two roots $\pm\sqrt2$ both lie in $K$, which is generated by them; so $K$ is the splitting field and the extension is normal and separable.
:::

:::

::: pf-step

$L/K$ is Galois: $L = K(\sqrt[4]{2})$ is obtained by adjoining a root of $x^2 - \sqrt{2} \in K[x]$. Since $\sqrt[4]{2} \notin K$ (as $[\QQ(\sqrt[4]{2}) : \QQ] = 4$ and $[K : \QQ] = 2$), $[L : K] = 2$. Every degree 2 extension in characteristic zero is Galois, so $L/K$ is Galois.

::: pf-proof
$\sqrt[4]2$ is a root of $x^2-\sqrt2\in K[x]$, and it does not lie in $K$, since otherwise $L=K$ and $[L:\QQ]=[K:\QQ]$, contrary to $4\neq2$. A separable quadratic extension is the splitting field of the minimal polynomial of either root, hence normal, and separability holds in characteristic $0$.
:::

:::

::: pf-step

$L/F$ is not Galois: The polynomial $x^4 - 2 \in \QQ[x]$ is irreducible over $\QQ$ by Eisenstein at $p = 2$. The field $L = \QQ(\sqrt[4]{2}) \subset \RR$ contains the real root $\sqrt[4]{2}$, but does not contain the complex roots $\pm i \sqrt[4]{2} \notin \RR$.

::: pf-proof
Eisenstein's criterion at $2$ applies to $x^4-2$; $L\subseteq\RR$ because $\sqrt[4]2$ is real, while the two roots $\pm i\sqrt[4]2$ are non-real. A normal extension containing one root of an irreducible polynomial contains all of its roots, so $L/\QQ$ is not normal.
:::

:::

::: pf-step

Thus $L/\QQ$ is not normal, and therefore is not Galois.

::: pf-proof
Galois requires normality, which the preceding subclaim denies.
:::

:::

::: pf-step

Hence, transitivity of Galois extensions fails in general.

::: pf-proof
The example has $K/F$ Galois and $L/K$ Galois but $L/F$ not Galois, which is exactly a failure of transitivity.
:::

:::

:::

:::

:::

:::
