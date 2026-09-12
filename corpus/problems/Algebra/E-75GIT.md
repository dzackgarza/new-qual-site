---
schema: qual/card@1
id: E-75GIT
kind: problem
title: $a$ is algebraic over $K(b)$ if $b$ is algebraic over $K(a)$ and transcendental
  over $K$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Transcendence
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against the UCR qualifying-algebra Galois problem list.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
1. Suppose that for an extension field $F$ over $K$ and for $a \in F$, we have that $b \in F$ is algebraic over $K(a)$ but transcendental over $K$.
   Prove that $a$ is algebraic over $K(b)$.
:::

::: {.solution}
<1>1. Because \(b\) is algebraic over \(K(a)\), there is a nonzero polynomial
\[
q(Y)=c_0+c_1Y+\cdots+c_mY^m\in K(a)[Y]
\]
such that \(q(b)=0\).
::: {.proof}
This is the definition of \(b\) being algebraic over \(K(a)\).
:::

<1>2. Clearing denominators in the coefficients \(c_i\in K(a)\) yields a nonzero polynomial \(P(X,Y)\in K[X,Y]\) such that
\[
P(a,b)=0.
\]
::: {.proof}
Write each \(c_i=r_i(a)/s_i(a)\) with \(r_i,s_i\in K[X]\) and \(s_i(a)\neq0\). Multiplying \(q(b)=0\) by the product of the denominators gives a relation
\[
\sum_i R_i(a)b^i=0
\]
with \(R_i\in K[X]\), not all zero. Set \(P(X,Y)=\sum_iR_i(X)Y^i\).
:::

<1>3. The polynomial \(P(X,b)\in K(b)[X]\) is nonzero.
::: {.proof}
Write
\[
P(X,Y)=\sum_{j=0}^d p_j(Y)X^j
\]
with \(p_j\in K[Y]\), not all zero. Since \(b\) is transcendental over \(K\), the evaluation map \(K[Y]\to K(b)\), \(Y\mapsto b\), is injective. Hence not all \(p_j(b)\) vanish, so \(P(X,b)\neq0\) in \(K(b)[X]\).
:::

<1>4. Therefore \(a\) is algebraic over \(K(b)\).
::: {.proof}
By <1>2,
\[
P(a,b)=0,
\]
and by <1>3, \(P(X,b)\) is a nonzero polynomial with coefficients in \(K(b)\). Thus \(a\) satisfies a nonzero polynomial over \(K(b)\), which is exactly algebraicity over \(K(b)\).
:::
:::
