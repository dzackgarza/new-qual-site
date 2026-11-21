---
schema: qual/card@1
id: P-CAF05B
kind: problem
title: "Local representation of an analytic function near a zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: that the order of vanishing m is finite, since f is not identically zero on a
    connected disk, and that h extends analytically over DD; the existence of a zero-free disk
    for h from the discreteness of the zero set; and the construction of the holomorphic
    logarithm from a primitive of h'/h, which is what makes g well defined. Not claimed: a
    retained solution set; the provenance names the UGA-style instruction sheet of the
    examination, which carries no solutions.
---

::: {.problem}
Let $f$ be a nonconstant analytic function in $\DD$ with $f(0) = 0$.
Show that there exist a real number $r$, $0 < r \leq 1$, a function $g \in H(B(0; r))$ with $g(0) \neq 0$, and a positive integer $m$, such that $$f(z) = (zg(z))^m, \qquad z \in B(0; r).$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/FA05_220_Complex_Analysis_Qual.pdf`, the examination paper (it opens with the three-hour general instructions), which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $\DD=B(0,1)$, $f$ is nonconstant and analytic on $\DD$ with $f(0)=0$, and $H(\Omega)$ denotes the holomorphic functions on an open set $\Omega$.

::: pf

::: {.pf-step #vanishing-order}
There are $m\ge1$ and $h\in H(\DD)$ with $h(0)\ne0$ and $f(z)=z^mh(z)$ on $\DD$.

::: pf-proof
$f$ is analytic at $0$, so $f(z)=\sum_{k\ge0}a_kz^k$ near $0$ with $a_0=f(0)=0$. Since $f$ is not identically zero and $\DD$ is connected, $f$ has a zero of finite order $m\ge1$ at $0$: $a_k=0$ for $k<m$ and $a_m\ne0$. Then $h(z)=f(z)/z^m=\sum_{k\ge m}a_kz^{k-m}$ is analytic near $0$ with $h(0)=a_m\ne0$, and it extends to an analytic function on $\DD-\theset0$ by the same formula; so $h\in H(\DD)$ with $h(0)\ne0$ and $f=z^mh$.

:::

:::

::: {.pf-step #disk}
There is $r$ with $0<r\le1$ such that $h$ has no zeros in $B(0,r)$.

::: pf-proof
The zero set of a nonzero analytic function has no accumulation point in $\DD$, and $h(0)\ne0$, so there is a disk $B(0,\rho)\subset\DD$ about $0$ free of zeros of $h$; take $r=\min(\rho,1)$.

:::

:::

::: {.pf-step #log}
$h$ has a holomorphic logarithm on $B(0,r)$.

::: pf-proof
$B(0,r)$ is simply connected and $h$ is holomorphic and nowhere zero on it, so $h'/h$ has a primitive $L_0$ there, and $h\exp(-L_0)$ has zero derivative, hence is a nonzero constant $c$; then $L=L_0+\log c$ is a holomorphic logarithm of $h$, for any branch of the logarithm of $c$.

:::

:::

::: {.pf-step #construction}
With $g=\exp(L/m)\in H(B(0,r))$, one has $g(0)\ne0$, $g^m=h$, and $f(z)=(zg(z))^m$ for $z\in B(0,r)$.

::: pf-proof
$g$ is a composite of holomorphic functions, so holomorphic; $\exp$ never vanishes, so $g(0)\ne0$; and $g^m=\exp(L)=h$. Then $(zg(z))^m=z^mg(z)^m=z^mh(z)=f(z)$ on $B(0,r)$, using step [](#vanishing-order){.pf-ref}.

:::

:::

::: {.pf-step #conclusion}
There exist $0<r\le1$, $g\in H(B(0,r))$ with $g(0)\ne0$, and a positive integer $m$ with $f(z)=(zg(z))^m$ on $B(0,r)$.

::: pf-proof
Take $m$ from step [](#vanishing-order){.pf-ref}, $r$ from step [](#disk){.pf-ref} and $g$ from step [](#construction){.pf-ref}.

:::

:::

:::
:::
