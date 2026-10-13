---
schema: qual/card@1
id: P-KSRING17-080
kind: problem
title: $\mathbb Z[\sqrt p]$ is not a UFD when $p=b^2+4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 80 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if p is a prime such that there is an integer b with $p = b ^ { 2 } + 4$ , then $\mathbb { Z } [ { \sqrt { p } } ]$ is not a unique factorization domain.
:::

::: {.solution}
Set
$$
R
\coloneqq
\ZZ[\sqrt p].
$$
For
$$
\alpha=a+c\sqrt p\in R,
$$
define
$$
N(\alpha)
\coloneqq
(a+c\sqrt p)(a-c\sqrt p)
=
a^2-pc^2.
$$

<1>1. The norm is multiplicative:
$$
N(\alpha\beta)
=
N(\alpha)N(\beta).
$$

::: {.proof}
Let
$$
\overline{\alpha}
$$
denote the conjugate obtained by replacing
$$
\sqrt p
$$
with
$$
-\sqrt p.
$$
Then
$$
N(\alpha)
=
\alpha\overline\alpha.
$$
Hence
$$
\begin{aligned}
N(\alpha\beta)
&=
\alpha\beta\,
\overline{\alpha\beta}\\
&=
\alpha\beta\,
\overline\alpha\,\overline\beta\\
&=
(\alpha\overline\alpha)
(\beta\overline\beta)\\
&=
N(\alpha)N(\beta).
\end{aligned}
$$
:::

<1>2. If
$$
u\in R
$$
is a unit, then
$$
N(u)=\pm1.
$$

::: {.proof}
If
$$
uv=1
$$
for some
$$
v\in R,
$$
then by step <1>1,
$$
N(u)N(v)
=
N(1)
=
1.
$$
Both norms are integers, so
$$
N(u)=\pm1.
$$
:::

<1>3. The integer $b$ is odd and
$$
p\equiv5\pmod8.
$$

::: {.proof}
If
$$
b
$$
were even, then
$$
b^2+4
$$
would be divisible by $4$, so it could not be prime.
Thus $b$ is odd.

Every odd square is congruent to
$$
1
\pmod8.
$$
Therefore
$$
p
=
b^2+4
\equiv
1+4
\equiv
5
\pmod8.
$$
:::

<1>4. There is no element
$$
\alpha\in R
$$
with
$$
N(\alpha)=2
\quad\text{or}\quad
N(\alpha)=-2.
$$

::: {.proof}
Suppose
$$
\alpha=a+c\sqrt p
$$
and
$$
a^2-pc^2=\pm2.
$$

If
$$
c
$$
is even, then modulo $4$,
$$
pc^2\equiv0,
$$
so
$$
a^2\equiv2\pmod4
$$
in either the $+2$ or $-2$ case, since
$$
-2\equiv2\pmod4.
$$
But a square modulo $4$ is only $0$ or $1$.
This is impossible.

If
$$
c
$$
is odd, then
$$
c^2\equiv1\pmod8.
$$
By step <1>3,
$$
p\equiv5\pmod8.
$$
Thus
$$
pc^2\equiv5\pmod8.
$$

If
$$
a^2-pc^2=2,
$$
then
$$
a^2\equiv7\pmod8.
$$
If
$$
a^2-pc^2=-2,
$$
then
$$
a^2\equiv3\pmod8.
$$
Neither $3$ nor $7$ is a square modulo $8$.
Again this is impossible.

Therefore no element of $R$ has norm $\pm2$.
:::

<1>5. The element
$$
2\in R
$$
is irreducible.

::: {.proof}
Suppose
$$
2=\alpha\beta
$$
in $R$.
Taking norms gives
$$
4
=
N(2)
=
N(\alpha)N(\beta).
$$

If neither
$$
\alpha
$$
nor
$$
\beta
$$
is a unit, then by step <1>2 neither norm is $\pm1$.
Since
$$
\alpha,\beta\ne0
$$
in the domain $R$, their norms are nonzero integers.
Thus
$$
\abs{N(\alpha)},
\abs{N(\beta)}
\ge2.
$$
Because their product has absolute value $4$, one must have
$$
\abs{N(\alpha)}
=
\abs{N(\beta)}
=
2.
$$
This contradicts step <1>4.

Hence every factorization
$$
2=\alpha\beta
$$
has a unit factor.
Therefore
$$
\boxed{2\text{ is irreducible}.}
$$
:::

<1>6. One has
$$
(b+\sqrt p)(b-\sqrt p)
=
-4.
$$

::: {.proof}
Compute
$$
\begin{aligned}
(b+\sqrt p)(b-\sqrt p)
&=
b^2-p\\
&=
b^2-(b^2+4)\\
&=
-4.
\end{aligned}
$$
:::

<1>7. The element
$$
2
$$
divides
$$
(b+\sqrt p)(b-\sqrt p).
$$

::: {.proof}
By step <1>6,
$$
(b+\sqrt p)(b-\sqrt p)
=
-4
=
2(-2).
$$
Hence
$$
2
\mid
(b+\sqrt p)(b-\sqrt p).
$$
:::

<1>8. The element
$$
2
$$
divides neither
$$
b+\sqrt p
$$
nor
$$
b-\sqrt p.
$$

::: {.proof}
Suppose
$$
b+\sqrt p
=
2(a+c\sqrt p)
$$
for integers
$$
a,c.
$$
Comparing coefficients of
$$
1
$$
and
$$
\sqrt p
$$
gives
$$
b=2a
$$
and
$$
1=2c,
$$
impossible.
Thus
$$
2\nmid b+\sqrt p.
$$

Likewise, if
$$
b-\sqrt p
=
2(a+c\sqrt p),
$$
comparison of the
$$
\sqrt p
$$
coefficient gives
$$
-1=2c,
$$
again impossible.
Hence
$$
2\nmid b-\sqrt p.
$$
:::

<1>9. Therefore
$$
2
$$
is irreducible but not prime in $R$.

::: {.proof}
Irreducibility is step <1>5.
Steps <1>7--<1>8 show that $2$ divides a product without dividing either factor.
Thus $2$ is not prime.
:::

<1>10. Hence
$$
\boxed{
\ZZ[\sqrt p]
\text{ is not a unique factorization domain}.
}
$$

::: {.proof}
In a UFD, every irreducible element is prime.
Step <1>9 exhibits an irreducible element of $R$ that is not prime.
Therefore $R$ cannot be a UFD.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required conclusion.
:::
:::
