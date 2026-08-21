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
solved: true
---

::: problem
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satsifies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $f: \DD \to \DD$ is analytic, has a single zero of order $k$ at $z = 0$, and satisfies $\lim_{|z| \to 1}|f(z)| = 1$.
Give, with proof, a formula for $f(z)$.

<1>1. $f$ has only finitely many zeros in $\DD$.
Proof: by the hypothesis, there is $r < 1$ with $|f(z)| > \tfrac12$ for $r < |z| < 1$; hence all zeros lie in the compact set $\{|z| \le r\}$ and, being isolated (if $f \not\equiv 0$; $f \equiv 0$ is excluded since $|f| \to 1$), are finite.
Let $a_1, \dots, a_m$ be the zeros other than $0$ (with multiplicity).

<1>2. Form the finite Blaschke product $B(z) = z^k \prod_{j=1}^m \frac{z - a_j}{1 - \bar a_j z}$.
Proof: $|a_j| < 1$, so each factor is a disk automorphism; $B$ is holomorphic on $\DD$ with zeros exactly those of $f$ (same multiplicities) and $|B(z)| = 1$ for $|z| = 1$ (each factor has modulus 1 on the circle).

<1>3. $h := f/B$ is holomorphic and zero-free on $\DD$.
Proof: $B$ and $f$ have identical zeros with identical multiplicities (<1>1, <1>2), so the singularities of $f/B$ at the zeros are removable and $h \ne 0$.

<1>4. $|h(z)| \to 1$ as $|z| \to 1$.
Proof: $|h(z)| = |f(z)|/|B(z)|$; by <1>2, $|B(z)| \to 1$ as $|z| \to 1$, and by hypothesis $|f(z)| \to 1$.

<1>5. $|h| \equiv 1$ on $\DD$.
<2>1. $\log|h|$ is harmonic on $\DD$ with boundary limit $0$.
Proof: $h$ is zero-free (<1>3), so $\log|h| = \Re\log h$ is harmonic; <1>4 gives the boundary limit.
<2>2. $\log|h| \equiv 0$.
Proof: a harmonic function on the disk whose radial limit is $0$ everywhere is identically $0$ (Poisson integral of its boundary values; or maximum principle on $|z| \le r$ with $r \nearrow 1$). <2>3. $h \equiv \alpha$ with $|\alpha| = 1$.
Proof: $|h| \equiv 1$ by <2>1–<2>2; a holomorphic function of constant modulus 1 is constant with modulus 1.

<1>6. $f(z) = \alpha z^k \prod_{j=1}^m \frac{z - a_j}{1 - \bar a_j z}$ with $|\alpha| = 1$ and $0 < |a_j| < 1$; conversely every such function satisfies the hypotheses.
Proof: $f = Bh$ with $h = \alpha$ by <1>3–<1>5. Conversely, for any such product, $f: \DD \to \DD$, $f$ has a single zero of order $k$ at $0$ (and the other listed zeros), and $|f(z)| \to 1$ as $|z| \to 1$.

<1>7. Q.E.D. Proof: <1>1–<1>6 give the formula with proof.
:::
