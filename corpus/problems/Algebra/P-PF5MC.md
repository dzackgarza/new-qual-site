---
schema: qual/card@1
id: P-PF5MC
kind: problem
title: Galois group of $x^5-2$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Calculate the Galois group of $x^5 - 2$." without naming the base field; the statement now names $\QQ$, the field the solution uses.'
---

::: {.problem}
Calculate the Galois group of $x^5 - 2$ over $\QQ$.
:::

::: {.solution}
Let $f(x)=x^5-2$, let $\alpha=\sqrt[5]{2}\in\RR$, let $\zeta=e^{2\pi i/5}$, and let $K$ be the splitting field of $f$ over $\QQ$.

::: pf

::: pf-step
$f$ is irreducible over $\QQ$, so $[\QQ(\alpha):\QQ]=5$.

::: pf-proof
$f$ is monic and Eisenstein at $p=2$, so it is irreducible over $\QQ$ by Eisenstein's criterion. Hence $f$ is the minimal polynomial of $\alpha$.
:::

:::

::: pf-step
$K=\QQ(\alpha,\zeta)$ and $[\QQ(\zeta):\QQ]=4$.

::: pf-proof
The roots of $f$ are $\zeta^k\alpha$ for $k=0,\ldots,4$. So $K$ contains $\alpha$ and $\zeta=(\zeta\alpha)/\alpha$, and conversely $\QQ(\alpha,\zeta)$ contains every root. The minimal polynomial of $\zeta$ is the cyclotomic polynomial $\Phi_5(x)=x^4+x^3+x^2+x+1$, which is irreducible of degree $4$.
:::

:::

::: {.pf-step #degree}
$[K:\QQ]=20$, $[K:\QQ(\zeta)]=5$, and $[K:\QQ(\alpha)]=4$.

::: pf-proof
Both $5$ and $4$ divide $[K:\QQ]$ by the tower law, so $20\mid[K:\QQ]$. Also $[K:\QQ]\le[\QQ(\zeta):\QQ]\cdot\deg f=20$. The remaining degrees follow from the tower law.
:::

:::

::: {.pf-step #sigma}
There is $\sigma\in\Gal(K/\QQ(\zeta))$ with $\sigma(\alpha)=\zeta\alpha$, and $N\coloneqq\langle\sigma\rangle=\Gal(K/\QQ(\zeta))\cong C_5$ is normal in $\Gal(K/\QQ)$.

::: pf-proof
By step [](#degree){.pf-ref}, $f$ is irreducible over $\QQ(\zeta)$, so $\Gal(K/\QQ(\zeta))$ acts transitively on the roots of $f$, and some $\sigma$ sends $\alpha$ to $\zeta\alpha$. Then $\sigma^k(\alpha)=\zeta^k\alpha$, so $\sigma$ has order $5=\abs{\Gal(K/\QQ(\zeta))}$. The group $\Gal(K/\QQ(\zeta))$ is the kernel of restriction $\Gal(K/\QQ)\to\Gal(\QQ(\zeta)/\QQ)$, so it is normal.
:::

:::

::: {.pf-step #tau}
There is $\tau\in\Gal(K/\QQ(\alpha))$ with $\tau(\zeta)=\zeta^2$, and $H\coloneqq\langle\tau\rangle\cong C_4$.

::: pf-proof
By step [](#degree){.pf-ref}, $\Phi_5$ is irreducible over $\QQ(\alpha)$, so some $\tau$ fixing $\alpha$ sends $\zeta$ to $\zeta^2$. Since $2$ has order $4$ modulo $5$, $\tau^k(\zeta)=\zeta^{2^k}$ shows that $\tau$ has order $4$.
:::

:::

::: {.pf-step #relation}
$\tau\sigma\tau^{-1}=\sigma^2$.

::: pf-proof
Both sides fix $\zeta$, since $N$ is normal and fixes $\zeta$. On $\alpha$,
$$\tau\sigma\tau^{-1}(\alpha)=\tau\sigma(\alpha)=\tau(\zeta\alpha)=\zeta^2\alpha=\sigma^2(\alpha).$$
An automorphism of $K$ is determined by its values on $\alpha$ and $\zeta$.
:::

:::

::: pf-step
$\Gal(K/\QQ)\cong\boxed{C_5\rtimes C_4=\langle\sigma,\tau\mid\sigma^5=\tau^4=1,\ \tau\sigma\tau^{-1}=\sigma^2\rangle}$, the Frobenius group of order $20$, isomorphic to $\operatorname{AGL}_1(\FF_5)$.

::: pf-proof
By steps [](#sigma){.pf-ref} and [](#tau){.pf-ref}, $N\cap H=1$ since the orders are coprime, so $\abs{NH}=20=\abs{\Gal(K/\QQ)}$ by step [](#degree){.pf-ref}. With $N$ normal, $\Gal(K/\QQ)=N\rtimes H$, and step [](#relation){.pf-ref} gives the action. The map $\sigma\mapsto(x\mapsto x+1)$, $\tau\mapsto(x\mapsto 2x)$ respects the relations and identifies the group with $\operatorname{AGL}_1(\FF_5)$.
:::

:::

:::

:::
