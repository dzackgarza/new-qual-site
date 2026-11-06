---
schema: qual/card@1
id: P-PRACT20-W6-13
kind: problem
title: Continuous images of compact sets are compact
classification:
  areas:
  - prelim
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-PRACTICE-WEEK6-2020 has an empty provenance list, and the only
    retained pages of the practice sheet are the three page images
    assets/attachments/prelim-practice-week6-2020/page-4.png, page-5.png and
    page-11.png, none of which carries this problem; so there is no printed page
    to compare the statement with. What was checked is the statement as it stands
    on the card: the statement is the standard one and the proof was derived from the definition of compactness and of continuity through preimages of open sets
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the solution is
    derived here rather than transcribed. The preimage cover argument, the finite subcover descending to the image, and the identification of the conclusion as compactness of the image
---

::: {.problem}
Let $X, Y$ be topological spaces and let $f : X \to Y$ be continuous.
Show that $f(K)$ is compact in $Y$ for any compact set $K \subseteq X$. In short: show that the continuous image of a compact set is compact.
:::

::: {.solution}

Let $X,Y$ be topological spaces, $f\colon X\to Y$ continuous and $K\subseteq
X$ compact.

::: pf

::: {.pf-step #cover}

Every open cover of $f(K)$ in $Y$ has a finite subcover.

::: pf-proof

Let $f(K)\subseteq\bigcup_\alpha V_\alpha$ with $V_\alpha$ open in $Y$. Then
$K\subseteq f^{-1}(f(K))\subseteq\bigcup_\alpha f^{-1}(V_\alpha)$, and each
$f^{-1}(V_\alpha)$ is open in $X$ because $f$ is continuous. So
$\{f^{-1}(V_\alpha)\}$ is an open cover of $K$, and compactness of $K$ gives a
finite subfamily $f^{-1}(V_{\alpha_1}),\dots,f^{-1}(V_{\alpha_n})$ covering
$K$.

:::

:::

::: {.pf-step #finitesubcover}

$f(K)\subseteq\bigcup_{j=1}^nV_{\alpha_j}$.

::: pf-proof

If $y\in f(K)$ then $y=f(x)$ for some $x\in K$, and $x$ lies in some
$f^{-1}(V_{\alpha_j})$ by step [](#cover){.pf-ref}, so $y=f(x)\in
V_{\alpha_j}$. Hence the finitely many $V_{\alpha_j}$ cover $f(K)$.

:::

:::

::: {.pf-step #compact}

$f(K)$ is compact, so the continuous image of a compact set is compact.

::: pf-proof

Steps [](#cover){.pf-ref} and [](#finitesubcover){.pf-ref} show that every
open cover of $f(K)$ in the subspace topology has a finite subcover: a cover
by sets open in $f(K)$ is a cover by intersections $V_\alpha\cap f(K)$ with
$V_\alpha$ open in $Y$, and the argument applies verbatim. That is compactness
of $f(K)$. In metric spaces the same conclusion reads: a sequence in $f(K)$ is
the image of a sequence in $K$, which has a convergent subsequence by
compactness, and continuity carries the limit to the limit of the image
subsequence.

:::

:::

:::


:::
