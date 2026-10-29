---
schema: qual/card@1
id: E-EYILL
kind: problem
title: No fixed points implies homotopic to antipodal
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Points
  - Homotopy
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source printed "Show that if f has no fixed points iff deg f = (-1)^{n+1} and f is homotopic to the antipodal map"; the converse is false (a reflection of S^2 has degree -1 and fixed points), so the statement asks for the forward implication.
---

::: {.exercise}
Show that if $f: S^n\to S^n$ has no fixed points, then $f$ is homotopic to the antipodal map and $\deg f = (-1)^{n+1}$.
:::

::: {.hint}
If $f(x)\neq x$, the line segment from $f(x)$ to $-x$ does not contain $0$.
:::

::: {.solution}
Let $a(x)=-x$ be the antipodal map, and regard $S^n\subseteq\RR^{n+1}$.

::: pf

::: {.pf-step #nonzero}

For $t\in[0,1]$ and $x\in S^n$, the point $H(t,x)=(1-t)f(x)-tx$ is nonzero.

::: pf-proof

Suppose $(1-t)f(x)=tx$. Taking norms gives $1-t=t$, so $t=1/2$ and then $f(x)=x$, which contradicts the hypothesis.

:::

:::

::: {.pf-step #homotopy}

$f\homotopic a$.

::: pf-proof

By step [](#nonzero){.pf-ref}, $G(t,x)=H(t,x)/\norm{H(t,x)}$ is a continuous map $[0,1]\times S^n\to S^n$ with $G(0,\wait)=f$ and $G(1,\wait)=a$.

:::

:::

::: pf-qed

Degree is a homotopy invariant, so step [](#homotopy){.pf-ref} gives $\deg f=\deg a$. The antipodal map is the composite of $n+1$ reflections, each of degree $-1$, so $\deg f=(-1)^{n+1}$.

:::

:::

:::
