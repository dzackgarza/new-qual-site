---
schema: qual/card@1
id: P-ZRVTI
kind: problem
title: Entire univalent functions are affine/linear
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Casorati-Weierstrass
  - Biholomorphisms
  - Singularities
relations: []
review: draft
---

::: {.problem}
Let $f: \CC \rightarrow \CC$ be an injective analytic (also called univalent) function. Show that there exist complex numbers $a \neq 0$ and $b$ such that $f(z)=a z+b$.

> Hint: Apply the Casorati-Weierstrass theorem to $f(1/z)$.
:::

::: {.remark title="Variations"}
The same problem is also asked as: show that $\Aut_\CC(\CC)$ is the group of maps $z\mapsto az+b$ with $a\in\units{\CC}$ and $b\in\CC$. An automorphism is injective and entire, so it is affine by the result above. Each such affine map is an automorphism.
:::

::: {.solution}

$f$ is not constant, because it is injective. Let $g(w)=f(1/w)$ for $w\neq0$.

::: pf

::: {.pf-step #notrem}

$g$ does not have a removable singularity at $0$.

::: pf-proof

Otherwise $g$ is bounded on some $0<\abs{w}<\delta$, so $f$ is bounded on $\abs{z}>1/\delta$. It is also bounded on the compact disk $\abs{z}\le1/\delta$. By Liouville's theorem $f$ is constant, a contradiction.

:::

:::

::: {.pf-step #notess}

$g$ does not have an essential singularity at $0$.

::: pf-proof

By the open mapping theorem, $f(\{\abs{z}<1\})$ is open, so it contains a disk $B$ about $f(0)$. If $0$ were essential, the Casorati–Weierstrass theorem would give $w$ with $0<\abs{w}<1$ and $g(w)\in B$. Then $f(1/w)=f(z')$ for some $\abs{z'}<1$, while $\abs{1/w}>1$, so $1/w\neq z'$. This contradicts injectivity.

:::

:::

::: {.pf-step #poly}

$f$ is a polynomial of degree $N\ge1$.

::: pf-proof

By Steps [](#notrem){.pf-ref} and [](#notess){.pf-ref}, $g$ has a pole at $0$ of some order $N\ge1$. Write $f(z)=\sum_{n\ge0}c_nz^n$. Then $g(w)=\sum_{n\ge0}c_nw^{-n}$ is the Laurent expansion of $g$ at $0$, and since it has only finitely many negative powers, $c_n=0$ for $n>N$ and $c_N\neq0$.

:::

:::

::: {.pf-step #deg1}

$N=1$.

::: pf-proof

The set of critical values $\{f(\zeta):f'(\zeta)=0\}$ is finite, because $f'$ is a nonzero polynomial. Choose $c$ outside it. Every root of $f(z)-c$ is then simple, so the degree-$N$ polynomial $f-c$ has $N$ distinct roots. Injectivity allows at most one, so $N=1$.

:::

:::

::: pf-qed

By Steps [](#poly){.pf-ref} and [](#deg1){.pf-ref}, $f(z)=az+b$ with $a=c_1\neq0$ and $b=c_0$.

:::

:::

:::
