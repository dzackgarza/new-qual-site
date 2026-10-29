---
schema: qual/card@1
id: P-WESCA10-II2
kind: problem
title: 'Residues of products at simple poles and a weighted residue formula'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
(a) Suppose $f$ has a simple pole at $a$ and $g$ is analytic near $a$.
Prove
$$
\operatorname{Res}(a,fg)=g(a)\operatorname{Res}(a,f).
$$

(b) Let $D$ be a domain, let $f$ be analytic in $D$ except for simple poles $a_1,\dots,a_n$, and let $g$ be analytic in $D$.
Prove that for every piecewise smooth closed path $\gamma$ avoiding the poles and null-homologous in $D$,
$$
\frac1{2\pi i}\int_\gamma f(z)g(z)\,dz
=\sum_{k=1}^n n(\gamma,a_k)g(a_k)\operatorname{Res}(a_k,f).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f$ has a simple pole at $a$ and $g$ is analytic near $a$, then
$$
\boxed{\operatorname{Res}(a,fg)
=g(a)\operatorname{Res}(a,f)}.
$$


::: pf-proof

Since $f$ has a simple pole at $a$, there is a function $h$ analytic near $a$
such that
$$
f(z)=\frac{c_{-1}}{z-a}+h(z),
\qquad
c_{-1}=\operatorname{Res}(a,f).
$$
Since $g$ is analytic near $a$, there is a function $q$ analytic near $a$
such that
$$
g(z)=g(a)+(z-a)q(z).
$$
Therefore
$$
f(z)g(z)
=\frac{c_{-1}g(a)}{z-a}
+c_{-1}q(z)+h(z)g(z).
$$
The final two terms are analytic near $a$, so the coefficient of
$(z-a)^{-1}$ is $c_{-1}g(a)$. This is exactly the residue of $fg$ at $a$.

:::

:::

::: {.pf-step #s1-2}

Under the hypotheses of part (b),
$$
\boxed{
\frac1{2\pi i}\int_\gamma f(z)g(z)\,dz
=\sum_{k=1}^n n(\gamma,a_k)g(a_k)\operatorname{Res}(a_k,f)
}.
$$


::: pf-proof

The product $fg$ is analytic on $D\setminus\{a_1,\dots,a_n\}$, and its only
possible singularities in $D$ are the points $a_k$. Since $\gamma$ is
null-homologous in $D$ and avoids these points, the residue theorem gives
$$
\frac1{2\pi i}\int_\gamma f(z)g(z)\,dz
=\sum_{k=1}^n
n(\gamma,a_k)\operatorname{Res}(a_k,fg).
$$
Applying step [](#s1-1){.pf-ref} at each $a_k$ gives
$$
\operatorname{Res}(a_k,fg)
=g(a_k)\operatorname{Res}(a_k,f),
$$
and substitution yields the displayed formula.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-2){.pf-ref} proves part (b).

:::

:::

:::
