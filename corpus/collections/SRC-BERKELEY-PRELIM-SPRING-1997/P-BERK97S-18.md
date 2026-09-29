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
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Distinguished the finite-product reading from an arbitrary infinite
    product. The finite case splits by lifting a free basis; the arbitrary
    infinite case can fail by the Baer--Specker theorem.
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

::: pf

::: {.pf-step #s1}

Statement (1) is false.

::: pf-proof

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

:::

::: {.pf-step #s2}

If the direct product in statement (2) has finitely many factors, write
$$
H=C_1\times\cdots\times C_r,
$$
where each $C_i$ is infinite cyclic, and choose a generator $h_i$ of $C_i$.
Then $H$ is free abelian on $h_1,\ldots,h_r$.

::: pf-proof

For a finite product, every element of $H$ has a unique expression
$$
n_1h_1+\cdots+n_rh_r
$$
with $n_1,\ldots,n_r\in\ZZ$. Thus $H\cong\ZZ^r$ with basis
$h_1,\ldots,h_r$.

:::

:::

::: pf-step

Under the finite-product interpretation, the quotient map $q$ admits a
homomorphic section
$$
s:H\longrightarrow G
$$
with $q\circ s=\operatorname{id}_H$.

::: pf-proof

For each $i\in\{1,\ldots,r\}$, choose $g_i\in G$ with
$$
q(g_i)=h_i.
$$
Since $H$ is free abelian on $h_1,\ldots,h_r$ by step [](#s2){.pf-ref}, there is a
unique homomorphism $s:H\to G$ satisfying
$$
s(h_i)=g_i
\qquad(1\leq i\leq r).
$$
For every $i\in\{1,\ldots,r\}$,
$$
(q\circ s)(h_i)=q(g_i)=h_i.
$$
Because the $h_i$ generate $H$, it follows that
$q\circ s=\operatorname{id}_H$.

:::

:::

::: {.pf-step #s4}

The map
$$
\Phi:K\times H\longrightarrow G,
\qquad
\Phi(k,h)=k+s(h),
$$
is an isomorphism.

::: pf-proof

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

:::

::: {.pf-step #s5}

Under the finite-product interpretation, statement (2) is true:
$$
G\cong H\times K.
$$

::: pf-proof

By step [](#s4){.pf-ref},
$$
G\cong K\times H.
$$
Since direct products of abelian groups are symmetric,
$K\times H\cong H\times K$.

:::

:::

::: {.pf-step #s6}

If arbitrary infinite direct products are allowed in statement (2),
then statement (2) is false in general.

::: pf-proof

Take $H=\prod_{n\geq1}\ZZ$. By the Baer--Specker theorem, $H$ is not a
free abelian group. Let $F$ be the free abelian group on the underlying set
of $H$, and let
$$
\pi:F\longrightarrow H
$$
send the basis element indexed by $h\in H$ to $h$. Then $\pi$ is
surjective. Put $K=\ker\pi$. By the first isomorphism theorem,
$$
F/K\cong H,
$$
so this is an instance of the quotient in the problem.

If $F\cong H\times K$, then $H$ is isomorphic to a direct summand, hence
to a subgroup, of the free abelian group $F$. Every subgroup of a free
abelian group is free, contradicting the Baer--Specker theorem. Thus this
quotient need not split when an arbitrary infinite product is permitted.

:::

:::

::: {.pf-step #s7}

The conclusions are
$$
\boxed{
\begin{aligned}
&\text{(1) is false;}\\
&\text{(2) is true for a finite direct product of infinite cyclic groups,}\\
&\text{and false in general for arbitrary infinite direct products.}
\end{aligned}
}
$$

::: pf-proof

Step [](#s1){.pf-ref} disproves statement (1). Step [](#s5){.pf-ref} proves statement (2) for the
finite-product reading, and step [](#s6){.pf-ref} supplies the infinite-product
counterexample.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} records the required conclusions.

:::

:::

:::
