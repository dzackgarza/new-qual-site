---
schema: qual/card@1
id: P-KPDL7
kind: problem
title: "Show that for every map $f: S^2 \\to S^1$, there is a point $x\\in S^2$ such that $f(x) = f(-x)$.\u2026"
classification:
  areas:
  - topology
  topics:
  - fixed-points
  - covering-spaces
  - fundamental-group
relations: []
review: draft
---

Show that for every map $f: S^2 \to S^1$, there is a point $x\in S^2$ such that $f(x) = f(-x)$.

::: {.solution}
Suppose towards a contradiction that $f$ does not possess this property, so there is no $x\in S^2$ such that $f(x) = f(-x)$.

Then define $g: S^2 \into S^1$ by $g(x) = {f(x) - f(-x)}$; by assumption, this is a nontrivial map, i.e. $g(x) \neq 0$ for *any* $x\in S^2$.

In particular, $-g(-x) = -{(f(-x) - f(x))} = {f(x) - f(-x)} = g(x)$, so $-g(x) = g(-x)$ and thus $g$ commutes with the antipodal map $\alpha: S^2 \to S^2$.

This means $g$ is constant on the fibers of the quotient map $p: S^2 \into \RP 2$, and thus descends to a well defined map $\tilde g: \RP 2 \into S^1$, and since $S^1 \cong \RP 1$, we can identify this with a map $\tilde g: \RP 2 \into \RP 1$ which thus induces a homomorphism $\tilde g_*: \pi_1(\RP 2) \to \pi_1(\RP 1)$.

Since $g$ was nontrivial, $\tilde g$ is nontrivial, and by functoriality of $\pi_1$, $\tilde g_*$ is nontrivial.

But $\pi_1(\RP 2) = \ZZ_2$ and $\pi_1(\RP 1) = \ZZ$, and $\tilde g_*: \ZZ^2 \into \ZZ$ can only be the trivial homomorphism - a contradiction.
:::
