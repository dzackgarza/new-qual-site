---
schema: qual/card@1
id: P-HCAX10
kind: problem
title: A compact-uniform limit of univalent functions can be constant
classification:
  areas:
  - complex-analysis
  topics:
  - Univalent Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The prose said "choose a closed disk that does not contain b and whose boundary contains no zero of g" without saying why such a disk exists (the zeros of g are isolated, and g is not identically zero on the disc since it is not identically zero on the region), and it applied Hurwitz without stating which version. The card now derives g not identically zero from nonconstancy of f, records the existence of the disk, and states Hurwitz's conclusion in the form used (zeros of the limit are limits of zeros of the approximants). The example and the two directions of the "only possible failure" are separate steps. No retained solution set covers the question; the card says the argument is its own.
---

::: {.problem}
Give a sequence of holomorphic injective functions which converges uniformly on compact sets to a non-injective function.
Show that this example describes the only possible failure of injectivity in such a limit.
:::

::: {.solution}
The collection's provenance is the oral-question extraction, which holds the question and no worked answer, so no retained solution set covers it; the argument is the card's own.

::: pf

::: {.pf-step #example}
On a domain $\Omega$, $f_n(z)=z/n$ is holomorphic and injective for every $n\ge1$, and $f_n\to0$ uniformly on compact subsets of $\Omega$.

::: pf-proof
$z\mapsto z/n$ is holomorphic with derivative $1/n\ne0$, hence injective. On a compact $K\subseteq\Omega$ with $M=\max_K\abs z$, one has $\abs{f_n(z)-0}\le M/n\to0$ uniformly. The limit $0$ is constant, hence not injective.
:::

:::

::: {.pf-step #hurwitz}
If $f_n:\Omega\to\CC$ are holomorphic and injective, $f_n\to f$ uniformly on compact sets, $f$ is not constant, and $f(a)=f(b)$ with $a\ne b$, then all sufficiently large $f_n$ take the same value at two distinct points.

::: pf-proof
Fix $a\ne b$ with $f(a)=f(b)$, put $g_n=f_n-f_n(b)$ and $g=f-f(b)$; then $g_n\to g$ uniformly on compact sets because $f_n(b)\to f(b)$, and $g(a)=f(a)-f(b)=0$. The function $g$ is not identically zero: if $g\equiv0$ on the region $\Omega$ then $f\equiv f(b)$ is constant. Its zeros are isolated, so choose $r>0$ with $\overline{D(a,r)}\subseteq\Omega$, $b\notin\overline{D(a,r)}$ and no zero of $g$ on the circle $\abs{z-a}=r$. On the disc $D(a,r)$, which is a region on which $g$ is not identically zero, Hurwitz's theorem gives: for all large $n$, $g_n$ has at least one zero $a_n$ in $D(a,r)$, since $g$ has one there. Then $f_n(a_n)=f_n(b)$ with $a_n\in D(a,r)$ and $b\notin\overline{D(a,r)}$, so $a_n\ne b$ and $f_n$ is not injective.
:::

:::

::: {.pf-step #only}
A compact-uniform limit of holomorphic injective functions on $\Omega$ is either injective or constant.

::: pf-proof
Let $f$ be such a limit. If $f$ is not constant and $f(a)=f(b)$ for some $a\ne b$, step [](#hurwitz){.pf-ref} contradicts injectivity of $f_n$ for large $n$. So a nonconstant limit is injective, and the failure of injectivity therefore occurs only when the limit is constant; step [](#example){.pf-ref} shows that this case does occur.
:::

:::

:::
:::
