---
schema: qual/card@1
id: E-XFV6F
kind: problem
title: Splitting field of $x^{3}-x+1$ over $\mathbb{F}_{3}$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
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
15. Consider the polynomial $f=x^{3}-x+1$ in $\FF_3[x]$.
    Prove that $f$ is irreducible.
    Calculate the degree of the splitting field of $f$ over $\FF_3$ and the cardinality of the splitting field of $f$.
:::


::: {.solution}
Let
\[
f(x)=x^3-x+1\in\FF_3[x].
\]

<1>1. The polynomial $f$ has no root in $\FF_3$.
::: {.proof}
Evaluate at the three elements of $\FF_3$:
\[
f(0)=1,
\qquad
f(1)=1-1+1=1,
\qquad
f(2)=8-2+1=7\equiv1\pmod3.
\]
Thus $f(a)\neq0$ for every $a\in\FF_3$.
:::

<1>2. Hence $f$ is irreducible over $\FF_3$.
::: {.proof}
A reducible cubic over a field has a linear factor, hence a root in that field. By <1>1, $f$ has no root in $\FF_3$, so it is irreducible.
:::

<1>3. If $\alpha$ is a root of $f$ in an algebraic closure, then
\[
[\FF_3(\alpha):\FF_3]=3
\]
and therefore
\[
|\FF_3(\alpha)|=3^3=27.
\]
::: {.proof}
By <1>2, the minimal polynomial of $\alpha$ over $\FF_3$ is $f$, which has degree $3$. Hence the simple extension has degree $3$. A degree-$3$ extension of the field with three elements is a three-dimensional vector space over $\FF_3$, so it has $3^3=27$ elements.
:::

<1>4. The field $\FF_3(\alpha)$ is the splitting field of $f$.
::: {.proof}
The field $\FF_3(\alpha)$ has $27$ elements. Every element $a$ of this field satisfies
\[
a^{27}=a,
\]
so every element is a root of $x^{27}-x$.

Since $f$ is irreducible of degree $3$, it divides $x^{27}-x$ over $\FF_3$: equivalently, the Frobenius orbit of any root of $f$ has length $3$, and its roots are
\[
\alpha,\alpha^3,\alpha^9.
\]
All three lie in $\FF_3(\alpha)$. Thus $f$ splits there. Since any splitting field contains a root $\alpha$, it must contain $\FF_3(\alpha)$, so this field is the splitting field.
:::

<1>5. Therefore the splitting field has degree $3$ over $\FF_3$ and cardinality $27$.
::: {.proof}
This is exactly <1>3--<1>4.
:::
:::
