---
schema: qual/card@1
id: P-JRI2M
kind: problem
title: A finite extension of a finite field is the splitting field of $x^{q^n}-x$ and is Galois
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Finite Fields
  - Galois Theory
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

::: {.problem}
Let $F$ be a field and let $f(x)\in F[x]$.

(a) Define a splitting field of $f(x)$ over $F$.

(b) Let $F$ be a finite field with $q$ elements and let $E/F$ be a finite extension of degree $n>0$. Exhibit an explicit polynomial $g(x)\in F[x]$ whose splitting field over $F$ is $E$.

(c) Show that $E/F$ is Galois.
:::

::: {.solution}

::: pf

::: pf-step

(a) A splitting field of $f$ over $F$ is a field extension $L/F$ such that $f$ splits into linear factors over $L$ and $L$ is generated over $F$ by the roots of $f$.

:::

::: {.pf-step #s2}

(b) Since $|F|=q$ and $[E:F]=n$, the field $E$ has $q^n$ elements. Take
$$
\boxed{g(x)=x^{q^n}-x}\in F[x].
$$
Then $E$ is the splitting field of $g$ over $F$.

::: pf-proof

The group $E^\times$ has order $q^n-1$, so by Lagrange's theorem every $a\in E$ satisfies
$$
a^{q^n}=a,
$$
so every element of $E$ is a root of $g$. The derivative is
$$
g'(x)=q^n x^{q^n-1}-1=-1,
$$
so $g$ has no repeated roots. Since its degree is $q^n$ and $E$ already supplies $q^n$ distinct roots, its roots are exactly the elements of $E$. Therefore $g$ splits over $E$ and its roots generate $E$ over $F$.

:::

:::

::: pf-step

(c) The extension $E/F$ is Galois.

::: pf-proof

By step [](#s2){.pf-ref}, $E$ is the splitting field over $F$ of the separable polynomial $x^{q^n}-x$. A splitting field of a separable polynomial is normal and separable, hence Galois.

Moreover,
$$
\Gal(E/F)=\langle x\mapsto x^q\rangle\cong C_n.
$$

:::

:::

:::

:::
