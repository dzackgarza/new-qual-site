---
schema: qual/card@1
id: P-HCAX21
kind: problem
title: Uniqueness in the Riemann mapping theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: h = g o f^-1 is an
    automorphism of the disc fixing 0; Schwarz and Schwarz applied to h^-1 give |h(z)| = |z|,
    so h is a rotation; the chain rule gives g'(z_0) = e^{i theta} f'(z_0); and e^{i theta} =
    g'/f' is real, positive and of modulus 1, hence 1. The hypothesis "the same argument" was
    used in the prose as though it gave e^{i theta} = 1 directly; it is now stated in the
    precise form that the quotient g'(z_0)/f'(z_0) is real and positive, since arguments are
    multivalued. The statement is true as printed. The collection's provenance is the
    examination paper only, so no retained solution set covers the exercise and the argument is
    the card's own.
---

::: {.problem}
Prove the uniqueness statement in the Riemann mapping theorem after fixing the image of one point and the argument of the derivative there.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #setup}
Let $\Omega\subsetneq\CC$ be simply connected, $z_0\in\Omega$, and $f,g:\Omega\to\DD$ conformal isomorphisms with $f(z_0)=g(z_0)=0$ and with $g'(z_0)/f'(z_0)$ real and positive.

::: pf-proof
This is the hypothesis: equal images of $z_0$ and equal argument of the derivatives there. Conformality gives $f'(z_0)\ne0$ and $g'(z_0)\ne0$, so the quotient is defined; "the same argument" is precisely the statement that the quotient is real and positive.
:::

:::

::: {.pf-step #automorphism}
$h\coloneqq g\circ f^{-1}$ is an automorphism of $\DD$ with $h(0)=0$.

::: pf-proof
$f^{-1}:\DD\to\Omega$ is conformal because $f$ is, and $g$ is conformal, so the composite is a conformal map of $\DD$ onto $\DD$; it is a bijection with holomorphic inverse. Finally $h(0)=g(f^{-1}(0))=g(z_0)=0$.
:::

:::

::: {.pf-step #equality}
$\abs{h(z)}=\abs{z}$ for every $z\in\DD$.

::: pf-proof
Schwarz's lemma applied to $h$, which maps the disc into itself and fixes $0$, gives $\abs{h(z)}\le\abs{z}$. The same lemma applied to $h^{-1}$, which also maps the disc into itself and fixes $0$, gives $\abs{h^{-1}(w)}\le\abs{w}$, that is $\abs{z}\le\abs{h(z)}$ for $w=h(z)$. Hence equality holds.
:::

:::

::: {.pf-step #rotation}
There is $\theta\in\RR$ with $h(z)=e^{i\theta}z$.

::: pf-proof
The equality case of Schwarz's lemma says that a holomorphic self-map of the disc fixing $0$ and satisfying $\abs{h(z)}=\abs{z}$ is a rotation $h(z)=e^{i\theta}z$ for some real $\theta$.
:::

:::

::: {.pf-step #derivative}
$g'(z_0)=e^{i\theta}f'(z_0)$.

::: pf-proof
$g=h\circ f$ on $\Omega$, so the chain rule at $z_0$ gives $g'(z_0)=h'(f(z_0))f'(z_0)=h'(0)f'(z_0)$, and $h'(0)=e^{i\theta}$ by step [](#rotation){.pf-ref}.
:::

:::

::: {.pf-step}
$e^{i\theta}=1$, hence $g=f$.

::: pf-proof
By step [](#derivative){.pf-ref} the quotient $g'(z_0)/f'(z_0)$ equals $e^{i\theta}$, which is real and positive by step [](#setup){.pf-ref} and has modulus $1$; the only such number is $1$. So $h(z)=z$, and $g=h\circ f=f$ on $\Omega$. Hence a conformal isomorphism onto the disc is determined by the image of one point and the argument of the derivative there.
:::

:::

:::
:::
