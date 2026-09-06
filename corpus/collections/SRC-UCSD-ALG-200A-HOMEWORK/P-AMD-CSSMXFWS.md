---
schema: qual/card@1
id: P-AMD-CSSMXFWS
kind: problem
title: Sylow subgroup normality in groups of order $595$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 6. The source
    asks to prove that every Sylow subgroup is normal when |G|=595=5*7*17.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Sylow congruence first makes the Sylow 5-subgroup unique. Modding it out
    gives a group of order 7*17 in which both Sylow subgroups are unique. Their
    normal preimages have orders 35 and 85; each preimage has a unique Sylow
    subgroup of the complementary prime, hence a characteristic Sylow 7- or
    17-subgroup, which is therefore normal in G.
---

::: {.problem}
Let $G$ be a finite group with
\[
|G|=595=5\cdot7\cdot17.
\]
Prove that every Sylow subgroup of $G$ is normal.
:::

::: {.solution}
<1>1. The Sylow $5$-subgroup of $G$ is unique and hence normal.
::: {.proof}
Let $n_5$ be the number of Sylow $5$-subgroups of $G$.
Sylow's theorem gives
\[
n_5\equiv1\pmod5
\qquad\text{and}\qquad
n_5\mid 7\cdot17=119.
\]
The divisors of $119$ are
\[
1,7,17,119,
\]
and modulo $5$ these are congruent to
\[
1,2,2,4,
\]
respectively.
Therefore
\[
n_5=1.
\]
Let $P_5$ denote this unique Sylow $5$-subgroup.
Then
\[
P_5\normal G.
\]
:::

<1>2. The quotient
\[
\overline G=G/P_5
\]
has order $119=7\cdot17$, and both of its Sylow subgroups are unique.
::: {.proof}
By <1>1,
\[
|\overline G|=|G|/|P_5|=595/5=119.
\]
Let $\overline n_{17}$ be the number of Sylow $17$-subgroups of $\overline G$.
Then
\[
\overline n_{17}\equiv1\pmod{17}
\qquad\text{and}\qquad
\overline n_{17}\mid7.
\]
Thus $\overline n_{17}\in\{1,7\}$, and $7\not\equiv1\pmod{17}$, so
\[
\overline n_{17}=1.
\]
Similarly, if $\overline n_7$ is the number of Sylow $7$-subgroups of $\overline G$, then
\[
\overline n_7\equiv1\pmod7
\qquad\text{and}\qquad
\overline n_7\mid17.
\]
Thus $\overline n_7\in\{1,17\}$, and $17\equiv3\pmod7$, so
\[
\overline n_7=1.
\]
Hence the Sylow $7$- and Sylow $17$-subgroups of $\overline G$ are both unique and normal.
:::

<1>3. There is a normal subgroup $K\normal G$ of order $85=5\cdot17$.
::: {.proof}
Let
\[
\pi:G\longrightarrow\overline G
\]
be the quotient map, and let $\overline R$ be the unique Sylow $17$-subgroup of $\overline G$.
By <1>2,
\[
\overline R\normal\overline G.
\]
Set
\[
K=\pi^{-1}(\overline R).
\]
The preimage of a normal subgroup under a homomorphism is normal, so
\[
K\normal G.
\]
Moreover,
\[
K/P_5\cong\overline R,
\]
so
\[
|K|=|P_5|\,|\overline R|=5\cdot17=85.
\]
:::

<1>4. The Sylow $17$-subgroup of $K$ is unique and characteristic in $K$.
::: {.proof}
Let $m_{17}$ be the number of Sylow $17$-subgroups of $K$.
Since $|K|=5\cdot17$, Sylow's theorem gives
\[
m_{17}\equiv1\pmod{17}
\qquad\text{and}\qquad
m_{17}\mid5.
\]
Thus
\[
m_{17}=1.
\]
Let $P_{17}$ be this unique Sylow $17$-subgroup of $K$.
Every automorphism of $K$ sends a Sylow $17$-subgroup to a Sylow $17$-subgroup, so uniqueness implies
\[
P_{17}\operatorname{char}K.
\]
:::

<1>5. The Sylow $17$-subgroup $P_{17}$ is normal in $G$.
::: {.proof}
By <1>3,
\[
K\normal G,
\]
and by <1>4,
\[
P_{17}\operatorname{char}K.
\]
A characteristic subgroup of a normal subgroup is normal in the ambient group.
Hence
\[
P_{17}\normal G.
\]
Since $|P_{17}|=17$, it is a Sylow $17$-subgroup of $G$.
:::

<1>6. There is a normal subgroup $L\normal G$ of order $35=5\cdot7$.
::: {.proof}
Let $\overline Q$ be the unique Sylow $7$-subgroup of $\overline G$.
By <1>2,
\[
\overline Q\normal\overline G.
\]
Set
\[
L=\pi^{-1}(\overline Q).
\]
Then
\[
L\normal G
\]
and
\[
L/P_5\cong\overline Q.
\]
Therefore
\[
|L|=|P_5|\,|\overline Q|=5\cdot7=35.
\]
:::

<1>7. The Sylow $7$-subgroup of $L$ is unique and characteristic in $L$.
::: {.proof}
Let $m_7$ be the number of Sylow $7$-subgroups of $L$.
Since $|L|=5\cdot7$, Sylow's theorem gives
\[
m_7\equiv1\pmod7
\qquad\text{and}\qquad
m_7\mid5.
\]
Thus
\[
m_7=1.
\]
Let $P_7$ be this unique Sylow $7$-subgroup of $L$.
Every automorphism of $L$ preserves the unique Sylow $7$-subgroup, so
\[
P_7\operatorname{char}L.
\]
:::

<1>8. The Sylow $7$-subgroup $P_7$ is normal in $G$.
::: {.proof}
By <1>6,
\[
L\normal G,
\]
and by <1>7,
\[
P_7\operatorname{char}L.
\]
Therefore
\[
P_7\normal G.
\]
Since $|P_7|=7$, it is a Sylow $7$-subgroup of $G$.
:::

<1>9. Every Sylow subgroup of $G$ is normal.
::: {.proof}
The Sylow $5$-subgroup is normal by <1>1, the Sylow $17$-subgroup is normal by <1>5, and the Sylow $7$-subgroup is normal by <1>8. Hence all Sylow subgroups of $G$ are normal.
:::
:::
