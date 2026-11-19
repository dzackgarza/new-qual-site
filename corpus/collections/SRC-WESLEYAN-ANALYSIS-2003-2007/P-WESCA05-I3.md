---
schema: qual/card@1
id: P-WESCA05-I3
kind: problem
title: "State the global Cauchy Theorem"
classification:
  areas: [complex-analysis]
  topics:
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 3 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's pf block held a single step restating the theorem and
    then a pf-qed whose entire content was 'Step ... is the requested statement of the theorem',
    which STYLE-08 forbids: a qed sentence may not merely report that the earlier steps answer
    the question. The statement is unchanged and stays the answer. Added the definition of a
    cycle and of homologous vanishing, which the statement uses, the explanation of what the
    theorem says beyond the classical form, and the derivation of the simply connected special
    case from the connectedness of the complement in the sphere together with the constancy of
    the winding number on components of the complement of the cycle. Not claimed: a retained
    solution set; the collection's provenance is the examination compilation.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 25. The card had cited neither the
    examination nor a page; it now names both, and the statement was compared with the
    printed item and left unchanged.

---

::: {.problem}
State the global Cauchy Theorem.
:::

::: {.solution}
The item is Section 1 item 3 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan University, Summer 2005 (statement of the global Cauchy theorem), on PDF p. 25 of the retained scan
assets/attachments/analysis_2003-2007.pdf.

The examination asks for the statement, so the card's answer is the statement itself, together with the definitions that make it intelligible and the special case that is usually quoted. Throughout $U \subseteq \CC$ is open, $f\colon U \to \CC$ is analytic, a cycle in $U$ is a finite formal sum $\Gamma = \sum_{j}n_{j}\gamma_{j}$ of closed paths in $U$ with integer coefficients, and $\operatorname{Ind}(\Gamma,w) \coloneqq \frac{1}{2\pi i}\int_{\Gamma}\frac{d\zeta}{\zeta - w}$ is the winding number of $\Gamma$ about $w \notin \Gamma$. The collection's `provenance` is the Wesleyan analysis compilation, and no solutions sheet accompanies it.

::: pf

::: {.pf-step #homologous}
$\Gamma$ is homologous to zero in $U$ when $\operatorname{Ind}(\Gamma, w) = 0$ for every $w \in \CC \setminus U$.

::: pf-proof
This is the definition of the hypothesis in the theorem; the winding number is defined for $w$ outside the support of $\Gamma$ because the integrand $1/(\zeta - w)$ is then continuous and piecewise smooth along $\Gamma$, and it is an integer because it is the integral of a closed form along a cycle.

:::

:::

::: {.pf-step #statement}
Global Cauchy theorem: if $U$ is open, $f$ analytic on $U$, and $\Gamma$ a cycle in $U$ homologous to zero in $U$, then $\boxed{\int_{\Gamma}f(z)\\,dz = 0}$.

::: pf-proof
This is the statement asked for. Its content beyond the classical form is that no hypothesis of simple connectivity on $U$ is needed: the vanishing is required not of every cycle but only of those whose winding numbers vanish at every point the domain omits, which is a condition on $\Gamma$ relative to $U$ alone and does not involve $f$.

:::

:::

::: {.pf-step #simply-connected}
If $U$ is simply connected then every cycle in $U$ is homologous to zero in $U$, so the classical Cauchy theorem for simply connected domains follows from the global one.

::: pf-proof
For a simply connected open $U \subseteq \CC$ the complement in the sphere, $\hat{\CC}\setminus U$, is connected. The function $w \mapsto \operatorname{Ind}(\Gamma,w)$ is constant on each component of $\CC\setminus \operatorname{supp}\Gamma$, and it vanishes on the unbounded component because there the integrand is $O(1/\abs{\zeta}^{2})$; as $\hat{\CC}\setminus U$ is connected and meets that unbounded component, the winding number vanishes on all of $\CC\setminus U$.

:::

:::

::: pf-step
The statement is the one of step [](#statement){.pf-ref}: analyticity on $U$ plus homological vanishing of the cycle in $U$ forces $\int_{\Gamma}f = 0$, and simple connectivity of $U$ is the special case in which the homological hypothesis is automatic.

::: pf-proof
Step [](#homologous){.pf-ref} fixes the meaning of 'homologous to zero', step [](#statement){.pf-ref} is the theorem, and step [](#simply-connected){.pf-ref} identifies the special case usually quoted, so the statement is complete and its hypotheses are all accounted for.

:::

:::

:::
:::
