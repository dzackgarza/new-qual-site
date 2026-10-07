---
schema: qual/card@1
id: P-ALGFINAL11-01
kind: problem
title: Classify groups of order 105
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be a group of order 105.

(a) Show that G has a normal subgroup of order 5 or 7. [points]:[4]

(b) Show that G has a cyclic normal subgroup of order 35. [4]

(c) Show that the Sylow 5- and 7-subgroups of G are both normal.
[3]

(d) Classify groups of order 105.
:::

::: {.solution}
Let $F$, $S$, and $T$ denote Sylow $5$-, $7$-, and $3$-subgroups of $G$, respectively.

<1>1. At least one of $F$ and $S$ is normal in $G$.
::: {.proof}
Sylow's theorems give
$$
n_5\equiv1\pmod5,
\qquad
n_5\mid21.
$$
The only possibilities are
$$
n_5=1\quad\text{or}\quad n_5=21.
$$
If $n_5=21$, then the Sylow $5$-subgroups, which intersect pairwise only in the identity, contribute
$$
21(5-1)=84
$$
nonidentity elements of order $5$.

Similarly,
$$
n_7\equiv1\pmod7,
\qquad
n_7\mid15,
$$
so
$$
n_7=1\quad\text{or}\quad n_7=15.
$$
If $n_7=15$, the Sylow $7$-subgroups contribute
$$
15(7-1)=90
$$
nonidentity elements of order $7$.

Both nonnormal cases cannot occur simultaneously, because
$$
84+90>104=|G|-1.
$$
Hence at least one of $F$ and $S$ is unique and therefore normal.
:::

<1>2. The subgroup
$$
N=FS
$$
is a cyclic normal subgroup of order $35$.
::: {.proof}
By step <1>1, at least one of $F$ and $S$ is normal, so $FS$ is a subgroup. Since
$$
F\cap S=1,
$$
one has
$$
|FS|=|F||S|=35.
$$

Any group of order $35=5\cdot7$ is cyclic: its Sylow $7$-subgroup is unique because $n_7\mid5$ and $n_7\equiv1\pmod7$, and its Sylow $5$-subgroup is unique because $n_5\mid7$ and $n_5\equiv1\pmod5$. Thus both are normal and commute, so
$$
FS\cong C_5\times C_7\cong C_{35}.
$$

Finally,
$$
[G:N]=3.
$$
Let $G$ act on the three left cosets of $N$. The image is a transitive subgroup of $S_3$, so its order is divisible by $3$; it also divides both $|G|=105$ and $|S_3|=6$, hence has order $3$. Therefore the kernel has index $3$ and is contained in the stabilizer $N$ of the coset $N$. Since both have order $35$, the kernel equals $N$. Hence
$$
N\trianglelefteq G.
$$
:::

<1>3. Both $F$ and $S$ are normal in $G$.
::: {.proof}
By step <1>2, $N$ is cyclic of order $35$. A cyclic group has unique subgroups of each order dividing its order, so $F$ and $S$ are respectively the unique subgroups of $N$ of orders $5$ and $7$. Hence both are characteristic in $N$.

Since
$$
F\char N\trianglelefteq G,
\qquad
S\char N\trianglelefteq G,
$$
both $F$ and $S$ are normal in $G$.
:::

<1>4. The subgroup $TS$ has order $21$, and
$$
G\cong F\times TS.
$$
::: {.proof}
Since $S\trianglelefteq G$ by step <1>3, the product $TS$ is a subgroup. Because $T\cap S=1$,
$$
|TS|=21.
$$
Also
$$
F\cap TS=1,
\qquad
|F||TS|=5\cdot21=105=|G|,
$$
so $G=F(TS)$.

Conjugation defines a homomorphism
$$
TS\longrightarrow\Aut(F).
$$
Since $F\cong C_5$,
$$
|\Aut(F)|=4.
$$
The image has order dividing both $21$ and $4$, hence is trivial. Therefore $TS$ centralizes $F$, and the multiplication map gives
$$
G\cong F\times TS.
$$
:::

<1>5. Up to isomorphism there are exactly two groups of order $21$:
$$
C_{21}
\qquad\text{and}\qquad
C_7\rtimes C_3,
$$
where the nontrivial action may be taken as
$$
bab^{-1}=a^2
$$
for $|a|=7$ and $|b|=3$.
::: {.proof}
For a group $H$ of order $21$, the Sylow $7$-subgroup is unique and therefore normal. If the Sylow $3$-subgroup is also normal, the two Sylow subgroups commute and
$$
H\cong C_7\times C_3\cong C_{21}.
$$

Otherwise $H$ is a nontrivial semidirect product
$$
C_7\rtimes C_3.
$$
Since
$$
\Aut(C_7)\cong C_6
$$
has a unique subgroup of order $3$, all nontrivial actions $C_3\to\Aut(C_7)$ have the same image and yield isomorphic semidirect products. The automorphism $a\mapsto a^2$ has order $3$ modulo $7$, giving the displayed presentation.
:::

<1>6. Therefore the groups of order $105$ are exactly
$$
\boxed{C_{105}}
$$
and
$$
\boxed{C_5\times(C_7\rtimes C_3)}.
$$
::: {.proof}
By step <1>4,
$$
G\cong C_5\times TS,
$$
where $|TS|=21$. Applying step <1>5 gives exactly the two displayed isomorphism types. In the cyclic case,
$$
C_5\times C_{21}\cong C_{105}
$$
because $\gcd(5,21)=1$.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), step <1>2 proves part (b), step <1>3 proves part (c), and step <1>6 gives the classification requested in part (d).
:::
:::
