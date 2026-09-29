---
schema: qual/card@1
id: P-4TYWT
kind: problem
title: Groups of order $p^2q^2$ have a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
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

::: {.problem}
- Show that a group of order $p^2 q^2$ has a normal Sylow subgroup.
:::

::: {.solution}
If $p=q$, then $G$ itself is the unique Sylow $p$-subgroup, so assume $p\neq q$ and, after interchanging the primes, $p<q$.

::: pf

::: pf-step

The number $n_q$ of Sylow $q$-subgroups is either $1$ or $p^2$.

::: pf-proof

Sylow's theorems give
\[
n_q\mid p^2,
\qquad
n_q\equiv1\pmod q.
\]
Thus $n_q\in\{1,p,p^2\}$. Since $1<p<q$, the possibility $n_q=p$ is incompatible with $n_q\equiv1\pmod q$. Hence $n_q=1$ or $p^2$.

:::

:::

::: {.pf-step #s2}

If $n_q=p^2$, then $(p,q)=(2,3)$.

::: pf-proof

The congruence $p^2\equiv1\pmod q$ gives
\[
q\mid(p-1)(p+1).
\]
Because $q>p$, one cannot have $q\mid p-1$, so $q\mid p+1$. Since $0<p+1<2q$, this forces $q=p+1$. The only consecutive primes are $2$ and $3$, so $p=2$ and $q=3$.

:::

:::

::: {.pf-step #s3}

Unless $|G|=36$, $G$ has a normal Sylow $q$-subgroup.

::: pf-proof

If $n_q=1$, the Sylow $q$-subgroup is normal. By step [](#s2){.pf-ref}, the only way $n_q\neq1$ can occur is $p=2$, $q=3$, which gives $|G|=36$.

:::

:::

::: {.pf-step #s4}

Now suppose $|G|=36$. If the Sylow $3$-subgroup is not normal, then $n_3=4$ and conjugation on the four Sylow $3$-subgroups gives a homomorphism
\[
\varphi:G\longrightarrow S_4
\]
whose kernel $K$ has order $3$ or $9$.

::: pf-proof

Sylow gives $n_3=1$ or $4$. Assume $n_3=4$. The action is transitive, and the stabilizer of a Sylow $3$-subgroup $Q$ is $N_G(Q)$, of order $36/4=9$. Thus $K\subseteq N_G(Q)$, so $|K|\mid9$. Since $G/K$ embeds in $S_4$, $K$ cannot be trivial because $36\nmid24$. Hence $|K|=3$ or $9$.

:::

:::

::: {.pf-step #s5}

If $|K|=9$, then $K$ is a normal Sylow $3$-subgroup. Hence, when no Sylow $3$-subgroup is normal, $|K|=3$ and $G/K\cong A_4$.

::: pf-proof

The first assertion is immediate from $K\trianglelefteq G$. In the remaining case $|K|=3$, the image has order $36/3=12$. A subgroup of order $12$ in $S_4$ has index $2$ and is therefore the unique index-$2$ subgroup $A_4$.

:::

:::

::: {.pf-step #s6}

Under the assumptions of step [](#s5){.pf-ref}, $K\subseteq Z(G)$.

::: pf-proof

Conjugation on the normal subgroup $K\cong C_3$ gives
\[
G\longrightarrow\operatorname{Aut}(K)\cong C_2.
\]
If this map were nontrivial, its kernel $H$ would be normal of order $18$. Sylow's theorem in $H$ gives
\[
n_3(H)\mid2,
\qquad
n_3(H)\equiv1\pmod3,
\]
so $n_3(H)=1$. Its unique subgroup of order $9$ is characteristic in $H$, hence normal in $G$, and is a Sylow $3$-subgroup of $G$, contrary to step [](#s5){.pf-ref}. Therefore the conjugation action on $K$ is trivial, so $K\subseteq Z(G)$.

:::

:::

::: {.pf-step #s7}

In the remaining order-$36$ case, $G$ has a normal Sylow $2$-subgroup.

::: pf-proof

Let $V_4\trianglelefteq A_4$ be its unique Sylow $2$-subgroup and put
\[
N=\varphi^{-1}(V_4).
\]
Then $N\trianglelefteq G$ and $|N|=|K||V_4|=12$. Let $P$ be a Sylow $2$-subgroup of $N$; then $|P|=4$, so $P$ is also a Sylow $2$-subgroup of $G$. Since $K\cap P=1$ and $K\subseteq Z(G)$ by step [](#s6){.pf-ref},
\[
|KP|=|K||P|=12=|N|,
\]
so $N=KP$. Every element of $N$ is $kp'$ with $k\in K$, $p'\in P$, and centrality of $K$ gives
\[
(kp')P(kp')^{-1}=p'Pp'^{-1}=P.
\]
Thus $P\trianglelefteq N$. It is therefore the unique Sylow $2$-subgroup of $N$, hence characteristic in $N$. Since $N\trianglelefteq G$, we get $P\trianglelefteq G$.

:::

:::

::: pf-step

Therefore every group of order $p^2q^2$ has a normal Sylow subgroup.

::: pf-proof

Combine step [](#s3){.pf-ref} with the order-$36$ analysis in steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

:::

:::
