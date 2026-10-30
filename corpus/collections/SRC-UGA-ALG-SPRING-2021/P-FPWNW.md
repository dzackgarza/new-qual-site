---
schema: qual/card@1
id: P-FPWNW
kind: problem
title: Groups of order $p^2$ are abelian; the Sylow theorems; groups of order $4225=5^2
  13^2$ are abelian, with their isomorphism classes
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---
::: {.problem}
a. Show that every group of order $p^2$ with $p$ prime is abelian.

b. State the 3 Sylow theorems.

c. Show that any group of order $4225 = 5^2 13^2$ is abelian.

d. Write down one representative from each isomorphism class of abelian groups of order 4225.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every group of order $p^2$ is abelian.

::: pf-proof

The class equation for a finite $p$-group implies that its center is nontrivial. Thus, if $\cardinality{G}=p^2$, then $\cardinality{Z(G)}$ is $p$ or $p^2$. In the latter case $G=Z(G)$. In the former, $G/Z(G)$ has prime order and is cyclic. A group with cyclic central quotient is abelian: if $G/Z(G)=\langle gZ(G)\rangle$, every pair of elements has the form $g^az,g^bw$ with $z,w$ central, so they commute. Thus $G$ is abelian in either case.

:::

:::

::: {.pf-step #s2}

The three Sylow theorems assert existence, conjugacy and containment, and a restriction on the number of Sylow subgroups.

::: pf-proof

If $\cardinality{G}=p^am$ with $p\nmid m$, then (i) there exists a subgroup of order $p^a$; (ii) every $p$-subgroup lies in a Sylow $p$-subgroup, and all Sylow $p$-subgroups are conjugate; (iii) their number $n_p$ divides $m$ and satisfies $n_p\equiv1\pmod p$. These are the three Sylow theorems.

:::

:::

::: {.pf-step #s3}

Every group of order $4225=5^2\,13^2$ is abelian.

::: pf-proof

By step [](#s2){.pf-ref}, $n_5$ divides $169$ and is congruent to $1$ modulo $5$. The divisors $1,13,169$ have residues $1,3,4$, respectively, so $n_5=1$. Likewise $n_{13}$ divides $25$ and is congruent to $1$ modulo $13$; the divisors $1,5,25$ have residues $1,5,12$, so $n_{13}=1$. Consequently the Sylow subgroups $P$ of order $25$ and $Q$ of order $169$ are normal. They have trivial intersection, and their product has order $4225$, so $G\cong P\times Q$. Both factors are abelian by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

There are exactly four isomorphism classes, represented by
$$
\boxed{\begin{gathered}
C_{25}\times C_{169},\qquad
C_{25}\times C_{13}\times C_{13},\\
C_5\times C_5\times C_{169},\qquad
C_5\times C_5\times C_{13}\times C_{13}.
\end{gathered}}
$$

::: pf-proof

By step [](#s3){.pf-ref}, any such group is abelian. The classification of finite abelian groups gives two isomorphism classes of order $25$, namely $C_{25}$ and $C_5^2$, and two of order $169$, namely $C_{169}$ and $C_{13}^2$. Forming their direct products produces all four possibilities. The Sylow subgroups are characteristic, so differences in either primary factor distinguish the isomorphism classes.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} establish parts (a), (b), (c), and (d), respectively.

:::

:::

:::
