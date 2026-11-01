---
schema: qual/card@1
id: E-HAT-4.1-1
kind: problem
title: "Alternative sum of maps and abelian $\\pi_n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct. The interchange law is checked region by region: with `+` using the
    first coordinate and `+'` the second, the two composites `(f+g)+'(h+k)` and `(f+'h)+(g+'k)` put
    `f, g, h, k` on the same four half-size sub-cubes of `I^n` and send the same separating faces to
    `x_0`, so the maps agree on the nose, not merely up to homotopy. The two deductions are right and
    use the constant map as a two-sided identity up to homotopy relative to the boundary: with
    `g = h = 0` the interchange law gives `f +' k ~ f + k` in `pi_n`, and with `f = k = 0` it gives
    `g +' h ~ h + g`, which combined with the agreement of the two sums gives
    `[g] + [h] = [g] +' [h] = [h] + [g]`. The dimension restriction `n >= 2` is exactly what makes two
    coordinates available. No correction was needed.
review: draft
---

::: {.problem}
Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.
:::

::: {.solution}
Let $n\ge2$ and use the first coordinate for $+$ and the second for $+'$. Dividing the first two coordinates into four half-size squares shows directly, on each square, that
$$
(f+g)+'(h+k)=(f+'h)+(g+'k).
$$
Both sides use $f,g,h,k$ on the same four regions and send their separating faces to $x_0$.

Let $0$ be the constant map. It is a two-sided identity for either sum up to homotopy relative to $\partial I^n$, by shrinking the half-cube on which the constant map is used. Put $g=h=0$ in the interchange equality. Its left side is homotopic to $f+'k$, and its right side is homotopic to $f+k$. Hence the two sums agree on $\pi_n(X,x_0)$.

Now put $f=k=0$. The left side is homotopic to $g+'h$, while the right side is homotopic to $h+g$. Since the two sums agree on homotopy classes, $[g]+[h]=[h]+[g]$. Thus $\pi_n(X,x_0)$ is abelian for $n\ge2$.
:::
