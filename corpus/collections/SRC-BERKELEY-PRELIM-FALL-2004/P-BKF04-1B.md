---
schema: qual/card@1
id: P-BKF04-1B
kind: problem
title: $A_n\cap S_m=A_m$ for the standard inclusion, but not for every embedding $S_m\hookrightarrow S_n$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument, which the body
    now cites (Fall 2004 solutions, Problem 1B, PDF p. 5, the file named in the collection's
    provenance); the card previously carried no citation. Added: the uniqueness argument for
    the sign homomorphism from generation by transpositions, the injectivity of the product
    embedding, and the case $m=1$ of part (b), where the equality does hold. One printed slip
    in the sheet is noted and corrected in the body: it writes the second factor's support as
    $\{n+1,\dots,2m\}$ where its own $n=2m$ gives $\{m+1,\dots,2m\}$. Mathematics of the card
    unchanged; the printed problem is unchanged.
---

::: {.problem}
Let $S_{n}$ be the group of permutations of $\{1, \ldots, n\}$, and let $A_{n}$ be the alternating subgroup. Suppose $m \leq n$.

(a) Identify $S_{m}$ with the subgroup of $S_{n}$ consisting of elements that fix $m + 1, \ldots, n$. Prove that $A_{n} \cap S_{m} = A_{m}$.

(b) Is it true in general that if $f \colon S_{m} \to S_{n}$ is an injective homomorphism, then $A_{n} \cap f(S_{m}) = f(A_{m})$? Give a proof or a counterexample.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Fall 2004 preliminary examination solutions, Problem 1B** (`assets/attachments/f04solution.pdf`, the file named in this collection's `provenance`), whose argument both parts below are: the restriction of $\operatorname{sgn}_n$ to $S_m$ is $\operatorname{sgn}_m$, and the diagonal embedding of $S_m\times S_m$ into $S_{2m}$ gives the counterexample. The card corrects one printed slip: the sheet says the second factor permutes $\{n+1,\dots,2m\}$, which is $\{m+1,\dots,2m\}$ for its own $n=2m$.

Throughout $S_k$ is the symmetric group on $\theset{1,\dots,k}$ and $A_k$ its alternating subgroup, and $S_m\subset S_n$ means the subgroup of permutations fixing $m+1,\dots,n$.

::: pf

::: {.pf-step #sign}
$\operatorname{sgn}_n$ is a homomorphism whose restriction to $S_m\subset S_n$ equals $\operatorname{sgn}_m$.

::: pf-proof
$\operatorname{sgn}_k$ is defined as the unique homomorphism $S_k\to\theset{\pm1}$ sending each transposition to $-1$; uniqueness holds because transpositions generate $S_k$. A transposition of $S_m$ is a transposition of $S_n$ fixing $m+1,\dots,n$, so the restriction $\restrictionof{\operatorname{sgn}_n}{S_m}$ is a homomorphism $S_m\to\theset{\pm1}$ sending every transposition to $-1$; by uniqueness it is $\operatorname{sgn}_m$.

:::

:::

::: {.pf-step #part-a}
$A_n\cap S_m=A_m$.

::: pf-proof
$A_k=\ker\operatorname{sgn}_k$ by definition, so by step [](#sign){.pf-ref}
$$
A_n\cap S_m=\ker(\operatorname{sgn}_n)\cap S_m=\ker\bigl(\restrictionof{\operatorname{sgn}_n}{S_m}\bigr)=\ker(\operatorname{sgn}_m)=A_m .
$$

:::

:::

::: {.pf-step #counterexample}
For $m\ge2$ there is an injective homomorphism $f:S_m\to S_{2m}$ with $A_{2m}\cap f(S_m)\ne f(A_m)$.

::: pf-proof
Let $S_m\times S_m$ act on $\theset{1,\dots,2m}$ with the first factor permuting $\theset{1,\dots,m}$ and fixing the rest and the second permuting $\theset{m+1,\dots,2m}$ and fixing the rest. This gives a homomorphism $\iota:S_m\times S_m\to S_{2m}$, injective because an element acting trivially on both halves is trivial. Define $f(\sigma)=\iota(\sigma,\sigma)$; it is injective since $\iota$ is. A transposition $\tau\in S_m$ is carried by $f$ to the product of the corresponding transposition of $\theset{1,\dots,m}$ with that of $\theset{m+1,\dots,2m}$: two disjoint transpositions, an even permutation, so $f(\tau)\in A_{2m}$. Transpositions generate $S_m$, so $f(S_m)\subseteq A_{2m}$ and therefore $A_{2m}\cap f(S_m)=f(S_m)$. Since $f$ is injective and $A_m\ne S_m$ for $m\ge2$, $f(A_m)\subsetneq f(S_m)$. So $A_{2m}\cap f(S_m)\ne f(A_m)$: the general statement of (b) fails.

:::

:::

::: {.pf-step #conclusion}
(a) holds, and (b) fails.

::: pf-proof
Step [](#part-a){.pf-ref} is (a); step [](#counterexample){.pf-ref} gives, for every $m\ge2$, an injective $f:S_m\to S_{2m}$ with $A_{2m}\cap f(S_m)\ne f(A_m)$, which answers (b) in the negative. The case $m=1$ is excluded from the counterexample because $A_1=S_1$, and then the equality holds for every injective $f:S_1\to S_n$ since $f(A_1)=f(S_1)$.

:::

:::

:::
:::
