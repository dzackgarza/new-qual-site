---
schema: qual/card@1
id: P-ALGFINAL11-03
kind: problem
title: Irreducible but nonprime elements in Z[sqrt(-5)]
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Prove that in $\mathbb { Z } [ { \sqrt { - 5 } } ]$ , 7 is irreducible but not prime.

[10]

(b) Is $\mathbb { Z } [ { \sqrt { - 5 } } ]$ a Principal Ideal Domain?
(Justify your answer.)

[5]
:::

::: {.solution}
Put
$$
R=\ZZ[\sqrt{-5}],
\qquad
N(a+b\sqrt{-5})=a^2+5b^2.
$$

<1>1. The norm is multiplicative, and an element of $R$ is a unit exactly when its norm is $1$.
::: {.proof}
For $x,y\in R$,
$$
N(xy)=xy\overline{xy}=x\bar x\,y\bar y=N(x)N(y).
$$
If $u$ is a unit, then
$$
1=N(1)=N(u)N(u^{-1}),
$$
so $N(u)=1$. Conversely, if $N(u)=1$, then
$$
u\bar u=1,
$$
so $u^{-1}=\bar u\in R$.
:::

<1>2. There is no element of $R$ having norm $7$.
::: {.proof}
If
$$
a^2+5b^2=7
$$
with $a,b\in\ZZ$, then $|b|\le1$. If $b=0$, one gets $a^2=7$, impossible. If $|b|=1$, one gets $a^2=2$, also impossible. Hence no such element exists.
:::

<1>3. The element $7$ is irreducible in $R$.
::: {.proof}
Suppose
$$
7=xy.
$$
Then by step <1>1,
$$
49=N(7)=N(x)N(y).
$$
If neither $x$ nor $y$ were a unit, then step <1>1 would give
$$
N(x)>1,
\qquad
N(y)>1.
$$
Since both norms are positive integers whose product is $49$, one must have
$$
N(x)=N(y)=7,
$$
contradicting step <1>2. Therefore every factorization of $7$ has a unit factor, so $7$ is irreducible.
:::

<1>4. The element $7$ is not prime in $R$.
::: {.proof}
One has
$$
(3+\sqrt{-5})(3-\sqrt{-5})=9+5=14,
$$
so
$$
7\mid(3+\sqrt{-5})(3-\sqrt{-5}).
$$
But $7$ divides neither factor. Indeed, if
$$
3+\sqrt{-5}=7(a+b\sqrt{-5})
$$
with $a,b\in\ZZ$, then comparing coefficients gives
$$
7a=3,
\qquad
7b=1,
$$
impossible; the conjugate factor is identical. Thus $7$ divides a product without dividing either factor, so it is not prime.
:::

<1>5. Therefore
$$
\boxed{R\text{ is not a PID}}.
$$
::: {.proof}
Every PID is a UFD, and in every UFD every irreducible element is prime. Steps <1>3 and <1>4 exhibit an irreducible element of $R$ that is not prime. Hence $R$ cannot be a PID.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>3 and step <1>4 prove part (a), and step <1>5 proves part (b).
:::
:::
