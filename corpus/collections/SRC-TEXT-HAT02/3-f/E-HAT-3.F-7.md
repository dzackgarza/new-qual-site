---
schema: qual/card@1
id: E-HAT-3.F-7
kind: problem
title: "Moore spaces as quotients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 7, printed page
    320; the statement matches word for word. Checked: choosing bases F_A ⊆ F_B with
    K_B ∩ F_A = K_A makes K_B/K_A free (Example 2.40, p. 125), so M(B,n)/M(A,n) has
    the homology of M(C,n); the long exact cohomology sequence of the pair, together
    with the universal coefficient theorem (Theorem 3.2, p. 195) applied to A, B, C,
    gives the six-term exact sequence displayed. No defect.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the construction already on the card: the free
    presentation with $K_B\cap F_A=K_A$, the cell structure of Example 2.40, the relative
    cellular chain complex of the quotient and the injectivity of its boundary, then the
    universal coefficient computation and the long exact sequence of the pair. Added: the
    verification that the subcomplex on $S_A\cup T_A$ is a Moore space for $A$, the argument
    that $T_A\sqcup T'$ is a basis using the freeness of $K_B/K_A$, and the two vanishing
    terms that give the zeros at each end of the displayed sequence. Cited: Example 2.40 on
    printed p. 143, Proposition 2.22 on printed p. 123, the exercise on printed p. 320. Not
    claimed: a retained solution set — the sets in `tmp/sources` cover §3.1–§3.3 and §4.1–§4.3
    — so the argument is the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read step by step against Hatcher, Algebraic Topology (2002), §3.F Exercise 7, Example 2.40,
    Proposition 2.22 and Theorem 3.2. The construction is correct: extending a generating set of A to
    one of B by lifts of generators of C makes the square commute; K_B meets F_A in K_A exactly; a
    lift of a basis of the free group K_B/K_A together with a basis of K_A is a basis of K_B; the
    cellular boundary of the Moore space is the inclusion K_B -> F_B, giving H_n = B; and in the
    quotient the boundary d_{n+1} on the T'-cells is injective because a combination of T' lying in
    F_A lies in K_A and meets it trivially, so H_n(Q) = F_B/(K_B+F_A) = B/A = C and every other
    reduced homology vanishes. Three page locators removed from the body: Example 2.40, Proposition
    2.22 and the exercise are cited by number, in the opening paragraph, in step `free-presentation`
    and in the cohomology step. No mathematics changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read again against Hatcher, §3.F Exercise 7. The construction is correct: a generating set of $A$
    extended by lifts of generators of $C$ gives $F_A\subset F_B$ with $F_B/F_A$ free and
    $K_B\cap F_A=K_A$, so $K_B/K_A$ is free; the Moore complexes built on $T_A\sqcup T'$ have
    boundary $K_B\hookrightarrow F_B$, the quotient by the subcomplex $M(A,n)$ has boundary the
    $S'$-coordinates, which is injective, and its $n$-th homology is
    $F_B/(K_B+F_A)\cong C$. One repair, in step `sequence`: it began the displayed sequence with a
    zero on the strength of $H^{n-1}(\text{pair})=0$, which does not make the map out of
    $H^n(\text{pair})$ injective — the term mapping into it is $H^{n-1}(M(A,n))$, which is
    $\widetilde H^{n-1}(M(A,n))=0$ only for $n\ge2$ and is $\ZZ$ for $n=1$. The step now separates
    the cases: for $n=1$ the map $H^0(M(B,1))\to H^0(M(A,1))$ is an isomorphism of copies of $\ZZ$
    because both spaces are connected, so the connecting map is zero. The provenance sentence is
    corrected to say what the retained sets hold.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Correction to the preceding event's repair. The coefficients were dropped there: the long exact
    sequence of the pair is taken with coefficients $G$, so the exceptional term at $n=1$ is
    $H^{0}(M(A,1);G)=G$, and $H^{0}(M(B,1);G)\to H^{0}(M(A,1);G)$ is the identity map of $G$, not of
    $\ZZ$. Step `sequence` now writes the coefficients in every term of that sentence. The
    mathematics of the repair is unchanged; this fixes its statement.
---

::: {.problem}
Show that for a short exact sequence of abelian groups $0 \to A \to B \to C \to 0$, a Moore space $M(C, n)$ can be realized as a quotient $M(B, n)/M(A, n)$.
Applying the long exact sequence of cohomology for the pair $(M(B,n), M(A,n))$ with any coefficient group $G$, deduce an exact sequence

$$0 \to \operatorname{Hom}(C,G) \to \operatorname{Hom}(B,G) \to \operatorname{Hom}(A,G) \to \operatorname{Ext}(C,G) \to \operatorname{Ext}(B,G) \to \operatorname{Ext}(A,G) \to 0.$$
:::

::: {.solution}
The statement is Hatcher, §3.F Exercise 7. No retained solution set holds a solution of any exercise of §3.F — Koukpari's set carries the §3.F heading *Limits and Ext* with nothing under it, Sam's begins at §4.1, and the others stop earlier — so the construction and the exact sequence below are the card's own. The construction of Moore spaces used is Example 2.40.

Throughout $0\to A\xrightarrow{i}B\xrightarrow{q}C\to0$ is a short exact sequence of abelian groups, $n\ge1$, and $G$ is any coefficient group.

::: pf

::: {.pf-step #free-presentation}
There are free abelian groups $F_A\subset F_B$ with $F_B/F_A$ free and surjections $F_A\twoheadrightarrow A$, $F_B\twoheadrightarrow B$ compatible with $i$, and kernels $K_A\subset K_B$ with $K_B\cap F_A=K_A$.

::: pf-proof
Choose a generating set $S_A$ of $A$ and extend it to a generating set $S_B=S_A\sqcup S'$ of $B$ by adjoining lifts of the elements of a generating set of $C$: choosing $s'\in B$ with $q(s')$ a chosen generator of $C$ and using that $q$ is onto makes every element of $B$ a combination of $S_A$ and the chosen lifts, since $q$ of a combination of the lifts differs from a given element by an element of $\ker q=\operatorname{im}i$. Let $F_A=\ZZ^{(S_A)}\subset F_B=\ZZ^{(S_B)}$ and let $F_A\to A$, $F_B\to B$ send each basis element to the corresponding element; these are surjective by construction, and the square with $i$ and the inclusion commutes because both composites send $s\in S_A$ to $i(s)\in B$. Put $K_A=\ker(F_A\to A)$ and $K_B=\ker(F_B\to B)$. If $x\in K_B\cap F_A$ then $x$ maps to $0$ in $B$ and lies in $F_A$, hence maps to $0$ in the composite $F_A\to A\xrightarrow{i}B$, so $x\in K_A$; the converse inclusion is clear. Since $F_B/F_A\cong\ZZ^{(S')}$ is free, so is the subgroup $K_B/K_A\cong(K_B+F_A)/F_A\subseteq F_B/F_A$, by the subgroup theorem for free abelian groups (Example 2.40).

:::

:::

::: {.pf-step #moore-space}
With bases $T_A$ of $K_A$ and $T'$ of a free complement, $T=T_A\sqcup T'$ is a basis of $K_B$, and the CW complex $M(B,n)$ of Example 2.40 built from these data has $\widetilde H_n\cong B$ and all other reduced homology zero, with the subcomplex on $S_A$ and $T_A$ a Moore space $M(A,n)$.

::: pf-proof
Lifting a basis of the free group $K_B/K_A$ to elements of $K_B$ gives, together with $T_A$, a basis of $K_B$: the images of the lifts form a basis of the quotient and $K_A$ is the kernel, so every element of $K_B$ is a unique combination. Let $M(B,n)$ be the wedge of $n$-spheres $S^n_s$, $s\in S_B$, together with one $(n+1)$-cell $e^{n+1}_t$ for each $t\in T$, attached so that the composite with the projection to $S^n_s$ has degree the coefficient $d_{t,s}$ of $s$ in $t$. The cellular boundary $d_{n+1}$ is then the inclusion $K_B\hookrightarrow F_B$, so $H_n=F_B/K_B\cong B$ and $H_{n+1}=0$, and no other reduced homology occurs because there are no other cells. Restricting to the cells indexed by $S_A$ and $T_A$ gives a subcomplex, and the same computation identifies its $n$-th homology with $F_A/K_A\cong A$ and its other reduced homology with $0$.

:::

:::

::: {.pf-step #quotient}
The quotient $Q=M(B,n)/M(A,n)$ has the homology of a Moore space $M(C,n)$.

::: pf-proof
$Q$ is a CW complex whose cells are the basepoint, the $n$-cells indexed by $S'$ and the $(n+1)$-cells indexed by $T'$. In the cellular chain complex of $Q$ the boundary $d_{n+1}:\ZZ^{(T')}\to\ZZ^{(S')}$ records only the $S'$-coordinates, the $S_A$-coordinates having been collapsed to the basepoint. That map is injective: a combination of elements of $T'$ lying in $F_A$ lies in $K_B\cap F_A=K_A$, and the subgroup generated by $T'$ meets $K_A$ trivially because $T_A\sqcup T'$ is a basis of $K_B$. Hence $\widetilde H_{n+1}(Q)=0$ and
$$
\widetilde H_n(Q)\cong\ZZ^{(S')}/\operatorname{im}d_{n+1}\cong F_B/(K_B+F_A)\cong (F_B/K_B)\big/\bigl((K_B+F_A)/K_B\bigr)\cong B/A\cong C,
$$
using $(K_B+F_A)/K_B\cong F_A/(K_B\cap F_A)=F_A/K_A\cong A$. All other reduced homology of $Q$ vanishes, so $Q$ is a Moore space $M(C,n)$.

:::

:::

::: {.pf-step #cohomology-of-moore}
For any abelian group $D$: $\widetilde H^n(M(D,n);G)\cong\operatorname{Hom}(D,G)$, $\widetilde H^{n+1}(M(D,n);G)\cong\operatorname{Ext}(D,G)$, and all other reduced cohomology groups vanish.

::: pf-proof
$M(D,n)$ has $H_n=D$, $H_{n+1}=0$ and no other homology, so the universal coefficient theorem gives $H^n\cong\operatorname{Hom}(H_n,G)\oplus\operatorname{Ext}(H_{n-1},G)=\operatorname{Hom}(D,G)$ and $H^{n+1}\cong\operatorname{Hom}(H_{n+1},G)\oplus\operatorname{Ext}(H_n,G)=\operatorname{Ext}(D,G)$, with every other group vanishing for the same reason.

:::

:::

::: {.pf-step #pair}
$H^k(M(B,n),M(A,n);G)\cong\widetilde H^k(M(C,n);G)$ for every $k$.

::: pf-proof
$(M(B,n),M(A,n))$ is a CW pair, so the quotient map induces isomorphisms $H^k(M(B,n),M(A,n))\cong\widetilde H^k(Q)$ (Proposition 2.22), and $Q$ is the Moore space $M(C,n)$ by step [](#quotient){.pf-ref}.

:::

:::

::: {.pf-step #sequence}
The long exact sequence of the pair with coefficients $G$ becomes
$$
0\to\operatorname{Hom}(C,G)\to\operatorname{Hom}(B,G)\to\operatorname{Hom}(A,G)\to\operatorname{Ext}(C,G)\to\operatorname{Ext}(B,G)\to\operatorname{Ext}(A,G)\to0 .
$$

::: pf-proof
The long exact sequence of the pair $(M(B,n),M(A,n))$ reads
$$
\cdots\to H^k(\text{pair})\to H^k(M(B,n))\to H^k(M(A,n))\to H^{k+1}(\text{pair})\to H^{k+1}(M(B,n))\to H^{k+1}(M(A,n))\to\cdots .
$$
Putting $k=n$ and using steps [](#cohomology-of-moore){.pf-ref} and [](#pair){.pf-ref} gives the displayed middle stretch. The sequence begins with an injection: the term mapping into $H^{n}(\text{pair};G)$ is $H^{n-1}(M(A,n);G)$, which is $\widetilde H^{n-1}(M(A,n);G)=0$ for $n\ge2$ and is $H^{0}(M(A,1);G)=G$ for $n=1$, where $H^{0}(M(B,1);G)\to H^{0}(M(A,1);G)$ is the identity map of $G$, because both spaces are connected and the pair is that of a subcomplex; so in both cases the connecting map into $H^{n}(\text{pair};G)$ is zero. It ends at $\operatorname{Ext}(A,G)$ because $H^{n+2}$ of the pair is $\widetilde H^{n+2}(M(C,n);G)=0$. So the sequence begins and ends with a zero as displayed, which is the claimed exact sequence.

:::

:::

:::
:::
