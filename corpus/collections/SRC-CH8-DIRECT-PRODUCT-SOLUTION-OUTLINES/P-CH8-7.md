---
schema: qual/card@1
id: P-CH8-7
kind: problem
title: Direct products are commutative up to isomorphism
classification:
  areas:
    - algebra
  topics:
    - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the retained solution outline for Gallian, Chapter 8, Exercise 7, PDF p. 2 of
    assets/attachments/Ch8Sltns.pdf, into numbered steps; the outline prints phi((g1,g2)(h1,h2)) =
    phi((g1g2,h1h2)) = (h1h2,g1g2), which garbles the components, and the card's correct version
    is kept. The general case is stated with the permutation the outline names (sigma in S_n) and
    its bijectivity is given an inverse. Checked: the componentwise product, injectivity,
    surjectivity and the general permutation argument. Not checked: the printed exercise and page
    in Gallian, which is not retained; the outline's page is the citation, and the certificate
    remark on the card is unchanged.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Gallian, Contemporary Abstract Algebra, seventh edition, Chapter 8
    Exercise 7, printed p. 167 (file p. 182 of the retained copy, whose running head on that
    page is 167). The printed exercise is the card's statement word for word, so no repair
    was needed, and the solution's opening sentence now names the exercise and the page.
    Not checked in this pass: the argument, which this edit does not touch.

---

::: {.problem}
Prove that $G_{1} \oplus G_{2}$ is isomorphic to $G_{2} \oplus G_{1}$. State the general case.
:::

::: {.solution}

In the seventh edition this is Chapter 8 Exercise 7, printed p. 167, where the printed
words are the statement below.

The argument is that of the retained solution outline for Chapter 8, Exercise 7, PDF p. 2 of `assets/attachments/Ch8Sltns.pdf`, restructured into numbered steps; the outline's homomorphism line misprints the second component as $h_1h_2$ where $g_2h_2$ belongs, and the step below writes it correctly. Here $G_1,G_2$ are groups and $G_1\oplus G_2$ is their external direct product with componentwise operation.

::: pf

::: {.pf-step #def}

$\phi(g_1,g_2)\coloneqq(g_2,g_1)$ defines a map $G_1\oplus G_2\to G_2\oplus G_1$.

::: pf-proof

For each pair the recipe names an element of $G_2\times G_1$, so $\phi$ is a function with the stated domain and codomain.

:::

:::

::: {.pf-step #hom}

$\phi$ is a homomorphism.

::: pf-proof

For $(g_1,g_2),(h_1,h_2)\in G_1\oplus G_2$, $\phi((g_1,g_2)(h_1,h_2))=\phi(g_1h_1,g_2h_2)=(g_2h_2,g_1h_1)=(g_2,g_1)(h_2,h_1)=\phi(g_1,g_2)\phi(h_1,h_2)$, the first and last equalities by the definition of the direct product and the middle by that of $\phi$.

:::

:::

::: {.pf-step #inj}

$\phi$ is injective.

::: pf-proof

If $\phi(g_1,g_2)=\phi(h_1,h_2)$ then $(g_2,g_1)=(h_2,h_1)$, so $g_2=h_2$ and $g_1=h_1$ by equality of ordered pairs, hence $(g_1,g_2)=(h_1,h_2)$.

:::

:::

::: {.pf-step #surj}

$\phi$ is surjective.

::: pf-proof

An element of $G_2\oplus G_1$ is $(g_2,g_1)$ with $g_1\in G_1$, $g_2\in G_2$; then $(g_1,g_2)\in G_1\oplus G_2$ and $\phi(g_1,g_2)=(g_2,g_1)$.

:::

:::

::: {.pf-step #done}

$G_1\oplus G_2\approx G_2\oplus G_1$.

::: pf-proof

Steps [](#def){.pf-ref} to [](#surj){.pf-ref} give a bijective homomorphism.

:::

:::

::: {.pf-step #general}

General case: for a permutation $\sigma\in S_n$, $G_1\oplus\cdots\oplus G_n\approx G_{\sigma(1)}\oplus\cdots\oplus G_{\sigma(n)}$.

::: pf-proof

The same argument with $\phi(g_1,\dots,g_n)\coloneqq(g_{\sigma^{-1}(1)},\dots,g_{\sigma^{-1}(n)})$: it is a homomorphism because the operation is componentwise, and it is a bijection with inverse $\phi_{\sigma^{-1}}$; the case $n=2$ and $\sigma$ the transposition is steps [](#hom){.pf-ref} to [](#surj){.pf-ref}.

:::

:::

:::

:::
