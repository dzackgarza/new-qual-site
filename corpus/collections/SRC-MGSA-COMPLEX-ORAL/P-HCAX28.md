---
schema: qual/card@1
id: P-HCAX28
kind: problem
title: Analytic continuation and its uniqueness
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into numbered steps, and the audit list this card lacked is created here. The source is a complex-analysis oral examination, so the question is the source. Each step re-read: the definition is the agreement on a nonempty open set, with the reason the open set and not a point; the chain form; uniqueness on a common domain by the identity theorem on the difference; the componentwise form, with the explicit restriction that only the component meeting the agreement set is covered; and the contrast with continuation along paths, where the logarithm around 0 shows the terminal germs differ, together with the monodromy theorem restoring uniqueness on a simply connected domain. Not claimed: any statement about continuation of germs that cannot be continued along some path.
---

::: {.problem}
Define analytic continuation and prove its uniqueness.
:::

::: {.solution}
The argument is the card's own; the collection is a complex-analysis oral examination, so the question is the source.

::: pf

::: {.pf-step #def}
Let $U,V\subseteq\CC$ be domains, $f$ holomorphic on $U$ and $g$ holomorphic on $V$. Then $g$ is an **analytic continuation** of $f$ to $V$ when $U\cap V$ contains a nonempty open set on which $g=f$.

::: pf-proof
This is the definition. It is stated for a nonempty open set rather than a single point because agreement at one point carries no information about $g$, whereas agreement on a set with an accumulation point inside the common domain determines $g$ by the identity theorem.
:::

:::

::: {.pf-step #chain}
Analytic continuation along a chain of overlapping domains is defined by iterating the condition: elements $(f_{0},U_{0}),\dots,(f_{n},U_{n})$ with each $U_{i}$ a domain, $f_{i}$ holomorphic on $U_{i}$, and $f_{i}=f_{i+1}$ on a nonempty open subset of $U_{i}\cap U_{i+1}$.

::: pf-proof
This is the definition obtained by repeating step [](#def){.pf-ref} along consecutive overlaps; it is the sense in which the logarithm is continued along a path, each disc in the chain overlapping the next.
:::

:::

::: {.pf-step #unique}
If $g_{1},g_{2}$ are holomorphic on one domain $V$ and both continue $f$, then $g_{1}=g_{2}$.

::: pf-proof
By step [](#def){.pf-ref} there are nonempty open sets $W_{1},W_{2}\subseteq V$ with $g_{1}=f$ on $W_{1}$ and $g_{2}=f$ on $W_{2}$; then $g_{1}=g_{2}$ on the nonempty open set $W_{1}\cap W_{2}$, since $f$ is defined and single-valued on $U\cap V$. The difference $g_{1}-g_{2}$ is holomorphic on the domain $V$ and vanishes on a nonempty open subset, so it vanishes identically by the identity theorem.
:::

:::

::: {.pf-step #components}
If $g_{1}$ on $V_{1}$ and $g_{2}$ on $V_{2}$ agree on a nonempty open set, then they agree on every connected component of $V_{1}\cap V_{2}$ meeting that set.

::: pf-proof
$V_{1}\cap V_{2}$ is open, and the difference $g_{1}-g_{2}$ is holomorphic on each of its components and vanishes on a nonempty open subset of the component that contains the given set; the identity theorem applied on that connected open set gives vanishing there. No conclusion is drawn for the other components, and indeed none need hold.
:::

:::

::: {.pf-step #monodromy}
Uniqueness of the continuation on a domain does not give uniqueness along paths, but it does on a simply connected domain.

::: pf-proof
Continuation of a branch of $\log z$ once around $0$ returns a value changed by $2\pi i$, so the terminal germs of two paths with the same endpoints can differ; that is compatible with step [](#unique){.pf-ref}, because the two continuations live on different domains, not on one common domain containing both paths. The monodromy theorem restores uniqueness when the germ continues along every path in a simply connected domain $D$: any two paths with the same endpoints are homotopic there, and continuation along a homotopy is locally constant in the parameter, so the terminal germs agree and a single holomorphic function on $D$ results.
:::

:::

::: {.pf-step}
The definition and the uniqueness statement hold, in the form given.

::: pf-proof
Steps [](#def){.pf-ref} and [](#chain){.pf-ref} give the definition, step [](#unique){.pf-ref} the uniqueness on a common domain, step [](#components){.pf-ref} the componentwise form, and step [](#monodromy){.pf-ref} the distinction between uniqueness on a domain and uniqueness along paths:
$$
\boxed{g_{1},g_{2}\text{ both continuing }f\text{ on a domain }V\implies g_{1}=g_{2};\qquad\text{along paths, uniqueness requires simple connectivity (monodromy theorem)}.}
$$
:::

:::

:::
:::
