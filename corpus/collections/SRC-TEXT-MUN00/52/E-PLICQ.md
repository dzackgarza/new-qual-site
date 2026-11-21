---
schema: qual/card@1
id: E-PLICQ
kind: problem
title: Abelian fundamental groups and base-point independence
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 3 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-3-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-3-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 3, printed p. 335. dbFin proves both directions by multiplying on the left and right by the classes of alpha and beta; the card routes the same proof through the inner automorphism beta-hat inverse times alpha-hat, which is correct under Munkres's convention that alpha-hat maps the group at x_0 to the group at x_1 by f goes to alpha-bar star f star alpha. Nothing needed repair.
---

::: {.exercise}

Let $x_0$ and $x_1$ be points of the path-connected space $X$.
Show that $\pi_1(X, x_0)$ is abelian if and only if for every pair $\alpha$ and $\beta$ of paths from $x_0$ to $x_1$, we have $\hat{\alpha} = \hat{\beta}$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows. For a path $\alpha$ from $x_{0}$ to $x_{1}$ the induced isomorphism $\hat\alpha:\pi_{1}(X,x_{1})\to\pi_{1}(X,x_{0})$ is $\hat\alpha([f])=[\alpha*f*\bar\alpha]$, and $\bar\alpha$ denotes the reverse path.

::: pf

::: {.pf-step #conjugation}
For paths $\alpha,\beta$ from $x_{0}$ to $x_{1}$ and a loop $f$ at $x_{0}$, with $\lambda=\alpha*\bar\beta$ one has
$$\hat\beta^{-1}\hat\alpha([f])=[\lambda^{-1}*f*\lambda].$$

::: pf-proof
$\hat\alpha([f])=[\alpha*f*\bar\alpha]$, so $\hat\beta^{-1}\hat\alpha([f])=\big[\bar\beta*(\alpha*f*\bar\alpha)*\beta\big]=[\bar\beta\alpha*f*\bar\alpha\beta]$ by associativity of path products up to homotopy. The loop $\lambda=\alpha*\bar\beta$ has reverse $\lambda^{-1}=\beta*\bar\alpha$, so $\lambda^{-1}*f*\lambda=\beta\bar\alpha*f*\alpha\bar\beta$, which is the same class. Hence $\hat\beta^{-1}\hat\alpha([f])=[\lambda^{-1}*f*\lambda]$, the automorphism of $\pi_{1}(X,x_{0})$ given by conjugation by $[\lambda^{-1}]$.
:::

:::

::: {.pf-step #forward}
If $\pi_{1}(X,x_{0})$ is abelian, then $\hat\alpha=\hat\beta$ for all paths $\alpha,\beta$ from $x_{0}$ to $x_{1}$.

::: pf-proof
In an abelian group every inner automorphism is the identity, so $[\lambda^{-1}*f*\lambda]=[f]$ for every $f$, and step [](#conjugation){.pf-ref} gives $\hat\beta^{-1}\hat\alpha=\mathrm{id}$, that is $\hat\alpha=\hat\beta$.
:::

:::

::: {.pf-step #backward}
If $\hat\alpha=\hat\beta$ for all such $\alpha,\beta$, then $\pi_{1}(X,x_{0})$ is abelian.

::: pf-proof
Fix a path $\beta$ from $x_{0}$ to $x_{1}$; such a path exists because $X$ is path connected. Given a loop $\mu$ at $x_{0}$, put $\alpha=\mu*\beta$, a path from $x_{0}$ to $x_{1}$. By hypothesis $\hat\alpha=\hat\beta$, so $\hat\beta^{-1}\hat\alpha=\mathrm{id}$, and with $\lambda=\alpha*\bar\beta$ step [](#conjugation){.pf-ref} says that conjugation by $[\lambda^{-1}]$ is the identity on $\pi_{1}(X,x_{0})$; note $[\lambda]=[\mu]$ since $\lambda=\mu*\beta*\bar\beta$ is homotopic to $\mu$. So every $[\mu]\in\pi_{1}(X,x_{0})$ is central, which is exactly that the group is abelian.
:::

:::

::: {.pf-qed}
The two implications are steps [](#forward){.pf-ref} and [](#backward){.pf-ref}, so $\pi_{1}(X,x_{0})$ is abelian exactly when $\hat\alpha=\hat\beta$ for every pair of paths from $x_{0}$ to $x_{1}$.
:::

:::

:::
