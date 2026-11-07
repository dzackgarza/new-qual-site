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
---

::: {.problem}
Make the transfer sequence explicit in the case of a trivial covering $\tilde{X} \to X$, where $\tilde{X} = X \times S^0$.
:::

::: {.solution}
Read **Hatcher's transfer construction, §2.B, printed pp. 173--174**, for the covering $X\times S^0\to X$. This gives the complete chain-level computation; no separate exactness argument is needed.

Use $\ZZ_2$ coefficients, as in the transfer sequence of §2.B. Since $X\times S^0=X\amalg X$, its singular chain complex is $C_*(X;\ZZ_2)\oplus C_*(X;\ZZ_2)$. In these coordinates the transfer and projection are
$$
\tau(c)=(c,c),\qquad p_\#(a,b)=a+b.
$$
Thus the short exact sequence defining Hatcher's transfer sequence is
$$
0\longrightarrow C_*(X;\ZZ_2)
\xrightarrow{\Delta}
C_*(X;\ZZ_2)^2
\xrightarrow{+}
C_*(X;\ZZ_2)\longrightarrow0.
$$
The diagonal is injective, the sum is surjective, and its kernel is the diagonal because the coefficients have characteristic two. The sequence splits as a sequence of chain complexes: $c\mapsto(c,0)$ is a section of the sum map. Consequently every connecting homomorphism vanishes, and the transfer sequence is the split short exact sequence
$$
0\longrightarrow H_n(X;\ZZ_2)
\xrightarrow{x\mapsto(x,x)}
H_n(X;\ZZ_2)^2
\xrightarrow{(a,b)\mapsto a+b}
H_n(X;\ZZ_2)\longrightarrow0
$$
in each degree $n$.
:::
