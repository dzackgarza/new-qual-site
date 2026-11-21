---
schema: qual/card@1
id: E-AMD-HICDBVN4
kind: problem
title: $K[\alpha_1,\ldots,\alpha_n]=K(\alpha_1,\ldots,\alpha_n)$ for algebraic $\alpha_i$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.1,
    exercise 4(d), book page 241: "(d) If each u_i is algebraic over K, then
    K(u_1, ..., u_n) = K[u_1, ..., u_n]." The card states exactly this part,
    which is the part the collection lists. The proof was checked: for α
    algebraic over a field L with minimal polynomial m_α, evaluation gives
    L[x]/(m_α) ≅ L[α], and since m_α is irreducible the ideal is maximal, so
    L[α] is a field and equals L(α); adjoining the α_i one at a time, each
    remains algebraic over the larger field because its minimal polynomial over
    K is still available there; and K[u_1, ..., u_n] is the iterated simple
    extension ring. Complete; no defect. The card claims only part (d); parts
    (a), (b), (c) of the same exercise are not claimed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, keeping the induction from the earlier proof. Checked
    against Hungerford, Algebra (1974), section V.1, exercise 4(d), book page 241, whose statement
    covers exactly the part proved. The argument is the card's own; no retained solution set is
    cited. Every step re-read: evaluation $L[x]\to L[\alpha]$ has kernel $(m_\alpha)$ (division
    with remainder), $(m_\alpha)$ is maximal since $L[x]$ is a PID and the minimal polynomial is
    irreducible, so $L[\alpha]$ is a field and equals $L(\alpha)$; each $\alpha_i$ stays algebraic
    over the larger field $K_{i-1}$ because its polynomial over $K$ is still available there; the
    polynomial and the rational constructions are both iterated one-element extensions. Also
    removed a stray second frontmatter separator line that sat between the audit block and the
    exercise, which made the card parse as an empty body followed by a thematic break.
---

::: {.exercise}
Let $F/K$ be a field extension, and let $\alpha_1,\dots,\alpha_n\in F$ be algebraic over $K$.
Show that
$$
K[\alpha_1,\dots,\alpha_n]=K(\alpha_1,\dots,\alpha_n).
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Hungerford, Algebra (1974), section V.1, exercise 4(d), book page 241: adjoining finitely many algebraic elements by polynomials gives the same thing as adjoining them by rational functions. The two ingredients are that a simple algebraic extension by polynomials is already a field, and that the polynomial and rational constructions are both iterated simple extensions.

::: pf

::: {.pf-step #simple}
Let $L$ be a field and $\alpha$ algebraic over $L$, with minimal polynomial $m_\alpha\in L[x]$. Then $L[\alpha]=L(\alpha)$.

:::: pf-proof

::: {.pf-step #eval}
Evaluation at $\alpha$ is a surjective ring homomorphism $\varphi:L[x]\to L[\alpha]$ with kernel $(m_\alpha)$.

::: pf-proof
$\varphi(f)=f(\alpha)$ is a ring homomorphism fixing $L$, and its image is by definition the subring $L[\alpha]$ of $F$, so $\varphi$ is surjective onto it. Since $m_\alpha(\alpha)=0$, the ideal $(m_\alpha)$ lies in $\ker\varphi$; conversely if $f(\alpha)=0$, division with remainder in the Euclidean domain $L[x]$ writes $f=q\,m_\alpha+r$ with $\deg r<\deg m_\alpha$, and $r(\alpha)=f(\alpha)-q(\alpha)m_\alpha(\alpha)=0$, so minimality of $\deg m_\alpha$ forces $r=0$ and $m_\alpha$ divides $f$. Hence $\ker\varphi=(m_\alpha)$.
:::

:::

::: {.pf-step #maximal}
$(m_\alpha)$ is a maximal ideal of $L[x]$.

::: pf-proof
$L[x]$ is a principal ideal domain because $L$ is a field, and in a principal ideal domain a nonzero ideal is maximal exactly when its generator is irreducible. The minimal polynomial $m_\alpha$ is irreducible over $L$: a factorisation $m_\alpha=gh$ with both factors of positive degree would give $g(\alpha)h(\alpha)=0$ in the field $F$, so one factor vanishes at $\alpha$ and is a nonzero polynomial over $L$ of degree smaller than $\deg m_\alpha$, contradicting minimality.
:::

:::

::: {.pf-step #field}
$L[\alpha]$ is a field, so $L[\alpha]=L(\alpha)$.

::: pf-proof
By the first isomorphism theorem with steps [](#eval){.pf-ref} and [](#maximal){.pf-ref}, $L[\alpha]\cong L[x]/(m_\alpha)$ is a field. It contains $L$ and $\alpha$, and $L(\alpha)$ is by definition the smallest subfield of $F$ containing both, so $L(\alpha)\subseteq L[\alpha]$; the reverse inclusion holds because every field is a ring. Hence the two are equal.
:::

:::

::::

:::

::: {.pf-step #induction}
With $K_0=K$ and $K_i=K_{i-1}[\alpha_i]$, each $K_i$ is a field and $K_i=K_{i-1}(\alpha_i)$.

::: pf-proof
Induction on $i$. The case $i=0$ is $K_0=K$. For the step, $\alpha_i$ is algebraic over $K$, so some nonzero $f\in K[x]$ has $f(\alpha_i)=0$; since $K\subseteq K_{i-1}$, the same $f$ lies in $K_{i-1}[x]$, so $\alpha_i$ is algebraic over $K_{i-1}$. Step [](#simple){.pf-ref} applied to the field $K_{i-1}$ then gives that $K_i=K_{i-1}[\alpha_i]$ is a field equal to $K_{i-1}(\alpha_i)$.
:::

:::

::: {.pf-step #poly}
$K[\alpha_1,\ldots,\alpha_n]=K_n$ and $K(\alpha_1,\ldots,\alpha_n)=K_n$.

::: pf-proof
$K[\alpha_1,\ldots,\alpha_n]$ is the smallest subring of $F$ containing $K$ and the $\alpha_i$. Inductively, the smallest subring containing $K,\alpha_1,\ldots,\alpha_i$ is the smallest subring containing $K[\alpha_1,\ldots,\alpha_{i-1}]$ and $\alpha_i$, which is $K_{i-1}[\alpha_i]=K_i$; so the polynomial construction gives $K_n$. The same induction with "subfield" and "smallest subfield" in place of "subring" gives $K(\alpha_1,\ldots,\alpha_n)=K_n$, using $K_i=K_{i-1}(\alpha_i)$ from step [](#induction){.pf-ref}.
:::

:::

::: {.pf-step}
$K[\alpha_1,\ldots,\alpha_n]=K(\alpha_1,\ldots,\alpha_n)$, as claimed.

::: pf-proof
Both sides equal $K_n$ by step [](#poly){.pf-ref}, hence they are equal.
:::

:::

:::
:::
