---
schema: qual/card@1
id: P-BERK96S-07
kind: problem
title: Irreducibility of $x^4+x^3+x^2+6x+1$ over $\QQ$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the mod-3 root check, the exclusion of quadratic factors by
    coefficient comparison, and the Gauss-lemma reduction argument.
---

::: {.problem}
Prove that
\[
x^4+x^3+x^2+6x+1
\]
is irreducible over $\mathbb Q$.
:::

::: {.solution}
Let
$$
f(x)\coloneqq x^4+x^3+x^2+6x+1.
$$
Its reduction modulo $3$ is
$$
\bar f(x)=x^4+x^3+x^2+1\in\FF_3[x].
$$

<1>1. The polynomial $\bar f$ has no linear factor in $\FF_3[x]$.

::: {.proof}
Direct evaluation gives
$$
\bar f(0)=1,
\qquad
\bar f(1)=1,
\qquad
\bar f(2)=2
$$
in $\FF_3$. Thus $\bar f$ has no root in $\FF_3$, hence no linear
factor.
:::

<1>2. The polynomial $\bar f$ has no factorization into two monic
quadratic polynomials over $\FF_3$.

::: {.proof}
Suppose
$$
\bar f(x)
=
(x^2+ax+b)(x^2+cx+d),
\qquad
a,b,c,d\in\FF_3.
$$
Comparing constant terms gives
$$
bd=1.
$$
Hence either
$$
b=d=1
$$
or
$$
b=d=2.
$$
In either case $b=d\neq0$. Comparing the coefficients of $x^3$ gives
$$
a+c=1,
$$
whereas comparing the coefficients of $x$ gives
$$
ad+bc=b(a+c)=0.
$$
Since $b\neq0$, this forces $a+c=0$, contradicting $a+c=1$.
:::

<1>3. The reduction $\bar f$ is irreducible in $\FF_3[x]$.

::: {.proof}
A reducible polynomial of degree $4$ over a field has a factor of degree
$1$ or $2$. Step <1>1 excludes degree-$1$ factors, and step <1>2 excludes
a factorization into two degree-$2$ factors. Hence $\bar f$ is
irreducible.
:::

<1>4. The polynomial $f$ is irreducible over $\QQ$.

::: {.proof}
The polynomial $f$ is monic and lies in $\ZZ[x]$. If it were reducible over
$\QQ$, Gauss's lemma would give a factorization into two nonconstant monic
polynomials in $\ZZ[x]$. Reducing that factorization modulo $3$ would give
a nontrivial factorization of $\bar f$ in $\FF_3[x]$, contradicting
step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required irreducibility statement.
:::
:::
