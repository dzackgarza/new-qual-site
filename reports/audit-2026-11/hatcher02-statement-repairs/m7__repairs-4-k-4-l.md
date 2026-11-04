# Statement-layer repairs: `4-k` and `4-l` (slice 7)

Scope: the 11 cards of `corpus/collections/SRC-TEXT-HAT02/4-k/` (E-HAT-4.K-1 … 6) and
`.../4-l/` (E-HAT-4.L-1 … 5). Authority: `tmp/hat/AT.txt`, §4.K exercises at lines
24094–24121 and §4.L exercises at lines 25802–25820. Nothing under `corpus/` was modified.

Conventions used in the blocks below.
- `OLD` and `NEW` are the exact contents of the fenced block that follows them (no
  surrounding pipes, no added indentation), so `OLD` can be replaced mechanically. Each
  `OLD` was checked to occur **exactly once** as a contiguous string in its card file.
- `BOOK` quotes the printed item with the printed line breaks joined by single spaces.
  AT.txt sets "con-tractible" (4.K ex.2) and "Poincaré" with combining accents across the
  extraction's line breaks; the quotes give the printed words without those artefacts.
- Printed matter is rendered in the card's existing LaTeX style (`$L$`, `$K$`,
  `\quatprojective`, `\OP`), with the printed wording otherwise unchanged.

---

CARD: corpus/collections/SRC-TEXT-HAT02/4-k/E-HAT-4.K-2.md
BOOK: AT.txt:24098-24100  "2. Show that a simplicial map f : K →L is a homotopy equivalence if f −1 (x) is contractible for all x ∈ L . [Consider the cover of L by open stars of simplices and the cover of K by the preimages of these open stars.]"
OLD:
```
Show that a simplicial map $f: K \to L$ is a homotopy equivalence if $f^{-1}(x)$ is contractible for all $x \in L$.
```
NEW:
```
Show that a simplicial map $f: K \to L$ is a homotopy equivalence if $f^{-1}(x)$ is contractible for all $x \in L$. [Consider the cover of $L$ by open stars of simplices and the cover of $K$ by the preimages of these open stars.]
```
WHY: The card dropped the whole printed bracketed hint telling the solver to use the open-star covers of $L$ and their preimages in $K$.

---

CARD: corpus/collections/SRC-TEXT-HAT02/4-l/E-HAT-4.L-3.md
BOOK: AT.txt:25807-25810  "3. Since there is a fiber bundle S 2 →CP5 →HP2 by Exercise 35 in §4.2, one might ask whether there is an analogous bundle S 4 →HP5 →OP2 . Use Steenrod powers for the prime 3 to show that such a bundle cannot exist. [The Gysin sequence can be used to determine the map on cohomology induced by the bundle projection HP5 →OP2 .]"
OLD:
```
Use Steenrod powers for the prime 3 to show that such a bundle cannot exist.
```
NEW:
```
Use Steenrod powers for the prime 3 to show that such a bundle cannot exist. [The Gysin sequence can be used to determine the map on cohomology induced by the bundle projection $\quatprojective^5 \to \OP^2$.]
```
WHY: The card dropped the printed bracketed hint pointing to the Gysin sequence as the way to compute the map induced by the bundle projection.

---

CARD: corpus/collections/SRC-TEXT-HAT02/4-l/E-HAT-4.L-4.md
BOOK: AT.txt:25811-25813  "4. Show there is no fiber bundle S 7 →S 23 →OP2 . [Compute the cohomology ring of the mapping cone of the projection S 23 →OP2 via Poincaré duality or the Thom isomorphism.]"
OLD:
```
Show there is no fiber bundle $S^7 \to S^{23} \to \OP^2$.
```
NEW:
```
Show there is no fiber bundle $S^7 \to S^{23} \to \OP^2$. [Compute the cohomology ring of the mapping cone of the projection $S^{23} \to \OP^2$ via Poincaré duality or the Thom isomorphism.]
```
WHY: The card dropped the printed bracketed hint naming the two methods (Poincaré duality or the Thom isomorphism) for computing the cohomology ring of the mapping cone.

---

## No change

Each card below was compared word by word against the printed item; only typographic
rendering differs (LaTeX vs. AT.txt's Unicode/line-broken form), no printed content is lost.

- `4-k/E-HAT-4.K-1.md` vs AT.txt:24095-24096 — matches.
- `4-k/E-HAT-4.K-3.md` vs AT.txt:24102 — matches.
- `4-k/E-HAT-4.K-4.md` vs AT.txt:24104-24105 — matches.
- `4-k/E-HAT-4.K-5.md` vs AT.txt:24109-24118 — matches, including the (i)/(ii)/(iii) clauses, the exactness sequence in (i), and the closing sentence on Lemma 4K.3 ("non-path-connected" in the card is the hyphenated form of AT.txt's "non-pathconnected").
- `4-k/E-HAT-4.K-6.md` vs AT.txt:24119-24121 — matches.
- `4-l/E-HAT-4.L-1.md` vs AT.txt:25803-25804 — matches.
- `4-l/E-HAT-4.L-2.md` vs AT.txt:25805-25806 — matches.
- `4-l/E-HAT-4.L-5.md` vs AT.txt:25817-25820 — matches; the card also keeps the printed reference to "the following diagram", see the note below.

Checks that came out empty in this slice (stated so that no one redoes them):
- *Asterisks.* The §4.K exercise block contains exactly one `∗` character, the subscript in
  `p∗` on line 24111; the §4.L exercise block contains none, and AT.txt has no ASCII `*`
  anywhere. No starred exercise or starred sub-part is printed in either slice, so there is
  no asterisk to restore.
- *Halved "iff".* Neither exercise block prints "if and only if" or "iff"; the only
  conditionals are 4.K ex.2 "is a homotopy equivalence if", 4.K ex.5 "if the following
  equivalent conditions are satisfied", 4.K ex.6 "is a quasifibration if", and the cards
  keep each of them with the same "if".

One thing that is printed but not restorable from AT.txt: 4.L ex.5 (card
`4-l/E-HAT-4.L-5.md`) ends "…encoded in the following diagram, where diagonal lines
indicate left-multiplication by Sq1 and horizontal lines indicate left-multiplication by
Sq2 ." — "the following diagram" is a figure, and the card reproduces the sentence but no
figure. AT.txt carries no image, so any NEW here would have to invent the diagram's layout;
I therefore left 4.L-5 as a no-change rather than fabricate one. Flagging it for whoever
owns figures/assets.

## Coverage

Compared all 11 cards of the slice against the printed text: `4-k` E-HAT-4.K-1 … 6 against
AT.txt:24094-24121 and `4-l` E-HAT-4.L-1 … 5 against AT.txt:25802-25820. I did not compare
any card outside these two directories, and I touched no file under `corpus/`. Defects found
and specified above: 3 (E-HAT-4.K-2, E-HAT-4.L-3, E-HAT-4.L-4), all of them dropped printed
bracketed hints; 8 cards need no change.
