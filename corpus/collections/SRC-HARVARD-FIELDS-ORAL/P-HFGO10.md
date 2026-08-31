---
schema: qual/card@1
id: P-HFGO10
kind: problem
title: Degree of a field's algebraic closure
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
What can be said about the degree of a field in its algebraic closure?
:::

::: {.solution}
<1>1. Statement of the possible degrees $[\overline{F} : F]$:
<2>1. By the Artin–Schreier Theorem, the degree of the algebraic closure $[\overline{F} : F]$ can only take the values:
\[
[\overline{F} : F] \in \{1, 2, \infty\}.
\]
In particular, it is impossible for $[\overline{F} : F]$ to be finite and strictly greater than $2$.

<1>2. Detailed characterization of the three cases:
<2>1. **Case 1 ($[\overline{F} : F] = 1$):**
This occurs if and only if $F$ is already algebraically closed ($F = \overline{F}$).
<2>2. **Case 2 ($[\overline{F} : F] = 2$):**
This occurs if and only if $F$ is a real closed field.
In this case:
- $\operatorname{char}(F) = 0$,
- $\overline{F} = F(i)$ where $i^2 = -1 \notin F^2$,
- $F$ admits a unique ordering making it an ordered field in which every positive element is a square and every polynomial of odd degree has a root in $F$.
Example: $F = \mathbb{R}$ with $\overline{F} = \mathbb{C}$, or $F = \mathbb{R}_{\mathrm{alg}}$ (the field of real algebraic numbers).
<2>3. **Case 3 ($[\overline{F} : F] = \infty$):**
This occurs for all other fields.
Examples include all finite fields $\mathbb{F}_q$, the rational numbers $\mathbb{Q}$, $p$-adic fields $\mathbb{Q}_p$, and function fields $k(t)$.

<1>3. Proof sketch of the Artin–Schreier constraint $[\overline{F} : F] < \infty \implies [\overline{F} : F] \le 2$:
<2>1. If $1 < [\overline{F} : F] < \infty$, the extension $\overline{F}/F$ is a finite Galois extension with Galois group $G = \operatorname{Gal}(\overline{F}/F)$.
By Sylow theory, if $|G|$ has an odd prime divisor $p$, $G$ contains a subgroup of order $p$, corresponding to an intermediate field $K$ with $[\overline{F} : K] = p$.
<2>2. A cyclic extension of degree $p$ of an algebraically closed field is impossible (by Kummer theory and Artin–Schreier theory, adjoining roots of $x^p - a$ or $x^p - x - a$ creates non-trivial finite extensions, contradicting that $\overline{F}$ is algebraically closed).
Thus $|G| = 2^k$.
A further cohomological analysis (or analysis of sums of squares) forces $k = 1$, so $G \cong \mathbb{Z}/2\mathbb{Z}$ and $[\overline{F} : F] = 2$.

<1>4. Conclusion:
$[\overline{F} : F]$ is $1$ if $F$ is algebraically closed, $2$ if $F$ is real closed, and $\infty$ otherwise. Q.E.D.
:::
