---
schema: qual/card@1
id: P-ALGF23B
kind: problem
title: "Groups of order pm with a self-normalizing Sylow p-subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Suppose $G$ is a finite group, $p$ is prime, $m$ is an integer, $\gcd(p, m) = 1$, and $|G| = pm$.
Suppose $P$ is a Sylow $p$-subgroup and $N_G(P) = P$.

(a) Prove that if $G$ has a subgroup $H$ of order $m$, then $$H = \{x \in G \mid o(x) \neq p\}.$$ Deduce that in this case, $H$ is a characteristic subgroup.

(b) Suppose $G$ is solvable.
Prove that $G$ has a normal subgroup $N$ such that $G/N \cong \mathbb{Z}/\ell\mathbb{Z}$ for some prime $\ell$.

(c) Suppose $G$ is solvable.
Prove that $G$ has a normal subgroup of order $m$.

Hint: Use induction on $|G|$, the subgroup $N$ from the previous part, and a Sylow $\ell$-subgroup of $N$ if needed.
:::

::: {.solution}
<1>1. Part (a): $H = \{x \in G \mid o(x) \neq p\}$ and characteristic property:
<2>1. By the Sylow Theorems, the number of Sylow $p$-subgroups is:
\[
n_p = [G : N_G(P)] = \frac{|G|}{|P|} = \frac{pm}{p} = m.
\]
Proof: Orbit-Stabilizer on conjugates of $P$ with $N_G(P) = P$.
<2>2. Since $|P| = p$ is prime, any two distinct Sylow $p$-subgroups intersect in only the identity $\{e\}$.
Each of the $m$ Sylow $p$-subgroups contains exactly $p - 1$ elements of order $p$.
Thus the total number of elements of order $p$ in $G$ is:
\[
n_p (p - 1) = m(p - 1) = pm - m.
\]
Proof: disjoint union of non-identity elements of distinct Sylow $p$-subgroups.
<2>3. The number of elements in $G$ with order different from $p$ is:
\[
|G| - (pm - m) = pm - (pm - m) = m.
\]
Proof: complement in $G$.
<2>4. If $H \le G$ is a subgroup of order $m$, since $\gcd(p, m) = 1$, by Lagrange's Theorem no element of $H$ can have order $p$.
Thus $H \subseteq \{x \in G \mid o(x) \neq p\}$.
Because $|H| = m = |\{x \in G \mid o(x) \neq p\}|$, we have:
\[
H = \{x \in G \mid o(x) \neq p\}.
\]
Proof: equality of finite sets of identical cardinality.
<2>5. Because group automorphisms preserve element orders, for any $\sigma \in \operatorname{Aut}(G)$ we have $\sigma(H) = H$.
Thus $H$ is a characteristic subgroup of $G$.
Proof: definition of characteristic subgroup.

<1>2. Part (b): Existence of a normal subgroup with prime cyclic quotient:
<2>1. Since $G$ is solvable and non-trivial ($|G| = pm \ge 2$), the commutator subgroup $[G, G] \subsetneq G$ is a proper normal subgroup.
The quotient $G^{\mathrm{ab}} = G / [G, G]$ is a non-trivial finite abelian group.
Proof: derived series terminates at $\{e\}$.
<2>2. Let $\ell$ be a prime divisor of $|G^{\mathrm{ab}}|$.
By Cauchy's Theorem for finite abelian groups, $G^{\mathrm{ab}}$ has a subgroup of index $\ell$.
The preimage of this subgroup under the quotient map $G \twoheadrightarrow G^{\mathrm{ab}}$ is a normal subgroup $N \triangleleft G$ such that:
\[
G / N \cong \mathbb{Z} / \ell\mathbb{Z}.
\]
Proof: correspondence theorem for normal subgroups.

<1>3. Part (c): Existence of a normal subgroup of order $m$:
<2>1. We proceed by induction on $|G| = pm$.
If $m = 1$, then $H = \{e\}$ is normal of order 1.
Proof: base case.
<2>2. By Part (b), let $N \triangleleft G$ with $[G : N] = \ell$ for some prime $\ell$.
- **Case 1 ($\ell = p$):** If $\ell = p$, then $|N| = m$. By Part (a), $N$ is characteristic in $G$, hence normal of order $m$.
Proof: $[G:N]=p \implies |N|=m$.
- **Case 2 ($\ell \mid m$):** If $\ell \mid m$, then $|N| = p(m/\ell)$.
In $N$, the Sylow $p$-subgroup $P$ satisfies $N_N(P) = N \cap N_G(P) = N \cap P = P$.
By the inductive hypothesis applied to $N$, $N$ has a normal subgroup $H_0$ of order $m/\ell$.
Proof: inductive hypothesis on the solvable group $N$.
<2>3. By Part (a) applied to $N$, $H_0$ is characteristic in $N$.
Since $H_0 \operatorname{char} N$ and $N \triangleleft G$, we have $H_0 \triangleleft G$.
Proof: characteristic subgroup of a normal subgroup is normal.
<2>4. Consider the quotient $\overline{G} = G / H_0$.
Then $|\overline{G}| = |G| / |H_0| = pm / (m/\ell) = p\ell$.
Since $|\overline{G}| < |G|$, by induction $\overline{G}$ has a normal subgroup $\overline{K} \triangleleft \overline{G}$ of order $\ell$.
Proof: inductive hypothesis on $\overline{G}$.
<2>5. The preimage $K \le G$ of $\overline{K}$ under $G \to G/H_0$ is normal in $G$ and has order:
\[
|K| = |\overline{K}| \cdot |H_0| = \ell \cdot \frac{m}{\ell} = m.
\]
Thus $K$ is a normal subgroup of $G$ of order $m$.
Proof: Correspondence Theorem.

<1>4. Conclusion:
Parts (a), (b), and (c) are proven. Q.E.D.
Proof: <1>1 through <1>3.
:::
