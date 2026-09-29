---
schema: qual/card@1
id: P-EUIAS
kind: problem
title: von Neumann's mean ergodic theorem for a unitary operator
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $U$ be a unitary operator on $H$ a Hilbert space, let $M \da \ts{x\in H \st Ux = x}$, let $P$ be the orthogonal projection onto $M$, and define
\[
S_N \da {1\over N} \sum_{n=0}^{N-1} U^n
.\]
Show that for all $x\in H$,
\[
\norm{ S_N x - Px}_H \converges{N\to \infty } \to 0
.\]
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

$M = \ker(U - I)$ is a closed subspace, and $M^\perp = \overline{\operatorname{ran}(U - I)}$.

::: pf-proof

$M$ is the kernel of the bounded operator $U - I$, hence a closed subspace. For a bounded operator $T$, $(\operatorname{ran} T^*)^\perp = \ker T$, so $(\ker T)^\perp = \overline{\operatorname{ran} T^*}$. Take $T = U - I$. Then $T^* = U^{-1} - I = -U^{-1}(U - I)$, so $\operatorname{ran}T^* = U^{-1}\operatorname{ran}(U - I)$. Since $U^{-1}(Uy - y) = Uz - z$ with $z = U^{-1}y$, and $Uy - y = U^{-1}(Uw - w)$ with $w = Uy$, $U^{-1}\operatorname{ran}(U - I) = \operatorname{ran}(U - I)$.

:::

:::

::: {.pf-step #s2}

$S_N x = x$ for $x \in M$ and every $N$.

::: pf-proof

$U^n x = x$ for all $n$.

:::

:::

::: {.pf-step #s3}

$\|S_N\| \le 1$, and $\|S_N x\| \to 0$ for $x \in \operatorname{ran}(U - I)$.

::: pf-proof

$\|U^n\| = 1$, so $\|S_N\| \le \frac1N\sum_{n<N}\|U^n\| = 1$. For $x = Uy - y$, the sum telescopes: $S_N x = \frac{1}{N}\sum_{n=0}^{N-1}(U^{n+1}y - U^ny) = \frac{1}{N}(U^N y - y)$, so $\|S_N x\| \le \frac{2\|y\|}{N}$.

:::

:::

::: {.pf-step #s4}

$\|S_N x\| \to 0$ for $x \in M^\perp$.

::: pf-proof

Given $\eps > 0$, step [](#s1){.pf-ref} gives $z \in \operatorname{ran}(U - I)$ with $\|x - z\| < \eps/2$. By step [](#s3){.pf-ref}, $\|S_N x\| \le \|S_N (x - z)\| + \|S_N z\| < \eps/2 + \|S_N z\| < \eps$ for $N$ large.

:::

:::

::: pf-qed

Write $x = Px + (x - Px)$ with $Px \in M$ and $x - Px \in M^\perp$. By step [](#s2){.pf-ref}, $S_N x - Px = S_N(x - Px)$, which tends to $0$ by step [](#s4){.pf-ref}.

:::

:::

:::
