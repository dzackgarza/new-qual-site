---
schema: qual/card@1
id: P-AGH264DOUBLECOVER
kind: problem
title: Integral closedness of a square-root extension
classification:
  areas:
  - algebraic-geometry
  topics:
  - Integral Closure
  - Normal Rings
  - Galois Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read Exercise II.6.4 and its full hint in the Hartshorne transcription. Corrected the source's minimal-polynomial assertion at h=0 and retained the arbitrary field of characteristic different from two.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be a field of characteristic different from two, put $R=k[x_1,\ldots,x_n]$, and let $f\in R$ be square-free and nonconstant.
Thus no irreducible factor occurs more than once in the factorization of $f$.
Let $A=R[z]/(z^2-f)$.
Show that $A$ is an integrally closed domain and is the integral closure of $R$ in its fraction field $K$.
:::

::: {.hint}
Put $F=k(x_1,\ldots,x_n)$.
First show that $K=F[z]/(z^2-f)$ is a quadratic Galois extension of $F$, with nontrivial automorphism $\sigma(z)=-z$.
For $\alpha=g+hz\in K$, with $g,h\in F$, the polynomial
$$
T^2-2gT+(g^2-h^2f)
$$
annihilates $\alpha$; it is the minimal polynomial when $h\ne0$.
Show that $\alpha$ is integral over $R$ if and only if $g,h\in R$.
:::

::: {.solution}
For an irreducible polynomial $q\in R$ and $u\in F^\times$, let $v_q(u)$ be the exponent of $q$ in the numerator of a reduced fraction for $u$, minus its exponent in the denominator.
The ring $R$ is a [[D-INULL|unique factorization domain]] by [[FT-OXN3Y|Gauss's lemma]], and is therefore integrally closed [@Har10a, proof of Proposition II.6.2].

::: pf

::: {.pf-step #s1}

The ring $A$ is a domain with fraction field $K=F(z)$, where $[K:F]=2$ and $\sigma(z)=-z$ generates its Galois group.

::: pf-proof

Because $f$ is nonconstant and square-free, it has an irreducible factor $q$ with $v_q(f)=1$.
Every square in $F^\times$ has even $q$-valuation, so $f$ is not a square in $F$.
The quadratic $T^2-f$ is consequently irreducible over $F$.

Division by this monic polynomial gives $A=R\oplus Rz$ as an $R$-module.
The natural map $A\to F[T]/(T^2-f)$ is injective, since $1,z$ are linearly independent over $F$ in the target field.
It follows that $A$ is a domain, and its fraction field is $K=F(z)$.
The roots $z,-z$ are distinct because $f\ne0$ and $\operatorname{char}k\ne2$.
They both lie in $K$, so $K/F$ is Galois of degree two with the asserted nontrivial automorphism.

:::

:::

::: {.pf-step #s2}

If $\alpha=g+hz\in K$ is integral over $R$, then $g,h\in R$.

::: pf-proof

The automorphism $\sigma$ fixes $R$, so $\sigma(\alpha)=g-hz$ satisfies the same monic equation over $R$ as $\alpha$.
Thus it is integral as well.
The sum and product of these two integral elements are integral: the ring $R[\alpha,\sigma(\alpha)]$ is a finite $R$-module, and the determinant trick applied to multiplication by their sum or product gives a monic equation for that element.
Consequently
$$
\alpha+\sigma(\alpha)=2g,\qquad
\alpha\sigma(\alpha)=g^2-h^2f
$$
are integral over $R$.
Both belong to $F$, so integral closedness of $R$ implies $2g,g^2-h^2f\in R$.
Since $2$ is a unit in $R$, we obtain $g\in R$ and $h^2f\in R$.

If $h=0$, the conclusion for $h$ holds.
If $h\ne0$, then for every irreducible $q\in R$,
$$
2v_q(h)+v_q(f)=v_q(h^2f)\ge0.
$$
Square-freeness gives $v_q(f)\in\{0,1\}$, and $v_q(h)$ is an integer, so $v_q(h)\ge0$.
A reduced fraction for $h$ therefore has no irreducible factor in its denominator.
Its denominator is a unit, and $h\in R$.

:::

:::

::: {.pf-step #s3}

The integral closure of $R$ in $K$ is $A$, and $A$ is integrally closed.

::: pf-proof

If $g,h\in R$, then direct substitution shows that $g+hz$ satisfies the monic equation
$$
T^2-2gT+(g^2-h^2f)=0.
$$
It is therefore integral over $R$.
Together with step [](#s2){.pf-ref}, this proves
$$
\boxed{\{\alpha\in K:\alpha\text{ is integral over }R\}=R\oplus Rz=A}.
$$

Now let $\beta\in K$ be integral over $A$.
The module $A[\beta]$ is finite over $A$, and $A$ is finite over $R$ by step [](#s1){.pf-ref}.
Hence $A[\beta]$ is a finite $R$-module containing $1$.
The determinant trick for multiplication by $\beta$ gives a monic equation over $R$, so $\beta$ is integral over $R$ and belongs to $A$ by the displayed equality.
Thus $A$ is [[D-QJ5M9|integrally closed]] in $K$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} supplies the domain and its fraction field, and step [](#s3){.pf-ref} proves both requested integral-closure assertions.

:::

:::

:::

::: {.remark title="The polynomial in the hint"}
For $h\ne0$, the element $g+hz$ generates $K$ over $F$, since $z=((g+hz)-g)/h$.
Its minimal polynomial is therefore the quadratic displayed in the hint.
For $h=0$, the minimal polynomial is instead $T-g$, whereas that quadratic is $(T-g)^2$.
The source calls the quadratic minimal without excluding $h=0$ [@Har10a, Exercise II.6.4].
:::
