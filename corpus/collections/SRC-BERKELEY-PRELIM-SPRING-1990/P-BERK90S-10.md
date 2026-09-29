---
schema: qual/card@1
id: P-BERK90S-10
kind: problem
title: Two nonisomorphic nonabelian groups of each of the orders $24$, $30$, and $40$
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
  note: Compared all three orders and the nonisomorphic nonabelian requirements with Problem 10 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Exhibited the three pairs from the hint and distinguished their isomorphism types by explicit center computations.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked all six group orders, noncommuting elements, the dihedral and symmetric center calculations, and the direct-product center formula.
---

::: {.problem}
Show that for each of the orders
$$
24,\qquad30,\qquad40,
$$
there are at least two nonisomorphic nonabelian groups of that order.
:::

::: {.hint}
For $m\geq3$, let $D_m$ be the dihedral group of order $2m$.
For $m\geq1$, let $C_m$ be the cyclic group of order $m$ and $S_m$
the symmetric group on $m$ letters. Consider the pairs
$$
(D_{12},S_4),\qquad
(D_{15},S_3\times C_5),\qquad
(D_{20},D_{10}\times C_2).
$$
Compare the centers within each pair. In the presentation
$$
D_m=\langle r,s\mid r^m=s^2=1,\ srs^{-1}=r^{-1}\rangle,
$$
a rotation $r^k$ commutes with $s$ exactly when $2k\equiv0\pmod m$,
and a reflection cannot commute with $r$ for $m\geq3$.
:::

::: {.solution}
For $m\geq3$, let $D_m$ be the [[D-4R2Z5|dihedral group]] of order
$2m$, with rotation $r$ of order $m$ and reflection $s$ satisfying
$srs^{-1}=r^{-1}$. Let $C_m$ be the cyclic group of order $m$ for
$m\geq1$, and let $S_m$ be the [[D-6BTFJ|symmetric group]] on
$m$ letters for $m\geq3$. Write $Z(G)$ for the center of a group $G$.

::: pf

::: {.pf-step #s1}

For $m\geq3$, the group $D_m$ is nonabelian and
$$
Z(D_m)=
\begin{cases}
\{1\},&m\text{ odd},\\
\{1,r^{m/2}\},&m\text{ even}.
\end{cases}
$$

::: pf-proof

Since $r$ has order $m\geq3$, the elements $r$ and $r^{-1}$ are
distinct. Thus $srs^{-1}=r^{-1}\neq r$, so $r$ and $s$ do not
commute.

Every element of $D_m$ is either $r^k$ or $r^ks$, with
$0\leq k<m$. Conjugation by $r^ks$ sends $r$ to $r^{-1}$, so
no element of the second form is central. A rotation $r^k$
commutes with $r$ and commutes with $s$ exactly when
$r^{-k}=r^k$, or $m\mid2k$. Since $r$ and $s$ generate $D_m$,
this condition is also sufficient for $r^k$ to be central.
For odd $m$, it forces $k=0$. For even $m$, it gives exactly
$k=0$ and $k=m/2$. This proves the stated formula.

:::

:::

::: {.pf-step #s2}

For $m\geq3$, the group $S_m$ is nonabelian and
$Z(S_m)=\{1\}$. For any groups $G$ and $H$,
$$
Z(G\times H)=Z(G)\times Z(H).
$$

::: pf-proof

The transpositions $(1\,2)$ and $(2\,3)$ do not commute, so $S_m$
is nonabelian. Suppose $\sigma\in Z(S_m)$. For distinct letters
$i,j$, conjugating $(i\,j)$ by $\sigma$ gives
$$
(\sigma(i)\,\sigma(j))
=\sigma(i\,j)\sigma^{-1}=(i\,j).
$$
Fix $i$ and choose distinct $j,k$ different from $i$. The displayed
equality gives both $\sigma(i)\in\{i,j\}$ and
$\sigma(i)\in\{i,k\}$, hence $\sigma(i)=i$. This holds for every
$i$, so $\sigma=1$.

An element $(g,h)\in G\times H$ commutes with every
$(g',h')\in G\times H$ exactly when $gg'=g'g$ for every $g'\in G$
and $hh'=h'h$ for every $h'\in H$. This proves the product formula.
An isomorphism of groups restricts to an isomorphism of their
centers, since it preserves commutation and is surjective.
Consequently groups with centers of different orders are
nonisomorphic.

:::

:::

::: {.pf-step #s3}

A pair of nonisomorphic nonabelian groups of order $24$ is
$\boxed{D_{12},\ S_4}$.

::: pf-proof

Their orders are $2\cdot12=24$ and $4!=24$, and both are
nonabelian by steps [](#s1){.pf-ref} and [](#s2){.pf-ref}. The same steps give
$\abs{Z(D_{12})}=2$ and $\abs{Z(S_4)}=1$, so the groups
are nonisomorphic.

:::

:::

::: {.pf-step #s4}

A pair of nonisomorphic nonabelian groups of order $30$ is
$\boxed{D_{15},\ S_3\times C_5}$.

::: pf-proof

Their orders are $2\cdot15=30$ and $3!\cdot5=30$. The group
$D_{15}$ is nonabelian by step [](#s1){.pf-ref}, and $S_3\times C_5$ contains
the nonabelian subgroup $S_3\times\{1\}$ by step [](#s2){.pf-ref}.
Since $C_5$ is abelian, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\abs{Z(D_{15})}=1,\qquad
Z(S_3\times C_5)=\{1\}\times C_5.
$$
Their centers have orders $1$ and $5$, so the groups are
nonisomorphic.

:::

:::

::: {.pf-step #s5}

A pair of nonisomorphic nonabelian groups of order $40$ is
$\boxed{D_{20},\ D_{10}\times C_2}$.

::: pf-proof

Their orders are $2\cdot20=40$ and $(2\cdot10)\cdot2=40$.
The first group is nonabelian by step [](#s1){.pf-ref}, and the second
contains the nonabelian subgroup $D_{10}\times\{1\}$.
Since $C_2$ is abelian, steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\abs{Z(D_{20})}=2,\qquad
\abs{Z(D_{10}\times C_2)}=2\cdot2=4.
$$
Thus the groups are nonisomorphic.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} exhibit two nonisomorphic nonabelian
groups for each of the requested orders $24$, $30$, and $40$.

:::

:::

:::
