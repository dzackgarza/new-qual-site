---
schema: qual/card@1
id: E-AMD-HIFDV6WB
kind: problem
title: Galois group of $x^3+4x+2$ over $\QQ$ is $S_3$
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
  date: 2026-08-29
---

::: {.exercise}
Show that $\operatorname{Gal}(x^3+4x+2 / \mathbb{Q}) \cong S_3$.
:::

::: solution
**Goal:** Prove that the Galois group of the cubic polynomial $f(x) = x^3 + 4x + 2 \in \mathbb{Q}[x]$ over $\mathbb{Q}$ is the symmetric group $S_3$.

<1>1. Irreducibility over $\mathbb{Q}$:
    *Proof:*
    <2>1. The polynomial $f(x) = x^3 + 0x^2 + 4x + 2 \in \mathbb{Z}[x]$ is monic.
    <2>2. Consider the prime $p = 2$:
        - $2 \nmid 1$ (leading coefficient),
        - $2 \mid 0$, $2 \mid 4$, and $2 \mid 2$,
        - $2^2 = 4 \nmid 2$ (constant term).
    <2>3. By Eisenstein's Criterion at $p = 2$, $f(x)$ is irreducible over $\mathbb{Q}$.

<1>2. Transitivity and candidate Galois groups:
    *Proof:*
    <2>1. Let $K$ be the splitting field of $f(x)$ over $\mathbb{Q}$, and let $G = \operatorname{Gal}(K/\mathbb{Q})$.
    <2>2. Since $f(x)$ is an irreducible cubic, $G$ embeds into $S_3$ as a transitive permutation subgroup on the $3$ roots.
    <2>3. The only transitive subgroups of $S_3$ are $A_3$ (of order $3$) and $S_3$ (of order $6$).

<1>3. Discriminant computation:
    *Proof:*
    <2>1. For a depressed cubic $x^3 + px + q$, the discriminant is given by $D = -4p^3 - 27q^2$.
    <2>2. For $f(x) = x^3 + 4x + 2$, we have $p = 4$ and $q = 2$:
        $$D = -4(4^3) - 27(2^2) = -4(64) - 27(4) = -256 - 108 = -364.$$
    <2>3. Because $D = -364 < 0$, $D$ is strictly negative and thus cannot be the square of any rational number: $\sqrt{D} \notin \mathbb{Q}$.
    <2>4. The Galois group of an irreducible cubic is $A_3$ if and only if $D \in (\mathbb{Q}^\times)^2$.
    <2>5. Since $D$ is not a square in $\mathbb{Q}$, $G \not\subseteq A_3$, which forces $G \cong S_3$.

<1>4. Complex conjugation transposition argument (alternative verification):
    *Proof:*
    <2>1. Because $D < 0$, $f(x)$ has exactly one real root and one pair of complex conjugate non-real roots.
    <2>2. Complex conjugation restricts to an automorphism in $G$ that fixes the real root and transposes the two non-real roots.
    <2>3. A transitive subgroup of $S_3$ containing a transposition must be all of $S_3$.

<1>5. Conclusion:
    $\operatorname{Gal}(x^3 + 4x + 2 / \mathbb{Q}) \cong S_3$. Q.E.D.
:::
