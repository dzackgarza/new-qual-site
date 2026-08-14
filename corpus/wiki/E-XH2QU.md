---
schema: qual/card@1
id: E-XH2QU
kind: exercise
title: "Show that $R[x]$ a PID $\\iff R$ is a field."
classification:
  areas:
  - algebra
  topics:
  - principal-ideal-domains
  - polynomials
  - fields
relations: []
review: draft
---

::: {.exercise title="?"}
Show that $R[x]$ a PID $\iff R$ is a field.
:::

::: {.solution}
Hint: take $r\in R$, then $\gens{r, x} = \gens{f}$ for some $f$.
Write $r = fp$ and $x = fq$ for $p, q\in R[x]$, show $\deg f = 0$ and $\deg q = 1$.
Write $f = c$ a constant, $q(x) = ax + b$ to get $c(ax+b)=x \implies ca=1 \implies c\in R\units \implies \gens{f} = R[x]$.
Conclude by writing $1= ar_1(x) + xr_2(x)$, evaluate at $x=0$ to get $a\inv = r_1(0)$.
:::
