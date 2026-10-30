---
schema: qual/card@1
id: P-KSRING17-103
kind: problem
title: A generalized Eisenstein criterion for a factor of degree at least $k$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 103 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source requires $p\mid a_i$ only for $i=1,\ldots,k-1$, which $x^2-1$, $p=2$, $k=2$ satisfies with two linear factors. The statement now requires $p\mid a_i$ for $i=0,\ldots,k-1$.
---

::: {.problem}
Let $f(x) = a_{0} + a_{1}x + \cdots + a_{k}x^{k} + \cdots + a_{n}x^{n} \in \ZZ[x]$ and $p$ a prime such that $p \divides a_{i}$ for $i = 0, \ldots, k - 1$, $p \nmid a_{k}$, $p \nmid a_{n}$, and $p^{2} \nmid a_{0}$. Show that $f(x)$ has an irreducible factor in $\ZZ[x]$ of degree at least $k$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The coefficient $a_0$ is nonzero and satisfies
$$
v_p(a_0)=1.
$$

::: pf-proof

One has
$$
p\mid a_0
$$
and
$$
p^2\nmid a_0.
$$
Therefore $a_0\ne0$ and the exact $p$-adic exponent of $a_0$ is $1$.

:::

:::

::: {.pf-step #s1-2}

Factor $f$ in $\ZZ[x]$ as
$$
f
=
c\,f_1f_2\cdots f_r,
$$
where
$$
c\in\ZZ\setminus\{0\}
$$
and each $f_j$ is primitive and irreducible of positive degree.

::: pf-proof

Apply Gauss's lemma and unique factorization in
$$
\ZZ[x].
$$
Any integer content is absorbed into $c$.

:::

:::

::: {.pf-step #s1-3}

The integer $c$ is not divisible by $p$.

::: pf-proof

If
$$
p\mid c,
$$
then every coefficient of
$$
f
$$
would be divisible by $p$.
In particular,
$$
p\mid a_n,
$$
contradicting the hypothesis
$$
p\nmid a_n.
$$
Thus
$$
p\nmid c.
$$

:::

:::

::: {.pf-step #s1-4}

Exactly one irreducible factor $f_j$ has constant coefficient divisible by $p$.

::: pf-proof

Write
$$
f_j(x)
=
b_{j,0}
+
b_{j,1}x
+
\cdots.
$$
Taking constant coefficients in the factorization from step [](#s1-2){.pf-ref} gives
$$
a_0
=
c
\prod_{j=1}^{r}
b_{j,0}.
$$
By step [](#s1-1){.pf-ref},
$$
v_p(a_0)=1,
$$
and by step [](#s1-3){.pf-ref},
$$
v_p(c)=0.
$$
Therefore
$$
\sum_{j=1}^{r}
v_p(b_{j,0})
=
1.
$$
All terms are nonnegative integers, so exactly one index, say
$$
j=j_0,
$$
satisfies
$$
v_p(b_{j_0,0})=1,
$$
and every other constant coefficient is prime to $p$.

:::

:::

::: {.pf-step #s1-5}

Reduce the factorization modulo $p$.
Then
$$
\overline f(x)
=
x^k h(x)
$$
for some
$$
h(x)\in\FF_p[x]
$$
with
$$
h(0)\ne0.
$$

::: pf-proof

By hypothesis,
$$
p\mid a_0,\ldots,a_{k-1},
$$
while
$$
p\nmid a_k.
$$
Thus the reduction
$$
\overline f(x)
$$
has zero coefficients in degrees
$$
0,1,\ldots,k-1,
$$
and nonzero coefficient in degree $k$.
Hence its exact order of vanishing at
$$
x=0
$$
is $k$.
Equivalently,
$$
\overline f(x)
=
x^k h(x)
$$
with
$$
h(0)\ne0.
$$

:::

:::

::: {.pf-step #s1-6}

For every
$$
j\ne j_0,
$$
the reduction
$$
\overline{f_j}(x)
$$
is not divisible by $x$.

::: pf-proof

By step [](#s1-4){.pf-ref},
$$
p\nmid b_{j,0}
$$
for
$$
j\ne j_0.
$$
Thus the constant term of
$$
\overline{f_j}
$$
is nonzero.
Therefore
$$
x\nmid\overline{f_j}(x).
$$

:::

:::

::: {.pf-step #s1-7}

The reduction
$$
\overline{f_{j_0}}(x)
$$
is nonzero.

::: pf-proof

The polynomial
$$
f_{j_0}
$$
is primitive.
If every coefficient of $f_{j_0}$ were divisible by $p$, its content would be divisible by $p$, contradicting primitivity.
Therefore at least one coefficient survives modulo $p$, so
$$
\overline{f_{j_0}}\ne0.
$$

:::

:::

::: {.pf-step #s1-8}

All $k$ powers of $x$ dividing $\overline f$ come from
$$
\overline{f_{j_0}}.
$$
Hence
$$
x^k
\mid
\overline{f_{j_0}}(x).
$$

::: pf-proof

Reducing the factorization from step [](#s1-2){.pf-ref} modulo $p$ gives
$$
\overline f
=
\overline c
\prod_{j=1}^{r}
\overline{f_j},
$$
where
$$
\overline c\ne0
$$
by step [](#s1-3){.pf-ref}.

By step [](#s1-6){.pf-ref}, every factor except
$$
\overline{f_{j_0}}
$$
has nonzero constant term and therefore contributes zero to the order of vanishing at
$$
x=0.
$$
Step [](#s1-5){.pf-ref} says the total order of vanishing of
$$
\overline f
$$
is exactly $k$.
Thus
$$
\overline{f_{j_0}}
$$
must itself vanish to order $k$ at $0$.
Equivalently,
$$
x^k
\mid
\overline{f_{j_0}}.
$$

:::

:::

::: {.pf-step #s1-9}

One has
$$
\deg f_{j_0}\ge k.
$$

::: pf-proof

By step [](#s1-7){.pf-ref},
$$
\overline{f_{j_0}}
$$
is a nonzero polynomial.
By step [](#s1-8){.pf-ref},
$$
x^k
\mid
\overline{f_{j_0}}.
$$
Therefore
$$
\deg\overline{f_{j_0}}
\ge
k.
$$
Reduction modulo $p$ cannot increase degree, so
$$
\deg f_{j_0}
\ge
\deg\overline{f_{j_0}}
\ge
k.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore $f$ has an irreducible factor of degree at least $k$.

::: pf-proof

The factor
$$
f_{j_0}
$$
is irreducible by step [](#s1-2){.pf-ref}, and step [](#s1-9){.pf-ref} gives
$$
\deg f_{j_0}\ge k.
$$
Thus
$$
\boxed{
f
\text{ has an irreducible factor in }\ZZ[x]
\text{ of degree at least }k.
}
$$

:::

:::

:::

:::
