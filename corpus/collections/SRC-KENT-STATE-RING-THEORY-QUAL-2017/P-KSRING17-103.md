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
---

::: {.problem}
Let $f ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { k } x ^ { k } + \cdots + a _ { n } x ^ { n } \in \mathbb { Z } [ x ]$ and p a prime such that $p | a _ { i }$ for $i = 1 , \ldots , k - 1 , p \nmid a _ { k } , p \nmid a _ { n }$ , and $p ^ { 2 } \nmid a _ { 0 }$ . Show that $f ( x )$ has an irreducible factor in $\mathbb { Z } [ x ]$ of degree at least k.
:::

::: {.remark}
Erratum: the statement also needs
$$
p\mid a_0.
$$
Without this hypothesis the claim is false; for example,
$$
f(x)=x^2-1,
\qquad
p=2,
\qquad
k=2
$$
satisfies the printed conditions but factors into two linear factors.
The proof below uses the intended hypotheses
$$
p\mid a_i
\quad
(0\le i\le k-1),
\qquad
p\nmid a_k,
\qquad
p\nmid a_n,
\qquad
p^2\nmid a_0.
$$
:::

::: {.solution}
Assume the corrected hypotheses.

<1>1. The coefficient $a_0$ is nonzero and satisfies
$$
v_p(a_0)=1.
$$

::: {.proof}
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

<1>2. Factor $f$ in $\ZZ[x]$ as
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

::: {.proof}
Apply Gauss's lemma and unique factorization in
$$
\ZZ[x].
$$
Any integer content is absorbed into $c$.
:::

<1>3. The integer $c$ is not divisible by $p$.

::: {.proof}
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

<1>4. Exactly one irreducible factor $f_j$ has constant coefficient divisible by $p$.

::: {.proof}
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
Taking constant coefficients in the factorization from step <1>2 gives
$$
a_0
=
c
\prod_{j=1}^{r}
b_{j,0}.
$$
By step <1>1,
$$
v_p(a_0)=1,
$$
and by step <1>3,
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

<1>5. Reduce the factorization modulo $p$.
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

::: {.proof}
By the corrected hypotheses,
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

<1>6. For every
$$
j\ne j_0,
$$
the reduction
$$
\overline{f_j}(x)
$$
is not divisible by $x$.

::: {.proof}
By step <1>4,
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

<1>7. The reduction
$$
\overline{f_{j_0}}(x)
$$
is nonzero.

::: {.proof}
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

<1>8. All $k$ powers of $x$ dividing $\overline f$ come from
$$
\overline{f_{j_0}}.
$$
Hence
$$
x^k
\mid
\overline{f_{j_0}}(x).
$$

::: {.proof}
Reducing the factorization from step <1>2 modulo $p$ gives
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
by step <1>3.

By step <1>6, every factor except
$$
\overline{f_{j_0}}
$$
has nonzero constant term and therefore contributes zero to the order of vanishing at
$$
x=0.
$$
Step <1>5 says the total order of vanishing of
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

<1>9. One has
$$
\deg f_{j_0}\ge k.
$$

::: {.proof}
By step <1>7,
$$
\overline{f_{j_0}}
$$
is a nonzero polynomial.
By step <1>8,
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

<1>10. Therefore $f$ has an irreducible factor of degree at least $k$.

::: {.proof}
The factor
$$
f_{j_0}
$$
is irreducible by step <1>2, and step <1>9 gives
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

<1>11. Q.E.D.

::: {.proof}
Step <1>10 proves the corrected generalized Eisenstein criterion.
:::
:::
