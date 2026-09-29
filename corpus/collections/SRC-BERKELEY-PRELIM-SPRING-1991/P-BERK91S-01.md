---
schema: qual/card@1
id: P-BERK91S-01
kind: problem
title: Groups of order at most five
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the isomorphism classification and the order bound five with Problem 1 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Classified the prime orders by Lagrange's theorem and constructed an isomorphism with the Klein four-group in the noncyclic order-four case.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked the trivial group, all possible element orders, representative independence and bijectivity of the explicit homomorphisms, and pairwise nonisomorphism of the listed groups.
---

::: {.problem}
List, up to isomorphism, all finite groups whose orders do not exceed $5$.
:::

::: {.hint}
Use Lagrange's theorem for the prime orders $2,3,5$. For a group
$G$ of order $4$, separate the case with an element of order
$4$ from the case in which every nonidentity element has order
$2$. In the latter case, use
$$
xy=(xy)^{-1}=y^{-1}x^{-1}=yx
$$
to prove commutativity. For distinct nonidentity elements $a,b$,
consider the homomorphism
$$
(\ZZ/2\ZZ)\times(\ZZ/2\ZZ)\longrightarrow G,
\qquad(\overline r,\overline s)\longmapsto a^r b^s.
$$
Account separately for the group of order $1$ and distinguish
the groups of order $4$ by their element orders.
:::

::: {.solution}
For a positive integer $m$, write $C_m\coloneqq(\ZZ/m\ZZ,+)$.
Let $G$ be a finite group with identity $e$ and $\abs{G}\leq5$.

::: pf

::: {.pf-step #s1}

If $\abs{G}=1$, then $G\cong C_1$. If
$\abs{G}=p\in\{2,3,5\}$, then $G\cong C_p$.

::: pf-proof

In the first case $G=\{e\}$, which is isomorphic to $C_1$ by
the unique map. In the second case choose $g\in G\setminus\{e\}$.
By [[T-GJNT5|Lagrange's theorem]], the order of $g$ divides
$p$. Since $g\neq e$, its order is $p$, and therefore its
powers exhaust $G$. The map
$$
\varphi\colon C_p\longrightarrow G,
\qquad \overline r\longmapsto g^r,
$$
is well defined because $g^p=e$, is a homomorphism by the
exponent law, and is bijective because $g$ has order $p$.

:::

:::

::: {.pf-step #s2}

If $\abs{G}=4$ and some element has order $4$, then
$G\cong C_4$.

::: pf-proof

Choose an element $g$ of order $4$. Its powers
$e,g,g^2,g^3$ are distinct and exhaust $G$. Thus
$$
\psi\colon C_4\longrightarrow G,
\qquad \overline r\longmapsto g^r,
$$
is a well-defined bijective homomorphism.

:::

:::

::: {.pf-step #s3}

If $\abs{G}=4$ and no element has order $4$, then
$G\cong C_2\times C_2$.

::: pf-proof

::: {.pf-step #s3-1}

Every element of $G$ is its own inverse, and $G$ is
commutative.

::: pf-proof

By [[T-GJNT5|Lagrange's theorem]], each element has order
$1$, $2$, or $4$. The assumption excludes order $4$, so
$x^2=e$ for every $x\in G$. Consequently, for every
$x,y\in G$,
$$
xy=(xy)^{-1}=y^{-1}x^{-1}=yx.
$$

:::

:::

::: {.pf-step #s3-2}

For distinct elements $a,b\in G\setminus\{e\}$, the map
$$
\theta\colon C_2\times C_2\longrightarrow G,
\qquad (\overline r,\overline s)\longmapsto a^r b^s,
$$
is an isomorphism.

::: pf-proof

Such $a,b$ exist since $G\setminus\{e\}$ has three elements.
Step [](#s3-1){.pf-ref} gives $a^2=b^2=e$ and $ab=ba$. The first equalities
make $\theta$ independent of the integer representatives
$r,s$, and commutativity gives
$$
a^{r+r'}b^{s+s'}=(a^r b^s)(a^{r'}b^{s'})
\qquad(r,s,r',s'\in\ZZ).
$$
Hence $\theta$ is a homomorphism. Its images are
$e,a,b,ab$. The first three are distinct by the choice of
$a,b$. If $ab=e$, then $b=a^{-1}=a$; if $ab=a$, then $b=e$;
and if $ab=b$, then $a=e$. Each equality contradicts that
choice. Thus the four images are distinct and exhaust $G$,
so $\theta$ is bijective.

:::

:::

::: pf-qed

Step [](#s3-2){.pf-ref} constructs the required isomorphism, using
step [](#s3-1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s4}

A complete list, with no two entries isomorphic, is
$$
\boxed{C_1,\ C_2,\ C_3,\ C_4,\ C_2\times C_2,\ C_5}.
$$

::: pf-proof

A group contains its identity, so its order is a positive
integer. Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} exhaust the orders $1,2,3,4,5$.
Every listed group has the required order. Groups with
different orders cannot be isomorphic. Among the two groups
of order $4$, the element $\overline1\in C_4$ has order $4$,
whereas every nonidentity element of $C_2\times C_2$ has
order $2$. An isomorphism preserves element orders, so these
two groups are not isomorphic.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives every isomorphism class exactly once.

:::

:::

:::
