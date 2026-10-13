---
schema: qual/card@1
id: P-NORI-GT-4-03
kind: problem
title: The norm of an element of a free ring extension is a multiple of the element
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 4.3 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let R be a subring of a commutative ring S. Assume that S, when regarded as a R-module, is free of rank n. Prove that for every $\alpha \in S$ , there exists $\beta \in S$ such that Norm $\mathbf { \Sigma } _ { R } ^ { S } ( \alpha ) = \beta \alpha$

Show that if S is an integral domain, then $\mathrm { N o r m } _ { R } ^ { S } ( \alpha ) \neq 0$
:::

::: {.solution}
Let
$$
m_\alpha:S\to S,
\qquad
m_\alpha(s)=\alpha s.
$$
With respect to any $R$-basis of the free rank-$n$ module $S$, this is represented by a matrix
$$
T_\alpha\in\mathbb M_n(R),
$$
and by definition
$$
\operatorname{Norm}_R^S(\alpha)=\det(T_\alpha).
$$

<1>1. There exists $\beta\in S$ such that
$$
\alpha\beta=\operatorname{Norm}_R^S(\alpha).
$$

::: {.proof}
Apply Problem 4.1 to the matrix $T_\alpha$ and to the vector corresponding to the element
$$
1\in S.
$$
It gives an element $\beta\in S$ such that
$$
m_\alpha(\beta)
=\det(T_\alpha)\cdot1.
$$
By the definitions of $m_\alpha$ and the norm, this is exactly
$$
\alpha\beta=\operatorname{Norm}_R^S(\alpha).
$$
:::

<1>2. The second assertion is false for $\alpha=0$.

::: {.proof}
If $\alpha=0$, then $m_\alpha$ is the zero endomorphism of the nonzero free module $S$, so
$$
\operatorname{Norm}_R^S(0)=\det(0)=0.
$$
Thus the intended statement must concern nonzero $\alpha$.
:::

<1>3. Suppose $S$ is an integral domain and $0\ne\alpha\in S$. Then
$$
m_\alpha:S\to S
$$
is injective.

::: {.proof}
If
$$
m_\alpha(s)=\alpha s=0,
$$
then the absence of zero divisors in $S$ and the assumption $\alpha\ne0$ imply $s=0$.
:::

<1>4. Under the hypotheses of step <1>3,
$$
\boxed{\operatorname{Norm}_R^S(\alpha)\ne0}.
$$

::: {.proof}
A subring $R$ of the integral domain $S$ is itself an integral domain. The matrix $T_\alpha$ represents the injective $R$-linear map $m_\alpha$ on the free module $S\cong R^n$. By Problem 4.2, injectivity is equivalent to
$$
\det(T_\alpha)\ne0.
$$
Since this determinant is $\operatorname{Norm}_R^S(\alpha)$, the claim follows.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves the divisibility assertion. Steps <1>2--<1>4 resolve the second sentence literally and prove its intended form for every nonzero $\alpha$ in an integral domain $S$.
:::
:::
