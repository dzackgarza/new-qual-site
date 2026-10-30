---
schema: qual/card@1
id: P-CAEXAMPREP-16
kind: problem
title: A holomorphic function cannot be locally constant away from a noncritical point
classification: {areas: [complex-analysis], topics: [Identity Theorem]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let $f$ be analytic on a domain $A$, and let $z_1,z_2\in A$.
Assume $f'(z_1)\ne0$.
Show that $f$ is not constant on any neighborhood of $z_2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f$ were constant on a neighborhood of $z_2$, then there would be a constant $c\in\CC$ and an open disk $B(z_2,r)\subseteq A$ on which $f-c$ vanishes identically.


::: pf-proof

Suppose that $f$ is constant on some neighborhood $U\subseteq A$ of $z_2$, with value $c$. Since $U$ is open and contains $z_2$, there exists $r>0$ such that $B(z_2,r)\subseteq U$. Hence $f(z)-c=0$ for every $z\in B(z_2,r)$.

:::

:::

::: {.pf-step #s1-2}

Under the assumption of step [](#s1-1){.pf-ref}, $f$ is constant on all of $A$.


::: pf-proof

The function $g=f-c$ is analytic on the domain $A$. By step [](#s1-1){.pf-ref}, its zero set contains the disk $B(z_2,r)$, so in particular it has the accumulation point $z_2\in A$. The identity theorem therefore gives $g\equiv0$ on the connected set $A$. Thus $f\equiv c$ on $A$.

:::

:::

::: {.pf-step #s1-3}

The conclusion of step [](#s1-2){.pf-ref} contradicts $f'(z_1)\ne0$.


::: pf-proof

If $f$ is constant on $A$, then $f'(z)=0$ for every $z\in A$. In particular $f'(z_1)=0$, contradicting the hypothesis.

:::

:::

::: {.pf-step #s1-4}

Therefore $f$ is not constant on any neighborhood of $z_2$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show that the existence of any neighborhood of $z_2$ on which $f$ is constant leads to a contradiction.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
