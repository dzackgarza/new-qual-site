---
schema: qual/card@1
id: P-6VMUH
kind: problem
title: Galois group of $x^4-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the **Galois group** of the polynomial $f(x) = x^4 - 3$ over $\QQ$, and describe its action on the roots.
:::

::: {.solution}
Let $\alpha=\sqrt[4]{3}$ and $K=\QQ(\alpha,i)$.

::: pf

::: {.pf-step #splitting-field}
$K$ is the splitting field of $f$, and $[K:\QQ]=8$.

::: pf-proof
The roots of $f$ are $\alpha,i\alpha,-\alpha,-i\alpha$, and they generate $\QQ(\alpha,i)$ because $i=i\alpha/\alpha$. Eisenstein at $3$ gives $[\QQ(\alpha):\QQ]=4$. Since $\QQ(\alpha)\subset\RR$, $i\notin\QQ(\alpha)$, so $[K:\QQ(\alpha)]=2$.
:::

:::

::: {.pf-step #generators}
There are automorphisms $r,s\in\Gal(K/\QQ)$ with $r(\alpha)=i\alpha$, $r(i)=i$, $s(\alpha)=\alpha$, $s(i)=-i$, and they satisfy $r^4=s^2=1$ and $srs=r^{-1}$.

::: pf-proof
By step [](#splitting-field){.pf-ref}, $[K:\QQ(i)]=4$, so $f$ is irreducible over $\QQ(i)$ and some element of $\Gal(K/\QQ(i))$ sends $\alpha$ to $i\alpha$; this is $r$. Complex conjugation restricts to $s$. Checking on the generators: $r^k(\alpha)=i^k\alpha$, so $r$ has order $4$; $s^2=1$; and $srs(\alpha)=-i\alpha=r^{-1}(\alpha)$, $srs(i)=i=r^{-1}(i)$.
:::

:::

::: pf-step
$\Gal(K/\QQ)=\langle r,s\rangle\cong\boxed{D_4}$, the dihedral group of order $8$. On the roots $(\alpha,i\alpha,-\alpha,-i\alpha)$, numbered $1,2,3,4$, it acts as the symmetries of a square, with $r=(1\ 2\ 3\ 4)$ and $s=(2\ 4)$.

::: pf-proof
The relations of step [](#generators){.pf-ref} present a quotient of $D_4$, and $\langle r,s\rangle$ contains the $4$ powers of $r$ and $s\notin\langle r\rangle$ (since $s$ moves $i$), so it has order $8$, which equals $[K:\QQ]$. The permutations follow from $r(i^k\alpha)=i^{k+1}\alpha$ and $s(i^k\alpha)=(-i)^k\alpha$.
:::

:::

:::

:::
