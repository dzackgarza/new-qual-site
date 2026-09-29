---
schema: qual/card@1
id: P-AGXVARKRULLHAUPT
kind: problem
title: Components of the zero locus of a nonconstant regular function have codimension one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Krull Height Theorem
  - Dimension
  - Regular Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 4.9 in the recorded source. It assumes that X is
    an affine variety and asks that every irreducible component of the zero
    fibre of a nonconstant regular function have dimension dim X - 1.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the source's missing standalone hypothesis that X is an affine
    variety, and made the standing base field explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Identified fibre components with minimal primes over (f), applied Krull's
    principal ideal theorem in the coordinate domain, and converted height one
    to dimension dim X - 1 by the affine height-dimension formula.
---

::: {.problem}
Let $X$ be an affine variety over the algebraically closed ground field $k$,
and let
$$
f\in\mco(X)
$$
be nonconstant. Show that every irreducible component $Z$ of
$f^{-1}(0)$ has
$$
\dim Z=\dim X-1.
$$
:::

::: {.solution}
Put
$$
A=\mco(X).
$$
Since $X$ is an affine variety, $A$ is a finitely generated integral
$k$-algebra.

::: pf

::: {.pf-step #f-nonzero-nonunit}
If $f^{-1}(0)$ is nonempty, then $f$ is a nonzero nonunit of $A$.

::: pf-proof
Because $f$ is nonconstant, it is not the zero element of $A$. Since $A$ is
a domain, $f$ is therefore not a zero divisor.

If $f$ were a unit, then it would vanish nowhere on $X$, so
$$
f^{-1}(0)=\varnothing.
$$
Thus whenever the zero fibre has an irreducible component, $f$ is also a
nonunit.
:::

:::

::: {.pf-step #z-equals-vp}
Let $Z$ be an irreducible component of $f^{-1}(0)$. Then there is a
prime ideal $\mathfrak p\subseteq A$, minimal over $(f)$, such that
$$
Z=V(\mathfrak p).
$$

::: pf-proof
The zero fibre is the closed subset
$$
f^{-1}(0)=V(f)\subseteq X.
$$
The irreducible components of a closed subset of an affine variety correspond
to the primes minimal over its defining ideal. Therefore each irreducible
component $Z$ is $V(\mathfrak p)$ for a prime $\mathfrak p$ minimal over
$(f)$.
:::

:::

::: {.pf-step #height-p-one}
Every prime $\mathfrak p$ occurring in step [](#z-equals-vp){.pf-ref} has
$$
\height\mathfrak p=1.
$$

::: pf-proof
By step [](#f-nonzero-nonunit){.pf-ref}, $f$ is neither a unit nor a zero divisor in the Noetherian ring
$A$. Krull's principal ideal theorem
[[PR-VARHT|Hauptidealsatz]]
therefore says that every prime minimal over $(f)$ has height one. This
applies to the prime $\mathfrak p$ from step [](#z-equals-vp){.pf-ref}.
:::

:::

::: {.pf-step #dim-z-formula}
Every irreducible component $Z$ of $f^{-1}(0)$ has
$$
\boxed{
\dim Z=\dim X-1.
}
$$

::: pf-proof
For the prime $\mathfrak p$ corresponding to $Z$, one has
$$
\dim Z=\dim(A/\mathfrak p).
$$
The affine height-dimension formula
[[P-AGH2320DIMENSION]] gives
$$
\dim(A/\mathfrak p)+\height\mathfrak p=\dim A.
$$
By step [](#height-p-one){.pf-ref},
$$
\height\mathfrak p=1.
$$
Hence
$$
\dim Z
=
\dim A-1
=
\dim X-1.
$$
:::

:::

::: pf-qed
If $f^{-1}(0)=\varnothing$, the assertion is vacuous. Otherwise steps
[](#z-equals-vp){.pf-ref}, [](#height-p-one){.pf-ref} and [](#dim-z-formula){.pf-ref} prove the stated dimension for every irreducible component.
:::

:::

:::
