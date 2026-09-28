---
schema: qual/card@1
id: P-V2OBF
kind: problem
title: The sets $|z-\alpha|+|z+\alpha|=k$ and $|z-\alpha|+|z+\alpha|\leq k$ for $2|\alpha|<k$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Describe each set in the $z$-plane in (a) and (b) below, where $\alpha$ is a complex number and $k$ is a positive number such that $2|\alpha|<k$.

(a) $|z-\alpha|+|z+\alpha|=k$;

(b) $|z-\alpha|+|z+\alpha| \leq k$.
:::

::: {.solution}
The two fixed points $\alpha$ and $-\alpha$ are the foci. Thus part (a) is an
ellipse, because the sum of the distances from $z$ to the two foci is the
constant $k>2|\alpha|$.

Its center is $0$. The major semiaxis is
\[
a=\frac{k}{2},
\]
the focal distance is
\[
c=|\alpha|,
\]
and therefore the minor semiaxis is
\[
b=\sqrt{a^2-c^2}
=\frac12\sqrt{k^2-4|\alpha|^2}.
\]
The major axis lies on the line through $\pm\alpha$.

If we rotate coordinates so that $\alpha=|\alpha|>0$ and write
$z=x+iy$, the equation is
\[
\boxed{
\frac{x^2}{(k/2)^2}
+\frac{y^2}{(k^2/4-|\alpha|^2)}=1.}
\]

Part (b) is the closed filled ellipse bounded by this curve, since it consists
of the points for which the same sum of focal distances is at most $k$.
:::
