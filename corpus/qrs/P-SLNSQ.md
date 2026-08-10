---
schema: qual/card@1
id: P-SLNSQ
kind: problem
title: "1. Note that $8=2^3$ is a prime power $p^n$, so we can get this as a q\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
1. Note that $8=2^3$ is a prime power $p^n$, so we can get this as a quotient of a polynomial algebra. In particular, since $p=2$, we'll want to look at $\FF_2[t]$, and we'll want to quotient it by a polynomial of degree $n=3$ that is irreducible in the base field $\FF_2$.

    We could use Rabin's test: $f$ is irreducible over $F$ iff
  $$
  x^{p^n} - x \equiv 0 \mod f \quad\text{ and }\quad
  \left( f , x ^ { p ^ { n / q } } - x \right) = 1 ~~\forall \text{ prime $q$ dividing $n$}
  $$

    But I'm bad at polynomial division. With some work, we can brute force by listing out all of the $2^4 = 16$ polynomials over $\FF_2$ of degree at most 3. Then start multiplying together low-degree terms to cross off higher degree terms; using degree arguments you can show that the irreducible polynomials are:
  $$
  x \\
  x+1 \\
  x^2 + 1 \\
  x^2 + x + 1 \\
  x^3 + x + 1 \\
  x^3 + x^2 + 1.
  $$

    So we can pick one of the degree 3 ones to obtain our desired field:
  $$
  GF(8) = \frac{\FF_2[t]}{\generators{t^3+t+1}}. \qed
  $$
    **General Principle** Trinomials of the form $x^n + ax^{<n} + b$ with $a,b \in \FF_p$ are usually irreducible.
