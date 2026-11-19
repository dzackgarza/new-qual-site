---
schema: qual/card@1
id: P-HFGO33
kind: problem
title: Cyclotomic extension of a field
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof: the definition is stated as the answer, with the reason the
    root must be primitive (adjoining a non-primitive n-th root gives the cyclotomic extension
    of its order); the equivalence with the splitting field of T^n - 1 proved rather than
    asserted, including the separability of T^n - 1 from gcd(T^n - 1, nT^{n-1}) = 1 when
    char F does not divide n; the failure of that equivalence in the opposite case, via
    T^n - 1 = (T^m - 1)^{p^a}; and the degree bound from the cyclotomic polynomial with equality
    over Q by irreducibility. The card previously stated the equivalence without the
    characteristic hypothesis that makes it true. Not claimed: a retained solution set; the
    provenance names the examination question list.
---

::: {.problem}
Define a cyclotomic extension.
:::

::: {.solution}
The question asks for a definition; the numbered steps state it and justify the accompanying claims — the equivalent description as a splitting field, the role of the characteristic hypothesis, and the degree. The exam compilation in this collection's `provenance` (`assets/attachments/MGSA_Fields_and_Galois_Theory_Oral_Questions.pdf`) is a question list carrying no solutions, so the definition given is the standard one (Lang, *Algebra*, VI §3).

::: pf

::: {.pf-step #definition}
A **cyclotomic extension** of a field $F$ is an extension of the form $F(\zeta_n)$, where $n\ge1$ and $\zeta_n$ is a primitive $n$-th root of unity in an algebraic closure of $F$.

::: pf-proof
A definition, needing no proof. The generator is required to be *primitive*, i.e. to have order exactly $n$ in the multiplicative group: adjoining a non-primitive $n$-th root of unity $\omega$ gives $F(\omega)=F(\zeta_d)$ for the order $d$ of $\omega$, which is a cyclotomic extension of lower level.

:::

:::

::: {.pf-step #roots}
$\zeta_n^k$ for $k=0,1,\dots,n-1$ are the $n$ distinct $n$-th roots of unity, and they are exactly the powers of $\zeta_n$; hence $F(\zeta_n)$ is the splitting field of $T^n-1$ over $F$ whenever $T^n-1$ has $n$ distinct roots.

::: pf-proof
The powers $\zeta_n^k$, $k\in\ZZ$, form a cyclic group of order $n$ contained in the roots of $T^n-1$; that polynomial has at most $n$ roots, so the powers exhaust them when there are $n$ of them, which happens iff $T^n-1$ is separable. Its formal derivative is $nT^{n-1}$, whose only root is $0$ when $\operatorname{char}F\nmid n$, so then $\gcd(T^n-1,nT^{n-1})=1$ and $T^n-1$ is separable. In that case the roots generate $F(\zeta_n)$ and $T^n-1$ splits there, so $F(\zeta_n)$ is the splitting field by the minimality clause.

:::

:::

::: {.pf-step #characteristic}
If $\operatorname{char}F=p$ divides $n$, then $T^n-1$ is not separable and $F(\zeta_n)$ need not be its splitting field; the equivalence of the previous step fails.

::: pf-proof
Write $n=p^am$ with $p\nmid m$. Then $T^n-1=(T^m-1)^{p^a}$ in characteristic $p$, by the freshman's dream $(X+Y)^p=X^p+Y^p$, so every root of $T^n-1$ is a root of $T^m-1$ and there are at most $m<n$ of them. A primitive $n$-th root of unity then need not exist at all in an algebraic closure, which is why the definition of the cyclotomic extension is stated with $\zeta_n$ rather than as a splitting field.

:::

:::

::: {.pf-step #degree}
$[F(\zeta_n):F]\le\varphi(n)$, and $[\QQ(\zeta_n):\QQ]=\varphi(n)$.

::: pf-proof
$\zeta_n$ is a root of the cyclotomic polynomial $\Phi_n\in\ZZ[T]\subseteq F[T]$, of degree $\varphi(n)$, so the minimal polynomial of $\zeta_n$ over $F$ divides $\Phi_n$ and the degree is at most $\varphi(n)$. Over $\QQ$, $\Phi_n$ is irreducible (Gauss's lemma reduces it to $\ZZ[T]$, where irreducibility is the standard theorem), so the minimal polynomial is $\Phi_n$ itself and the degree is $\varphi(n)$.

:::

:::

:::
:::
