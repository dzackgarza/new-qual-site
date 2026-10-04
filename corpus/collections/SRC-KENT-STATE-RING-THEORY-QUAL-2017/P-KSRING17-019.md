---
schema: qual/card@1
id: P-KSRING17-019
kind: problem
title: Chinese remainder theorem for $\mathbb Z_{mn}\cong\mathbb Z_m\times\mathbb Z_n$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 19 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let m and n be relatively prime integers.

(a) Show that if c and d are any integers, then there is an integer x such that $x \equiv c ( \mathrm { m o d } m )$ and $x \equiv d ( \mathrm { m o d } n )$

(b) Show that $\mathbb { Z } _ { m n }$ and $\mathbb { Z } _ { m } \times \mathbb { Z } _ { n }$ are isomorphic as rings.
:::

::: {.solution}
Since
$$
\gcd(m,n)=1,
$$
Bézout's identity gives integers
$$
u,v
$$
such that
$$
um+vn=1.
$$

<1>1. For arbitrary integers $c,d$, define
$$
x
\coloneqq
dum+cvn.
$$
Then
$$
x\equiv c\pmod m
\qquad\text{and}\qquad
x\equiv d\pmod n.
$$

::: {.proof}
Modulo $m$,
$$
um\equiv0,
$$
while
$$
vn
\equiv
1
\pmod m
$$
because
$$
um+vn=1.
$$
Therefore
$$
x
=
dum+cvn
\equiv
c
\pmod m.
$$

Similarly, modulo $n$,
$$
vn\equiv0
$$
and
$$
um\equiv1,
$$
so
$$
x
\equiv
d
\pmod n.
$$
:::

<1>2. Define
$$
\Phi:\ZZ\to\ZZ/m\ZZ\times\ZZ/n\ZZ
$$
by
$$
\Phi(a)
\coloneqq
(a+(m),a+(n)).
$$
Then $\Phi$ is a ring homomorphism.

::: {.proof}
Reduction modulo an ideal preserves addition, multiplication, and identity. Hence each coordinate map
$$
\ZZ\to\ZZ/m\ZZ
$$
and
$$
\ZZ\to\ZZ/n\ZZ
$$
is a ring homomorphism, and therefore their product $\Phi$ is one as well.
:::

<1>3. The map $\Phi$ is surjective.

::: {.proof}
Let
$$
(c+(m),d+(n))
\in
\ZZ/m\ZZ\times\ZZ/n\ZZ
$$
be arbitrary. By step <1>1, there exists an integer $x$ with
$$
x\equiv c\pmod m,
\qquad
x\equiv d\pmod n.
$$
Hence
$$
\Phi(x)
=
(c+(m),d+(n)).
$$
Thus $\Phi$ is surjective.
:::

<1>4. The kernel of $\Phi$ is
$$
(mn).
$$

::: {.proof}
An integer $a$ lies in $\ker\Phi$ exactly when
$$
m\mid a
\qquad\text{and}\qquad
n\mid a.
$$
Because $\gcd(m,n)=1$, these two divisibilities are equivalent to
$$
mn\mid a.
$$
Hence
$$
\ker\Phi
=
(mn).
$$
:::

<1>5. Therefore
$$
\boxed{
\ZZ/mn\ZZ
\cong
\ZZ/m\ZZ\times\ZZ/n\ZZ
}
$$
as rings.

::: {.proof}
By steps <1>2--<1>4, $\Phi$ is a surjective ring homomorphism with kernel $(mn)$. The first isomorphism theorem gives
$$
\ZZ/\ker\Phi
\cong
\ZZ/m\ZZ\times\ZZ/n\ZZ.
$$
Substituting
$$
\ker\Phi=(mn)
$$
gives the displayed isomorphism.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>5 proves part (b).
:::
:::
