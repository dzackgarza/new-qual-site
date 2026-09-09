---
schema: qual/card@1
id: P-J77DY
kind: problem
title: No simple group of order $p^2 q^2$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that no group of order $p^2q^2$ is simple for primes $p<q$.
:::

::: {.solution}
If $p=q$, then $G$ is a $p$-group and has nontrivial center, so it is not simple. Assume $p<q$.

<1>1. The number $n_q$ of Sylow $q$-subgroups is either $1$ or $p^2$.
::: {.proof}
Sylow gives
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
Thus $n_q\in\{1,p,p^2\}$. Since $1<p<q$, the possibility $n_q=p$ is impossible. Hence $n_q=1$ or $p^2$.
:::

<1>2. If $n_q=p^2$, then $(p,q)=(2,3)$.
::: {.proof}
The congruence $p^2\equiv1\pmod q$ gives
\[
q\mid(p-1)(p+1).
\]
Because $q>p$, one cannot have $q\mid p-1$, so $q\mid p+1$. Since $0<p+1<2q$, this forces $q=p+1$. The only consecutive primes are $2$ and $3$.
:::

<1>3. Unless $|G|=36$, the Sylow $q$-subgroup is normal, so $G$ is not simple.
::: {.proof}
If $n_q=1$, the unique Sylow $q$-subgroup is a nontrivial proper normal subgroup. By <1>2, the only remaining case is $p=2$, $q=3$.
:::

<1>4. Suppose $|G|=36$ and no Sylow $3$-subgroup is normal. Then $n_3=4$, and conjugation on the four Sylow $3$-subgroups gives
\[
\varphi:G\longrightarrow S_4
\]
with kernel $K$ of order $3$ or $9$.
::: {.proof}
The action is transitive. The stabilizer of a Sylow $3$-subgroup $Q$ is $N_G(Q)$, of order $36/4=9$, so $K\subseteq N_G(Q)$ and $|K|\mid9$. Since $G/K$ embeds in $S_4$, $K$ cannot be trivial because $36\nmid24$. Hence $|K|=3$ or $9$.
:::

<1>5. If $|K|=9$, then $K$ itself is a normal Sylow $3$-subgroup. Thus in the remaining case $|K|=3$ and $G/K\cong A_4$.
::: {.proof}
When $|K|=3$, the image has order $12$. A subgroup of order $12$ in $S_4$ has index $2$, hence is $A_4$.
:::

<1>6. In the remaining case, $K\subseteq Z(G)$.
::: {.proof}
Conjugation on $K\cong C_3$ gives a homomorphism
\[
G\longrightarrow\Aut(K)\cong C_2.
\]
If it were nontrivial, its kernel $H$ would be normal of order $18$. Sylow's theorem in $H$ gives a unique Sylow $3$-subgroup of order $9$, hence a characteristic subgroup of $H$ and therefore a normal Sylow $3$-subgroup of $G$, contradiction. Thus conjugation on $K$ is trivial.
:::

<1>7. The remaining order-$36$ case has a normal Sylow $2$-subgroup.
::: {.proof}
Let $V_4\trianglelefteq A_4$ be the Klein four subgroup and put
\[
N=\varphi^{-1}(V_4).
\]
Then $N\trianglelefteq G$ and $|N|=12$. Let $P$ be a Sylow $2$-subgroup of $N$, so $|P|=4$. Since $K\cap P=1$, $K\subseteq Z(G)$, and $|KP|=12$, we have $N=KP$.

For $k\in K$ and $p'\in P$, centrality of $K$ gives
\[
(kp')P(kp')^{-1}=p'P(p')^{-1}=P.
\]
Hence $P\trianglelefteq N$. It is therefore the unique Sylow $2$-subgroup of $N$, hence characteristic in $N$. Since $N\trianglelefteq G$, we get $P\trianglelefteq G$.
:::

Thus every group of order $p^2q^2$ has a nontrivial proper normal subgroup, so no such group is simple.
:::
