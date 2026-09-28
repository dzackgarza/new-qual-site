---
schema: qual/card@1
id: P-F2Y4F
kind: problem
title: $(\mathbb{Z}/2\mathbb{Z})[y]/(y^4+y^3+y^2+y+1)$ is a field over which $x^4+x+1$
  and $x^2+x+1$ split and $x^3+x+1$ is irreducible
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared all three parts and all four polynomials with June 2012 Fields 3 on PDF page 11."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the exhaustive quadratic-factor obstruction, both divisibilities into x^16-x, splitting over the given quotient field, and the degree-three subfield obstruction."
---

::: {.problem}
a. Prove that $K = (\mathbb{Z}/2\mathbb{Z})[y]/(y^4 + y^3 + y^2 + y + 1)$ is a field.

b. Prove that $x^4 + x + 1$ and $x^2 + x + 1$ factor completely over the field $K$ above.

c. Prove that $x^3 + x + 1$ is irreducible over the field $K$ above.
:::

::: {.solution}
All polynomial computations below are in characteristic two.

<1>1. The polynomial $h(y)=y^4+y^3+y^2+y+1$ is irreducible
over $\mathbb F_2$, so $K$ is a field with $16$ elements.

::: {.proof}
Neither $0$ nor $1$ is a root of $h$, so $h$ has no linear
factor. If it were reducible, its factorization into monic
irreducibles would therefore consist of two quadratics.
The only monic irreducible quadratic over $\mathbb F_2$ is
$q(y)=y^2+y+1$: a root-free monic quadratic must have
constant term one, and of $y^2+1$ and $y^2+y+1$ only the
latter is nonzero at $1$.

Modulo $q$ one has $y^2=y+1$, $y^3=1$, and $y^4=y$.
Consequently $h\equiv y+1\not\equiv0\pmod q$.
Thus no irreducible quadratic divides $h$, proving its
irreducibility. The quotient by an irreducible polynomial
over a field is a field [@DF04]. Polynomial division gives
the basis $1,\bar y,\bar y^2,\bar y^3$ of $K$ over
$\mathbb F_2$, so $[K:\mathbb F_2]=4$ and $|K|=2^4=16$.
:::

<1>2. The polynomial $x^{16}-x$ factors as
$$
x^{16}-x=\prod_{a\in K}(x-a)
$$
in $K[x]$.

::: {.proof}
The multiplicative group $K^\times$ has order $15$, so
Lagrange's theorem gives $a^{15}=1$ for each nonzero $a$
[@DF04]. Hence every $a\in K$, including zero, satisfies
$a^{16}=a$. The sixteen distinct linear factors on the
right therefore divide the monic degree-sixteen polynomial
on the left. Equality follows from their degrees and
leading coefficients.
:::

<1>3. Both polynomials in part (b) divide $x^{16}-x$, and
therefore split completely over $K$.

::: {.proof}
In the quotient $\mathbb F_2[x]/(x^4+x+1)$, write $t$ for
the class of $x$. The identity $t^4=t+1$ gives
$$
t^{16}=(t+1)^4=t^4+1=t.
$$
Here $(u+v)^4=u^4+v^4$ follows by squaring twice in
characteristic two. Thus $x^{16}-x$ belongs to the ideal
$(x^4+x+1)$, which is precisely the required divisibility.

In $\mathbb F_2[x]/(x^2+x+1)$ one has $t^2=t+1$ and
$$
t^4=(t+1)^2=t^2+1=t,
\qquad t^{16}=(t^4)^4=t^4=t.
$$
This proves the other divisibility. Both remain valid in
$K[x]$. By step <1>2, every irreducible factor of a divisor
of $x^{16}-x$ in $K[x]$ is linear: unique factorization in
the Euclidean domain $K[x]$ applies [@DF04]. Thus each
polynomial in part (b) factors completely over the specified
field $K$, not merely over some extension of it.
:::

<1>4. The polynomial $g(x)=x^3+x+1$ is irreducible over $K$.

::: {.proof}
The values $g(0)=g(1)=1$ show that $g$ has no root in
$\mathbb F_2$. A reducible cubic over a field has a linear
factor, so $g$ is irreducible over $\mathbb F_2$.
If $b\in K$ were a root, its minimal polynomial over
$\mathbb F_2$ would be $g$, and $[\mathbb F_2(b):\mathbb F_2]=3$.
The tower law would then imply
$$
4=[K:\mathbb F_2]
 =[K:\mathbb F_2(b)]\,[\mathbb F_2(b):\mathbb F_2]
 =3[K:\mathbb F_2(b)],
$$
which is impossible for a positive integer degree.
Hence $g$ has no root in $K$. Since its degree is three,
it is irreducible over $K$.
:::
:::
