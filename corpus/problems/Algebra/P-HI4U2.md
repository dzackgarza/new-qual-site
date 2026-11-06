---
schema: qual/card@1
id: P-HI4U2
kind: problem
title: The rings and fields $K[x]$, $K(x)$, $K[\alpha]$, and $K(\alpha)$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
  - Fields
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source asks "What are the following objects?" without declaring $K$, $x$ or $\alpha$; the statement declares them.'
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks what
    four objects are, so it is a description request, not a proof obligation, and no
    pf block was added; the record is this note. What was checked: the four answers
    (K[x] the polynomial ring; K(x) its fraction field of rational functions; K[alpha]
    the smallest subring of the ambient field containing K and alpha; K(alpha) the
    smallest subfield), and the three further claims the solution makes, which were
    verified by reading against a fresh derivation: evaluation at alpha is the
    unique K-algebra map K[x] -> K[alpha] and is surjective by the definition of
    K[alpha] as the image; its injectivity when alpha is transcendental gives
    K[alpha] = K[x] and hence K(alpha) = K(x); and when alpha is algebraic with
    minimal polynomial m the kernel is (m), irreducible, so K[x]/(m) is a field and
    K[alpha] = K(alpha). All correct. What was not checked: no source solution is
    retained for this card, so no source comparison was made; the statements are not
    certified by a formal proof here, the card asking for descriptions.
---

::: {.problem}
Let $K$ be a field, $x$ an indeterminate, and $\alpha$ an element of a field extension of $K$.
What are the following objects?

- $K(x)$

- $K[x]$

- $K(\alpha)$

- $K[\alpha]$
:::

::: {.solution}
For a field $K$ and a variable $x$, $K[x]$ is the ring of polynomials in $x$ with coefficients in $K$, and $K(x)=\Frac(K[x])$ is the field of rational functions $p/q$ with $p,q\in K[x]$, $q\neq0$.

For a field extension $K\subseteq F$ and $\alpha\in F$, $K[\alpha]$ is the smallest subring of $F$ containing $K$ and $\alpha$, and $K(\alpha)$ is the smallest subfield of $F$ containing $K$ and $\alpha$.
Evaluation $x\mapsto\alpha$ is the unique $K$-algebra homomorphism $K[x]\to K[\alpha]$ sending $x$ to $\alpha$, and it is surjective.
If $\alpha$ is transcendental over $K$, it is injective, so $K[\alpha]\cong K[x]$ and $K(\alpha)\cong K(x)$.
If $\alpha$ is algebraic with minimal polynomial $m$, its kernel is $(m)$, and $K[\alpha]\cong K[x]/(m)$ is already a field, so $K[\alpha]=K(\alpha)$.
:::
