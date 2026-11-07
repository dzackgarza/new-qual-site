---
schema: qual/card@1
id: E-HAT-2.B-9
kind: problem
title: "Transfer sequence for trivial coverings"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 9, printed page
    177; the statement matches word for word. Checked: for the trivial double cover
    X × S^0 = X ⊔ X over Z_2 the transfer and projection are τ(c) = (c,c) and
    p(a,b) = a + b, so the transfer sequence is the split short exact sequence
    0 → H_n(X) → H_n(X)^2 → H_n(X) → 0 with all connecting maps zero, the splitting
    being c ↦ (c,0); the chain-level sequence of Hatcher's construction (§2.B,
    p. 173) is split for the same reason. No defect.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Specializes Hatcher's transfer construction on pp.173-174 directly to X times S^0. The
    displayed sequence is already split at chain level: C_*(X times S^0;Z_2) is two copies of
    C_*(X;Z_2), the transfer is the diagonal, projection is addition, and c maps to (c,0) is a
    chain section of projection. Consequently all connecting homomorphisms are zero, not merely
    zero on a homology calculation suggested by the reader.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read Hatcher pp.174-175 in the actual book: p.174 defines the two-lift transfer and proves
    surjectivity of projection, and p.175 identifies the transfer image with its exactness
    kernel before passing to homology. This is a complete published chain-level argument whose
    specialization to X times S^0 is precisely the displayed diagonal/sum sequence and split
    section in the card. Corrected the citation from pp.173-174 to pp.174-175 and checked the
    trivial covering against Hatcher p.177 Exercise 9. The #105 source obligation is covered.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Corrected the preceding coverage claim. Hatcher pp.174-175 supplies the general transfer
    theorem, and the card instantiates it by diagonal/sum coordinates with a chain section.
    That specialization is not itself a complete published exercise solution: the trivial-cover
    coordinate computation and its splitting are absent from every retained published solution
    collection. The mathematical proof is unchanged; the #105 complete-solution source obligation
    remains open.
---

::: {.problem}
Make the transfer sequence explicit in the case of a trivial covering $\tilde{X} \to X$, where $\tilde{X} = X \times S^0$.
:::

::: {.solution}
Hatcher's complete published transfer construction in **§2.B, printed pp. 174--175**, specializes directly to $X\times S^0\to X$. He defines the short exact sequence of chain complexes by sending a singular simplex to the sum of its two lifts and projecting from the total space. The computation below carries out that construction in the two-sheet coordinates; no separate exactness argument is needed. This is a checked instantiation of the general theorem, not a found complete published solution of Exercise 2.B.9, whose source obligation remains open.

Use $\ZZ_2$ coefficients, as in the transfer sequence of §2.B.

::: pf

::: {.pf-step #trivial-chains}
In two-sheet coordinates the transfer and projection are $\tau(c)=(c,c)$ and $p_\#(a,b)=a+b$, giving the exact sequence
$$
0\longrightarrow C_*(X;\ZZ_2)
\xrightarrow{\Delta}
C_*(X;\ZZ_2)^2
\xrightarrow{+}
C_*(X;\ZZ_2)\longrightarrow0.
$$

::: pf-proof
Since $X\times S^0=X\amalg X$, its singular chain complex is $C_*(X;\ZZ_2)\oplus C_*(X;\ZZ_2)$. The two lifts of a base simplex are its images in the two copies, hence $\tau(c)=(c,c)$; projection adds them. The diagonal is injective, addition is surjective, and $(a,b)$ lies in its kernel exactly when $b=-a=a$ in characteristic two, which is exactly the diagonal image.
:::

:::

::: {.pf-step #chain-section}
The short exact sequence in step [](#trivial-chains){.pf-ref} splits as a sequence of chain complexes.

::: pf-proof
The chain map $s(c)=(c,0)$ satisfies $p_\#\circ s=\operatorname{id}$, so it is a section of projection.
:::

:::

::: pf-step
All connecting homomorphisms vanish, and the transfer sequence is the split short exact sequence
$$
0\longrightarrow H_n(X;\ZZ_2)
\xrightarrow{x\mapsto(x,x)}
H_n(X;\ZZ_2)^2
\xrightarrow{(a,b)\mapsto a+b}
H_n(X;\ZZ_2)\longrightarrow0
$$
in each degree $n$.

::: pf-proof
By step [](#chain-section){.pf-ref}, the long exact sequence associated to a split short exact sequence of chain complexes has zero connecting homomorphisms. Exactness at each term therefore gives the displayed homology sequence.
:::

:::

:::
:::
