---
schema: qual/card@1
id: P-BSATZ
kind: problem
title: $\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}\le\frac{\abs{z}}{MR}$ for $\abs{f}\le M$ on $D(0,R)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Show that if $f: D(0, R) \rightarrow \CC$ is holomorphic, with $\abs{f(z)} \leq M$ for some $M>0$, then
$$
\abs{\frac{f(z)-f(0)}{M^{2}-\overline{f(0)} f(z)}} \leq \frac{\abs{z}}{M R} .
$$
:::

::: {.solution}

Assume $\abs{f(0)}<M$; the case $\abs{f(0)}=M$ is treated in the remark. Let $F(\zeta)=f(R\zeta)/M$ for $\zeta\in\DD$, let $a=F(0)=f(0)/M$, and let $\psi_a(w)=\frac{w-a}{1-\bar aw}$, an automorphism of $\DD$ because $\abs{a}<1$.

::: pf

::: {.pf-step #into}

$F$ maps $\DD$ into $\DD$.

::: pf-proof

$\abs{F}\le1$ on $\DD$. If $\abs{F(\zeta_0)}=1$ for some $\zeta_0\in\DD$, the maximum modulus principle makes $F$ constant, so $\abs{a}=1$, contrary to the assumption.

:::

:::

::: {.pf-step #schwarz}

$\abs{\psi_a(F(\zeta))}\le\abs{\zeta}$ for $\zeta\in\DD$.

::: pf-proof

By Step [](#into){.pf-ref}, $\psi_a\circ F$ is a holomorphic self-map of $\DD$, and it sends $0$ to $\psi_a(a)=0$. Apply the Schwarz lemma.

:::

:::

::: pf-qed

Let $z\in D(0,R)$ and $\zeta=z/R$. Then
$$
\psi_a(F(\zeta))=\frac{f(z)/M-f(0)/M}{1-\overline{f(0)}f(z)/M^2}=M\,\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)},
$$
where the denominator is nonzero because $\abs{\overline{f(0)}f(z)}<M^2$. Step [](#schwarz){.pf-ref} gives
$$
\abs{\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}}\le\frac{\abs{z}}{MR}.
$$

:::

:::

:::

::: remark
If $\abs{f(0)}=M$, the maximum modulus principle makes $f$ the constant $f(0)$, and the left side is $0/0$. The inequality is meaningful only when $\abs{f(0)}<M$.

The argument is due to Swaroop Hegde.
:::
