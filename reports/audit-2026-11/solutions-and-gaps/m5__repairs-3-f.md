# Repairs — Hatcher, §3.F: `E-HAT-3.F-2`, `E-HAT-3.F-3`, `E-HAT-3.F-7` (swarm slice 7)

**Scope.** The three §3.F cards named in slice 7: the Mittag–Leffler card, the `Ext(A, Q) = 0`
card, and the Moore-space quotient card. Nothing under `corpus/` was touched. Each repair is an
exact `OLD:`/`NEW:` replacement of one step, and the `NEW` text *is* the corrected step in full.
The repaired cards are materialised in `.scratch/repaired/` and can be regenerated with
`python3 verify_repairs.py`; the blocks below are generated from the same files by
`python3 build_doc.py`, so they cannot drift from what is offered for installation.

This file is also a patch specification in the form `tools/apply_repairs.py` consumes, so it
can be applied mechanically; `--check` first, and note that a plain run installs all six
blocks, the three assigned repairs of §1–§3 **and** the three optional ones of §4. To install
only the assigned three, delete the §4 blocks (or paste the three `*.OLD.txt`/`*.NEW.*` pairs
by hand).

**Authority.** `tmp/hat/AT.txt`; line numbers are `awk 'NR'` record numbers of that file
(records separated by a newline — the file contains form feeds, so Python's
`str.splitlines()` would inflate every number). §3.F begins at the page headed
`Limits and Ext  Section 3.F  311` (AT.txt:15482) and ends where §3.G begins
(AT.txt:16016). Printed pages are read off the running heads in the file: e.g. the records
AT.txt:15536–15658 lie between the heads for pages 312 and 314 and are therefore on page 313.
Quotations below are the extraction's own text, including its mangled inverse limits
(`lim1 Gi` with `←--` on the next line is the book's `lim¹ G_i`) and `Q` for `ℚ`.

**Result at a glance.**

| card | printed statement | defect in the card | repaired in |
| --- | --- | --- | --- |
| `E-HAT-3.F-2` | AT.txt:15980–15984 | a step says to choose `g_0` "arbitrarily"; the recursion is unsolvable unless `g_0 ∈ I_0` | §1 |
| `E-HAT-3.F-3` | AT.txt:15985–15986 | a step passes from `H_{n+1}(X;Q) = 0` to `H^{n+1}(X;Q) = 0` without the field-coefficient universal coefficient theorem, and states the rational homology of `X` without the Tor term | §2 |
| `E-HAT-3.F-7` | AT.txt:15997–16003 | the construction is carried out only for `n ≥ 2`, while the exercise and Example 2.40 cover every `n ≥ 1` | §3 |

All three printed statements are correctly transcribed in the cards: the defects are proof
defects. Three further appeals in these cards are true but unnamed; they are not the assigned
gaps and are offered separately, as optional blocks, in §4.

---

## 1. `E-HAT-3.F-2` — `g_0` has to lie in `I_0`

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-2.md

BOOK, exercise 2 (AT.txt:15980–15984):
```
                                                              α2        α1
             lim1 Gi = 0 if the sequence ··· ---→ G2 ------→ G1 ------→ G0 satisfies the
2. Show that ←--
Mittag–Leffler condition that for each i the images of the maps Gi+n →Gi are inde-
pendent of n for sufficiently large n .
```
BOOK, the same recursion with `g_0 = 0` in the case where all the bonding maps are onto
(AT.txt:15639–15643, page 313):
```
      If all the αi ’s are isomorphisms then ←-- lim Gi ≈ G0 and lim1 Gi = 0 . In fact,
                                                                     ←--          Q
      lim1 Gi = 0 if each αi is surjective, for to realize a given element (hi ) ∈ i Gi as
      ←--
      δ(gi ) we can take g0 = 0 and then solve α1 (g1 ) = −h0 , α2 (g2 ) = g1 − h1 , ··· .
```
DEFECT: the card's step instructs the reader to choose `g_0` *arbitrarily*. The equation to be
solved at the first stage is `α_1(g_1) = g_0 − b_0`, whose right side must lie in
`α_1(G_1) = I_0`; an arbitrary `g_0 ∈ G_0` need not. The instruction is false, not merely
under-justified: for the tower `Z ←0← 0 ←0← ···` with `G_0 = Z` and `G_i = 0` for `i ≥ 1`
(the Mittag–Leffler condition is met trivially, and `I_0 = 0`), the element `b = 0` forces
`g_0 = 0`, since `α_1 = 0` admits no `g_1` with `α_1(g_1) = 1`. With `g_0 ∈ I_0` everything
works, because the stable images carry exactly the structure the recursion needs, and that
structure is what the card's preceding sentence proves.

OLD: the step as it stands, byte-exact.
```text
Hence the tower $(I_i)$ has surjective bonding maps, so its $\varprojlim{}^1$ vanishes: given $(b_i)\in\prod I_i$, choose $g_0$ arbitrarily and then recursively choose $g_{i+1}$ with
$$
\alpha_{i+1}(g_{i+1})=g_i-b_i.
$$
This solves $\Phi(g)=b$.
```
NEW: the corrected step in full.
```text
Hence the tower $(I_i)$ has surjective bonding maps, so its $\varprojlim{}^1$ vanishes. Precisely, since $\alpha_{i+1}(I_{i+1})=I_i$, the map $\Phi$ carries $\prod_i I_i$ into itself, so $\varprojlim{}^1I_i$ is the cokernel of the restriction of $\Phi$ to $\prod_i I_i$, and it is enough to solve $\Phi(g)=b$ with $g\in\prod_i I_i$, for each $b=(b_i)\in\prod_i I_i$. Take $g_0=0$, which lies in $I_0$, and then choose $g_{i+1}\in I_{i+1}$ recursively with
$$
\alpha_{i+1}(g_{i+1})=g_i-b_i.
$$
Each choice is possible: $g_i\in I_i$ by induction and $b_i\in I_i$, so $g_i-b_i\in I_i=\alpha_{i+1}(I_{i+1})$. The resulting $g=(g_i)\in\prod_i I_i$ satisfies
$$
g_i-\alpha_{i+1}(g_{i+1})=b_i\qquad\text{for all }i,
$$
that is, $\Phi(g)=b$.
```

WHY THE NEW STEP IS CORRECT.
1. `Φ` carries `∏_i I_i` into itself: for `g_i ∈ I_i` one has
   `α_{i+1}(g_{i+1}) ∈ α_{i+1}(I_{i+1}) = I_i` by the card's preceding sentence. So `lim¹ I_i`
   is the cokernel of `Φ` restricted to `∏_i I_i`, and surjectivity of that restriction is
   exactly what has to be shown.
2. `g_0 = 0` lies in `I_0`; this is what the book does (AT.txt:15641–15643).
3. Induction: if `g_i ∈ I_i` then `g_i − b_i ∈ I_i = α_{i+1}(I_{i+1})`, so some
   `g_{i+1} ∈ I_{i+1}` satisfies `α_{i+1}(g_{i+1}) = g_i − b_i`, and choosing such an element
   keeps the induction hypothesis available. Only the surjectivity of `α_{i+1}` on `I_{i+1}`,
   already proved in the card, is used.
4. For those choices, `Φ(g)_i = g_i − α_{i+1}(g_{i+1}) = b_i` for every `i`, i.e. `Φ(g) = b`;
   hence `lim¹ I_i = 0`.

Nothing else in the card refers to the removed sentence, and the following paragraph (the
quotient tower `Q_i = G_i/I_i`) reads unchanged.

---

## 2. `E-HAT-3.F-3` — the field-coefficient universal coefficient theorem

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-3.md

BOOK, exercise 3 (AT.txt:15985–15986):
```
3. Show that Ext(A, Q) = 0 for all A . [Consider the homology with Q coefficients of
a Moore space M(A, n) .]
```
The step to be repaired is the second nested step of the card's third proof (`s3`,
"Alternative topological perspective via Moore spaces"). It has two defects.

* **`H_{n+1}(X;Q) = 0 ⟹ H^{n+1}(X;Q) = 0` is unproved.** The card's preceding nested step
  displays the integral coefficient sequence of Theorem 3.2 (AT.txt:9744–9749, page 195):
  ```
   Theorem 3.2. If a chain complex C of free abelian groups has homology groups
 Hn (C) , then the cohomology groups H n (C; G) of the cochain complex Hom(Cn , G)
 are determined by split exact sequences
                                                     h
                0 -→ Ext(Hn−1 (C), G) -→ H n (C; G) --→ Hom(Hn (C), G) -→ 0              ⊓
                                                                                         ⊔
  ```
  and the step under repair concludes from it that "the exact sequence forces
  `Ext(A,Q) = 0`". But in that sequence
  `Ext(A,Q)` is the kernel of `H^{n+1}(X;Q) → Hom(H_{n+1}(X),Q)`, so the inference needs
  `H^{n+1}(X;Q) = 0` from somewhere else — as written the step is circular. The missing
  ingredient is the field-coefficient form of the theorem, printed at AT.txt:9904–9908
  (page 198):
  ```
  …groups H n (X; F ) . In the generalization of the universal coefficient theorem to the
case of modules over a principal ideal domain, the ExtF terms vanish since F is a
field, so we obtain isomorphisms

                                   H n (X; F ) ≈ HomF (Hn (X; F ), F )
  ```
  With `F = Q` this reads `H^{n+1}(X;Q) ≅ Hom_Q(H_{n+1}(X;Q), Q)`, which vanishes as soon as
  `H_{n+1}(X;Q)` does. That isomorphism, and not the integral sequence, is the step that was
  missing.
* **The rational homology of `X` is stated without its Tor term.** `H_{n+1}(X;Q) ≅
  H_{n+1}(X) ⊗ Q` is not the universal coefficient theorem, which reads (Theorem 3A.3,
  AT.txt:13099–13102, page 264)
  ```
   Theorem 3A.3. If C is a chain complex of free abelian groups, then there are natural
 short exact sequences
                  0 -→ Hn (C) ⊗ G -→ Hn (C; G) -→ Tor(Hn−1 (C), G) -→ 0
 for all n and all G , and these sequences split, though not naturally.
  ```
  Here the conclusion `H_{n+1}(X;Q) = 0` is still correct, but it needs both outer terms:
  `H_{n+1}(X) = 0` *and* `Tor(H_n(X),Q) = Tor(A,Q) = 0`, and the second is a real input
  (Proposition 3A.5(3), AT.txt:13141, page 265: `Tor(A,B) = 0 if A or B is free, or more
  generally torsionfree`), not a consequence of the first.

OLD: the whole nested step, byte-exact.
```text
::: pf-step

Since $\QQ$ is a field, $H_{n+1}(X; \QQ) \cong H_{n+1}(X) \otimes \QQ = 0 \otimes \QQ = 0$, so $H^{n+1}(X; \QQ) = 0$.
The exact sequence forces $\operatorname{Ext}(A, \QQ) = 0$.

::: pf-proof

exactness with vanishing middle group.

:::

:::
```
NEW: the corrected step in full — two sibling steps, the first carrying the new label `s3a`,
which the second cites, so the nested numbering becomes `3.1, 3.2, 3.3` and the reference
renders as "3.2".
```markdown
::: {.pf-step #s3a}

$H_{n+1}(X; \QQ) = 0$.

::: pf-proof

Theorem 3A.3 in degree $n+1$ applies to the free cellular chain complex of $X$ and, together with $\widetilde H_{n+1}(X) = 0$ and $\widetilde H_n(X) \cong A$, gives the exact sequence
$$
0 \longrightarrow H_{n+1}(X) \otimes \QQ \longrightarrow H_{n+1}(X; \QQ) \longrightarrow \operatorname{Tor}(H_n(X), \QQ) \longrightarrow 0,
$$
whose outer terms are $0 \otimes \QQ = 0$ and $\operatorname{Tor}(A, \QQ) = 0$, the latter because $\QQ$ is torsionfree (Proposition 3A.5(3)). Hence $H_{n+1}(X; \QQ) = 0$.

:::

:::

::: {.pf-step #s3b}

$H^{n+1}(X; \QQ) = 0$, and hence $\operatorname{Ext}(A, \QQ) = 0$.

::: pf-proof

Over the field $\QQ$, cohomology is the dual of homology, $H^{n+1}(X; \QQ) \cong \operatorname{Hom}_{\QQ}(H_{n+1}(X; \QQ), \QQ)$, since the $\operatorname{Ext}$ term of the universal coefficient theorem vanishes when the coefficient group is a field (§3.1, page 198); this group is zero by step [](#s3a){.pf-ref}. Then Theorem 3.2 in degree $n+1$, with $H_n(X) \cong A$ and $H_{n+1}(X) = 0$, gives the exact sequence
$$
0 \longrightarrow \operatorname{Ext}(A, \QQ) \longrightarrow H^{n+1}(X; \QQ) \longrightarrow \operatorname{Hom}(H_{n+1}(X), \QQ) \longrightarrow 0,
$$
so $\operatorname{Ext}(A, \QQ) = 0$.

:::

:::
```

WHY THE NEW STEPS ARE CORRECT.
1. `X = M(A,n)` has `H̃_i(X) = 0` for `i ≠ n` and `H̃_n(X) ≅ A` (the card's preceding step) and
   `C_*(X)` is free, so Theorem 3A.3 in degree `n+1` gives
   `0 → H_{n+1}(X) ⊗ Q → H_{n+1}(X;Q) → Tor(H_n(X),Q) → 0`, i.e. `0 → 0 → H_{n+1}(X;Q) → 0`
   once `H_{n+1}(X) = 0` and `Tor(A,Q) = 0` (Proposition 3A.5(3): `Q` is torsionfree). Hence
   `H_{n+1}(X;Q) = 0`.
2. Over the field `Q`, `H^{n+1}(X;Q) ≅ Hom_Q(H_{n+1}(X;Q), Q)` (AT.txt:9904–9908, page 198),
   which is `0` by step `s3a`.
3. Theorem 3.2 in degree `n+1` with `G = Q` gives
   `0 → Ext(H_n(X),Q) → H^{n+1}(X;Q) → Hom(H_{n+1}(X),Q) → 0`; with `H̃_n(X) ≅ A` and
   `H^{n+1}(X;Q) = 0`, exactness gives `Ext(A,Q) = 0`.

For the record: the card's *other* proof (`s1` + `s2` — `Q` is divisible, hence injective by
Baer's criterion, hence `d* : Hom(F_0,Q) → Hom(F_1,Q)` is onto for a free presentation of `A`,
hence `Ext(A,Q) = coker d* = 0`) is complete and already establishes the statement. The repair
is needed because the card presents the book's Moore-space argument as a second route, and that
route did not stand as written.

---

## 3. `E-HAT-3.F-7` — the construction has to cover `n = 1`

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-7.md

BOOK, exercise 7 (AT.txt:15997–16003):
```
7. Show that for a short exact sequence of abelian groups 0→A→B →C →0 , a Moore
space M(C, n) can be realized as a quotient M(B, n)/M(A, n) . Applying the long exact
«page break»
sequence of cohomology for the pair M(B, n), M(A, n) with any coefficient group
G , deduce an exact sequence

 0→Hom(C, G)→Hom(B, G)→Hom(A, G)→Ext(C, G)→Ext(B, G)→Ext(A, G)→0
```
The exercise places no restriction on `n`, and Hatcher's construction of Moore spaces is made
"Given an abelian group `G` and an integer `n ≥ 1`" (Example 2.40, AT.txt:7201–7202,
page 143). So the exercise is about every `n ≥ 1`.

DEFECT: the card opens "For `n ≥ 2`, realize `i` by a cellular map `M(A,n) → M(B,n)` inducing
`i` on the only nonzero reduced homology group", and the whole construction inherits that
restriction, so the card proves the statement only for `n ≥ 2`. Three things are missing or
merely asserted:

1. no treatment of `n = 1`, which the exercise includes;
2. the existence of that cellular map is asserted, not proved — the tools for it (Hurewicz and
   Whitehead, Theorems 4.37 and 4.5) are not available in §3.F;
3. "The spaces in the pair are `(n−1)`-connected, so their quotient `Q` is `(n−1)`-connected as
   well" is asserted too. It is true, but it rests on the cell structure: the quotient has
   cells only in dimensions `0`, `n`, `n+1`, and one should say so.

The replacement removes all three at once, by building `M(A,n)`, `M(B,n)` and `M(C,n)` from
*compatible* bases, so that `M(A,n)` is a subcomplex of `M(B,n)` and the quotient is a Moore
space `M(C,n)` on the nose, for every `n ≥ 1`. No Hurewicz, no Whitehead, no `K(·,1)`.

One warning, because the natural shortcut for `n = 1` is wrong: a Moore space `M(G,1)` must
have `H_2 = 0`, and `K(G,1)` need not have it. For `G = Z²` the space `K(Z²,1)` is the torus,
and `H_2(T²) ≅ Z` (Example 2.3, AT.txt:5365–5376, page 106):
```
Example 2.3. X = T , the torus with the ∆ complex structure pictured earlier, having
one vertex, three edges a , b , and c , and two 2 simplices U and L . As in the previous
example, ∂1 = 0 so H0∆(T ) ≈ Z . Since ∂2 U = a + b − c = ∂2 L and {a, b, a + b − c} is
a basis for ∆1 (T ) , it follows that H1∆(T ) ≈ Z ⊕ Z with basis the homology classes [a]
and [b] . Since there are no 3 simplices, H2∆(T ) is equal to Ker ∂2 , which is infinite
cyclic generated by U − L since ∂(pU + qL) = (p + q)(a + b − c) = 0 only if p = −q .
```
So the `n = 1` case is not a formality; it needs the compatible-basis argument below.

OLD: the whole first paragraph of the proof, i.e. the construction, byte-exact.
```text
Choose Moore spaces functorially enough for the given short exact sequence
$$
0\to A\xrightarrow{i}B\xrightarrow{q}C\to0.
$$
For $n\ge2$, realize $i$ by a cellular map
$$
M(A,n)\longrightarrow M(B,n)
$$
inducing $i$ on the only nonzero reduced homology group. Replace it by a mapping-cylinder inclusion, so we may regard $M(A,n)$ as a subcomplex of $M(B,n)$. Let
$$
Q=M(B,n)/M(A,n).
$$
The reduced homology long exact sequence of the pair gives
$$
\widetilde H_j(Q)=0\quad(j\ne n),
\qquad
\widetilde H_n(Q)\cong B/A\cong C.
$$
The spaces in the pair are $(n-1)$-connected, so their quotient $Q$ is $(n-1)$-connected as well. Thus $Q$ is a Moore space $M(C,n)$, so
$$
M(C,n)\simeq M(B,n)/M(A,n).
$$
```
NEW: the corrected construction in full.
```text
Let
$$
0\to A\xrightarrow{i}B\xrightarrow{q}C\to0
$$
be the given short exact sequence. Choose a generating set $S_A$ of $A$ and extend it to a generating set $S_B=S_A\sqcup S'$ of $B$ by adjoining preimages in $B$ of a generating set of $C$; let $F_B=\ZZ^{(S_B)}$ and $F_A=\ZZ^{(S_A)}\subseteq F_B$ be the free abelian groups on these bases, and let
$$
K_B=\ker(F_B\to B),\qquad K_A=\ker(F_A\to A)
$$
be the kernels of the surjections sending each basis element to itself. Then $K_B\cap F_A=K_A$, so $K_B/K_A$ is isomorphic to a subgroup of $F_B/F_A=\ZZ^{(S')}$ and hence is free abelian, as in Example 2.40. A basis $T_A$ of $K_A$ together with lifts to $K_B$ of a basis of $K_B/K_A$ is therefore a basis $T=T_A\sqcup T'$ of $K_B$.

For $n\ge1$ let $M(B,n)$ be the CW complex of Example 2.40 built from these data: a wedge of $n$-spheres indexed by $S_B$, with one $(n+1)$-cell $e^{n+1}_t$ attached for each $t\in T$, the attaching map of $e^{n+1}_t$ being chosen so that its composite with the projection onto the summand $S^n_s$ has degree the coefficient of $s$ in $t=\sum_s d_{t,s}s$. As Hatcher computes in Example 2.40, the cellular boundary map $d_{n+1}$ is then the inclusion $K_B\hookrightarrow F_B$, so
$$
H_n(M(B,n))\cong F_B/K_B\cong B,\qquad H_{n+1}(M(B,n))=0,
$$
the remaining reduced homology vanishing because there are no other cells. Since $T_A\subseteq T$ and each $t\in T_A$ lies in $F_A$, the corresponding cells form a subcomplex which by the same computation is a Moore space $M(A,n)$ with $H_n\cong A$.

Let $Q=M(B,n)/M(A,n)$. Its cells are one $0$-cell, the $n$-cells indexed by $S'$ and the $(n+1)$-cells indexed by $T'$, and after $M(A,n)$ has been collapsed to a point the coefficient of each $n$-cell $S^n_s$ with $s\in S_A$ is $0$, so $d_{n+1}\colon\ZZ^{(T')}\to\ZZ^{(S')}$ records only the $S'$-coordinates. That map is injective: an integral combination of elements of $T'$ lying in $F_A$ lies in $K_B\cap F_A=K_A$, and the subgroup generated by $T'$ meets $K_A$ trivially. Hence $\widetilde H_{n+1}(Q)=0$ and
$$
\widetilde H_n(Q)\cong \ZZ^{(S')}/\operatorname{im}d_{n+1}\cong F_B/(K_B+F_A)\cong B/A\cong C,
$$
where $(K_B+F_A)/K_B\cong F_A/(K_B\cap F_A)=F_A/K_A\cong A$, and all other reduced homology of $Q$ vanishes. Thus $Q$ is a Moore space $M(C,n)$, and this holds for every $n\ge1$, the range in which Example 2.40 constructs Moore spaces.
```

WHY THE NEW CONSTRUCTION IS CORRECT.
1. `S_A` generates `A` and `S_B = S_A ⊔ S'` generates `B`; `F_A ⊂ F_B` are free on those bases,
   and the maps onto `A` and `B` send each basis element to itself, so both are onto, with
   kernels `K_A` and `K_B`.
2. `K_B ∩ F_A = K_A`: an element of `F_A` dies in `B` exactly when its image in `A` dies, since
   that image is what it is. Hence `K_B/K_A ≅ (K_B + F_A)/F_A ⊆ F_B/F_A = Z^{(S')}` is a
   subgroup of a free abelian group, so it is free — the same step Hatcher takes in
   Example 2.40 (AT.txt:7212–7214: "The kernel of this homomorphism is a subgroup of a free
   abelian group, hence is itself free abelian"). Therefore `K_B ≅ K_A ⊕ K_B/K_A`, and a basis
   `T_A` of `K_A` extends to a basis `T = T_A ⊔ T'` of `K_B`.
3. Example 2.40 attaches one `(n+1)`-cell per element of a chosen basis of the kernel, with
   prescribed degrees, and computes (AT.txt:7218–7221): "Then the cellular boundary map
   `d_{n+1}` will be the inclusion `K ↪ F`, hence `X` will have the desired homology groups."
   With `T` a basis of `K_B`, `d_{n+1}` is injective with image `K_B`, so `H_n(M(B,n)) ≅
   F_B/K_B ≅ B` and `H_{n+1}(M(B,n)) = ker d_{n+1} = 0`, all other reduced homology vanishing
   because there are no other cells. The same computation applies to the subcomplex built on
   `S_A` and `T_A` — a subcomplex because each `t ∈ T_A` lies in `F_A`, so its attaching map
   lies in the wedge over `S_A`.
4. In the quotient the remaining cells are the `n`-cells of `S'` and the `(n+1)`-cells of `T'`;
   the boundary map records only `S'`-coordinates and is injective, because a combination of
   elements of `T'` whose `S'`-coordinates vanish lies in `F_A ∩ K_B = K_A`, which meets the
   subgroup generated by `T'` trivially. Its image is `(K_B + F_A)/F_A`, so
   `H̃_n(Q) ≅ (F_B/F_A)/((K_B+F_A)/F_A) ≅ F_B/(K_B+F_A) ≅ B/A = C` — using
   `(K_B+F_A)/K_B ≅ F_A/(K_B∩F_A) = F_A/K_A ≅ A` — and `H̃_{n+1}(Q) = 0`. Hence `Q` is a
   Moore space `M(C,n)`, for every `n ≥ 1`.

The card's second paragraph (the cohomology long exact sequence of the pair) is unaffected:
`(M(B,n), M(A,n))` is still a CW pair and the conclusion is unchanged. Its one unproved
identification is covered by optional block (c) in §4.

---

## 4. Optional, independent hardenings

These are not the assigned gaps: each replaces a true-but-unnamed appeal by its name or by a
two-line proof. They are independent of §1–§3 and of each other, except that (a) and (b) both
live in the card repaired in §1. Install or drop each on its own.

### (a) `E-HAT-3.F-2` — name the subsequence invariance

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-2.md

BOOK (AT.txt:15646–15650, page 313):
```
      Deleting a finite number of terms from the end of the sequence ··· →G1 →G0
      does not affect lim Gi or lim1 Gi . More generally, lim Gi and lim1 Gi are un-
                       ←--          ←--                                    ←--           ←--
      changed if we replace the sequence ··· →G1 →G0 by a subsequence, with the
      appropriate compositions of αj ’s as the maps.
```

OLD: byte-exact.
```text
Passing to a cofinal subsequence, we may assume each bonding map $Q_{i+1}\to Q_i$ is zero.
```
NEW: the corrected step in full.
```text
Since $\varprojlim$ and $\varprojlim{}^1$ do not change when the tower is replaced by a subsequence, with the appropriate composites of the $\alpha_i$ as bonding maps (Hatcher, page 313), we may pass to a cofinal subsequence and assume each bonding map $Q_{i+1}\to Q_i$ is zero.
```

### (b) `E-HAT-3.F-2` — derive the six-term `lim`/`lim¹` sequence

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-2.md

BOOK, the definition the derivation uses (AT.txt:15619–15620, page 313):
```
define a map δ : i Gi → i Gi by δ(··· , gi , ···) = (··· , gi − αi+1 (gi+1 ), ···) , so that
lim Gi is the kernel of δ . Denoting the cokernel of δ by lim1 Gi , we have then an exact
```

OLD: byte-exact.
```text
The short exact sequence of towers
$$
0\to I_i\to G_i\to Q_i\to0
$$
gives the standard exact sequence for inverse limits and their first derived limits. Since both outer $\varprojlim{}^1$ terms vanish, so does the middle one:
```
NEW: the corrected step in full.
```text
Taking products over $i$, the short exact sequence of towers
$$
0\to I_i\to G_i\to Q_i\to0
$$
gives a short exact sequence of two-term complexes $0\to\prod_i I_i\to\prod_i G_i\to\prod_i Q_i\to0$ whose boundary maps are $\delta$, and the snake lemma applied to $\delta$ yields the exact sequence
$$
0\to\varprojlim I_i\to\varprojlim G_i\to\varprojlim Q_i\to\varprojlim{}^1I_i\to\varprojlim{}^1G_i\to\varprojlim{}^1Q_i\to0.
$$
Since $\varprojlim{}^1I_i=0$ and $\varprojlim{}^1Q_i=0$, exactness at $\varprojlim{}^1G_i$ forces $\varprojlim{}^1G_i=0$:
```

WHY (b) IS CORRECT. `δ` is a map of the two-term complex `∏_i X_i → ∏_i X_i`; the product of
the exact rows `0 → I_i → G_i → Q_i → 0` is exact because a product of surjections is
surjective; `ker δ = lim` and `coker δ = lim¹` by Hatcher's definition (AT.txt:15619–15626,
page 313); and the snake lemma, applied to the resulting commutative square of complexes,
produces exactly the six displayed terms. With `lim¹ I_i = 0` and `lim¹ Q_i = 0`, exactness at
`lim¹ G_i` gives `lim¹ G_i = 0`, which is all the card uses.

### (c) `E-HAT-3.F-7` — name Proposition 2.22 in the second paragraph

CARD: corpus/collections/SRC-TEXT-HAT02/3-f/E-HAT-3.F-7.md

BOOK (AT.txt:6294–6295, page 124):
```
 Proposition 2.22. For good pairs (X, A) , the quotient map q : (X, A)→(X/A, A/A)
 induces isomorphisms q∗ : Hn (X, A)→Hn (X/A, A/A) ≈ H   e n (X/A) for all n .
```

OLD: byte-exact.
```text
The long exact sequence of the pair, together with
$$
H^*(M(B,n),M(A,n);G)\cong\widetilde H^*(M(C,n);G),
$$
therefore becomes exactly
```
NEW: the corrected step in full.
```text
For this CW pair the relative cellular chain complex $C_*(M(B,n),M(A,n))$ is the cellular chain complex of $Q$, with free terms, so that
$$
H^*(M(B,n),M(A,n);G)\cong\widetilde H^*(M(C,n);G)
$$
(Proposition 2.22, applied to the cellular chain complexes); the long exact sequence of the pair therefore becomes exactly
```

WHY (c) IS CORRECT. For a CW pair the relative cellular chain complex of the pair *is* the
cellular chain complex of the quotient — the cells of `X/A` are the cells of `X` not in `A`,
plus the collapsed `0`-cell — and each term is free; so `Hom(−,G)` of that complex computes
both `H^*(X,A;G)` and `H̃^*(X/A;G)`. That is Proposition 2.22 read on cellular chains, and CW
pairs are good (AT.txt:6382).

---

## 5. Verification performed

Mechanical, and re-runnable from this directory:

```
python3 extract_old.py       # cuts each OLD out of the card itself
python3 verify_repairs.py    # OLD unique -> NEW applies -> the card parses and renders
python3 build_doc.py         # regenerates this document from those same files
```

1. `extract_old.py` cuts each `OLD` out of the card file itself. The `3.F-3` step is
   cut by fenced-div depth rather than by a text marker, so that the closing fences of the
   enclosing `pf-proof` and `pf-step` stay in the card; a marker cut silently removed two
   closures on the first attempt, which `verify_repairs.py` caught as a nesting change
   (the `QED` step became a nested step and the numbering came out `3.4` instead of `4`).
2. `verify_repairs.py` checks, in installation order, that
   * each `OLD` occurs **exactly once** in the card as it will stand when installed;
   * the card resulting from the replacement has balanced fenced divs (depth `0` at EOF, no
     underflow);
   * the text from `.solution` onwards renders through the repository's own Lamport filter
     (`~/.pandoc/filters/lamport_proof.lua`, the filter `tools/qualc/lamport.py` invokes)
     with `pandoc` exit `0`, and every `pf-ref` resolves to a number;
   * for `E-HAT-3.F-3` the nested numbering comes out `3.1, 3.2, 3.3` with the outer numbers
     `1, 2, 3, 4`, and the new reference renders as `3.2`, i.e. it points at the new step
     `s3a`.
   Current result: `FAILURES: 0`; repaired cards written to `.scratch/repaired/`.
3. The repository's own installer parses this file:
   `python3 tools/apply_repairs.py --check .ultramath/smvy31u3e/m5/repairs-3-f.md` reports
   `would patch .../E-HAT-3.F-2.md (3)`, `.../E-HAT-3.F-3.md (1)`, `.../E-HAT-3.F-7.md (2)`
   and exits `0`, i.e. six patches parsed, every `OLD` unique, no card missing, nothing
   written. `--check` writes nothing, and that is the only mode this document was run in.
4. Every result cited in the `NEW` blocks was checked against `tmp/hat/AT.txt` at the line
   numbers given above, and every page number was read off the running heads of that file.

## 6. Coverage and limits

* Compared with the book: exercise 2 (AT.txt:15980–15984), exercise 3 (AT.txt:15985–15986),
  exercise 7 (AT.txt:15997–16003); the printed statements match the cards. Passages used by the
  repairs: Example 2.40 (AT.txt:7201–7232), Example 2.3 (AT.txt:5365–5376), Proposition 2.22
  (AT.txt:6294–6295), Theorem 3.2 (AT.txt:9744–9749), field coefficients (AT.txt:9904–9908),
  Theorem 3A.3 (AT.txt:13099–13102), Proposition 3A.5 (AT.txt:13137–13147), `lim`/`lim¹`
  (AT.txt:15613–15650).
* Read in full, beyond the repaired steps: all of `E-HAT-3.F-2`, `E-HAT-3.F-3`, `E-HAT-3.F-7`.
  Apart from the repaired defects I found no false step in them; the remaining unproved-but-true
  appeals are §4 (a), (b) for `3.F-2` and §4 (c) for `3.F-7`.
* Not done here: I did not audit the other six §3.F cards (`3.F-1`, `-4`, `-5`, `-6`, `-8`,
  `-9`) — they are outside this slice — and I changed no frontmatter, audit event, title or
  statement. In particular I did not re-issue audit events: `E-HAT-3.F-3` still carries only a
  `solution-written` event, and the `solution-reviewed` events on `3.F-2` and `3.F-7` predate
  these repairs.
* Nothing is installed under `corpus/`; `.scratch/repaired/` is for inspection only.
* **File inventory** (this directory, `.ultramath/smvy31u3e/m5/`):
  * `repairs-3-f.md` — this file.
  * The three assigned repairs, byte-exact and ready to paste:
    `E-HAT-3.F-2.OLD.txt` / `E-HAT-3.F-2.NEW.txt`,
    `E-HAT-3.F-3.OLD.txt` / `E-HAT-3.F-3.NEW.md`,
    `E-HAT-3.F-7.OLD.txt` / `E-HAT-3.F-7.NEW.txt`.
  * The optional hardenings: `E-HAT-3.F-2.OPT-a.{OLD,NEW}.txt`,
    `E-HAT-3.F-2.OPT-b.{OLD,NEW}.txt`, `E-HAT-3.F-7.OPT-c.{OLD,NEW}.txt`.
  * Scripts: `extract_old.py` (writes the `OLD` blocks), `verify_repairs.py` (the checks
    above; writes the repaired cards), `build_doc.py` (writes this document). Each `.OLD` file
    is written by `extract_old.py`, so re-running it must leave the files unchanged; it does.
  * `.scratch/` holds only regenerable outputs: `repaired/<card>.md` and
    `<card>.solution.md`.
