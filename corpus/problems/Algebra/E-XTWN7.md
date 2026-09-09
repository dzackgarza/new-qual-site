---
schema: qual/card@1
id: E-XTWN7
kind: problem
title: $\mathbb{Q}(x)$ is Galois over $\mathbb{Q}(x^{2})$ but not over $\mathbb{Q}(x^{3})$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Transcendence
  - Field Extensions
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

::: problem
4. Prove that as extensions of $\QQ$, $\QQ(x)$ is Galois over $\QQ(x^2)$ but not over $\QQ(x^3)$.
:::


::: {.solution}
Let $x$ be transcendental over $\QQ$.

<1>1. The extension $\QQ(x)/\QQ(x^2)$ has degree $2$.
::: {.proof}
Put $t=x^2$. Then $x$ satisfies
\[
T^2-t\in\QQ(t)[T]=\QQ(x^2)[T].
\]
Thus the degree is at most $2$. It is not $1$, because $x\notin\QQ(x^2)$: every element of $\QQ(x^2)$ is fixed by the automorphism of $\QQ(x)$ sending $x$ to $-x$, whereas $x$ is not. Hence
\[
[\QQ(x):\QQ(x^2)]=2.
\]
:::

<1>2. The extension $\QQ(x)/\QQ(x^2)$ is Galois, with Galois group $C_2$.
::: {.proof}
The minimal polynomial of $x$ over $\QQ(x^2)$ is
\[
T^2-x^2,
\]
whose two roots in $\QQ(x)$ are $x$ and $-x$. Since the characteristic is $0$, the polynomial is separable, and it splits in $\QQ(x)$. Hence the extension is Galois. Its two automorphisms are
\[
x\longmapsto x,
\qquad
x\longmapsto -x,
\]
so the Galois group is cyclic of order $2$.
:::

<1>3. The extension $\QQ(x)/\QQ(x^3)$ has degree $3$.
::: {.proof}
Put $s=x^3$. Then $x$ satisfies
\[
T^3-s\in\QQ(s)[T],
\]
so the degree is at most $3$. The polynomial $T^3-s$ is irreducible over $\QQ(s)$ by Eisenstein's criterion in $\QQ[s][T]$ with the prime element $s$: every nonleading coefficient is divisible by $s$, the constant term $-s$ is not divisible by $s^2$, and the leading coefficient is not divisible by $s$. By Gauss's lemma it remains irreducible over $\QQ(s)$. Therefore
\[
[\QQ(x):\QQ(x^3)]=3.
\]
:::

<1>4. A primitive cube root of unity $\zeta_3$ does not lie in $\QQ(x)$.
::: {.proof}
The element $\zeta_3$ is algebraic over $\QQ$. We claim that every element of $\QQ(x)$ algebraic over $\QQ$ already lies in $\QQ$.

Indeed, let $r(x)\in\QQ(x)$ be nonconstant. Then $x$ is algebraic over $\QQ(r(x))$: writing $r(x)=a(x)/b(x)$ with coprime $a,b\in\QQ[x]$, the element $x$ satisfies
\[
a(T)-r(x)b(T)=0
\]
over $\QQ(r(x))$. Hence $\QQ(x)/\QQ(r(x))$ is algebraic. Since
\[
\operatorname{trdeg}_{\QQ}\QQ(x)=1,
\]
algebraic extensions preserve transcendence degree, so
\[
\operatorname{trdeg}_{\QQ}\QQ(r(x))=1.
\]
Thus $r(x)$ is transcendental over $\QQ$. Therefore the only elements of $\QQ(x)$ algebraic over $\QQ$ are the constants in $\QQ$.

Since $\zeta_3\notin\QQ$, it follows that $\zeta_3\notin\QQ(x)$.
:::

<1>5. The extension $\QQ(x)/\QQ(x^3)$ is not normal, hence not Galois.
::: {.proof}
The minimal polynomial from <1>3 is
\[
T^3-x^3,
\]
whose roots in an algebraic closure are
\[
x,\qquad \zeta_3x,\qquad \zeta_3^2x.
\]
If $\zeta_3x\in\QQ(x)$, then dividing by $x$ would give $\zeta_3\in\QQ(x)$, contradicting <1>4. Hence the minimal polynomial does not split over $\QQ(x)$, so the extension is not normal. Therefore it is not Galois.
:::

<1>6. Consequently,
\[
\QQ(x)/\QQ(x^2)\text{ is Galois, whereas }\QQ(x)/\QQ(x^3)\text{ is not.}
\]
::: {.proof}
Combine <1>2 and <1>5.
:::
:::
