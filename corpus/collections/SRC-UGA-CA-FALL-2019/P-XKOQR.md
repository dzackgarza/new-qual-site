---
schema: qual/card@1
id: P-XKOQR
kind: problem
title: A holomorphic map is a local bijection iff $f'\neq 0$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Open Mapping Theorem
  - Argument Principle
  - Rouché
relations: []
review: draft
---

::: {.problem}
A holomorphic mapping $f: U \rightarrow V$ is a local bijection on $U$ if for every $z \in U$ there exists an open disc $D \subset U$ centered at $z$ so that $f: D \rightarrow f(D)$ is a bijection.
Prove that a holomorphic map $f: U \rightarrow V$ is a local bijection if and only if $f^{\prime}(z) \neq 0$ for all $z \in U$.
:::

::: {.concept}
\envlist

- Inverse function theorem: if $F\in C^1(\RR^n\to \RR^n)$ and $D_f$ is invertible at $p$, then $F$ is invertible in a neighborhood of $p$, and $\inverseof{F}$ is $C^1$.

:::

::: {.solution}

::: pf

::: {.pf-step #if}

If $f'(z_0)\neq0$, then $f$ is a bijection from some open disc centered at $z_0$ onto its image.

::: pf-proof

Write $f=u+iv$. By the Cauchy–Riemann equations the real Jacobian of $f$ at $z_0$ is $u_xv_y-u_yv_x=u_x^2+v_x^2=\abs{f'(z_0)}^2>0$. The map $f$ is $C^1$ as a map of $\RR^2$, so the inverse function theorem gives an open neighborhood $N$ of $z_0$ on which $f$ is injective. Any open disc $D\subset N$ centered at $z_0$ works.

:::

:::

::: {.pf-step #onlyif}

If $f'(z_0)=0$, then $f$ is not injective on any open disc $D\subset U$ centered at $z_0$.

::: pf-proof

If $f$ is constant on $D$, it is not injective there. Otherwise $f$ is nonconstant on the connected set $D$, so $h=f-f(z_0)$ has a zero of some finite order $k$ at $z_0$, and $k\ge2$ because $h'(z_0)=0$. The zeros of $h$ and of $f'$ in $D$ are isolated, so there is $r>0$ with $\abs{z-z_0}\le r$ contained in $D$ and $h(z)\neq0$, $f'(z)\neq0$ for $0<\abs{z-z_0}\le r$. Let $m=\min_{\abs{z-z_0}=r}\abs{h(z)}>0$ and fix $p$ with $0<\abs{p-f(z_0)}<m$. On $\abs{z-z_0}=r$, $\abs{p-f(z_0)}<\abs{h(z)}$, so by Rouché's theorem $f-p=h-(p-f(z_0))$ has $k$ zeros, counted with multiplicity, in $\abs{z-z_0}<r$. None of them is $z_0$, because $f(z_0)\neq p$, so $f'$ does not vanish at any of them, and each is simple. Hence $f$ takes the value $p$ at $k\ge2$ distinct points of $D$.

:::

:::

::: pf-qed

Step [](#if){.pf-ref} proves that $f'\neq0$ on $U$ implies that $f$ is a local bijection, and Step [](#onlyif){.pf-ref} proves the converse.

:::

:::

:::
