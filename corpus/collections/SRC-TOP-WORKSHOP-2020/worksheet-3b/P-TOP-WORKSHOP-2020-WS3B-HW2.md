---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-HW2
kind: problem
title: Deck transformations of the universal cover of $S^1$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the definition, the integer translations exhibited as
    deck transformations, and the converse that they are all of them. No retained solution set covers this
    exercise (the collection retains the worksheets, not solutions), so the argument is the card's own; the
    fibre $p^{-1}(1)=ZZ$ and the lift-uniqueness step were checked for this pass.
---

::: {.problem}
What is a deck transformation?
Describe the deck transformations from one of the universal covers above.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. A deck transformation of a covering $p:E\to B$ is a homeomorphism $\phi:E\to E$ with $p\circ\phi=p$, so it permutes each fibre $p^{-1}(b)$ while preserving the projection. The universal cover used is $p:\RR\to S^{1}$, $p(t)=e^{2\pi i t}$.

::: pf

::: {.pf-step #definition}
A deck transformation of $p:E\to B$ is a homeomorphism $\phi:E\to E$ with $p\circ\phi=p$; equivalently, it carries each fibre $p^{-1}(b)$ into itself.

::: pf-proof
$p\circ\phi=p$ says that $\phi(x)$ lies in the fibre of $p(x)$, for every $x\in E$; since $\phi$ is a homeomorphism it maps each fibre bijectively onto itself. The condition is not automatic for an arbitrary map, which is why it is part of the definition.
:::

:::

::: {.pf-step #translations}
For every $n\in\ZZ$ the translation $T_{n}(t)=t+n$ is a deck transformation of $p$.

::: pf-proof
$T_{n}$ is a homeomorphism of $\RR$ with inverse $T_{-n}$. And $p(T_{n}(t))=e^{2\pi i(t+n)}=e^{2\pi i t}e^{2\pi i n}=e^{2\pi i t}=p(t)$, because $e^{2\pi i n}=1$ for integers $n$. So $p\circ T_{n}=p$.
:::

:::

::: {.pf-step}
Every deck transformation of $p$ is some $T_{n}$; hence $\operatorname{Deck}(\RR/S^{1})\cong\ZZ$.

::: pf-proof
Let $\phi$ be a deck transformation. Since $\phi$ preserves the projection, $p(\phi(0))=p(0)=1$, so $\phi(0)\in p^{-1}(1)=\{t\in\RR\mid e^{2\pi i t}=1\}=\ZZ$; write $n=\phi(0)$. Now $\phi$ and $T_{n}$ are both lifts of $p$ to $\RR$ — that is, $p\circ\phi=p\circ T_{n}$ — and they agree at the point $0$, where both take the value $n$. The domain $\RR$ is connected, so two lifts of a covering that agree at one point coincide; hence $\phi=T_{n}$. Together with step [](#translations){.pf-ref} this gives a bijection $\ZZ\to\operatorname{Deck}(\RR/S^{1})$, $n\mapsto T_{n}$, and composition of translations adds the indices, so it is an isomorphism of groups.
:::

:::

:::
:::
