---
schema: qual/card@1
id: P-CAF10C
kind: problem
title: "Uniform limit of injective analytic functions is injective or constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz
  - Univalent Functions
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The prose said "choose disjoint closed disks around a and b" and then applied Hurwitz in a disk around b; the card now takes one disc about b missing a, proves that each g_n is zero-free on its closure (which is where injectivity of f_n is used, f_n(z) = f_n(a) forcing z = a), and states Hurwitz's conclusion in the form used, including why g is not identically zero on the disc (identity theorem on the region G). No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let $G$ be a domain and $\{f_n\}_{n=1}^{\infty}$ a sequence of analytic functions in $G$ that converge to $f$ in $H(G)$.
Assume that each $f_n$ is 1-to-1. Show that $f$ is either constant or 1-to-1.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Assume $f$ is not constant and let $a\ne b$ in $G$; we show $f(a)\ne f(b)$.

::: pf

::: {.pf-step #setup}
Choose $r>0$ with the closed disc $\overline{D(b,r)}$ contained in $G$ and not containing $a$, and put $g_n=f_n-f_n(a)$, $g=f-f(a)$.

::: pf-proof
$G$ is open and $a\ne b$, so a small disc about $b$ of radius $r<\abs{a-b}$ lies in $G$ and its closure misses $a$.
:::

:::

::: {.pf-step #conv}
$g_n\to g$ locally uniformly on $G$.

::: pf-proof
$g_n-g=(f_n-f)-(f_n(a)-f(a))$; the first term tends to $0$ locally uniformly by hypothesis and the second is a sequence of constants tending to $0$ because $f_n(a)\to f(a)$. On a compact set both terms tend to $0$ uniformly.
:::

:::

::: {.pf-step #zerofree}
Each $g_n$ is zero-free on $\overline{D(b,r)}$.

::: pf-proof
$g_n(z)=0$ means $f_n(z)=f_n(a)$; since $f_n$ is injective this forces $z=a$, which is not in $\overline{D(b,r)}$.
:::

:::

::: {.pf-step #hurwitz}
If $f(a)=f(b)$ then $g$ is zero-free on $D(b,r)$.

::: pf-proof
$g(b)=f(b)-f(a)=0$ under the supposition, and $g$ is not identically zero on $D(b,r)$: if it were, then since $D(b,r)$ is a nonempty open subset of the region $G$, the identity theorem would give $g\equiv0$ on $G$, making $f\equiv f(a)$ constant, contrary to hypothesis. Now $g_n\to g$ locally uniformly on the disc $D(b,r)$ by step [](#conv){.pf-ref}, and every $g_n$ is zero-free there by step [](#zerofree){.pf-ref}; Hurwitz's theorem says that a locally uniform limit of zero-free holomorphic functions on a region is either identically zero or zero-free. So $g$ is zero-free on $D(b,r)$.
:::

:::

::: {.pf-step #contradiction}
$f(a)\ne f(b)$.

::: pf-proof
Suppose $f(a)=f(b)$. By step [](#hurwitz){.pf-ref}, $g$ is either identically zero on $D(b,r)$ — excluded — or zero-free there; but $g(b)=0$ with $b\in D(b,r)$. So the supposition is false.
:::

:::

::: {.pf-step}
$f$ is constant or injective.

::: pf-proof
If $f$ is not constant, step [](#contradiction){.pf-ref} applies to arbitrary distinct $a,b\in G$ and gives $f(a)\ne f(b)$, so $f$ is injective.
:::

:::

:::
:::
