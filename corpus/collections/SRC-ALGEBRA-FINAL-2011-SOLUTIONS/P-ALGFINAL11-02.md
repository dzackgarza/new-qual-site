---
schema: qual/card@1
id: P-ALGFINAL11-02
kind: problem
title: Norms and prime elements in quadratic integer rings
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n > 1$ be in $\ZZ$, and let $R := \ZZ[\sqrt{-n}]$.
For $x = a + b\sqrt{-n} \in R$ ($a, b \in \ZZ$), set $\bar{x} = a - b\sqrt{-n}$, and define the norm
$$
N(x) = x\bar{x} = a^{2} + nb^{2}.
$$

(a) Assuming $x \neq 0$, describe group isomorphisms $R/xR \cong R/\bar{x}R \cong xR/x\bar{x}R$.

(b) Deduce from (a) that $N(x)^{2} = [R : xR]\,[xR : x\bar{x}R] = [R : xR]^{2}$.

(c) Deduce from (b) that if $N(x)$ is prime in $\ZZ$ then $x$ is prime in $R$.

(d) Deduce from (c) that if $p$ is a prime in $\ZZ$ then there is *at most one* way to represent $p$ in the form $p = a^{2} + nb^{2}$ where $a$ and $b$ are positive integers.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) Conjugation $y\mapsto\bar y$ induces $R/xR\cong R/\bar xR$, and multiplication by $x$ induces $R/\bar xR\cong xR/x\bar xR$.

::: pf-proof
Conjugation is a ring automorphism of $R$ that carries $xR$ onto $\bar xR$, so it induces the first isomorphism. The map $R\to xR/x\bar xR$, $y\mapsto xy+x\bar xR$, is a surjective group homomorphism. Its kernel is $\bar xR$: if $xy=x\bar xz$, then $y=\bar xz$ because $R$ is an integral domain and $x\ne0$.
:::

:::

::: {.pf-step #s2}
(b) $N(x)^2=[R:xR]\,[xR:x\bar xR]=[R:xR]^2$.

::: pf-proof
The map $(a,b)\mapsto a+b\sqrt{-n}$ is a group isomorphism $\ZZ^2\to R$. For an integer $m>0$ it carries $(m\ZZ)^2$ onto $mR$, so $[R:mR]=m^2$. Apply this with $m=N(x)=x\bar x>0$:
$$
N(x)^2=[R:x\bar xR]=[R:xR]\,[xR:x\bar xR]=[R:xR]^2,
$$
where the last equality is step [](#s1){.pf-ref}.
:::

:::

::: {.pf-step #s3}
(c) If $N(x)$ is prime in $\ZZ$, then $x$ is prime in $R$.

::: pf-proof
By step [](#s2){.pf-ref}, $\cardinality{R/xR}=N(x)$ is prime. Hence the additive group $R/xR$ has no subgroup other than $0$ and itself, so $R/xR$ has no ideal other than $0$ and itself, and $xR$ is maximal. A maximal ideal is prime, so $x$ is prime.
:::

:::

::: {.pf-step #s4}
(d) If $p=a^2+nb^2=c^2+nd^2$ with $a,b,c,d>0$, then $a=c$ and $b=d$.

::: pf-proof
Put $x=a+b\sqrt{-n}$ and $y=c+d\sqrt{-n}$. By step [](#s3){.pf-ref}, $x$ is prime in $R$, and $x\mid p=y\bar y$, so $x\mid y$ or $x\mid\bar y$. The norm is multiplicative, because $\overline{uv}=\bar u\bar v$. If $y=xu$ or $\bar y=xu$, taking norms gives $N(u)=1$. Write $u=r+s\sqrt{-n}$; then $r^2+ns^2=1$ with $n>1$ forces $u=\pm1$. So $y=\pm x$ or $\bar y=\pm x$. Comparing the coefficients, whose signs are fixed by $a,b,c,d>0$, only $y=x$ is possible. Hence $a=c$ and $b=d$.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer (a), (b), (c) and (d).
:::

:::

:::
