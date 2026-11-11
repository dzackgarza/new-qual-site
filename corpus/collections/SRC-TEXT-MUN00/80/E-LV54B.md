---
schema: qual/card@1
id: E-LV54B
kind: problem
title: Composites of covering maps over a base with a universal covering
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 80 Exercise 1, printed p. 487. The composite of two coverings is a covering when the base has a universal cover: the card proves the evenness of p over a neighbourhood whose inclusion is trivial on pi_1, using the universal cover of Z, and gives the Hawaiian earring example for the failure without that hypothesis. Checked against Theorem 80.3 and the definition of a covering map. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repairs. Citations added at every step: Definition of a covering map (printed p. 336), Lemma 79.1 (printed p. 478) for the lifting criterion and uniqueness of lifts, Theorem 53.2 (printed p. 338) and Lemma 80.1 (printed p. 484) for restrictions of a covering to a path component, Lemma 80.4 (printed p. 486) for the neighbourhood on which the inclusion kills pi_1, the injectivity of p_* (printed p. 477), Theorem 23.5 (printed p. 150) that the image of a connected space is connected, Theorem 24.1 (printed p. 153), and the Convention of Chapter 13 (printed p. 477). Corrected: the proof of the internal lemma said "U is path connected and locally path connected" without saying where local path connectedness of U comes from, which is the Convention plus the openness of U; the step "s_e(U) is the path component" now separates the two halves it needs, namely that every path in c^{-1}(U)$ starting at e lies in s_e(U) (uniqueness of path liftings) and that c restricted to it is a homeomorphism; and part (b) now says that the surgery is performed for every integer k >= 1, so that the double cover over C_{k+1} joins the two sheets, which was only implicit. What the certificate does not cover: the exercise is starred, and part (b) is an example whose correct working is checked claim by claim rather than by a picture in the book.
---

::: {.exercise}

Let $q: X \to Y$ and $r: Y \to Z$ be maps; let $p = r \circ q$.

(a) Let $q$ and $r$ be covering maps.
Show that if $Z$ has a universal covering space, then $p$ is a covering map.
Compare [[E-PBG3W]].

(b) Give an example where $q$ and $r$ are covering maps but $p$ is not.

:::

::: {.solution}

By the Convention of Chapter 13 (printed p. 477) all covering maps of this chapter have path connected and locally path connected total space and base, and $c_*$ is injective for a covering map $c$ (printed p. 477). Let $\rho: \widetilde Z \to Z$ be a universal covering of $Z$, that is, $\widetilde Z$ is simply connected.

::: pf

::: {.pf-step #lemma}

Let $c: E \to B$ be a covering map and let $U \subseteq B$ be a path-connected open set such that the inclusion induces the trivial map $\pi_1(U, u) \to \pi_1(B, u)$. Then $U$ is evenly covered by $c$, and the slices are the path components of $c^{-1}(U)$.

::: pf-proof

::: pf-step

For each $e \in c^{-1}(U)$ there is a lift $s_e: U \to E$ of the inclusion with $s_e(c(e)) = e$.

::: pf-proof

$U$ is open in the locally path connected space $B$, hence locally path connected. It is path connected by hypothesis, and the image of $\pi_1(U,u)$ in $\pi_1(B,u)$ is trivial, so it lies in $c_*\pi_1(E,e)$. The lifting criterion of Lemma 79.1 (printed p. 478) gives the lift.

:::

:::

::: pf-step

$s_e(U)$ is the path component of $c^{-1}(U)$ that contains $e$, and $c$ maps it homeomorphically onto $U$.

::: pf-proof

$s_e(U)$ is the continuous image of the path connected space $U$, hence path connected: the composite of a path in $U$ with $s_e$ is a path in $E$. A path $\gamma$ in $c^{-1}(U)$ from $e$ is a lift of $c \circ \gamma$ starting at $e$, and so is $s_e \circ c \circ \gamma$; the two agree by the uniqueness of path liftings (Lemma 54.1, printed p. 342). Hence every such path stays in $s_e(U)$, and $s_e(U)$ is the path component of $e$ in $c^{-1}(U)$. Because $c \circ s_e = \id_U$, the restriction $c|_{s_e(U)}$ is a continuous bijection onto $U$ with continuous inverse $s_e$, so it is a homeomorphism.

:::

:::

::: pf-step

$c^{-1}(U)$ is the disjoint union of these path components, and each of them is open.

::: pf-proof

$c^{-1}(U)$ is open in $E$, and $E$ is locally path connected by the Convention, so the path components of the open subspace $c^{-1}(U)$ are open in $c^{-1}(U)$. They are disjoint and cover it by definition. The slices of the definition of a covering map (printed p. 336) are exactly these sets, so $U$ is evenly covered by $c$.

:::

:::

:::

:::

::: {.pf-step #part-a}

(a) $p$ is a covering map.

::: pf-proof

::: pf-step

Each $z \in Z$ has a path-connected open neighborhood $U$ such that $\pi_1(U, z) \to \pi_1(Z, z)$ is trivial.

::: pf-proof

By Lemma 80.4 (printed p. 486) applied to the simply connected covering $\rho$, the point $z$ has a neighborhood $U_0$ such that $\pi_1(U_0,z) \to \pi_1(Z,z)$ is trivial; a section of $\rho$ over $U_0$ exists, and the inclusion of $U_0$ factors through the simply connected space $\widetilde Z$. Replacing $U_0$ by a path-connected neighborhood $U \subseteq U_0$ of $z$, which exists because $Z$ is locally path connected, keeps the induced map trivial, since it factors through the trivial map of $\pi_1(U_0,z)$.

:::

:::

::: pf-step

$r^{-1}(U)$ is a disjoint union of open sets $V_\alpha$, each mapped homeomorphically onto $U$ by $r$, and each $V_\alpha \to Y$ induces the trivial map on $\pi_1$.

::: pf-proof

The first part is step [](#lemma){.pf-ref} applied to $c = r$; in particular each $V_\alpha$ is path connected. The composite $\pi_1(V_\alpha) \to \pi_1(Y) \xrightarrow{r_*} \pi_1(Z)$ equals $\pi_1(V_\alpha) \cong \pi_1(U) \to \pi_1(Z)$, which is trivial, and $r_*$ is injective, so $\pi_1(V_\alpha) \to \pi_1(Y)$ is trivial.

:::

:::

::: pf-step

$p^{-1}(U)$ is a disjoint union of open sets, each mapped homeomorphically onto $U$ by $p$, and $p$ is surjective.

::: pf-proof

By step [](#lemma){.pf-ref} applied to $c = q$ and to the path-connected open set $V_\alpha$, each $q^{-1}(V_\alpha)$ is a disjoint union of open sets $W_{\alpha\beta}$ mapped homeomorphically onto $V_\alpha$. Then $p^{-1}(U) = q^{-1}(r^{-1}(U)) = \bigsqcup_{\alpha,\beta} W_{\alpha\beta}$, and $p|_{W_{\alpha\beta}} = r|_{V_\alpha} \circ q|_{W_{\alpha\beta}}$ is a homeomorphism onto $U$. Also $p$ is surjective, being a composite of surjective maps, which is required of a covering map by the definition (printed p. 336).

:::

:::

:::

:::

::: pf-step

(b) Let $H = \bigcup_{n \ge 1} C_n \subseteq \RR^2$ be the Hawaiian earring, where $C_n$ is the circle of radius $1/n$ through the origin $0$. There are coverings $q: X \to Y$ and $r: Y \to H$ such that $p = r \circ q$ is not a covering map.

::: pf-proof

::: pf-step

Let $Y$ be the real line $\RR$ with, at each integer $k$, a copy $H_k$ of $\bigcup_{n \ge 2} C_n$ attached at its point $0$. Let $r: Y \to H$ wrap $\RR$ around $C_1$ by $t \mapsto e^{2\pi i t}$ (shifted so that integers go to $0$) and map each $H_k$ identically onto $\bigcup_{n \ge 2} C_n$. Then $r$ is a covering map.

::: pf-proof

Away from $0$ the map is a local homeomorphism with evenly covered neighborhoods coming from $\RR \to C_1$ or from the identity. Let $D$ be an open disk at $0$ of radius less than $1$ and let $U = H \cap D$; it meets $C_1$ in an open arc. Its preimage is the disjoint union over $k$ of the corresponding neighborhoods of $k$, each mapped homeomorphically onto $U$.

:::

:::

::: pf-step

Let $X$ be obtained from two copies $Y \times \{0, 1\}$ of $Y$ as follows: for each integer $k \ge 1$, delete the two copies of the circle $C_{k+1} \subseteq H_k$ and attach one circle that double covers $C_{k+1}$, with its two points over $0$ attached at $(k, 0)$ and $(k, 1)$. Let $q: X \to Y$ be the evident map. Then $q$ is a covering map and $X$ is path connected.

::: pf-proof

Each point of $Y$ other than the integers $k \ge 1$ has a neighborhood whose preimage is two copies of it. At $k \ge 1$, take the neighborhood of $k$ in $Y$ that is a small interval of $\RR$, small arcs of $C_2, \dots, C_{k+1}$ at $0$ in $H_k$, and every $C_n \subseteq H_k$ inside a disk too small to contain $C_{k+1}$. Its preimage is two copies, one at $(k, 0)$ and one at $(k, 1)$, because the double cover of $C_{k+1}$ restricted to a small arc at $0$ is two arcs. The circle over $C_2 \subseteq H_1$ joins the two copies of $Y$, so $X$ is path connected.

:::

:::

::: pf-step

$p = r \circ q$ is not a covering map.

::: pf-proof

Let $U$ be any neighborhood of $0$ in $H$. It contains $C_n$ for all $n \ge N$, for some $N$. Take $k = N$. The point $(k, 0) \in X$ lies over $0$. If $U$ were evenly covered, the slice through $(k, 0)$ would map homeomorphically onto $U \supseteq C_{k+1}$, and the inverse would lift the loop $C_{k+1}$ at $0$ to a loop at $(k, 0)$. The only lift of $C_{k+1}$ starting at $(k, 0)$ ends at $(k, 1)$, since $q$ over that circle is the double covering, so it is not a loop.

:::

:::

:::

:::

:::

:::
