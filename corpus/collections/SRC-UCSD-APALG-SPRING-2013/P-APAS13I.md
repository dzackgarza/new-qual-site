---
schema: qual/card@1
id: P-APAS13I
kind: problem
title: External tensor product of representations of a direct product of groups
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $G$ and $H$ be finite groups and let $A\colon G\to\mathrm{GL}_n(\CC)$ and $B\colon H\to\mathrm{GL}_m(\CC)$ be representations of $G$ and $H$ respectively.

(a) Show that $A\times B\colon G\times H\to\mathrm{GL}_{nm}(\CC)$ is a representation where for $(\sigma,\tau)\in G\times H$,
$$
A\times B((\sigma,\tau))=A(\sigma)\otimes B(\tau)
$$
and for matrices $M$ and $N$, $M\otimes N$ is the Kronecker product of $M$ and $N$.

(b) Show that $A\times B$ is an irreducible representation of $G\times H$ if and only if $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.

(c) Show that every irreducible representation of $G\times H$ is of the form $A\times B$ where $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.

(d) Show that it is not always the case that if $C$ is a representation of $G\times H$, then $C$ is similar to a representation of the form $A\times B\colon G\times H\to\mathrm{GL}_n(\CC)$ where $A$ is a representation of $G$ and $B$ is a representation of $H$.
(Hint: Consider the two-dimensional representations of $S_2\times S_2$.)
:::

::: {.solution}

The argument is the card's own, by characters; part (d) is decided by the character test rather than by the scalar-action test of the earlier version of this card, which asserted of a one-dimensional first factor that the first group acts by scalar matrices, and that is false unless the other factor's matrices are themselves scalar.

Let $A:G\to\mathrm{GL}_{n}(\CC)$ and $B:H\to\mathrm{GL}_{m}(\CC)$ be representations of finite groups, and let $\chi_{A}$, $\chi_{B}$ be their characters.

::: pf

::: {.pf-step #representation}
(a) $A\times B(\sigma,\tau)=A(\sigma)\otimes B(\tau)$ is a representation of $G\times H$.

::: pf-proof
The Kronecker product satisfies $(M_{1}\otimes N_{1})(M_{2}\otimes N_{2})=(M_{1}M_{2})\otimes(N_{1}N_{2})$ for matrices of matching sizes, and $I\otimes I=I$. Hence for $(\sigma_{1},\tau_{1}),(\sigma_{2},\tau_{2})\in G\times H$,
$$
(A\times B)\big((\sigma_{1},\tau_{1})(\sigma_{2},\tau_{2})\big)=A(\sigma_{1}\sigma_{2})\otimes B(\tau_{1}\tau_{2})=\big(A(\sigma_{1})\otimes B(\tau_{1})\big)\big(A(\sigma_{2})\otimes B(\tau_{2})\big),
$$
and $(A\times B)(e,e)=I_{n}\otimes I_{m}=I_{nm}$; each $A(\sigma)\otimes B(\tau)$ is invertible with inverse $A(\sigma)^{-1}\otimes B(\tau)^{-1}$. So $A\times B$ is a homomorphism $G\times H\to\mathrm{GL}_{nm}(\CC)$.
:::

:::

::: {.pf-step #character}
(b) $\chi_{A\times B}(\sigma,\tau)=\chi_{A}(\sigma)\chi_{B}(\tau)$, and $\langle\chi_{A\times B},\chi_{A\times B}\rangle_{G\times H}=\langle\chi_{A},\chi_{A}\rangle_{G}\langle\chi_{B},\chi_{B}\rangle_{H}$.

::: pf-proof
$\operatorname{tr}(M\otimes N)=\operatorname{tr}(M)\operatorname{tr}(N)$, since the Kronecker product has the products $M_{ij}N_{kl}$ on its diagonal entries, so the character of $A\times B$ is the product of the characters. Then
$$
\langle\chi_{A\times B},\chi_{A\times B}\rangle_{G\times H}=\frac{1}{\cardinality{G}\cardinality{H}}\sum_{\sigma\in G}\sum_{\tau\in H}\abs{\chi_{A}(\sigma)}^{2}\abs{\chi_{B}(\tau)}^{2}=\langle\chi_{A},\chi_{A}\rangle_{G}\,\langle\chi_{B},\chi_{B}\rangle_{H}.
$$
:::

:::

::: {.pf-step #b}
(b) $A\times B$ is irreducible if and only if $A$ and $B$ are irreducible.

::: pf-proof
A complex representation of a finite group is irreducible exactly when the norm of its character is $1$. Each of $\langle\chi_{A},\chi_{A}\rangle_{G}$ and $\langle\chi_{B},\chi_{B}\rangle_{H}$ is a nonnegative integer, being the sum of the squares of the multiplicities in the decomposition of the character into irreducibles; so by step [](#character){.pf-ref} the product is $1$ exactly when both factors are $1$. Hence $A\times B$ is irreducible exactly when $A$ and $B$ are.
:::

:::

::: {.pf-step #c-exhaust}
(c) If $A_{1},\ldots,A_{r}$ and $B_{1},\ldots,B_{s}$ are complete sets of inequivalent irreducibles of $G$ and of $H$, then the $A_{i}\times B_{j}$ are a complete set of inequivalent irreducibles of $G\times H$.

::: pf-proof
Each $A_{i}\times B_{j}$ is irreducible by step [](#b){.pf-ref}. They are pairwise inequivalent because
$$
\langle\chi_{A_{i}\times B_{j}},\chi_{A_{i'}\times B_{j'}}\rangle=\langle\chi_{A_{i}},\chi_{A_{i'}}\rangle_{G}\langle\chi_{B_{j}},\chi_{B_{j'}}\rangle_{H}
$$
by the same computation as step [](#character){.pf-ref}, and this is $1$ when $(i,j)=(i',j')$ and $0$ otherwise, by the orthonormality of each complete set; distinct irreducibles have orthogonal characters. Finally, with $d_{i}=\dim A_{i}$ and $e_{j}=\dim B_{j}$,
$$
\sum_{i,j}(d_{i}e_{j})^{2}=\Big(\sum_{i}d_{i}^{2}\Big)\Big(\sum_{j}e_{j}^{2}\Big)=\cardinality{G}\cardinality{H}=\cardinality{G\times H},
$$
using that the sum of the squares of the dimensions of the inequivalent irreducibles of a finite group is its order. Since the inequivalent irreducibles of $G\times H$ are pairwise inequivalent and the sums of the squares of their dimensions add to $\cardinality{G\times H}$, the $rs$ representations $A_{i}\times B_{j}$ already exhaust them, so every irreducible of $G\times H$ is of that form.
:::

:::

::: {.pf-step #d-example}
(d) Identify $S_{2}$ with $C_{2}=\{0,1\}$ and let $C(s,t)=\mathrm{diag}\big((-1)^{s},(-1)^{t}\big)$.

::: pf-proof
$C(s,t)$ is a diagonal matrix with entries of modulus $1$, and $C(s,t)C(s',t')=\mathrm{diag}\big((-1)^{s+s'},(-1)^{t+t'}\big)=C(s+s',t+t')$, so $C$ is a two-dimensional representation of $C_{2}\times C_{2}$. Its character is $\chi_{C}(s,t)=(-1)^{s}+(-1)^{t}$, and $C$ is the direct sum of the two distinct linear characters $(s,t)\mapsto(-1)^{s}$ and $(s,t)\mapsto(-1)^{t}$.
:::

:::

::: {.pf-step #d-character}
(d) No external tensor product of dimension $2$ has the character $\chi_{C}$, so $C$ is not similar to any $A\times B$.

::: pf-proof
Let $A:G\to\mathrm{GL}_{n}$ and $B:H\to\mathrm{GL}_{m}$ with $G=H=C_{2}$ satisfy $nm=2$; then $\{n,m\}=\{1,2\}$. If $n=1$ then $A$ is a linear character $\alpha$ and, by step [](#character){.pf-ref},
$$
\chi_{A\times B}(s,t)=\alpha(s)\chi_{B}(t),
$$
so $\chi_{A\times B}(1,0)=\alpha(1)\chi_{B}(0)=\pm2$ because $\alpha(1)=\pm1$ and $\chi_{B}(0)=\dim B=2$. But $\chi_{C}(1,0)=(-1)^{1}+(-1)^{0}=0$. If $m=1$ the same computation with the roles exchanged gives $\chi_{A\times B}(0,1)=\pm2$ while $\chi_{C}(0,1)=0$. So no such $A\times B$ has the character of $C$; similar representations have equal characters, so $C$ is not similar to any $A\times B$.
:::

:::

::: {.pf-step #d-conclusion}
(d) Not every representation of $G\times H$ is similar to an external tensor product.

::: pf-proof
The representation $C$ of step [](#d-example){.pf-ref} is a two-dimensional representation of $C_{2}\times C_{2}$ that is not similar to any $A\times B$ by step [](#d-character){.pf-ref}. So the conclusion of (c) fails for reducible representations: every irreducible representation of $G\times H$ is an external tensor product, but a direct sum of two of them need not be one.
:::

:::

:::
:::
