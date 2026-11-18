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

---

::: {.problem}
Use Exercise 4 to construct a multiplication map $\mu: K(G, n) \times K(G, n) \to K(G, n)$ for any abelian group $G$, making a CW complex $K(G, n)$ into an H-space whose multiplication is commutative and associative up to homotopy and has a homotopy inverse.
Show also that the H-space multiplication $\mu$ is unique up to homotopy.
:::

::: {.solution}

The construction and the uniqueness are the card's own, both resting on Exercise 4: homotopy classes of maps into $K(G,n)$ are the cohomology group $H^{n}(-;G)$, so on a product of Eilenberg--MacLane spaces they are homomorphisms on $\pi_{n}$. Write $K=K(G,n)$ with $G$ abelian.

::: pf

::: {.pf-step #classification}
$K\times K$ is a $K(G\oplus G,n)$, and homotopy classes of maps $K\times K\to K$ correspond to homomorphisms $G\oplus G\to G$.

::: pf-proof
A product of Eilenberg--MacLane spaces is again one: $\pi_{n}(K\times K)=G\oplus G$ and the other homotopy groups vanish. By Exercise 4, $[B,K(G,n)]\cong H^{n}(B;G)$ for CW complexes $B$; for $B=K\times K$ the Hurewicz and universal coefficient theorems give $H^{n}(B;G)\cong\Hom(H_{n}(B),G)=\Hom(G\oplus G,G)$, the higher homology of a $K(G\oplus G,n)$ being confined to degree $n$ and $H_{n}=G\oplus G$.
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
