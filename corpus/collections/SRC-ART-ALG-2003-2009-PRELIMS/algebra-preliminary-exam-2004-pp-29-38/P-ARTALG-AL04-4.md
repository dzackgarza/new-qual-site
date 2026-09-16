---
schema: qual/card@1
id: P-ARTALG-AL04-4
kind: problem
title: Normality at the smallest prime index
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the order, least-prime condition, and index hypothesis with 2004 Groups 4 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the coset action without presupposing normality, both image-order divisibilities, and the final equality of the subgroup with the action kernel."
---

::: {.problem}
Let $G$ be a group and let $p$ be the smallest prime divisor of $|G|$.
Suppose that $H$ is a subgroup of $G$ of index $p$.
Prove that $H$ is normal.
:::

::: {.solution}
<1>1. The action on left cosets gives a homomorphism
$\rho:G\to S_p$ whose kernel $K$ is contained in $H$.

::: {.proof}
There are exactly $p$ left cosets of $H$. Left multiplication
$g\cdot(xH)=(gx)H$ is well defined and permutes these cosets.
Composition agrees with multiplication in $G$, giving $\rho$.
The action is transitive, since $yx^{-1}$ sends $xH$ to $yH$.
Any element of the kernel fixes the coset $H$, hence belongs to
its stabilizer, which is exactly $H$. Thus $K\subseteq H$.
This construction uses cosets as a set, not a quotient group.
:::

<1>2. The image of $\rho$ has order exactly $p$.

::: {.proof}
Let $m=|\rho(G)|$. The first isomorphism theorem and Lagrange's
theorem give $m\mid |G|$ and $m\mid p!$ [@DF04].
Every prime dividing $m$ must therefore be at least $p$, by
minimality of $p$, and at most $p$, since it divides $p!$.
Thus $p$ is its only possible prime divisor. The exponent of
$p$ in $p!$ is one, so $m=1$ or $m=p$.
Transitivity and orbit-stabilizer give $p\mid m$, hence $m=p$.
:::

<1>3. The subgroup $H$ equals $K$ and is normal.

::: {.proof}
The index of $K$ is $[G:K]=|\rho(G)|=p$. Since $K\subseteq H$,
index multiplication gives
$$
p=[G:K]=[G:H][H:K]=p[H:K].
$$
Therefore $[H:K]=1$ and $H=K$. A homomorphism kernel is normal,
so $H\lhd G$.
:::
:::
