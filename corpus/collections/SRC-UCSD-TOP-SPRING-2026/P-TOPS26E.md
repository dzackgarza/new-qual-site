---
schema: qual/card@1
id: P-TOPS26E
kind: problem
title: $\operatorname{Ext}^1_{\ZZ}(\QQ\oplus\ZZ\oplus\ZZ_3\oplus\ZZ_7,\ZZ\oplus\ZZ_6\oplus\ZZ_{21})$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Compute
\[
\operatorname{Ext}^1_{\ZZ}(\QQ \oplus \ZZ \oplus \ZZ_3 \oplus \ZZ_7,\ \ZZ \oplus \ZZ_6 \oplus \ZZ_{21}).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #ext-additive-first-variable}
Put
$$B=\ZZ\oplus\ZZ/6\oplus\ZZ/21.$$
Since $\operatorname{Ext}^1_{\ZZ}(-,B)$ sends finite direct sums in the first variable to direct sums,
$$
\operatorname{Ext}^1(\QQ\oplus\ZZ\oplus\ZZ/3\oplus\ZZ/7,B)
\cong
\operatorname{Ext}^1(\QQ,B)\oplus\operatorname{Ext}^1(\ZZ,B)
\oplus\operatorname{Ext}^1(\ZZ/3,B)\oplus\operatorname{Ext}^1(\ZZ/7,B).
$$

::: pf-proof
Ext is contravariant and additive in its first argument for finite direct sums.
:::

:::

::: {.pf-step #ext-cyclic-formula}
One has
$$\operatorname{Ext}^1(\ZZ,B)=0,
\qquad
\operatorname{Ext}^1(\ZZ/n,B)\cong B/nB.$$

::: pf-proof
The first equality holds because $\ZZ$ is free. For the second, apply $\operatorname{Hom}_{\ZZ}(-,B)$ to
$$0\to\ZZ\xrightarrow{n}\ZZ\to\ZZ/n\to0.$$
:::

:::

::: {.pf-step #ext-z3-z7-computation}
Hence
$$
\operatorname{Ext}^1(\ZZ/3,B)\cong(\ZZ/3)^3,
\qquad
\operatorname{Ext}^1(\ZZ/7,B)\cong(\ZZ/7)^2.
$$

::: pf-proof
Modulo $3$, the three summands of $B$ contribute $\ZZ/3$, $\ZZ/3$, and $\ZZ/3$. Modulo $7$, they contribute $\ZZ/7$, $0$, and $\ZZ/7$.
:::

:::

::: {.pf-step #ext-q-z-classical}
The classical computation is
$$\operatorname{Ext}^1_{\ZZ}(\QQ,\ZZ)\cong\widehat{\ZZ}/\ZZ,$$
where $\widehat{\ZZ}=\prod_p\ZZ_p$ is the profinite completion.

::: pf-proof
Apply $\operatorname{Hom}_{\ZZ}(-,\ZZ)$ to
$$0\to\ZZ\to\QQ\to\QQ/\ZZ\to0.$$
Since $\operatorname{Hom}(\QQ,\ZZ)=\operatorname{Hom}(\QQ/\ZZ,\ZZ)=0$, the resulting exact sequence is
$$0\to\ZZ\to\operatorname{Ext}^1(\QQ/\ZZ,\ZZ)\to\operatorname{Ext}^1(\QQ,\ZZ)\to0.$$
Now
$$\QQ/\ZZ\cong\bigoplus_p C_{p^\infty}$$
and
$$\operatorname{Ext}^1(C_{p^\infty},\ZZ)\cong\ZZ_p,$$
so
$$\operatorname{Ext}^1(\QQ/\ZZ,\ZZ)\cong\prod_p\ZZ_p=\widehat{\ZZ}.$$
The map from $\ZZ$ is the diagonal embedding, giving the quotient above.
:::

:::

::: {.pf-step #ext-q-finite-vanishes}
For every finite abelian group $F$,
$$\operatorname{Ext}^1_{\ZZ}(\QQ,F)=0.$$

::: pf-proof
It suffices to take $F=\ZZ/n$. Apply $\operatorname{Hom}(\QQ,-)$ to
$$0\to\ZZ\xrightarrow n\ZZ\to\ZZ/n\to0.$$
Since $\operatorname{Hom}(\QQ,\ZZ)=\operatorname{Hom}(\QQ,\ZZ/n)=0$ and $\operatorname{Ext}^2_{\ZZ}(\QQ,\ZZ)=0$, one obtains
$$\operatorname{Ext}^1(\QQ,\ZZ/n)\cong\operatorname{coker}\bigl(n:\widehat{\ZZ}/\ZZ\to\widehat{\ZZ}/\ZZ\bigr).$$
Multiplication by $n$ on $\widehat{\ZZ}/\ZZ$ is surjective: for $x\in\widehat{\ZZ}$ choose $m\in\ZZ$ with $x+m\equiv0\pmod{n\widehat{\ZZ}}$, then $(x+m)/n\in\widehat{\ZZ}$. Hence the cokernel vanishes.
:::

:::

::: {.pf-step #ext-q-b}
Therefore
$$\operatorname{Ext}^1(\QQ,B)\cong\widehat{\ZZ}/\ZZ.$$

::: pf-proof
Ext is additive in the second variable over the finite direct sum defining $B$, and the finite summands vanish by step [](#ext-q-finite-vanishes){.pf-ref}.
:::

:::

::: pf-step
Combining the preceding steps,
$$
\boxed{
\operatorname{Ext}^1_{\ZZ}(\QQ\oplus\ZZ\oplus\ZZ_3\oplus\ZZ_7,
\ZZ\oplus\ZZ_6\oplus\ZZ_{21})
\cong
\widehat{\ZZ}/\ZZ\oplus(\ZZ/3)^3\oplus(\ZZ/7)^2.}
$$

::: pf-proof
Use steps [](#ext-additive-first-variable){.pf-ref}, [](#ext-cyclic-formula){.pf-ref}, [](#ext-z3-z7-computation){.pf-ref}, [](#ext-q-z-classical){.pf-ref}, [](#ext-q-finite-vanishes){.pf-ref} and [](#ext-q-b){.pf-ref}.
:::

:::

:::

:::
