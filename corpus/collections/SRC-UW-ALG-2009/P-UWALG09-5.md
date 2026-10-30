---
schema: qual/card@1
id: P-UWALG09-5
kind: problem
title: Baer's criterion for $\ZZ/p\ZZ$ over $\ZZ/n\ZZ$ and for divisible modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Checked against Problem 5 of the UW 2009 algebra qualifying exam.
- event: solution-written
  by: claude-opus-5.5
  date: 2026-10-31
---

::: {.problem}
Let $R$ be a ring and $Q$ an $R$-module.
According to Baer's criterion, $Q$ is injective if and only if for every ideal $I$ of $R$, any $R$-module map $f:I\to Q$ may be extended to an $R$-module map $g:R\to Q$.

(a) Suppose that $p$ is prime and $n$ is a positive integer with $p$ dividing $n$.
Then multiplication makes $\ZZ/p\ZZ$ into a module over the ring $\ZZ/n\ZZ$.
Show that $\ZZ/p\ZZ$ is injective as a $\ZZ/n\ZZ$-module if and only if $p^2$ does not divide $n$.

(b) Prove that if $R$ is a PID, then an $R$-module $Q$ is injective if and only if $rQ=Q$ for every nonzero $r\in R$.
:::

::: {.solution}

Write $\bar a$ for the class of an integer $a$ in $\ZZ/n\ZZ$ or $\ZZ/p\ZZ$.
Every ideal of $\ZZ/n\ZZ$ is principal, of the form $(\bar d)$ with $d\divides n$, and $(\bar d)\cong\ZZ/(n/d)\ZZ$ as a $\ZZ/n\ZZ$-module.
A module map $f:(\bar d)\to\ZZ/p\ZZ$ is therefore determined by $c\coloneqq f(\bar d)$, and any $c$ with $(n/d)c=0$ in $\ZZ/p\ZZ$ defines one.
A module map $g:\ZZ/n\ZZ\to\ZZ/p\ZZ$ is $g(\bar x)=xb$ with $b=g(\bar 1)$, and it extends $f$ exactly when $db=c$ in $\ZZ/p\ZZ$.

::: pf

::: pf-step

(a) If $p^2\notdivides n$, then $\ZZ/p\ZZ$ is an injective $\ZZ/n\ZZ$-module.

::: pf-proof

Let $d\divides n$ and let $f:(\bar d)\to\ZZ/p\ZZ$ have $f(\bar d)=c$.
If $p\notdivides d$, then $d$ is invertible modulo $p$, and $b\coloneqq d^{-1}c$ gives $db=c$.
If $p\divides d$, then $p\notdivides n/d$, because $p^2\notdivides n$. The condition $(n/d)c=0$ in the field $\ZZ/p\ZZ$ then forces $c=0$, and $b\coloneqq0$ gives $db=c$.
In both cases $f$ extends to $\ZZ/n\ZZ$, so Baer's criterion holds.

:::

:::

::: pf-step

(a) If $p^2\divides n$, then $\ZZ/p\ZZ$ is not an injective $\ZZ/n\ZZ$-module.

::: pf-proof

Take $d=p$. Since $p\divides n/p$, the value $c=\bar 1$ satisfies $(n/p)c=0$ in $\ZZ/p\ZZ$, so there is a module map $f:(\bar p)\to\ZZ/p\ZZ$ with $f(\bar p)=\bar 1$.
An extension $g$ would need $pb=\bar1$ in $\ZZ/p\ZZ$, but $pb=0$ for every $b\in\ZZ/p\ZZ$.
Hence $f$ does not extend, and Baer's criterion fails.

:::

:::

::: pf-step

(b) If $R$ is a PID and $Q$ is injective, then $rQ=Q$ for every nonzero $r\in R$.

::: pf-proof

Let $r\neq0$ and $q\in Q$. Since $R$ is a domain, $x\mapsto xr$ is an isomorphism $R\to(r)$, so there is a module map $f:(r)\to Q$ with $f(xr)=xq$.
By Baer's criterion $f$ extends to $g:R\to Q$, and then $q=f(r)=g(r)=r\,g(1)\in rQ$.

:::

:::

::: pf-step

(b) If $R$ is a PID and $rQ=Q$ for every nonzero $r\in R$, then $Q$ is injective.

::: pf-proof

Every ideal of $R$ is $(r)$ for some $r\in R$. If $r=0$, the only module map $(0)\to Q$ is zero, and $g=0$ extends it.
If $r\neq0$, a module map $f:(r)\to Q$ is determined by $q\coloneqq f(r)$. Choose $q'\in Q$ with $rq'=q$ and set $g(x)\coloneqq xq'$.
Then $g$ is a module map $R\to Q$ with $g(xr)=xrq'=xq=f(xr)$, so $g$ extends $f$.
Baer's criterion holds, so $Q$ is injective.

:::

:::

:::

:::
