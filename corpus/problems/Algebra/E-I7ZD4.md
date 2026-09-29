---
schema: qual/card@1
id: E-I7ZD4
kind: problem
title: Cayley-Hamilton via Jordan canonical form
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Prove Cayley-Hamilton using the JCF.
:::

::: {.solution}
Let $A\in\Endo_k(V)$ with $V$ finite-dimensional.

::: pf

::: {.pf-step #reduce-to-algebraic-closure}
It is enough to prove the identity after extending scalars to an algebraic closure $\overline{k}$.

::: pf-proof
Set
\[
\overline{V}=V\otimes_k\overline{k},
\qquad
\overline{A}=A\otimes1.
\]
The characteristic polynomial is unchanged by scalar extension, so $\chi_{\overline A}(t)=\chi_A(t)$ viewed in $\overline{k}[t]$. Moreover, the natural map
\[
\Endo_k(V)\longrightarrow\Endo_{\overline{k}}(\overline V),
\qquad T\longmapsto T\otimes1,
\]
is injective. Hence if $\chi_A(A)\otimes1=0$, then $\chi_A(A)=0$ already over $k$.
:::

:::

::: {.pf-step #jordan-form-of-a}
Over $\overline{k}$, choose a basis in which $\overline A$ has Jordan form
\[
J=\bigoplus_r J_{m_r}(\lambda_r).
\]

::: pf-proof
The characteristic polynomial splits over $\overline{k}$, so the Jordan canonical form theorem applies. Similarity preserves polynomial evaluation: if $\overline A=PJP^{-1}$, then
\[
p(\overline A)=Pp(J)P^{-1}
\]
for every polynomial $p$.
:::

:::

::: {.pf-step #block-nilpotent}
On a Jordan block $J_m(\lambda)$ one has
\[
(J_m(\lambda)-\lambda I)^m=0.
\]

::: pf-proof
Write
\[
J_m(\lambda)=\lambda I+N,
\]
where $N$ has $1$ on the superdiagonal and $0$ elsewhere. The matrix $N$ shifts each basis vector at most one step along the Jordan chain, so $N^m=0$. Thus
\[
(J_m(\lambda)-\lambda I)^m=N^m=0.
\]
:::

:::

::: {.pf-step #char-poly-kills-jordan-blocks}
The characteristic polynomial $\chi_J$ annihilates every Jordan block of $J$.

::: pf-proof
For each eigenvalue $\lambda$, let $a_\lambda$ be its algebraic multiplicity. Then
\[
\chi_J(t)=\prod_\lambda(t-\lambda)^{a_\lambda}.
\]
If $J_m(\lambda)$ is one of the blocks, then $m\le a_\lambda$. Hence the factor
\[
(J_m(\lambda)-\lambda I)^{a_\lambda}
\]
is zero by step [](#block-nilpotent){.pf-ref}. Since all factors in the polynomial $\chi_J(J_m(\lambda))$ commute, this gives
\[
\chi_J(J_m(\lambda))=0.
\]
Therefore $\chi_J(J)=0$ block by block.
:::

:::

::: pf-step
Hence $\chi_A(A)=0$.

::: pf-proof
By steps [](#jordan-form-of-a){.pf-ref} and [](#char-poly-kills-jordan-blocks){.pf-ref},
\[
\chi_{\overline A}(\overline A)=0.
\]
Using step [](#reduce-to-algebraic-closure){.pf-ref},
\[
\chi_A(A)\otimes1=0
\]
implies $\chi_A(A)=0$ over the original field $k$.
:::

:::

:::

:::
