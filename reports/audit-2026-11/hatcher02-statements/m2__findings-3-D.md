# findings-3-D — SRC-TEXT-HAT02 §3.D (The Cohomology of SO(n))

Cards in section: **3** (E-HAT-3.D-1 … 3). Book exercise block: AT.txt **line 15093** ("Exercises"),
statements at **15094–15099**. In-text pointer to exercise 1 at **14620–14622**.

## Per card

| id | statement | proof |
|---|---|---|
| E-HAT-3.D-1 | **statement matches.** Book 15094–15096: "1. Show that a topological group with a finite-dimensional CW structure is an ori-entable manifold. [Consider the homeomorphisms x ֏ gx or x ֏ xg for fixed g and varying x in the group.]" Card keeps both sentences and the bracketed hint. (Only rendering differs: the book's mapsto glyph "֏" is written `\mapsto`.) | unread (statement layer only) |
| E-HAT-3.D-2 | **statement matches.** Book 15097–15098: "2. Using the CW structure on SO(n) , show that π1 SO(n) ≈ Z2 for n ≥ 3 . Find a loop representing a generator, and describe how twice this loop is nullhomotopic." | unread |
| E-HAT-3.D-3 | **statement matches.** Book 15099: "3. Compute the Pontryagin ring structure in H∗ (SO(5); Z) ." | unread |

## Defects
None at the statement level. All three statements are faithful, including the bracketed hint on
exercise 1 (AT 15095–15096).

## Census
Cards already carrying `source-checked` + `solution-written` + `solution-reviewed` in frontmatter
(all three authored `gpt-5.6-sol`, dates 2026-09-09): 3/3. Those frontmatter events are therefore
not evidence of a `claude` review; the section is unread in the sense of the task.

## PROOF AUDIT (read in full)

- **E-HAT-3.D-1 — proof correct.** Key steps check out: the complement of a single top-dimensional
  cell is a subcomplex hence closed, so `e^d` is open and ≅ R^d (this is Hatcher's own point at AT
  14619–14623, that SO(n) is connected because it has a CW structure with a single 0-cell); left
  translation is a homeomorphism, so every point has a Euclidean d-neighbourhood. The orientation
  transport is right: the transition map is `L_h L_g^{-1}=L_{hg^{-1}}` and the path `L_{γ(t)}` is an
  isotopy from the identity, so orientation class is preserved. One step is informal — "transport it
  to g by L_g" presupposes path-independence, which the following two sentences then supply — but
  the argument is complete and valid.
- **E-HAT-3.D-2 — proof correct** (checked against AT 14620–14700 and 14787–14798). Cells are
  indexed by admissible sequences with cell dimension the sum of the entries (AT 14795–14797: "this
  product of spheres also has cells in one-to-one correspondence with admissible sequences"), so for
  n ≥ 3 the 2-skeleton has exactly e^0, e^1, e^2. The 2-cell of RP^{n-1} attaches to RP^1 by the
  double cover, giving ⟨a | a²⟩ = Z_2, and higher cells do not change π1. The geometric description
  of the generator (a 2-plane rotating through 0 ≤ θ ≤ 2π) and of the nullhomotopy of twice it (the
  characteristic map of e² traverses e¹ twice) is consistent with that attaching map.
- **E-HAT-3.D-3 — proof has a (minor) gap.** The additive answer is right: free Z in degrees
  0,3,7,10 and Z_2 in 1,3,4,5,6,8 is exactly what the book's own description gives — AT 15085–15091
  ("Thus SO(n) has the same homology and cohomology groups as the product space V3,2 × V5,2 × ··· "),
  combined with the table H_i(V_{2k+1,2};Z) = Z for i = 0,4k−1 and Z_2 for i = 2k−1 (AT 15080–15084).
  But the card *asserts* "The cellular complex of SO(5) is C^2⊗C^4" and then invokes the integral
  Künneth theorem on it. That isomorphism of chain complexes is nowhere established, and AT
  15086–15089 explicitly says SO(n) is *distinguished* from the product by its cup product
  structure, so the product's complex cannot simply be substituted for SO(5)'s. The Künneth
  computation of the groups is therefore unsupported (though its output is correct). Two further
  assertions are used without argument: that `bd` generates H_10(SO(5);Z), and that reduction mod 2
  is injective on each 2-torsion subgroup (true, but only for 2-groups). The mod-2 input the card uses
  ("exterior algebra on e^1,e^2,e^3,e^4") is correct: it is the Hopf-algebra dual of Theorem 3D.2's
  Z_2[β_i]/(β_i^{p_i}) (AT 14799–14801).
