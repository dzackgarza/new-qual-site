---
schema: qual/card@1
id: P-BKS21-9B
kind: problem
title: Irreducibility of $x^4+x+2021$ over $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Prove that
$$
x^4+x+2021
$$
is irreducible over $\QQ$.
:::

::: {.solution}
Let
$$
f(x)\coloneqq x^4+x+2021\in\mathbb Z[x].
$$

<1>1. Modulo $2$,
$$
\overline f(x)=x^4+x+1\in\mathbb F_2[x].
$$

::: {.proof}
Since $2021\equiv1\pmod2$, reduction of the coefficients modulo $2$ gives the displayed polynomial.
:::

<1>2. The polynomial $\overline f$ has no linear factor over $\mathbb F_2$.

::: {.proof}
The only possible roots are $0$ and $1$, and
$$
\overline f(0)=1,
\qquad
\overline f(1)=1+1+1=1
$$
in $\mathbb F_2$. Hence $\overline f$ has no root and therefore no linear factor.
:::

<1>3. The only monic irreducible quadratic over $\mathbb F_2$ is
$$
q(x)=x^2+x+1.
$$

::: {.proof}
The monic quadratics over $\mathbb F_2$ are
$$
x^2,\quad
x^2+1,\quad
x^2+x,\quad
x^2+x+1.
$$
The first three have a root in $\mathbb F_2$, while
$$
q(0)=1,
\qquad
q(1)=1
$$
so $q$ has no root and is irreducible.
:::

<1>4. The polynomial $q$ does not divide $\overline f$.

::: {.proof}
Modulo $q$ one has
$$
x^2=x+1.
$$
Hence
$$
x^3=x(x+1)=x^2+x=1
$$
and therefore
$$
x^4=x.
$$
Thus
$$
\overline f(x)
=
x^4+x+1
\equiv
x+x+1
=1
\pmod q,
$$
so the remainder is nonzero.
:::

<1>5. The polynomial $\overline f$ is irreducible in $\mathbb F_2[x]$.

::: {.proof}
If a quartic over a field is reducible, then it has either a linear factor or a factorization into two quadratics. Step <1>2 rules out a linear factor. If it factored as two quadratics with no linear factor, both quadratic factors would have to be irreducible; by step <1>3 both would then equal $q$, contradicting step <1>4. Hence $\overline f$ is irreducible.
:::

<1>6. The polynomial
$$
\boxed{x^4+x+2021}
$$
is irreducible over $\mathbb Q$.

::: {.proof}
The polynomial $f$ is primitive. Since its reduction modulo $2$ is irreducible by step <1>5, the standard reduction criterion together with Gauss's lemma implies that $f$ is irreducible in $\mathbb Q[x]$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
