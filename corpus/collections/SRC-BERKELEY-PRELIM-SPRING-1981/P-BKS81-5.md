---
schema: qual/card@1
id: P-BKS81-5
kind: problem
title: Irreducible factorizations of $x^4-4$ and $x^3-2$ over $\mathbb R$, $\mathbb Z$, and $\mathbb Z/3\mathbb Z$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked each displayed factorization and the irreducibility of every remaining quadratic or cubic factor over the stated coefficient ring.
---

::: {.problem}
Decompose
\[
x^4-4
\qquad\text{and}\qquad
x^3-2
\]
into irreducible factors over $\mathbb R$, over $\mathbb Z$, and over $\mathbb Z/3\mathbb Z$.
:::

::: {.solution}
::: pf

::: {.pf-step #factorizations-over-r}
Over $\RR$, the irreducible factorizations are
$$
\boxed{
x^4-4
=(x-\sqrt2)(x+\sqrt2)(x^2+2)
}
$$
and
$$
\boxed{
x^3-2
=(x-\sqrt[3]{2})
\bigl(x^2+\sqrt[3]{2}\,x+\sqrt[3]{4}\bigr).
}
$$

::: pf-proof
The first identity follows from
$$
x^4-4=(x^2-2)(x^2+2).
$$
The factor $x^2+2$ has no real root, hence is irreducible over $\RR$.

For the second identity, put $a=\sqrt[3]{2}$ and use
$$
x^3-a^3=(x-a)(x^2+ax+a^2).
$$
The quadratic factor has discriminant
$$
a^2-4a^2=-3a^2<0,
$$
so it is irreducible over $\RR$.
:::

:::

::: {.pf-step #factorizations-over-z}
Over $\ZZ$, the irreducible factorizations are
$$
\boxed{
x^4-4=(x^2-2)(x^2+2)
}
$$
and
$$
\boxed{x^3-2\text{ is irreducible}.}
$$

::: pf-proof
Both quadratic factors of $x^4-4$ are primitive. Neither has a rational
root, so neither factors into linear polynomials over $\QQ$; by Gauss's
lemma they are irreducible in $\ZZ[x]$.

The polynomial $x^3-2$ is Eisenstein at the prime $2$: the prime $2$
divides every nonleading coefficient, while $4$ does not divide the
constant term $-2$. Hence it is irreducible in $\ZZ[x]$.
:::

:::

::: {.pf-step #factorizations-over-z3}
Over $\ZZ/3\ZZ$, the irreducible factorizations are
$$
\boxed{
x^4-4=(x-1)(x+1)(x^2+1)
}
$$
and
$$
\boxed{
x^3-2=(x+1)^3.
}
$$

::: pf-proof
Modulo $3$,
$$
x^4-4=x^4-1=(x-1)(x+1)(x^2+1).
$$
The polynomial $x^2+1$ has no root in $\ZZ/3\ZZ$, since its values at
$0,1,2$ are $1,2,2$, respectively. A quadratic over a field is reducible
exactly when it has a root, so $x^2+1$ is irreducible.

Also $-2=1$ in $\ZZ/3\ZZ$, and the binomial coefficients $3$ vanish there.
Thus
$$
x^3-2=x^3+1=(x+1)^3.
$$
The factor $x+1$ is linear and therefore irreducible.
:::

:::

::: pf-qed
Steps [](#factorizations-over-r){.pf-ref}, [](#factorizations-over-z){.pf-ref}, and [](#factorizations-over-z3){.pf-ref} give the complete irreducible decompositions over all
three requested coefficient rings.
:::

:::
:::
