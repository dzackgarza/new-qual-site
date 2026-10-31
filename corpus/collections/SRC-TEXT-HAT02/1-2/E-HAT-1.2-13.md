---
schema: qual/card@1
id: E-HAT-1.2-13
kind: problem
title: Two ways to identify boundary circles of disk with two holes give non-isomorphic fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The other identification gives H_1 = Z^2 + Z/3, not the closed surface N_3; solution recomputed from the CW structure of the identified pair of pants.
---

::: {.problem}
The space $Y$ in the preceding exercise can be obtained from a disk with two holes by identifying its three boundary circles.
There are only two essentially different ways of identifying the three boundary circles.
Show that the other way yields a space $Z$ with $\pi_1(Z)$ not isomorphic to $\pi_1(Y)$.
[Abelianize the fundamental groups to show they are not isomorphic.]
:::

::: {.solution}
Let $P$ be the disk with two holes, with outer boundary circle $C_0$ and inner boundary circles $C_1,C_2$, all oriented counterclockwise in the plane.
An identification of the three circles is a quotient $P\to K$ onto a space in which the $C_i$ become one circle $C$, each $C_i\to C$ a homeomorphism of degree $d_i=\pm1$ for a fixed orientation of $C$.

::: pf

::: {.pf-step #s1}

The quotient $K$ is a CW complex with one $0$-cell $v$, three $1$-cells $c,e_1,e_2$, and one $2$-cell attached along
$$
c^{d_0}\,e_1\,c^{-d_1}\,e_1^{-1}\,e_2\,c^{-d_2}\,e_2^{-1}.
$$

::: pf-proof

Give $P$ the CW structure with one vertex $v_i$ on each $C_i$, the three circles $C_i$ as loops at $v_i$, two arcs $e_1,e_2$ from $v_0$ to $v_1$ and $v_2$, and one $2$-cell.
Cutting $P$ along $e_1$ and $e_2$ leaves a disk whose boundary reads $C_0\,e_1\,C_1^{-1}\,e_1^{-1}\,e_2\,C_2^{-1}\,e_2^{-1}$, the inner circles being traversed clockwise.
We may take the identifications to send each $v_i$ to one point $v$ of $C$.
In the quotient each $C_i$ becomes $c^{d_i}$, which gives the stated attaching word.

:::

:::

::: {.pf-step #s2}

$$
H_1(K)\cong\ZZ^2\oplus\ZZ/\abs{d_0-d_1-d_2}.
$$

::: pf-proof

By step [](#s1){.pf-ref} and van Kampen, $\pi_1(K)$ has generators $c,e_1,e_2$ and the single relator of step [](#s1){.pf-ref}.
Abelianizing, the $e_i$ cancel and the relation becomes $(d_0-d_1-d_2)c=0$.
Hence $H_1(K)=\ZZ e_1\oplus\ZZ e_2\oplus\ZZ c/(d_0-d_1-d_2)$.

:::

:::

::: {.pf-step #s3}

The integer $\abs{d_0-d_1-d_2}$ is $3$ when $d_1=d_2=-d_0$, and is $1$ otherwise.

::: pf-proof

Each $d_i$ is $\pm1$.
If $d_1=d_2=-d_0$ then $d_0-d_1-d_2=3d_0$.
Otherwise at least one of $-d_1,-d_2$ equals $-d_0$, so the sum is $\pm1$.
These are the two essentially different identifications.

:::

:::

::: {.pf-step #s4}

$H_1(Y)\cong\ZZ^2$.

::: pf-proof

By the preceding exercise, $\pi_1(Y)=\langle a,b,c\mid aba^{-1}b^{-1}cb^{\varepsilon}c^{-1}\rangle$ with $\varepsilon=\pm1$.
Abelianizing gives $\varepsilon b=0$, so $b=0$ and $H_1(Y)$ is free abelian on $a$ and $c$.
Thus $Y$ is the identification with $\abs{d_0-d_1-d_2}=1$ in step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

For the other identification, $H_1(Z)\cong\ZZ^2\oplus\ZZ/3$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} with $d_1=d_2=-d_0$.

:::

:::

::: pf-qed

$\pi_1(Y)\not\cong\pi_1(Z)$, because isomorphic groups have isomorphic abelianizations and $H_1(Y)=\pi_1(Y)^{\mathrm{ab}}$ is torsion-free while $H_1(Z)$ has an element of order $3$, by steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::
