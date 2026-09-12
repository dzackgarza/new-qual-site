---
schema: qual/card@1
id: P-ALGS23H
kind: problem
title: "Flat and projective modules"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
In this question, briefly justify your answers by stating the main relevant results.

(a) Suppose $D$ is a PID. Prove that a finitely generated $D$-module is flat if and only if it is free.

(b) Prove that every projective $A$-module is flat, where $A$ is a unital commutative ring.
:::


::: {.solution}
**(a).**

<1>1. Every free \(D\)-module is flat.
::: {.proof}
Tensoring with a free module \(D^{(I)}\) is naturally the direct sum of \(I\) copies of the identity functor. Direct sums preserve injections, so \(-\otimes_D D^{(I)}\) is exact.
:::

<1>2. Let \(M\) be a flat \(D\)-module. Then \(M\) is torsion-free.
::: {.proof}
Let \(0\ne d\in D\). Since \(D\) is a domain, multiplication by \(d\) gives an injective map
\[
D\xrightarrow{\cdot d}D.
\]
Because \(M\) is flat, tensoring with \(M\) preserves this injection. Under the canonical identifications \(D\otimes_D M\cong M\), the induced map is multiplication by \(d\) on \(M\). Hence \(dm=0\) implies \(m=0\).
:::

<1>3. If \(M\) is finitely generated and flat, then \(M\) is free.
::: {.proof}
By <1>2, \(M\) is torsion-free. The structure theorem for finitely generated modules over a PID gives
\[
M\cong D^r\oplus T
\]
with \(T\) the torsion submodule. Torsion-freeness forces \(T=0\), so \(M\cong D^r\).
:::

<1>4. Therefore a finitely generated \(D\)-module is flat if and only if it is free.
::: {.proof}
The forward implication is <1>3 and the reverse implication is <1>1.
:::

**(b).**

<1>5. Let \(P\) be a projective \(A\)-module. Then there exist a free \(A\)-module \(F\) and an \(A\)-module \(Q\) such that
\[
F\cong P\oplus Q.
\]
::: {.proof}
Choose a surjection from a free module \(F\twoheadrightarrow P\). Projectivity of \(P\) gives a section, so the resulting short exact sequence splits.
:::

<1>6. A direct summand of a flat module is flat.
::: {.proof}
Suppose \(F=P\oplus Q\) is flat and \(u:X\hookrightarrow Y\) is injective. Tensoring with \(F\) gives an injective map
\[
u\otimes F:(X\otimes_A P)\oplus(X\otimes_A Q)\longrightarrow (Y\otimes_A P)\oplus(Y\otimes_A Q).
\]
This map is the direct sum of \(u\otimes P\) and \(u\otimes Q\). If \((u\otimes P)(z)=0\), then \((z,0)\) lies in the kernel of \(u\otimes F\), so \(z=0\). Thus \(u\otimes P\) is injective for every injection \(u\), which is the flatness criterion.
:::

<1>7. Every projective \(A\)-module is flat.
::: {.proof}
By <1>5, \(P\) is a direct summand of a free module. Free modules are flat by the same argument as <1>1, and <1>6 shows that a direct summand of a flat module is flat.
:::
:::
