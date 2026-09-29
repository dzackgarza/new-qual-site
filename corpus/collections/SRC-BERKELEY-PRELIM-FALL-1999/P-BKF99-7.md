---
schema: qual/card@1
id: P-BKF99-7
kind: problem
title: A finite transitive group action has a derangement
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Double-counted fixed-point pairs to show that a transitive action has
    average fixed-point count one. Since the identity fixes at least two
    points, some group element must fix none.
---

::: {.problem}
Let a finite group $G$ act transitively on a set $X$ with $|X|\ge2$. Prove that some element $g\in G$ acts on $X$ without fixed points.
:::

::: {.solution}

For $g\in G$, let
$$
\operatorname{Fix}(g)=\{x\in X:g x=x\}.
$$

::: pf

::: {.pf-step #double-count-fixed-points}
$$
\sum_{g\in G}\abs{\operatorname{Fix}(g)}=\abs{G}.
$$

::: pf-proof
Count the set
$$
S=\{(g,x)\in G\times X:g x=x\}
$$
in two ways. Counting first by $g$ gives
$$
\abs{S}=\sum_{g\in G}\abs{\operatorname{Fix}(g)}.
$$
Counting first by $x$ gives
$$
\abs{S}=\sum_{x\in X}\abs{G_x},
$$
where $G_x$ is the stabilizer of $x$. Transitivity implies that every orbit
has size $\abs{X}$, so orbit-stabilizer gives
$$
\abs{G_x}=\frac{\abs{G}}{\abs{X}}
$$
for every $x\in X$. Therefore
$$
\abs{S}
=
\abs{X}\frac{\abs{G}}{\abs{X}}
=
\abs{G}.
$$
:::

:::

::: {.pf-step #element-with-no-fixed-point}
Some element $g\in G$ satisfies
$$
\abs{\operatorname{Fix}(g)}=0.
$$

::: pf-proof
Suppose instead that every element of $G$ fixed at least one point. The
identity element fixes every point, so
$$
\abs{\operatorname{Fix}(e)}
=
\abs{X}
\geq2.
$$
Hence
$$
\sum_{g\in G}\abs{\operatorname{Fix}(g)}
\geq
2+(\abs{G}-1)
=
\abs{G}+1,
$$
contradicting step [](#double-count-fixed-points){.pf-ref}. Thus at least one element has no fixed point.
:::

:::

::: pf-qed
The element supplied by step [](#element-with-no-fixed-point){.pf-ref} is the required derangement.
:::

:::

:::
