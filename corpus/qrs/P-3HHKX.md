---
schema: qual/card@1
id: P-3HHKX
kind: problem
title: "Prove the following inequality, and explain when equality\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - geometry
relations: []
review: draft
---

::: problem
Prove the following inequality, and explain when equality holds:
\[
\abs{z+w} \geq \abs{ \abs{z} - \abs{w} }
.\]
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove $\abs{z + w} \ge \abs{\abs{z} - \abs{w}}$ and explain when equality holds.

<1>1. $\abs{z} \le \abs{z + w} + \abs{w}$.
    Proof: Triangle inequality applied to $z = (z + w) + (-w)$: $\abs{z} \le \abs{z + w} + \abs{-w} = \abs{z+w} + \abs{w}$, hence $\abs{z} - \abs{w} \le \abs{z + w}$.

<1>2. $\abs{w} \le \abs{z + w} + \abs{z}$.
    Proof: Same argument with roles swapped: $\abs{w} \le \abs{z + w} + \abs{z}$, hence $\abs{w} - \abs{z} \le \abs{z + w}$.

<1>3. $\abs{\abs{z} - \abs{w}} \le \abs{z + w}$.
    Proof: $\abs{\abs{z} - \abs{w}} = \max(\abs{z} - \abs{w}, \abs{w} - \abs{z}) \le \abs{z + w}$ by <1>1 and <1>2.

<1>4. Equality characterization.
    Proof: Equality holds iff $\abs{z} - \abs{w} = \abs{z+w}$ with $\abs{z} \ge \abs{w}$ (or the symmetric case). By the equality case of the triangle inequality, $\abs{z + w} = \abs{z} + \abs{w}$ iff $z$ and $w$ are nonnegative real multiples of each other. Here $z = (z+w) + (-w)$: equality in <1>1 requires $z + w$ and $-w$ to be nonnegatively aligned, i.e. $z + w = \lambda(-w)$ with $\lambda \ge 0$, i.e. $z = -(\lambda + 1)w$, i.e. $z/w \le 0$ (real, nonpositive). Symmetrically for <1>2. Conclusion: equality holds iff $z$ and $w$ are collinear with opposite directions: $z/w \in (-\infty, 0]$, i.e. $\arg z = \arg w + \pi \pmod{2\pi}$ (or one of them is $0$).

<1>5. Q.E.D.
    Proof: <1>3 proves the inequality; <1>4 characterizes equality.

:::
