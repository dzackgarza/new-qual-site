---
schema: qual/card@1
id: P-MMAQ-JCG7I3RIX7
kind: problem
title: A group with a subgroup of index $n$ has a normal subgroup $N$ with $n\leq[G:N]\leq
  n!$, and there is no simple group of order $36$
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Simple Groups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
- Let $G$ be a group (not necessarily finite) that contains a subgroup of index $n$.
  Show that $G$ contains a `\textit{normal}`{=tex} subgroup $N$ such that $n\leq[G:N]\leq n!$

- Use part (a) to show that there is no simple group of order 36.
:::

::: {.solution}
<1>1. Part (a): Normal core and index bounds:
<2>1. Let $H \le G$ be a subgroup of index $[G : H] = n$.
Let $X = G/H = \{x_1 H, \dots, x_n H\}$ be the set of left cosets of $H$ in $G$, with $|X| = n$.
::: {.proof}
definition of index.
:::
<2>2. The group $G$ acts on $X$ by left multiplication: $g \cdot (x H) = (gx) H$.
This action induces a group homomorphism:
\[
\rho: G \to S(X) \cong S_n.
\]
::: {.proof}
group action on cosets.
:::
<2>3. Define $N = \ker(\rho) = \bigcap_{g \in G} g H g^{-1} = \operatorname{Core}_G(H)$.
$N$ is a normal subgroup of $G$ ($N \trianglelefteq G$).
::: {.proof}
kernel of a group homomorphism is normal.
:::
<2>4. By the First Isomorphism Theorem, $G/N \cong \operatorname{im}(\rho) \le S_n$.
Thus $[G : N] = |G/N| = |\operatorname{im}(\rho)|$ divides $|S_n| = n!$, so $[G : N] \le n!$.
::: {.proof}
Lagrange's Theorem for subgroups of $S_n$.
:::
<2>5. Furthermore, $N = \ker(\rho) \subseteq H$ because for any $g \in N$, $g \cdot (eH) = eH \implies g \in H$.
By multiplicativity of indices:
\[
[G : N] = [G : H][H : N] = n [H : N] \ge n.
\]
Thus $n \le [G : N] \le n!$, and $[G : N] \mid n!$.
::: {.proof}
tower law for subgroup indices.
:::

<1>2. Part (b): No simple group of order 36:
<2>1. Suppose for contradiction that there exists a simple group $G$ of order $|G| = 36 = 2^2 \cdot 3^2$.
::: {.proof}
assumption for contradiction.
:::
<2>2. By Sylow’s Third Theorem, the number $n_3$ of Sylow 3-subgroups satisfies:
\[
n_3 \equiv 1 \pmod 3 \quad \text{and} \quad n_3 \mid 4 \implies n_3 \in \{1, 4\}.
\]
::: {.proof}
Sylow's Theorem.
:::
<2>3. If $n_3 = 1$, the unique Sylow 3-subgroup $P$ is normal in $G$ with $|P| = 9$.
Since $1 < 9 < 36$, $P$ is a non-trivial proper normal subgroup, contradicting simplicity.
::: {.proof}
unique Sylow subgroups are normal.
:::
<2>4. If $n_3 = 4$, let $P$ be a Sylow 3-subgroup of order 9.
Its index in $G$ is $[G : P] = 36 / 9 = 4$.
::: {.proof}
Lagrange's Theorem.
:::
<2>5. Apply Part (a) to $H = P$ with $n = 4$:
There exists a normal subgroup $N \trianglelefteq G$ such that $N \subseteq P$ and $[G : N]$ divides $4! = 24$.
::: {.proof}
Part (a).
:::
<2>6. Since $G$ is assumed simple, its only normal subgroups are $N = \{e\}$ and $N = G$:
- If $N = G$, then $N \subseteq P \implies G \subseteq P$, which is impossible since $|P| = 9 < 36$.
- If $N = \{e\}$, then $[G : N] = |G| = 36$. But by <2>5, $[G : N]$ must divide 24, and 36 does not divide 24.
Both cases yield a contradiction.
::: {.proof}
divisibility in $\mathbb{Z}$.
:::

<1>3. Conclusion:
There is no simple group of order 36. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
