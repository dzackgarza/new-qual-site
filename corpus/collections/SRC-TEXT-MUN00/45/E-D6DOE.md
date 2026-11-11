---
schema: qual/card@1
id: E-D6DOE
kind: problem
title: Ascoli's theorem over proper metric targets
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §45 Exercise 6 (printed p. 280) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book's proof
    of Theorem 45.4 (printed pp. 277-279) and of Lemma 45.3, whose steps the card now follows one by one,
    with Theorem 45.1, Lemma 45.2, Theorem 43.6 (completeness of C(X,Y) for complete Y) and Theorem 27.3.
    What the hypothesis is used for, located at each place: a metric space whose closed bounded subspaces
    are compact is complete, because a Cauchy sequence is bounded and so lies in a closed ball; and in
    Step 3 the closed ball of radius N+1 about y_0 that contains all the values is closed and bounded,
    hence compact, which is the target Y_0 to which Lemma 45.3 is applied. Step 1, Step 2 and the proof of
    Lemma 45.2 use no property of the target beyond the triangle inequality, and the proof of Lemma 45.3
    uses only compactness of the target. The card's earlier solution was a sketch that named the property
    without locating its two uses; it is now the four steps written out.
---

::: {.exercise}

Show that our proof of Ascoli's theorem goes through if $\RR^n$ is replaced by any metric space in which all closed bounded subspaces are compact.
:::

::: {.solution}
Let $(Y, d)$ be a metric space in which every closed bounded subspace is compact, and let $X$ be compact. Two consequences of the hypothesis are used:

- $Y$ is complete: a Cauchy sequence is bounded, so it lies in a closed ball $\overline{B}(a, r)$, which is closed and bounded, hence compact, and a compact metric space is complete (Theorem 45.1, or Lemma 43.1 with Theorem 28.2);
- the closure of a bounded subset of $Y$ is compact, since it lies in some closed ball $\overline{B}(a, r)$.

Now follow the four steps of the proof of Theorem 45.4.

**Step 1 (only if).** If $\mathcal{G} \subset \mathcal{C}(X, Y)$ is compact, then $\mathcal{G}$ is totally bounded under $\rho$ by Theorem 45.1, hence equicontinuous under $d$ by Lemma 45.2; the proof of Lemma 45.2 uses only metrizability of $Y$. Compactness of $\mathcal{G}$ also makes $\mathcal{G}$ bounded under $\rho$, hence pointwise bounded, since $d(f(a), g(a)) \le \rho(f, g)$ in any metric target. So a family with compact closure is equicontinuous and pointwise bounded.

**Step 2 (the closure inherits both).** If $\mathcal{F}$ is equicontinuous and pointwise bounded, so is its closure $\mathcal{G}$: the equicontinuity is the $\varepsilon/3$ argument with an approximation $f \in \mathcal{F}$ of $g \in \mathcal{G}$, and the pointwise boundedness uses $\operatorname{diam} \mathcal{F}_a \le M$ and two approximations within $1$. Neither half uses anything about $Y$ beyond the triangle inequality.

**Step 3 (a compact target containing all the values).** Let $\mathcal{G}$ be equicontinuous and pointwise bounded. For each $a \in X$ choose a neighbourhood $U_a$ of $a$ with $d(g(x), g(a)) < 1$ for $x \in U_a$ and $g \in \mathcal{G}$; finitely many $U_{a_1}, \ldots, U_{a_k}$ cover $X$. Each set $\mathcal{G}_{a_i}$ is bounded, so lies in a closed ball about $a_i$; a finite union of bounded sets is bounded, so all the sets $\mathcal{G}_{a_i}$ lie in one closed ball $\overline{B}(y_0, N)$. Then for every $g \in \mathcal{G}$ and every $x \in X$, choosing $i$ with $x \in U_{a_i}$,
$$
d(g(x), y_0) \le d(g(x), g(a_i)) + d(g(a_i), y_0) < N + 1 .
$$
Here the hypothesis enters: the closed ball $Y_0 = \overline{B}(y_0, N+1)$ is closed and bounded, hence compact, and $\mathcal{G} \subset \mathcal{C}(X, Y_0)$. (For $Y = \RR^n$ one takes the same closed ball, compact by Heine-Borel, Theorem 27.3.)

**Step 4 (if).** Let $\mathcal{F}$ be equicontinuous and pointwise bounded. By Step 2 its closure $\mathcal{G}$ is equicontinuous and pointwise bounded, and by Step 3 $\mathcal{G} \subset \mathcal{C}(X, Y_0)$ with $Y_0$ compact. Lemma 45.3, whose proof uses only compactness of the target, gives total boundedness of $\mathcal{G}$ under $\rho$. Completeness of $\mathcal{C}(X, Y)$ under $\rho$ is Theorem 43.6, which needs only that $Y$ be complete, and $Y$ is complete by the first consequence above. A closed subspace of a complete metric space is complete, so $\mathcal{G}$ is complete and totally bounded, hence compact by Theorem 45.1.

Therefore a subspace $\mathcal{F}$ of $\mathcal{C}(X, Y)$ has compact closure if and only if it is equicontinuous and pointwise bounded under $d$, which is Ascoli's theorem with $\RR^n$ replaced by $Y$. Nothing in the argument uses the vector-space structure of $\RR^n$, only the compactness of closed bounded subspaces: in Step 3 to produce the compact target $Y_0$ and in the completeness of $Y$.
:::
