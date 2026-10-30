---
schema: qual/card@1
id: P-KSRING17-019
kind: problem
title: Chinese remainder theorem for $\ZZ_{mn}\cong\ZZ_m\times\ZZ_n$
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
Let $m$ and $n$ be relatively prime integers.

(a) Show that if $c$ and $d$ are any integers, then there is an integer $x$ such that $x \equiv c \pmod{m}$ and $x \equiv d \pmod{n}$.

(b) Show that $\ZZ_{mn}$ and $\ZZ_{m} \times \ZZ_{n}$ are isomorphic as rings.
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

::: pf

::: {.pf-step #s1-1}

For arbitrary integers $c,d$, define
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


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Define
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


::: pf-proof

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

:::

::: {.pf-step #s1-3}

The map $\Phi$ is surjective.


::: pf-proof

Let
$$
(c+(m),d+(n))
\in
\ZZ/m\ZZ\times\ZZ/n\ZZ
$$
be arbitrary. By step [](#s1-1){.pf-ref}, there exists an integer $x$ with
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

:::

::: {.pf-step #s1-4}

The kernel of $\Phi$ is
$$
(mn).
$$


::: pf-proof

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

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\ZZ/mn\ZZ
\cong
\ZZ/m\ZZ\times\ZZ/n\ZZ
}
$$
as rings.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref}, $\Phi$ is a surjective ring homomorphism with kernel $(mn)$. The first isomorphism theorem gives
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

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
