---
schema: qual/card@1
id: E-GZX7B
kind: problem
title: The printed conclusion of Exercise 41.10 fails; components are sigma-compact
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source claims that each component has a countable basis. An uncountable product of compact intervals is connected, compact, Hausdorff, and not first countable. The printed proof establishes a countable compact cover.'
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 10, printed p. 261, with the printed proof skeleton, Lemma 39.1, Theorem 41.1 and the order topology of $\overline S_\Omega$. What was corrected: the printed conclusion, that each component has a countable basis, is false, and the card records the counterexample (the disjoint union of two copies of $\overline S_\Omega$, locally compact Hausdorff and paracompact, whose components have no countable basis). An earlier audit note on this card had offered an uncountable product of compact intervals as the counterexample, which is not locally compact. The card proves the corrected statement, that each component is a countable union of compact subspaces, which is what the printed proof establishes.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    The counterexample on this card was wrong and the one it rejected was right. Two copies of
    $\overline S_\Omega$ do not refute the printed statement: $\overline S_\Omega$ is totally disconnected,
    since for $\alpha<\beta$ the set $[0,\alpha]=[0,\alpha+1)$ is a basis element of the order topology whose
    complement $(\alpha,\Omega]$ is another, so distinct points lie in different clopen sets and every
    component is a point, which has a countable basis. The counterexample is $[0,1]^J$ for uncountable $J$:
    it is compact (Theorem 37.3), Hausdorff (Theorem 19.4), hence locally compact (§29: a compact space is
    automatically locally compact) and paracompact (§41: every compact space is paracompact, as the
    section's opening remark states), connected because path connected --- the coordinatewise linear path is
    continuous by Theorem 19.6 and a path connected space is connected (§24) --- so it is its own component,
    and it has no countable basis: a compact Hausdorff space with a countable basis is regular (Theorem
    32.3) and metrizable by the Urysohn metrization theorem (Theorem 34.1), while the sequence lemma fails
    for $X$ exactly as in Example 2 of §21 (Lemma 21.2). A previous note on this card had rejected
    $[0,1]^J$ on the ground that it is not locally compact; that is withdrawn. The $\sigma$-compact part of
    the proof below is unchanged and is what the printed skeleton yields. Not checked here: nothing beyond
    the printed exercise's own proof outline is claimed.
---

::: {.exercise}

Theorem.
If $X$ is a Hausdorff space that is locally compact and paracompact, then each component of $X$ has a countable basis.

Proof.
If $X_0$ is a component of $X$, then $X_0$ is locally compact and paracompact.
Let $\mathcal{C}$ be a locally finite covering of $X_0$ by sets open in $X_0$ that have compact closures.
Let $U_1$ be a nonempty element of $\mathcal{C}$, and in general let $U_n$ be the union of all elements of $\mathcal{C}$ that intersect $\overline{U}_{n-1}$.
Show that $\overline{U}_n$ is compact, and the sets $U_n$ cover $X_0$.
:::

::: {.solution}
The printed conclusion is false. Let $J$ be an uncountable set and let $X=[0,1]^J$ carry the product topology. Then $X$ is compact by the Tychonoff theorem (Theorem 37.3) and Hausdorff, being a product of Hausdorff spaces (Theorem 19.4); hence $X$ is locally compact, since a compact space is automatically locally compact (§29, the remark following the definition), and paracompact, since a finite open covering is a locally finite one and a compact space is therefore paracompact (§41, the definition and the remark after it). $X$ is connected: for $x,y\in X$ the map $\gamma:[0,1]\to X$ whose $\alpha$-th coordinate is $(1-t)x_\alpha+ty_\alpha$ is a path from $x$ to $y$, since each of its coordinate functions is continuous and $X$ carries the product topology (Theorem 19.6), and a path connected space is connected (§24). So $X$ is a component of itself, and it has no countable basis: a compact Hausdorff space with a countable basis is regular (Theorem 32.3) and hence metrizable by the Urysohn metrization theorem (Theorem 34.1), while $X$ is not metrizable, because it fails the sequence lemma (Lemma 21.2) --- the set $A$ of points of $X$ that are $1$ in all but finitely many coordinates has $0$ in its closure, and a sequence in $A$ is $1$ in some coordinate outside the countable set of coordinates in which its terms differ from $1$, so it does not converge to $0$; this is the argument of Example 2 of §21.

So the hypothesis holds and the conclusion fails. What the printed proof establishes, and what is proved below, is the corrected statement: each component of $X$ is a countable union of compact subspaces. Closures are taken in $X_0$.


::: pf

::: {.pf-step #closures-compact}
$\overline{U}_n$ is compact for every $n \ge 1$.

::: pf-proof

::: {.pf-step #u1-closure-compact}
$\overline{U}_1$ is compact.

::: pf-proof
$U_1 \in \mathcal{C}$, and every member of $\mathcal{C}$ has compact closure.
:::

:::

::: {.pf-step #finite-members-meet-closure}
If $\overline{U}_{n-1}$ is compact, then only finitely many members $V_1, \ldots, V_m$ of $\mathcal{C}$ meet $\overline{U}_{n-1}$.

::: pf-proof
By local finiteness, each $x \in \overline{U}_{n-1}$ has an open neighborhood $W_x$ that meets only finitely many members of $\mathcal{C}$. Finitely many of these, $W_{x_1}, \ldots, W_{x_k}$, cover the compact set $\overline{U}_{n-1}$. A member of $\mathcal{C}$ that meets $\overline{U}_{n-1}$ meets some $W_{x_i}$, and there are only finitely many such members.
:::

:::

::: pf-qed
Induct on $n$, with base case step [](#u1-closure-compact){.pf-ref}. If $\overline{U}_{n-1}$ is compact, step [](#finite-members-meet-closure){.pf-ref} gives $U_n = V_1 \cup \cdots \cup V_m$, so
$$\overline{U}_n = \overline{V}_1 \cup \cdots \cup \overline{V}_m$$
is a finite union of compact sets, hence compact.
:::

:::

:::

::: {.pf-step #a-nonempty-open}
$A = \bigcup_{n=1}^\infty U_n$ is nonempty and open in $X_0$.

::: pf-proof
$A$ contains the nonempty set $U_1$, and each $U_n$ is a union of sets open in $X_0$.
:::

:::

::: {.pf-step #a-closed}
$A$ is closed in $X_0$.

::: pf-proof
Let $x \in \overline{A}$. Since $\mathcal{C}$ covers $X_0$, some $V_0 \in \mathcal{C}$ contains $x$. The open set $V_0$ meets $A$, so it meets $U_{n-1}$ for some $n \ge 2$, hence meets $\overline{U}_{n-1}$. By the definition of $U_n$, $V_0 \subseteq U_n \subseteq A$, so $x \in A$.
:::

:::

::: pf-qed
Step [](#closures-compact){.pf-ref} shows that each $\overline{U}_n$ is compact. By steps [](#a-nonempty-open){.pf-ref} and [](#a-closed){.pf-ref}, $A$ is a nonempty open and closed subset of the connected space $X_0$, so $A = X_0$. Hence $X_0=\bigcup_n\overline{U}_n$ is a countable union of compact subspaces.
:::

:::

:::
