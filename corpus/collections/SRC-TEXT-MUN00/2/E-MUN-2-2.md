---
schema: qual/card@1
id: E-MUN-2-2
kind: problem
title: Preimage preserves all set operations; image preserves unions only
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 2; restored parts (g) and (h) to the printed request for counterexamples where equality fails.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Parts (g) and (h) were not stored as the book prints them. Munkres, Topology (2000),
    §2 Exercise 2, printed pp. 20-21, reads "(g) f(A_0 cap A_1) is a subset of
    f(A_0) cap f(A_1); show that equality holds if f is injective" and "(h) f(A_0 - A_1)
    contains f(A_0) - f(A_1); show that equality holds if f is injective", checked on the
    page image of printed p. 21 as well as the text layer. The card asked instead for
    "an example where equality fails", which is a different exercise: the printed one
    asks for the equality under injectivity. The earlier note calling the replacement
    "restored ... to the printed request" was false and is kept above unchanged as
    history. The statements now read as printed; the counterexamples the card already
    carried are kept as the remark showing that the injectivity hypothesis is needed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.2,
    printed pp. 11-12 (tmp/sources/munkres-solutions-whitman.pdf), parts (a)-(h). Added
    the two missing directions of the printed (g) and (h), the injective case: he proves
    them by the argument now on the card, that equal image values come from one point.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: one step per part, with the two directions
    of the printed (g) and (h) and their counterexamples to the equality without injectivity
    as substeps. The argument is the retained solution's, unchanged; its cited pages were not
    re-read in this pass, and the printed statement was not re-read either, its source
    correction being the earlier event above.
---

::: {.exercise}

Let $f: A \to B$ and let $A_i \subset A$ and $B_i \subset B$ for $i = 0$ and $i = 1$ . Show that $f^{-1}$ preserves inclusions, unions, intersections, and differences of sets:

(a) $B_0 \subset B_1 \Rightarrow f^{-1}(B_0) \subset f^{-1}(B_1)$ .

(b) $f^{-1}(B_{0} \cup B_{1}) = f^{-1}(B_{0}) \cup f^{-1}(B_{1}).$

(c) $f^{-1}(B_{0} \cap B_{1}) = f^{-1}(B_{0}) \cap f^{-1}(B_{1}).$

(d) $f^{-1}(B_0 - B_1) = f^{-1}(B_0) - f^{-1}(B_1)$ .

Show that $f$ preserves inclusions and unions only:

(e) $A_0 \subset A_1 \Rightarrow f(A_0) \subset f(A_1)$ .

(f) $f(A_{0} \cup A_{1}) = f(A_{0}) \cup f(A_{1}).$

(g) $f(A_0 \cap A_1) \subset f(A_0) \cap f(A_1)$ ; show that equality holds if $f$ is injective.

(h) $f(A_0 - A_1) \supset f(A_0) - f(A_1)$ ; show that equality holds if $f$ is injective.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.2, printed pp. 11--12** (`tmp/sources/munkres-solutions-whitman.pdf`), all eight parts; the chains of equivalences for the preimage, the injective directions of (g) and (h), and the counterexamples are his.

For preimages the only input is the equivalence $x\in f^{-1}(S)\iff f(x)\in S$. Throughout, $f:A\to B$, $A_{i}\subset A$ and $B_{i}\subset B$ for $i=0,1$.

::: pf

::: {.pf-step #preimage-inclusion}
(a) $B_{0}\subset B_{1}$ implies $f^{-1}(B_{0})\subset f^{-1}(B_{1})$.

::: pf-proof
Let $x\in f^{-1}(B_{0})$, so $f(x)\in B_{0}$. Since $B_{0}\subset B_{1}$ this gives $f(x)\in B_{1}$, that is $x\in f^{-1}(B_{1})$.
:::

:::

::: {.pf-step #preimage-union}
(b) $f^{-1}(B_{0}\cup B_{1})=f^{-1}(B_{0})\cup f^{-1}(B_{1})$.

::: pf-proof
For each $x\in A$,
$$
x\in f^{-1}(B_{0}\cup B_{1})
\iff f(x)\in B_{0}\text{ or }f(x)\in B_{1}
\iff x\in f^{-1}(B_{0})\cup f^{-1}(B_{1}),
$$
so the two sets have the same elements.
:::

:::

::: {.pf-step #preimage-intersection}
(c) $f^{-1}(B_{0}\cap B_{1})=f^{-1}(B_{0})\cap f^{-1}(B_{1})$.

::: pf-proof
The same chain with “and” in place of “or”: $x$ lies in the left side exactly when $f(x)\in B_{0}$ and $f(x)\in B_{1}$, which is exactly the definition of the right side.
:::

:::

::: {.pf-step #preimage-difference}
(d) $f^{-1}(B_{0}-B_{1})=f^{-1}(B_{0})-f^{-1}(B_{1})$.

::: pf-proof
Likewise: $x\in f^{-1}(B_{0}-B_{1})$ exactly when $f(x)\in B_{0}$ and $f(x)\notin B_{1}$, that is when $x\in f^{-1}(B_{0})$ and $x\notin f^{-1}(B_{1})$.
:::

:::

::: {.pf-step #image-inclusion}
(e) $A_{0}\subset A_{1}$ implies $f(A_{0})\subset f(A_{1})$.

::: pf-proof
Every value $f(x)$ with $x\in A_{0}$ satisfies $x\in A_{1}$ as well, so it is a value of $f$ on $A_{1}$.
:::

:::

::: {.pf-step #image-union}
(f) $f(A_{0}\cup A_{1})=f(A_{0})\cup f(A_{1})$.

::: pf-proof
A point $y\in B$ lies in $f(A_{0}\cup A_{1})$ exactly when $y=f(x)$ for some $x$ in at least one of $A_{0},A_{1}$, which is exactly when $y\in f(A_{0})$ or $y\in f(A_{1})$.
:::

:::

::: {.pf-step #image-intersection}
(g) $f(A_{0}\cap A_{1})\subset f(A_{0})\cap f(A_{1})$, with equality when $f$ is injective and not in general.

::: pf-proof
The inclusion, the injective case, and a counterexample to equality without injectivity.

::: {.pf-step #g-subset}
$f(A_{0}\cap A_{1})\subset f(A_{0})\cap f(A_{1})$.

::: pf-proof
If $y=f(x)$ with $x\in A_{0}\cap A_{1}$, then $x\in A_{0}$ gives $y\in f(A_{0})$ and $x\in A_{1}$ gives $y\in f(A_{1})$.
:::

:::

::: {.pf-step #g-injective}
If $f$ is injective, equality holds.

::: pf-proof
Let $y\in f(A_{0})\cap f(A_{1})$, so $y=f(x_{0})=f(x_{1})$ with $x_{0}\in A_{0}$ and $x_{1}\in A_{1}$. Injectivity gives $x_{0}=x_{1}$, a point of $A_{0}\cap A_{1}$, so $y\in f(A_{0}\cap A_{1})$; with step [](#g-subset){.pf-ref} the two sets are equal.
:::

:::

::: {.pf-step #g-fails}
Without injectivity the equality can fail.

::: pf-proof
Take $f:\{0,1\}\to\{*\}$ the constant map, $A_{0}=\{0\}$ and $A_{1}=\{1\}$. Then $A_{0}\cap A_{1}=\varnothing$, so $f(A_{0}\cap A_{1})=\varnothing$, while $f(A_{0})\cap f(A_{1})=\{*\}\cap\{*\}=\{*\}$. So the inclusion in step [](#g-subset){.pf-ref} is proper here and the injectivity hypothesis is needed.
:::

:::

:::

:::

::: {.pf-step #image-difference}
(h) $f(A_{0}-A_{1})\supset f(A_{0})-f(A_{1})$, with equality when $f$ is injective and not in general.

::: pf-proof
The inclusion, the injective case, and a counterexample to equality without injectivity.

::: {.pf-step #h-superset}
$f(A_{0})-f(A_{1})\subset f(A_{0}-A_{1})$.

::: pf-proof
Let $y\in f(A_{0})-f(A_{1})$ and write $y=f(x)$ with $x\in A_{0}$. Were $x\in A_{1}$ then $y\in f(A_{1})$, contrary to hypothesis; so $x\in A_{0}-A_{1}$ and $y\in f(A_{0}-A_{1})$.
:::

:::

::: {.pf-step #h-injective}
If $f$ is injective, equality holds.

::: pf-proof
Let $y\in f(A_{0}-A_{1})$, say $y=f(x)$ with $x\in A_{0}-A_{1}$. Then $y\in f(A_{0})$. If also $y=f(x_{0})$ with $x_{0}\in A_{1}$, injectivity gives $x=x_{0}\in A_{1}$, contradicting $x\in A_{0}-A_{1}$; so $y\notin f(A_{1})$ and $y\in f(A_{0})-f(A_{1})$. With step [](#h-superset){.pf-ref} the two sets are equal.
:::

:::

::: {.pf-step #h-fails}
Without injectivity the equality can fail.

::: pf-proof
For the constant map $f:\{0,1\}\to\{*\}$, $A_{0}=\{0,1\}$ and $A_{1}=\{1\}$ give $A_{0}-A_{1}=\{0\}$, so $f(A_{0}-A_{1})=\{*\}$, while $f(A_{0})-f(A_{1})=\{*\}-\{*\}=\varnothing$. So (h) is a proper inclusion here.
:::

:::

:::

:::

:::
:::
