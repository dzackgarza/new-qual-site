---
schema: qual/card@1
id: P-FHDRZ
kind: problem
title: The smallest finite field in which a degree $4$ polynomial with integer coefficients
  necessarily has four roots
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $f\in\FF_q[x]$ have degree at most $4$.
Find the smallest extension $\FF_{q^N}$ that is guaranteed to split every such polynomial completely.
:::

::: {.solution}
Every irreducible factor of a polynomial of degree at most $4$ has degree in
\[
\{1,2,3,4\}.
\]
An irreducible polynomial over $\FF_q$ of degree $d$ splits over $\FF_{q^N}$ if and only if $d\mid N$.
Therefore every polynomial of degree at most $4$ splits over $\FF_{q^N}$ exactly when
\[
1,2,3,4\mid N.
\]
The smallest such integer is
\[
N=\operatorname{lcm}(1,2,3,4)=12.
\]
Hence
\[
\boxed{\FF_{q^{12}}}
\]
is the smallest extension that splits every polynomial of degree at most $4$ over $\FF_q$.

Minimality is genuine: irreducible polynomials of degrees $3$ and $4$ exist over every finite field, so any universal splitting field must have extension degree divisible by both $3$ and $4$, hence by $12$.
:::
