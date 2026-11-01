---
schema: qual/card@1
id: P-AUD1Q
kind: problem
title: $\Ext$ groups between $R$ and $R/(x)$ over $R=K[x]/(x^2)$
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2018`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All three computed from the periodic minimal free resolution of $k=R/(x)$, in which every
    differential is multiplication by $x$: since $\operatorname{ann}_R(x)=(x)=xR$, the complex
    $\Hom_R(F_\bullet,k)$ has zero differentials and $\Hom_R(F_\bullet,R)$ has differential
    multiplication by $x$, giving $k$ in every degree for $\Ext(k,k)$, $0$ above degree $0$ for
    $\Ext(R,k)$ and $\Ext(k,R)$, with $\Ext^0(k,R)=\operatorname{ann}(x)\cong k$. Nothing is left in
    outline.
---

::: {.problem}
Let $K$ be a field and $R=K[x]/(x^2)$.
For each integer $i\geq0$, compute

(a) $\Ext_R^i(R,R/(x))$

(b) $\Ext_R^i(R/(x),R)$

(c) $\Ext_R^i(R/(x),R/(x))$
:::

::: {.solution}

Let $R=K[x]/(x^2)$, let $x$ denote the class of $x$ (so $x^2=0$ and $x\ne0$), let $\mathfrak m=(x)$ and $k=R/(x)=K$.

::: pf

::: {.pf-step #s1}

$\operatorname{ann}_R(x)=(x)$ and $(x)\ne0$.

::: pf-proof

An element $r=a+bx$ of $R$, with $a,b\in K$, satisfies $xr=ax+bx^2=ax$, which vanishes exactly when $a=0$. So $\operatorname{ann}_R(x)=\{bx\}=\mathfrak m$. In particular $\mathfrak m\ne0$, since $x\ne0$, and $\mathfrak m^2=(x^2)=0$.

:::

:::

::: {.pf-step #s2}

$\cdots\to R\xrightarrow{\,x\,}R\xrightarrow{\,x\,}R\to k\to0$ is a free resolution of $k$.

::: pf-proof

The augmentation $R\to k$ is the quotient map and has kernel $\mathfrak m=(x)=\operatorname{im}(x\cdot)$, which by step [](#s1){.pf-ref} equals $\ker(x\cdot:R\to R)$. So the sequence is exact at $R$ in degree $0$ and at every $R$ in positive degree, since each such stage reads $\operatorname{im}(x\cdot)=\ker(x\cdot)$. Each $R$ is free of rank one.

:::

:::

::: {.pf-step #s3}

Part (a): $\Ext_R^0(R,k)\cong k$ and $\Ext_R^i(R,k)=0$ for $i\ge1$.

::: pf-proof

$R$ is free, hence projective, so $0\to R\to R\to R\to0$ with the identity in degree $1$ and the zero map in degree $0$ is a projective resolution of $R$. Applying $\Hom_R(-,k)$ gives $0\to\Hom_R(R,k)\to\Hom_R(R,k)\to0$ with differentials given by precomposition with the identity and with $0$, so $\Hom_R(R,k)\cong k$ sits in degree $0$ and nothing survives in higher degrees. Hence $\Ext_R^0(R,k)\cong k$ and $\Ext_R^i(R,k)=0$ for $i\ge1$.

:::

:::

::: {.pf-step #s4}

Part (b): $\Ext_R^0(k,R)=\operatorname{ann}_R(x)\cong k$ and $\Ext_R^i(k,R)=0$ for $i\ge1$.

::: pf-proof

Apply $\Hom_R(-,R)$ to the resolution of step [](#s2){.pf-ref}. Since $\Hom_R(R,R)\cong R$ in each degree, and the differential $\delta^i:\Hom_R(R,R)\to\Hom_R(R,R)$ is precomposition with multiplication by $x$, that is $f\mapsto f\circ(x\cdot)$, i.e. multiplication by $x$ on $R$, the cohomology is
$$
\Ext_R^i(k,R)=\frac{\ker(x\cdot:R\to R)}{\operatorname{im}(x\cdot:R\to R)}=\frac{\operatorname{ann}_R(x)}{(x)}
$$
for $i\ge1$, which is $0$ by step [](#s1){.pf-ref}. In degree $0$, $\Ext_R^0(k,R)=\ker\bigl(\delta^0\bigr)=\operatorname{ann}_R(x)=(x)$, which is a one-dimensional $k$-vector space, so $\Ext_R^0(k,R)\cong k$.

:::

:::

::: {.pf-step #s5}

Part (c): $\Ext_R^i(k,k)\cong k$ for every $i\ge0$.

::: pf-proof

Apply $\Hom_R(-,k)$ to the resolution of step [](#s2){.pf-ref}. Each $\Hom_R(R,k)\cong k$: a homomorphism $R\to k$ is determined by the image of $1$ and automatically kills $x$, so it is given by an arbitrary scalar. The differential $\delta^i$ sends $f$ to $f\circ(x\cdot)$, and $(f\circ(x\cdot))(1)=f(x)=x\cdot f(1)=0$ because $x$ acts as zero on $k$. So every differential in the complex $\Hom_R(F_\bullet,k)$ is zero, and the complex is
$$
k\xrightarrow{\ 0\ }k\xrightarrow{\ 0\ }k\xrightarrow{\ 0\ }\cdots
$$
Consequently $\Ext_R^i(k,k)=k$ for every $i\ge0$.

:::

:::

::: {.pf-step #s6}

Summary, and the two structural points behind it.

::: pf-proof

(a) $\Ext_R^i(R,k)=k$ for $i=0$ and $0$ for $i\ge1$;
(b) $\Ext_R^i(k,R)=k$ for $i=0$ and $0$ for $i\ge1$;
(c) $\Ext_R^i(k,k)=k$ for all $i\ge0$.

The vanishing in (b) for $i\ge1$ reflects that $R=K[x]/(x^2)$ is a Frobenius ring and hence injective as a module over itself; the nonvanishing in every degree in (c) reflects that $k$ has infinite projective dimension over $R$, with the two-periodic resolution of step [](#s2){.pf-ref} supplying Betti numbers $1$ in every degree.

:::

:::

:::

:::
