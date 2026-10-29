---
schema: qual/card@1
id: P-PMGNP
kind: problem
title: $\Ext$ of cyclic groups
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
  - Abelian Groups
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Explain $\Ext^1_{\ZZ}$ for abelian groups, where it appears, and compute
$$\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ/n\ZZ)
\quad\text{and}\quad
\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ).$$
:::

::: {.solution}
For abelian groups $A$ and $B$, $\Ext^1_{\ZZ}(A,B)$ is the first right derived functor of $\Hom_{\ZZ}(-,B)$ evaluated at $A$, computed from a projective resolution of $A$. It classifies extensions $0\to B\to E\to A\to0$ up to equivalence, with the split extension as zero. It measures the failure of $\Hom_{\ZZ}(-,B)$ to be right exact, and it appears in the universal coefficient theorem for cohomology, $H^n(X;B)\cong\Hom(H_n(X),B)\oplus\Ext^1_{\ZZ}(H_{n-1}(X),B)$.

::: pf

::: {.pf-step #cyclic-source}
For every abelian group $B$, $\Ext^1_{\ZZ}(\ZZ/m\ZZ,B)\cong B/mB$.

::: pf-proof
The sequence $0\to\ZZ\xrightarrow{\times m}\ZZ\to\ZZ/m\ZZ\to0$ is a free resolution. Applying $\Hom_{\ZZ}(-,B)$ and using $\Hom_{\ZZ}(\ZZ,B)\cong B$ gives the exact sequence
$$0\to\Hom(\ZZ/m\ZZ,B)\to B\xrightarrow{\times m}B\to\Ext^1_{\ZZ}(\ZZ/m\ZZ,B)\to0,$$
so $\Ext^1_{\ZZ}(\ZZ/m\ZZ,B)$ is the cokernel $B/mB$ of multiplication by $m$.
:::

:::

::: pf-step
$\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ/n\ZZ)\cong\boxed{\ZZ/\gcd(m,n)\ZZ}$.

::: pf-proof
By step [](#cyclic-source){.pf-ref} with $B=\ZZ/n\ZZ$, the group is $(\ZZ/n\ZZ)/m(\ZZ/n\ZZ)=\ZZ/(m,n)\ZZ$, and the ideal $(m,n)$ of $\ZZ$ is $\gcd(m,n)\ZZ$.
:::

:::

::: pf-step
$\Ext^1_{\ZZ}(\ZZ/m\ZZ,\ZZ)\cong\boxed{\ZZ/m\ZZ}$.

::: pf-proof
This is step [](#cyclic-source){.pf-ref} with $B=\ZZ$.
:::

:::

:::

:::
