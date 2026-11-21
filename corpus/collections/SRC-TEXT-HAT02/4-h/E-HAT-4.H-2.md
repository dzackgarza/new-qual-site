---
schema: qual/card@1
id: E-HAT-4.H-2
kind: problem
title: "Cofibrations are preserved by pushout"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.H, printed p. 458, with the homotopy extension property
    of §0.4 on printed p. 14. The argument was right and is kept: from $u\colon P\to Y$ and
    $H\colon B\times I\to Y$ with $H(b,0)=u(j(b))$ one forms $u\circ q$ and
    $H\circ(f\times\mathrm{id})$, whose initial condition on $A$ holds because $jf=qi$; the
    homotopy extension property of $i$ extends it to $H_X$ on $X\times I$; and $P\times I$ is the
    pushout of $B\times I$ and $X\times I$ along $A\times I$ because $I$ is compact Hausdorff, so
    $H$ and $H_X$ paste. Rewritten from a nest of `pf` blocks whose proofs were noun phrases
    ('test data for the Homotopy Extension Property', 'composition of continuous maps',
    'definition of cofibration', 'universal property of pushouts', 'Gluing Lemma for pushouts',
    'evaluation at $t=0$') and which ended in a 'Conclusion ... Q.E.D.' step proved by naming
    three labels. Four steps now, each carrying its argument. Not claimed: a certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher §4.H Exercise 2, the homotopy extension property of Chapter 0, Proposition
    4H.1 and Proposition A.17. The argument is correct and is kept: the initial condition on $A$
    holds by $jf=qi$, the homotopy extension property of $i$ extends the data to $X\times I$, the
    product with $I$ preserves the pushout, and the two maps paste. Repairs are in the citations and
    in one omitted check: the product-with-$I$ step now cites Proposition A.17, which is the
    statement that $f\times\id$ is a quotient map for locally compact $Z$, instead of
    asserting it; the reference to §0.4 is replaced by §4.H with Proposition 4H.1, which is where
    Hatcher defines a cofibration as an inclusion with the homotopy extension property; and the
    injectivity of $j\colon B\to P$, which the conclusion needs and the card had taken for granted,
    is now proved from the pushout description. No statement changed. Not checked: no certificate.
---

::: {.problem}
Consider a pushout diagram as at the right, where $B\sqcup_f X$ is $B$ with $X$ attached along $A$ via $f$.
Show that if $A \hookrightarrow X$ is a cofibration, so is $B \hookrightarrow B\sqcup_f X$.
:::

::: {.solution}
Write $P=B\sqcup_fX$ for the pushout, with inclusions $j\colon B\to P$ and $q\colon X\to P$, so that $j f=q i$ for $i\colon A\hookrightarrow X$. By §4.H and Proposition 4H.1 a cofibration may be taken to be an inclusion with the homotopy extension property, so it is enough to produce, for every space $Y$, every $u\colon P\to Y$ and every homotopy $H\colon B\times I\to Y$ with $H(b,0)=u(j(b))$, a homotopy $\widetilde H\colon P\times I\to Y$ with $\widetilde H(p,0)=u(p)$ that extends $H$ on $B\times I$. The exercise is Exercise 2 of §4.H.

::: pf

::: {.pf-step #s1}

The pair $\bigl(u\circ q,\; H\circ(f\times\mathrm{id}_I)\bigr)$ is admissible data for the homotopy extension property of $i\colon A\hookrightarrow X$.

::: pf-proof

For $a\in A$ one has $(H\circ(f\times\mathrm{id}_I))(a,0)=H(f(a),0)=u(j(f(a)))=u(q(i(a)))=(u\circ q)(i(a))$, using the pushout relation $jf=qi$; this is exactly the initial condition required of a homotopy on $A\times I$ extending the map $u\circ q$ on $X$.

:::

:::

::: {.pf-step #s2}

There is a homotopy $H_X\colon X\times I\to Y$ with $H_X(x,0)=u(q(x))$ for all $x$ and $H_X(i(a),t)=H(f(a),t)$ for all $a$, $t$.

::: pf-proof

This is the homotopy extension property of the cofibration $i\colon A\hookrightarrow X$, applied to the data of the previous step.

:::

:::

::: {.pf-step #s3}

$H$ and $H_X$ paste to a continuous map $\widetilde H\colon P\times I\to Y$.

::: pf-proof

Proposition A.17 states that $f\times\id\colon Y\times Z\to Z'\times Z$ is a quotient map whenever $f\colon Y\to Y'$ is a quotient map and $Z$ is locally compact; with $Z=I$ this says that taking the product with $I$ preserves the pushout, so $P\times I$ is the pushout of $B\times I$ and $X\times I$ along $A\times I$ under $f\times\mathrm{id}_I$ and $i\times\mathrm{id}_I$. The two maps $H\colon B\times I\to Y$ and $H_X\colon X\times I\to Y$ agree on $A\times I$ by the previous step, so the universal property of the pushout yields the map $\widetilde H$.

:::

:::

::: {.pf-step #s4}

$\widetilde H$ extends $H$ and satisfies $\widetilde H(p,0)=u(p)$ for all $p\in P$, so $j\colon B\to P$ has the homotopy extension property and is a cofibration.

::: pf-proof

On $B\times I$ the map $\widetilde H$ is $H$ by construction. At $t=0$ it equals $u$ on each of the two pieces: $\widetilde H(j(b),0)=H(b,0)=u(j(b))$, and $\widetilde H(q(x),0)=H_X(x,0)=u(q(x))$; since $P$ is the union of $j(B)$ and $q(X)$, this is $\widetilde H(\cdot,0)=u$. The homotopy extension property is therefore verified for $j$, and $j$ is an inclusion: a point of $B$ is identified in the pushout only with the points of $X$ that map to it under $f$, and those are identified with each other, so distinct points of $B$ stay distinct. By §4.H that makes $j$ a cofibration.

:::

:::

:::

:::
