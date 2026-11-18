---
schema: qual/card@1
id: E-HAT-3.C-14
kind: problem
title: Coproduct from the diagonal map
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 14; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read. The chain is correct and short: naturality of the Kronecker pairing gives
    $\langle D_*z,\alpha\times\beta\rangle=\langle z,D^*(\alpha\times\beta)\rangle$, the definition of the cup product gives $D^*(\alpha\times\beta)=\alpha\smile\beta$, so $D_*$ is the transpose of the cup product. Repaired: the closing sentence now states the two conventions it silently used — that the transpose of the product lives in $H_*\otimes H_*$ only because of the assumed degreewise finiteness and freeness, and that the identification of the dual of a tensor product with the tensor product of duals carries the Koszul sign $(-1)^{|\alpha||\beta|}$, which is why no sign is visible in the displayed identity and where it would appear if the identity is expanded. No statement changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 3.C Exercise 14, printed p. 291, and the definition of the cup product as
    $D^*(alpha x beta)$ (Section 3.2, p. 206). Each step re-read: degreewise finite freeness makes
    homology and cohomology graded duals and licenses the Kunneth identifications; Kronecker
    naturality converts the pairing with $D_*z$ into a pairing with $D^*(alpha x beta)$; the cup
    product is by definition that pullback; and the resulting identity is precisely that $D_*$ is
    the dual of the multiplication. The two conventions written out in the last steps (finiteness
    for $(H^* x H^*)^* = H_* x H_*$, and the Koszul sign $(-1)^{\abs{\alpha}\abs{\beta}}$ in the graded
    identification) are kept as before: no statement is strengthened and the sign convention is
    not claimed to vanish.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Page correction to the note above, which cited the exercise one page off (or, for the Section 4
    cards, carried over the Section 4.1 page). The exercise is printed on p. 292 of Hatcher,
    Algebraic Topology (2002), checked against the retained PDF text at PDF p. 301, whose running
    folio reads 292. The solution section now states the corrected page; the mathematics is
    unchanged.
---

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Hatcher, Algebraic Topology, Section 3.C Exercise 14, printed p. 292, and against the definition of the cup product as the composite $H^*(X\times X)\to H^*(X)$ induced by the diagonal (Section 3.2, p. 206).

::: pf

::: {.pf-step #setup}
Let $D:X\to X\times X$ be the diagonal, $D(x)=(x,x)$. Assuming the cohomology of $X$ is degreewise finitely generated and free, homology and cohomology are graded duals and the Künneth formula identifies $D_*$ with a map
$$
D_*:H_*(X;R)\longrightarrow H_*(X;R)\otimes H_*(X;R).
$$

::: pf-proof
The two hypotheses make $H^n(X;R)$ finitely generated free in each degree, so $H^n(X;R)\cong(H_n(X;R))^*$ and the dual of a tensor product is the tensor product of the duals. The Künneth formula, whose hypothesis is the same degreewise freeness, identifies $H_*(X\times X;R)$ with $H_*(X;R)\otimes H_*(X;R)$.
:::

:::

::: {.pf-step #kronecker}
For $z\in H_*(X;R)$ and cohomology classes $\alpha,\beta$ of $X$,
$$
\bigl\langle D_*z,\alpha\times\beta\bigr\rangle=\bigl\langle z,D^*(\alpha\times\beta)\bigr\rangle .
$$

::: pf-proof
This is naturality of the Kronecker pairing: for a map $f$ and classes $u$, $v$ in the target, $\langle f_*u,v\rangle=\langle u,f^*v\rangle$. Apply it to $f=D$ and to the cross product $\alpha\times\beta$.
:::

:::

::: {.pf-step #cup}
$D^*(\alpha\times\beta)=\alpha\smile\beta$.

::: pf-proof
Hatcher defines the cup product by $\alpha\smile\beta=D^*(\alpha\times\beta)$, where the cross product is taken in $H^*(X\times X;R)$; the identification of the source with $H^*(X)\otimes H^*(X)$ is the Künneth isomorphism, which the hypotheses make available.
:::

:::

::: {.pf-step #transpose}
$D_*$ is the transpose of the cup-product multiplication.

::: pf-proof
By steps [](#kronecker){.pf-ref} and [](#cup){.pf-ref},
$$
\bigl\langle D_*z,\alpha\times\beta\bigr\rangle=\bigl\langle z,\alpha\smile\beta\bigr\rangle ,
$$
for all $z,\alpha,\beta$. The left-hand side is the pairing of $D_*z$ with the decomposable element $\alpha\times\beta$ of $H^*(X)\otimes H^*(X)$, which separates the decomposables; the right-hand side is the pairing of $z$ with the cup product of $\alpha$ and $\beta$. This is exactly the statement that $D_*$ is the linear dual of the multiplication $H^*(X)\otimes H^*(X)\to H^*(X)$ under the duality $\langle-,-\rangle$ between $H_*$ and $H^*$ and the identification $(H^*\otimes H^*)^*\cong H_*\otimes H_*$.
:::

:::

::: {.pf-step #conventions}
The two conventions in the last step are what make it an identification of the Hopf-algebra coproduct; in expanded form a Koszul sign appears.

::: pf-proof
First, $(H^*(X)\otimes H^*(X))^*\cong H_*(X)\otimes H_*(X)$ requires the degreewise finiteness and freeness assumed in step [](#setup){.pf-ref}; without it the dual of the tensor product is a product of duals, not a tensor product. Second, in the graded setting the identification carries the sign $(-1)^{\abs{\alpha}\abs{\beta}}$, so if $\Delta z=\sum_i z_i'\otimes z_i''$, the displayed identity reads
$$
\bigl\langle z,\alpha\smile\beta\bigr\rangle=\sum_i(-1)^{\abs{z_i'}\abs{\beta}}\bigl\langle z_i',\alpha\bigr\rangle\bigl\langle z_i'',\beta\bigr\rangle .
$$
The sign is invisible in the unexpanded display only because it sits inside the identification of the duals.
:::

:::

::: {.pf-step}
The coproduct of the Hopf algebra $H_*(X;R)$ dual to $H^*(X;R)$ is induced by the diagonal $D$.

::: pf-proof
By definition, the Hopf algebra dual to $H^*(X;R)$ is $H_*(X;R)$ with multiplication the transpose of the cup product and coproduct the transpose of the multiplication of $H^*(X;R)$. Step [](#transpose){.pf-ref} identifies the first of these transposes with $D_*$, and step [](#conventions){.pf-ref} records the graded bookkeeping. Hence the coproduct is the map induced by $D$, which is the assertion of the exercise.
:::

:::

:::
:::
