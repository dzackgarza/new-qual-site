---
schema: qual/card@1
id: P-ALGPAN11-11
kind: problem
title: When x maps to a x a^2 is a homomorphism
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Statement and choices transcribed from the ALGEBRA_REVIEW1.pdf page render; the machine extractions were garbled at this item.
---
::: {.problem}
The map $x\mapsto axa^2$ of a group $G$ into itself is a homomorphism if and only if

(A) $G$ is abelian (B) $G=\{e\}$ (C) $a=e$ (D) $a^2=a$ (E) $a^3=e$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
$\varphi(x)=axa^2$ is a homomorphism if and only if $a^3=e$.

::: pf-proof
For $x,y\in G$, $\varphi(x)\varphi(y)=axa^2\,aya^2=axa^3ya^2$ and $\varphi(xy)=axya^2$. Cancelling $ax$ on the left and $ya^2$ on the right, $\varphi(x)\varphi(y)=\varphi(xy)$ if and only if $a^3=e$. So $a^3=e$ makes $\varphi$ a homomorphism, and conversely $x=y=e$ forces $a^3=e$.
:::

:::

::: {.pf-step #s2}
None of (A)–(D) is equivalent to $a^3=e$.

::: pf-proof
In $G=\ZZ/3$ (written multiplicatively) with $a\ne e$, $a^3=e$ holds while (B), (C) and (D) fail. In $G=S_3$ with $a=e$, $a^3=e$ holds while (A) fails.
:::

:::

::: pf-qed
By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the answer is choice (E).
:::

:::

:::
