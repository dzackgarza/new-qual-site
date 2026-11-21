---
schema: qual/card@1
id: E-HAT-4.3-6
kind: problem
title: "H-space structure on $K(G,n)$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 6 of §4.3, printed p. 419, with Exercise 4 and Theorem 4.57.
    Correct: $K\times K$ is a $K(G\oplus G,n)$, so homotopy classes $K\times K\to K$ are
    $\operatorname{Hom}(G\oplus G,G)$ through $[B,K(G,n)]\cong H^n(B;G)$ and
    $H^n(K(G\oplus G,n);G)=\operatorname{Hom}(G\oplus G,G)$; addition gives a multiplication whose
    restrictions to $K\times\{e\}$ and $\{e\}\times K$ correspond to $a\mapsto a+0$ and
    $b\mapsto 0+b$, so the unit holds up to homotopy; associativity, commutativity and the inverse
    $a\mapsto-a$ follow because the three composites induce the same homomorphism on
    $\pi_n=G\oplus G\oplus G$ or $G\oplus G$; and uniqueness holds because any H-space
    multiplication restricts to the identity on each factor up to homotopy, hence induces
    $(a,b)\mapsto a+b$, which determines it up to homotopy. Nothing changed. Not claimed: a
    published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.3 Exercise 6, with Exercise 4,
    Theorem 4.57, and the retained solution of Steven V. Sam, §4.3 Exercise 6,
    of `tmp/sources/hatcher-solutions-sam-2008.pdf`. Two defects repaired. The
    card attributed the bijection $[B,K(G,n)]\cong H^{n}(B;G)$ for all CW complexes $B$ to
    Exercise 4, which gives only the case $B=K(G',n)$; it now cites Theorem 4.57 for the
    general statement and Exercise 4 for the case at hand. And it read $H^{n}(B;G)\cong
    \Hom(H_{n}(B),G)$ off the universal coefficient theorem without the Ext term; the sequence
    is now written out and the vanishing of $\Ext(H_{n-1}(B),G)$ is argued separately for
    $n\ge2$ and $n=1$. The lead claimed the argument was the card's own; Sam's solution covers
    the exercise and is now named, with the coefficient computation identified as what the card
    adds. Statement unchanged. Not checked: Exercise 4 itself was not re-derived, and there is
    no certificate.
---

::: {.problem}
Use Exercise 4 to construct a multiplication map $\mu: K(G, n) \times K(G, n) \to K(G, n)$ for any abelian group $G$, making a CW complex $K(G, n)$ into an H-space whose multiplication is commutative and associative up to homotopy and has a homotopy inverse.
Show also that the H-space multiplication $\mu$ is unique up to homotopy.
:::

::: {.solution}

The construction and the uniqueness follow the retained solution set of **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.3 Exercise 6**: $K(G,n)\times K(G,n)\simeq K(G\times G,n)$, Exercise 4 turns maps out of that product into homomorphisms $G\times G\to G$, and the addition homomorphism gives the multiplication. The steps below write out the coefficient computation that solution leaves implicit. Write $K=K(G,n)$ with $G$ abelian.

::: pf

::: {.pf-step #classification}
$K\times K$ is a $K(G\oplus G,n)$, and homotopy classes of maps $K\times K\to K$ correspond to homomorphisms $G\oplus G\to G$.

::: pf-proof
A product of Eilenberg--MacLane spaces is again one: $\pi_{n}(K\times K)=G\oplus G$ and the other homotopy groups vanish. Theorem 4.57 identifies $\langle B,K(G,n)\rangle$ with $H^{n}(B;G)$ for every CW complex $B$, and for $B=K\times K=K(G\oplus G,n)$ Exercise 4 identifies that set with $\Hom(G\oplus G,G)$. The coefficient computation is the universal coefficient sequence $0\to\Ext(H_{n-1}(B),G)\to H^{n}(B;G)\to\Hom(H_{n}(B),G)\to0$: $H_{n}(B)$ is $G\oplus G$, by Hurewicz for $n\ge2$ and as the abelianization of $\pi_{1}$ for $n=1$, and $\Ext(H_{n-1}(B),G)$ vanishes, since $H_{n-1}(B)=0$ for $n\ge2$ while $H_{0}(B)=\ZZ$ is free for $n=1$. Hence $H^{n}(B;G)=\Hom(G\oplus G,G)$.
:::

:::

::: {.pf-step #multiplication}
The map $\mu$ corresponding to addition $(a,b)\mapsto a+b$ is an H-space multiplication.

::: pf-proof
Let $\mu$ be the class corresponding to $+$ under step [](#classification){.pf-ref}. Its restriction to $K\times\{e\}$ corresponds to the composite $G\to G\oplus G\xrightarrow{+}G$, $a\mapsto a+0=a$, that is to the identity homomorphism, so $\restrictionof{\mu}{K\times\{e\}}\simeq1$; likewise on $\{e\}\times K$. Hence $\mu$ is a multiplication with a two-sided identity up to homotopy, that is an H-space structure on $K$.
:::

:::

::: {.pf-step #properties}
$\mu$ is commutative and associative up to homotopy and has a homotopy inverse.

::: pf-proof
The two maps $\mu(\mu\times1)$ and $\mu(1\times\mu):K^{3}\to K$ both induce $(a,b,c)\mapsto a+b+c$ on $\pi_{n}$, so by step [](#classification){.pf-ref} they are homotopic: associativity up to homotopy. The maps $\mu$ and $\mu\tau$, with $\tau$ the interchange, both induce $(a,b)\mapsto a+b$, so $\mu\simeq\mu\tau$: commutativity up to homotopy. Let $\nu$ correspond to $a\mapsto-a$; then $\mu(1\times\nu)$ induces $a+(-a)=0$, hence is homotopic to the constant map, and similarly $\mu(\nu\times1)$: so $\nu$ is a homotopy inverse.
:::

:::

::: {.pf-step #unique}
Any H-space multiplication on $K$ is homotopic to $\mu$.

::: pf-proof
Let $m:K\times K\to K$ be an H-space multiplication. Up to homotopy it restricts to the identity on $K\times\{e\}$ and on $\{e\}\times K$, so the homomorphism it induces on $\pi_{n}=G\oplus G$ has $a\mapsto a$ on each summand, hence is $a+b$. By step [](#classification){.pf-ref} a map is determined up to homotopy by the homomorphism it induces on $\pi_{n}$, so $m\simeq\mu$. Therefore
$$
\boxed{K(G,n)\text{ has an H-space multiplication, unique up to homotopy, which is commutative and associative up to homotopy and has a homotopy inverse}.}
$$
:::

:::

:::
:::
