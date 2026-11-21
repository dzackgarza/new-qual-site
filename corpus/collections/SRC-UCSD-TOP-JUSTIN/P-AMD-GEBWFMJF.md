---
schema: qual/card@1
id: P-AMD-GEBWFMJF
kind: problem
title: Ham Sandwich theorem
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's proof was a skeleton of eight label-steps with empty
    proofs over nested one-sentence claims, with two pf-qed blocks inside the proof answering
    sub-questions rather than closing the theorem. It is now five proved steps: the
    parametrisation of oriented hyperplanes with the check that the mid-set is a null set (and
    the degenerate case v = 0 named); the additivity of mu over the two closed half-spaces;
    continuity of the coordinate functions by dominated convergence with the dominating function
    chi_{A_i} and the exceptional null set identified; the Borsuk--Ulam application; and the
    closing step, which now contains the argument that v* != 0 when some A_i has positive
    measure — the point the card had asserted in one line — together with the trivial case.
    Nothing mathematical was weakened, and the reference to [[P-AMD-6OJQMSOZ]] for the Borsuk--
    Ulam theorem is kept. Not claimed: a retained solution set.
---

::: {.problem}
Prove the Ham Sandwich theorem.
:::

::: {.solution}
The Ham Sandwich theorem: if $A_{1},\ldots,A_{n} \subseteq \RR^{n}$ are bounded Lebesgue measurable sets, then some affine hyperplane divides each $A_{i}$ into two pieces of equal measure. Throughout $\mu$ is Lebesgue measure on $\RR^{n}$, $S^{n} \subseteq \RR^{n+1}$ is the unit sphere, and a point $u \in S^{n}$ is written $u = (v,w)$ with $v \in \RR^{n}$ and $w \in \RR$. The collection's `provenance` is the UCSD topology qualifying compilation, and no solutions sheet accompanies it, so the argument below is the card's own; the proof of the Borsuk--Ulam theorem it uses is [[P-AMD-6OJQMSOZ]].

::: pf

::: {.pf-step #halfspaces}
For $u = (v,w) \in S^{n}$ put $H^{+}(u) \coloneqq \theset{x \in \RR^{n} \mid \langle x,v\rangle + w \ge 0}$. Then $H^{+}(-u)$ is the complementary closed half-space, and $H^{+}(u) \cap H^{+}(-u) = H(u) \coloneqq \theset{x \mid \langle x,v\rangle + w = 0}$ is an affine hyperplane, of Lebesgue measure zero.

::: pf-proof
With $-u = (-v,-w)$ one gets $H^{+}(-u) = \theset{x \mid \langle x,v\rangle + w \le 0}$, so a point lies in both exactly when $\langle x,v\rangle + w = 0$ and in one or the other always; this is the parametrisation of oriented affine hyperplanes by the sphere, the pair $\pm u$ giving the same hyperplane with the two orientations. If $v \ne 0$ the set $H(u)$ is an affine hyperplane, a translate of the proper subspace $v^{\perp}$, and such a set is a closed null set; if $v = 0$ then $u = (0,\pm1)$, $H(u)$ is empty or all of $\RR^{n}$ according to $w = \pm1$, and in either case the conclusion below holds trivially.

:::

:::

::: {.pf-step #additive}
$\mu\bigl(A_{i} \cap H^{+}(u)\bigr) + \mu\bigl(A_{i} \cap H^{+}(-u)\bigr) = \mu(A_{i})$ for every $i$ and every $u \in S^{n}$.

::: pf-proof
By step [](#halfspaces){.pf-ref} the two closed half-spaces cover $\RR^{n}$ and meet in $H(u)$, so $A_{i}$ is the union of $A_{i}\cap H^{+}(u)$ and $A_{i}\cap H^{+}(-u)$ with intersection $A_{i}\cap H(u)$, a null set. Additivity of $\mu$ over a union of two measurable sets gives the identity.

:::

:::

::: {.pf-step #continuous}
The map $F\colon S^{n} \to \RR^{n}$, $F(u) \coloneqq \bigl(\mu(A_{1}\cap H^{+}(u)), \ldots, \mu(A_{n}\cap H^{+}(u))\bigr)$, is continuous.

::: pf-proof
It suffices to treat one coordinate: $f_{i}(u) = \int_{\RR^{n}}\chi_{A_{i}}(x)\chi_{H^{+}(u)}(x)\\,d\mu(x)$. If $u_{k} \to u$ in $S^{n}$ then for every $x$ with $\langle x,v\rangle + w \ne 0$ one has $\langle x,v_{k}\rangle + w_{k} \ne 0$ for $k$ large, so $\chi_{H^{+}(u_{k})}(x) \to \chi_{H^{+}(u)}(x)$; the exceptional set is the hyperplane $H(u)$, a null set by step [](#halfspaces){.pf-ref}. The integrands are dominated in modulus by $\chi_{A_{i}}$, which is integrable because $A_{i}$ is bounded and measurable, so the dominated convergence theorem gives $f_{i}(u_{k}) \to f_{i}(u)$.

:::

:::

::: {.pf-step #borsuk}
There is $u^{*} \in S^{n}$ with $F(u^{*}) = F(-u^{*})$, hence $\mu\bigl(A_{i}\cap H^{+}(u^{*})\bigr) = \tfrac12\mu(A_{i})$ for every $i$.

::: pf-proof
$F$ is continuous by step [](#continuous){.pf-ref} and $S^{n} \subseteq \RR^{n+1}$ is the sphere of dimension $n$, so the Borsuk--Ulam theorem — every continuous $S^{n} \to \RR^{n}$ identifies a pair of antipodal points — gives $u^{*}$ with $F(u^{*}) = F(-u^{*})$. Reading this coordinatewise and substituting into step [](#additive){.pf-ref} gives $2\mu(A_{i}\cap H^{+}(u^{*})) = \mu(A_{i})$ for each $i$.

:::

:::

::: pf-step
$H(u^{*})$ is an affine hyperplane bisecting every $A_{i}$: $\mu\bigl(A_{i} \cap H^{+}(u^{*})\bigr) = \mu\bigl(A_{i} \cap H^{+}(-u^{*})\bigr) = \tfrac12\mu(A_{i})$.

::: pf-proof
If some $\mu(A_{i}) > 0$ then $u^{*} \ne (0,\pm1)$, because for $u = (0,1)$ the half-space $H^{+}(u)$ is all of $\RR^{n}$ while $H^{+}(-u) = \varnothing$, so $f_{i}(u) = \mu(A_{i}) \ne 0 = f_{i}(-u)$ and $F(u) \ne F(-u)$; thus $v^{*} \ne 0$ and $H(u^{*})$ is a genuine affine hyperplane by step [](#halfspaces){.pf-ref}. Step [](#borsuk){.pf-ref} then gives the two halves equal measure $\tfrac12\mu(A_{i})$ each. If instead every $\mu(A_{i}) = 0$ then any hyperplane divides each $A_{i}$ into two null pieces, so the conclusion holds trivially.

:::

:::

:::
:::
