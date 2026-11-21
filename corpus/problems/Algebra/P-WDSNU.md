---
schema: qual/card@1
id: P-WDSNU
kind: problem
title: Regular representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Group Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the regular representation of a finite group $G$?
State its character, decomposition into irreducible representations, and connection to the group algebra $\CC[G]$.
:::

::: {.solution}

No retained solution set covers this question, and it asks for a definition and its structure: the representation, its character, the multiplicities and the algebra isomorphism are separate steps, with the multiplicities computed rather than asserted.

Let $G$ be a finite group and $\CC[G]$ its group algebra with basis $(e_{h})_{h\in G}$.

::: pf

::: {.pf-step #definition}
The left regular representation is the action of $G$ on $\CC[G]$ by left multiplication, $g\cdot e_{h}=e_{gh}$, extended linearly; it has dimension $\cardinality{G}$ and is faithful.

::: pf-proof
Left multiplication by $g$ permutes the basis, so it is a linear automorphism of $\CC[G]$ and $g\mapsto(\cdot g\cdot)$ is a homomorphism into $GL_{\cardinality{G}}(\CC)$; the dimension is $\cardinality{G}$ by definition of the basis. It is faithful because $g\cdot e_{1}=e_{g}\ne e_{1}$ for $g\ne1$.
:::

:::

::: {.pf-step #character}
$\chi_{\mathrm{reg}}(g)=\cardinality{G}$ if $g=1$ and $0$ otherwise.

::: pf-proof
The character is the trace of $g$ acting on the basis: the basis vector $e_{h}$ is fixed by left multiplication by $g$ exactly when $gh=h$, that is $g=1$. So for $g\ne1$ the matrix of the action has zero diagonal, and for $g=1$ it is the identity with trace $\cardinality{G}$.
:::

:::

::: {.pf-step #multiplicities}
If $V_{1},\dots,V_{r}$ are the irreducible complex representations with characters $\chi_{i}$ and dimensions $d_{i}$, then $\CC[G]\cong\bigoplus_{i}V_{i}^{\oplus d_{i}}$ as $G$-modules.

::: pf-proof
The multiplicity of $V_{i}$ in the regular representation is $\langle\chi_{\mathrm{reg}},\chi_{i}\rangle=\frac{1}{\cardinality{G}}\sum_{g}\chi_{\mathrm{reg}}(g)\overline{\chi_{i}(g)}=\frac{1}{\cardinality{G}}\cardinality{G}\overline{\chi_{i}(1)}=d_{i}$, using step [](#character){.pf-ref} and $\chi_{i}(1)=d_{i}$; complete reducibility of finite-dimensional complex representations gives the direct sum decomposition.
:::

:::

::: {.pf-step #algebra}
As algebras, $\CC[G]\cong\bigoplus_{i}\operatorname{End}(V_{i})$, and $\dim\CC[G]=\sum_{i}d_{i}^{2}$.

::: pf-proof
The group algebra is semisimple (Maschke's theorem, as $\CC$ has characteristic $0$), so by Wedderburn's structure theorem it is a product of full matrix algebras over $\CC$; the only simple quotient occurring is $\operatorname{End}(V_{i})$ for each irreducible $V_{i}$, acting on the $d_{i}$-dimensional space $V_{i}$, and comparing the description with step [](#multiplicities){.pf-ref} gives $\CC[G]\cong\bigoplus_{i}\operatorname{End}(V_{i})$. Taking dimensions gives $\cardinality{G}=\dim\CC[G]=\sum_{i}\dim\operatorname{End}(V_{i})=\sum_{i}d_{i}^{2}$.
:::

:::

::: {.pf-qed}
The regular representation is the left multiplication action of step [](#definition){.pf-ref}, with character of step [](#character){.pf-ref}, decomposition of step [](#multiplicities){.pf-ref} into each irreducible with multiplicity its dimension, and algebra structure of step [](#algebra){.pf-ref}; a function on $G$ corresponds to an element of $\CC[G]$, and the Fourier transform is the resulting identification of $\CC[G]$ with $\bigoplus_{i}\operatorname{End}(V_{i})$.
:::

:::

:::
