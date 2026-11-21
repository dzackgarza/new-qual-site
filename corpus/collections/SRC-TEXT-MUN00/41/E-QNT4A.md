---
schema: qual/card@1
id: E-QNT4A
kind: problem
title: Perfect maps and paracompactness
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Feryll", *Praying For Stockholm*,
    "Paracompactness and Perfect Maps (6.41.8)" (31 December 2014),
    http://feryll.blogspot.com/2014/12/paracompactness-and-perfect-maps-6418.html, read 2026-11-10; cited
    by URL and date read, attributed to the handle the post carries. Checked against Munkres, Topology
    (2000), Section 41 Exercise 8, printed pp. 260-261, with Exercise 7 of §31 (perfect map), Lemma 41.3,
    Theorem 41.1 and Theorem 26.4. Part (a) is the post's: a finite subcover of each compact fibre, the
    open saturated set V_y = Y - p(X - O_y), a locally finite open refinement of {V_y}, and the family
    p^{-1}(W) cap U. What was corrected: for part (b) the post takes a locally finite open refinement A of
    the pulled-back cover and sets C = {p(A)}, which is not open because a perfect map is closed and not
    open; the card takes the closed refinement that the book's hint uses, notes that p(F) is closed and
    that {p(F)} covers Y, and proves p(F) locally finite at y by covering the compact fibre with finitely
    many neighbourhoods and passing to the saturated neighbourhood N = Y - p(X - O). The card also
    records the Hausdorffness of Y, which the post leaves unstated and which the statement "so is Y"
    requires.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    nine steps, each carrying a `pf-proof`, and answers Munkres, Topology, §41 Exercise 8. Cited by
    number only: Theorem 41.1 (a paracompact Hausdorff space is normal), Theorem 33.2 (normality
    separates closed sets), Lemma 41.3 (condition (3), a locally finite closed covering refinement)
    and §31 Exercise 7(b) (a perfect map carries regularity). The transcription is from Feryll,
    Praying For Stockholm, "Paracompactness and Perfect Maps (6.41.8)", named by its numbered
    exercise. Checked: that the sets V_y satisfy p^{-1}(V_y) inside O_y, that the family R refines U
    and covers X, that local finiteness of W passes to R, that the fibres of two distinct points are
    closed and disjoint, and that the neighbourhood N = Y - p(X - O) meets only the members of F that
    O meets.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read, with two citation repairs. The solution named the retained file
    `tmp/sources/feryll-2015-munkres-58-9-10.md` as the text of Feryll's "Paracompactness and
    Perfect Maps (6.41.8)"; that file is his post on §58 Exercises 9--10, on degrees of maps
    $S^n\to S^n$, and contains nothing on perfect maps. The post was fetched at the URL now in
    the solution and read: it states the exercise as "if $X$ is Hausdorff, $X$ is paracompact if
    and only if $Y$ is", proves the forward direction with the families $p^{-1}(A)\cap B$ over a
    locally finite refinement of $\{p(V_y)\}$, and the reverse with a locally finite refinement of
    the pullback cover and its images under $p$; it does not prove $Y$ Hausdorff. Part (a) of the
    card is that argument; part (b) is the card's own, and the solution now says so. The step
    separating two fibres cited "Theorem 33.2", which is the heredity and productivity of complete
    regularity; the separation is the definition of normality (§32), and the step now cites that.
    Everything else was checked and stands: the lemma on $W=Y-p(X-U)$, the cover and local
    finiteness of part (a), and in part (b) the closed refinement of Lemma 41.3 (3), the
    closedness and refinement of the images $p(F)$, and their local finiteness through the compact
    fibre. Citation by number: §41 Exercise 8, §31 Exercise 7, Lemma 41.3 and Theorem 41.1.

---

::: {.exercise}

Let $p: X \to Y$ be a perfect map.
(See Exercise 7 of §31.)

(a) Show that if $Y$ is paracompact, so is $X$.
[Hint: If $\mathcal{A}$ is an open covering of $X$, find a locally finite open covering of $Y$ by sets $B$ such that $p^{-1}(B)$ can be covered by finitely many elements of $\mathcal{A}$; then intersect $p^{-1}(B)$ with these elements of $\mathcal{A}$.]

(b) Show that if $X$ is a paracompact Hausdorff space, then so is $Y$.
[Hint: If $\mathcal{B}$ is a locally finite closed covering of $X$, then $\theset{p(B) \mid B \in \mathcal{B}}$ is a locally finite closed covering of $Y$.]
:::

::: {.solution}

Part (a) is the argument of Feryll, *Praying For Stockholm*, "Paracompactness and Perfect Maps (6.41.8)" (31 December 2014), http://feryll.blogspot.com/2014/12/paracompactness-and-perfect-maps-6418.html, read 2026-11-20; that post states the exercise in the combined form "if $X$ is Hausdorff, $X$ is paracompact if and only if $Y$ is" and does not ask for $Y$ to be Hausdorff; its own part (a) works with $p(V_y)$, which need not be open, and the card uses instead the open $V_y=Y-p(X-O_y)$ supplied by the lemma of step [](#lemma){.pf-ref}. Part (b) here is the card's own: the closed refinement $\mathcal F$ of the pullback cover, the closed images $p(F)$, their local finiteness through the compact fibre, and the separate proofs that $Y$ is Hausdorff and regular.

::: pf

::: {.pf-step #lemma}
If $U\subseteq X$ is open and $p^{-1}(y)\subseteq U$, then $W=Y-p(X-U)$ is an open neighbourhood of $y$ with $p^{-1}(W)\subseteq U$.

::: pf-proof
$p$ is closed, so $p(X-U)$ is closed in $Y$ and $W$ is open. The fibre meets $X-U$ in no point, so $y\notin p(X-U)$ and $y\in W$. Finally $p^{-1}(W)=X-p^{-1}(p(X-U))\subseteq X-(X-U)=U$, since $X-U\subseteq p^{-1}(p(X-U))$.
:::

:::

::: {.pf-step #part-a-cover}
(a) Let $\mathcal U$ be an open cover of $X$. For each $y\in Y$ there are finitely many members $U_{y,1},\dots,U_{y,r(y)}$ of $\mathcal U$ covering the fibre $p^{-1}(y)$; with $O_y=\bigcup_jU_{y,j}$ the sets $V_y=Y-p(X-O_y)$ are open, contain $y$, satisfy $p^{-1}(V_y)\subseteq O_y$, and cover $Y$.

::: pf-proof
$p^{-1}(y)$ is compact and the members of $\mathcal U$ cover it, so finitely many suffice for $O_y$. Step [](#lemma){.pf-ref} gives the three properties of $V_y$, and $y\in V_y$ for every $y$ gives the cover.
:::

:::

::: {.pf-step #part-a-refinement}
There is a locally finite open cover $\mathcal W$ of $Y$ refining $\{V_y:y\in Y\}$.

::: pf-proof
$\{V_y\}$ is an open cover of the paracompact space $Y$, so it has a locally finite open refinement covering $Y$; this is condition (4) of Munkres, Lemma 41.3, or the definition of paracompactness.
:::

:::

::: {.pf-step #part-a-local}
For $W\in\mathcal W$ choose $y(W)$ with $W\subseteq V_{y(W)}$ and put
$$
\mathcal R=\{p^{-1}(W)\cap U_{y(W),j}:W\in\mathcal W,\ 1\le j\le r(y(W))\}.
$$
Then $\mathcal R$ is an open refinement of $\mathcal U$ that covers $X$ and is locally finite.

::: pf-proof
Each member is open, being the intersection of the open set $p^{-1}(W)$ with a member of $\mathcal U$, and it lies in that member, so $\mathcal R$ refines $\mathcal U$. It covers $X$: a point $x$ lies in $p^{-1}(W)$ for some $W$, because $\mathcal W$ covers $Y$, and then $x\in p^{-1}(W)\subseteq p^{-1}(V_{y(W)})\subseteq O_{y(W)}$, so $x$ lies in some $U_{y(W),j}$. For local finiteness let $x\in X$; since $\mathcal W$ is locally finite at $p(x)$ there is an open neighbourhood $N$ of $p(x)$ meeting only finitely many members $W$, and then $p^{-1}(N)$ is an open neighbourhood of $x$ meeting only the finitely many families $\{p^{-1}(W)\cap U_{y(W),j}\}_j$ belonging to those $W$.
:::

:::

::: {.pf-step #part-a-done}
(a) If $Y$ is paracompact, then $X$ is paracompact.

::: pf-proof
Given an open cover $\mathcal U$ of $X$, step [](#part-a-local){.pf-ref} produces a locally finite open refinement covering $X$. So every open cover has such a refinement, which is paracompactness.
:::

:::

::: {.pf-step #part-b-hausdorff}
(b) If $X$ is paracompact Hausdorff, then $Y$ is Hausdorff.

::: pf-proof
$X$ is normal by Munkres, Theorem 41.1. Let $y_1\ne y_2$ and put $F_i=p^{-1}(y_i)$; the fibres are compact, hence closed in the Hausdorff space $X$, and disjoint, so normality gives disjoint open sets $O_1\supseteq F_1$ and $O_2\supseteq F_2$ (the definition of normality, §32). Step [](#lemma){.pf-ref} gives open $W_i\ni y_i$ with $p^{-1}(W_i)\subseteq O_i$, and $W_1\cap W_2=\varnothing$ because a point of the intersection would have a nonempty fibre inside $O_1\cap O_2$.
:::

:::

::: {.pf-step #part-b-regular}
(b) If $X$ is paracompact Hausdorff, then $Y$ is regular.

::: pf-proof
A perfect map carries regularity from $X$ to $Y$: this is Munkres, §31 Exercise 7(b), proved on [[E-Y4MFU]]. $X$ is regular because it is paracompact Hausdorff and hence normal (Theorem 41.1), and with step [](#part-b-hausdorff){.pf-ref} the space $Y$ is regular.
:::

:::

::: {.pf-step #part-b-images}
(b) Let $\mathcal U$ be an open cover of $Y$. The pullback cover $\{p^{-1}(U):U\in\mathcal U\}$ of $X$ has a locally finite closed refinement $\mathcal F$ covering $X$, and $\{p(F):F\in\mathcal F\}$ is a locally finite closed cover of $Y$ refining $\mathcal U$.

::: pf-proof
$X$ is paracompact and regular, so condition (3) of Munkres, Lemma 41.3 applied to the pullback cover gives $\mathcal F$. For $F\in\mathcal F$ choose $U(F)\in\mathcal U$ with $F\subseteq p^{-1}(U(F))$; then $p(F)$ is closed because $p$ is closed, and $p(F)\subseteq U(F)$, so the images refine $\mathcal U$ and are closed. They cover $Y$ because $\mathcal F$ covers $X$ and $p$ is surjective. For local finiteness let $y\in Y$. The compact fibre $p^{-1}(y)$ is covered by finitely many open sets each meeting only finitely many members of $\mathcal F$, and their union $O$ therefore meets only finitely many members; then $N=Y-p(X-O)$ is an open neighbourhood of $y$ with $p^{-1}(N)\subseteq O$. If $N\cap p(F)\ne\varnothing$, choose $z\in N\cap p(F)$ and $x\in F$ with $p(x)=z$; then $x\in p^{-1}(N)\subseteq O$, so $F$ is one of the finitely many members meeting $O$. Hence $\{p(F)\}$ is locally finite at $y$.
:::

:::

::: {.pf-step #part-b-done}
(b) If $X$ is paracompact Hausdorff, then $Y$ is paracompact.

::: pf-proof
Let $\mathcal U$ be an open cover of $Y$. Step [](#part-b-images){.pf-ref} produces a locally finite closed cover of $Y$ refining $\mathcal U$, so condition (3) of Munkres, Lemma 41.3 holds for $Y$, which is regular by step [](#part-b-regular){.pf-ref}. Hence $Y$ is paracompact.
:::

:::

:::

:::
