---
schema: qual/card@1
id: P-S5JSR
kind: problem
title: The Galois group of $x^n-2$ is dihedral exactly for $n=3,4,6$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
---

::: {.problem}
Let $n\ge3$. For the splitting field of $x^n-2$ over $\QQ$, prove the affine embedding
$$
\Gal\hookrightarrow (\ZZ/n\ZZ)\rtimes(\ZZ/n\ZZ)^\times
$$
and prove that the Galois group is dihedral of order $2n$ exactly for $n=3,4,6$.
:::

::: {.solution}

Let $\alpha=2^{1/n}>0$, let $\zeta=\zeta_n$ be a primitive $n$-th root of unity, and let $G=\Gal(L/\QQ)$. The roots of $x^n-2$ are $\zeta^j\alpha$, so the splitting field is $L=\QQ(\alpha,\zeta)$. Since $x^n-2$ is Eisenstein at $2$, $[\QQ(\alpha):\QQ]=n$.

::: pf

::: {.pf-step #affine}

The map $\sigma\mapsto(a,b)$, where $\sigma(\alpha)=\zeta^a\alpha$ and $\sigma(\zeta)=\zeta^b$, is an injective homomorphism $G\hookrightarrow(\ZZ/n\ZZ)\rtimes(\ZZ/n\ZZ)^\times$ with law $(a,b)(c,d)=(a+bc,bd)$.

::: pf-proof

$\sigma(\alpha)$ is a root of $x^n-2$ and $\sigma(\zeta)$ is a primitive $n$-th root of unity, so $a\in\ZZ/n\ZZ$ and $b\in(\ZZ/n\ZZ)^\times$ exist and are unique. If $\sigma\mapsto(a,b)$ and $\tau\mapsto(c,d)$, then $\sigma\tau(\alpha)=\sigma(\zeta^c\alpha)=\zeta^{bc+a}\alpha$ and $\sigma\tau(\zeta)=\zeta^{bd}$. Since $\alpha$ and $\zeta$ generate $L$, $\sigma$ is determined by $(a,b)$.

:::

:::

::: {.pf-step #order}

If $G\cong D_{2n}$, then $n\in\{3,4,6,8,12\}$.

::: pf-proof

Restriction to $\QQ(\zeta)$ is a surjection $G\twoheadrightarrow\Gal(\QQ(\zeta)/\QQ)\cong(\ZZ/n\ZZ)^\times$ onto an abelian group. Every abelian quotient of $D_{2n}$ has order at most $4$ and exponent at most $2$, so $(\ZZ/n\ZZ)^\times$ has order at most $4$ and exponent at most $2$. For $n\ge3$ this leaves $n\in\{3,4,6,8,12\}$; $n=5,10$ are excluded because $(\ZZ/n\ZZ)^\times\cong C_4$.

:::

:::

::: pf-step

For $n=3,4,6$, $G\cong D_{2n}$.

::: pf-proof

Here $\QQ(\zeta)$ is imaginary quadratic and $\QQ(\alpha)\subset\RR$, so $\QQ(\alpha)\cap\QQ(\zeta)=\QQ$ and $\zeta\notin\QQ(\alpha)$; hence $[L:\QQ]=2n$. Let $r\in G$ fix $\zeta$ and send $\alpha\mapsto\zeta\alpha$, and let $s$ be complex conjugation restricted to $L$. By step [](#affine){.pf-ref}, $r\mapsto(1,1)$ has order $n$, $s\mapsto(0,-1)$ has order $2$, and $(0,-1)(1,1)(0,-1)=(-1,1)$, so $srs=r^{-1}$. Since $s\notin\langle r\rangle$ and $\abs{G}=2n$, $G=\langle r,s\rangle\cong D_{2n}$.

:::

:::

::: pf-step

For $n=12$, $G\not\cong D_{24}$.

::: pf-proof

$L$ contains the splitting fields $M_1=\QQ(2^{1/4},i)$ of $x^4-2$ and $M_2=\QQ(2^{1/3},\zeta_3)$ of $x^3-2$, of degrees $8$ and $6$. Their quadratic subfields are $\QQ(i),\QQ(\sqrt2),\QQ(\sqrt{-2})$ and $\QQ(\sqrt{-3})$ respectively, so $M_1\cap M_2$, which is Galois over $\QQ$ of degree dividing $\gcd(8,6)=2$, equals $\QQ$. Hence $[L:\QQ]\ge[M_1M_2:\QQ]=48>24$.

:::

:::

::: pf-step

For $n=8$, $G\not\cong D_{16}$.

::: pf-proof

Here $\sqrt2=\alpha^4=\zeta+\zeta^{-1}$. For $\sigma\mapsto(a,b)$, $\sigma(\alpha^4)=(-1)^a\sqrt2$ and $\sigma(\zeta+\zeta^{-1})=\zeta^b+\zeta^{-b}$, which is $\sqrt2$ for $b=\pm1$ and $-\sqrt2$ for $b=\pm3$. So $a$ is even exactly when $b\equiv\pm1\pmod 8$, and $\abs{G}\le16$. In $(\ZZ/8\ZZ)\rtimes(\ZZ/8\ZZ)^\times$, $(a,b)^2=(a(1+b),b^2)=(a(1+b),1)$. The elements of order dividing $2$ allowed by the parity condition are therefore $(0,1)$, $(4,1)$, and $(a,-1)$ with $a$ even, while $(a,\pm3)$ with $a$ odd has $a(1+b)\neq0$. So $G$ has at most $5$ involutions, whereas $D_{16}$ has $9$.

:::

:::

::: pf-qed

By step [](#order){.pf-ref} and the four cases $n=3,4,6$, $n=12$, $n=8$, the Galois group of $x^n-2$ is dihedral of order $2n$ exactly for $\boxed{n=3,4,6}$.

:::

:::

:::
