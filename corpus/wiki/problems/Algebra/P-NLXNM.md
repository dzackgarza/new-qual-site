---
schema: qual/card@1
id: P-NLXNM
kind: problem
title: Conjugation on Sylow $p$-subgroups; $|G|$ divides $n_p!$ if $G$ is simple;
  no simple group of order $ap^k$ for $1\le a\le 4$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Group Actions
relations: []
review: draft
---

:::{.problem}
Let $G$ be a finite group and $p$ a prime number. Let
$X_p$ be the set of Sylow-$p$ subgroups of $G$ and $n_p$ be the
cardinality of $X_p$. Let $\mathrm{Sym}(X)$ be the permutation group on
the set $X_p$.

1.  Construct a homomorphism $\rho: G \to \mathrm{Sym}(X_p)$ with image
    a transitive subgroup (i.e. with a single orbit).

2.  Deduce that if $G$ is simple then the order of $G$ divides $n_p!$.

3.  Show that for any $1\leq a \leq 4$ and any prime power $p^k$, no
    group of order $ap^k$ is simple.
:::

:::{.solution}
\envlist

1.  Define the required group action by $$\begin{aligned}
            \rho: G \to \mathrm{Sym}(X_p) \\
            g \mapsto (\gamma_g: P \mapsto gPg^{-1}).
        \end{aligned}$$ The claim is that this action is transitive on
    $X_p$. This can be equivalently stated as
    $$\forall P \in X_p, \exists g \in G, P' \in X_p \mid gP'g^{-1} = P.$$

    However, by Sylow 2, all Sylow $p-$subgroups are conjugate to each
    other, and thus this condition is satisfied.

2.  Suppose that $G$ is simple, so that we have
    $$H \trianglelefteq G \implies H = \{ e \} \text{ or } H = G.$$

    Note that $\mathrm{Sym}(X_p) = (n_p)!$, and if we have an injective
    homomorphism $G \xrightarrow{\phi} \mathrm{Sym}(X_p)$, then
    $|G| = |\phi(G)|$, since $\phi(G) \leq \mathrm{Sym}(X_p)$ will be a
    subgroup and thus have order dividing $(n_p)!$, which proves the
    statement.

    Using the $\phi$ defined in (1), we can apply the first isomorphism
    theorem
    $$G / \ker \phi \cong \mathrm{im} \phi \leq \mathrm{Sym}(X_p),$$ and
    so it suffices to show that $\ker \phi = \{e\}$.

    Note that since $\ker \phi \trianglelefteq G$ and $G$ is simple, we
    can only have $\ker \phi = \{e\}$ or $\ker \phi = G$.

    Towards a contradiction, suppose $\ker \phi = G$.

    By definition, we have $$\begin{aligned}
        \ker \phi &= \{ g\in G \mid \gamma_g = \mathrm{id}_{X_p} \} \\
        &= \{ g\in G \mid \forall P \in X_p,~ gPg^{-1} = P \} \\
        &= \bigcap_{P \in X_p} N_G(P),
        \end{aligned}$$

    and so the kernel of $\varphi$ is the intersection of all of the
    normalizers of the Sylow $p-$subgroups.

    But this means that $N_G(P) = G$ for every Sylow $p-$subgroup, which
    means that $n_p = 1$ and there is a unique $P$ which must be normal
    in $G$. Since $G$ is simple, this forces $P$ to be trivial or the
    whole group.

    Towards a contradiction, suppose $P = G$. Then $G$ is a $p-$group
    and thus has order $p^n$. But then $G$ has normal subgroups of order
    $p^k$ for all $0 < k < n$, contradicting the simplicity of $G$.

    But the only other option is that $P$ is trivial, whereas we know
    nontrivial Sylow $p-$subgroups exist by Sylow 1.

    Thus we can not have $\ker \phi = G$, and so $\ker \phi$ is trivial
    as desired.

3.  Suppose $\left| G \right| = ap^k$, where $1 \leq a \leq 4$. Then by
    Sylow 3, we have $n_p = 1 \mod p$ and $n_p$ divides $a$. If $a=1$,
    then $n_p = 1$, and so $G$ can not be simple. Moreover, if
    $p \geq a$, then $n_p \leq a$ and $n_p = 1\mod p$ forces $n_p = 1$
    again.

    So we can restrict our attention to $2 \leq a \leq 4$ and
    $p = 2, 3$, which reduces to checking the cases
    $ap^k = 2 (3^k), 4 (3^k)$, or $3 (2^k)$ for $k\geq 1$.

    If $ap^k = 2(3^k)$, we have $n_3 = 1 \mod 3$ and $n_3 \divides 2$,
    which forces $n_3 = 1$, so this can not be a simple group.

    Similarly, if $ap^k = 4(3^k)$, then $n_3 = 1 \mod 3$ and $n_3$
    divides 4, which forces $n_3 = 1$ and thus $G$ can't be simple.

    If $ap^k = 3(2^k)$, then $n_2 = 1 \mod 2$ and $n_2$ divides 3, so
    $n_2 = 1, 3$. But then $n_3! = 6$, and if $k > 1$, we have
    $3(2^k) > 6 = n_3!$, so $G$ can not be simple by the result in (2).

    If $k = 1$, then $G$ is order 6, so $G$ is isomorphic to either
    $\ZZ_6$ or $S_3$. The group $S_3$ is not simple, since
    $A_3 \trianglelefteq S_3$, and the only simple cyclic groups are of
    prime order, so $\ZZ_6$ is not simple. This exhausts all of the
    possible cases. 

:::

