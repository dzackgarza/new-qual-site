---
schema: qual/card@1
id: P-N6YDQ
kind: problem
title: 'Splitting field of $x^5-3$ over $\mathbb{Q}$: cyclotomic subfield, Galois
  group over $\mathbb{Q}(\zeta_5)$, and degree'
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Galois Theory
  - Roots of Unity
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the polynomial, cyclotomic subfield, and degree requests with Summer 2007 Fields 2 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both Eisenstein arguments, the coprime-degree lower bound after base extension, and the explicit cyclic automorphism action."
---

::: problem
Let $L$ be the splitting field of $x^5 - 3$ over $\mathbb{Q}$.

a. Let $\zeta_5$ be a primitive 5th root of unity.
Prove that $\mathbb{Q}(\zeta_5) \subset L$.

b. What is the Galois group of $L$ over $\mathbb{Q}(\zeta_5)$?

c. What is the dimension of $L$ over $\mathbb{Q}$?
:::

::: solution
Write $\alpha=\sqrt[5]{3}$ for the positive real root,
$\zeta=\zeta_5$, and $F=\mathbb Q(\zeta)$. The answers are
$$
F\subset L=F(\alpha),\qquad
\operatorname{Gal}(L/F)\cong C_5,\qquad [L:\mathbb Q]=20.
$$

<1>1. The splitting field contains $\zeta$ and equals
$\mathbb Q(\alpha,\zeta)$.

::: proof
The five roots are $\alpha\zeta^j$ for $0\leq j<5$.
The field $L$ contains both $\alpha$ and $\alpha\zeta$, so it
contains their ratio $\zeta$; here $\alpha\ne0$.
Conversely, $\mathbb Q(\alpha,\zeta)$ contains every root.
These two containments prove the assertion.
:::

<1>2. The degrees are $[L:F]=5$ and $[L:\mathbb Q]=20$.

::: proof
Eisenstein's criterion at $3$ makes $x^5-3$ irreducible over
$\mathbb Q$ [@DF04], so $[\mathbb Q(\alpha):\mathbb Q]=5$.
Also $\zeta$ is a root of
$$
\Phi_5(x)=x^4+x^3+x^2+x+1.
$$
Its translate is
$$
\Phi_5(t+1)=t^4+5t^3+10t^2+10t+5,
$$
which is Eisenstein at $5$. Translation of the variable is an
automorphism of $\mathbb Q[x]$, so $\Phi_5$ is irreducible and
$[F:\mathbb Q]=4$.

Set $d=[L:F]$. Since $L=F(\alpha)$ and $\alpha$ satisfies a
degree-$5$ polynomial over $F$, we have $1\leq d\leq5$.
The tower law gives $[L:\mathbb Q]=4d$. The subfield
$\mathbb Q(\alpha)\subseteq L$ has degree $5$, so the same law
implies $5\mid4d$. As $\gcd(4,5)=1$, we obtain $5\mid d$,
hence $d=5$ and $[L:\mathbb Q]=20$.
This establishes the degree over $F$ without assuming that
irreducibility over $\mathbb Q$ survives a change of coefficient field.
:::

<1>3. The Galois group over $F$ is cyclic of order $5$.

::: proof
The extension $L/F$ is a splitting field of $x^5-3$ in characteristic
zero, so it is finite Galois. Its automorphism group has order
$[L:F]=5$ [@DF04]. An $F$-automorphism must send $\alpha$ to a root
$\alpha\zeta^j$, and this image determines it because $L=F(\alpha)$.
Thus the map
$$
\operatorname{Gal}(L/F)\longrightarrow\mathbb Z/5\mathbb Z,
\qquad \sigma\longmapsto j\quad
\text{when }\sigma(\alpha)=\alpha\zeta^j
$$
is injective. It is a homomorphism: every such automorphism fixes
$\zeta$, so composition adds the exponents modulo $5$.
Both groups have five elements, making the map an isomorphism.
In particular the automorphism fixing $F$ and sending
$\alpha$ to $\zeta\alpha$ generates the group.
:::
:::
