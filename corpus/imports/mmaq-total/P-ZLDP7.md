---
schema: qual/card@1
id: P-ZLDP7
kind: problem
title: State Rouche's theorem.
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
relations: []
review: draft
---

::: problem
1.  State Rouche's theorem.

2.  Let $f$ be analytic in a neighborhood of $0$, and satisfying
    $f'(0) \neq 0$. Use Rouche's theorem to show that there exists a
    neighborhood $U$ of $0$ such that $f$ is a bijection in $U$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) State Rouch\'e's theorem; (2) use it to show that if $f$ is analytic near $0$ with $f'(0) \neq 0$, then $f$ is a bijection on some neighborhood of $0$.

<1>1. Statement of Rouch\'e's theorem.
    Proof: Let $\gamma$ be a simple closed contour, and let $f, g$ be analytic on and inside $\gamma$ with $\abs{f(z)} < \abs{g(z)}$ for all $z \in \gamma$. Then $f$ and $f + g$ have the same number of zeros (counting multiplicity) inside $\gamma$.

<1>2. Setup for (2): write $f(z) - f(0) = f'(0)z + z^2 h(z)$ near $0$, where $h$ is analytic.
    Proof: Taylor expansion of the analytic $f$ around $0$ up to first order with remainder $z^2 h(z)$, valid on a disk contained in the domain.

<1>3. Choose $\rho > 0$ so that $\abs{f'(0) z} > \abs{z^2 h(z)}$ on $\abs{z} = \rho$.
    Proof: On $\abs{z} = \rho$, $\abs{f'(0)z} = \abs{f'(0)}\rho$ and $\abs{z^2 h(z)} \le \rho^2 \max_{\abs{z} = \rho}\abs{h(z)}$. Since $\abs{f'(0)} > 0$ and $h$ is bounded on the compact circle, $\abs{f'(0)} > \rho\max_{\abs{z}=\rho}\abs{h(z)}$ for all sufficiently small $\rho$; pick such a $\rho > 0$.

<1>4. $f(z) - f(0)$ and $f'(0)z$ have the same number of zeros in $\abs{z} < \rho$.
    Proof: Rouch\'e's theorem (<1>1) on $\abs{z} = \rho$, applied to the pair $f'(0)z$ and $z^2h(z)$, using the strict inequality from <1>3. The function $f'(0)z$ has exactly one zero (at $0$, simple), so $g(z) := f(z) - f(0)$ has exactly one zero in $\abs{z} < \rho$; since $g(0) = 0$, that zero is $z = 0$ and it is simple.

<1>5. $g$ is injective on $\abs{z} < \rho$ (after possibly shrinking $\rho$).
    Proof: Fix a small $w$ with $\abs{w} < \abs{f'(0)}\rho/2$ (also require $\abs{w}$ small enough that $\abs{f'(0)z - w} \ge \abs{f'(0)}\rho - \abs{w} > \rho^2\max\abs{h}$ on $\abs{z} = \rho$; this holds for $\abs{w} < \abs{f'(0)}\rho/2$ once <1>3 holds with room). On $\abs{z} = \rho$, $\abs{g(z) - w - (f'(0)z - w)} = \abs{z^2 h(z)} < \abs{f'(0)z - w}$, so Rouch\'e applies to $g(z) - w$ and $f'(0)z - w$: both have the same number of zeros in $\abs{z} < \rho$. The latter is linear with one zero, so $g(z) = w$ has exactly one solution in the disk. Since $g(0) = 0$, every $z_1 \neq z_2$ in the disk with $g(z_1) = g(z_2) = w \neq 0$ would give two solutions of $g(z) = w$ — impossible; and $w = 0$ has only the solution $z = 0$ by <1>4. Hence $g$ is injective on the disk.

<1>6. $f$ is a bijection on a neighborhood of $0$.
    Proof: $f = g + f(0)$, so <1>5 gives that $f$ is injective on $\abs{z} < \rho$. By the open mapping theorem (or <1>5 applied to every $w$ in a neighborhood of $f(0)$), the image $f(\abs{z} < \rho)$ is open, so $f$ maps a neighborhood of $0$ bijectively onto a neighborhood of $f(0)$.

<1>7. Q.E.D.
    Proof: <1>1 states the theorem; <1>2–<1>6 prove the local bijectivity.

:::
