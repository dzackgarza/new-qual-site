---
schema: qual/card@1
id: P-7ONAR
kind: problem
title: Sylow theorems
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
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
State/prove the Sylow theorems.
:::

::: {.solution}
Let $G$ be finite and write
$$
\abs{G}=p^a m,
\qquad p\nmid m.
$$
A subgroup of order $p^a$ is called a Sylow $p$-subgroup.

::: pf

::: pf-step

A Sylow $p$-subgroup of $G$ exists (the first Sylow theorem).

::: pf-proof

We argue by induction on $\abs{G}$. If $p\nmid\abs{G}$, then $a=0$ and the trivial subgroup is Sylow. Assume $p\mid \abs{G}$.

If $p\mid \abs{Z(G)}$, Cauchy's theorem gives a central subgroup $C\le Z(G)$ of order $p$. Then
$$
\abs{G/C}=p^{a-1}m.
$$
By induction, $G/C$ has a subgroup $\overline P$ of order $p^{a-1}$. Its inverse image $P$ in $G$ has order $p^a$.

Now suppose $p\nmid \abs{Z(G)}$. The class equation is
$$
\abs{G}=\abs{Z(G)}+\sum_i [G:C_G(x_i)],
$$
where the $x_i$ represent the noncentral conjugacy classes. If every index $[G:C_G(x_i)]$ were divisible by $p$, then the right side would be congruent to $\abs{Z(G)}\not\equiv0\pmod p$, contradicting $p\mid\abs{G}$. Thus for some noncentral $x$,
$$
p\nmid [G:C_G(x)].
$$
Hence the full $p$-part $p^a$ of $\abs{G}$ divides $\abs{C_G(x)}$. Since $x$ is noncentral, $C_G(x)<G$, so induction applied to $C_G(x)$ gives a subgroup of order $p^a$. This is a Sylow $p$-subgroup of $G$.

:::

:::

::: {.pf-step #s2}

If $P$ is a Sylow $p$-subgroup and $H\le G$ is any $p$-subgroup, then $H$ is contained in a conjugate of $P$. In particular, all Sylow $p$-subgroups are conjugate (the second Sylow theorem).

::: pf-proof

Let $H$ act by left multiplication on the set $G/P$ of left cosets. The number of cosets is
$$
[G:P]=m,
$$
which is not divisible by $p$. Every $H$-orbit has size a power of $p$. If every orbit had size divisible by $p$, then $p$ would divide $\abs{G/P}=m$, impossible. Thus there is a fixed coset $gP$.

The equality
$$
hgP=gP\qquad(h\in H)
$$
is equivalent to
$$
g^{-1}hg\in P\qquad(h\in H).
$$
Hence
$$
g^{-1}Hg\le P,
$$
or equivalently $H\le gPg^{-1}$.

If $H$ is itself Sylow, then $\abs{H}=\abs{P}$, so containment forces equality. Thus every Sylow $p$-subgroup is conjugate to $P$.

:::

:::

::: pf-step

The number $n_p$ of Sylow $p$-subgroups satisfies
$$
n_p\mid m
\qquad\text{and}\qquad
n_p\equiv1\pmod p
$$
(the third Sylow theorem).

::: pf-proof

By step [](#s2){.pf-ref}, the Sylow $p$-subgroups form one conjugacy orbit. The stabilizer of $P$ under conjugation is its normalizer $N_G(P)$, so orbit-stabilizer gives
$$
n_p=[G:N_G(P)].
$$
Since $P\le N_G(P)$,
$$
[G:P]=[G:N_G(P)]\,[N_G(P):P]=n_p[N_G(P):P].
$$
Thus $n_p\mid [G:P]=m$.

For the congruence, let $P$ act by conjugation on the set $\Syl_p(G)$. Every orbit has size a power of $p$. We claim that $P$ is the unique fixed point. Certainly $P$ fixes itself. If another Sylow subgroup $Q$ is fixed, then $P\le N_G(Q)$. Since $Q\trianglelefteq N_G(Q)$, the product $PQ$ is a subgroup of $N_G(Q)$; it is a $p$-subgroup of $G$. Maximality of the Sylow subgroup $Q$ forces $PQ=Q$, hence $P\le Q$. Since $\abs{P}=\abs{Q}$, we get $P=Q$.

Therefore all orbits except the singleton $\{P\}$ have cardinality divisible by $p$, so
$$
n_p\equiv1\pmod p.
$$

:::

:::

:::

:::
