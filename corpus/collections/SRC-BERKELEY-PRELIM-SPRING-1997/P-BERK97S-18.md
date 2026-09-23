---
schema: qual/card@1
id: P-BERK97S-18
kind: problem
title: Splitting extensions with finite-cyclic and free-abelian quotients
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $H=G/K$ be the quotient of an abelian group $G$ by a subgroup $K$. Prove or disprove:

1. If $H$ is finite cyclic, then $G$ is isomorphic to the direct product $H\times K$.
2. If $H$ is a direct product of infinite cyclic groups, then $G$ is isomorphic to $H\times K$.
:::

::: {.solution}
Let
$$
q:G\longrightarrow H=G/K
$$
denote the quotient homomorphism.

<1>1. Statement (1) is false.

::: {.proof}
Take
$$
G=\ZZ/4\ZZ
$$
and let
$$
K=2\ZZ/4\ZZ.
$$
Then $K\cong\ZZ/2\ZZ$, and
$$
H=G/K\cong\ZZ/2\ZZ,
$$
so $H$ is finite cyclic. However,
$$
H\times K
\cong
(\ZZ/2\ZZ)\times(\ZZ/2\ZZ)
$$
has no element of order $4$, whereas $G=\ZZ/4\ZZ$ does. Hence
$G\not\cong H\times K$.
:::

<1>2. For statement (2), let $(h_i)_{i\in I}$ be generators of the
infinite cyclic direct factors of $H$. Then $H$ is free abelian on
$(h_i)_{i\in I}$.

::: {.proof}
This is the direct-product decomposition assumed in statement (2): every
element of $H$ has a unique expression as a finite integral linear
combination of the chosen generators.
:::

<1>3. The quotient map $q$ admits a homomorphic section
$$
s:H\longrightarrow G
$$
with $q\circ s=\operatorname{id}_H$.

::: {.proof}
For each $i\in I$, choose $g_i\in G$ with
$$
q(g_i)=h_i.
$$
Since $H$ is free abelian on $(h_i)_{i\in I}$ by step <1>2, there is a
unique homomorphism $s:H\to G$ satisfying
$$
s(h_i)=g_i
\qquad(i\in I).
$$
For every $i\in I$,
$$
(q\circ s)(h_i)=q(g_i)=h_i.
$$
Because the $h_i$ generate $H$, it follows that
$q\circ s=\operatorname{id}_H$.
:::

<1>4. The map
$$
\Phi:K\times H\longrightarrow G,
\qquad
\Phi(k,h)=k+s(h),
$$
is an isomorphism.

::: {.proof}
It is a homomorphism because $G$ is abelian. For $g\in G$, put
$$
h=q(g).
$$
Then
$$
q\bigl(g-s(h)\bigr)
=q(g)-(q\circ s)(h)
=h-h
=0,
$$
so $g-s(h)\in K$. Hence
$$
g=\Phi\bigl(g-s(h),h\bigr),
$$
and $\Phi$ is surjective.

If $\Phi(k,h)=0$, applying $q$ gives
$$
0=q(k)+(q\circ s)(h)=h,
$$
because $q(k)=0$ for $k\in K$. Thus $h=0$, and then
$k=\Phi(k,0)=0$. Therefore $\Phi$ is injective.
:::

<1>5. Statement (2) is true:
$$
\boxed{G\cong H\times K}.
$$

::: {.proof}
By step <1>4,
$$
G\cong K\times H.
$$
Since direct products of abelian groups are symmetric,
$K\times H\cong H\times K$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 disproves statement (1), and step <1>5 proves statement (2).
:::
:::
