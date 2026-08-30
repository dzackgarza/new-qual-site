---
schema: qual/card@1
id: P-PF5MC
kind: problem
title: Galois group of $x^5-2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Calculate the Galois group of $x^5 - 2$.
:::

::: solution
**Goal:** Identify $\operatorname{Gal}(x^5-2)$.

<1>1. Irreducibility:
    *Proof:*  
    $x^5-2$ is Eisenstein at $p=2$, so it is irreducible over $\mathbb Q$.
    Therefore $[\mathbb Q(\alpha):\mathbb Q]=5$ for $\alpha=\sqrt[5]{2}$.

<1>2. Split field:
    *Proof:*  
    The roots are $\zeta_5^j\alpha$ for $j=0,\dots,4$, where $\zeta_5=e^{2\pi i/5}$.
    Hence the splitting field is
    $$K=\mathbb Q(\alpha,\zeta_5).$$

<1>3. Automorphisms:
    *Proof:*  
    For $a\in\{1,2,3,4\}$ define $\tau_a\in\operatorname{Gal}(K/\mathbb Q)$ by
    \[
    \tau_a(\alpha)=\alpha,\qquad \tau_a(\zeta_5)=\zeta_5^a.
    \]
    These give a subgroup isomorphic to $(\mathbb Z/5\mathbb Z)^\times\cong C_4$.

    For $b\in\{0,1,2,3,4\}$ define $\sigma_b$ by
    \[
    \sigma_b(\alpha)=\zeta_5^b\alpha,\qquad \sigma_b(\zeta_5)=\zeta_5.
    \]
    Then $\sigma_b(\alpha)$ is a root, so $\sigma_b\in\operatorname{Gal}(K/\mathbb Q)$ and
    $\{\sigma_b\}\cong C_5$.

<1>4. Group structure and size:
    *Proof:*  
    $\sigma_b$ acts trivially on $\zeta_5$, so $\sigma_b$ form the kernel of the
    restriction map $\operatorname{Gal}(K/\mathbb Q)\to\operatorname{Gal}(\mathbb Q(\zeta_5)/\mathbb Q)\cong C_4$.
    The kernel is $C_5$, and the quotient is $C_4$, so
    \[
    \operatorname{Gal}(K/\mathbb Q)\cong C_5\rtimes C_4.
    \]
    Concretely this is the affine linear group $x\mapsto ax+b$ on $\mathbb F_5$, of order $20$.

<1>5. Conclusion:
    *Proof:*  
    The Galois group of $x^5-2$ is the order-$20$ Frobenius group $C_5\rtimes C_4$.
:::
