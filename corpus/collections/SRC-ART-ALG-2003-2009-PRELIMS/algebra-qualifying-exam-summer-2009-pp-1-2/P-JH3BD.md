---
schema: qual/card@1
id: P-JH3BD
kind: problem
title: Factorizations of $x^5-1$, $x^6-1$, and related polynomials over $\mathbf{C}$,
  $\mathbf{Q}$, and finite fields
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

a. $x^5-1$ over $\mathbf{C}$.

b. $x^6-1$ over $\mathbf{Q}$.

c. $x^7+3x^5-6x^3+9x-15$ over $\mathbf{Q}$.

d. $x^{11}-x$ over $\mathbf{F}_{11}$.

e. $x^{13}-x-1$ over $\mathbf{F}_{13}$.
:::

::: solution
<1>1. Over $\mathbf C$, with $\zeta=e^{2\pi i/5}$, the factorization is
$$
x^5-1=\prod_{j=0}^{4}(x-\zeta^j).
$$

::: proof
The five numbers $\zeta^j$ are distinct and each has fifth power $1$.
Thus the product of their linear factors divides $x^5-1$; both polynomials
are monic of degree $5$, so they are equal. A polynomial of degree $1$
over a field cannot be a product of two positive-degree polynomials, so
every displayed factor is irreducible.
:::

<1>2. Over $\mathbf Q$, the factorization is
$$
x^6-1=(x-1)(x+1)(x^2+x+1)(x^2-x+1).
$$

::: proof
Factor $x^6-1=(x^3-1)(x^3+1)$ and use the sum and difference of cubes.
The linear factors are irreducible. The two quadratic factors have
discriminant $-3$, so neither has a rational root. A reducible quadratic
over a field has a linear factor and hence a root, proving their
irreducibility.
:::

<1>3. The polynomial $x^7+3x^5-6x^3+9x-15$ is itself irreducible over
$\mathbf Q$, so there are no further factors.

::: proof
Its leading coefficient is $1$, all other coefficients are divisible by
$3$, and its constant coefficient is not divisible by $9$. Here is the
Eisenstein argument in this case. By Gauss's lemma, a proper factorization
over $\mathbf Q$ would give monic positive-degree factors $g,h\in\mathbf Z[x]$
[@DF04]. Modulo $3$, their product is $x^7$, so each reduction is a
positive power of $x$. Consequently $3$ divides both $g(0)$ and $h(0)$,
forcing $9\mid g(0)h(0)=-15$, a contradiction.
:::

<1>4. Over $\mathbf F_{11}$, the factorization is
$$
x^{11}-x=\prod_{a\in\mathbf F_{11}}(x-a).
$$

::: proof
Every nonzero $a$ belongs to the multiplicative group of order $10$, so
$a^{10}=1$ and $a^{11}=a$. The identity also holds at $a=0$. Thus the
eleven distinct field elements give eleven distinct linear factors of
the monic degree-$11$ polynomial. Their product is the polynomial, and
each factor is irreducible.
:::

<1>5. The polynomial $x^{13}-x-1$ is irreducible over $\mathbf F_{13}$.

::: proof
Choose a root $\alpha$ in an algebraic closure, and let
$d=[\mathbf F_{13}(\alpha):\mathbf F_{13}]$. Its minimal polynomial divides
the given polynomial, so $1\leq d\leq13$. The root equation gives
$\alpha^{13}=\alpha+1$. Induction, using the Frobenius homomorphism in
characteristic $13$, gives
$$
\alpha^{13^j}=\alpha+j\cdot1\qquad(j\geq0).
$$
The field $\mathbf F_{13}(\alpha)$ has $13^d$ elements, so every element
of it satisfies $z^{13^d}=z$. Taking $j=d$ in the displayed identity
therefore gives $d\cdot1=0$, and hence $13\mid d$. Thus $d=13$.
The degree-$13$ minimal polynomial divides the monic polynomial
$x^{13}-x-1$ of the same degree, so they are equal. This proves
irreducibility and completes all five factorizations.
:::
:::
