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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise and found none
    (issue #144). Math StackExchange through the API, site math, with the queries "Ascoli theorem
    metric space compact", "Ascoli theorem metric space", "Ascoli Arzela general metric space" and
    "Arzela Ascoli theorem equicontinuous" returns 1492990, whose only answer is a link to
    generalisations, 106138 and 1159772, which survey statements of the theorem for metric targets
    rather than following Munkres' proof step by step. None of them shows that the proof goes
    through when closed bounded subspaces of the target are compact, which is what the exercise
    asks. dbFin has no chapter-7 page (404, checked 2026-11-15), and no GitHub Munkres repository
    named in the COMPLAINTS.md entry for §30--§36 reaches Chapter 7. The card keeps its own proof,
    which this pass did not re-read; the search is recorded in the COMPLAINTS.md entry for
    §43--§50 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The AoPS blog post by cinnamon_e, "Topology by Munkres Chapter 7 | Day 16" (2025-09-09, listed
    on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), also answers this exercise, at its item 6
    of §45. The text is held, but the formulas are not: the extraction drops every inline formula,
    so the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read, with one false inequality repaired. The proof of the only-if direction chose
    an $\varepsilon/3$-net $g_1,\ldots,g_k$ and neighbourhoods on which each $g_i$ moves by less
    than $\varepsilon/3$, then bounded $d(g(x),g(y))$ by three terms and called the sum less than
    $\varepsilon$. The middle term is only known to be below $2\varepsilon/3$ on $U$, so $4\varepsilon/3$
    is what follows; the step now estimates $d(g(x),g(a))$ at the base point, where the middle term
    is below $\varepsilon/3$, which is exactly equicontinuity at $a$. Added also: $\mathcal G$ is
    bounded under $\rho$ because it is compact, and on a bounded family $\rho$ and
    $\bar\rho=\min(\rho,1)$ have the same balls below radius $1$, so Lemma 45.2, stated for
    $\bar\rho$, applies to the card's supremum metric. The rest was checked and stands. Citation by
    number: §45 Exercise 6, Theorem 45.1, Lemma 45.2 and Lemma 45.3.

---

::: {.exercise}

Show that our proof of Ascoli's theorem goes through if $\RR^n$ is replaced by any metric space in which all closed bounded subspaces are compact.
:::

::: {.solution}

The argument is the card's own, following the four steps of the proof of Theorem 45.4 with $\RR^{n}$ replaced by a metric space $Y$ in which every closed bounded subspace is compact; no published solution of this exercise was located, and the sets searched are recorded in the audit trail.

Let $(Y,d)$ be a metric space in which every closed bounded subspace is compact, let $X$ be compact, and let $\mathcal{C}(X,Y)$ carry the uniform metric $\rho(f,g)=\max_{x\in X}d\big(f(x),g(x)\big)$.

::: pf

::: {.pf-step #preliminaries}
$Y$ is complete, and the closure of a bounded subset of $Y$ is compact.

::: pf-proof
A Cauchy sequence in $Y$ is bounded, so it lies in a closed ball $\overline{B}(a,r)$, which is closed and bounded, hence compact; a compact metric space is complete (Theorem 45.1), so the sequence has a limit in $Y$ and $Y$ is complete. A bounded $B\subset Y$ lies in a closed ball $\overline{B}(a,r)$, whose closure $\overline{B}$ of $B$ is then a closed subset of that compact ball, hence compact by Theorem 26.2.
:::

:::

::: {.pf-step #only-if}
If $\mathcal{G}\subset\mathcal{C}(X,Y)$ is compact, then $\mathcal{G}$ is equicontinuous and pointwise bounded.

::: pf-proof
A compact subspace of a metric space is totally bounded (Theorem 45.1), so for $\varepsilon>0$ there are $g_{1},\ldots,g_{k}\in\mathcal{G}$ with $\mathcal{G}\subset\bigcup_{i}B_{\rho}(g_{i},\varepsilon/3)$; each $g_{i}$ is continuous, so each point $a\in X$ has a neighbourhood $U_{i}$ on which $d\big(g_{i}(x),g_{i}(a)\big)<\varepsilon/3$. On the intersection $U$ of the finitely many $U_{i}$, let $g\in\mathcal{G}$ and choose $i$ with $\rho(g,g_{i})<\varepsilon/3$; then for $x\in U$
$$
d\big(g(x),g(a)\big)\le d\big(g(x),g_{i}(x)\big)+d\big(g_{i}(x),g_{i}(a)\big)+d\big(g_{i}(a),g(a)\big)<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon,
$$
the first and third terms being below $\varepsilon/3$ because $\rho(g,g_{i})<\varepsilon/3$ and the second by the choice of $U_{i}$. So $\mathcal{G}$ is equicontinuous at $a$ (Lemma 45.2). Since $\mathcal{G}$ is compact it is bounded under $\rho$, and on a bounded family the supremum metric $\rho$ and the uniform metric $\bar\rho=\min(\rho,1)$ have the same balls of radius below $1$, so the lemma, stated for $\bar\rho$, applies. And $\mathcal{G}$ is bounded under $\rho$, so for a fixed $a\in X$ the set $\mathcal{G}_{a}=\{g(a)\}$ is bounded, since $d\big(f(a),g(a)\big)\le\rho(f,g)$; so $\mathcal{G}$ is pointwise bounded.
:::

:::

::: {.pf-step #closure}
If $\mathcal{F}$ is equicontinuous and pointwise bounded, then so is its closure $\mathcal{G}=\overline{\mathcal{F}}$ in $\mathcal{C}(X,Y)$.

::: pf-proof
Let $\varepsilon>0$ and $a\in X$; choose a neighbourhood $U$ of $a$ with $d\big(f(x),f(a)\big)<\varepsilon/3$ for all $x\in U$ and $f\in\mathcal{F}$. For $g\in\mathcal{G}$ choose $f\in\mathcal{F}$ with $\rho(f,g)<\varepsilon/3$; then for $x\in U$,
$$
d\big(g(x),g(a)\big)\le d\big(g(x),f(x)\big)+d\big(f(x),f(a)\big)+d\big(f(a),g(a)\big)<\varepsilon ,
$$
so $\mathcal{G}$ is equicontinuous. For pointwise boundedness, let $\mathcal{F}_{a}$ have diameter at most $M$; then $d\big(g(a),g'(a)\big)\le d\big(g(a),f(a)\big)+d\big(f(a),f'(a)\big)+d\big(f'(a),g'(a)\big)<M+2$ for $g,g'\in\mathcal{G}$ and suitable $f,f'\in\mathcal{F}$, so $\mathcal{G}_{a}$ is bounded.
:::

:::

::: {.pf-step #compact-target}
If $\mathcal{G}\subset\mathcal{C}(X,Y)$ is equicontinuous and pointwise bounded, then $\mathcal{G}\subset\mathcal{C}(X,Y_{0})$ for a compact subspace $Y_{0}$ of $Y$.

::: pf-proof
For each $a\in X$ choose a neighbourhood $U_{a}$ of $a$ with $d\big(g(x),g(a)\big)<1$ for $x\in U_{a}$ and $g\in\mathcal{G}$; finitely many $U_{a_{1}},\ldots,U_{a_{k}}$ cover the compact $X$. Each $\mathcal{G}_{a_{i}}$ is bounded, so finitely many of them lie in one closed ball $\overline{B}(y_{0},N)$: choose $y_{0}\in Y$ and $N$ with $d\big(g(a_{i}),y_{0}\big)\le N$ for all $i$ and $g\in\mathcal{G}$, possible since a finite union of bounded sets is bounded. For $g\in\mathcal{G}$ and $x\in U_{a_{i}}$,
$$
d\big(g(x),y_{0}\big)\le d\big(g(x),g(a_{i})\big)+d\big(g(a_{i}),y_{0}\big)<N+1 ,
$$
so $\mathcal{G}\subset\mathcal{C}(X,Y_{0})$ with $Y_{0}=\overline{B}(y_{0},N+1)$, which is closed and bounded, hence compact by step [](#preliminaries){.pf-ref}.
:::

:::

::: {.pf-step #if}
If $\mathcal{F}\subset\mathcal{C}(X,Y)$ is equicontinuous and pointwise bounded, then $\overline{\mathcal{F}}$ is compact; hence a subspace of $\mathcal{C}(X,Y)$ has compact closure exactly when it is equicontinuous and pointwise bounded.

::: pf-proof
Let $\mathcal{G}=\overline{\mathcal{F}}$, which is equicontinuous and pointwise bounded by step [](#closure){.pf-ref} and lies in $\mathcal{C}(X,Y_{0})$ with $Y_{0}$ compact by step [](#compact-target){.pf-ref}. Lemma 45.3 uses only the compactness of the target space and gives that $\mathcal{G}$ is totally bounded under $\rho$. The space $\mathcal{C}(X,Y)$ is complete because $Y$ is complete (Theorem 43.6), and $\mathcal{G}$ is closed in it, hence complete; a complete totally bounded metric space is compact (Theorem 45.1). So $\mathcal{F}$ has compact closure. Conversely a compact $\mathcal{G}$ gives the two properties by step [](#only-if){.pf-ref}, and steps [](#only-if){.pf-ref} and this one together are Ascoli's theorem with $\RR^{n}$ replaced by $Y$.
:::

:::

:::
:::
