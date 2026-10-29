---
schema: qual/card@1
id: P-VJURQ
kind: problem
title: A polynomial over $\QQ$ with Galois group $S_n$, in particular $S_7$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Construct, for every $n\ge2$, a polynomial over $\QQ$ whose Galois group is $S_n$. Give an explicit example for $n=7$.
:::

::: {.solution}
For a monic $f\in\ZZ[x]$ of degree $n$ with distinct roots, regard $G_f=\Gal(f/\QQ)$ as a subgroup of $S_n$ through its action on the roots.
Dedekind's theorem states: if $p$ is a prime such that $f\bmod p$ is squarefree, and $f\bmod p$ factors into irreducibles of degrees $d_1,\ldots,d_k$, then $G_f$ contains a permutation of cycle type $(d_1,\ldots,d_k)$.

::: pf

::: {.pf-step #criterion}
Let $H\le S_n$ be transitive and contain an $(n-1)$-cycle and a transposition. Then $H=S_n$.

::: pf-proof
The $(n-1)$-cycle fixes one point $i$ and permutes the other $n-1$ points transitively, so the stabilizer of $i$ is transitive on the complement of $i$.
With transitivity of $H$, this makes $H$ doubly transitive.
Let $(a\ b)\in H$, and let $(c\ d)$ be any transposition.
Choose $h\in H$ with $h(a)=c$ and $h(b)=d$; then $h(a\ b)h^{-1}=(c\ d)\in H$.
So $H$ contains every transposition, and $H=S_n$.
:::

:::

::: {.pf-step #cycle-types}
Let $f$ be monic of degree $n$ in $\ZZ[x]$. If $f\bmod 2$ is irreducible, $f\bmod 3$ is a product of a linear factor and an irreducible factor of degree $n-1$, and $f\bmod 5$ is a squarefree product of an irreducible quadratic and irreducible factors of odd degrees, then $G_f=S_n$.

::: pf-proof
The reductions mod $2$, $3$ and $5$ are squarefree, so Dedekind's theorem applies to each.
Since $f\bmod 2$ is irreducible, $f$ is irreducible over $\QQ$, so $G_f$ is transitive.
The factorization mod $3$ gives an $(n-1)$-cycle in $G_f$.
The factorization mod $5$ gives $\sigma\in G_f$ of cycle type $(2,d_1,\ldots,d_k)$ with every $d_j$ odd; for $L=\operatorname{lcm}(d_1,\ldots,d_k)$, which is odd, $\sigma^L$ is a transposition.
Step [](#criterion){.pf-ref} gives $G_f=S_n$.
:::

:::

::: pf-step
For every $n\ge2$ there is a monic $f\in\ZZ[x]$ of degree $n$ with $G_f=S_n$.

::: pf-proof
For each prime $p$ and each $d\ge1$ there are monic irreducible polynomials of degree $d$ over $\FF_p$, because $\FF_{p^d}=\FF_p(\alpha)$ for some $\alpha$ and the minimal polynomial of $\alpha$ has degree $d$.
Choose monic $f_1,f_2,f_3\in\ZZ[x]$ of degree $n$ whose reductions are as follows.

- $f_1\bmod 2$ is irreducible of degree $n$.
- $f_2\bmod 3$ is $x$ times an irreducible polynomial of degree $n-1$; for $n=2$, take $x(x-1)$.
- $f_3\bmod 5$ is an irreducible quadratic $q$ for $n=2$; $q\cdot g$ with $g$ irreducible of degree $n-2$ when $n-2$ is odd; $q\cdot x\cdot g$ with $g$ irreducible of degree $n-3\ge3$ when $n-2\ge4$ is even; and $q\cdot x(x-1)$ for $n=4$.

Each of these reductions is squarefree, because its irreducible factors are pairwise distinct.
Put $f=-15f_1+10f_2+6f_3$.
It is monic because $-15+10+6=1$, and $f\equiv f_1\pmod 2$, $f\equiv f_2\pmod 3$, $f\equiv f_3\pmod 5$.
Step [](#cycle-types){.pf-ref} gives $G_f=S_n$.
:::

:::

::: pf-step
$\Gal(x^7-x-1/\QQ)\cong S_7$.

::: pf-proof
Let $f=x^7-x-1$.
Over $\FF_2$, $f=x^7+x+1$ has no root, and it has no irreducible factor of degree $2$ or $3$, so it is irreducible; a computation of the factorizations gives
$$
f\equiv(x^2+x+2)(x^5+2x^4+2x^3+2x+1)\pmod 3,
$$
$$
f\equiv(x+3)(x^6+2x^5+4x^4+3x^3+x^2+2x+3)\pmod 5,
$$
with each displayed factor irreducible.
These are squarefree, so $G_f$ is transitive, contains a permutation of type $(2,5)$, whose fifth power is a transposition, and contains a $6$-cycle.
Step [](#criterion){.pf-ref} gives $G_f=S_7$.
:::

:::

:::
:::
