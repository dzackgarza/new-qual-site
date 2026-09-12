---
schema: qual/card@1
id: P-YLMKZ
kind: problem
title: Root bounds for polynomials over division rings
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: problem
Can a polynomial over a division ring (skew-field) have more roots than its degree?
:::

::: solution
Yes. Over a noncommutative division ring, a polynomial can have more roots than its degree.

Take the Hamilton quaternions $\mathbb H$ and the polynomial
\[
p(x)=x^2+1.
\]
For every pure imaginary unit quaternion
\[
q=bi+cj+dk,
\qquad
b^2+c^2+d^2=1,
\]
one has
\[
q^2
=b^2i^2+c^2j^2+d^2k^2
+bc(ij+ji)+bd(ik+ki)+cd(jk+kj).
\]
Using
\[
i^2=j^2=k^2=-1,\qquad ij=-ji,\quad ik=-ki,\quad jk=-kj,
\]
this becomes
\[
q^2=-(b^2+c^2+d^2)=-1.
\]
Thus
\[
p(q)=q^2+1=0.
\]
The unit sphere
\[
\{bi+cj+dk:b^2+c^2+d^2=1\}
\]
therefore consists entirely of roots of the quadratic polynomial $x^2+1$. Hence a degree-$2$ polynomial over the division ring $\mathbb H$ has infinitely many roots.
:::
