---
schema: qual/card@1
id: P-QM6M4
kind: problem
title: Galois groups of the compositum and intersection of two splitting fields
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - field-extensions
  - subgroups
relations: []
review: draft
solved: true
---

::: problem
Let $K$ be a Galois extension of $\QQ$ with Galois group $G$, and let $E_1 , E_2$ be intermediate fields of $K$ which are the splitting fields of irreducible $f_i (x) \in \QQ[x]$.

Let $E = E_1 E_2 \subset K$.

Let $H_i = \Gal(K/E_i)$ and $H = \Gal(K/E)$.

(a) Show that $H = H_1 \cap H_2$.

(b) Show that $H_1 H_2$ is a subgroup of $G$.

(c) Show that
    $$
    \Gal(K/(E_1 \cap E_2 )) = H_1 H_2
    .$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) $H = H_1 \cap H_2$:**
By the Fundamental Theorem of Galois Theory:
For any $\sigma \in G = \Gal(K/\QQ)$:
$\sigma \in H = \Gal(K/E_1 E_2) \iff \sigma(\alpha) = \alpha$ for all $\alpha \in E_1 E_2$.
Since $E_1 E_2$ is generated over $\QQ$ by $E_1$ and $E_2$, $\sigma$ fixes $E_1 E_2$ pointwise if and only if $\sigma$ fixes $E_1$ pointwise and $\sigma$ fixes $E_2$ pointwise.
Thus $\sigma \in \Gal(K/E_1) = H_1$ and $\sigma \in \Gal(K/E_2) = H_2$, so $\sigma \in H_1 \cap H_2$.
Therefore, $H = H_1 \cap H_2$.

**(b) $H_1 H_2$ is a subgroup of $G$:**
Since each $E_i$ is a splitting field over $\QQ$, each extension $E_i / \QQ$ is normal, hence Galois.
By the Fundamental Theorem of Galois Theory, the corresponding subgroup $H_i = \Gal(K/E_i)$ is a **normal subgroup** of $G = \Gal(K/\QQ)$ for both $i = 1, 2$.
A standard group-theoretic fact states that if $N_1, N_2 \normal G$ are normal subgroups, then the product set $N_1 N_2 = \{n_1 n_2 \mid n_1 \in N_1, n_2 \in N_2\}$ is a subgroup of $G$ (and is also normal in $G$).
Since $H_1, H_2 \normal G$, $H_1 H_2$ is a subgroup of $G$.

**(c) $\Gal(K/(E_1 \cap E_2)) = H_1 H_2$:**
By the Galois correspondence, for any two intermediate fields $E_1, E_2$:
The Galois group $\Gal(K/(E_1 \cap E_2))$ is the smallest subgroup of $G$ containing both $\Gal(K/E_1) = H_1$ and $\Gal(K/E_2) = H_2$, denoted $\langle H_1, H_2 \rangle$.
Since $H_1 \normal G$ and $H_2 \normal G$, the product $H_1 H_2$ is itself a subgroup of $G$.
Therefore, $\langle H_1, H_2 \rangle = H_1 H_2$.
Thus:
$$
\Gal(K/(E_1 \cap E_2)) = H_1 H_2.
$$
:::
