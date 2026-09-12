---
schema: qual/card@1
id: P-TOPS26E
kind: problem
title: $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q\oplus\mathbb Z\oplus\mathbb Z_3\oplus\mathbb Z_7,\mathbb Z\oplus\mathbb Z_6\oplus\mathbb Z_{21})$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: problem
Compute
\[
\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Q} \oplus \mathbb{Z} \oplus \mathbb{Z}_3 \oplus \mathbb{Z}_7,\ \mathbb{Z} \oplus \mathbb{Z}_6 \oplus \mathbb{Z}_{21}).
\]
:::

::: {.solution}
<1>1. Put
$$B=\mathbb Z\oplus\mathbb Z/6\oplus\mathbb Z/21.$$
Since $\operatorname{Ext}^1_{\mathbb Z}(-,B)$ sends finite direct sums in the first variable to direct sums,
$$
\operatorname{Ext}^1(\mathbb Q\oplus\mathbb Z\oplus\mathbb Z/3\oplus\mathbb Z/7,B)
\cong
\operatorname{Ext}^1(\mathbb Q,B)\oplus\operatorname{Ext}^1(\mathbb Z,B)
\oplus\operatorname{Ext}^1(\mathbb Z/3,B)\oplus\operatorname{Ext}^1(\mathbb Z/7,B).
$$
::: {.proof}
Ext is contravariant and additive in its first argument for finite direct sums.
:::

<1>2. One has
$$\operatorname{Ext}^1(\mathbb Z,B)=0,
\qquad
\operatorname{Ext}^1(\mathbb Z/n,B)\cong B/nB.$$
::: {.proof}
The first equality holds because $\mathbb Z$ is free. For the second, apply $\operatorname{Hom}_{\mathbb Z}(-,B)$ to
$$0\to\mathbb Z\xrightarrow{n}\mathbb Z\to\mathbb Z/n\to0.$$
:::

<1>3. Hence
$$
\operatorname{Ext}^1(\mathbb Z/3,B)\cong(\mathbb Z/3)^3,
\qquad
\operatorname{Ext}^1(\mathbb Z/7,B)\cong(\mathbb Z/7)^2.
$$
::: {.proof}
Modulo $3$, the three summands of $B$ contribute $\mathbb Z/3$, $\mathbb Z/3$, and $\mathbb Z/3$. Modulo $7$, they contribute $\mathbb Z/7$, $0$, and $\mathbb Z/7$.
:::

<1>4. The classical computation is
$$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q,\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z,$$
where $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$ is the profinite completion.
::: {.proof}
Apply $\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)$ to
$$0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.$$
Since $\operatorname{Hom}(\mathbb Q,\mathbb Z)=\operatorname{Hom}(\mathbb Q/\mathbb Z,\mathbb Z)=0$, the resulting exact sequence is
$$0\to\mathbb Z\to\operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)\to\operatorname{Ext}^1(\mathbb Q,\mathbb Z)\to0.$$
Now
$$\mathbb Q/\mathbb Z\cong\bigoplus_p C_{p^\infty}$$
and
$$\operatorname{Ext}^1(C_{p^\infty},\mathbb Z)\cong\mathbb Z_p,$$
so
$$\operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)\cong\prod_p\mathbb Z_p=\widehat{\mathbb Z}.$$
The map from $\mathbb Z$ is the diagonal embedding, giving the quotient above.
:::

<1>5. For every finite abelian group $F$,
$$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q,F)=0.$$
::: {.proof}
It suffices to take $F=\mathbb Z/n$. Apply $\operatorname{Hom}(\mathbb Q,-)$ to
$$0\to\mathbb Z\xrightarrow n\mathbb Z\to\mathbb Z/n\to0.$$
Since $\operatorname{Hom}(\mathbb Q,\mathbb Z)=\operatorname{Hom}(\mathbb Q,\mathbb Z/n)=0$ and $\operatorname{Ext}^2_{\mathbb Z}(\mathbb Q,\mathbb Z)=0$, one obtains
$$\operatorname{Ext}^1(\mathbb Q,\mathbb Z/n)\cong\operatorname{coker}\bigl(n:\widehat{\mathbb Z}/\mathbb Z\to\widehat{\mathbb Z}/\mathbb Z\bigr).$$
Multiplication by $n$ on $\widehat{\mathbb Z}/\mathbb Z$ is surjective: for $x\in\widehat{\mathbb Z}$ choose $m\in\mathbb Z$ with $x+m\equiv0\pmod{n\widehat{\mathbb Z}}$, then $(x+m)/n\in\widehat{\mathbb Z}$. Hence the cokernel vanishes.
:::

<1>6. Therefore
$$\operatorname{Ext}^1(\mathbb Q,B)\cong\widehat{\mathbb Z}/\mathbb Z.$$
::: {.proof}
Ext is additive in the second variable over the finite direct sum defining $B$, and the finite summands vanish by <1>5.
:::

<1>7. Combining the preceding steps,
$$
\boxed{
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q\oplus\mathbb Z\oplus\mathbb Z_3\oplus\mathbb Z_7,
\mathbb Z\oplus\mathbb Z_6\oplus\mathbb Z_{21})
\cong
\widehat{\mathbb Z}/\mathbb Z\oplus(\mathbb Z/3)^3\oplus(\mathbb Z/7)^2.}
$$
::: {.proof}
Use <1>1--<1>6.
:::
:::
