---
schema: qual/card@1
id: P-KSRING17-008
kind: problem
title: Primes $p\equiv 1 \pmod 4$ are sums of two squares
classification:
  areas: [algebra]
  topics:
  - Sums of Two Squares
  - Gaussian Integers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
If p is a prime satisfying $p \equiv 1$ (mod 4), then p is a sum of two squares.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There exists an integer $a$ such that
$$
a^2\equiv-1\pmod p.
$$


::: pf-proof

Write
$$
p=4m+1.
$$
Wilson's theorem gives
$$
(p-1)!\equiv-1\pmod p.
$$
Pair the factors $k$ and $p-k$ for
$$
1\le k\le\frac{p-1}{2}.
$$
Then
$$
\begin{aligned}
(p-1)!
&=
\prod_{k=1}^{(p-1)/2}
k(p-k)\\
&\equiv
(-1)^{(p-1)/2}
\left(
\left(\frac{p-1}{2}\right)!
\right)^2
\pmod p.
\end{aligned}
$$
Since
$$
\frac{p-1}{2}=2m
$$
is even,
$$
\left(
\left(\frac{p-1}{2}\right)!
\right)^2
\equiv
-1
\pmod p.
$$
Thus one may take
$$
a
\coloneqq
\left(\frac{p-1}{2}\right)!.
$$

:::

:::

::: {.pf-step #s1-2}

The element $p$ is not prime in the Gaussian integer ring
$$
\ZZ[i].
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
p
\mid
a^2+1
=
(a+i)(a-i)
$$
in $\ZZ[i]$.

However,
$$
p\nmid a+i.
$$
Indeed, if
$$
a+i
=
p(x+iy),
$$
then comparison of imaginary parts would give
$$
1=py,
$$
impossible in $\ZZ$. Similarly,
$$
p\nmid a-i.
$$
Thus $p$ divides a product without dividing either factor, so it is not a prime element of $\ZZ[i]$.

:::

:::

::: {.pf-step #s1-3}

The element $p$ is reducible in $\ZZ[i]$.


::: pf-proof

The Gaussian integers form a Euclidean domain with Euclidean function
$$
N(x+iy)
\coloneqq
x^2+y^2.
$$
Hence $\ZZ[i]$ is a UFD, and in a UFD every irreducible element is prime.

Step [](#s1-2){.pf-ref} shows that $p$ is not prime. Therefore $p$ cannot be irreducible. Since $p$ is neither zero nor a unit, it is reducible:
$$
p=\alpha\beta
$$
for nonunits
$$
\alpha,\beta\in\ZZ[i].
$$

:::

:::

::: {.pf-step #s1-4}

One of the factors in step [](#s1-3){.pf-ref} has Gaussian norm exactly $p$.


::: pf-proof

Taking norms in
$$
p=\alpha\beta
$$
gives
$$
p^2
=
N(p)
=
N(\alpha)N(\beta).
$$
Since $\alpha$ and $\beta$ are nonunits,
$$
N(\alpha)>1,
\qquad
N(\beta)>1.
$$
Both norms are positive integers dividing $p^2$. Since $p$ is prime, the only possibility is
$$
N(\alpha)=N(\beta)=p.
$$

:::

:::

::: {.pf-step #s1-5}

Hence $p$ is a sum of two squares.


::: pf-proof

Write
$$
\alpha=x+iy
$$
with
$$
x,y\in\ZZ.
$$
By step [](#s1-4){.pf-ref},
$$
p
=
N(\alpha)
=
x^2+y^2.
$$
Therefore
$$
\boxed{
p=x^2+y^2
}
$$
for integers $x,y$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
