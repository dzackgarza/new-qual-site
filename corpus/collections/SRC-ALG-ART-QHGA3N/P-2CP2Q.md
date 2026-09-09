---
schema: qual/card@1
id: P-2CP2Q
kind: problem
title: Galois group of $x^3-3x-3$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Compute the Galois group of $f(x) = x^3-3x -3\in \QQ[x]/\QQ$.
:::


::: {.solution}
<1>1. The polynomial \(f(x)=x^3-3x-3\) is irreducible over \(\mathbb Q\).
::: {.proof}
A reducible cubic over \(\mathbb Q\) has a rational root. By the rational root theorem, any rational root must lie in \(\{\pm1,\pm3\}\). Direct substitution gives
\[
f(1)=-5,\quad f(-1)=-1,\quad f(3)=15,\quad f(-3)=-21,
\]
so \(f\) has no rational root and is irreducible.
:::

<1>2. The discriminant of \(f\) is
\[
\Delta(f)=-135.
\]
::: {.proof}
For a depressed cubic \(x^3+ax+b\), the discriminant is
\[
-4a^3-27b^2.
\]
Here \(a=-3\) and \(b=-3\), so
\[
\Delta(f)=-4(-3)^3-27(-3)^2=108-243=-135.
\]
:::

<1>3. The discriminant is not a square in \(\mathbb Q\).
::: {.proof}
One has
\[
-135=-3^3\cdot5<0.
\]
In particular it is not a square in \(\mathbb Q\).
:::

<1>4. Therefore the Galois group of the splitting field of \(f\) over \(\mathbb Q\) is \(S_3\).
::: {.proof}
Because \(f\) is irreducible of degree \(3\), its Galois group acts transitively on its three roots, so it is either \(A_3\cong C_3\) or \(S_3\). For an irreducible separable cubic over a field of characteristic not \(2\), the Galois group is contained in \(A_3\) exactly when the discriminant is a square in the base field. By <1>3 the discriminant is not a square, so the group is not contained in \(A_3\). Hence
\[
\operatorname{Gal}(f/\mathbb Q)\cong S_3.
\]
:::
:::
