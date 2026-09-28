---
schema: qual/card@1
id: P-BERK92S-14
kind: problem
title: Minimal polynomial of $\sqrt5+\sqrt7$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
\[
\alpha=\sqrt5+\sqrt7.
\]

1. Find explicitly a degree-four polynomial $f(x)\in\mathbb Q[x]$ having $\alpha$ as a root.
2. Prove that $f(x)$ is irreducible over $\mathbb Q$.
:::

::: {.solution}
<1>1. The number $\alpha$ is a root of
$$
f(x)\coloneqq x^4-24x^2+4\in\QQ[x].
$$

::: {.proof}
Since
$$
\alpha^2
=12+2\sqrt{35},
$$
we have
$$
(\alpha^2-12)^2=140.
$$
Expanding gives
$$
\alpha^4-24\alpha^2+4=0,
$$
so $f(\alpha)=0$.
:::

<1>2.
$$
\QQ(\alpha)=\QQ(\sqrt5,\sqrt7).
$$

::: {.proof}
The inclusion
$\QQ(\alpha)\subseteq\QQ(\sqrt5,\sqrt7)$ is immediate. Conversely,
$$
\frac2\alpha
=\sqrt7-\sqrt5,
$$
because
$(\sqrt7+\sqrt5)(\sqrt7-\sqrt5)=2$. Therefore
$$
\sqrt7
=\frac12\left(\alpha+\frac2\alpha\right),
\qquad
\sqrt5
=\frac12\left(\alpha-\frac2\alpha\right),
$$
so both radicals lie in $\QQ(\alpha)$.
:::

<1>3.
$$
[\QQ(\sqrt5,\sqrt7):\QQ]=4.
$$

::: {.proof}
Since $5$ is not a square in $\QQ$,
$$
[\QQ(\sqrt5):\QQ]=2.
$$
It remains to show $\sqrt7\notin\QQ(\sqrt5)$. Suppose instead that
$$
\sqrt7=a+b\sqrt5
\qquad(a,b\in\QQ).
$$
Squaring and using the $\QQ$-linear independence of $1$ and $\sqrt5$
gives
$$
7=a^2+5b^2,
\qquad
ab=0.
$$
If $b=0$, then $\sqrt7=a\in\QQ$, impossible. If $a=0$, then
$b^2=7/5$, also impossible for rational $b$: writing $b=m/n$ in
lowest terms would give $5m^2=7n^2$, forcing $7$ to divide both $m$
and $n$.

Thus $x^2-7$ is irreducible over $\QQ(\sqrt5)$, so
$$
[\QQ(\sqrt5,\sqrt7):\QQ(\sqrt5)]=2.
$$
The tower law gives the claimed degree $4$.
:::

<1>4. The polynomial $f(x)=x^4-24x^2+4$ is irreducible over $\QQ$.

::: {.proof}
By steps <1>2 and <1>3,
$$
[\QQ(\alpha):\QQ]=4.
$$
Hence the minimal polynomial of $\alpha$ over $\QQ$ has degree $4$.
Step <1>1 gives a monic degree-four polynomial $f\in\QQ[x]$ having
$\alpha$ as a root. Therefore $f$ is the minimal polynomial of
$\alpha$, and in particular is irreducible over $\QQ$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 answers part 1, and step <1>4 proves part 2.
:::
:::
