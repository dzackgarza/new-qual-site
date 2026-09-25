---
schema: qual/card@1
id: P-BKS11-6B
kind: problem
title: Irreducibility of $x^4+x+2011$ over $\mathbb Q$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 5 of the retained Spring 2011 solution PDF and independently reviewed the reduction-mod-2 argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked absence of linear factors and of the unique irreducible quadratic factor over F_2, then applied Gauss's lemma.
---

::: {.problem}
Prove that the polynomial $x ^ { 4 } + x + 2011$ is irreducible over $\mathbb { Q } .$
:::

::: {.solution}
Set
$$
f(x)\coloneqq x^4+x+2011\in\ZZ[x].
$$

<1>1. Modulo $2$, the polynomial $f$ becomes
$$
\overline f(x)=x^4+x+1\in\FF_2[x].
$$

::: {.proof}
Since
$$
2011\equiv1\pmod2,
$$
reducing all coefficients of $f$ modulo $2$ gives the displayed polynomial.
:::

<1>2. The polynomial $\overline f$ has no linear factor over $\FF_2$.

::: {.proof}
The only possible roots are $0$ and $1$. One has
$$
\overline f(0)=1
$$
and
$$
\overline f(1)=1+1+1=1
$$
in $\FF_2$. Hence $\overline f$ has no root and therefore no linear
factor.
:::

<1>3. The polynomial $\overline f$ is not divisible by
$$
q(x)\coloneqq x^2+x+1.
$$

::: {.proof}
The polynomial $q$ is the unique monic irreducible quadratic over
$\FF_2$. Modulo $q$,
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
=
1
\pmod q.
$$
So $q$ does not divide $\overline f$.
:::

<1>4. The polynomial $\overline f$ is irreducible over $\FF_2$.

::: {.proof}
If a quartic over a field is reducible, then either it has a linear factor,
or it factors as a product of two quadratics. Step <1>2 rules out a linear
factor.

If it factors as two quadratics and neither factor has a linear factor,
then both quadratic factors are irreducible. Over $\FF_2$, the only monic
irreducible quadratic is $q=x^2+x+1$, so $q$ would divide
$\overline f$. Step <1>3 rules this out.
:::

<1>5. The polynomial
$$
\boxed{x^4+x+2011}
$$
is irreducible over $\QQ$.

::: {.proof}
The polynomial $f$ is primitive because its leading coefficient is $1$.
If it were reducible over $\QQ$, Gauss's lemma would make it reducible in
$\ZZ[x]$. Since $f$ is monic, the two nonconstant factors can be taken
monic. Their reductions modulo $2$ therefore retain their positive degrees
and give a nontrivial factorization of $\overline f$, contradicting
step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required irreducibility statement.
:::
:::
