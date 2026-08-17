---
schema: qual/card@1
id: P-E54MV
kind: problem
title: "Writing $f(x) = x^3 - 3x - 3 = \\sum a_i x_i \\in \\QQ[x]$, we can conclu\u2026"
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - irreducibility-criteria
  - permutations
relations: []
review: draft
solved: false
---

::: problem
Writing $f(x) = x^3 - 3x - 3 = \sum a_i x_i \in \QQ[x]$, we can conclude that $f$ is irreducible over $\QQ$ by Eisenstein with the prime $p=3$, since $p\divides a_0 = -3, a_1 = 3, a_2 = 0$, but $p^2 \nmid a_3 = 1$.

We can check that $f(0) < 0$ and $f(10) > 0$, so $f$ has at least one real root.
By the 1st derivative test, we can find that $f$ is increasing on $(-\infty, -1)$ and less than zero, decreasing on $(-1, 1)$ and less than zero, and increasing on $(1, \infty)$, where it it attains its root.
This root has multiplicity one, since $\gcd(f, f') = 1$, which means that $f$ has *exactly* one real root $r_0$, and thus a complex conjugate pair of roots $r_1, \overline r_1$ as well.

This means that complex conjugation is a nontrivial element $\tau$ of the Galois group $G \leq S_3$, and thus $G$ contains a 2-cycle.

The Galois group must be a transitive subgroup of $S_3$, which restricts the possibilities to $S_3, A_3$.

Since $A_3$ only contains 3-cycles, this possibility is ruled out.
Thus the Galois group must be $S_3$.
$\qed$
:::
