---
schema: qual/card@1
id: P-HGRO29
kind: problem
title: Composite-order groups below 60 are not simple
classification:
  areas: [algebra]
  topics: [Group Theory, Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $G$ be a finite group with composite order less than $60$.
Prove that $G$ is not simple.
:::

::: solution
Assume throughout that $|G|=n<60$ is composite.

<1>1. If $n$ is a prime power, then $G$ is not simple.
::: proof
Let $n=p^a$ with $a\ge2$. A finite $p$-group has nontrivial center. If
$Z(G)\ne G$, then $Z(G)$ is a nontrivial proper normal subgroup. If $Z(G)=G$,
then $G$ is abelian; a finite abelian simple group has prime order, contradicting
that $p^a$ is composite.
:::

<1>2. Apart from
\[
12,24,30,36,48,56,
\]
every non-prime-power composite $n<60$ forces a unique Sylow subgroup.
::: proof
If $p^a\Vert n$, the number $n_p$ of Sylow $p$-subgroups must satisfy
\[
n_p\equiv1\pmod p,
\qquad
n_p\mid \frac{n}{p^a}.
\]
For every non-prime-power composite $n<60$ outside the six displayed values,
the following table gives a prime $p$ for which the only divisor of
$n/p^a$ congruent to $1$ modulo $p$ is $1$:
\[
\begin{array}{c|l}
p & n \\
\hline
3 & 6,15,18,33,45,51,54\\
5 & 10,20,35,40,50\\
7 & 14,21,28,42\\
11 & 22,44,55\\
13 & 26,39,52\\
17 & 34\\
19 & 38,57\\
23 & 46\\
29 & 58.
\end{array}
\]
Thus $n_p=1$ in each listed case, so the Sylow $p$-subgroup is a nontrivial
proper normal subgroup.
:::

<1>3. A group of order $12$ is not simple.
::: proof
The number $n_3$ of Sylow $3$-subgroups is $1$ or $4$. If $n_3=1$, the Sylow
$3$-subgroup is normal. If $n_3=4$, the four Sylow $3$-subgroups contribute
$4(3-1)=8$ nonidentity elements. Only three nonidentity elements remain, so
every Sylow $2$-subgroup of order $4$ consists of the identity together with
those same three elements. Hence the Sylow $2$-subgroup is unique and normal.
:::

<1>4. A group of order $24$ is not simple.
::: proof
If the Sylow $3$-subgroup is unique, we are done. Otherwise $n_3=4$. Conjugation
on the four Sylow $3$-subgroups gives a nontrivial homomorphism
\[
\varphi:G\to S_4.
\]
If $G$ were simple, $\ker\varphi$ would be trivial, so $G$ would embed in
$S_4$. Since both groups have order $24$, this would give $G\cong S_4$, but
$S_4$ is not simple because $A_4\trianglelefteq S_4$. Contradiction.
:::

<1>5. A group of order $30$ is not simple.
::: proof
If neither the Sylow $5$-subgroup nor the Sylow $3$-subgroup were unique, then
\[
n_5=6,
\qquad
n_3=10.
\]
Distinct subgroups of prime order intersect trivially, so the Sylow $5$-subgroups
would contribute $6(5-1)=24$ nonidentity elements and the Sylow $3$-subgroups
would contribute $10(3-1)=20$ more. This exceeds $30$. Hence one of these
Sylow subgroups is unique and normal.
:::

<1>6. A group of order $36$ is not simple.
::: proof
Here $n_3=1$ or $4$. If $n_3=1$, the Sylow $3$-subgroup is normal. If $n_3=4$,
conjugation on the four Sylow $3$-subgroups gives
\[
\varphi:G\to S_4.
\]
The action is transitive, so $4$ divides $|\operatorname{im}\varphi|$; also the
image order divides both $36$ and $24$. Hence it is $4$ or $12$, and therefore
\[
|\ker\varphi|=9\text{ or }3.
\]
Thus $G$ has a nontrivial proper normal subgroup.
:::

<1>7. A group of order $48$ is not simple.
::: proof
The number $n_3$ is $1$, $4$, or $16$. If $n_3=1$, we are done. If $n_3=4$,
the conjugation action on the four Sylow $3$-subgroups gives a nontrivial map
$G\to S_4$; simplicity would force an embedding, impossible because
$48>|S_4|=24$.

If $n_3=16$, the Sylow $3$-subgroups contribute
\[
16(3-1)=32
\]
nonidentity elements. Exactly $15$ nonidentity elements remain. A Sylow
$2$-subgroup has order $16$, so its $15$ nonidentity elements must be exactly
those remaining elements. Hence every Sylow $2$-subgroup is the same subgroup,
so it is unique and normal.
:::

<1>8. A group of order $56$ is not simple.
::: proof
The number $n_7$ is $1$ or $8$. If $n_7=1$, the Sylow $7$-subgroup is normal.
If $n_7=8$, the eight Sylow $7$-subgroups contribute
\[
8(7-1)=48
\]
nonidentity elements. Exactly seven nonidentity elements remain. A Sylow
$2$-subgroup has order $8$, so its seven nonidentity elements must be precisely
those remaining elements. Therefore the Sylow $2$-subgroup is unique and
normal.
:::

<1>9. Therefore every group of composite order less than $60$ is not simple.
::: proof
Prime-power orders are covered by <1>1. Every other composite order below $60$
is either in the table of <1>2 or is one of the six residual orders handled in
<1>3--<1>8.
:::
:::
