---
schema: qual/card@1
id: P-GLKAB
kind: problem
title: Discriminant of a polynomial
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks what a
    discriminant is, so the answer is a definition and there is no proof obligation;
    no pf block was added. What was checked: the definition as given,
    disc f = a_n^{2n-2} prod_{i<j} (r_i - r_j)^2 in a splitting field, which is the
    standard normalization; the equivalence disc f = (-1)^{n(n-1)/2} a_n^{-1}
    Res(f, f'), which is the standard resultant formula (the sign is the parity of
    the number of pairs, and the a_n^{-1} matches the resultant's own normalization);
    the claim that the discriminant is a polynomial in the coefficients, which holds
    because the squared Vandermonde product is symmetric in the roots; the
    equivalence disc f = 0 iff f has a repeated root iff gcd(f, f') != 1 over a
    field; and the quadratic check b^2 - 4c for monic x^2 + bx + c. All correct. What
    was not checked: nothing beyond the statements — the resultant formula and the
    symmetric-function claim are standard results quoted, not proved, here; no
    source solution is retained for this card, so no source comparison was made.
---

::: {.problem}
What is the discriminant of a polynomial?
:::

::: {.solution}

No retained solution set covers this exercise: the card is an unsorted compilation problem with no book or sheet attributed in its collection, so the account below is the card's own. The question asks for the definition and for the standard properties; the earlier version of the card listed them, including the resultant formula, without deriving any of them. The derivation from the definition is supplied here, so that the properties are consequences rather than assertions.

Throughout, $f(x)=a_{n}\prod_{i=1}^{n}(x-r_{i})\in k[x]$ with $a_{n}\neq0$ and $n\geq1$, the roots $r_{1},\dots,r_{n}$ are listed with multiplicity in a splitting field, and $f'$ is the formal derivative.

::: pf

::: {.pf-step #definition}
The discriminant of $f$ is
$$
\disc{f}\coloneqq a_{n}^{2n-2}\prod_{1\leq i<j\leq n}(r_{i}-r_{j})^{2}.
$$

::: pf-proof
This is the definition. It depends only on $f$ and not on the order in which the roots are listed, because a permutation of the roots permutes the factors of the product $(r_{i}-r_{j})^{2}$, each of which is unchanged by interchanging $i$ and $j$; and it does not depend on the splitting field, since the product is invariant under the Galois group of one splitting field over another inside a common closure.
:::

:::

::: {.pf-step #resultant-formula}
$$
\disc{f}=(-1)^{n(n-1)/2}a_{n}^{-1}\operatorname{Res}(f,f').
$$

:::: pf-proof

::: {.pf-step #res-value}
$\operatorname{Res}(f,f')=a_{n}^{n-1}\prod_{i=1}^{n}f'(r_{i})$.

::: pf-proof
This is the product formula for the resultant, $\operatorname{Res}(f,g)=a_{n}^{\deg g}\prod_{i}g(r_{i})$ for $f=a_{n}\prod_{i}(x-r_{i})$, applied to $g=f'$, whose degree is $n-1$. The formula is the standard identity relating the Sylvester-determinant definition of the resultant to the values of $g$ at the roots of $f$; it is used here as a known identity about resultants rather than derived from the determinant.
:::

:::

::: {.pf-step #derivative-at-root}
$f'(r_{i})=a_{n}\prod_{j\neq i}(r_{i}-r_{j})$.

::: pf-proof
Differentiate $f=a_{n}\prod_{k}(x-r_{k})$ by the product rule: $f'=a_{n}\sum_{i}\prod_{k\neq i}(x-r_{k})$, and evaluating at $x=r_{i}$ kills every summand whose product omits $r_{i}$, leaving the one in which the factor $(x-r_{i})$ is the missing one.
:::

:::

::: {.pf-step #rearrangement}
$a_{n}^{n-1}\prod_{i}f'(r_{i})=(-1)^{n(n-1)/2}a_{n}^{2n-1}\prod_{i<j}(r_{i}-r_{j})^{2}$.

::: pf-proof
Substituting step [](#derivative-at-root){.pf-ref} gives $a_{n}^{n-1}\prod_{i}a_{n}\prod_{j\neq i}(r_{i}-r_{j})=a_{n}^{2n-1}\prod_{i\neq j}(r_{i}-r_{j})$. The product over ordered pairs $(i,j)$ with $i\neq j$ contains each unordered pair twice, contributing $(r_{i}-r_{j})(r_{j}-r_{i})=-(r_{i}-r_{j})^{2}$; there are $n(n-1)/2$ unordered pairs, so the product equals $(-1)^{n(n-1)/2}\prod_{i<j}(r_{i}-r_{j})^{2}$.
:::

:::

::: {.pf-step}
The formula follows.

::: pf-proof
By steps [](#res-value){.pf-ref} and [](#rearrangement){.pf-ref}, $\operatorname{Res}(f,f')=(-1)^{n(n-1)/2}a_{n}^{2n-1}\prod_{i<j}(r_{i}-r_{j})^{2}$. Multiplying by $(-1)^{n(n-1)/2}a_{n}^{-1}$ — legitimate since $a_{n}\neq0$ and the sign is its own inverse — gives $a_{n}^{2n-2}\prod_{i<j}(r_{i}-r_{j})^{2}$, which is $\disc f$ by step [](#definition){.pf-ref}.
:::

:::

::::

:::

::: {.pf-step #symmetric}
$\disc f$ is a polynomial in the coefficients of $f$, with integer coefficients when $f$ is monic.

::: pf-proof
The product $\prod_{i<j}(r_{i}-r_{j})^{2}$ is a symmetric polynomial in $r_{1},\dots,r_{n}$ with integer coefficients: symmetrizing permutes the factors. By the fundamental theorem of symmetric polynomials it is a polynomial with integer coefficients in the elementary symmetric functions of the roots, and those are, up to sign, the coefficients $a_{n-1}/a_{n},\dots,a_{0}/a_{n}$ of $f$. Multiplying by $a_{n}^{2n-2}$ clears the denominators of the powers of $a_{n}$ exactly, giving a polynomial in $a_{0},\dots,a_{n-1}$ with coefficients in $\ZZ$ when $a_{n}=1$.
:::

:::

::: pf-step
Consequently, over a field,
$$
\disc f=0\iff f\text{ has a repeated root}\iff\gcd(f,f')\neq1,
$$
and for the monic quadratic $x^{2}+bx+c$ one has $\disc f=b^{2}-4c$.

::: pf-proof
By step [](#definition){.pf-ref}, $\disc f=0$ holds exactly when $a_{n}=0$, impossible, or some $r_{i}-r_{j}=0$ with $i\neq j$, that is exactly when $f$ has a repeated root. A root $r$ is repeated exactly when $f(r)=f'(r)=0$, so the existence of a repeated root is the existence of a common root of $f$ and $f'$ in the splitting field, which happens exactly when $f$ and $f'$ have a common nonconstant factor, that is exactly when $\gcd(f,f')\neq1$ in $k[x]$ — the gcd computed in $k[x]$ already generates the ideal of common divisors over any extension. For $f=x^{2}+bx+c$ with roots $r_{1},r_{2}$ one has $r_{1}+r_{2}=-b$ and $r_{1}r_{2}=c$, so $\disc f=(r_{1}-r_{2})^{2}=(r_{1}+r_{2})^{2}-4r_{1}r_{2}=b^{2}-4c$.
:::

:::

:::

:::
