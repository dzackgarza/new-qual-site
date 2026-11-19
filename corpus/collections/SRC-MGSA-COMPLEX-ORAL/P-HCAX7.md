---
schema: qual/card@1
id: P-HCAX7
kind: problem
title: Complex tori and their automorphisms
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Tori
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct.
    Repair: the card's covolume sentence was garbled ('multiplication by a scales Euclidean
    covolume by |a|^2'), and a stray determinant expression has been removed in favour of the
    covolume statement alone. Added: the reason the difference F~(z+lambda) - F~(z) is
    continuous and into a discrete set, hence constant, and that the resulting homomorphism
    lambda -> phi(lambda) takes values in the lattice; the separate step that a covering-map
    lift is holomorphic; the two inclusions a Lambda <= Lambda and the reverse from the inverse
    map; the semidirect-product law (b,a)(b',a') = (b + ab', aa'); and the verification omega^2
    = omega - 1 that makes the sixth roots of unity act on Z + Z omega. Not claimed: a retained
    solution set; the collection's provenance is the oral examination compilation.
---

::: {.problem}
Define a complex torus and determine its group of holomorphic automorphisms.
:::

::: {.solution}
A complex torus is $T = \CC/\Lambda$ where $\Lambda = \ZZ\omega_{1} \oplus \ZZ\omega_{2}$ is a lattice, that is $\omega_{1}, \omega_{2}$ are linearly independent over $\RR$; $\pi\colon\CC \to T$ is the quotient map, a universal covering, and $U(\Lambda) \coloneqq \theset{a \in \CC^{*} \mid a\Lambda = \Lambda}$. The collection's `provenance` is the MGSA oral examination compilation, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #lift}
Every holomorphic $F\colon T \to T$ admits an entire lift $\widetilde{F}\colon\CC \to \CC$ with $\pi \circ \widetilde{F} = F \circ \pi$.

::: pf-proof
$\CC$ is simply connected and $\pi$ is a covering map, so the map $F \circ \pi\colon\CC \to T$ lifts through $\pi$ by the lifting criterion for covering spaces; the lift is holomorphic because $\pi$ is a local biholomorphism.

:::

:::

::: {.pf-step #translate}
There is a function $\varphi\colon\Lambda \to \CC$ with $\widetilde{F}(z + \lambda) = \widetilde{F}(z) + \varphi(\lambda)$ for all $z \in \CC$ and $\lambda \in \Lambda$, and $\varphi$ takes values in $\Lambda$.

::: pf-proof
For $\lambda \in \Lambda$ the map $z \mapsto \widetilde{F}(z + \lambda) - \widetilde{F}(z)$ is continuous, and it takes values in $\Lambda$ because $\pi$ of it equals $F\bigl(\pi(z)\bigr)$ in both terms. A continuous map into a discrete set is constant, so it equals $\varphi(\lambda)$, and the value lies in $\Lambda$.

:::

:::

::: {.pf-step #periodic}
$\widetilde{F}'$ is $\Lambda$-periodic, hence constant.

::: pf-proof
Differentiating the identity of step [](#translate){.pf-ref} in $z$ gives $\widetilde{F}'(z + \lambda) = \widetilde{F}'(z)$. So $\widetilde{F}'$ descends to a holomorphic function on $T$, which is compact; a holomorphic function on a compact complex manifold is bounded and attains its maximum, so it is constant by the maximum modulus principle (equivalently, Liouville's theorem applied to the lifted entire function).

:::

:::

::: {.pf-step #affine}
$\widetilde{F}(z) = az + b$ with $a \in \CC$ and $b = \widetilde{F}(0)$.

::: pf-proof
By step [](#periodic){.pf-ref} $\widetilde{F}' \equiv a$ for some constant $a$, and integrating gives $\widetilde{F}(z) = az + \widetilde{F}(0)$.

:::

:::

::: {.pf-step #descends}
Such an affine map descends to $T$ exactly when $a\Lambda \subseteq \Lambda$, and it is an automorphism of $T$ exactly when $a\Lambda = \Lambda$.

::: pf-proof
The map descends to a well-defined map of $T$ exactly when $\widetilde{F}(z + \lambda) - \widetilde{F}(z) = a\lambda$ lies in $\Lambda$ for every $\lambda \in \Lambda$, that is when $a\Lambda \subseteq \Lambda$. If $F$ is an automorphism, apply the same reasoning to $F^{-1}$, whose lift is the inverse of $\widetilde{F}$: it has the form $z \mapsto a'z + b'$ with $a' a = 1$ and $a'\Lambda \subseteq \Lambda$, so $\Lambda = a(a'\Lambda) \subseteq a\Lambda$, and with the inclusion $a\Lambda \subseteq \Lambda$ this gives equality. Conversely, if $a\Lambda = \Lambda$ then $a \ne 0$ and $z \mapsto a^{-1}(z - b)$ is a holomorphic inverse that descends as well.

:::

:::

::: {.pf-step #finite}
$U(\Lambda)$ is a finite subgroup of the unit circle, and $\Aut_{\mathrm{hol}}(T)$ is the semidirect product $T \rtimes U(\Lambda)$.

::: pf-proof
For $a \in U(\Lambda)$ the multiplication $z \mapsto az$ carries the lattice to itself, and multiplication by $a$ scales the covolume (the Euclidean area of a fundamental parallelogram) by the factor $\abs{a}^{2}$, so preserving $\Lambda$ forces $\abs{a} = 1$. Fix $0 \ne \lambda \in \Lambda$; then $a\lambda \in \Lambda$ and $\abs{a\lambda} = \abs{\lambda}$, so $a\lambda$ ranges over the finite set $\Lambda \cap \overline{D(0,\abs{\lambda})}$, and $a$ is determined by $a\lambda$ because $\lambda \ne 0$; so $U(\Lambda)$ is finite. Each affine map $z \mapsto az + b$ with $a \in U(\Lambda)$ descends by step [](#descends){.pf-ref}, and the resulting maps compose as $(b,a)(b',a') = (b + ab', aa')$, so the maps with $a = 1$ — the translations by $T$ — form a normal subgroup and the maps with $b = 0$ form $U(\Lambda)$ meeting it trivially; every automorphism is the product of the two parts. Hence $\Aut_{\mathrm{hol}}(T) \cong T \rtimes U(\Lambda)$.

:::

:::

::: {.pf-step #examples}
For $\Lambda = \ZZ + i\ZZ$ the group $U(\Lambda)$ is $\theset{\pm1, \pm i}$, and for $\Lambda = \ZZ + \ZZ e^{i\pi/3}$ it contains the sixth roots of unity.

::: pf-proof
For the square lattice, $\abs{a} = 1$ and $a\cdot 1, a\cdot i \in \Lambda$ force $a \in \theset{\pm1,\pm i}$, and those four work. For $\omega = e^{i\pi/3}$ one has $\omega^{2} = \omega - 1 \in \Lambda$, so multiplication by $\omega$ carries $1 \mapsto \omega$ and $\omega \mapsto \omega^{2} = \omega - 1$ into $\Lambda$; hence every sixth root of unity lies in $U(\Lambda)$.

:::

:::

::: pf-step
$\Aut_{\mathrm{hol}}(\CC/\Lambda) = \boxed{\theset{z \mapsto az + b \mid a \in U(\Lambda),\\ b \in \CC} \cong T \rtimes U(\Lambda)}$, a finite extension of the translations.

::: pf-proof
Steps [](#lift){.pf-ref} to [](#descends){.pf-ref} show that every holomorphic automorphism is induced by an affine map with $a\Lambda = \Lambda$, step [](#finite){.pf-ref} identifies the group structure and the finiteness of $U(\Lambda)$, and step [](#examples){.pf-ref} computes it in the two standard lattices.

:::

:::

:::
:::
