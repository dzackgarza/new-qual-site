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
---

::: {.exercise}

Let $q: X \to Y$ and $r: Y \to Z$ be maps; let $p = r \circ q$.

(a) Let $q$ and $r$ be covering maps.
Show that if $Z$ has a universal covering space, then $p$ is a covering map.
Compare [[E-PBG3W]].

(b) Give an example where $q$ and $r$ are covering maps but $p$ is not.
:::

::: {.solution}
As in Munkres §80, all spaces are path connected and locally path connected. Let $\rho: \tilde Z \to Z$ be a universal covering.

::: pf

::: {.pf-step #lemma}
Let $c: E \to B$ be a covering map and let $U \subseteq B$ be a path-connected open set such that the inclusion induces the trivial map $\pi_1(U, u) \to \pi_1(B, u)$. Then $U$ is evenly covered by $c$, and the slices are the path components of $c^{-1}(U)$.

::: pf-proof

::: pf-step
For each $e \in c^{-1}(U)$ there is a lift $s_e: U \to E$ of the inclusion with $s_e(c(e)) = e$.

::: pf-proof
$U$ is path connected and locally path connected, and the image of $\pi_1(U)$ in $\pi_1(B)$ is trivial, so it lies in $c_*\pi_1(E, e)$. Apply the lifting criterion.
:::

:::

::: pf-step
$s_e(U)$ is the path component of $c^{-1}(U)$ that contains $e$, and $c$ maps it homeomorphically onto $U$.

::: pf-proof
$s_e(U)$ is path connected. A path $\gamma$ in $c^{-1}(U)$ from $e$ is the unique lift of $c \circ \gamma$ starting at $e$, and so is $s_e \circ c \circ \gamma$; so $\gamma$ lies in $s_e(U)$. Thus $s_e(U)$ is the path component. Because $c \circ s_e = \id_U$, the map $c\restrict_{s_e(U)}$ is a continuous bijection onto $U$ with continuous inverse $s_e$.
:::

:::

::: pf-step
$c^{-1}(U)$ is the disjoint union of these path components, and each is open.

::: pf-proof
$c^{-1}(U)$ is open in $E$, and $E$ is locally path connected, so the path components of $c^{-1}(U)$ are open.
:::

:::

:::

:::

::: {.pf-step #part-a}
(a) $p$ is a covering map.

::: pf-proof

::: pf-step
Each $z \in Z$ has a path-connected open neighborhood $U$ such that $\pi_1(U) \to \pi_1(Z)$ is trivial.

::: pf-proof
Take $U$ to be the path component containing $z$ of a neighborhood evenly covered by $\rho$. A section $U \to \tilde Z$ of $\rho$ exists, so the inclusion $U \to Z$ factors through the simply connected space $\tilde Z$.
:::

:::

::: pf-step
$r^{-1}(U)$ is a disjoint union of open sets $V_\alpha$, each mapped homeomorphically onto $U$ by $r$, and each $V_\alpha \to Y$ induces the trivial map on $\pi_1$.

::: pf-proof
The first part is step [](#lemma){.pf-ref} for $c = r$. The composite $\pi_1(V_\alpha) \to \pi_1(Y) \xrightarrow{r_*} \pi_1(Z)$ equals $\pi_1(V_\alpha) \cong \pi_1(U) \to \pi_1(Z)$, which is trivial, and $r_*$ is injective.
:::

:::

::: pf-step
$p^{-1}(U)$ is a disjoint union of open sets, each mapped homeomorphically onto $U$ by $p$.

::: pf-proof
By step [](#lemma){.pf-ref} for $c = q$, each $q^{-1}(V_\alpha)$ is a disjoint union of open sets $W_{\alpha\beta}$ mapped homeomorphically onto $V_\alpha$. Then $p^{-1}(U) = \bigsqcup_{\alpha,\beta} W_{\alpha\beta}$, and $p\restrict_{W_{\alpha\beta}} = r\restrict_{V_\alpha} \circ q\restrict_{W_{\alpha\beta}}$ is a homeomorphism onto $U$. Also $p$ is surjective because $q$ and $r$ are.
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
Let $X$ be obtained from two copies $Y \times \{0, 1\}$ of $Y$ as follows: for each $k \ge 1$, delete the two copies of the circle $C_{k+1} \subseteq H_k$ and attach one circle that double covers $C_{k+1}$, with its two points over $0$ attached at $(k, 0)$ and $(k, 1)$. Let $q: X \to Y$ be the evident map. Then $q$ is a covering map and $X$ is path connected.

::: pf-proof
Each point of $Y$ other than the integers $k \ge 1$ has a neighborhood whose preimage is two copies of it. At $k \ge 1$, take the neighborhood of $k$ in $Y$ that is a small interval of $\RR$, small arcs of $C_2, \dots, C_{k+1}$ at $0$ in $H_k$, and every $C_n \subseteq H_k$ inside a disk too small to contain $C_{k+1}$. Its preimage is two copies, one at $(k, 0)$ and one at $(k, 1)$, because the double cover of $C_{k+1}$ restricted to a small arc at $0$ is two arcs. The circle over $C_2 \subseteq H_1$ joins the two copies of $Y$.
:::

:::

::: pf-step
$p = r \circ q$ is not a covering map.

::: pf-proof
Let $U$ be any neighborhood of $0$ in $H$. It contains $C_n$ for all $n \ge N$, for some $N$. Take $k = N$. The point $(k, 0) \in X$ lies over $0$. If $U$ were evenly covered, the slice through $(k, 0)$ would map homeomorphically onto $U \supseteq C_{k+1}$, and the inverse would lift the loop $C_{k+1}$ at $0$ to a loop at $(k, 0)$. The only lift of $C_{k+1}$ starting at $(k, 0)$ ends at $(k, 1)$, so it is not a loop.
:::

:::

:::

:::

:::

:::
