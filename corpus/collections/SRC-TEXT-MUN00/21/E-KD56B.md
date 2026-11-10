---
schema: qual/card@1
id: E-KD56B
kind: problem
title: First countability of the lower limit topology and the ordered square
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 4, printed p. 134, with the lower
    limit topology of §13 and the ordered square of §16; the stored statement is the printed
    one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.4, PDF p. 24. Explicit countable bases are
    given at every point: half-open intervals of decreasing length in R_l, and in the
    ordered square at the two corners, at points of the interior fibres, and at the two
    kinds of boundary point of a fibre. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Show that $\RR_\ell$ and the ordered square satisfy the first countability axiom.
(This result does not, of course, imply that they are metrizable.)
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.4, PDF p. 24** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the countable bases at each kind of point are theirs.

**$\RR_{\ell}$.** For $x\in\RR_{\ell}$ the countable collection $\{U_{n}\}_{n\in\ZZ_{+}}$ with $U_{n}=[x,x+1/n)$ is a basis at $x$: if $V$ is a neighbourhood of $x$ there is a basis element $[a,b)$ with $x\in[a,b)\subset V$, and then $1/n<b-x$ gives $U_{n}=[x,x+1/n)\subset[a,b)\subset V$.

**The ordered square $I_{o}^{2}$.** At $0\times0$ the sets $U_{n}=[0\times0,\,0\times1/n)$ for $n\in\ZZ_{+}$ form a countable basis; at $1\times1$ the sets $V_{n}=(1\times(1-1/n),\,1\times1]$ do.

For $a\times b$ different from $0\times0$ and $1\times1$:

- if $0<b<1$, put $\delta=\min\{b,1-b\}$; then the sets $\big(a\times(b-\delta/n),\,a\times(b+\delta/n)\big)$ for $n\in\ZZ_{+}$ are a countable basis at $a\times b$;
- if $b=0$ (so $a>0$), the sets $\big((a-a/n)\times0,\ a\times1/n\big)$ for $n\in\ZZ_{+}$ are a countable basis at $a\times0$;
- if $b=1$ (so $a<1$), the sets $\big(a\times(1-1/n),\ ((a+(1-a)/n)\times1\big)$ for $n\in\ZZ_{+}$ are a countable basis at $a\times1$.

In each case the sets are open intervals or half-open intervals of the order topology containing the point, and any basis element $((a',b'),(a'',b''))$ containing it contains one of them: in the first case because the point is not on the boundary fibre and the interval has positive room in both coordinates; in the second because the lower end can be pushed down in the first coordinate and the upper end kept at first coordinate $a$ with a small positive second coordinate; in the third symmetrically.
:::
