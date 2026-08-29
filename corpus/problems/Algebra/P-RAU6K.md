---
schema: qual/card@1
id: P-RAU6K
kind: problem
title: A cubic with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Give an example of a cubic polynomial over $\mathbb{Q}$ with Galois group $S_3$, and prove that its Galois group is indeed $S_3$.
:::

::: solution
**Goal:** Exhibit a cubic polynomial $f(x) \in \mathbb{Q}[x]$ and prove $\operatorname{Gal}(f/\mathbb{Q}) \cong S_3$.

<1>1. Candidate Polynomial: $f(x) = x^3 - 2$:
    *Proof:*
    <2>1. Let $f(x) = x^3 - 2 \in \mathbb{Z}[x]$.

<1>2. Irreducibility over $\mathbb{Q}$:
    *Proof:*
    <2>1. By Eisenstein's Criterion at the prime $p = 2$:
        - $p = 2$ divides the constant term $-2$ and all intermediate coefficients $0$.
        - $p = 2$ does not divide the leading coefficient $1$.
        - $p^2 = 4$ does not divide the constant term $-2$.
    <2>2. Therefore, $f(x)$ is irreducible over $\mathbb{Q}$.
    <2>3. Since $\deg(f) = 3$ and $f$ is irreducible, the degree of any single root extension is $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$.
    <2>4. By the Orbit-Stabilizer Theorem / transitivity of the Galois group action on the 3 roots, $3$ divides $|\operatorname{Gal}(f/\mathbb{Q})|$.

<1>3. Discriminant and Splitting Field:
    *Proof:*
    <2>1. The roots of $f(x)$ in $\mathbb{C}$ are:
        $$\alpha_1 = \sqrt[3]{2}, \qquad \alpha_2 = \sqrt[3]{2} \, \omega, \qquad \alpha_3 = \sqrt[3]{2} \, \omega^2$$
        where $\omega = e^{2\pi i / 3} = \frac{-1 + i\sqrt{3}}{2}$ is a primitive cube root of unity.
    <2>2. The discriminant of a depressed cubic $x^3 + px + q$ is $\Delta = -4p^3 - 27q^2$.
        For $p = 0, q = -2$:
        $$\Delta(f) = -27(-2)^2 = -27(4) = -108 = -3 \cdot 36 = (6i\sqrt{3})^2.$$
    <2>3. Since $\Delta(f) = -108 < 0$, $\Delta(f)$ is not the square of any rational number in $\mathbb{Q}$.
    <2>4. For an irreducible cubic over $\mathbb{Q}$, $\operatorname{Gal}(f/\mathbb{Q}) \cong A_3 \cong \mathbb{Z}_3 \iff \Delta \in (\mathbb{Q}^\times)^2$.
    <2>5. Since $\Delta \notin (\mathbb{Q}^\times)^2$, $\operatorname{Gal}(f/\mathbb{Q})$ cannot be contained in $A_3$.
    <2>6. The only transitive subgroups of $S_3$ are $A_3$ and $S_3$.
    <2>7. Therefore:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong S_3.$$

<1>4. Splitting Field Degree:
    *Proof:*
    <2>1. The splitting field is $K = \mathbb{Q}(\sqrt[3]{2}, \omega) = \mathbb{Q}(\sqrt[3]{2}, i\sqrt{3})$.
    <2>2. $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$ and $[\mathbb{Q}(i\sqrt{3}) : \mathbb{Q}] = 2$.
    <2>3. Since $\gcd(2, 3) = 1$, $[K : \mathbb{Q}] = 3 \cdot 2 = 6 = |S_3|$.

<1>5. Conclusion:
    $f(x) = x^3 - 2$ is irreducible with non-square discriminant $\Delta = -108$, so $\operatorname{Gal}(x^3 - 2 / \mathbb{Q}) \cong S_3$. Q.E.D.
:::
