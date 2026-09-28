---
schema: qual/card@1
id: P-DCR24
kind: problem
title: Sylow subgroups of $A_5$, their normalizers, and subgroups of orders $6$, $10$,
  and $15$
classification:
  areas:
  - prelim
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
a. Find Sylow subgroups $P_2, P_3$, and $P_5$ for the three primes $2, 3, 5$ dividing the order of $A_5$.
(It suffices to find generators of each of these groups.)

b. Find the normalizers in $A_5$ of each of the three groups you found in part (a).

c. For each of the divisors $d = 6, 10, 15$ of 60, either find a subgroup of $A_5$ of order $d$ or explain why none exists for that choice of $d$.
:::

::: {.solution}
Since $\abs{A_5}=5!/2=60=2^2\cdot3\cdot5$, Sylow $2$-, $3$-, and $5$-subgroups of $A_5$ have orders $4$, $3$, and $5$.

<1>1. For part (a), take
$$
P_2=\langle(1\,2)(3\,4),(1\,3)(2\,4)\rangle,\qquad P_3=\langle(1\,2\,3)\rangle,\qquad P_5=\langle(1\,2\,3\,4\,5)\rangle.
$$

::: {.proof}
The double transpositions $(1\,2)(3\,4)$, $(1\,3)(2\,4)$, $(1\,4)(2\,3)$ are even, commute, and together with $1$ form the Klein four-group $V_4$ of order $4$.
A $3$-cycle and a $5$-cycle are even and generate cyclic subgroups of orders $3$ and $5$.
:::

<1>2. For part (b),
$$
N_{A_5}(P_2)=A_4,\qquad N_{A_5}(P_3)=\langle(1\,2\,3),(1\,2)(4\,5)\rangle\cong S_3,\qquad N_{A_5}(P_5)=\langle(1\,2\,3\,4\,5),(2\,5)(3\,4)\rangle\cong D_{10},
$$
where $A_4$ is the alternating group on $\{1,2,3,4\}$ and $D_{10}$ is dihedral of order $10$.

::: {.proof}
The index of the normalizer of a Sylow subgroup is the number of Sylow subgroups for that prime [@DF04], so it suffices to count Sylow subgroups and exhibit a subgroup of the right order inside each normalizer.
The $15$ double transpositions of $A_5$ lie three to a Klein four-group, so $n_2=5$ and $\abs{N_{A_5}(P_2)}=12$; since $V_4\lhd A_4$, the normalizer is $A_4$.
The $3$-cycles in $A_5$ number $20$, so $n_3=10$ and $\abs{N_{A_5}(P_3)}=6$; conjugation by $(1\,2)(4\,5)$ sends $(1\,2\,3)$ to $(2\,1\,3)=(1\,2\,3)^{-1}$, so the displayed group of order $6$ normalizes $P_3$, and it is nonabelian, hence $\cong S_3$.
The $5$-cycles number $24$, so $n_5=6$ and $\abs{N_{A_5}(P_5)}=10$; conjugation by $(2\,5)(3\,4)$ sends $(1\,2\,3\,4\,5)$ to $(1\,5\,4\,3\,2)=(1\,2\,3\,4\,5)^{-1}$, so the displayed dihedral group of order $10$ is the normalizer.
:::

<1>3. For part (c), $A_5$ has subgroups of orders $6$ and $10$ and none of order $15$.

::: {.proof}
The normalizers of $P_3$ and $P_5$ in step <1>2 have orders $6$ and $10$.
A group of order $15$ is cyclic, because its Sylow $3$- and $5$-subgroups are both unique and hence normal, so it is their direct product $\ZZ/3\times\ZZ/5\cong\ZZ/15$.
The elements of $A_5$ have cycle types $1^5$, $2^21$, $31^2$, $5$, hence orders $1,2,3,5$; none has order $15$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 answer parts (a), (b), and (c).
:::
:::
