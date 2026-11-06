---
schema: qual/card@1
id: E-6TMP7
kind: problem
title: Galois group of $x^2-2$ is $\ZZ/2\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Compute the Galois group of $x^2-2$." with no base field; the statement now names the base field $\QQ$ that the solution uses.'
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement
    (already repaired by the earlier source-corrected event; the base field is
    needed and present, so no further repair), the existing prose solution
    against a fresh re-derivation (correct, and subsumed by the structured
    proof), and the collection record (SRC-UNSORTED-ALGEBRA, a compilation with
    no provenance href), so no printed source exists here to compare against.
    What was not checked: any printed source for this statement.
---

::: {.exercise}
Compute the Galois group of $x^2-2$ over $\QQ$.
:::

::: {.solution}
Write $\alpha=\sqrt2\in\RR$ and $L=\QQ(\alpha)$.

::: pf

::: {.pf-step #irred}
$x^2-2$ is irreducible over $\QQ$.

::: pf-proof
Suppose $\alpha=a/b$ with $a,b\in\ZZ$, $b\neq0$ and $\gcd(a,b)=1$. Then $a^2=2b^2$, so $2\mid a^2$ and therefore $2\mid a$; writing $a=2c$ gives $4c^2=2b^2$, that is $b^2=2c^2$, so $2\mid b$, contradicting $\gcd(a,b)=1$. Hence $\alpha\notin\QQ$, and likewise $-\alpha\notin\QQ$. A quadratic polynomial over a field is reducible exactly when it has a root in that field, and the roots of $x^2-2$ are $\pm\alpha$; so $x^2-2$ is irreducible over $\QQ$.
:::

:::

::: {.pf-step #minpoly}
$[\QQ(\alpha):\QQ]=2$, and $x^2-2$ is the minimal polynomial of $\alpha$ over $\QQ$.

::: pf-proof
By step [](#irred){.pf-ref}, $x^2-2$ is irreducible over $\QQ$; it is monic and vanishes at $\alpha$, hence it is the minimal polynomial of $\alpha$. The degree of a simple algebraic extension equals the degree of the minimal polynomial of its generator, so $[\QQ(\alpha):\QQ]=2$.
:::

:::

::: {.pf-step #split}
$L$ is the splitting field of $x^2-2$ over $\QQ$.

::: pf-proof
The roots of $x^2-2$ in $\RR$ are $\alpha$ and $-\alpha$, and $-\alpha\in L$ because $L$ is a field containing $\alpha$. So $x^2-2$ splits into linear factors over $L$, and $L=\QQ(\alpha)$ is generated over $\QQ$ by its roots.
:::

:::

::: {.pf-step #exists}
There is a $\QQ$-automorphism $\sigma$ of $L$ with $\sigma(\alpha)=-\alpha$.

::: pf-proof
Both $\alpha$ and $-\alpha$ have minimal polynomial $x^2-2$ over $\QQ$ (step [](#minpoly){.pf-ref} for $\alpha$, and $(-\alpha)^2-2=0$ with $x^2-2$ irreducible for $-\alpha$), and $\QQ(-\alpha)=\QQ(\alpha)=L$. For simple algebraic extensions the assignment of a root of an irreducible polynomial to another root extends to a field isomorphism $\QQ(\alpha)\to\QQ(-\alpha)$ fixing $\QQ$; since the two fields coincide, this is a $\QQ$-automorphism $\sigma$ of $L$ with $\sigma(\alpha)=-\alpha$.
:::

:::

::: {.pf-step #order}
$|\Gal(L/\QQ)|=[L:\QQ]=2$.

::: pf-proof
By step [](#split){.pf-ref}, $L$ is the splitting field over $\QQ$ of $x^2-2$; that polynomial is separable because $2\neq0$ in $\QQ$, so $L/\QQ$ is a finite Galois extension. For such an extension the number of automorphisms fixing the base field equals the degree, hence $|\Gal(L/\QQ)|=[L:\QQ]$, which is $2$ by step [](#minpoly){.pf-ref}.
:::

:::

::: {.pf-step}
$\Gal(\QQ(\sqrt2)/\QQ)=\{\mathrm{id},\sigma\}$ with $\sigma(\alpha)=-\alpha$, and $\Gal(\QQ(\sqrt2)/\QQ)=\boxed{\ZZ/2\ZZ}$.

::: pf-proof
A $\QQ$-automorphism $\tau$ of $L$ fixes $\QQ$, so it sends the root $\alpha$ of $x^2-2$ to a root of $x^2-2$ lying in $L$, namely $\alpha$ or $-\alpha$; since $L=\QQ(\alpha)$, $\tau$ is determined by $\tau(\alpha)$. The identity and the map $\sigma$ of step [](#exists){.pf-ref} are therefore the only candidates, and step [](#order){.pf-ref} says there are exactly two. A group of order $2$ is cyclic, so $\Gal(\QQ(\sqrt2)/\QQ)\cong\ZZ/2\ZZ$.
:::

:::

:::
:::
