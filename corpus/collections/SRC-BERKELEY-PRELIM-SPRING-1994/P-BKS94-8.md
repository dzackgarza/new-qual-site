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
<1>1. Every ring automorphism
$$
\varphi:\ZZ[x]\longrightarrow\ZZ[x]
$$
fixes every integer.

::: {.proof}
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

<1>2. If
$$
p(x)\coloneqq\varphi(x),
$$
then $p$ has degree $1$.

::: {.proof}
Let $\psi=\varphi^{-1}$ and put
$$
q(x)\coloneqq\psi(x).
$$
By step <1>1, both automorphisms fix the coefficients in $\ZZ$. Therefore
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

<1>3. There are $\varepsilon\in\{1,-1\}$ and $b\in\ZZ$ such that
$$
\varphi(x)=\varepsilon x+b.
$$

::: {.proof}
By step <1>2, write
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

<1>4. Conversely, for every $b\in\ZZ$ and
$\varepsilon\in\{1,-1\}$, the assignment
$$
x\longmapsto\varepsilon x+b
$$
extends to an automorphism of $\ZZ[x]$.

::: {.proof}
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

<1>5. The complete list is
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

::: {.proof}
Step <1>3 shows that every automorphism is on the list, and step <1>4 shows
that every map on the list is an automorphism.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives all automorphisms of $\ZZ[x]$.
:::
:::
