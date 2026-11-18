---
schema: qual/card@1
id: P-APAS11B
kind: problem
title: Twisting irreducible characters by linear characters, and conjugate-partition signs
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam labels the first part (d); it is part (a) here.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: that rho* is a representation (the scalar factor is a
    homomorphism), and that the sign-twisting corresponds to omega under the Frobenius
    characteristic with the reason given on the power sums p_mu, which are the characteristics
    of the cycle-type indicators; the conjugation of the partition is then a consequence of
    omega(s_lambda) = s_lambda'. Not claimed: a retained solution set; the provenance names the
    examination paper only. Statement, and the two-sided sign formula in (b), unchanged.
---

::: {.problem}
If $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Prove that if $\lambda(x)$ is a linear character of a finite group $G$, then for any irreducible character $\chi$ of $G$, the function $\chi^*$ defined by $\chi^*(\sigma)=\lambda(\sigma)\chi(\sigma)$ for all $\sigma\in G$ is also an irreducible character of $G$.

(b) Given a partition $\lambda$ of $n$, let $\ell(\lambda)$ denote the number of parts of $\lambda$ and $\lambda'$ denote its conjugate partition.
Let $\chi^\lambda_\mu$ denote the value of the character of the irreducible representation $A^\lambda$ of $S_n$ at the conjugacy class indexed by the partition $\mu$.
Show that
$$
\chi^{\lambda'}_\mu=(-1)^{n-\ell(\mu)}\chi^\lambda_\mu.
$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2011 applied-algebra examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $G$ is a finite group, $\lambda:G\to\CC^\times$ a linear character, and $\chi$ the character of an irreducible representation $\rho:G\to\GL(V)$.

::: pf

::: {.pf-step #part-a-representation}
$\rho^*:\rho^*(g)\coloneqq\lambda(g)\rho(g)$ is a representation of $G$ on $V$, with character $\chi^*(g)=\lambda(g)\chi(g)$.

::: pf-proof
$\lambda(g)$ is a nonzero scalar and $\lambda$ is a homomorphism, so $\rho^*(gh)=\lambda(gh)\rho(gh)=\lambda(g)\lambda(h)\rho(g)\rho(h)=\rho^*(g)\rho^*(h)$, and $\rho^*(1)=I$; the trace of a scalar multiple is the scalar times the trace, so the character is $\chi^*$.

:::

:::

::: {.pf-step #part-a-irreducible}
$\rho^*$ is irreducible, so $\chi^*$ is an irreducible character.

::: pf-proof
A subspace $W\subseteq V$ is $\rho^*$-invariant iff $\rho^*(g)W\subseteq W$ for all $g$ iff $\lambda(g)\rho(g)W\subseteq W$ for all $g$ iff $\rho(g)W\subseteq W$ for all $g$, since $\lambda(g)\ne0$ and $W$ is a subspace: multiplication by a nonzero scalar preserves the subspace and is reversible. So $\rho$ and $\rho^*$ have the same invariant subspaces; $\rho$ being irreducible, so is $\rho^*$. A representation is irreducible iff its character is, so $\chi^*$ is irreducible.

:::

:::

::: {.pf-step #sign-tensor}
$A^{\lambda'}\cong A^{\lambda}\otimes\operatorname{sgn}$ for every partition $\lambda$ of $n$.

::: pf-proof
Under the Frobenius characteristic, which is an isometry taking characters of $S_n$ to symmetric functions of degree $n$ and irreducible characters to Schur functions, tensoring a character by the sign character corresponds to applying the involution $\omega$: for a class function $f$ with characteristic $\operatorname{ch}(f)$, the characteristic of $\sigma\mapsto\operatorname{sgn}(\sigma)f(\sigma)$ is $\omega(\operatorname{ch} f)$, because on power sums $p_\mu$, which are the characteristics of the indicators of cycle types, $\omega(p_\mu)=(-1)^{\sum_i(\mu_i-1)}p_\mu=\operatorname{sgn}(\mu)\,p_\mu$. Since $\omega(s_\lambda)=s_{\lambda'}$, the character of $A^\lambda\otimes\operatorname{sgn}$ has characteristic $s_{\lambda'}$, and characters are determined by their characteristics, so $A^{\lambda'}\cong A^\lambda\otimes\operatorname{sgn}$.

:::

:::

::: {.pf-step #sign-value}
If $\sigma\in S_n$ has cycle type $\mu$ with $\ell(\mu)$ parts, then $\operatorname{sgn}(\sigma)=(-1)^{n-\ell(\mu)}$.

::: pf-proof
A cycle of length $r$ equals $r-1$ transpositions, hence has sign $(-1)^{r-1}$; $\operatorname{sgn}$ is a homomorphism and $\sigma$ is the product of its $\ell(\mu)$ disjoint cycles, so $\operatorname{sgn}(\sigma)=\prod_i(-1)^{\mu_i-1}=(-1)^{\sum_i\mu_i-\ell(\mu)}$, and $\sum_i\mu_i=n$.

:::

:::

::: {.pf-step #part-b}
$\chi^{\lambda'}_{\mu}=(-1)^{n-\ell(\mu)}\chi^{\lambda}_{\mu}$.

::: pf-proof
By step [](#sign-tensor){.pf-ref} the character of $A^{\lambda'}$ is $\operatorname{sgn}\cdot\chi^\lambda$, so for $\sigma$ of cycle type $\mu$, step [](#sign-value){.pf-ref} gives
$$
\chi^{\lambda'}(\sigma)=(-1)^{n-\ell(\mu)}\chi^{\lambda}(\sigma).
$$
Character values are constant on conjugacy classes, and all elements of cycle type $\mu$ form one class, so the identity reads $\chi^{\lambda'}_\mu=(-1)^{n-\ell(\mu)}\chi^{\lambda}_\mu$.

:::

:::

:::
:::
