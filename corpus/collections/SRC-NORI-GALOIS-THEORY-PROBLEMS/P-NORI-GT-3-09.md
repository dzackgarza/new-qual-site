---
schema: qual/card@1
id: P-NORI-GT-3-09
kind: problem
title: Quartics of the form $Q^2-cP^2$ and quadratic subfields
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.9 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $f = Q^{2} - cP^{2}$ where $c \in F$ and $P, Q \in F[X]$ with $Q$ monic of degree two and $\deg(P) < 2$. Show that if $g$ is an irreducible monic polynomial of degree $\geq 3$ that divides $f$, then $g = f$.

Show that if $f$ is irreducible, then the field $E = F(\theta)$ obtained by adjoining a root $\theta$ of $f$ necessarily contains a quadratic extension of $F$.
:::

::: {.solution}

Because $Q$ is monic of degree $2$ and $\deg P<2$, the polynomial
$$
f=Q^2-cP^2
$$
is monic of degree $4$.

::: pf

::: {.pf-step #s1-1}

Suppose an irreducible monic polynomial $g$ of degree $3$ divides $f$, and let $\alpha$ be a root of $g$ in an algebraic closure of $F$. Then
$$
P(\alpha)\ne0.
$$


::: pf-proof

If $P(\alpha)=0$, then from
$$
0=f(\alpha)=Q(\alpha)^2-cP(\alpha)^2
$$
one gets $Q(\alpha)=0$. Thus the minimal polynomial $g$ of $\alpha$ over $F$ divides both $P$ and $Q$. But
$$
\deg P<2<3=\deg g
$$
and
$$
\deg Q=2<3,
$$
which is impossible.

:::

:::

::: {.pf-step #s1-2}

Under the hypothesis of step [](#s1-1){.pf-ref}, the field $F(\alpha)$ contains an element $u$ satisfying
$$
u^2=c.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $P(\alpha)\ne0$. Set
$$
u=\frac{Q(\alpha)}{P(\alpha)}\in F(\alpha).
$$
Since $f(\alpha)=0$,
$$
Q(\alpha)^2=cP(\alpha)^2,
$$
and division by $P(\alpha)^2$ gives $u^2=c$.

:::

:::

::: {.pf-step #s1-3}

If $c$ is not a square in $F$, step [](#s1-2){.pf-ref} is impossible.


::: pf-proof

If $c$ is not a square, then $u\notin F$ and the polynomial
$$
X^2-c
$$
has no root in $F$, hence is irreducible of degree $2$. Therefore
$$
[F(u):F]=2.
$$
But
$$
F\subset F(u)\subset F(\alpha),
$$
and
$$
[F(\alpha):F]=\deg g=3.
$$
The tower law would force $2$ to divide $3$, a contradiction.

:::

:::

::: {.pf-step #s1-4}

If $c$ is a square in $F$, no irreducible cubic polynomial can divide $f$.


::: pf-proof

Write
$$
c=d^2
$$
with $d\in F$. Then
$$
f
=Q^2-d^2P^2
=(Q-dP)(Q+dP).
$$
Each factor has degree at most $2$; in fact both have leading term $X^2$ because $Q$ is monic of degree $2$ and $\deg P<2$. Any irreducible factor of this product divides one of the two quadratic factors, so it has degree at most $2$. Thus an irreducible cubic factor cannot occur.

:::

:::

::: {.pf-step #s1-5}

Hence an irreducible monic divisor $g$ of $f$ with $\deg g\ge3$ must have degree $4$, and therefore
$$
\boxed{g=f}.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} rule out degree $3$. Since $f$ has degree $4$, a divisor of degree at least $3$ can only have degree $4$. If monic degree-$4$ polynomials $g$ and $f$ satisfy $g\mid f$, their quotient is a monic constant, necessarily $1$. Thus $g=f$.

:::

:::

::: {.pf-step #s1-6}

Now suppose $f$ is irreducible, let $\theta$ be a root, and set
$$
E=F(\theta).
$$
Then
$$
P(\theta)\ne0.
$$


::: pf-proof

If $P(\theta)=0$, then $f(\theta)=0$ gives $Q(\theta)=0$. The irreducible polynomial $f$, which is the minimal polynomial of $\theta$ and has degree $4$, would then divide $P$ and $Q$, impossible because both have degree less than $4$.

:::

:::

::: {.pf-step #s1-7}

The element
$$
u=\frac{Q(\theta)}{P(\theta)}\in E
$$
satisfies
$$
u^2=c.
$$


::: pf-proof

This is the same calculation as in step [](#s1-2){.pf-ref}, using $f(\theta)=0$ and step [](#s1-6){.pf-ref} to divide by $P(\theta)^2$.

:::

:::

::: {.pf-step #s1-8}

The element $c$ is not a square in $F$.


::: pf-proof

If $c=d^2$ for some $d\in F$, then as in step [](#s1-4){.pf-ref},
$$
f=(Q-dP)(Q+dP)
$$
would be a product of two polynomials of degree $2$, contradicting irreducibility of the quartic $f$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{F(u)\subset E\text{ is a quadratic extension of }F}.
$$


::: pf-proof

By step [](#s1-7){.pf-ref}, $u$ is a root of $X^2-c$. By step [](#s1-8){.pf-ref}, this polynomial has no root in $F$, so it is irreducible of degree $2$. Hence
$$
[F(u):F]=2.
$$
Since $u\in E$, this gives the required quadratic subextension of $E/F$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the first assertion, and step [](#s1-9){.pf-ref} proves that every irreducible quartic of the prescribed form generates an extension containing a quadratic extension of $F$.

:::

:::

:::
