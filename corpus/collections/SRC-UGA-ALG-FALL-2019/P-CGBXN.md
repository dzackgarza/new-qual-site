---
schema: qual/card@1
id: P-CGBXN
kind: problem
title: The degree of $\FF_q(\omega)$ is the multiplicative order of $q$ modulo $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Roots of Unity
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was label-steps with no proofs over twenty nested one-
    sentence claims, ending in a pf-qed that only listed which step proves which part. Each part
    now has an argument: the cyclic structure of E^× and Lagrange for (a); the division
    algorithm on the exponent for (b), which is the step that converts 'q^k ≡ 1 mod n' into 'm |
    k'; and for (c) the separability of x^n - 1 (whose derivative is checked to have no common
    root with it, using gcd(n,q) = 1), the identification of its n roots with the elements of
    order dividing n in the cyclic group F_{q^m}^×, and the tower law. The answer m = k is
    unchanged. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---
::: {.problem}
Let $F = \FF_q$ be a finite field with $q$ elements. Let $n$ be a positive integer relatively prime to $q$ ($\gcd(n, q) = 1$), and let $\omega$ be a primitive $n$-th root of unity in an algebraic closure $\overline{F}$. Let $E = F(\omega) = F[\omega]$ and $k = [E : F]$.

(a) Prove that $n$ divides $q^k - 1$.

(b) Let $m = \operatorname{ord}_n(q)$ be the multiplicative order of $q$ in the group $(\ZZ/n\ZZ)^\times$. Prove that $m$ divides $k$.

(c) Prove that $m = k$.
:::

::: {.solution}
Throughout $F = \FF_{q}$, $n$ is a positive integer with $\gcd(n,q) = 1$, $\omega$ is a primitive $n$-th root of unity in an algebraic closure $\overline{F}$ of $F$, $E \coloneqq F(\omega)$, $k \coloneqq [E:F]$, and $m \coloneqq \operatorname{ord}_{n}(q)$ is the order of $q$ in $(\ZZ/n\ZZ)^{\times}$, so that $m$ is the least positive integer with $n \mid q^{m}-1$. The collection's `provenance` is the Fall 2019 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #a}
(a) $n \mid q^{k} - 1$.

::: pf-proof
$E$ is a finite extension of the finite field $F$, so $\cardinality{E} = q^{k}$; its multiplicative group $E^{\times}$ is cyclic of order $q^{k}-1$. Since $\omega \in E^{\times}$ has order exactly $n$ — it is a primitive $n$-th root of unity — Lagrange's theorem gives $n \mid q^{k}-1$.

:::

:::

::: {.pf-step #b}
(b) $m \mid k$.

::: pf-proof
By step [](#a){.pf-ref} $n$ divides $q^{k}-1$, that is $q^{k} \equiv 1 \pmod n$, so $k$ is a positive integer with $n \mid q^{k}-1$. The order $m$ of $q$ modulo $n$ is the least such positive integer, and the set of positive integers $j$ with $q^{j} \equiv 1 \pmod n$ is exactly the set of multiples of $m$: writing $j = am + r$ with $0 \le r < m$ gives $q^{j} \equiv q^{r}$, so $q^{j} \equiv 1$ forces $r = 0$ by minimality of $m$. Hence $m \mid k$.

:::

:::

::: {.pf-step #c}
(c) $m = k$.

::: pf-proof
By definition of $m$ one has $n \mid q^{m}-1$, so the multiplicative group $\FF_{q^{m}}^{\times}$, which is cyclic of order $q^{m}-1$, has an element of order $n$. The polynomial $x^{n}-1$ is separable — its derivative $nx^{n-1}$ has no root in common with it, since $n \ne 0$ in $\FF_{q}$ by $\gcd(n,q) = 1$ and $x \ne 0$ at any root — so it has exactly $n$ distinct roots in $\FF_{q^{m}}$, and they are precisely the elements of order dividing $n$. The primitive $n$-th roots are the generators of that cyclic subgroup of order $n$, and they are the powers $\omega^{i}$ with $i$ coprime to $n$; since the roots of $x^{n}-1$ in $\FF_{q^{m}}$ already number $n$ and include one primitive root, all the powers $\omega^{i}$ lie in $\FF_{q^{m}}$, in particular $\omega$ itself. Hence $E = F(\omega) \subseteq \FF_{q^{m}}$, and by the tower law $k = [E:F]$ divides $[\FF_{q^{m}}:F] = m$. With step [](#b){.pf-ref} this gives $m = k$.

:::

:::

::: pf-step
The three assertions hold: $n \mid q^{k}-1$, $m \mid k$, and $m = k$, so $k$ is the multiplicative order of $q$ modulo $n$.

::: pf-proof
Parts (a) and (b) are steps [](#a){.pf-ref} and [](#b){.pf-ref}; part (c) is step [](#c){.pf-ref}, which closes the two divisibilities in the single equality $m = k$.

:::

:::

:::
:::
