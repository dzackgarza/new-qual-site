---
schema: qual/card@1
id: P-QY54D
kind: problem
title: Center and central quotient of $Q_8$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent Hungerford solutions-manual transcription for II.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section II.6,
    exercise 4, book page 99: "What is the center of the quaternion group Q_8?
    Show that Q_8/C(Q_8) is abelian." The card states this with Z(Q_8) for the
    center; section 4 of this chapter writes C(G) for the center and the card's
    use of Z is the same object. The proof was checked: ±1 are central; ij = k
    and ji = -k show i and -i are not, and the cyclic permutation of i, j, k
    gives the same for ±j, ±k, so the center is exactly {±1}; the quotient has
    order 4 with every coset of square 1, so it is Z_2 ⊕ Z_2 rather than Z_4 and
    in particular is abelian. Complete; no defect.
---

::: {.problem}
What is the center of the quaternion group $Q_8$?
Show that $Q_8/Z(Q_8)$ is abelian.
:::

::: {.solution}
Write
$$
Q_8=\{\pm1,\pm i,\pm j,\pm k\},
$$
with $i^2=j^2=k^2=ijk=-1$.

::: pf

::: {.pf-step #s1}

The center of $Q_8$ is
$$
Z(Q_8)=\{\pm1\}.
$$

::: pf-proof

The elements $1$ and $-1$ commute with every element of $Q_8$, so
$\{\pm1\}\subseteq Z(Q_8)$.

On the other hand,
$$
ij=k\qquad\text{while}\qquad ji=-k,
$$
so neither $i$ nor $-i$ is central. Cyclically permuting $i,j,k$ shows that none
of $\pm j,\pm k$ is central either. Thus no further elements lie in the center.

:::

:::

::: {.pf-step #s2}

The quotient $Q_8/Z(Q_8)$ has four elements, each of order dividing $2$.

::: pf-proof

By step [](#s1){.pf-ref}, the quotient has order $8/2=4$. Its cosets are
$$
Z(Q_8),\quad iZ(Q_8),\quad jZ(Q_8),\quad kZ(Q_8).
$$
Moreover,
$$
(iZ(Q_8))^2=i^2Z(Q_8)=(-1)Z(Q_8)=Z(Q_8),
$$
and similarly for the $j$- and $k$-cosets.

:::

:::

::: pf-step

Hence
$$
Q_8/Z(Q_8)\cong \ZZ_2\oplus\ZZ_2,
$$
in particular the quotient is abelian.

::: pf-proof

By step [](#s2){.pf-ref} the quotient has order $4$ and no element of order $4$, so it is the
Klein four group rather than the cyclic group of order $4$. Therefore it is
isomorphic to $\ZZ_2\oplus\ZZ_2$ and is abelian.

:::

:::

:::

:::
