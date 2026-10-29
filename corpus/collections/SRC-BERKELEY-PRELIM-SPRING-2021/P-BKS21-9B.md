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
f(x)\coloneqq x^4+x+2021\in\ZZ[x].
$$

::: pf

::: {.pf-step #s1-1}

Modulo $2$,
$$
\overline f(x)=x^4+x+1\in\mathbb F_2[x].
$$


::: pf-proof

Since $2021\equiv1\pmod2$, reduction of the coefficients modulo $2$ gives the displayed polynomial.

:::

:::

::: {.pf-step #s1-2}

The polynomial $\overline f$ has no linear factor over $\mathbb F_2$.


::: pf-proof

The only possible roots are $0$ and $1$, and
$$
\overline f(0)=1,
\qquad
\overline f(1)=1+1+1=1
$$
in $\mathbb F_2$. Hence $\overline f$ has no root and therefore no linear factor.

:::

:::

::: {.pf-step #s1-3}

The only monic irreducible quadratic over $\mathbb F_2$ is
$$
q(x)=x^2+x+1.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-4}

The polynomial $q$ does not divide $\overline f$.


::: pf-proof

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

:::

::: {.pf-step #s1-5}

The polynomial $\overline f$ is irreducible in $\mathbb F_2[x]$.


::: pf-proof

If a quartic over a field is reducible, then it has either a linear factor or a factorization into two quadratics. Step [](#s1-2){.pf-ref} rules out a linear factor. If it factored as two quadratics with no linear factor, both quadratic factors would have to be irreducible; by step [](#s1-3){.pf-ref} both would then equal $q$, contradicting step [](#s1-4){.pf-ref}. Hence $\overline f$ is irreducible.

:::

:::

::: {.pf-step #s1-6}

The polynomial
$$
\boxed{x^4+x+2021}
$$
is irreducible over $\QQ$.


::: pf-proof

The polynomial $f$ is primitive. Since its reduction modulo $2$ is irreducible by step [](#s1-5){.pf-ref}, the standard reduction criterion together with Gauss's lemma implies that $f$ is irreducible in $\QQ[x]$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
