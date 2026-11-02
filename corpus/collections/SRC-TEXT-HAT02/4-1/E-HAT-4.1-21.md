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

- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    Corrects the immediately preceding event, which introduced a hypothesis the exercise does not have.
    That note claimed an (m-1)-connected covering X_m exists only when pi_i(X) = 0 for 2 <= i <= m-1,
    on the reasoning of an ordinary covering space, for which pi_i(X_m) is isomorphic to pi_i(X) for
    i >= 2. The reasoning is sound for a covering map but the premise is wrong: Hatcher's
    "(m-1)-connected covering" is the (m-1)-connected cover in the Whitehead tower (Example 4.20,
    AT.txt:17730-17747, where the map Z_n -> X is described as an "n connected cover" and the case n = 1
    is only the universal cover by analogy), realized as the homotopy fibre of X -> X^{m-1} (Section 4.3,
    AT.txt:20576-20579: "The n connected covering of Y can also be obtained as the homotopy fiber of the
    nth stage Y -> Y^n of a Postnikov tower for Y"). It therefore exists for every connected CW complex,
    it is generally not a covering map when m > 1 (the Hopf map S^3 -> S^2 is the 2 connected cover of
    S^2, the book's own example), and no vanishing hypothesis on pi_i(X) is needed. The card now says
    this, and deduces pi_i(X_m) = 0 for i <= m-1 and pi_i(X_m) = pi_i(X) for i >= m from the long exact
    sequence of that homotopy fibration, which is the property the rest of the proof uses. The exercise
    is not false and X_m is not undefined; the audit note this event replaces said otherwise and was
    wrong. The earlier audit report on this card carries the same error (it restricted existence to
    2 <= i <= m-2 and called X_m the universal cover for m >= 2); a correction is appended to that report.
    Not checked: nothing beyond the cited spans; no independent verification of the Whitehead-tower
    construction.

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
when $n\ge m-1$. The word "covering" in the exercise is Hatcher's name for the $(m-1)$-connected cover in the Whitehead tower, not an ordinary covering space: it is defined, for every connected CW complex $X$, as the homotopy fibre of $X\to X^{m-1}$ (Example 4.20, and §4.3 where the $n$ connected covering of $Y$ is identified with the homotopy fibre of $Y\to Y_n$). The long exact sequence of that homotopy fibration gives $\pi_i(X_m)=0$ for $i\le m-1$ and $\pi_i(X_m)\cong\pi_i(X)$ for $i\ge m$, because $X^{m-1}$ carries the homotopy groups of $X$ up to degree $m-1$ and none above; no vanishing hypothesis on $\pi_i(X)$ is needed. For $m=2$ the cover is the universal cover, and for $m>1$ it need not be a covering map at all: the Hopf map $S^3\to S^2$ is the 2 connected cover of $S^2$. That identification is what makes the two iterands comparable, and it is the same object on both sides, $\operatorname{hofib}(X^n\to X^{m-1})$. The map $X\to X^n$ induces a map between these fibers. Its long exact homotopy sequence shows that $X_m\to(X^n)_m$ is an isomorphism on $\pi_i$ for $i\le n$. The target has no homotopy above $n$, so this map exhibits $(X^n)_m$ as an $n$th Postnikov stage of $X_m$. Hence
$$
\boxed{(X^n)_m\simeq (X_m)^n.}
$$
The last step is uniqueness of Postnikov stages. An $n$th Postnikov stage of $X_m$ is a space under $X_m$ whose structure map is an isomorphism on $\pi_i$ for $i\le n$ and whose homotopy groups vanish above $n$; two such are homotopy equivalent under $X_m$, by Whitehead's theorem applied to the resulting map of towers (Hatcher, §4.3). Both $(X^n)_m$ and $(X_m)^n$ have this property, each being obtained from a CW complex by taking homotopy fibres and by attaching cells that kill homotopy groups, so they are homotopy equivalent.
If $n<m-1$, both iterated constructions are contractible; the case $n=m-1$ follows from the same fiber model. Thus the notation $X_m^n$ is unambiguous up to homotopy, and it has exactly the stated nonzero homotopy groups.
:::
