---
schema: qual/card@1
id: P-BKS94-8
kind: problem
title: Automorphisms of $\ZZ[x]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Showed every automorphism fixes Z, then used the inverse automorphism and
    degree multiplication under polynomial composition to force x to map to
    plus/minus x plus an integer.
---

::: {.problem}
Find all automorphisms of $\mathbb { Z } [ x ]$ , the ring of polynomials over $\mathbb { Z }$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every ring automorphism
$$
\varphi:\ZZ[x]\longrightarrow\ZZ[x]
$$
fixes every integer.

::: pf-proof

An automorphism sends the multiplicative identity to the multiplicative
identity, so
$$
\varphi(1)=1.
$$
By additivity,
$$
\varphi(n)=n
$$
for every $n\in\ZZ$.

:::

:::

::: {.pf-step #s2}

If
$$
p(x)\coloneqq\varphi(x),
$$
then $p$ has degree $1$.

::: pf-proof

Let $\psi=\varphi^{-1}$ and put
$$
q(x)\coloneqq\psi(x).
$$
By step [](#s1){.pf-ref}, both automorphisms fix the coefficients in $\ZZ$. Therefore
$$
x
=
\psi(\varphi(x))
=
\psi(p(x))
=
p(q(x)).
$$
Neither $p$ nor $q$ can be constant, and
$$
1
=
\deg x
=
\deg(p\circ q)
=
(\deg p)(\deg q).
$$
Thus
$$
\deg p=\deg q=1.
$$

:::

:::

::: {.pf-step #s3}

There are $\varepsilon\in\{1,-1\}$ and $b\in\ZZ$ such that
$$
\varphi(x)=\varepsilon x+b.
$$

::: pf-proof

By step [](#s2){.pf-ref}, write
$$
p(x)=ax+b,
\qquad
q(x)=cx+d
$$
with $a,c\in\ZZ\setminus\{0\}$. The coefficient of $x$ in
$$
p(q(x))=x
$$
is $ac$, so
$$
ac=1.
$$
Hence
$$
a=c=1
\qquad\text{or}\qquad
a=c=-1.
$$
Thus $a=\varepsilon\in\{1,-1\}$.

:::

:::

::: {.pf-step #s4}

Conversely, for every $b\in\ZZ$ and
$\varepsilon\in\{1,-1\}$, the assignment
$$
x\longmapsto\varepsilon x+b
$$
extends to an automorphism of $\ZZ[x]$.

::: pf-proof

Substitution gives a ring endomorphism
$$
\varphi_{\varepsilon,b}(f)(x)
=
f(\varepsilon x+b).
$$
If $\varepsilon=1$, its inverse is substitution
$$
x\longmapsto x-b.
$$
If $\varepsilon=-1$, the substitution
$$
x\longmapsto -x+b
$$
is its own inverse. Hence each displayed substitution is an automorphism.

:::

:::

::: {.pf-step #s5}

The complete list is
$$
\boxed{
\varphi_{\varepsilon,b}(f)(x)
=
f(\varepsilon x+b),
\qquad
\varepsilon\in\{1,-1\},
\quad
b\in\ZZ
}.
$$

::: pf-proof

Step [](#s3){.pf-ref} shows that every automorphism is on the list, and step [](#s4){.pf-ref} shows
that every map on the list is an automorphism.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives all automorphisms of $\ZZ[x]$.

:::

:::

:::
