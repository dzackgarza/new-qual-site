---
schema: qual/card@1
id: P-CASP21D
kind: problem
title: 'A bound on $\abs{f(0)}$ for a holomorphic function vanishing at four points of $B(0,2)$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Products
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: F(w) = f(2w) maps
    the disc into itself with zeros at the four half-points; the Blaschke extraction is
    justified by Schwarz-Pick (a holomorphic self-map of the disc vanishing at a, divided by
    phi_a, is again a self-map), applied four times; and |F(0)| = |H(0)| prod |a| <= (1/2)^4
    = 1/16 < 1/15. The prose said only that "successively applying the Schwarz lemma gives"
    the factorisation; the extraction step and its justification are now separate. The
    stronger constant 1/16 was already the card's claim and is confirmed. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Let $f : G \to \CC$ be a holomorphic function in $G = \{z : \abs{z} < 2\}$ such that $\abs{f(z)} < 1$ for $z \in G$.
Assume that $f(1) = f(-1) = f(i) = f(-i) = 0$.
Show that $\abs{f(0)} \leq \frac{1}{15}$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
For $a\in\DD$ write $\phi_a(w)\coloneqq\frac{w-a}{1-\bar aw}$.

::: pf

::: {.pf-step #lemma}
If $g:\DD\to\DD$ is holomorphic and $g(a)=0$ for some $a\in\DD$, then $g/\phi_a$ extends to a holomorphic map $\DD\to\overline{\DD}$.

::: pf-proof
Since $g(a)=0$, the quotient $g(w)/(w-a)$ extends holomorphically across $a$, so $h\coloneqq g/\phi_a=g(w)\frac{1-\bar aw}{w-a}$ is holomorphic on $\DD$. For $w\ne a$, Schwarz--Pick applied to $g$ at the points $w$ and $a$ gives $\abs{g(w)}\le\abs{\phi_a(w)}$, because $\abs{(g(w)-g(a))/(1-\overline{g(a)}g(w))}=\abs{g(w)}$ and $\abs{(w-a)/(1-\bar aw)}=\abs{\phi_a(w)}$; hence $\abs{h(w)}\le1$ there, and by continuity at $a$.
:::

:::

::: {.pf-step #scaling}
$F(w)\coloneqq f(2w)$ is holomorphic on $\DD$, maps $\DD$ into $\DD$, and vanishes at $\frac12,-\frac12,\frac i2,-\frac i2$.

::: pf-proof
For $\abs{w}<1$ one has $\abs{2w}<2$, so $2w\in G$ and $\abs{F(w)}=\abs{f(2w)}<1$; $F$ is holomorphic as a composition. Its zeros are the preimages under $w\mapsto2w$ of $\pm1$ and $\pm i$, namely $\pm\frac12$ and $\pm\frac i2$, and these are distinct points of $\DD$.
:::

:::

::: {.pf-step #factorisation}
There is a holomorphic $H:\DD\to\overline{\DD}$ with
$$
F(w)=H(w)\prod_{a\in\left\{\frac12,-\frac12,\frac i2,-\frac i2\right\}}\phi_a(w).
$$

::: pf-proof
Apply step [](#lemma){.pf-ref} four times: $F_0\coloneqq F$ vanishes at $a_1=\frac12$, so $F_1\coloneqq F_0/\phi_{a_1}$ is holomorphic $\DD\to\overline{\DD}$, and it vanishes at $a_2=-\frac12$ because $\phi_{a_1}$ does not vanish there; continuing through $a_2,a_3=\frac i2,a_4=-\frac i2$ gives $H\coloneqq F_4$ with the stated factorisation, the factors being nowhere-zero on $\DD$ except at their own zeros.
:::

:::

::: {.pf-step #value}
$\abs{f(0)}=\abs{F(0)}\le\left(\frac12\right)^4=\frac{1}{16}$.

::: pf-proof
Evaluating the factorisation of step [](#factorisation){.pf-ref} at $0$: $\phi_a(0)=-a$, so $\abs{\phi_a(0)}=\abs{a}=\frac12$ for each of the four factors, and $\abs{H(0)}\le1$ since $H$ maps into $\overline{\DD}$. Hence $\abs{F(0)}\le\left(\frac12\right)^4$, and $F(0)=f(0)$.
:::

:::

::: {.pf-step}
$\abs{f(0)}\le\frac{1}{15}$, indeed $\abs{f(0)}\le\frac{1}{16}$.

::: pf-proof
Step [](#value){.pf-ref} gives $\abs{f(0)}\le\frac1{16}$, and $\frac1{16}<\frac1{15}$ since $15<16$; so the requested bound holds, with the stronger constant $\frac1{16}$.
:::

:::

:::
:::
