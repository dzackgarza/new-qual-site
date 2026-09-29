---
schema: qual/card@1
id: P-CIEHS
kind: problem
title: Holomorphic self-maps of the disk with a zero of order $k$ at $0$ and $|f|\to
  1$ at the boundary
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satsifies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

::: {.solution}
**Goal:** Suppose $f: \DD \to \DD$ is analytic, has a single zero of order $k$ at $z = 0$, and satisfies $\lim_{|z| \to 1}|f(z)| = 1$.
Give, with proof, a formula for $f(z)$.

::: pf

::: {.pf-step #finitely-many-zeros}
$f$ has only finitely many zeros in $\DD$.

::: pf-proof
by the hypothesis, there is $r < 1$ with $|f(z)| > \tfrac12$ for $r < |z| < 1$; hence all zeros lie in the compact set $\{|z| \le r\}$ and, being isolated (if $f \not\equiv 0$; $f \equiv 0$ is excluded since $|f| \to 1$), are finite.
Let $a_1, \dots, a_m$ be the zeros other than $0$ (with multiplicity).
:::

:::

::: {.pf-step #blaschke-product}
Form the finite Blaschke product $B(z) = z^k \prod_{j=1}^m \frac{z - a_j}{1 - \bar a_j z}$.

::: pf-proof
$|a_j| < 1$, so each factor is a disk automorphism; $B$ is holomorphic on $\DD$ with zeros exactly those of $f$ (same multiplicities) and $|B(z)| = 1$ for $|z| = 1$ (each factor has modulus 1 on the circle).
:::

:::

::: {.pf-step #h-holomorphic-zero-free}
$h := f/B$ is holomorphic and zero-free on $\DD$.

::: pf-proof
$B$ and $f$ have identical zeros with identical multiplicities (steps [](#finitely-many-zeros){.pf-ref} and [](#blaschke-product){.pf-ref}), so the singularities of $f/B$ at the zeros are removable and $h \ne 0$.
:::

:::

::: {.pf-step #h-modulus-limit-one}
$|h(z)| \to 1$ as $|z| \to 1$.

::: pf-proof
$|h(z)| = |f(z)|/|B(z)|$; by step [](#blaschke-product){.pf-ref}, $|B(z)| \to 1$ as $|z| \to 1$, and by hypothesis $|f(z)| \to 1$.
:::

:::

::: {.pf-step #h-modulus-identically-one}
$|h| \equiv 1$ on $\DD$.

::: pf-proof

::: {.pf-step #log-h-harmonic-boundary-zero}
$\log|h|$ is harmonic on $\DD$ with boundary limit $0$.

::: pf-proof
$h$ is zero-free (step [](#h-holomorphic-zero-free){.pf-ref}), so $\log|h| = \Re\log h$ is harmonic; step [](#h-modulus-limit-one){.pf-ref} gives the boundary limit.
:::

:::

::: {.pf-step #log-h-zero}
$\log|h| \equiv 0$.

::: pf-proof
a harmonic function on the disk whose radial limit is $0$ everywhere is identically $0$ (Poisson integral of its boundary values; or maximum principle on $|z| \le r$ with $r \nearrow 1$).
:::

:::

::: pf-step
$h \equiv \alpha$ with $|\alpha| = 1$.

::: pf-proof
$|h| \equiv 1$ by steps [](#log-h-harmonic-boundary-zero){.pf-ref} and [](#log-h-zero){.pf-ref}; a holomorphic function of constant modulus 1 is constant with modulus 1.
:::

:::

:::

:::

::: {.pf-step #final-formula}
$f(z) = \alpha z^k \prod_{j=1}^m \frac{z - a_j}{1 - \bar a_j z}$ with $|\alpha| = 1$ and $0 < |a_j| < 1$; conversely every such function satisfies the hypotheses.

::: pf-proof
$f = Bh$ with $h = \alpha$ by steps [](#h-holomorphic-zero-free){.pf-ref}, [](#h-modulus-limit-one){.pf-ref} and [](#h-modulus-identically-one){.pf-ref}. Conversely, for any such product, $f: \DD \to \DD$, $f$ has a single zero of order $k$ at $0$ (and the other listed zeros), and $|f(z)| \to 1$ as $|z| \to 1$.
:::

:::

::: pf-qed
Steps [](#finitely-many-zeros){.pf-ref}, [](#blaschke-product){.pf-ref}, [](#h-holomorphic-zero-free){.pf-ref}, [](#h-modulus-limit-one){.pf-ref}, [](#h-modulus-identically-one){.pf-ref} and [](#final-formula){.pf-ref} give the formula with proof.
:::

:::
