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
Let
$$
f(x)=a_n\prod_{i=1}^n(x-r_i)
$$
in a splitting field, with $a_n\ne0$. The discriminant of $f$ is
$$
\disc{f}
=
a_n^{2n-2}\prod_{1\le i<j\le n}(r_i-r_j)^2.
$$

Equivalently,
$$
\disc{f}
=
(-1)^{n(n-1)/2}a_n^{-1}\operatorname{Res}(f,f').
$$
Because the product of squared root differences is symmetric in the roots, the fundamental theorem of symmetric polynomials shows that the discriminant is a polynomial in the coefficients of $f$.

Over a field, one has
$$
\disc{f}=0
\iff
f\text{ has a repeated root}
\iff
\gcd(f,f')\ne1.
$$
For a monic quadratic $x^2+bx+c$, this gives $\disc{f}=b^2-4c$.
:::
