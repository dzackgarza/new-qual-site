---
schema: qual/card@1
id: P-PSCIU
kind: problem
title: "Let $G$ be a finite group and $H<G$ a subgroup. Let"
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - centralizers-and-normalizers
  - cosets-and-lagrange
relations: []
review: draft
solved: true
---
:::{.problem}
Let $G$ be a finite group and $H<G$ a subgroup. Let
$n_H$ be the number of subgroups of $G$ that are conjugate to $H$. Show
that $n_H$ divides the order of $G$.
:::

:::{.solution}
.* Let $$C_H = \{ gHg^{-1} \mid g\in G \}$$ be the conjugacy class
of $H$, so $|C_H| = n_H$.

We wish to show that $n_{H}$ divides $|G|$.

**Claim 1**: $$n_{H} = [G: N_G(H)],$$ where $N_G(H) \leq G$ is the
normalizer of $H$ in $G$.

Note that if this claim is true, then we can apply Lagrange's theorem,
which states $$A \leq G \implies |G| = [A: G]~|A|,$$

which in this case translates to
$$|G| = [N_G(H) : G]~|N_G(H)| = n_H~|N_G(H)|.$$

Since $n_H$ divides the right-hand side, it must divide the left-hand
side as well, which is precisely what we would like to show.

**Proof of Claim 1**:

The normalizer of $H$ in $G$, written $N_G(H)$, is the largest subgroup
of $G$ containing $H$ such that $H \trianglelefteq N_G(H)$, i.e.
$$N_G(H) = \{g \in G ~\mid~ gHg^{-1} = H \} \leq G.$$

Now consider $S$, the set of left cosets of $N_G(H)$. Suppose there are
$k$ of them, so $$[G: N_G(H)] = |S| \coloneqq k.$$

Then $S$ can be written as
$$S = \{ g_1 N_G(H), ~g_2 N_G(H), ~\cdots, ~g_k N_G(H) \}.$$

where each $g_i$ is a distinct element of $G$ yielding a distinct coset
$g_i N_G(H)$. In particular, if $i\neq j$, then $g_i \neq g_j$, and
$g_i N_G(H) \not \in g_j N_G(H)$.

In particular, $S$ acts on $C_H$, $$\begin{aligned}
S &\curvearrowright C_H \\
g_i N_G(H) &\curvearrowright H = g_i H g_i^{-1},\end{aligned}$$

taking $H$ to one of its conjugate subgroups.

So define $$K \coloneqq 
\{ g_i H g_i^{-1} \mid 1 \leq i \leq k \}.$$

Note that $K \subseteq C_H$, and has at most $k$ elements.

We claim that $K$ has $k$ *distinct* elements, i.e. that each $g_{i}$
takes $H$ to a *distinct* conjugate subgroup. We have $$\begin{aligned}
g_{i} H g^{-1}_{i} 
    &= g_{j} H g^{-1}_{j} &\implies \\
g_j^{-1} g_{i} H g^{-1}_{i} g_j 
    &= H &\implies \\
(g_j^{-1} g_{i}) H (g_j^{-1} g_{i})^{-1} 
    &= H &\implies \\
g_j^{-1} g_{i} &\in N_G(H) &\implies \\
g_i &\in g_j N_G(H) &\implies \\
g_i &= g_j,\end{aligned}$$

where the last line follows because we assumed that each coset contains
at most one $g_i$.

Thus $K$ has $k$ distinct elements, and so
$$= k = |K| \leq |C_H| = n_H.$$

We now claim that $k \geq n_H$ as well.

Let $H' \in C_H$ be any subgroup conjugate to $H$, so $H' = gHg^{-1}$
for some $g\in G$. Then $g = g_i$ for some $i$, so $g \in g_{i} N_G(H)$.

Thus $g = g_{i} n$ for some $n\in N_G(H)$, but
$n\in N_G(H) \iff nHn^{-1} = H$ by definition, and so we have
$$\begin{aligned}
    H' 
    &= gHg^{-1} \\
    &= (g_i n) H (g_i n)^{-1} \\
    &= g_i (n H n^{-1}) g_i^{-1} \\
    &= g_i H g_i^{-1} \in K.\end{aligned}$$

Since $H' \in C_H$ was an arbitrary subgroup conjugate to $H$, this says
that $C_H \subseteq K$ and thus $$n_H = |C_H| \leq |K| = k$$

Thus $$[G: N_G(H)] = k = |M| = |K| = n_H,$$ which is what we wanted to
show. ◻
:::

