---
schema: qual/card@1
id: P-MMAQ-RQA4XXNOF3
kind: problem
title: No simple group of order $30$, and simple groups of order $60$ are isomorphic
  to $A_5$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
In this problem, as you apply Sylow's Theorem, state precisely which portions you are using.

- Prove that there is no simple group of order 30.

- Suppose that $G$ is a simple group of order 60. Determine the number of $p$-Sylow subgroups of $G$ for each prime $p$ dividing 60, then prove that $G$ is isomorphic to the alternating group $A_5$.

> Note: in the second part, you needn't show that $A_5$ is simple.
> You need only show that if there is a simple group of order 60, then it must be isomorphic to $A_5$.
:::


::: {.solution}
<1>1. There is no simple group of order $30$.
::: {.proof}
Suppose $|G|=30$ and $G$ is simple. By Sylow's third theorem,
\[
n_5\equiv1\pmod5,\qquad n_5\mid6,
\]
so $n_5\in\{1,6\}$. Simplicity rules out $n_5=1$, because a unique Sylow subgroup is normal by Sylow's second theorem. Hence $n_5=6$.

Similarly,
\[
n_3\equiv1\pmod3,\qquad n_3\mid10,
\]
so $n_3\in\{1,10\}$, and simplicity forces $n_3=10$.

Distinct Sylow subgroups of prime order intersect trivially. Thus the six Sylow $5$-subgroups contribute
\[
6(5-1)=24
\]
nonidentity elements of order $5$, while the ten Sylow $3$-subgroups contribute
\[
10(3-1)=20
\]
nonidentity elements of order $3$. These sets are disjoint, so together with the identity they would give at least
\[
1+24+20=45>30
\]
elements, a contradiction.
:::

<1>2. Now suppose $G$ is simple of order $60$. Then
\[
n_5=6,\qquad n_3=10.
\]
::: {.proof}
For $p=5$, Sylow's third theorem gives
\[
n_5\equiv1\pmod5,\qquad n_5\mid12,
\]
so $n_5\in\{1,6\}$. Simplicity excludes $1$, hence $n_5=6$.

For $p=3$,
\[
n_3\equiv1\pmod3,\qquad n_3\mid20,
\]
so $n_3\in\{1,4,10\}$. The value $1$ is excluded by simplicity. If $n_3=4$, conjugation on the four Sylow $3$-subgroups gives a nontrivial homomorphism
\[
G\longrightarrow S_4.
\]
Its kernel is normal. Since $G$ is simple and the action is nontrivial, the map would be injective, impossible because $60\nmid24$. Therefore $n_3=10$.
:::

<1>3. The number $n_2$ of Sylow $2$-subgroups satisfies
\[
n_2\in\{5,15\}.
\]
::: {.proof}
Sylow's third theorem gives
\[
n_2\equiv1\pmod2,\qquad n_2\mid15,
\]
so $n_2\in\{1,3,5,15\}$. The value $1$ is excluded by simplicity. If $n_2=3$, conjugation on the three Sylow $2$-subgroups gives a nontrivial homomorphism $G\to S_3$, which by simplicity would be injective; this is impossible because $60>6$. Hence only $5$ and $15$ remain.
:::

<1>4. If $n_2=5$, then $G$ embeds in $S_5$.
::: {.proof}
Conjugation gives a transitive action of $G$ on its five Sylow $2$-subgroups, hence a nontrivial homomorphism
\[
\varphi:G\longrightarrow S_5.
\]
Its kernel is normal. Since $G$ is simple and the action is nontrivial, $\ker\varphi=1$, so $\varphi$ is injective.
:::

<1>5. If $n_2=15$, then $G$ still has a subgroup of index $5$, and hence still embeds in $S_5$.
::: {.proof}
By <1>2, $n_5=6$, so the Sylow $5$-subgroups contribute exactly
\[
6(5-1)=24
\]
nonidentity elements. Hence only $60-24=36$ elements, including the identity, remain outside those subgroups.

If the fifteen Sylow $2$-subgroups were pairwise disjoint away from the identity, they would contribute
\[
15(4-1)=45
\]
nonidentity elements, impossible. Therefore two distinct Sylow $2$-subgroups $P,Q$ intersect nontrivially. Since $|P|=|Q|=4$, their intersection has order $2$; let
\[
P\cap Q=\langle x\rangle,\qquad x\ne1.
\]
Every group of order $4$ is abelian, so both $P$ and $Q$ centralize $x$. Thus
\[
P,Q\le C_G(x).
\]
Because $P\ne Q$, the centralizer strictly contains $P$. Its order divides $60$ and is divisible by $4$, so
\[
|C_G(x)|\in\{12,20,60\}.
\]
The value $60$ would put $x$ in $Z(G)$, impossible because a nonabelian simple group has trivial center. The value $20$ would give a subgroup of index $3$; the coset action on three points would produce a nontrivial homomorphism $G\to S_3$, hence an injection by simplicity, again impossible. Therefore
\[
|C_G(x)|=12,
\]
so $C_G(x)$ has index $5$.

The action of $G$ on the five left cosets of $C_G(x)$ gives a nontrivial homomorphism $G\to S_5$. By simplicity its kernel is trivial, hence $G$ embeds in $S_5$.
:::

<1>6. In either case,
\[
G\cong A_5.
\]
::: {.proof}
By <1>4 and <1>5, there is an injective homomorphism
\[
G\hookrightarrow S_5.
\]
Its image has order $60$, hence index $2$ in $S_5$. Every index-$2$ subgroup is the kernel of a surjection $S_5\to C_2$. All transpositions are conjugate and generate $S_5$, so any nontrivial homomorphism $S_5\to C_2$ sends every transposition to the nontrivial element; hence it is the sign homomorphism. Therefore the unique index-$2$ subgroup of $S_5$ is
\[
\ker(\operatorname{sgn})=A_5.
\]
Thus the image of $G$ is $A_5$, and $G\cong A_5$.
:::

<1>7. Consequently, for a simple group $G$ of order $60$,
\[
\boxed{n_2=5,\qquad n_3=10,\qquad n_5=6}.
\]
::: {.proof}
The values of $n_3$ and $n_5$ were proved in <1>2. By <1>6, $G\cong A_5$. The Sylow $2$-subgroups of $A_5$ are the five Klein four groups
\[
V_i=\{1\}\cup\{(ab)(cd):\{a,b,c,d\}=\{1,2,3,4,5\}\setminus\{i\}\},
\]
one for each fixed letter $i$. Hence $n_2=5$.
:::
:::
