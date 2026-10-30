---
schema: qual/card@1
id: P-JH3BD
kind: problem
title: Factorizations of $x^5-1$, $x^6-1$, and related polynomials over $\CC$,
  $\QQ$, and finite fields
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared all five polynomials and coefficient fields with page 2 of the original scan, Rings 4; corrected the area to algebra."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---
::: {.problem}
Give a complete factorization of each of the following over the indicated rings.
Explain why the factors you obtain are irreducible.

(a) $x^5-1$ over $\CC$.

(b) $x^6-1$ over $\QQ$.

(c) $x^7+3x^5-6x^3+9x-15$ over $\QQ$.

(d) $x^{11}-x$ over $\mathbf{F}_{11}$.

(e) $x^{13}-x-1$ over $\mathbf{F}_{13}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a), if $\zeta=e^{2\pi i/5}$, then over $\CC$,
$$
x^5-1=\boxed{\prod_{j=0}^{4}(x-\zeta^j)}.
$$

::: pf-proof

The numbers $1,\zeta,\zeta^2,\zeta^3,\zeta^4$ are the five distinct roots of
$x^5-1$. Hence the displayed product is a monic degree-$5$ polynomial with
the same roots as $x^5-1$, so the two polynomials are equal. Each factor has
degree $1$, hence is irreducible over the field $\CC$.

:::

:::

::: {.pf-step #s2}

For part (b), over $\QQ$,
$$
x^6-1
=\boxed{(x-1)(x+1)(x^2+x+1)(x^2-x+1)}.
$$

::: pf-proof

The identities
$$
x^6-1=(x^3-1)(x^3+1)
$$
and
$$
x^3-1=(x-1)(x^2+x+1),
\qquad
x^3+1=(x+1)(x^2-x+1)
$$
give the factorization. The linear factors are irreducible. Each quadratic
factor has discriminant $-3$, which is not a square in $\QQ$, so neither has
a root in $\QQ$; therefore both quadratics are irreducible.

:::

:::

::: {.pf-step #s3}

For part (c), the complete factorization over $\QQ$ is the polynomial
itself:
$$
\boxed{x^7+3x^5-6x^3+9x-15}.
$$

::: pf-proof

Eisenstein's criterion applies with $p=3$: every nonleading coefficient is
divisible by $3$, while the constant coefficient $-15$ is not divisible by
$9$. Hence the polynomial is irreducible in $\QQ[x]$ [@DF04].

:::

:::

::: {.pf-step #s4}

For part (d), over $\FF_{11}$,
$$
x^{11}-x
=\boxed{\prod_{a\in\FF_{11}}(x-a)}.
$$

::: pf-proof

For $a\in\FF_{11}^{\times}$, Fermat's theorem gives $a^{10}=1$, so
$a^{11}=a$; the same identity is immediate for $a=0$. Thus every element of
$\FF_{11}$ is a root of $x^{11}-x$. These are $11$ distinct roots of a monic
degree-$11$ polynomial, so their linear factors multiply to the polynomial.
Each linear factor is irreducible over $\FF_{11}$.

:::

:::

::: {.pf-step #s5}

For part (e), $x^{13}-x-1$ is irreducible over $\FF_{13}$, so its
complete factorization is
$$
\boxed{x^{13}-x-1}.
$$

::: pf-proof

Let $\alpha$ be a root in an algebraic closure of $\FF_{13}$ and set
$$
d=[\FF_{13}(\alpha):\FF_{13}].
$$
The minimal polynomial of $\alpha$ divides $x^{13}-x-1$, hence
$1\le d\le13$. Since
$$
\alpha^{13}=\alpha+1,
$$
induction using the Frobenius homomorphism in characteristic $13$ gives
$$
\alpha^{13^j}=\alpha+j
\qquad(j\ge0),
$$
where $j$ denotes its image in the prime field. The field
$\FF_{13}(\alpha)$ has $13^d$ elements, so
$$
\alpha^{13^d}=\alpha.
$$
Taking $j=d$ in the preceding formula yields $d=0$ in $\FF_{13}$, hence
$13\mid d$. Because $1\le d\le13$, one has $d=13$. Therefore the minimal
polynomial of $\alpha$ has degree $13$ and divides the monic degree-$13$
polynomial $x^{13}-x-1$; the two polynomials are equal.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} give the complete factorizations and irreducibility
justifications required in parts (a)--(e).

:::

:::

:::
