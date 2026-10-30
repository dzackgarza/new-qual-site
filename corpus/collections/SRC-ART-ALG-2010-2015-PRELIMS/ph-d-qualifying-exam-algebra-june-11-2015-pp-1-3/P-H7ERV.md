---
schema: qual/card@1
id: P-H7ERV
kind: problem
title: At most two $F$-conjugates of $L$ when $[K:F]=2$ and $L/K$ is finite Galois
classification:
  areas:
  - prelim
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Let $F$ be a field of characteristic zero and $\overline{F}$ be an algebraic closure of $F$.
Suppose that $K$ and $L$ are fields, with $F \subseteq K \subseteq L \subseteq \overline{F}$, such that $[K : F] = 2$ and $L/K$ is a finite Galois extension.
Prove that there are at most two fields $M \subseteq \overline{F}$ conjugate to $L$ over $F$ (remember that $M \subseteq \overline{F}$ is conjugate to $L$ over $F$ just in case there is an isomorphism of $L$ onto $M$ which is the identity on $F$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The quadratic extension $K/F$ is Galois, and
$\cardinality{\Aut_F(K)}=2$.

::: pf-proof

Because $\operatorname{char}F=0$, every algebraic extension of $F$ is
separable. A separable extension of degree $2$ is normal: if
$K=F(\alpha)$ and the minimal polynomial of $\alpha$ has roots
$\alpha$ and $\alpha'$, then
$\alpha'=-b-\alpha\in K$ for a quadratic
$X^2+bX+c\in F[X]$. Hence $K/F$ is Galois. Therefore
$$
\cardinality{\Aut_F(K)}=[K:F]=2.
$$

:::

:::

::: {.pf-step #s2}

Every field $M\subseteq\overline F$ conjugate to $L$ over $F$ has
the form $M=\sigma(L)$ for some
$\sigma\in\Aut_F(\overline F)$.

::: pf-proof

An $F$-isomorphism $L\to M$ is an embedding of the finite separable
extension $L/F$ into the algebraic closure $\overline F$. By the extension
theorem for embeddings of algebraic extensions, it extends to an
$F$-automorphism $\sigma$ of $\overline F$. Its image of $L$ is exactly
$M$.

:::

:::

::: {.pf-step #s3}

For every $\sigma\in\Aut_F(\overline F)$, one has
$\sigma(K)=K$.

::: pf-proof

By step [](#s1){.pf-ref}, $K/F$ is normal. Hence every $F$-embedding of $K$ into
$\overline F$ has image $K$. Restricting $\sigma$ to $K$ gives such an
embedding.

:::

:::

::: {.pf-step #s4}

If $\sigma,\tau\in\Aut_F(\overline F)$ have
$\sigma\restrict_K=\tau\restrict_K$, then
$$
\sigma(L)=\tau(L).
$$

::: pf-proof

By step [](#s3){.pf-ref}, both $\sigma$ and $\tau$ stabilize $K$. Therefore
$\sigma^{-1}\tau$ fixes $K$ pointwise. Since $L/K$ is Galois, hence
normal, every $K$-automorphism of $\overline F$ stabilizes $L$. Thus
$$
(\sigma^{-1}\tau)(L)=L.
$$
Applying $\sigma$ gives $\tau(L)=\sigma(L)$.

:::

:::

::: {.pf-step #s5}

There are at most two fields conjugate to $L$ over $F$.

::: pf-proof

By step [](#s2){.pf-ref}, every such field is $\sigma(L)$ for some
$\sigma\in\Aut_F(\overline F)$. By step [](#s4){.pf-ref}, this image depends only
on the restriction $\sigma\restrict_K$. Step [](#s1){.pf-ref} gives only two possible
restrictions, namely the two elements of $\Aut_F(K)$. Hence at most two
distinct images $\sigma(L)$ can occur.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required bound.

:::

:::

:::
