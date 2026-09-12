---
schema: qual/card@1
id: P-AMD-A6MEOFBL
kind: problem
title: Three presentations of $\pi_1(K)$ are isomorphic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that all 3 presentations of $\pi_1(K)$ are isomorphic

1. Square with sides glued

2. Two mobius strips glues along boundary

3. Multiplication rule
:::

::: {.solution}
Let
$$
G_1=\langle a,b\mid bab^{-1}=a^{-1}\rangle,
\qquad
G_2=\langle c,d\mid c^2=d^2\rangle,
$$
and let
$$
G_3=\ZZ\rtimes\ZZ,
\qquad
(m,n)(p,q)=(m+(-1)^n p,n+q).
$$

<1>1. The square model of the Klein bottle has fundamental group $G_1$.
::: {.proof}
Its CW structure has one vertex, two oriented $1$-cells $a,b$, and one $2$-cell attached by the Klein-bottle word $aba^{-1}b$ (equivalently, after replacing a generator by its inverse, $bab^{-1}a$). Seifert--van Kampen therefore gives the presentation $bab^{-1}=a^{-1}$.
:::

<1>2. The decomposition into two Möbius bands has fundamental group $G_2$.
::: {.proof}
If $c$ and $d$ are the core-circle generators of the two Möbius bands, each boundary circle represents twice the corresponding core generator, hence $c^2$ and $d^2$. Van Kampen for the union along the common boundary circle gives
$$
\pi_1(K)\cong\langle c,d\mid c^2=d^2\rangle=G_2.
$$
:::

<1>3. Define
$$
\Phi:G_1\to G_2,\qquad \Phi(a)=cd^{-1},\quad \Phi(b)=d.
$$
Then $\Phi$ is a well-defined homomorphism.
::: {.proof}
In $G_2$ the relation $d^2=c^2$ gives $d^{-2}=c^{-2}$. Hence
$$
\Phi(bab^{-1})
=d(cd^{-1})d^{-1}
=dcd^{-2}
=dcc^{-2}
=dc^{-1}
=(cd^{-1})^{-1}
=\Phi(a^{-1}).
$$
Thus the defining relation of $G_1$ is respected.
:::

<1>4. Define
$$
\Psi:G_2\to G_1,\qquad \Psi(c)=ab,\quad \Psi(d)=b.
$$
Then $\Psi$ is a well-defined homomorphism.
::: {.proof}
From $bab^{-1}=a^{-1}$ one obtains $ba=a^{-1}b$. Therefore
$$
\Psi(c^2)=(ab)^2=a(ba)b=a(a^{-1}b)b=b^2=\Psi(d^2),
$$
so the defining relation of $G_2$ is respected.
:::

<1>5. The maps $\Phi$ and $\Psi$ are inverse isomorphisms, so $G_1\cong G_2$.
::: {.proof}
On generators,
$$
\Psi\Phi(a)=\Psi(cd^{-1})=(ab)b^{-1}=a,
\qquad
\Psi\Phi(b)=b,
$$
and
$$
\Phi\Psi(c)=\Phi(ab)=(cd^{-1})d=c,
\qquad
\Phi\Psi(d)=d.
$$
Hence both composites are the identity.
:::

<1>6. Define
$$
\Theta:G_1\to G_3,\qquad \Theta(a)=(1,0),\quad \Theta(b)=(0,1).
$$
Then $\Theta$ is a well-defined homomorphism.
::: {.proof}
Using the multiplication in $G_3$,
$$
(0,1)(1,0)(0,-1)=(-1,0)=(1,0)^{-1},
$$
so the relation $bab^{-1}=a^{-1}$ is satisfied.
:::

<1>7. For all $n,p\in\ZZ$ one has
$$
b^n a^p=a^{(-1)^n p}b^n
$$
in $G_1$.
::: {.proof}
The defining relation gives $ba^p=a^{-p}b$ for every $p\in\ZZ$. Iterating for positive $n$ gives the formula; replacing $n$ by $-n$ gives the negative cases as well.
:::

<1>8. The map
$$
\Lambda:G_3\to G_1,\qquad \Lambda(m,n)=a^m b^n,
$$
is a homomorphism.
::: {.proof}
By <1>7,
$$
\Lambda(m,n)\Lambda(p,q)
=a^m b^n a^p b^q
=a^{m+(-1)^n p}b^{n+q}
=\Lambda(m+(-1)^n p,n+q),
$$
which is exactly the multiplication law of $G_3$.
:::

<1>9. The maps $\Theta$ and $\Lambda$ are inverse isomorphisms, so $G_1\cong G_3$.
::: {.proof}
For $(m,n)\in G_3$,
$$
\Theta\Lambda(m,n)=\Theta(a)^m\Theta(b)^n=(m,n).
$$
Conversely, $\Lambda\Theta$ fixes the generators $a,b$ of $G_1$, hence is the identity.
:::

<1>10. Consequently
$$\boxed{G_1\cong G_2\cong G_3\cong\pi_1(K).}$$
::: {.proof}
Combine <1>1--<1>2, <1>5, and <1>9.
:::
:::
