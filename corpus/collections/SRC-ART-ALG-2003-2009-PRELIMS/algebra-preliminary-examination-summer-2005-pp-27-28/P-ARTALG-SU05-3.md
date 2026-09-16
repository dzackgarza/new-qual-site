---
schema: qual/card@1
id: P-ARTALG-SU05-3
kind: problem
title: 'Principal ideal domains and the nonprincipal ideal $(2,x)\subset\ZZ[x]$'
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with Summer 2005 problem 3 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified properness of (2,x) and excluded every possible generator using the constant polynomial 2 and the coefficient of x."
---

::: {.problem}
(a) State the definition of a principal ideal domain.

(b) Let $\mathbb{Z}$ be the ring of integers.
Is $\mathbb{Z}[x]$ a principal ideal domain?
Either prove that it is, or present an example showing that it is not.
:::

::: {.solution}
<1>1. A principal ideal domain is a commutative ring $R$ with
identity $1\ne0$, no zero divisors, and every ideal of the form
$(a)=\{ra:r\in R\}$ for some $a\in R$ [@DF04].

<1>2. The ideal $I=(2,x)$ of $\mathbb Z[x]$ is proper.

::: {.proof}
Every element of $I$ has the form $2g(x)+xh(x)$ with
$g,h\in\mathbb Z[x]$. Its constant coefficient is $2g(0)$,
which is even. The polynomial $1$ has odd constant coefficient,
so $1\notin I$ and $I\ne\mathbb Z[x]$.
:::

<1>3. The ideal $I$ is not principal, so $\mathbb Z[x]$ is not a
principal ideal domain.

::: {.proof}
Suppose $I=(f)$. Since $2\in I$, there is $g\in\mathbb Z[x]$
such that $fg=2$. Neither factor is zero. Leading coefficients
of nonzero integer polynomials have nonzero product, so degrees
add; hence $\deg f+\deg g=0$. Both factors are constant
integers, and $f$ divides $2$. Thus $f\in\{1,-1,2,-2\}$.

The possibilities $f=1$ and $f=-1$ contradict the properness
proved in step <1>2. The possibilities $f=2$ and $f=-2$ would
give $I=(2)$, but every coefficient of a polynomial in $(2)$
is even, whereas the coefficient of $x$ in $x\in I$ is $1$.
Thus no generator exists.

The same leading-coefficient argument shows that $\mathbb Z[x]$
is an integral domain. Its failure here is precisely the existence
of the nonprincipal ideal $I$, not the domain condition.
:::
:::
