---
schema: qual/card@1
id: E-HAT-4.1-21
kind: problem
title: "Postnikov towers and covering spaces commute"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 21; the stored statement matches.
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
    Read against the book (AT.txt:17900-17906 for the statement). Two things were asserted and are now
    stated. First, the notation X_m itself carries a hypothesis the card did not record: an
    (m-1)-connected covering exists only when pi_i(X) = 0 for 2 <= i <= m-1, because a covering has
    pi_i(X_m) isomorphic to pi_i(X) for i >= 2; the card now says so and notes that for m = 2 it is
    vacuous and X_2 is the universal cover, while for X = S^2 and m = 3 the symbol denotes nothing. This
    corrects the earlier audit note on this card, which gave the range as 2 <= i <= m-2; the correct
    upper end is m-1, since (m-1)-connectedness of X_m makes pi_{m-1}(X_m) vanish, and that group is
    pi_{m-1}(X). Second, the final "(X^n)_m is an nth Postnikov stage of X_m, hence (X^n)_m ~ (X_m)^n"
    used uniqueness of Postnikov stages without saying so; the card now names it and cites Hatcher
    Section 4.3, together with the reason the hypothesis applies (both spaces are built from CW complexes
    by homotopy fibres and by attaching killing cells). The homotopy-group bookkeeping and the degenerate
    cases n < m-1 and n = m-1 were checked and are unchanged. Not checked: no re-reading of Hatcher's
    §4.3 beyond the statement of uniqueness.

---

::: {.problem}
For this problem it is convenient to use the notations $X^n$ for the $n$th stage in a Postnikov tower for $X$ and $X_m$ for an $(m-1)$-connected covering of $X$, where $X$ is a connected CW complex.
Show that $(X^n)_m \simeq (X_m)^n$, so the notation $X_m^n$ is unambiguous.
Thus $\pi_i(X_m^n) \approx \pi_i(X)$ for $m \leq i \leq n$ and all other homotopy groups of $X_m^n$ are zero.
:::

::: {.solution}
Let $X^n$ be the $n$-th Postnikov stage of $X$, and $X_m$ an $(m-1)$-connected covering of $X$. The two constructions affect disjoint ranges of homotopy groups:

- passing to $X^n$ preserves $\pi_i$ for $i\le n$ and kills $\pi_i$ for $i>n$;
- passing to $X_m$ kills $\pi_i$ for $i<m$ and preserves $\pi_i$ for $i\ge m$.

Therefore both iterated constructions $(X^n)_m$ and $(X_m)^n$ have homotopy groups
$$
\pi_i\cong
\begin{cases}
\pi_i(X),&m\le i\le n,\\
0,&i<m\text{ or }i>n.
\end{cases}
$$
To compare the spaces, use the homotopy-fiber models
$$
X_m\simeq\operatorname{hofib}(X\to X^{m-1}),
\qquad
(X^n)_m\simeq\operatorname{hofib}(X^n\to X^{m-1})
$$
when $n\ge m-1$. These displays carry a hypothesis that the problem's notation carries as well: an $(m-1)$-connected covering $X_m$ exists only if $\pi_i(X)=0$ for $2\le i\le m-1$, since a covering has $\pi_i(X_m)\cong\pi_i(X)$ for $i\ge2$. For $m=2$ the condition is vacuous and $X_2$ is the universal cover; when it fails, for instance for $X=S^2$ and $m=3$, the symbol $X_m$ denotes nothing. Under it, $X_m$ is the cover whose classifying subgroup makes it $(m-1)$-connected, the projection $X_m\to X$ is a fibration with fibre the homotopy fibre, and the fibre is $(m-1)$-connected with the same homotopy groups as $X_m$, so Whitehead's theorem gives the displayed equivalence. The map $X\to X^n$ induces a map between these fibers. Its long exact homotopy sequence shows that $X_m\to(X^n)_m$ is an isomorphism on $\pi_i$ for $i\le n$. The target has no homotopy above $n$, so this map exhibits $(X^n)_m$ as an $n$th Postnikov stage of $X_m$. Hence
$$
\boxed{(X^n)_m\simeq (X_m)^n.}
$$
The last step is uniqueness of Postnikov stages. An $n$th Postnikov stage of $X_m$ is a space under $X_m$ whose structure map is an isomorphism on $\pi_i$ for $i\le n$ and whose homotopy groups vanish above $n$; two such are homotopy equivalent under $X_m$, by Whitehead's theorem applied to the resulting map of towers (Hatcher, §4.3). Both $(X^n)_m$ and $(X_m)^n$ have this property, each being obtained from a CW complex by taking homotopy fibres and by attaching cells that kill homotopy groups, so they are homotopy equivalent.
If $n<m-1$, both iterated constructions are contractible; the case $n=m-1$ follows from the same fiber model. Thus the notation $X_m^n$ is unambiguous up to homotopy, and it has exactly the stated nonzero homotopy groups.
:::
