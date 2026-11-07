---
schema: qual/card@1
id: E-HAT-2.2-16
kind: problem
title: Ranks of simplicial chain groups of $\Delta^n$ and homology of skeleta
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 16; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular-chain proof checked.
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The card wrote the vertices of the simplex as the Greek letter, `\nu_0`,
    where Hatcher writes them `v_0`; the vertex symbol is restored throughout.
    Found by comparing the statement with the printed exercise.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the ranks: $\operatorname{rank}C_i=\binom{n+1}{i+1}$ with the induction
    $\binom{n+1}{i+1}-\binom{n}{i}=\binom{n}{i+1}$ simultaneously for cycles and boundaries, and
    $\binom{n}{k+1}$ for the top group of the $k$-skeleton. The degree-zero case of the third step
    as written compared $Z_0/B_0$ with the reduced homology of the simplex; that comparison is only
    valid in the augmented complex, where $\partial_0$ is the augmentation, and the step is
    repaired to say so.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Certificate for the repaired degree-zero step. proofs/cards/ChainLevelSteps.lean proves the two
    ingredients: `choose_rank_step`, Pascal's identity
    $\binom{n+1}{i+1}-\binom{n}{i}=\binom{n}{i+1}$ in the form the rank induction uses, and
    `ker_ne_top_of_surjective_to_int`, that an augmentation onto $\ZZ$ has proper kernel, so the
    augmented degree-zero cycles are not the ordinary $Z_0=C_0$. The passage from the chain complex
    of the simplex to its homology remains Hatcher's computation and is not formalized.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 16 as printed on p. 156, including the skeleton conclusion
    rank C(n,k+1) in degree k. Rechecked the rank induction: rank C_i = C(n+1,i+1) and the
    base case is rank B_{-1} = rank im(epsilon) = 1 in the augmented complex, so
    rank Z_0 = (n+1)-1 = n = C(n,1); the step now says where the augmentation comes from
    (p. 110). Exactness of the reduced complex is now cited as Proposition 2.8 p. 110 with
    Corollary 2.11 p. 111 plus Theorem 2.27 p. 128, and the chain groups as p. 104. The
    skeleton argument is checked: for i < k both partial boundaries are present, and in
    degree k there are no (k+1)-chains so B_k = 0 while Z_k = Z_k(Delta^n).
    What is not covered: no certificate for this card; the rank identities are verified by
    hand only.
---

::: {.problem}
Let $\Delta^n = [v_0, \cdots, v_n]$ have its natural $\Delta$-complex structure with $k$ simplices $[v_{i_0}, \cdots, v_{i_k}]$ for $i_0 < \cdots < i_k$.
Compute the ranks of the simplicial (or cellular) chain groups $\Delta_i(\Delta^n)$ and the subgroups of cycles and boundaries.
[Hint: Pascal's triangle.] Apply this to show that the $k$ skeleton of $\Delta^n$ has homology groups $\tilde{H}_i((\Delta^n)^k)$ equal to 0 for $i < k$, and free of rank $\binom{n}{k+1}$ for $i = k$.
:::

::: {.solution}
For the standard simplex $\Delta^n$, the group of $i$-chains is free on the $(i+1)$-element subsets of its $n+1$ vertices; this is the definition of the simplicial chain group, the free abelian group on the open $i$-simplices of a $\Delta$-complex (p. 104). Hence
$$
\operatorname{rank} C_i(\Delta^n)=\binom{n+1}{i+1}.
$$

::: pf

::: {.pf-step #s1}

In the reduced simplicial chain complex of $\Delta^n$,
$$
\operatorname{rank} Z_i
=
\operatorname{rank} B_i
=
\binom{n}{i+1}
\qquad (0\le i\le n).
$$
Here $\binom{n}{n+1}=0$.

::: pf-proof

The simplex is contractible, so its reduced singular homology vanishes: $H_n(\Delta^n)=0$ for $n>0$ and $\widetilde H_0(\Delta^n)=0$, by Proposition 2.8 (p. 110) for the one-point space together with Corollary 2.11 (p. 111), homotopy invariance. The simplicial chain complex computes the singular homology by Theorem 2.27 (p. 128), so the reduced simplicial chain complex is exact. Thus
$$
Z_i=B_i
$$
for all $i\ge0$. Since
$$
0\to Z_i\to C_i\xrightarrow{\partial_i}B_{i-1}\to0
$$
is exact, ranks satisfy
$$
\operatorname{rank} Z_i
=
\binom{n+1}{i+1}-\operatorname{rank} B_{i-1}.
$$
Starting with
$$
\operatorname{rank}B_{-1}=1
$$
in the augmented complex, where $\partial_0=\varepsilon:C_0\to\ZZ$ is the augmentation of p. 110 and $B_{-1}=\operatorname{im}\varepsilon=\ZZ$, and using Pascal's identity gives inductively
$$
\operatorname{rank}Z_i
=
\binom{n+1}{i+1}-\binom{n}{i}
=
\binom{n}{i+1}.
$$
Exactness gives the same formula for $B_i$.

:::

:::

::: pf-step

In the ordinary chain complex,
$$
\operatorname{rank}Z_0=n+1,
\qquad
\operatorname{rank}B_0=n,
$$
and for $i\ge1$ the formulas of step [](#s1){.pf-ref} remain valid.

::: pf-proof

Ordinarily $\partial_0=0$, so $Z_0=C_0$ has rank $n+1$. The augmentation kernel has rank $n$, and because $\Delta^n$ is connected this kernel is $B_0$. For $i\ge1$, reduced and ordinary chains agree.

Now let
$$
K=(\Delta^n)^k
$$
be the $k$-skeleton.

:::

:::

::: pf-step

For $i<k$,
$$
\widetilde H_i(K)=0.
$$

::: pf-proof

Work in the augmented chain complexes, in which $\partial_0$ is the augmentation $C_0\to\ZZ$; there $Z_0$ is the kernel of the augmentation rather than $C_0$. In degrees at most $k$ the chain groups and boundary maps of $K$ agree with those of the full simplex. If $i<k$, then $\partial_{i+1}$ is present in both, so
$$
Z_i(K)=Z_i(\Delta^n),
\qquad
B_i(K)=B_i(\Delta^n).
$$
The augmented complex of $\Delta^n$ is exact, so its cycles and boundaries agree in every degree, and the quotient $Z_i(K)/B_i(K)$ is zero.

:::

:::

::: pf-step

In degree $k$,
$$
\widetilde H_k(K)\cong\ZZ^{\binom{n}{k+1}}.
$$

::: pf-proof

There are no $(k+1)$-chains in the $k$-skeleton, so
$$
B_k(K)=0.
$$
On the other hand the boundary map out of $C_k$ is unchanged, hence
$$
Z_k(K)=Z_k(\Delta^n).
$$
By step [](#s1){.pf-ref} this is free of rank
$$
\binom{n}{k+1}.
$$
Therefore
$$
\boxed{
\widetilde H_i((\Delta^n)^k)=
\begin{cases}
0,&i<k,\\
\ZZ^{\binom{n}{k+1}},&i=k.
\end{cases}}
$$

:::

:::

:::

:::
